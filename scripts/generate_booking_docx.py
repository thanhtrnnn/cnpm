"""Generate DOCX for "Quản lý đặt & trả phòng" module.

Features:
- H1 with blue underline (phase names)
- H2/H3/H4 proper hierarchy
- Wireframes in monospace frames with equal spacing
- Real PlantUML diagram images
- Scenario tables with 30/70 column width
- Bold headers, inline code, bullets
"""
import os
import re
from docx import Document
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, '..', 'docs', 'tabs')
DIAGRAM_DIR = os.path.join(SCRIPT_DIR, '..', 'output', 'diagrams')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'output')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'booking_module.docx')

# Files in order with phase headers: (filename, phase_header_before)
FILES = [
    (None, 'II. PHA PHÂN TÍCH'),
    ('section-booking-ii.1-fix.md', None),
    (None, 'III. PHA THIẾT KẾ'),
    ('section-booking-iii.1.md', None),
    ('section-booking-iii.2.md', None),
    ('section-booking-iii.3.1.md', None),
    ('section-booking-iii.3.2.md', None),
    ('section-booking-iii.4.md', None),
    (None, 'IV. PHA CÀI ĐẶT VÀ KIỂM THỬ'),
    ('section-booking-iv.md', None),
]

# Diagram files mapped to their placeholder comments in markdown
DIAGRAM_MAP = {
    'booking_entity_class': 'output/diagrams/booking_entity_class.png',
    'booking_erd': 'output/diagrams/booking_erd.png',
    'booking_mvc_class': 'output/diagrams/booking_mvc_class.png',
    'booking_seq_datphong': 'output/diagrams/booking_seq_1.png',
    'booking_seq_checkin': 'output/diagrams/booking_seq_2.png',
    'booking_seq_checkout': 'output/diagrams/booking_seq_3.png',
    'booking_seq_huyphong': 'output/diagrams/booking_seq_4.png',
}


def clean_inline(text):
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text


def extract_inline_formatting(text):
    segments = []
    i = 0
    current = ''
    while i < len(text):
        if text[i:i+2] == '**':
            if current:
                segments.append((current, False, False))
                current = ''
            j = text.find('**', i + 2)
            if j != -1:
                segments.append((text[i+2:j], True, False))
                i = j + 2
                continue
        if text[i] == '`':
            if current:
                segments.append((current, False, False))
                current = ''
            j = text.find('`', i + 1)
            if j != -1:
                segments.append((text[i+1:j], False, True))
                i = j + 1
                continue
        if text[i] == '[':
            m = re.match(r'\[(.+?)\]\((.+?)\)', text[i:])
            if m:
                if current:
                    segments.append((current, False, False))
                    current = ''
                segments.append((m.group(1), False, False))
                i += m.end()
                continue
        current += text[i]
        i += 1
    if current:
        segments.append((current, False, False))
    return segments


def determine_heading_level(text):
    t = text.strip()
    if re.match(r'^[IVX]+\.\s+PHA\s', t) or t.startswith('PHA '):
        return 1
    if t in ('II. PHA PHÂN TÍCH', 'III. PHA THIẾT KẾ', 'IV. PHA CÀI ĐẶT VÀ KIỂM THỬ',
             'PHA XÁC ĐỊNH YÊU CẦU'):
        return 1
    if re.match(r'^\d+\.\d+\.\s', t):
        return 2
    section_names = [
        'Bảng thuật ngữ', 'Mô hình hóa chức năng', 'Mô hình hóa lớp',
        'Mô hình hóa tĩnh', 'Mô hình hóa động', 'Thiết kế lớp thực thể',
        'Thiết kế CSDL', 'Thiết kế tĩnh', 'Thiết kế giao diện',
        'Thiết kế mô hình MVC', 'Kiểm thử chức năng',
        'Mô hình nghiệp vụ bằng ngôn ngữ tự nhiên',
        'Mô hình nghiệp vụ bằng UML',
    ]
    for name in section_names:
        if t.startswith(name):
            return 2
    if re.match(r'^[a-e]\)\s', t):
        return 3
    if re.match(r'^Bước\s\d', t):
        return 3
    if re.match(r'^\d+\.\s+Tầng\s', t):
        return 4
    if t.startswith('Use case '):
        return 4
    if t.startswith('Màn hình '):
        return 3
    if t.startswith('Biểu đồ ') or t.startswith('Kịch bản phiên bản'):
        return 3
    if t.startswith('TC') and re.match(r'^TC\d+', t):
        return 3
    return None


