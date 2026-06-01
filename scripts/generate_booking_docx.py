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
    (None, 'I. PHA XÁC ĐỊNH YÊU CẦU'),
    ('section-booking-i.md', None),
    ('section-booking-i-uc.md', None),
    (None, 'II. PHA PHÂN TÍCH'),
    ('section-booking-ii.1-datphong.md', None),
    ('section-booking-ii.1-fix.md', None),
    ('section-booking-ii.3-2.4.md', None),
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
    # Phase II - Analysis BCE diagrams
    'booking_bce_datphong': 'output/diagrams/booking_bce_datphong.png',
    'booking_bce_huyphong': 'output/diagrams/booking_bce_huyphong.png',
    'booking_bce_checkin': 'output/diagrams/booking_bce_checkin.png',
    'booking_bce_checkout': 'output/diagrams/booking_bce_checkout.png',
    # Phase II - Analysis sequence diagrams
    'booking_aseq_datphong': 'output/diagrams/booking_aseq_datphong.png',
    'booking_aseq_huyphong': 'output/diagrams/booking_aseq_huyphong.png',
    'booking_aseq_checkin': 'output/diagrams/booking_aseq_checkin.png',
    'booking_aseq_checkout': 'output/diagrams/booking_aseq_checkout.png',
    # Phase III - Design diagrams
    'booking_entity_class': 'output/diagrams/booking_entity_class.png',
    'booking_erd': 'output/diagrams/booking_erd.png',
    'booking_mvc_class': 'output/diagrams/booking_mvc_class.png',
    'booking_seq_datphong': 'output/diagrams/booking_seq_1.png',
    'booking_seq_checkin': 'output/diagrams/booking_seq_2.png',
    'booking_seq_checkout': 'output/diagrams/booking_seq_3.png',
    'booking_seq_huyphong': 'output/diagrams/booking_seq_4.png',
    # Phase I - UC diagrams
    'booking_uc_overview': 'output/diagrams/booking_uc_overview.png',
    'booking_uc_datphong': 'output/diagrams/booking_uc_datphong.png',
    'booking_uc_huyphong': 'output/diagrams/booking_uc_huyphong.png',
    'booking_uc_checkin': 'output/diagrams/booking_uc_checkin.png',
    'booking_uc_checkout': 'output/diagrams/booking_uc_checkout.png',
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


