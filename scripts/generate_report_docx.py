"""Generate DOCX for BÁO CÁO (Phần I–V).

Sources: docs/tabs/report/phan-*.md
Output:  output/report.docx

Font:     Times New Roman throughout
Headings: TNR, bold, #1F4E79 (XÁC ĐỊNH YÊU CẦU style)
  # (PHẦN)  → 16pt
  ## (N.)   → 14pt
  ### (N.N.)→ 13pt
"""
import os
import re
from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_DIR   = os.path.join(SCRIPT_DIR, '..')
REPORT_DIR = os.path.join(REPO_DIR, 'docs', 'tabs', 'report')
OUTPUT_DIR = os.path.join(REPO_DIR, 'output')
OUTPUT_FILE = os.path.join(OUTPUT_DIR, 'report.docx')

# Full DIAGRAM_MAP — 105 entries mapping PLACEHOLDER keys to screenshot files
def _img(module, filename):
    return os.path.join(REPO_DIR, 'docs', 'tabs', 'exports', module, 'screenshots', filename)

DIAGRAM_MAP = {
    # ═══════════════════════════════════════════════════════════════════════════
    # MODULE 1: ACCOUNT (13 images)
    # ═══════════════════════════════════════════════════════════════════════════
    # Phase I — UC
    'account_uc_overview':   _img('account', 'image_01.png'),
    'account_uc_uc01':       _img('account', 'image_02.png'),
    'account_uc_uc02':       _img('account', 'image_03.png'),
    'account_uc_uc03':       _img('account', 'image_04.png'),
    'account_uc_uc04':       _img('account', 'image_05.png'),
    'account_uc_uc20':       _img('account', 'image_06.png'),
    # Phase II — Entity + BCE + Seq phân tích
    'account_entity':               _img('account', 'image_07.png'),
    'account_bce':                  _img('account', 'image_08.png'),
    'account_seq_analysis_uc01':    _img('account', 'image_09.png'),
    'account_seq_analysis_uc02':    _img('account', 'image_10.png'),
    'account_seq_analysis_uc03':    _img('account', 'image_11.png'),
    'account_seq_analysis_uc04':    _img('account', 'image_12.png'),
    'account_seq_analysis_uc20':    _img('account', 'image_13.png'),

    # ═══════════════════════════════════════════════════════════════════════════
    # MODULE 2: BOOKING (21 images)
    # ═══════════════════════════════════════════════════════════════════════════
    # Phase I — UC
    'booking_uc_overview':          _img('booking', 'image_01.png'),
    'booking_uc_datphong':          _img('booking', 'image_02.png'),
    'booking_uc_huyphong':          _img('booking', 'image_03.png'),
    'booking_uc_checkin':           _img('booking', 'image_04.png'),
    'booking_uc_checkout':          _img('booking', 'image_05.png'),
    # Phase II — Entity + BCE + Seq phân tích
    'booking_entity':                       _img('booking', 'image_06.png'),
    'booking_bce':                          _img('booking', 'image_07.png'),
    'booking_seq_analysis_datphong':        _img('booking', 'image_08.png'),
    'booking_seq_analysis_huyphong':        _img('booking', 'image_09.png'),
    'booking_seq_analysis_checkin':         _img('booking', 'image_10.png'),
    'booking_seq_analysis_checkout':        _img('booking', 'image_11.png'),
    # Phase III — Thiết kế
    'booking_design_entity':                _img('booking', 'image_12.png'),
    'booking_db':                           _img('booking', 'image_13.png'),
    'booking_design_class':                 _img('booking', 'image_14.png'),
    'booking_seq_design_datphong':          _img('booking', 'image_15.png'),
    'booking_seq_design_checkin':           _img('booking', 'image_16.png'),
    'booking_wireframe_01':                 _img('booking', 'image_17.png'),
    'booking_wireframe_02':                 _img('booking', 'image_18.png'),
    'booking_wireframe_03':                 _img('booking', 'image_19.png'),
    'booking_wireframe_04':                 _img('booking', 'image_20.png'),
    'booking_wireframe_05':                 _img('booking', 'image_21.png'),

    # ═══════════════════════════════════════════════════════════════════════════
    # MODULE 3: SERVICES (42 images)
    # ═══════════════════════════════════════════════════════════════════════════
    # Phase I — UC
    'services_uc_overview':         _img('services', 'image_01.png'),
    'services_uc_order':            _img('services', 'image_02.png'),
    'services_uc_baocao':           _img('services', 'image_03.png'),
    'services_uc_menu':             _img('services', 'image_04.png'),
    'services_uc_kho':              _img('services', 'image_05.png'),
    # Phase II — Entity + BCE + Seq phân tích
    'services_entity':                      _img('services', 'image_06.png'),
    'services_bce':                         _img('services', 'image_07.png'),
    'services_seq_analysis_order':          _img('services', 'image_08.png'),
    'services_seq_analysis_baocao':         _img('services', 'image_09.png'),
    'services_seq_analysis_menu':           _img('services', 'image_10.png'),
    'services_seq_analysis_kho':            _img('services', 'image_11.png'),
    # Phase III — Thiết kế
    'services_design_entity':               _img('services', 'image_12.png'),
    'services_db':                          _img('services', 'image_13.png'),
    'services_design_class_order':          _img('services', 'image_14.png'),
    'services_design_class_baocao':         _img('services', 'image_15.png'),
    'services_design_class_menu':           _img('services', 'image_16.png'),
    'services_design_class_kho':            _img('services', 'image_17.png'),
    'services_seq_design_order':            _img('services', 'image_18.png'),
    'services_seq_design_baocao':           _img('services', 'image_19.png'),
    'services_seq_design_menu':             _img('services', 'image_20.png'),
    'services_seq_design_kho':              _img('services', 'image_21.png'),
    'services_wireframe_01':                _img('services', 'image_22.png'),
    'services_wireframe_02':                _img('services', 'image_23.png'),
    'services_wireframe_03':                _img('services', 'image_24.png'),
    'services_wireframe_04':                _img('services', 'image_25.png'),
    'services_wireframe_05':                _img('services', 'image_26.png'),
    'services_wireframe_06':                _img('services', 'image_27.png'),
    'services_wireframe_07':                _img('services', 'image_28.png'),
    'services_wireframe_08':                _img('services', 'image_29.png'),
    'services_wireframe_09':                _img('services', 'image_30.png'),
    'services_wireframe_10':                _img('services', 'image_31.png'),
    'services_wireframe_11':                _img('services', 'image_32.png'),
    'services_wireframe_12':                _img('services', 'image_33.png'),
    'services_wireframe_13':                _img('services', 'image_34.png'),
    'services_wireframe_14':                _img('services', 'image_35.png'),
    'services_wireframe_15':                _img('services', 'image_36.png'),
    'services_wireframe_16':                _img('services', 'image_37.png'),
    'services_wireframe_17':                _img('services', 'image_38.png'),
    'services_wireframe_18':                _img('services', 'image_39.png'),
    'services_wireframe_19':                _img('services', 'image_40.png'),
    'services_wireframe_20':                _img('services', 'image_41.png'),
    'services_wireframe_21':                _img('services', 'image_42.png'),

    # ═══════════════════════════════════════════════════════════════════════════
    # MODULE 4: CORE (18 images)
    # ═══════════════════════════════════════════════════════════════════════════
    # Phase I — UC
    'core_uc_overview':             _img('core', 'image_01.png'),
    'core_uc_uc16':                 _img('core', 'image_02.png'),
    'core_uc_uc17':                 _img('core', 'image_03.png'),
    'core_uc_uc18':                 _img('core', 'image_04.png'),
    'core_uc_uc19':                 _img('core', 'image_05.png'),
    'core_uc_uc20':                 _img('core', 'image_06.png'),
    # Phase II — Entity + BCE + Seq phân tích
    'core_entity':                          _img('core', 'image_07.png'),
    'core_bce':                             _img('core', 'image_08.png'),
    'core_seq_analysis_uc16':               _img('core', 'image_09.png'),
    'core_seq_analysis_uc17':               _img('core', 'image_10.png'),
    'core_seq_analysis_uc18':               _img('core', 'image_11.png'),
    'core_seq_analysis_uc19':               _img('core', 'image_12.png'),
    'core_seq_analysis_uc20':               _img('core', 'image_13.png'),
    # Phase III — Thiết kế
    'core_design_entity':                   _img('core', 'image_14.png'),
    'core_db':                              _img('core', 'image_15.png'),
    'core_design_class':                    _img('core', 'image_16.png'),
    'core_wireframe_01':                    _img('core', 'image_17.png'),
    'core_wireframe_02':                    _img('core', 'image_18.png'),

    # ═══════════════════════════════════════════════════════════════════════════
    # MODULE 5: REPORT (11 images)
    # ═══════════════════════════════════════════════════════════════════════════
    # Phase I — UC
    'hr_uc_overview':               _img('report', 'image_01.png'),
    'hr_uc_nhanvien':               _img('report', 'image_02.png'),
    'hr_uc_baocao':                 _img('report', 'image_03.png'),
    'hr_uc_khachhang':              _img('report', 'image_04.png'),
    'hr_uc_tonghop':                _img('report', 'image_05.png'),
    # Phase II — Entity (no analysis seq images for this module)
    'hr_entity':                    _img('report', 'image_06.png'),
    # Phase III — Thiết kế
    'hr_bce':                       _img('report', 'image_07.png'),
    'hr_seq_design_nhanvien':       _img('report', 'image_08.png'),
    'hr_seq_design_baocao':         _img('report', 'image_09.png'),
    'hr_seq_design_khachhang':      _img('report', 'image_10.png'),
    'hr_seq_design_tonghop':        _img('report', 'image_11.png'),
}

