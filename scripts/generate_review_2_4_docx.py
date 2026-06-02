"""Generate DOCX for section 2.4 review + tables 3.1 and 3.2 (XÁC ĐỊNH YÊU CẦU).

Heading/spacing mirrors the existing XÁC ĐỊNH YÊU CẦU tab style:
  H2 (N.N.)  : 13pt, #1F4E79 dark blue, spaceAbove=14pt, spaceBelow=8pt
  H3 (N.N.N.): 12pt, #1F4E79 dark blue, spaceAbove=10pt, spaceBelow=6pt
  Body        : 11pt, lineSpacing=1.25, spaceBelow=6pt
  UC bold     : 11pt bold, spaceAbove=8pt, spaceBelow=4pt
  Sub-label   : 11pt italic, spaceBelow=2pt
  Note        : 10pt italic, spaceBelow=4pt
"""
import os, re
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SCRIPT_DIR      = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR        = os.path.join(SCRIPT_DIR, '..')
INPUT_FILE      = os.path.join(ROOT_DIR, 'exports', 'xac-dinh-yeu-cau', 'review-2.4.md')
INPUT_FILE_3x   = os.path.join(ROOT_DIR, 'exports', 'xac-dinh-yeu-cau', 'review-3.1-3.2.md')
OUTPUT_FILE     = os.path.join(ROOT_DIR, 'output', 'review-2.4.docx')

DARK_BLUE = RGBColor(0x1F, 0x4E, 0x79)


def set_paragraph_spacing(para, space_before_pt=0, space_after_pt=6,
                           line_spacing=1.25):
    pPr = para._p.get_or_add_pPr()
    spb = OxmlElement('w:spacing')
    spb.set(qn('w:before'), str(int(space_before_pt * 20)))
    spb.set(qn('w:after'),  str(int(space_after_pt  * 20)))
    spb.set(qn('w:line'),   str(int(line_spacing * 240)))
    spb.set(qn('w:lineRule'), 'auto')
    pPr.append(spb)