def add_heading(doc, text, level):
    """Add heading with black text, no underline."""
    p = doc.add_heading(level=level)
    segments = extract_inline_formatting(text)
    for seg_text, is_bold, is_code in segments:
        run = p.add_run(seg_text)
        run.font.color.rgb = RGBColor(0, 0, 0)
        if is_bold:
            run.bold = True
        if is_code:
            run.font.name = 'Courier New'

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

    # Strip PlantUML code blocks, replacing with named diagram placeholders
    def replace_plantuml(match):
        block_content = match.group(1).strip()
        # Determine diagram name based on file and content
        base = os.path.basename(md_file)
        if 'ii.3-2.4' in base:
            # Phase II analysis diagrams - use content to identify
            if 'ReceptionistHomeView' in block_content and 'SearchFreeRoomView' in block_content and 'SearchClientView' in block_content:
                if 'class ' in block_content:
                    return '<!-- DIAGRAM: booking_bce_datphong -->'
                else:
                    return '<!-- DIAGRAM: booking_aseq_datphong -->'
            elif 'SearchBookingView' in block_content:
                if 'class ' in block_content:
                    return '<!-- DIAGRAM: booking_bce_huyphong -->'
                else:
                    return '<!-- DIAGRAM: booking_aseq_huyphong -->'
            elif 'CheckInView' in block_content:
                if 'class ' in block_content:
                    return '<!-- DIAGRAM: booking_bce_checkin -->'
                else:
                    return '<!-- DIAGRAM: booking_aseq_checkin -->'
            elif 'CheckOutView' in block_content:
                if 'class ' in block_content:
                    return '<!-- DIAGRAM: booking_bce_checkout -->'
                else:
                    return '<!-- DIAGRAM: booking_aseq_checkout -->'
        elif 'iii.1' in base:
            return '<!-- DIAGRAM: booking_entity_class -->'
        elif 'iii.2' in base:
            return '<!-- DIAGRAM: booking_erd -->'
        elif 'iii.3.2' in base:
            return '<!-- DIAGRAM: booking_mvc_class -->'
        elif 'iii.4' in base:
            if 'SearchFreeRoomView' in block_content or 'SearchFreeRoomForm' in block_content or 'Đặt phòng' in block_content:
                return '<!-- DIAGRAM: booking_seq_datphong -->'
            elif 'CheckInView' in block_content or 'Check-in' in block_content:
                return '<!-- DIAGRAM: booking_seq_checkin -->'
            elif 'CheckOutView' in block_content or 'Check-out' in block_content:
                return '<!-- DIAGRAM: booking_seq_checkout -->'
            elif 'SearchBookingView' in block_content or 'CancelBookingPage' in block_content or 'Hủy' in block_content:
                return '<!-- DIAGRAM: booking_seq_huyphong -->'
        elif 'i-uc' in base:
            # Match by rectangle title (most reliable)
            if 'rectangle "Quản lý đặt và trả phòng"' in block_content:
                return '<!-- DIAGRAM: booking_uc_overview -->'
            elif 'rectangle "Đặt phòng"' in block_content:
                return '<!-- DIAGRAM: booking_uc_datphong -->'
            elif 'rectangle "Huỷ phòng"' in block_content:
                return '<!-- DIAGRAM: booking_uc_huyphong -->'
            elif 'rectangle "Check-in"' in block_content:
                return '<!-- DIAGRAM: booking_uc_checkin -->'
            elif 'rectangle "Check-out"' in block_content:
                return '<!-- DIAGRAM: booking_uc_checkout -->'
        return '<!-- DIAGRAM: unknown -->'

    content = re.sub(r'```plantuml\s*\n(.*?)```', replace_plantuml, content, flags=re.DOTALL)

    lines = content.split('\n')
    i = 0
    current_table = []
    in_table = False
    is_scenario_table = False
    in_code_block = False
    code_lines = []
    in_wireframe = False
    wireframe_lines = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Named diagram placeholder — insert diagram image
        if stripped.startswith('<!-- DIAGRAM:') and stripped.endswith('-->'):
            diagram_name = stripped.replace('<!-- DIAGRAM:', '').replace('-->', '').strip()
            if diagram_name in DIAGRAM_MAP:
                add_diagram_image(doc, DIAGRAM_MAP[diagram_name])
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

        # Heading (## / ### / ####) — cap at level 3
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            md_level = len(m.group(1))
            text = m.group(2).strip()
            # Cap at level 3 (no H4)
            level = min(md_level, 3)
            add_heading(doc, text, level)
            i += 1
            continue

        # Bold paragraph that wraps a heading: **## X.Y. Title**
        bm_heading = re.match(r'^\*\*#{1,4}\s+(.+?)\*\*$', stripped)
        if bm_heading:
            text = bm_heading.group(1).strip()
            level = determine_heading_level(text)
            if level:
                add_heading(doc, text, level)
            else:
                p = doc.add_paragraph()
                run = p.add_run(text)
                run.bold = True
            i += 1
            continue

        # Bold paragraph — keep as bold text, not heading
        bm = re.match(r'^\*\*(.+?)\*\*$', stripped)
        if bm:
            text = bm.group(1).strip()
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

        if filename is None:
            # Standalone phase header (no file follows)
            if phase_header:
                add_heading(doc, phase_header, 1)
            continue

        md_file = os.path.join(DOCS_DIR, filename)
        if not os.path.exists(md_file):
            print(f"SKIP: {filename}")
            continue
        print(f"Processing: {filename}")

        # Skip phase header if file already contains it as first heading
        if phase_header:
            with open(md_file, 'r', encoding='utf-8') as f:
                first_lines = f.read()[:500]
            if phase_header not in first_lines:
                add_heading(doc, phase_header, 1)

        process_file(doc, md_file)
        doc.add_paragraph('')

    doc.save(OUTPUT_FILE)
    print(f"\nSaved: {OUTPUT_FILE}")
    print(f"Size: {os.path.getsize(OUTPUT_FILE)} bytes")


if __name__ == '__main__':
    main()