# Markdown files to process in order
MD_FILES = [
    os.path.join(REPORT_DIR, 'phan-i-ii.md'),
    os.path.join(REPORT_DIR, 'phan-iii.md'),
    os.path.join(REPORT_DIR, 'phan-iv.md'),
    os.path.join(REPORT_DIR, 'phan-v.md'),
]

TNR = 'Times New Roman'
HEADING_COLOR = RGBColor(0x1F, 0x4E, 0x79)
HEADING_SIZES = {1: Pt(16), 2: Pt(14), 3: Pt(13), 4: Pt(12)}
BODY_SIZE = Pt(12)
TABLE_SIZE = Pt(11)


# ─── inline formatting ────────────────────────────────────────────────────────

def _parse_inline(text):
    """Return list of (text, bold, italic, code) segments."""
    segs = []
    i = 0
    buf = ''
    while i < len(text):
        # bold **
        if text[i:i+2] == '**':
            if buf:
                segs.append((buf, False, False, False))
                buf = ''
            j = text.find('**', i + 2)
            if j != -1:
                segs.append((text[i+2:j], True, False, False))
                i = j + 2
                continue
        # italic * (single, not **)
        elif text[i] == '*' and text[i:i+2] != '**':
            if buf:
                segs.append((buf, False, False, False))
                buf = ''
            j = text.find('*', i + 1)
            if j != -1 and text[j:j+2] != '**':
                segs.append((text[i+1:j], False, True, False))
                i = j + 1
                continue
        # code `
        elif text[i] == '`':
            if buf:
                segs.append((buf, False, False, False))
                buf = ''
            j = text.find('`', i + 1)
            if j != -1:
                segs.append((text[i+1:j], False, False, True))
                i = j + 1
                continue
        buf += text[i]
        i += 1
    if buf:
        segs.append((buf, False, False, False))
    return segs