def add_heading_with_blue_underline(doc, text, level):
    """Add heading with blue underline for H1."""
    p = doc.add_heading(level=level)
    segments = extract_inline_formatting(text)
    for seg_text, is_bold, is_code in segments:
        run = p.add_run(seg_text)
        if is_bold:
            run.bold = True
        if is_code:
            run.font.name = 'Courier New'

    if level == 1:
        # Add blue underline
        for run in p.runs:
            run.font.color.rgb = RGBColor(0, 0, 200)
            rPr = run._element.get_or_add_rPr()
            u = parse_xml(f'<w:u {nsdecls("w")} w:val="single" w:color="0000C8"/>')
            rPr.append(u)

    return p


def add_formatted_paragraph(doc, text, style='Normal'):
    p = doc.add_paragraph(style=style)
    segments = extract_inline_formatting(text)
    for seg_text, is_bold, is_code in segments:
        run = p.add_run(seg_text)
        if is_bold:
            run.bold = True
        if is_code:
            run.font.name = 'Courier New'
            run.font.size = Pt(10)
    return p


def set_cell_shading(cell, color):
    """Set cell background color."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def add_scenario_table(doc, rows):
    """Add a 2-column scenario table with 30/70 width split."""
    if not rows or len(rows[0]) < 2:
        return

    table = doc.add_table(rows=len(rows), cols=2)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER

    # Set column widths: 30% / 70%
    for row in table.rows:
        row.cells[0].width = Cm(5)
        row.cells[1].width = Cm(12)

    for ri, row in enumerate(rows):
        for ci in range(2):
            cell = table.cell(ri, ci)
            cell.text = ''
            p = cell.paragraphs[0]
            p.style = doc.styles['Normal']

            cell_text = row[ci] if ci < len(row) else ''
            # Replace <br> with actual line breaks
            parts = cell_text.split('<br>')
            for pi, part in enumerate(parts):
                part = part.strip()
                if not part:
                    continue
                segments = extract_inline_formatting(part)
                for seg_text, is_bold, is_code in segments:
                    run = p.add_run(seg_text)
                    run.font.size = Pt(10)
                    if is_bold or ri == 0:
                        run.bold = True
                    if is_code:
                        run.font.name = 'Courier New'
                        run.font.size = Pt(9)
                if pi < len(parts) - 1:
                    p.add_run('\n')

            # Header row shading
            if ri == 0:
                set_cell_shading(cell, 'D9E2F3')

    return table


def add_data_table(doc, rows):
    """Add a generic data table."""
    if not rows:
        return
    num_cols = max(len(r) for r in rows)
    table = doc.add_table(rows=len(rows), cols=num_cols)
    table.style = 'Table Grid'

    for ri, row in enumerate(rows):
        for ci, cell_text in enumerate(row):
            if ci < num_cols:
                cell = table.cell(ri, ci)
                cell.text = ''
                p = cell.paragraphs[0]
                p.style = doc.styles['Normal']
                segments = extract_inline_formatting(cell_text)
                for seg_text, is_bold, is_code in segments:
                    run = p.add_run(seg_text)
                    run.font.size = Pt(10)
                    if is_bold or ri == 0:
                        run.bold = True
                    if is_code:
                        run.font.name = 'Courier New'
                        run.font.size = Pt(9)
                if ri == 0:
                    set_cell_shading(cell, 'D9E2F3')
    return table


def add_wireframe(doc, lines):
    """Add wireframe in a monospace frame with equal spacing."""
    # Add all wireframe lines in a single monospace block
    text = '\n'.join(lines)
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']

    # Add border around the paragraph
    pPr = p._element.get_or_add_pPr()
    pBdr = parse_xml(
        f'<w:pBdr {nsdecls("w")}>'
        f'  <w:top w:val="single" w:sz="4" w:space="4" w:color="808080"/>'
        f'  <w:left w:val="single" w:sz="4" w:space="4" w:color="808080"/>'
        f'  <w:bottom w:val="single" w:sz="4" w:space="4" w:color="808080"/>'
        f'  <w:right w:val="single" w:sz="4" w:space="4" w:color="808080"/>'
        f'</w:pBdr>'
    )
    pPr.append(pBdr)

    # Add background shading
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:fill="F5F5F5"/>')
    pPr.append(shd)

    run = p.add_run(text)
    run.font.name = 'Courier New'
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(0, 0, 0)

    return p


def add_diagram_image(doc, image_path, width=Inches(6)):
    """Add a diagram image to the document."""
    if not os.path.exists(image_path):
        p = doc.add_paragraph(f'[Image not found: {image_path}]')
        p.style = doc.styles['Normal']
        return p
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(image_path, width=width)
    return p


def find_diagram_for_placeholder(comment_text):
    """Find diagram file path from placeholder comment."""
    for key, path in DIAGRAM_MAP.items():
        if key in comment_text:
            return path
    return None


def process_file(doc, md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip PlantUML code blocks but remember their positions
    plantuml_blocks = []
    for m in re.finditer(r'```plantuml\s*\n(.*?)```', content, re.DOTALL):
        plantuml_blocks.append(m.group(1).strip())
    content = re.sub(r'```plantuml\s*\n.*?```', '<!-- PLANTUML_PLACEHOLDER -->', content, flags=re.DOTALL)

    lines = content.split('\n')
    i = 0
    current_table = []
    in_table = False
    is_scenario_table = False
    in_code_block = False
    code_lines = []
    in_wireframe = False
    wireframe_lines = []
    plantuml_idx = 0

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # PlantUML placeholder — insert diagram image
        if stripped == '<!-- PLANTUML_PLACEHOLDER -->':
            if plantuml_idx < len(plantuml_blocks):
                # Find the corresponding diagram file
                # Map by order: first block in iii.1 = entity, iii.2 = erd, etc.
                diagram_files = [
                    'output/diagrams/booking_entity_class.png',
                    'output/diagrams/booking_erd.png',
                    'output/diagrams/booking_mvc_class.png',
                    'output/diagrams/booking_seq_1.png',
                    'output/diagrams/booking_seq_2.png',
                    'output/diagrams/booking_seq_3.png',
                    'output/diagrams/booking_seq_4.png',
                ]
                # Find which file this is from
                base = os.path.basename(md_file)
                if 'iii.1' in base:
                    img = 'output/diagrams/booking_entity_class.png'
                elif 'iii.2' in base:
                    img = 'output/diagrams/booking_erd.png'
                elif 'iii.3.2' in base:
                    img = 'output/diagrams/booking_mvc_class.png'
                elif 'iii.4' in base:
                    seq_map = {0: 'booking_seq_1', 1: 'booking_seq_2', 2: 'booking_seq_3', 3: 'booking_seq_4'}
                    img = f'output/diagrams/{seq_map.get(plantuml_idx, "booking_seq_1")}.png'
                else:
                    img = None
                if img:
                    add_diagram_image(doc, img)
                plantuml_idx += 1
            i += 1
            continue

        # Code block
        if stripped.startswith('```'):
            if in_code_block:
                code_text = '\n'.join(code_lines)
                if code_text.strip():
                    # Check if it's a wireframe (contains +-- or |)
                    if any('+--' in l or '| ' in l for l in code_lines):
                        add_wireframe(doc, code_lines)
                    else:
                        p = doc.add_paragraph()
                        run = p.add_run(code_text)
                        run.font.name = 'Courier New'
                        run.font.size = Pt(9)
                code_lines = []
                in_code_block = False
            else:
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            code_lines.append(line)
            i += 1
            continue

        # Placeholder comment — check for diagram
        if stripped.startswith('<!-- PLACEHOLDER:') or stripped.startswith('<!-- PLACEHOLDER -->'):
            img_path = find_diagram_for_placeholder(stripped)
            if img_path:
                add_diagram_image(doc, img_path)
            i += 1
            continue

        # Empty line
        if not stripped:
            if in_table and current_table:
                if is_scenario_table:
                    add_scenario_table(doc, current_table)
                else:
                    add_data_table(doc, current_table)
                current_table = []
                in_table = False
            i += 1
            continue

        # Table separator row
        if re.match(r'^\|[\s\-:|]+\|$', stripped):
            i += 1
            continue

        # Table row
        if stripped.startswith('|') and '|' in stripped[1:]:
            if not in_table:
                in_table = True
                # Detect scenario table (2-column Use Case spec)
                cells = [c.strip() for c in stripped.split('|')[1:-1]]
                is_scenario_table = (len(cells) == 2 and any(
                    kw in cells[0].lower() for kw in ['use case', 'actor', 'tiền', 'hậu', 'kịch', 'ngoại']
                ))
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            current_table.append(cells)
            i += 1
            continue

        # Flush table
        if in_table and current_table:
            if is_scenario_table:
                add_scenario_table(doc, current_table)
            else:
                add_data_table(doc, current_table)
            current_table = []
            in_table = False

        # Heading
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            text = m.group(2).strip()
            content_level = determine_heading_level(text)
            if content_level:
                level = content_level
            add_heading_with_blue_underline(doc, text, level)
            i += 1
            continue

        # Bold paragraph
        bm = re.match(r'^\*\*(.+?)\*\*$', stripped)
        if bm:
            text = bm.group(1).strip()
            content_level = determine_heading_level(text)
            if content_level:
                add_heading_with_blue_underline(doc, text, content_level)
            else:
                p = add_formatted_paragraph(doc, text, style='Normal')
                for run in p.runs:
                    run.bold = True
            i += 1
            continue

        # Bullet
        bm = re.match(r'^(\s*)[-]\s+(.+)$', line)
        if bm:
            text = bm.group(2).strip()
            add_formatted_paragraph(doc, text, style='List Bullet')
            i += 1
            continue

        # Regular paragraph
        add_formatted_paragraph(doc, stripped, style='Normal')
        i += 1

    # Flush remaining table
    if in_table and current_table:
        if is_scenario_table:
            add_scenario_table(doc, current_table)
        else:
            add_data_table(doc, current_table)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    doc = Document()

    # Default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(11)

    # Heading styles
    for level in range(1, 5):
        hs = doc.styles[f'Heading {level}']
        hs.font.name = 'Arial'
        if level == 1:
            hs.font.size = Pt(16)
            hs.font.bold = True
            hs.font.color.rgb = RGBColor(0, 0, 200)
        elif level == 2:
            hs.font.size = Pt(14)
            hs.font.bold = True
        elif level == 3:
            hs.font.size = Pt(12)
            hs.font.bold = True
        elif level == 4:
            hs.font.size = Pt(11)
            hs.font.bold = True

    for item in FILES:
        filename, phase_header = item

        # Add phase header (H1 with blue underline)
        if phase_header:
            add_heading_with_blue_underline(doc, phase_header, 1)

        if filename is None:
            continue

        md_file = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(md_file):
            print(f"SKIP: {filename}")
            continue
        print(f"Processing: {filename}")
        process_file(doc, md_file)
        doc.add_paragraph('')

    doc.save(OUTPUT_FILE)
    print(f"\nSaved: {OUTPUT_FILE}")
    print(f"Size: {os.path.getsize(OUTPUT_FILE)} bytes")


if __name__ == '__main__':
    main()
