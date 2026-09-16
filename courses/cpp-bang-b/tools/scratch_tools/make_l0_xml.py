import re
from pathlib import Path
import xml.etree.ElementTree as ET

import sys
sys.path.insert(0, '/Users/vu/.gemini/antigravity-ide/brain/3610f3da-8aad-4288-b82c-870385e11baf/scratch')
from generate_l0_problems import PROBLEMS

W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

def clean_latex(text: str) -> str:
    text = re.sub(r'\$([^\$]+)\$', r'\1', text)
    text = text.replace(r'\le', '≤').replace(r'\ge', '≥')
    text = text.replace(r'\ne', '≠').replace(r'\times', '×')
    text = text.replace(r'\dots', '...').replace(r'\text{s}', 's').replace(r'\text{MB}', 'MB')
    text = text.replace(r'\%', '%')
    return text

def format_problem_tag(code: str) -> str:
    parts = code.split('_')
    if len(parts) >= 3:
        return f"{parts[0].upper()}-{parts[1].upper()}-{parts[2]}"
    return code.upper().replace('_', '-')

def create_p(text: str, style: str = "BodyText", bold_prefix: str = None, space_before: int = 0, space_after: int = 60, line: int = 276):
    p = ET.Element(f"{{{W_NS}}}p")
    pPr = ET.SubElement(p, f"{{{W_NS}}}pPr")
    if style:
        pStyle = ET.SubElement(pPr, f"{{{W_NS}}}pStyle")
        pStyle.set(f"{{{W_NS}}}val", style)
    if space_before > 0 or space_after > 0:
        sp = ET.SubElement(pPr, f"{{{W_NS}}}spacing")
        if space_before > 0:
            sp.set(f"{{{W_NS}}}before", str(space_before))
        if space_after > 0:
            sp.set(f"{{{W_NS}}}after", str(space_after))
        sp.set(f"{{{W_NS}}}line", str(line))
        sp.set(f"{{{W_NS}}}lineRule", "auto")

    if bold_prefix:
        r_b = ET.SubElement(p, f"{{{W_NS}}}r")
        rPr_b = ET.SubElement(r_b, f"{{{W_NS}}}rPr")
        ET.SubElement(rPr_b, f"{{{W_NS}}}b")
        t_b = ET.SubElement(r_b, f"{{{W_NS}}}t")
        t_b.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t_b.text = bold_prefix

    if text:
        r_t = ET.SubElement(p, f"{{{W_NS}}}r")
        t_elem = ET.SubElement(r_t, f"{{{W_NS}}}t")
        t_elem.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t_elem.text = text
    return p

def create_heading3(text: str, space_before: int = 180, space_after: int = 60):
    p = ET.Element(f"{{{W_NS}}}p")
    pPr = ET.SubElement(p, f"{{{W_NS}}}pPr")
    pStyle = ET.SubElement(pPr, f"{{{W_NS}}}pStyle")
    pStyle.set(f"{{{W_NS}}}val", "Heading3")
    sp = ET.SubElement(pPr, f"{{{W_NS}}}spacing")
    sp.set(f"{{{W_NS}}}before", str(space_before))
    sp.set(f"{{{W_NS}}}after", str(space_after))
    sp.set(f"{{{W_NS}}}line", "276")
    sp.set(f"{{{W_NS}}}lineRule", "auto")

    r = ET.SubElement(p, f"{{{W_NS}}}r")
    rPr = ET.SubElement(r, f"{{{W_NS}}}rPr")
    ET.SubElement(rPr, f"{{{W_NS}}}b")
    col = ET.SubElement(rPr, f"{{{W_NS}}}color")
    col.set(f"{{{W_NS}}}val", "1E293B")
    sz = ET.SubElement(rPr, f"{{{W_NS}}}sz")
    sz.set(f"{{{W_NS}}}val", "26")

    t = ET.SubElement(r, f"{{{W_NS}}}t")
    t.text = text
    return p