def _apply_runs(p, text, size=BODY_SIZE):
    for seg, bold, italic, code in _parse_inline(text):
        run = p.add_run(seg)
        run.font.name = TNR
        run.font.size = size
        run.bold = bold
        run.italic = italic
        if code:
            run.font.name = 'Courier New'
            run.font.size = Pt(10)


# ─── block helpers ────────────────────────────────────────────────────────────

def add_heading(doc, text, level):
    p = doc.add_heading(level=level)
    size = HEADING_SIZES.get(level, Pt(12))
    for seg, bold, italic, code in _parse_inline(text):
        run = p.add_run(seg)
        run.font.name = TNR
        run.font.size = size
        run.font.bold = True
        run.font.color.rgb = HEADING_COLOR
        if italic:
            run.italic = True
        if code:
            run.font.name = 'Courier New'
    return p


def add_para(doc, text, size=BODY_SIZE):
    p = doc.add_paragraph()
    p.style = doc.styles['Normal']
    _apply_runs(p, text, size)
    return p


def _set_shading(cell, color):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def add_table(doc, rows):
    if not rows:
        return
    num_cols = max(len(r) for r in rows)
    tbl = doc.add_table(rows=len(rows), cols=num_cols)
    tbl.style = 'Table Grid'
    tbl.alignment = WD_TABLE_ALIGNMENT.LEFT
    for ri, row_data in enumerate(rows):
        for ci in range(num_cols):
            cell = tbl.cell(ri, ci)
            cell.text = ''
            p = cell.paragraphs[0]
            p.style = doc.styles['Normal']
            cell_text = row_data[ci] if ci < len(row_data) else ''
            _apply_runs(p, cell_text, TABLE_SIZE)
            if ri == 0:
                for run in p.runs:
                    run.bold = True
                _set_shading(cell, 'D9E2F3')
    return tbl


