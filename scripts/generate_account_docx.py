"""Generate DOCX for "Tài khoản & Thành viên" module.

Features:
- H1 with blue underline (phase names)
- H2/H3/H4 proper hierarchy
- Wireframes in monospace frames
- Real PlantUML diagram images
- Scenario tables with 30/70 column width
- Bold headers, inline code, bullets
"""
import os
import re
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DOCS_DIR = os.path.join(SCRIPT_DIR, '..', 'docs', 'tabs')
DIAGRAM_DIR = os.path.join(SCRIPT_DIR, '..', 'output', 'diagrams')
OUTPUT_DIR = os.path.join(SCRIPT_DIR, '..', 'output')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'account_module.docx')

FILES = [
    (None, 'I. PHA XÁC ĐỊNH YÊU CẦU'),
    ('section-account-i.md', None),
    (None, 'II. PHA PHÂN TÍCH'),
    ('section-account-ii.md', None),
    (None, 'III. PHA THIẾT KẾ'),
    ('section-account-iii.md', None),
    (None, 'IV. PHA CÀI ĐẶT VÀ KIỂM THỬ'),
    ('section-account-iv.md', None),
]

DIAGRAM_MAP = {
    'account_entity_class': 'output/diagrams/account_entity_class.png',
    'account_erd': 'output/diagrams/account_erd.png',
    'account_mvc_class': 'output/diagrams/account_dao_class.png',
    'account_dao_class': 'output/diagrams/account_dao_class.png',
    'account_seq_login': 'output/diagrams/account_seq_login.png',
    'account_seq_register': 'output/diagrams/account_seq_register.png',
    'account_seq_changepw': 'output/diagrams/account_seq_changepw.png',
    'account_seq_profile': 'output/diagrams/account_seq_profile.png',
    'account_seq_staff': 'output/diagrams/account_seq_staff.png',
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
        current += text[i]
        i += 1
    if current:
        segments.append((current, False, False))
    return segments


def determine_heading_level(text):
    t = text.strip()
    if re.match(r'^[IVX]+\.\s+PHA\s', t) or t.startswith('PHA '):
        return 1
    if t in ('II. PHA PHÂN TÍCH', 'III. PHA THIẾT KẾ', 'IV. PHA CÀI ĐẶT VÀ KIỂM THỬ'):
        return 1
    if re.match(r'^\d+\.\d+\.\s', t):
        return 2
    if re.match(r'^\d+\.\s', t):
        return 2
    section_names = [
        'Danh sách Use Case', 'Danh sách Actor', 'UC con',
        'Biểu đồ Use Case', 'Kịch bản chuẩn', 'Trích xuất',
        'Thiết kế lớp', 'Thiết kế CSDL', 'Wireframe',
        'MVC', 'Biểu đồ tuần tự', 'Lập kế hoạch',
        'Test case', 'Mô hình',
    ]
    for name in section_names:
        if t.startswith(name):
            return 2
    if re.match(r'^UC\d+', t):
        return 3
    if t.startswith('Màn hình '):
        return 3
    if t.startswith('Bước ') or t.startswith('Mô hình'):
        return 3
    if t.startswith('TC') and re.match(r'^TC\d+', t):
        return 3
    return None


def add_heading_with_blue_underline(doc, text, level):
    p = doc.add_heading(level=level)
    segments = extract_inline_formatting(text)
    for seg_text, is_bold, is_code in segments:
        run = p.add_run(seg_text)
        if is_bold:
            run.bold = True
        if is_code:
            run.font.name = 'Courier New'
    if level == 1:
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
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def add_scenario_table(doc, rows):
    if not rows or len(rows[0]) < 2:
        return
    table = doc.add_table(rows=len(rows), cols=2)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
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
            if ri == 0:
                set_cell_shading(cell, 'D9E2F3')
    return table


def add_data_table(doc, rows):
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
    text = '\n'.join(lines)
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
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
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:val="clear" w:fill="F5F5F5"/>')
    pPr.append(shd)
    run = p.add_run(text)
    run.font.name = 'Courier New'
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(0, 0, 0)
    return p


def add_diagram_image(doc, image_path, width=Inches(6)):
    if not os.path.exists(image_path):
        p = doc.add_paragraph(f'[Image not found: {image_path}]')
        return p
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    run.add_picture(image_path, width=width)
    return p


def process_file(doc, md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strip PlantUML but remember
    content = re.sub(r'```plantuml\s*\n.*?```', '<!-- PLANTUML_PLACEHOLDER -->', content, flags=re.DOTALL)

    lines = content.split('\n')
    i = 0
    current_table = []
    in_table = False
    is_scenario_table = False
    in_code_block = False
    code_lines = []
    skip_phase_heading = True  # Skip first H1/H2 phase heading per file

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # PlantUML placeholder — insert diagram
        if stripped == '<!-- PLANTUML_PLACEHOLDER -->':
            base = os.path.basename(md_file)
            img = None
            if 'iii' in base:
                img = 'output/diagrams/account_entity_class.png'
            elif 'iii.2' in base or ('iii' in base and 'entity' not in base and 'erd' not in base and 'mvc' not in base):
                # Check which section by content
                pass
            # Simple mapping by file
            if 'ii' in base and 'iii' not in base:
                img = None  # No diagram in phase II files from markdown
            elif 'iii' in base:
                # Will be determined by position
                pass
            i += 1
            continue

        # Code block
        if stripped.startswith('```'):
            if in_code_block:
                code_text = '\n'.join(code_lines)
                if code_text.strip():
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

        # Placeholder comment — insert diagram
        if 'PLACEHOLDER' in stripped:
            for key, path in DIAGRAM_MAP.items():
                if key in stripped:
                    add_diagram_image(doc, path)
                    break
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

        # Table separator
        if re.match(r'^\|[\s\-:|]+\|$', stripped):
            i += 1
            continue

        # Table row
        if stripped.startswith('|') and '|' in stripped[1:]:
            if not in_table:
                in_table = True
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
            # Skip first phase heading per file (already added by FILES list)
            if skip_phase_heading and level <= 1:
                skip_phase_heading = False
                i += 1
                continue
            skip_phase_heading = False
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

    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(11)

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