def create_sample_table(input_lines: list, output_lines: list):
    tbl = ET.Element(f"{{{W_NS}}}tbl")
    tblPr = ET.SubElement(tbl, f"{{{W_NS}}}tblPr")
    tblStyle = ET.SubElement(tblPr, f"{{{W_NS}}}tblStyle")
    tblStyle.set(f"{{{W_NS}}}val", "Table")
    tblW = ET.SubElement(tblPr, f"{{{W_NS}}}tblW")
    tblW.set(f"{{{W_NS}}}w", "6800")
    tblW.set(f"{{{W_NS}}}type", "dxa")
    jc = ET.SubElement(tblPr, f"{{{W_NS}}}jc")
    jc.set(f"{{{W_NS}}}val", "center")

    tblBorders = ET.SubElement(tblPr, f"{{{W_NS}}}tblBorders")
    for b_name in ["top", "left", "bottom", "right"]:
        b = ET.SubElement(tblBorders, f"{{{W_NS}}}{b_name}")
        b.set(f"{{{W_NS}}}val", "single")
        b.set(f"{{{W_NS}}}sz", "4")
        b.set(f"{{{W_NS}}}space", "0")
        b.set(f"{{{W_NS}}}color", "CBD5E1")
    for b_name in ["insideH", "insideV"]:
        b = ET.SubElement(tblBorders, f"{{{W_NS}}}{b_name}")
        b.set(f"{{{W_NS}}}val", "single")
        b.set(f"{{{W_NS}}}sz", "4")
        b.set(f"{{{W_NS}}}space", "0")
        b.set(f"{{{W_NS}}}color", "E2E8F0")

    tblGrid = ET.SubElement(tbl, f"{{{W_NS}}}tblGrid")
    col1 = ET.SubElement(tblGrid, f"{{{W_NS}}}gridCol")
    col1.set(f"{{{W_NS}}}w", "3400")
    col2 = ET.SubElement(tblGrid, f"{{{W_NS}}}gridCol")
    col2.set(f"{{{W_NS}}}w", "3400")

    tr_h = ET.SubElement(tbl, f"{{{W_NS}}}tr")
    trPr_h = ET.SubElement(tr_h, f"{{{W_NS}}}trPr")
    ET.SubElement(trPr_h, f"{{{W_NS}}}cantSplit")
    jc_h = ET.SubElement(trPr_h, f"{{{W_NS}}}jc")
    jc_h.set(f"{{{W_NS}}}val", "center")

    for title in ["Đầu vào (Input)", "Đầu ra (Output)"]:
        tc = ET.SubElement(tr_h, f"{{{W_NS}}}tc")
        tcPr = ET.SubElement(tc, f"{{{W_NS}}}tcPr")
        tcW = ET.SubElement(tcPr, f"{{{W_NS}}}tcW")
        tcW.set(f"{{{W_NS}}}w", "3400")
        tcW.set(f"{{{W_NS}}}type", "dxa")
        shd = ET.SubElement(tcPr, f"{{{W_NS}}}shd")
        shd.set(f"{{{W_NS}}}val", "clear")
        shd.set(f"{{{W_NS}}}color", "auto")
        shd.set(f"{{{W_NS}}}fill", "F1F5F9")
        tcMar = ET.SubElement(tcPr, f"{{{W_NS}}}tcMar")
        for m_name, m_val in [("top", "40"), ("left", "60"), ("bottom", "40"), ("right", "60")]:
            m = ET.SubElement(tcMar, f"{{{W_NS}}}{m_name}")
            m.set(f"{{{W_NS}}}w", m_val)
            m.set(f"{{{W_NS}}}type", "dxa")
        vAlign = ET.SubElement(tcPr, f"{{{W_NS}}}vAlign")
        vAlign.set(f"{{{W_NS}}}val", "center")

        p = ET.SubElement(tc, f"{{{W_NS}}}p")
        pPr = ET.SubElement(p, f"{{{W_NS}}}pPr")
        pStyle = ET.SubElement(pPr, f"{{{W_NS}}}pStyle")
        pStyle.set(f"{{{W_NS}}}val", "Compact")
        ET.SubElement(pPr, f"{{{W_NS}}}keepNext")
        sp = ET.SubElement(pPr, f"{{{W_NS}}}spacing")
        sp.set(f"{{{W_NS}}}before", "60")
        sp.set(f"{{{W_NS}}}after", "60")
        sp.set(f"{{{W_NS}}}line", "276")
        sp.set(f"{{{W_NS}}}lineRule", "auto")
        jc_p = ET.SubElement(pPr, f"{{{W_NS}}}jc")
        jc_p.set(f"{{{W_NS}}}val", "center")

        r = ET.SubElement(p, f"{{{W_NS}}}r")
        rPr = ET.SubElement(r, f"{{{W_NS}}}rPr")
        rf = ET.SubElement(rPr, f"{{{W_NS}}}rFonts")
        rf.set(f"{{{W_NS}}}ascii", "Consolas")
        rf.set(f"{{{W_NS}}}hAnsi", "Consolas")
        ET.SubElement(rPr, f"{{{W_NS}}}b")
        sz = ET.SubElement(rPr, f"{{{W_NS}}}sz")
        sz.set(f"{{{W_NS}}}val", "22")
        t = ET.SubElement(r, f"{{{W_NS}}}t")
        t.text = title

    tr_d = ET.SubElement(tbl, f"{{{W_NS}}}tr")
    trPr_d = ET.SubElement(tr_d, f"{{{W_NS}}}trPr")
    ET.SubElement(trPr_d, f"{{{W_NS}}}cantSplit")
    jc_d = ET.SubElement(trPr_d, f"{{{W_NS}}}jc")
    jc_d.set(f"{{{W_NS}}}val", "center")

    def calc_indent(lines):
        max_l = max([len(l) for l in lines] + [1])
        if max_l <= 4:
            return 1440
        return max(200, int(1440 - (max_l - 4) * 65))

    in_indent = calc_indent(input_lines)
    out_indent = calc_indent(output_lines)

    for lines, indent_val in [(input_lines, in_indent), (output_lines, out_indent)]:
        tc = ET.SubElement(tr_d, f"{{{W_NS}}}tc")
        tcPr = ET.SubElement(tc, f"{{{W_NS}}}tcPr")
        tcW = ET.SubElement(tcPr, f"{{{W_NS}}}tcW")
        tcW.set(f"{{{W_NS}}}w", "3400")
        tcW.set(f"{{{W_NS}}}type", "dxa")
        shd = ET.SubElement(tcPr, f"{{{W_NS}}}shd")
        shd.set(f"{{{W_NS}}}val", "clear")
        shd.set(f"{{{W_NS}}}color", "auto")
        shd.set(f"{{{W_NS}}}fill", "FFFFFF")
        tcMar = ET.SubElement(tcPr, f"{{{W_NS}}}tcMar")
        for m_name, m_val in [("top", "40"), ("left", "60"), ("bottom", "40"), ("right", "60")]:
            m = ET.SubElement(tcMar, f"{{{W_NS}}}{m_name}")
            m.set(f"{{{W_NS}}}w", m_val)
            m.set(f"{{{W_NS}}}type", "dxa")
        vAlign = ET.SubElement(tcPr, f"{{{W_NS}}}vAlign")
        vAlign.set(f"{{{W_NS}}}val", "center")

        for line_str in lines:
            p = ET.SubElement(tc, f"{{{W_NS}}}p")
            pPr = ET.SubElement(p, f"{{{W_NS}}}pPr")
            pStyle = ET.SubElement(pPr, f"{{{W_NS}}}pStyle")
            pStyle.set(f"{{{W_NS}}}val", "Compact")
            sp = ET.SubElement(pPr, f"{{{W_NS}}}spacing")
            sp.set(f"{{{W_NS}}}before", "40")
            sp.set(f"{{{W_NS}}}after", "40")
            sp.set(f"{{{W_NS}}}line", "276")
            sp.set(f"{{{W_NS}}}lineRule", "auto")
            ind = ET.SubElement(pPr, f"{{{W_NS}}}ind")
            ind.set(f"{{{W_NS}}}left", str(indent_val))

            r = ET.SubElement(p, f"{{{W_NS}}}r")
            rPr = ET.SubElement(r, f"{{{W_NS}}}rPr")
            rf = ET.SubElement(rPr, f"{{{W_NS}}}rFonts")
            rf.set(f"{{{W_NS}}}ascii", "Consolas")
            rf.set(f"{{{W_NS}}}hAnsi", "Consolas")
            sz = ET.SubElement(rPr, f"{{{W_NS}}}sz")
            sz.set(f"{{{W_NS}}}val", "22")
            t = ET.SubElement(r, f"{{{W_NS}}}t")
            t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
            t.text = line_str

    return tbl

