"""Google Docs API client wrapper."""

import os
from googleapiclient.errors import HttpError
from .auth import get_service, get_drive_service


class GDocsClient:
    """Wrapper for Google Docs API operations."""

    def __init__(self, service=None, drive_service=None, credentials_path=None):
        self.service = service or get_service(credentials_path)
        self.drive_service = drive_service or get_drive_service(credentials_path)

    def read_document(self, document_id: str, include_tabs: bool = True) -> dict:
        """Fetch full document structure. Returns raw API response.

        Args:
            document_id: Google Docs document ID
            include_tabs: If True, includes content from all tabs (requires includeTabsContent)
        """
        kwargs = {'documentId': document_id}
        if include_tabs:
            kwargs['includeTabsContent'] = True
        return self.service.documents().get(**kwargs).execute()

    def read_as_text(self, document_id: str) -> str:
        """Extract plain text content from document."""
        doc = self.read_document(document_id)
        return self._extract_text(doc)

    def get_all_tabs(self, document_id: str) -> list:
        """Get list of all tabs in the document (including nested child tabs).

        Returns:
            List of dicts with 'tabId', 'title', 'children' (recursive)
        """
        doc = self.read_document(document_id, include_tabs=True)
        tabs = doc.get('tabs', [])
        return self._extract_tabs_tree(tabs)

    def _extract_tabs_tree(self, tabs: list) -> list:
        """Recursively extract tab hierarchy."""
        result = []
        for tab in tabs:
            props = tab.get('tabProperties', {})
            tab_info = {
                'tabId': props.get('tabId', ''),
                'title': props.get('title', ''),
                'children': self._extract_tabs_tree(tab.get('childTabs', []))
            }
            result.append(tab_info)
        return result

    def print_tabs_tree(self, document_id: str, indent: int = 0):
        """Print tab hierarchy as a tree."""
        tabs = self.get_all_tabs(document_id)
        self._print_tabs_recursive(tabs, indent)

    def _print_tabs_recursive(self, tabs: list, indent: int = 0):
        """Recursively print tab tree."""
        prefix = "  " * indent
        for tab in tabs:
            child_count = len(tab['children'])
            suffix = f" ({child_count} children)" if child_count > 0 else ""
            print(f"{prefix}- {tab['title']}{suffix}")
            if tab['children']:
                self._print_tabs_recursive(tab['children'], indent + 1)

    def find_tab_by_title(self, document_id: str, title: str) -> dict | None:
        """Find a tab by title (case-insensitive partial match).

        Returns:
            Tab dict with 'tabId', 'title', 'content' or None if not found
        """
        doc = self.read_document(document_id, include_tabs=True)
        tabs = doc.get('tabs', [])
        return self._search_tabs(tabs, title.lower())

    def _search_tabs(self, tabs: list, title_lower: str) -> dict | None:
        """Recursively search for tab by title."""
        for tab in tabs:
            tab_title = tab.get('tabProperties', {}).get('title', '')
            if title_lower in tab_title.lower():
                return tab
            # Search children
            result = self._search_tabs(tab.get('childTabs', []), title_lower)
            if result:
                return result
        return None

    def read_tab_content(self, document_id: str, tab_title: str) -> str:
        """Read plain text content from a specific tab.

        Args:
            document_id: Google Docs document ID
            tab_title: Tab title (case-insensitive partial match)

        Returns:
            Plain text content of the tab
        """
        tab = self.find_tab_by_title(document_id, tab_title)
        if not tab:
            raise ValueError(f"Tab '{tab_title}' not found in document")

        # Get content from the tab's document structure
        body = tab.get('documentTab', {}).get('body', {})
        content = body.get('content', [])
        return self._extract_content_text(content)

    def _extract_content_text(self, content: list) -> str:
        """Extract text from content elements."""
        text_parts = []
        for element in content:
            if 'paragraph' in element:
                para = element['paragraph']
                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')
                text_parts.append(para_text)
            elif 'table' in element:
                table = element['table']
                for row in table.get('tableRows', []):
                    row_texts = []
                    for cell in row.get('tableCells', []):
                        cell_text = ''
                        for cell_content in cell.get('content', []):
                            if 'paragraph' in cell_content:
                                for elem in cell_content['paragraph'].get('elements', []):
                                    if 'textRun' in elem:
                                        cell_text += elem['textRun'].get('content', '')
                        row_texts.append(cell_text.strip())
                    text_parts.append(' | '.join(row_texts))
        return ''.join(text_parts)

    def get_tab_structure(self, document_id: str, tab_title: str) -> dict:
        """Get structured content from a specific tab (text, tables, images).

        Returns:
            dict with 'title', 'text', 'tables', 'images', 'headings'
        """
        tab = self.find_tab_by_title(document_id, tab_title)
        if not tab:
            raise ValueError(f"Tab '{tab_title}' not found in document")

        body = tab.get('documentTab', {}).get('body', {})
        content = body.get('content', [])
        inline_objects = tab.get('documentTab', {}).get('inlineObjects', {})

        result = {
            'title': tab.get('tabProperties', {}).get('title', ''),
            'text': '',
            'tables': [],
            'images': [],
            'headings': []
        }

        text_parts = []
        for element in content:
            if 'paragraph' in element:
                para = element['paragraph']
                style = para.get('paragraphStyle', {})
                heading = style.get('headingType', 'NORMAL_TEXT')

                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')
                    elif 'inlineObjectElement' in elem:
                        obj_id = elem['inlineObjectElement']['inlineObjectId']
                        if obj_id in inline_objects:
                            obj = inline_objects[obj_id]
                            props = obj.get('inlineObjectProperties', {}).get('embeddedObject', {})
                            img_props = props.get('imageProperties', {})
                            result['images'].append({
                                'id': obj_id,
                                'title': props.get('title', ''),
                                'description': props.get('description', ''),
                                'contentUri': img_props.get('contentUri', ''),
                                'size': props.get('size', {})
                            })

                if heading != 'NORMAL_TEXT':
                    result['headings'].append({
                        'text': para_text.strip(),
                        'level': heading
                    })

                text_parts.append(para_text)

            elif 'table' in element:
                table = element['table']
                rows = table.get('tableRows', [])
                table_data = []
                for row in rows:
                    row_data = []
                    for cell in row.get('tableCells', []):
                        cell_text = ''
                        for cell_content in cell.get('content', []):
                            if 'paragraph' in cell_content:
                                for elem in cell_content['paragraph'].get('elements', []):
                                    if 'textRun' in elem:
                                        cell_text += elem['textRun'].get('content', '')
                        row_data.append(cell_text.strip())
                    table_data.append(row_data)
                result['tables'].append({
                    'rows': len(rows),
                    'columns': len(rows[0].get('tableCells', [])) if rows else 0,
                    'data': table_data
                })

        result['text'] = ''.join(text_parts)
        return result

    def _extract_text(self, doc: dict) -> str:
        """Extract text from document body content."""
        content = doc.get('body', {}).get('content', [])
        text_parts = []

        for element in content:
            if 'paragraph' in element:
                para = element['paragraph']
                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')
                text_parts.append(para_text)
            elif 'table' in element:
                table = element['table']
                for row in table.get('tableRows', []):
                    row_texts = []
                    for cell in row.get('tableCells', []):
                        cell_text = ''
                        for cell_content in cell.get('content', []):
                            if 'paragraph' in cell_content:
                                for elem in cell_content['paragraph'].get('elements', []):
                                    if 'textRun' in elem:
                                        cell_text += elem['textRun'].get('content', '')
                        row_texts.append(cell_text.strip())
                    text_parts.append(' | '.join(row_texts))

        return ''.join(text_parts)

    def replace_text(self, document_id: str, find: str, replace: str) -> dict:
        """Replace all occurrences of text in document."""
        body = {
            'requests': [{
                'replaceAllText': {
                    'containsText': {'text': find, 'matchCase': False},
                    'replaceText': replace
                }
            }]
        }
        return self.service.documents().batchUpdate(
            documentId=document_id, body=body
        ).execute()

    def insert_text_at(self, document_id: str, index: int, text: str) -> dict:
        """Insert text at specific index in document body."""
        body = {
            'requests': [{
                'insertText': {
                    'location': {'index': index},
                    'text': text
                }
            }]
        }
        return self.service.documents().batchUpdate(
            documentId=document_id, body=body
        ).execute()

    def insert_image(self, document_id: str, index: int, image_path: str,
                     width_px: int = 600, height_px: int = 400) -> dict:
        """Insert image at index. Uploads to Drive first."""
        file_metadata = {'name': os.path.basename(image_path)}
        media = self._create_media(image_path)
        file = self.drive_service.files().create(
            body=file_metadata, media_body=media, fields='id'
        ).execute()

        # Make file accessible
        self.drive_service.permissions().create(
            fileId=file['id'], body={'type': 'anyone', 'role': 'reader'}
        ).execute()

        image_url = f"https://drive.google.com/uc?id={file['id']}"
        body = {
            'requests': [{
                'insertInlineImage': {
                    'location': {'index': index},
                    'uri': image_url,
                    'objectSize': {
                        'width': {'magnitude': width_px, 'unit': 'PT'},
                        'height': {'magnitude': height_px, 'unit': 'PT'}
                    }
                }
            }]
        }
        return self.service.documents().batchUpdate(
            documentId=document_id, body=body
        ).execute()

    def _create_media(self, file_path: str):
        """Create media upload object for Drive API."""
        from googleapiclient.http import MediaFileUpload
        mime_type = 'image/png' if file_path.endswith('.png') else 'image/jpeg'
        return MediaFileUpload(file_path, mimetype=mime_type)

    def batch_update(self, document_id: str, requests: list) -> dict:
        """Execute arbitrary batchUpdate requests."""
        return self.service.documents().batchUpdate(
            documentId=document_id, body={'requests': requests}
        ).execute()

    def clear_and_replace_section(self, document_id: str, heading_text: str,
                                   new_content: str) -> dict:
        """Find section by heading, clear it, write new content.

        Strategy:
        1. Read document to find heading index
        2. Find next heading of same or higher level
        3. Delete content between headings
        4. Insert new content
        """
        doc = self.read_document(document_id)
        content = doc.get('body', {}).get('content', [])

        heading_start = None
        heading_end = None
        heading_level = None

        for element in content:
            if 'paragraph' in element:
                para = element['paragraph']
                style = para.get('paragraphStyle', {})
                heading = style.get('headingType', 'NORMAL_TEXT')

                if heading != 'NORMAL_TEXT':
                    # Check if this is our target heading
                    para_text = ''
                    for elem in para.get('elements', []):
                        if 'textRun' in elem:
                            para_text += elem['textRun'].get('content', '')

                    if heading_text.lower() in para_text.lower():
                        heading_start = element['startIndex']
                        heading_level = heading
                    elif heading_start is not None:
                        # Found next heading - stop here
                        heading_end = element['startIndex']
                        break

        if heading_start is None:
            raise ValueError(f"Heading '{heading_text}' not found in document")

        # If no next heading found, use end of document
        if heading_end is None:
            body_end = doc.get('body', {}).get('content', [{}])[-1].get('endIndex', 1)
            heading_end = body_end

        # Delete existing content (keep the heading itself)
        requests = []
        if heading_end > heading_start + 1:
            requests.append({
                'deleteContentRange': {
                    'range': {
                        'startIndex': heading_start + 1,
                        'endIndex': heading_end - 1
                    }
                }
            })

        # Insert new content after heading
        requests.append({
            'insertText': {
                'location': {'index': heading_start + 1},
                'text': new_content
            }
        })

        return self.batch_update(document_id, requests)

    def get_document_sections(self, document_id: str) -> list:
        """Get list of all headings/sections in the document.

        Returns:
            List of dicts with 'text', 'level', 'startIndex', 'endIndex'
        """
        doc = self.read_document(document_id)
        content = doc.get('body', {}).get('content', [])
        sections = []

        for element in content:
            if 'paragraph' in element:
                para = element['paragraph']
                style = para.get('paragraphStyle', {})
                heading = style.get('headingType', 'NORMAL_TEXT')

                if heading != 'NORMAL_TEXT':
                    para_text = ''
                    for elem in para.get('elements', []):
                        if 'textRun' in elem:
                            para_text += elem['textRun'].get('content', '')

                    sections.append({
                        'text': para_text.strip(),
                        'level': heading,
                        'startIndex': element['startIndex'],
                        'endIndex': element['endIndex']
                    })

        return sections

    def get_full_document_structure(self, document_id: str) -> dict:
        """Get complete document structure with all elements.

        Returns:
            dict with:
            - 'title': document title
            - 'total_elements': count of content elements
            - 'headings': list of headings with their styles
            - 'tables': list of tables with their content
            - 'images': list of inline images
            - 'lists': list of list items
            - 'paragraphs_count': total paragraph count
            - 'full_text': complete text content
        """
        doc = self.read_document(document_id)

        content = doc.get('body', {}).get('content', [])
        inline_objects = doc.get('inlineObjects', {})
        lists = doc.get('lists', {})

        result = {
            'title': doc.get('title', ''),
            'total_elements': len(content),
            'headings': [],
            'tables': [],
            'images': [],
            'lists': [],
            'paragraphs_count': 0,
            'full_text': ''
        }

        text_parts = []
        current_heading = None

        for element in content:
            if 'paragraph' in element:
                result['paragraphs_count'] += 1
                para = element['paragraph']
                style = para.get('paragraphStyle', {})
                heading = style.get('headingType', 'NORMAL_TEXT')
                named_style = style.get('namedStyleType', 'NORMAL_TEXT')

                para_text = ''
                for elem in para.get('elements', []):
                    if 'textRun' in elem:
                        para_text += elem['textRun'].get('content', '')
                    elif 'inlineObjectElement' in elem:
                        obj_id = elem['inlineObjectElement']['inlineObjectId']
                        if obj_id in inline_objects:
                            obj = inline_objects[obj_id]
                            props = obj.get('inlineObjectProperties', {}).get('embeddedObject', {})
                            result['images'].append({
                                'id': obj_id,
                                'title': props.get('title', ''),
                                'description': props.get('description', ''),
                                'index': element.get('startIndex', 0)
                            })

                # Track headings
                if heading != 'NORMAL_TEXT' or named_style.startswith('HEADING'):
                    result['headings'].append({
                        'text': para_text.strip(),
                        'level': heading if heading != 'NORMAL_TEXT' else named_style,
                        'index': element.get('startIndex', 0)
                    })

                text_parts.append(para_text)

            elif 'table' in element:
                table = element['table']
                rows = table.get('tableRows', [])
                table_data = []
                for row in rows:
                    row_data = []
                    for cell in row.get('tableCells', []):
                        cell_text = ''
                        for cell_content in cell.get('content', []):
                            if 'paragraph' in cell_content:
                                for elem in cell_content['paragraph'].get('elements', []):
                                    if 'textRun' in elem:
                                        cell_text += elem['textRun'].get('content', '')
                        row_data.append(cell_text.strip())
                    table_data.append(row_data)
                result['tables'].append({
                    'rows': len(rows),
                    'columns': len(rows[0].get('tableCells', [])) if rows else 0,
                    'data': table_data,
                    'index': element.get('startIndex', 0)
                })

        result['full_text'] = ''.join(text_parts)
        return result

    def print_document_summary(self, document_id: str):
        """Print a summary of the document structure."""
        structure = self.get_full_document_structure(document_id)

        print(f"Document: {structure['title']}")
        print(f"Total elements: {structure['total_elements']}")
        print(f"Paragraphs: {structure['paragraphs_count']}")
        print(f"Tables: {len(structure['tables'])}")
        print(f"Images: {len(structure['images'])}")
        print(f"\nHeadings ({len(structure['headings'])}):")
        for h in structure['headings']:
            indent = "  " * (1 if 'HEADING_1' in h['level'] else 2 if 'HEADING_2' in h['level'] else 3)
            print(f"{indent}{h['level']}: {h['text'][:60]}")
        print(f"\nTables ({len(structure['tables'])}):")
        for i, t in enumerate(structure['tables']):
            print(f"  Table {i+1}: {t['rows']}x{t['columns']}")
            if t['data']:
                print(f"    First row: {' | '.join(str(c)[:30] for c in t['data'][0])}")
