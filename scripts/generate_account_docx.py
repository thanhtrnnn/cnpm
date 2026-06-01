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
    # Phase I
    'account_uc_overview': 'output/diagrams/account_uc_overview.png',
    'account_uc_detail_login': 'output/diagrams/account_uc_detail_login.png',
    'account_uc_detail_register': 'output/diagrams/account_uc_detail_register.png',
    'account_uc_detail_changepw': 'output/diagrams/account_uc_detail_changepw.png',
    'account_uc_detail_profile': 'output/diagrams/account_uc_detail_profile.png',
    'account_uc_detail_staff': 'output/diagrams/account_uc_detail_staff.png',
    # Phase II — Analysis
    'account_entity_analysis': 'output/diagrams/account_entity_analysis.png',
    'account_class_analysis': 'output/diagrams/account_class_analysis.png',
    'account_seq_login_analysis': 'output/diagrams/account_seq_login_analysis.png',
    'account_seq_register_analysis': 'output/diagrams/account_seq_register_analysis.png',
    'account_seq_changepw_analysis': 'output/diagrams/account_seq_changepw_analysis.png',
    'account_seq_profile_analysis': 'output/diagrams/account_seq_profile_analysis.png',
    'account_seq_staff_analysis': 'output/diagrams/account_seq_staff_analysis.png',
    # Phase III — Design
    'account_entity_class': 'output/diagrams/account_entity_class.png',
    'account_erd': 'output/diagrams/account_erd.png',
    'account_dao_class': 'output/diagrams/account_mvc_class.png',
    'account_mvc_class': 'output/diagrams/account_mvc_class.png',
    'account_seq_login_design': 'output/diagrams/account_seq_login_design.png',
    'account_seq_register_design': 'output/diagrams/account_seq_register_design.png',
    'account_seq_changepw_design': 'output/diagrams/account_seq_changepw_design.png',
    'account_seq_profile_design': 'output/diagrams/account_seq_profile_design.png',
    'account_seq_staff_design': 'output/diagrams/account_seq_staff_design.png',
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


def parse_inline_html_table(text):
    """Extract <table>...</table> and return structured rows for native DOCX table."""
    import re as _re
    match = _re.search(r'<table>(.*?)</table>', text, _re.DOTALL)
    if not match:
        return text, []
    table_html = match.group(1)
    rows = []
    for tr_match in _re.finditer(r'<tr>(.*?)</tr>', table_html, _re.DOTALL):
        cells = []
        for td_match in _re.finditer(r'<t[dh]>(.*?)</t[dh]>', tr_match.group(1)):
            cells.append(td_match.group(1).strip())
        if cells:
            rows.append(cells)
    # Remove the <table>...</table> from text
    clean_text = text[:match.start()].rstrip() + text[match.end():].lstrip()
    return clean_text, rows


def add_native_table_in_cell(parent_cell, rows, header_row=True):
    """Add a native DOCX table inside a parent cell."""
    if not rows:
        return
    num_cols = max(len(r) for r in rows)
    # Calculate available width (parent cell is ~12cm, leave some margin)
    available_width = Cm(11)
    col_width = int(available_width / num_cols)
    # Create nested table
    nested = parent_cell.add_table(rows=len(rows), cols=num_cols)
    nested.style = 'Table Grid'
    nested.alignment = WD_TABLE_ALIGNMENT.CENTER
    for ri, row_data in enumerate(rows):
        for ci in range(num_cols):
            cell = nested.cell(ri, ci)
            cell.text = ''
            p = cell.paragraphs[0]
            cell_text = row_data[ci] if ci < len(row_data) else ''
            segments = extract_inline_formatting(cell_text)
            for seg_text, is_bold, is_code in segments:
                run = p.add_run(seg_text)
                run.font.size = Pt(9)
                if is_bold or (header_row and ri == 0):
                    run.bold = True
                if is_code:
                    run.font.name = 'Courier New'
                    run.font.size = Pt(8)
            # Set cell width
            cell.width = col_width
            # Header row shading
            if header_row and ri == 0:
                set_cell_shading(cell, 'D9E2F3')
            # Cell margins
            tc = cell._tc
            tcPr = tc.get_or_add_tcPr()
            tcMar = parse_xml(
                f'<w:tcMar {nsdecls("w")}>'
                '<w:top w:w="40" w:type="dxa"/>'
                '<w:bottom w:w="40" w:type="dxa"/>'
                '<w:left w:w="80" w:type="dxa"/>'
                '<w:right w:w="80" w:type="dxa"/>'
                '</w:tcMar>'
            )
            tcPr.append(tcMar)


