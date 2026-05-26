"""Google Docs API client wrapper."""

import os
from googleapiclient.errors import HttpError
from .auth import get_service, get_drive_service


class GDocsClient:
    """Wrapper for Google Docs API operations."""

    def __init__(self, service=None, drive_service=None, credentials_path=None):
        self.service = service or get_service(credentials_path)
        self.drive_service = drive_service or get_drive_service(credentials_path)

    def read_document(self, document_id: str) -> dict:
        """Fetch full document structure. Returns raw API response."""
        return self.service.documents().get(documentId=document_id).execute()

    def read_as_text(self, document_id: str) -> str:
        """Extract plain text content from document."""
        doc = self.read_document(document_id)
        return self._extract_text(doc)

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