def parse_de_bai(code: str, num_str: str, title: str):
    p_path = Path(f"problems/{code}/De_Bai.md")
    content = p_path.read_text(encoding="utf-8")

    elements = []
    tag = format_problem_tag(code)
    h3_text = f"Bài {num_str} [{tag}]: {title}"
    elements.append(create_heading3(h3_text))

    def extract_sec(sec_title):
        m = re.search(rf"^## {sec_title}\s*\n(.*?)(?=^## |\Z)", content, re.M | re.S)
        return m.group(1).strip() if m else ""

    boi_canh = clean_latex(extract_sec("Bối cảnh"))
    nhiem_vu = clean_latex(extract_sec("Nhiệm vụ"))
    input_sec = clean_latex(extract_sec("Input"))
    output_sec = clean_latex(extract_sec("Output"))
    sample_sec = extract_sec("Sample 1")
    giai_thich_m = re.search(r"### Giải thích\s*\n(.*?)(?=^## |\Z)", content, re.M | re.S)
    giai_thich = clean_latex(giai_thich_m.group(1).strip() if giai_thich_m else "")
    rang_buoc = clean_latex(extract_sec("Ràng buộc"))

    elements.append(create_p(boi_canh, style="FirstParagraph", bold_prefix="Bối cảnh: "))
    elements.append(create_p(nhiem_vu, style="BodyText", bold_prefix="Nhiệm vụ: "))

    elements.append(create_p("", style="BodyText", bold_prefix="Đầu vào (Input):"))
    for l in input_sec.splitlines():
        l = l.strip().lstrip('- ').strip()
        if l:
            elements.append(create_p(l, style="Compact", space_before=20, space_after=30))

    elements.append(create_p("", style="FirstParagraph", bold_prefix="Đầu ra (Output):"))
    for l in output_sec.splitlines():
        l = l.strip().lstrip('- ').strip()
        if l:
            elements.append(create_p(l, style="Compact", space_before=20, space_after=30))

    elements.append(create_p("", style="FirstParagraph", bold_prefix="Ví dụ mẫu (Sample 1):"))

    in_m = re.search(r"### Input\s*```[a-z]*\n(.*?)```", sample_sec, re.S)
    out_m = re.search(r"### Output\s*```[a-z]*\n(.*?)```", sample_sec, re.S)
    in_lines = in_m.group(1).strip().splitlines() if in_m else [""]
    out_lines = out_m.group(1).strip().splitlines() if out_m else [""]
    elements.append(create_sample_table(in_lines, out_lines))

    if giai_thich:
        elements.append(create_p("", style="Compact", bold_prefix="Giải thích:"))
        for l in giai_thich.splitlines():
            l = l.strip()
            if l:
                elements.append(create_p(l, style="", space_before=20, space_after=40))

    elements.append(create_p("", style="BodyText", bold_prefix="Ràng buộc & Giới hạn:"))
    for l in rang_buoc.splitlines():
        l = l.strip().lstrip('- ').strip()
        if l:
            elements.append(create_p(l, style="Compact", space_before=20, space_after=30))

    return elements