def add_heading2(doc, text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(13)
    run.font.color.rgb = DARK_BLUE
    run.font.bold = False
    p.style = doc.styles['Heading 2']
    set_paragraph_spacing(p, space_before_pt=14, space_after_pt=8, line_spacing=1.0)
    return p


def add_heading3(doc, text):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(12)
    run.font.color.rgb = DARK_BLUE
    run.font.bold = False
    p.style = doc.styles['Heading 3']
    set_paragraph_spacing(p, space_before_pt=10, space_after_pt=6, line_spacing=1.0)
    return p


def add_uc_title(doc, text):
    """Bold UC title line, e.g. UC01 – Đăng nhập"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(11)
    run.font.bold = True
    set_paragraph_spacing(p, space_before_pt=10, space_after_pt=4, line_spacing=1.0)
    return p


def add_variant_label(doc, text):
    """Italic variant scenario name like *Đặt phòng trực tuyến:*"""
    p = doc.add_paragraph()
    label = text.strip().strip('*')
    run = p.add_run(label)
    run.font.size = Pt(11)
    run.font.italic = True
    set_paragraph_spacing(p, space_before_pt=6, space_after_pt=2, line_spacing=1.0)
    return p


def add_body(doc, text):
    p = doc.add_paragraph(text)
    p.style = doc.styles['Normal']
    for run in p.runs:
        run.font.size = Pt(11)
    set_paragraph_spacing(p, space_before_pt=0, space_after_pt=6, line_spacing=1.25)
    return p


def add_note(doc, text):
    """Italic note for ⚠️ lines"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.size = Pt(10)
    run.font.italic = True
    set_paragraph_spacing(p, space_before_pt=2, space_after_pt=4, line_spacing=1.0)
    return p


def is_blank(line):
    return line.strip() == ''


def is_comment(line):
    s = line.strip()
    return s.startswith('<!--') or s.startswith('-->')


def is_heading2(line):
    return line.startswith('## ')


def is_separator(line):
    return line.strip() == '---'


def is_uc_title(line):
    """**UC01 – ...** or **UC21 – ...**"""
    s = line.strip()
    return s.startswith('**UC') and s.endswith('**')


def is_variant_label(line):
    """*Variant label:* — italic scenario name like *Đặt phòng trực tuyến:*"""
    s = line.strip()
    return re.match(r'^\*.+\*$', s) is not None and not s.startswith('**')


def is_note(line):
    return line.strip().startswith('>')


def strip_bold(text):
    return text.strip().strip('*').strip()


def strip_italic(text):
    return text.strip().strip('*').strip(':').strip()


def parse_sublabel(text):
    s = text.strip()
    # *Luồng 1 — ...:*  →  Luồng 1 — ...:
    s = re.sub(r'^\*(.+)\*$', r'\1', s)
    return s


def parse_note(text):
    # > ⚠️ text  →  ⚠️ text
    return re.sub(r'^>\s*', '', text.strip())


def parse_md_table_rows(lines):
    """Parse markdown table lines (| col | col |) → list of row lists.
    Skips separator rows (|---|---|).
    """
    rows = []
    for ln in lines:
        s = ln.strip()
        if not s.startswith('|'):
            break
        if re.match(r'^\|[-| :]+\|$', s):
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        rows.append(cells)
    return rows


def add_md_table(doc, rows):
    """Render a list of row-lists as a DOCX table with header row styled."""
    if not rows:
        return
    ncols = max(len(r) for r in rows)
    tbl = doc.add_table(rows=len(rows), cols=ncols)
    tbl.style = 'Table Grid'

    # Column widths: distribute across ~6 inches page width
    col_width = Inches(6.0 / ncols)
    for col in tbl.columns:
        for cell in col.cells:
            cell.width = col_width

    for ri, row in enumerate(rows):
        for ci, cell_text in enumerate(row):
            cell = tbl.cell(ri, ci)
            p = cell.paragraphs[0]
            run = p.add_run(cell_text)
            run.font.size = Pt(10)
            if ri == 0:
                run.font.bold = True
            set_paragraph_spacing(p, space_before_pt=2, space_after_pt=2, line_spacing=1.0)

    # Space after table
    doc.add_paragraph()


def render_3x_file(doc, filepath):
    """Parse review-3.1-3.2.md and append its content to doc."""
    with open(filepath, encoding='utf-8') as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')
        s = line.strip()

        if not s or s.startswith('<!--') or s.startswith('-->') or s == '---':
            i += 1
            continue

        if line.startswith('## '):
            add_heading2(doc, line[3:].strip())
            i += 1
        elif line.startswith('### '):
            add_heading3(doc, line[4:].strip())
            i += 1
        elif s.startswith('|'):
            # Collect all table lines
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                table_lines.append(lines[i])
                i += 1
            rows = parse_md_table_rows(table_lines)
            add_md_table(doc, rows)
        else:
            if s:
                add_body(doc, s)
            i += 1


def main():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    doc = Document()

    # Set default Normal style font
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(11)

    with open(INPUT_FILE, encoding='utf-8') as f:
        lines = f.readlines()

    # Skip the HTML comment block at top (lines until closing -->)
    start = 0
    if lines and lines[0].strip().startswith('<!--'):
        for i, ln in enumerate(lines):
            if '-->' in ln:
                start = i + 1
                break

    # Also skip the final comment block
    end = len(lines)
    for i, ln in enumerate(lines):
        if ln.strip().startswith('<!-- ='):
            end = i
            break

    lines = lines[start:end]

    i = 0
    while i < len(lines):
        line = lines[i].rstrip('\n')

        if is_blank(line) or is_separator(line) or is_comment(line):
            i += 1
            continue

        if is_heading2(line):
            add_heading2(doc, line[3:].strip())
        elif is_uc_title(line):
            add_uc_title(doc, strip_bold(line))
        elif is_variant_label(line):
            add_variant_label(doc, line)
        elif is_note(line):
            add_note(doc, parse_note(line))
        else:
            text = line.strip()
            if text:
                add_body(doc, text)

        i += 1

    # ── Append section 3 (3.1 + 3.2 tables) ────────────────────────────────
    render_3x_file(doc, INPUT_FILE_3x)

    doc.save(OUTPUT_FILE)
    print(f'Saved: {OUTPUT_FILE}')

    # Quick verification
    from docx import Document as _Doc
    verify = _Doc(OUTPUT_FILE)
    paras = verify.paragraphs
    tables = verify.tables
    print(f'Paragraphs: {len(paras)}, Tables: {len(tables)}')
    if tables:
        for t in tables:
            print(f'  Table {len(t.rows)}r × {len(t.columns)}c — first cell: {t.cell(0,0).text!r}')


if __name__ == '__main__':
    main()