def add_scenario_table(doc, rows):
    if not rows or len(rows[0]) < 2:
        return
    # Detect if first row is a generic header (Trường/Nội dung) vs old format (Use case/Actor)
    first_cell_lower = rows[0][0].lower().strip().replace('*', '')
    is_generic_header = first_cell_lower in ['trường', 'field']
    start_row = 1 if is_generic_header else 0
    data_rows = rows[start_row:]
    if not data_rows:
        return
    table = doc.add_table(rows=len(data_rows), cols=2)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for row in table.rows:
        row.cells[0].width = Cm(5)
        row.cells[1].width = Cm(12)
    for ri, row in enumerate(data_rows):
        for ci in range(2):
            cell = table.cell(ri, ci)
            cell.text = ''
            p = cell.paragraphs[0]
            p.style = doc.styles['Normal']
            cell_text = row[ci] if ci < len(row) else ''
            # Extract inline HTML tables
            clean_text, inline_rows = parse_inline_html_table(cell_text)
            parts = clean_text.split('<br>')
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
            # Add inline table as native DOCX table
            if inline_rows:
                add_native_table_in_cell(cell, inline_rows)
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
                is_scenario_table = (len(cells) == 2 and (
                    any(kw in cells[0].lower() for kw in ['use case', 'actor', 'tiền', 'hậu', 'kịch', 'ngoại'])
                    or cells[0].lower().strip() in ['trường', 'field']
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

        # Bullet (-, *, ▪, •, 🔹, ►)
        bm = re.match(r'^(\s*)[-*▪•🔹►]\s+(.+)$', line)
        if bm:
            indent = len(bm.group(1))
            text = bm.group(2).strip()
            level = min(indent // 2, 2)  # 0, 1, 2
            p = add_formatted_paragraph(doc, text, style='Normal')
            p.paragraph_format.left_indent = Pt(18 * (level + 1))
            p.paragraph_format.first_line_indent = Pt(-12)
            # Add bullet character
            first_run = p.runs[0] if p.runs else p.add_run('')
            first_run_text = first_run.text
            first_run.text = '•  ' + first_run_text if level == 0 else ('◦  ' + first_run_text if level == 1 else ('▪  ' + first_run_text))
            i += 1
            continue

        # Numbered list (1. 2. etc.)
        nm = re.match(r'^(\s*)\d+[.)]\s+(.+)$', line)
        if nm:
            indent = len(nm.group(1))
            text = nm.group(2).strip()
            level = min(indent // 2, 2)
            p = add_formatted_paragraph(doc, text, style='Normal')
            p.paragraph_format.left_indent = Pt(18 * (level + 1))
            p.paragraph_format.first_line_indent = Pt(-12)
            # Add number
            num_match = re.match(r'^(\d+[.)])\s', line.strip())
            if num_match:
                first_run = p.runs[0] if p.runs else p.add_run('')
                first_run.text = num_match.group(1) + '  ' + first_run.text
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

    # Add numbering config for bullets and numbered lists
    numbering_part = doc.part.numbering_part
    numbering_xml = numbering_part._element
    nsmap = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    # Bullet list definition
    from docx.oxml import OxmlElement
    abstract_num_bullet = OxmlElement('w:abstractNum')
    abstract_num_bullet.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}abstractNumId', '1')
    multi_level = OxmlElement('w:multiLevelType')
    multi_level.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'hybridMultilevel')
    abstract_num_bullet.append(multi_level)
    for lvl, (indent, hang) in enumerate([(360, 360), (720, 360), (1080, 360)]):
        level = OxmlElement('w:lvl')
        level.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ilvl', str(lvl))
        start = OxmlElement('w:start')
        start.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '1')
        level.append(start)
        num_fmt = OxmlElement('w:numFmt')
        num_fmt.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'bullet')
        level.append(num_fmt)
        level_text = OxmlElement('w:lvlText')
        level_text.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '•' if lvl == 0 else ('◦' if lvl == 1 else '▪'))
        level.append(level_text)
        pPr = OxmlElement('w:pPr')
        ind = OxmlElement('w:ind')
        ind.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}left', str(indent))
        ind.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hanging', str(hang))
        pPr.append(ind)
        level.append(pPr)
        if lvl == 0:
            rPr = OxmlElement('w:rPr')
            rFonts = OxmlElement('w:rFonts')
            rFonts.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hint', 'default')
            rPr.append(rFonts)
            level.append(rPr)
        abstract_num_bullet.append(level)
    numbering_xml.append(abstract_num_bullet)
    num_bullet = OxmlElement('w:num')
    num_bullet.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}numId', '1')
    abstract_ref = OxmlElement('w:abstractNumId')
    abstract_ref.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '1')
    num_bullet.append(abstract_ref)
    numbering_xml.append(num_bullet)

    # Numbered list definition
    abstract_num_num = OxmlElement('w:abstractNum')
    abstract_num_num.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}abstractNumId', '2')
    multi_level2 = OxmlElement('w:multiLevelType')
    multi_level2.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'hybridMultilevel')
    abstract_num_num.append(multi_level2)
    for lvl, (indent, hang) in enumerate([(360, 360), (720, 360), (1080, 360)]):
        level = OxmlElement('w:lvl')
        level.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}ilvl', str(lvl))
        start = OxmlElement('w:start')
        start.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '1')
        level.append(start)
        num_fmt = OxmlElement('w:numFmt')
        num_fmt.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', 'decimal')
        level.append(num_fmt)
        level_text = OxmlElement('w:lvlText')
        level_text.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', f'%{lvl+1}.')
        level.append(level_text)
        pPr = OxmlElement('w:pPr')
        ind = OxmlElement('w:ind')
        ind.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}left', str(indent))
        ind.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}hanging', str(hang))
        pPr.append(ind)
        level.append(pPr)
        abstract_num_num.append(level)
    numbering_xml.append(abstract_num_num)
    num_num = OxmlElement('w:num')
    num_num.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}numId', '2')
    abstract_ref2 = OxmlElement('w:abstractNumId')
    abstract_ref2.set('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val', '2')
    num_num.append(abstract_ref2)
    numbering_xml.append(num_num)

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