def _setup_bullets(doc):
    numbering_xml = doc.part.numbering_part._element
    W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    abst = OxmlElement('w:abstractNum')
    abst.set(W + 'abstractNumId', '1')
    ml = OxmlElement('w:multiLevelType')
    ml.set(W + 'val', 'hybridMultilevel')
    abst.append(ml)
    for idx, (left, hang) in enumerate([(360, 360), (720, 360), (1080, 360)]):
        lvl = OxmlElement('w:lvl')
        lvl.set(W + 'ilvl', str(idx))
        st = OxmlElement('w:start'); st.set(W + 'val', '1'); lvl.append(st)
        fmt = OxmlElement('w:numFmt'); fmt.set(W + 'val', 'bullet'); lvl.append(fmt)
        sym = '•' if idx == 0 else ('◦' if idx == 1 else '▪')
        lt = OxmlElement('w:lvlText'); lt.set(W + 'val', sym); lvl.append(lt)
        pPr = OxmlElement('w:pPr')
        ind = OxmlElement('w:ind')
        ind.set(W + 'left', str(left)); ind.set(W + 'hanging', str(hang))
        pPr.append(ind); lvl.append(pPr)
        abst.append(lvl)
    numbering_xml.append(abst)
    num = OxmlElement('w:num'); num.set(W + 'numId', '1')
    ref = OxmlElement('w:abstractNumId'); ref.set(W + 'val', '1')
    num.append(ref); numbering_xml.append(num)


def add_bullet(doc, text, level=0):
    p = add_para(doc, text)
    W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
    pPr = p._element.get_or_add_pPr()
    numPr = OxmlElement('w:numPr')
    ilvl = OxmlElement('w:ilvl'); ilvl.set(W + 'val', str(level)); numPr.append(ilvl)
    numId = OxmlElement('w:numId'); numId.set(W + 'val', '1'); numPr.append(numId)
    pPr.append(numPr)
    return p


# ─── markdown processor ───────────────────────────────────────────────────────

def process_md(doc, md_path):
    with open(md_path, encoding='utf-8') as f:
        lines = f.read().split('\n')

    i = 0
    in_table = False
    current_table = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # PLACEHOLDER comment → embed diagram image
        if stripped.startswith('<!--') and 'PLACEHOLDER' in stripped:
            m_ph = re.search(r'PLACEHOLDER:\s*(\S+)', stripped)
            if m_ph:
                key = m_ph.group(1).rstrip('-->')  .strip()
                img_path = DIAGRAM_MAP.get(key)
                if img_path and os.path.exists(img_path):
                    p = doc.add_paragraph()
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    run = p.add_run()
                    run.add_picture(img_path, width=Inches(5.5))
                else:
                    add_para(doc, f'[Biểu đồ: {key}]')
            i += 1
            continue

        # Other HTML comments — skip entirely
        if stripped.startswith('<!--'):
            i += 1
            continue

        # Horizontal rule --- (UC separators)
        if re.match(r'^-{3,}$', stripped):
            i += 1
            continue

        # Empty line
        if not stripped:
            if in_table and current_table:
                add_table(doc, current_table)
                current_table = []
                in_table = False
            i += 1
            continue

        # Table separator line |---|---|
        if re.match(r'^\|[\s\-:|]+\|$', stripped):
            i += 1
            continue

        # Table row
        if stripped.startswith('|') and stripped.endswith('|'):
            if not in_table:
                in_table = True
            cells = [c.strip() for c in stripped.split('|')[1:-1]]
            current_table.append(cells)
            i += 1
            continue

        # Flush pending table before non-table content
        if in_table and current_table:
            add_table(doc, current_table)
            current_table = []
            in_table = False

        # Heading  # / ## / ### / ####
        m = re.match(r'^(#{1,4})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            add_heading(doc, m.group(2).strip(), level)
            i += 1
            continue

        # Bullet  - text  (any indent level)
        bm = re.match(r'^(\s*)[-*]\s+(.+)$', line)
        if bm:
            level = min(len(bm.group(1)) // 2, 2)
            add_bullet(doc, bm.group(2).strip(), level)
            i += 1
            continue

        # Regular paragraph (includes **bold** standalone, italic labels, flow text)
        add_para(doc, stripped)
        i += 1

    # Flush any remaining table
    if in_table and current_table:
        add_table(doc, current_table)


# ─── main ─────────────────────────────────────────────────────────────────────

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    doc = Document()

    _setup_bullets(doc)

    # Global styles
    normal = doc.styles['Normal']
    normal.font.name = TNR
    normal.font.size = BODY_SIZE

    for lvl in range(1, 5):
        hs = doc.styles[f'Heading {lvl}']
        hs.font.name = TNR
        hs.font.size = HEADING_SIZES[lvl]
        hs.font.bold = True
        hs.font.color.rgb = HEADING_COLOR

    for md_path in MD_FILES:
        if not os.path.exists(md_path):
            print(f'SKIP (not found): {md_path}')
            continue
        print(f'Processing: {os.path.basename(md_path)}')
        process_md(doc, md_path)

    doc.save(OUTPUT_FILE)
    print(f'Saved: {OUTPUT_FILE}  ({os.path.getsize(OUTPUT_FILE):,} bytes)')


if __name__ == '__main__':
    main()