def create_source_code_p(code_text: str):
    p = ET.Element(f"{{{W_NS}}}p")
    pPr = ET.SubElement(p, f"{{{W_NS}}}pPr")
    pStyle = ET.SubElement(pPr, f"{{{W_NS}}}pStyle")
    pStyle.set(f"{{{W_NS}}}val", "SourceCode")

    pBdr = ET.SubElement(pPr, f"{{{W_NS}}}pBdr")
    for side, col, sz, sp in [("top", "E2E8F0", "4", "2"), ("left", "CBD5E1", "8", "4"), ("bottom", "E2E8F0", "4", "2"), ("right", "E2E8F0", "4", "4")]:
        b = ET.SubElement(pBdr, f"{{{W_NS}}}{side}")
        b.set(f"{{{W_NS}}}val", "single")
        b.set(f"{{{W_NS}}}sz", sz)
        b.set(f"{{{W_NS}}}space", sp)
        b.set(f"{{{W_NS}}}color", col)

    shd = ET.SubElement(pPr, f"{{{W_NS}}}shd")
    shd.set(f"{{{W_NS}}}val", "clear")
    shd.set(f"{{{W_NS}}}color", "auto")
    shd.set(f"{{{W_NS}}}fill", "F8FAFC")

    sp = ET.SubElement(pPr, f"{{{W_NS}}}spacing")
    sp.set(f"{{{W_NS}}}before", "60")
    sp.set(f"{{{W_NS}}}after", "80")
    sp.set(f"{{{W_NS}}}line", "252")
    sp.set(f"{{{W_NS}}}lineRule", "auto")

    lines = code_text.strip().splitlines()
    for idx, line in enumerate(lines):
        r = ET.SubElement(p, f"{{{W_NS}}}r")
        rPr = ET.SubElement(r, f"{{{W_NS}}}rPr")
        rf = ET.SubElement(rPr, f"{{{W_NS}}}rFonts")
        rf.set(f"{{{W_NS}}}ascii", "Consolas")
        rf.set(f"{{{W_NS}}}hAnsi", "Consolas")
        sz = ET.SubElement(rPr, f"{{{W_NS}}}sz")
        sz.set(f"{{{W_NS}}}val", "18")
        col = ET.SubElement(rPr, f"{{{W_NS}}}color")
        col.set(f"{{{W_NS}}}val", "0F172A")

        t = ET.SubElement(r, f"{{{W_NS}}}t")
        t.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        t.text = line

        if idx < len(lines) - 1:
            r_br = ET.SubElement(p, f"{{{W_NS}}}r")
            rPr_br = ET.SubElement(r_br, f"{{{W_NS}}}rPr")
            rf_br = ET.SubElement(rPr_br, f"{{{W_NS}}}rFonts")
            rf_br.set(f"{{{W_NS}}}ascii", "Consolas")
            rf_br.set(f"{{{W_NS}}}hAnsi", "Consolas")
            ET.SubElement(r_br, f"{{{W_NS}}}br")

    return p
