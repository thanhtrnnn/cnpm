"""Convert Markdown content to Google Docs API batchUpdate requests."""

import re
from typing import List, Dict, Any, Tuple


# Heading level mapping: markdown ## -> Google Docs HEADING_X
HEADING_LEVELS = {
    '#': 'HEADING_1',
    '##': 'HEADING_2',
    '###': 'HEADING_3',
    '####': 'HEADING_4',
    '#####': 'HEADING_5',
    '######': 'HEADING_6',
}

# Google Docs heading style mapping
HEADING_NAMED_STYLES = {
    'HEADING_1': {'namedStyleType': 'HEADING_1'},
    'HEADING_2': {'namedStyleType': 'HEADING_2'},
    'HEADING_3': {'namedStyleType': 'HEADING_3'},
    'HEADING_4': {'namedStyleType': 'HEADING_4'},
    'HEADING_5': {'namedStyleType': 'HEADING_5'},
    'HEADING_6': {'namedStyleType': 'HEADING_6'},
    'NORMAL_TEXT': {'namedStyleType': 'NORMAL_TEXT'},
}


class MarkdownConverter:
    """Convert markdown text to Google Docs API requests."""

    def __init__(self, plantuml_renderer=None):
        """
        Args:
            plantuml_renderer: Callable that takes PlantUML code and returns image path.
                             If None, PlantUML blocks are inserted as code text.
        """
        self.plantuml_renderer = plantuml_renderer
        self.requests = []
        self.current_index = 1  # Start after document body start

    def convert(self, markdown_text: str, start_index: int = 1) -> List[Dict[str, Any]]:
        """Convert markdown text to list of Google Docs batchUpdate requests.

        Args:
            markdown_text: Markdown formatted text (from cnpm skill output)
            start_index: Starting index in the document (default: 1 for document body start)

        Returns:
            List of batchUpdate request dicts
        """
        self.requests = []
        self.current_index = start_index

        lines = markdown_text.split('\n')
        i = 0

        while i < len(lines):
            line = lines[i]

            # Skip empty lines
            if not line.strip():
                i += 1
                continue

            # Heading
            heading_match = re.match(r'^(#{1,6})\s+(.+)$', line)
            if heading_match:
                level = heading_match.group(1)
                text = heading_match.group(2)
                self._add_heading(text, level)
                i += 1
                continue

            # Table
            if line.strip().startswith('|') and i + 1 < len(lines) and re.match(r'^\|[\s\-:|]+\|$', lines[i + 1].strip()):
                table_lines = [line]
                j = i + 1
                while j < len(lines) and lines[j].strip().startswith('|'):
                    table_lines.append(lines[j])
                    j += 1
                self._add_table(table_lines)
                i = j
                continue

            # PlantUML code block
            if line.strip().startswith('```plantuml'):
                code_lines = []
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith('```'):
                    code_lines.append(lines[j])
                    j += 1
                plantuml_code = '\n'.join(code_lines)
                self._add_plantuml(plantuml_code)
                i = j + 1  # Skip closing ```
                continue

            # Other code block
            if line.strip().startswith('```'):
                code_lines = []
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith('```'):
                    code_lines.append(lines[j])
                    j += 1
                code_text = '\n'.join(code_lines)
                self._add_code_block(code_text)
                i = j + 1
                continue

            # Bullet list
            if re.match(r'^[\s]*[-*]\s+', line):
                self._add_bullet(line)
                i += 1
                continue

            # Numbered list
            if re.match(r'^[\s]*\d+\.\s+', line):
                self._add_numbered_item(line)
                i += 1
                continue

            # Horizontal rule
            if re.match(r'^[\s]*[-*_]{3,}\s*$', line):
                self._add_horizontal_rule()
                i += 1
                continue

            # Regular paragraph
            self._add_paragraph(line)
            i += 1

        return self.requests

    def _add_heading(self, text: str, level: str):
        """Add a heading request."""
        named_style = HEADING_LEVELS.get(level, 'NORMAL_TEXT')
        clean_text = self._clean_inline_formatting(text) + '\n'

        # Insert text
        self.requests.append({
            'insertText': {
                'location': {'index': self.current_index},
                'text': clean_text
            }
        })

        # Apply heading style
        self.requests.append({
            'updateParagraphStyle': {
                'range': {
                    'startIndex': self.current_index,
                    'endIndex': self.current_index + len(clean_text) - 1
                },
                'paragraphStyle': {
                    'namedStyleType': named_style
                },
                'fields': 'namedStyleType'
            }
        })

        # Apply inline formatting (bold, italic, etc.)
        self._apply_inline_formatting(text, self.current_index)

        self.current_index += len(clean_text)

    def _add_paragraph(self, text: str):
        """Add a regular paragraph."""
        clean_text = self._clean_inline_formatting(text) + '\n'

        self.requests.append({
            'insertText': {
                'location': {'index': self.current_index},
                'text': clean_text
            }
        })

        # Explicitly reset to NORMAL_TEXT to prevent style inheritance from previous paragraph
        if len(clean_text) > 1:
            self.requests.append({
                'updateParagraphStyle': {
                    'range': {
                        'startIndex': self.current_index,
                        'endIndex': self.current_index + len(clean_text) - 1
                    },
                    'paragraphStyle': {
                        'namedStyleType': 'NORMAL_TEXT'
                    },
                    'fields': 'namedStyleType'
                }
            })

        self._apply_inline_formatting(text, self.current_index)
        self.current_index += len(clean_text)

    def _add_table(self, table_lines: List[str]):
        """Add a markdown table."""
        # Parse table
        rows = []
        for line in table_lines:
            line = line.strip()
            if not line.startswith('|'):
                continue
            # Skip separator line
            if re.match(r'^\|[\s\-:|]+\|$', line):
                continue
            cells = [c.strip() for c in line.split('|')[1:-1]]
            rows.append(cells)

        if not rows:
            return

        num_rows = len(rows)
        num_cols = max(len(row) for row in rows)

        # Pad rows to have same number of columns
        for row in rows:
            while len(row) < num_cols:
                row.append('')

        # Insert table
        self.requests.append({
            'insertTable': {
                'location': {'index': self.current_index},
                'rows': num_rows,
                'columns': num_cols
            }
        })

        # Calculate table structure indices
        # In Google Docs, each cell contains a paragraph with 1 char (newline)
        # Table structure: each cell = 2 indices (content + newline)
        # Plus table/row/cell structure markers
        # Total indices per row = num_cols * 2 (cells) + 1 (row marker)
        # Total indices for table = num_rows * (num_cols * 2 + 1) + 1 (table marker)
        table_indices = num_rows * (num_cols * 2 + 1) + 1
        self.current_index += table_indices

    def _add_plantuml(self, code: str):
        """Add PlantUML diagram (rendered as image if renderer available)."""
        if self.plantuml_renderer:
            try:
                image_path = self.plantuml_renderer(code)
                # Note: Image insertion needs to be handled by the client
                # Store the image path for the caller
                self.requests.append({
                    'insertImage': {
                        'location': {'index': self.current_index},
                        'imagePath': image_path
                    }
                })
                self.current_index += 1  # Image takes 1 character
                return
            except Exception:
                pass  # Fall back to code block

        # Fall back to code block
        self._add_code_block(code)

    def _add_code_block(self, code: str):
        """Add a code block with monospace formatting."""
        text = code + '\n'

        self.requests.append({
            'insertText': {
                'location': {'index': self.current_index},
                'text': text
            }
        })

        # Reset paragraph style to prevent inheritance
        self.requests.append({
            'updateParagraphStyle': {
                'range': {
                    'startIndex': self.current_index,
                    'endIndex': self.current_index + len(text) - 1
                },
                'paragraphStyle': {
                    'namedStyleType': 'NORMAL_TEXT'
                },
                'fields': 'namedStyleType'
            }
        })

        # Apply monospace font
        self.requests.append({
            'updateTextStyle': {
                'range': {
                    'startIndex': self.current_index,
                    'endIndex': self.current_index + len(text) - 1
                },
                'textStyle': {
                    'weightedFontFamily': {'fontFamily': 'Courier New'}
                },
                'fields': 'weightedFontFamily'
            }
        })

        self.current_index += len(text)

    def _add_bullet(self, line: str):
        """Add a bullet list item."""
        # Extract text after bullet marker
        text = re.sub(r'^[\s]*[-*]\s+', '', line) + '\n'

        self.requests.append({
            'insertText': {
                'location': {'index': self.current_index},
                'text': text
            }
        })

        # Reset paragraph style to prevent inheritance
        self.requests.append({
            'updateParagraphStyle': {
                'range': {
                    'startIndex': self.current_index,
                    'endIndex': self.current_index + len(text) - 1
                },
                'paragraphStyle': {
                    'namedStyleType': 'NORMAL_TEXT'
                },
                'fields': 'namedStyleType'
            }
        })

        # Apply bullet formatting
        self.requests.append({
            'createParagraphBullets': {
                'range': {
                    'startIndex': self.current_index,
                    'endIndex': self.current_index + len(text) - 1
                },
                'bulletPreset': 'BULLET_DISC_CIRCLE_SQUARE'
            }
        })

        self._apply_inline_formatting(text, self.current_index)
        self.current_index += len(text)

    def _add_numbered_item(self, line: str):
        """Add a numbered list item."""
        text = re.sub(r'^[\s]*\d+\.\s+', '', line) + '\n'

        self.requests.append({
            'insertText': {
                'location': {'index': self.current_index},
                'text': text
            }
        })

        # Reset paragraph style to prevent inheritance
        self.requests.append({
            'updateParagraphStyle': {
                'range': {
                    'startIndex': self.current_index,
                    'endIndex': self.current_index + len(text) - 1
                },
                'paragraphStyle': {
                    'namedStyleType': 'NORMAL_TEXT'
                },
                'fields': 'namedStyleType'
            }
        })

        self.requests.append({
            'createParagraphBullets': {
                'range': {
                    'startIndex': self.current_index,
                    'endIndex': self.current_index + len(text) - 1
                },
                'bulletPreset': 'NUMBERED_DECIMAL_ALPHA_ROMAN'
            }
        })

        self._apply_inline_formatting(text, self.current_index)
        self.current_index += len(text)

    def _add_horizontal_rule(self):
        """Add a horizontal rule (as a line of dashes)."""
        text = '─' * 50 + '\n'
        self.requests.append({
            'insertText': {
                'location': {'index': self.current_index},
                'text': text
            }
        })
        self.current_index += len(text)

    def _clean_inline_formatting(self, text: str) -> str:
        """Remove markdown formatting markers from text (for plain text insertion)."""
        # Remove bold markers
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        # Remove italic markers
        text = re.sub(r'\*(.+?)\*', r'\1', text)
        # Remove inline code
        text = re.sub(r'`(.+?)`', r'\1', text)
        # Remove links, keep text
        text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
        return text

    def _apply_inline_formatting(self, original_text: str, base_index: int):
        """Apply bold, italic, etc. formatting to inserted text."""
        # Find bold markers
        for match in re.finditer(r'\*\*(.+?)\*\*', original_text):
            start = base_index + match.start()
            end = base_index + match.start() + len(match.group(1))
            self.requests.append({
                'updateTextStyle': {
                    'range': {
                        'startIndex': start,
                        'endIndex': end
                    },
                    'textStyle': {'bold': True},
                    'fields': 'bold'
                }
            })

        # Find italic markers (single *)
        for match in re.finditer(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)', original_text):
            start = base_index + match.start()
            end = base_index + match.start() + len(match.group(1))
            self.requests.append({
                'updateTextStyle': {
                    'range': {
                        'startIndex': start,
                        'endIndex': end
                    },
                    'textStyle': {'italic': True},
                    'fields': 'italic'
                }
            })


def convert_markdown_to_requests(markdown_text: str, plantuml_renderer=None, start_index: int = 1) -> List[Dict[str, Any]]:
    """Convenience function to convert markdown to Google Docs requests.

    Args:
        markdown_text: Markdown formatted text
        plantuml_renderer: Optional callable for PlantUML rendering
        start_index: Starting index in the document (default: 1 for document body start)

    Returns:
        List of batchUpdate request dicts
    """
    converter = MarkdownConverter(plantuml_renderer)
    return converter.convert(markdown_text, start_index)


def extract_plantuml_blocks(markdown_text: str) -> List[str]:
    """Extract all PlantUML code blocks from markdown text.

    Args:
        markdown_text: Markdown text containing PlantUML blocks

    Returns:
        List of PlantUML code strings (without @startuml/@enduml markers)
    """
    blocks = []
    pattern = r'```plantuml\s*\n(.*?)```'
    for match in re.finditer(pattern, markdown_text, re.DOTALL):
        code = match.group(1).strip()
        # Remove @startuml/@enduml if present
        code = re.sub(r'^@startuml\s*\n?', '', code)
        code = re.sub(r'\n?@enduml\s*$', '', code)
        blocks.append(code.strip())
    return blocks
