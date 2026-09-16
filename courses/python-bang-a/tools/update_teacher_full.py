#!/usr/bin/env python3
"""
UPDATE SCRIPT: Nối Q2 (L07-L14, Chương 3-5) vào python-giaovien-quyen-1.docx 
để tạo python-giaovien-full.docx (287 bài, sách giáo viên hoàn chỉnh).
- Gắn đủ 12 hình ảnh bài học chuẩn trực quan.
- Mục lục tinh gọn, sang trọng: 5 Chương + 14 Bài học (vừa vặn 1 trang).
"""

import re
import sys
import json
import html
import shutil
import zipfile
import subprocess
from pathlib import Path

import docx
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls, qn

REPO_ROOT = Path("/Users/vu/Developer/ikhEdu_lessons")
PYTHON_DIR = REPO_ROOT / "courses" / "python-bang-a"
Q1_DOCX = PYTHON_DIR / "python-giaovien-quyen-1.docx"
FULL_DOCX = PYTHON_DIR / "python-giaovien-full.docx"
TEMPLATE_DOCX = REPO_ROOT / "courses" / "cpp-bang-b" / "c++-level-1-quyen-1.docx"
MANIFEST_FILE = PYTHON_DIR / "word_build_manifest_gv.json"
PREFACE_FILE = PYTHON_DIR / "reference" / "Loi_Noi_Dau_GV.md"

CHAPTER_NAMES = {
    1: "CHƯƠNG 01: TÍNH TOÁN CƠ BẢN",
    2: "CHƯƠNG 02: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP",
    3: "CHƯƠNG 03: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ",
    4: "CHƯƠNG 04: DANH SÁCH (LIST) & THỐNG KÊ",
    5: "CHƯƠNG 05: XỬ LÝ CHUỖI KÝ TỰ"
}

# Mapping problem codes to specific diagrams and captions
# Tự động nạp toàn bộ thư viện 190+ hình minh họa thuần bối cảnh (Pure Scenario Diagrams)
PROBLEM_IMAGES_MAP_FILE = PYTHON_DIR / "problem_diagrams_full_map.json"
if PROBLEM_IMAGES_MAP_FILE.exists():
    with open(PROBLEM_IMAGES_MAP_FILE, "r", encoding="utf-8") as f:
        PROBLEM_IMAGES_MAP = json.load(f)
else:
    PROBLEM_IMAGES_MAP = {}


def parse_de_bai(de_bai_path):
    """Parse De_Bai.md into structured sections without Ràng buộc."""
    with open(de_bai_path, "r", encoding="utf-8") as f:
        text = f.read()

    bcanh_m = re.search(r'## Bối cảnh\s*\n(.*?)(?=\n## Nhiệm vụ|\n## Input|\Z)', text, re.DOTALL)
    nv_m = re.search(r'## Nhiệm vụ\s*\n(.*?)(?=\n## Input|\n## Output|\Z)', text, re.DOTALL)
    inp_m = re.search(r'## Input\s*\n(.*?)(?=\n## Output|\n## Sample|\Z)', text, re.DOTALL)
    out_m = re.search(r'## Output\s*\n(.*?)(?=\n## Sample|\Z)', text, re.DOTALL)

    bcanh = bcanh_m.group(1).strip() if bcanh_m else ""
    nv = nv_m.group(1).strip() if nv_m else ""
    inp = inp_m.group(1).strip() if inp_m else ""
    out = out_m.group(1).strip() if out_m else ""

    samples = []
    sample_blocks = re.findall(r'## (Sample \d+)\s*\n(.*?)(?=\n## Sample \d+|\n## Ràng buộc|\Z)', text, re.DOTALL)
    for s_title, s_body in sample_blocks:
        sinp_m = re.search(r'### Input\s*```(?:text)?\n(.*?)```', s_body, re.DOTALL)
        sout_m = re.search(r'### Output\s*```(?:text)?\n(.*?)```', s_body, re.DOTALL)
        sexpl_m = re.search(r'### Giải thích\s*\n(.*)', s_body, re.DOTALL)

        sinp = sinp_m.group(1).strip() if sinp_m else ""
        sout = sout_m.group(1).strip() if sout_m else ""
        sexpl = sexpl_m.group(1).strip() if sexpl_m else ""

        samples.append({
            "title": s_title,
            "input": sinp,
            "output": sout,
            "explain": sexpl
        })

    return {
        "bcanh": bcanh,
        "nv": nv,
        "inp": inp,
        "out": out,
        "samples": samples
    }

def parse_guide(guide_path):
    """Parse Huong_Dan_Giang_Day.md into sections (Heading 4)."""
    with open(guide_path, "r", encoding="utf-8") as f:
        text = f.read()

    sections = []
    raw_secs = re.split(r'\n(?=##\s+\d+\.)', text)
    
    for raw in raw_secs:
        m = re.match(r'##\s+(\d+\.\s+[^\n]+)\n(.*)', raw.strip(), re.DOTALL)
        if m:
            sec_title = m.group(1).strip()
            sec_body = m.group(2).strip()
            sec_title = re.sub(r'\s+Chuẩn Thi Đấu', '', sec_title, flags=re.IGNORECASE)
            sec_title = re.sub(r'\s+Thi Đấu', '', sec_title, flags=re.IGNORECASE)
            sec_body = re.sub(r'\n---\s*$', '', sec_body).strip()
            sec_body = re.sub(r'^(#{1,3})\s+', '##### ', sec_body, flags=re.MULTILINE)
            sections.append({
                "title": sec_title,
                "body": sec_body
            })

    return sections

def format_teacher_problem_markdown(prob_idx, prob_code, prob_title, parsed_de_bai, sol_code, parsed_guide):
    """Format full problem block for teacher book."""
    md = []
    md.append(f"### Bài {prob_idx:02d} [{prob_code}]: {prob_title}\n\n")

    if parsed_de_bai["bcanh"]:
        md.append(f"Bối cảnh: {parsed_de_bai['bcanh']}\n\n")

    if parsed_de_bai["nv"]:
        md.append(f"Nhiệm vụ: {parsed_de_bai['nv']}\n\n")

    if parsed_de_bai["inp"]:
        md.append(f"**Đầu vào (Input):**\n\n{parsed_de_bai['inp']}\n\n")

    if parsed_de_bai["out"]:
        md.append(f"**Đầu ra (Output):**\n\n{parsed_de_bai['out']}\n\n")

    for s in parsed_de_bai["samples"]:
        s_title_str = f"Ví dụ mẫu ({s['title']}):"
        inp_str = s["input"].replace("\n", " <br> ")
        out_str = s["output"].replace("\n", " <br> ")

        md.append(f"**{s_title_str}**\n\n")
        md.append("| Đầu vào (Input) | Đầu ra (Output) |\n")
        md.append("| :--- | :--- |\n")
        md.append(f"| {inp_str} | {out_str} |\n\n")

        if s["explain"]:
            md.append(f"**Giải thích:** {s['explain']}\n\n")

    for g_sec in parsed_guide:
        if "Lời giải tham khảo" in g_sec["title"]:
            continue
        md.append(f"#### {g_sec['title']}\n\n")
        md.append(f"{g_sec['body']}\n\n")

    md.append("#### 4. Lời giải tham khảo\n\n")
    md.append(f"```python\n{sol_code}\n```\n\n")

    return "".join(md)

def build_q2_markdown(manifest_data):
    """Build Markdown string for Q2 (lessons 7-14, chapters 3-5). No images in markdown; images inserted cleanly via python-docx."""
    md_parts = []
    current_chapter = None
    q2_lessons = manifest_data["lessons"][6:]
    prob_count = 0
    guide_h4_count = 0

    for lesson_info in q2_lessons:
        chap_num = lesson_info["chapter"]
        chap_title = CHAPTER_NAMES.get(chap_num, f"CHƯƠNG {chap_num:02d}")
        lesson_title = lesson_info["title"]

        if chap_num != current_chapter:
            current_chapter = chap_num
            md_parts.append(f"# {chap_title}\n\n")

        md_parts.append(f"# {lesson_title}\n\n")

        for p_idx, prob in enumerate(lesson_info["problems"], 1):
            prob_code = prob["code"]
            prob_title = prob["title"]
            de_bai_file = PYTHON_DIR / prob["de_bai"]
            sol_file = PYTHON_DIR / prob["solution"]
            guide_file = PYTHON_DIR / prob["guide"]

            parsed_de_bai = parse_de_bai(de_bai_file)
            with open(sol_file, "r", encoding="utf-8") as sf:
                sol_code = sf.read().strip()
            parsed_guide = parse_guide(guide_file)

            p_md = format_teacher_problem_markdown(p_idx, prob_code, prob_title, parsed_de_bai, sol_code, parsed_guide)
            md_parts.append(p_md)
            prob_count += 1
            guide_h4_count += 4

    print(f"  → Q2 Markdown: {len(q2_lessons)} bài học, {prob_count} bài toán, {guide_h4_count} mục H4.")
    return "".join(md_parts)

def convert_q2_markdown_to_docx(full_md, out_docx):
    """Convert Q2 markdown to docx via pandoc."""
    print(f"🔧 Đang chạy Pandoc chuyển đổi Q2 Markdown → DOCX...")
    intermediate_md = PYTHON_DIR / f"_build_intermediate_q2.md"
    with open(intermediate_md, "w", encoding="utf-8") as f:
        f.write(full_md)

    cmd = [
        "pandoc",
        str(intermediate_md),
        "-o", str(out_docx),
        "--reference-doc", str(TEMPLATE_DOCX),
        "--from=markdown+tex_math_dollars+pipe_tables+fenced_code_blocks+yaml_metadata_block+header_attributes",
        "--to=docx",
        "--standalone",
        "--wrap=auto",
        "--columns=80"
    ]

    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"❌ Pandoc lỗi: {res.stderr}")
        sys.exit(1)

    print(f"  ✅ Pandoc thành công: {out_docx.name} ({out_docx.stat().st_size:,} bytes)")
    if intermediate_md.exists():
        intermediate_md.unlink()
    return True

def style_q2_doc(doc_q2, start_bm_idx=10000):
    """Apply design styles and create bookmarks on doc_q2."""
    bm_idx = start_bm_idx

    for idx, para in enumerate(doc_q2.paragraphs):
        style_name = para.style.name if para.style else ""
        text = para.text.strip()

        # Heading 1: Chapter or Lesson
        if style_name == "Heading 1" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading1"):
            para.paragraph_format.keep_with_next = True
            is_chapter = text.startswith("CHƯƠNG")

            if is_chapter:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(5)
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            else:
                # Lesson H1
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(14)
                para.paragraph_format.space_after = Pt(4)
                prev_text = doc_q2.paragraphs[idx - 1].text.strip() if idx > 0 else ""
                if prev_text.startswith("CHƯƠNG"):
                    para.paragraph_format.page_break_before = False
                else:
                    para.paragraph_format.page_break_before = True

                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(15.5)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

            # Bookmark
            if text:
                bm_name = f"_toc_h1_q2_{bm_idx}"
                bm_idx += 1
                para._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_idx}" w:name="{bm_name}"/>'))
                para._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_idx}"/>'))

        # Heading 3: Problem
        elif style_name == "Heading 3" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading3"):
            para.paragraph_format.keep_with_next = True
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            para.paragraph_format.space_before = Pt(10)
            para.paragraph_format.space_after = Pt(4)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(14)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        # Heading 4: Guide sections
        elif style_name == "Heading 4" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading4"):
            para.paragraph_format.keep_with_next = True
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            para.paragraph_format.space_before = Pt(6)
            para.paragraph_format.space_after = Pt(3)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        # Heading 5: Sub-items in guide
        elif style_name == "Heading 5" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading5"):
            para.paragraph_format.keep_with_next = True
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            para.paragraph_format.space_before = Pt(4)
            para.paragraph_format.space_after = Pt(2)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        # Code Blocks (Source Code)
        elif style_name == "Source Code" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "SourceCode"):
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            pPr = para._p.get_or_add_pPr()
            for numPr in pPr.findall(qn("w:numPr")):
                pPr.remove(numPr)
            for r in para.runs:
                r.font.name = "Consolas"
                r.font.size = Pt(9.0)
                r.font.color.rgb = RGBColor(0x0F, 0x2A, 0x44)

            sp = pPr.find(qn("w:spacing"))
            if sp is not None:
                sp.set(qn("w:before"), "20")
                sp.set(qn("w:after"), "20")
                sp.set(qn("w:line"), "252")
            else:
                pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="20" w:after="20" w:line="252" w:lineRule="auto"/>'))

            if pPr.find(qn("w:shd")) is None:
                pPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>'))
            if pPr.find(qn("w:pBdr")) is None:
                bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                    <w:left w:val="single" w:sz="6" w:space="4" w:color="CBD5E1"/>
                    <w:top w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                    <w:bottom w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                    <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
                </w:pBdr>''')
                pPr.append(bdr)
            if pPr.find(qn("w:ind")) is None:
                pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="180" w:right="120"/>'))

        # Callout / Block Text
        elif style_name in ["Block Text", "Quote"] or text.startswith(">"):
            pPr = para._p.get_or_add_pPr()
            if pPr.find(qn("w:shd")) is None:
                pPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="EFF6FF"/>'))
            if pPr.find(qn("w:pBdr")) is None:
                bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                    <w:left w:val="single" w:sz="16" w:space="4" w:color="3B82F6"/>
                    <w:top w:val="single" w:sz="4" w:space="3" w:color="E2E8F0"/>
                    <w:bottom w:val="single" w:sz="4" w:space="3" w:color="E2E8F0"/>
                    <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
                </w:pBdr>''')
                pPr.append(bdr)
            if pPr.find(qn("w:ind")) is None:
                pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="200" w:right="120"/>'))

            para.paragraph_format.space_before = Pt(3)
            para.paragraph_format.space_after = Pt(3)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)

        # Normal text & Body Text
        else:
            if text.startswith("Giải thích:") or text.startswith("**Giải thích:**"):
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            else:
                para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            para.paragraph_format.line_spacing = 1.15
            for r in para.runs:
                if not r.font.name:
                    r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    # Tables styling
    for table in doc_q2.tables:
        table_tblPr = table._tbl.tblPr

        for row in table.rows:
            trPr = row._tr.get_or_add_trPr()
            for h in trPr.findall(qn("w:tblHeader")):
                trPr.remove(h)
            if trPr.find(qn("w:cantSplit")) is None:
                trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        math_ns = "http://schemas.openxmlformats.org/officeDocument/2006/math"
        for mr in table._tbl.findall(".//{" + math_ns + "}r"):
            mr_rPr = mr.find(qn("w:rPr"))
            if mr_rPr is not None:
                for sz in mr_rPr.findall(qn("w:sz")):
                    sz.set(qn("w:val"), "24")
                for szCs in mr_rPr.findall(qn("w:szCs")):
                    szCs.set(qn("w:val"), "24")
            else:
                mr.insert(0, parse_xml(f'<w:rPr {nsdecls("w")}><w:sz {nsdecls("w")} w:val="24"/><w:szCs {nsdecls("w")} w:val="24"/></w:rPr>'))

        is_sample = False
        if len(table.rows) >= 2 and len(table.rows[0].cells) == 2:
            c0_t = table.rows[0].cells[0].text.strip()
            c1_t = table.rows[0].cells[1].text.strip()
            if ("Đầu vào" in c0_t or "Input" in c0_t) and ("Đầu ra" in c1_t or "Output" in c1_t):
                is_sample = True

        if is_sample:
            table_tblPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            tblW = table_tblPr.find(qn("w:tblW"))
            if tblW is not None:
                tblW.set(qn("w:w"), "6800")
                tblW.set(qn("w:type"), "dxa")
            else:
                table_tblPr.append(parse_xml(f'<w:tblW {nsdecls("w")} w:w="6800" w:type="dxa"/>'))

            for b in table_tblPr.findall(qn("w:tblBorders")):
                table_tblPr.remove(b)
            table_tblPr.append(parse_xml(f'''<w:tblBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                <w:insideV w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            </w:tblBorders>'''))

            for cell in table.rows[0].cells:
                tcPr = cell._tc.get_or_add_tcPr()
                for w in tcPr.findall(qn("w:tcW")): tcPr.remove(w)
                tcPr.append(parse_xml(f'<w:tcW {nsdecls("w")} w:w="3400" w:type="dxa"/>'))
                for s in tcPr.findall(qn("w:shd")): tcPr.remove(s)
                tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>'))
                for tm in tcPr.findall(qn("w:tcMar")): tcPr.remove(tm)
                tcPr.append(parse_xml(f'''<w:tcMar {nsdecls("w")}>
                    <w:top w:w="40" w:type="dxa"/>
                    <w:left w:w="60" w:type="dxa"/>
                    <w:bottom w:w="40" w:type="dxa"/>
                    <w:right w:w="60" w:type="dxa"/>
                </w:tcMar>'''))
                for va in tcPr.findall(qn("w:vAlign")): tcPr.remove(va)
                tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

                for p in cell.paragraphs:
                    pPr = p._p.get_or_add_pPr()
                    sp = pPr.find(qn("w:spacing"))
                    if sp is not None:
                        sp.set(qn("w:before"), "60")
                        sp.set(qn("w:after"), "60")
                        sp.set(qn("w:line"), "276")
                        sp.set(qn("w:lineRule"), "auto")
                    else:
                        pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="60" w:after="60" w:line="276" w:lineRule="auto"/>'))
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for r in p.runs:
                        r.font.name = "Consolas"
                        r.font.size = Pt(11)
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

            for r_idx in range(1, len(table.rows)):
                row = table.rows[r_idx]
                for cell in row.cells:
                    tcPr = cell._tc.get_or_add_tcPr()
                    for w in tcPr.findall(qn("w:tcW")): tcPr.remove(w)
                    tcPr.append(parse_xml(f'<w:tcW {nsdecls("w")} w:w="3400" w:type="dxa"/>'))
                    for s in tcPr.findall(qn("w:shd")): tcPr.remove(s)
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="FFFFFF"/>'))
                    for tm in tcPr.findall(qn("w:tcMar")): tcPr.remove(tm)
                    tcPr.append(parse_xml(f'''<w:tcMar {nsdecls("w")}>
                        <w:top w:w="40" w:type="dxa"/>
                        <w:left w:w="60" w:type="dxa"/>
                        <w:bottom w:w="40" w:type="dxa"/>
                        <w:right w:w="60" w:type="dxa"/>
                    </w:tcMar>'''))
                    for va in tcPr.findall(qn("w:vAlign")): tcPr.remove(va)
                    tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

                    orig_p_list = list(cell.paragraphs)
                    lines = []
                    for p in orig_p_list:
                        p_text = p.text
                        if "<br>" in p_text or "<br/>" in p_text or "&lt;br&gt;" in p_text:
                            sub = re.split(r'<br\s*/?>|&lt;br&gt;', p_text)
                            for s in sub:
                                s_clean = s.strip()
                                if s_clean:
                                    lines.append(s_clean)
                        else:
                            p_clean = p_text.strip()
                            if p_clean:
                                lines.append(p_clean)

                    if not lines:
                        lines = [""]

                    max_len = max(len(l) for l in lines) if lines else 0
                    if max_len <= 4:
                        dyn_indent_pt = 72.0
                    else:
                        dyn_indent_pt = max(10.0, 72.0 - (max_len - 4) * 3.25)
                    dyn_indent_dxa = int(round(dyn_indent_pt * 20))

                    for p in orig_p_list:
                        p_elem = p._p
                        p_parent = p_elem.getparent()
                        if p_parent is not None:
                            p_parent.remove(p_elem)

                    for line_idx, line_str in enumerate(lines):
                        new_p = parse_xml(f'''<w:p {nsdecls("w")}>
                            <w:pPr>
                                <w:jc w:val="left"/>
                                <w:ind w:left="{dyn_indent_dxa}"/>
                                <w:spacing w:before="30" w:after="30" w:line="240" w:lineRule="auto"/>
                            </w:pPr>
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="Consolas" w:hAnsi="Consolas"/>
                                    <w:sz w:val="19"/>
                                    <w:szCs w:val="19"/>
                                    <w:color w:val="0F2A44"/>
                                </w:rPr>
                                <w:t xml:space="preserve">{html.escape(line_str)}</w:t>
                            </w:r>
                        </w:p>''')
                        cell._tc.append(new_p)

        else:
            table_tblPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            for b in table_tblPr.findall(qn("w:tblBorders")):
                table_tblPr.remove(b)
            table_tblPr.append(parse_xml(f'''<w:tblBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                <w:insideV w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            </w:tblBorders>'''))

            for r_idx, row in enumerate(table.rows):
                for cell in row.cells:
                    tcPr = cell._tc.get_or_add_tcPr()
                    for tm in tcPr.findall(qn("w:tcMar")): tcPr.remove(tm)
                    tcPr.append(parse_xml(f'''<w:tcMar {nsdecls("w")}>
                        <w:top w:w="60" w:type="dxa"/>
                        <w:left w:w="80" w:type="dxa"/>
                        <w:bottom w:w="60" w:type="dxa"/>
                        <w:right w:w="80" w:type="dxa"/>
                    </w:tcMar>'''))
                    for va in tcPr.findall(qn("w:vAlign")): tcPr.remove(va)
                    tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

                    if r_idx == 0:
                        for s in tcPr.findall(qn("w:shd")): tcPr.remove(s)
                        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>'))
                        for p in cell.paragraphs:
                            pPr = p._p.get_or_add_pPr()
                            sp = pPr.find(qn("w:spacing"))
                            if sp is not None:
                                sp.set(qn("w:before"), "60")
                                sp.set(qn("w:after"), "60")
                                sp.set(qn("w:line"), "276")
                                sp.set(qn("w:lineRule"), "auto")
                            else:
                                pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="60" w:after="60" w:line="276" w:lineRule="auto"/>'))
                            for r in p.runs:
                                r.font.name = "Times New Roman"
                                r.font.size = Pt(12)
                                r.font.bold = True
                                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
                    else:
                        fill_c = "F8FAFC" if r_idx % 2 == 0 else "FFFFFF"
                        for s in tcPr.findall(qn("w:shd")): tcPr.remove(s)
                        tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_c}"/>'))
                        for p in cell.paragraphs:
                            pPr = p._p.get_or_add_pPr()
                            sp = pPr.find(qn("w:spacing"))
                            if sp is not None:
                                sp.set(qn("w:before"), "40")
                                sp.set(qn("w:after"), "40")
                                sp.set(qn("w:line"), "276")
                                sp.set(qn("w:lineRule"), "auto")
                            else:
                                pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="40" w:after="40" w:line="276" w:lineRule="auto"/>'))
                            for r in p.runs:
                                r.font.name = "Times New Roman"
                                r.font.size = Pt(12)
                                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

def insert_picture_with_caption(doc, img_filename, caption_text, target_p_elem):
    """Insert a centered picture paragraph and an italic caption before target_p_elem."""
    img_path = str(PYTHON_DIR / "assets_png" / img_filename)
    if not Path(img_path).exists():
        print(f"  ⚠️ Không tìm thấy file ảnh: {img_path}")
        return

    # 1. Paragraph chứa hình ảnh
    p_pic = doc.add_paragraph()
    p_pic.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_pic.paragraph_format.space_before = Pt(6)
    p_pic.paragraph_format.space_after = Pt(2)
    p_pic.paragraph_format.line_spacing = 1.0
    r_pic = p_pic.add_run()
    r_pic.add_picture(img_path, width=Inches(5.0))
    target_p_elem.addprevious(p_pic._p)

    # 2. Paragraph chứa chú thích hình ảnh (Caption)
    p_cap = doc.add_paragraph()
    p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap.paragraph_format.space_before = Pt(0)
    p_cap.paragraph_format.space_after = Pt(6)
    p_cap.paragraph_format.line_spacing = 1.0
    r_cap = p_cap.add_run(f"Hình minh họa: {caption_text}")
    r_cap.font.name = "Times New Roman"
    r_cap.font.size = Pt(10)
    r_cap.font.italic = True
    r_cap.font.color.rgb = RGBColor(0x47, 0x55, 0x69)
    target_p_elem.addprevious(p_cap._p)

def main():
    print("================================================================================")
    print("🚀 BẮT ĐẦU UPDATE SÁCH GIÁO VIÊN FULL (QUYỂN 1 + QUYỂN 2: 287 BÀI)")
    print("================================================================================")

    # 1. Load manifest & preface
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    with open(PREFACE_FILE, "r", encoding="utf-8") as f:
        preface_lines = f.read().split("\n")
    preface_paras = [line.strip() for line in preface_lines if line.strip() and not line.startswith("#")]

    # 2. Build Q2 markdown & convert to docx
    full_q2_md = build_q2_markdown(manifest_data)
    inter_q2_docx = PYTHON_DIR / "_inter_q2_raw.docx"
    convert_q2_markdown_to_docx(full_q2_md, inter_q2_docx)

    doc_q2 = docx.Document(str(inter_q2_docx))
    style_q2_doc(doc_q2, start_bm_idx=10000)
    doc_q2.save(str(inter_q2_docx))
    print(f"  ✅ Q2 docx post-processed.")

    # 3. Open Q1 docx (Read-only source)
    print(f"\n📖 Đang đọc {Q1_DOCX.name} để tiến hành sửa đổi và ghép nối...")
    doc = docx.Document(str(Q1_DOCX))

    # --- VIỆC 2: SỬA 2 CHỖ TRONG PHẦN Q1 ---
    print("\n✍️ Thực hiện VIỆC 2: Sửa 2 chỗ trong Q1...")
    if len(preface_paras) >= 2:
        p1 = doc.paragraphs[1]
        p1.text = preface_paras[0]
        p1.paragraph_format.line_spacing = 1.5
        p1.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p1.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(14)
            r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        p2 = doc.paragraphs[2]
        p2.text = preface_paras[1]
        p2.paragraph_format.line_spacing = 1.5
        p2.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        for r in p2.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(14)
            r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        print("  ✅ (a) Đã cập nhật Lời nói đầu verbatim theo Loi_Noi_Dau_GV.md")

    new_bcanh = "Bối cảnh: Trong giờ toán, cô giáo đố cả lớp một số N cực lớn lên tới 10^9 (1 tỷ). Bạn nào cũng tròn mắt ngạc nhiên. Nếu cộng từng số một từ 1 đến N thì máy tính phải làm tới 1 tỷ phép tính, chờ mãi không xong! Cả lớp đang loay hoay chưa biết làm sao cho nhanh. Hãy giúp cả lớp tìm cách tính thật nhanh."
    new_nv = "Nhiệm vụ: Hãy tính tổng S = 1 + 2 + … + N thật nhanh bằng công thức toán học."
    
    found_p14 = False
    for i, p in enumerate(doc.paragraphs):
        if 'pya_l07_p14' in p.text and p.style.name == 'Heading 3':
            p_bc = doc.paragraphs[i+1]
            p_nv = doc.paragraphs[i+2]
            p_bc.text = new_bcanh
            p_nv.text = new_nv
            p_bc.paragraph_format.line_spacing = 1.15
            p_bc.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p_bc.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            p_nv.paragraph_format.line_spacing = 1.15
            p_nv.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            for r in p_nv.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            found_p14 = True
            break
    if found_p14:
        print("  ✅ (b) Đã cập nhật Bối cảnh và Nhiệm vụ bài pya_l07_p14.")

    # --- VIỆC 3 (Header): Sửa Header phải thành "Giáo trình Python - Sách giáo viên" ---
    print("\n🏷️ Thực hiện VIỆC 3 (Header): Cập nhật Header phải cho cả 3 headers...")
    for s_idx, s in enumerate(doc.sections):
        for name, h in [('header', s.header), ('first_header', s.first_page_header), ('even_header', s.even_page_header)]:
            for p in h.paragraphs:
                for r in p.runs:
                    if 'quyển 1' in r.text.lower() or 'quyen 1' in r.text.lower():
                        r.text = "Giáo trình Python - Sách giáo viên"
                        print(f"  ✅ Đã sửa {name} run thành: 'Giáo trình Python - Sách giáo viên'")

    # --- VIỆC 1: NỐI NỘI DUNG Q2 VÀO TRƯỚC MỤC LỤC ---
    print("\n📦 Thực hiện VIỆC 1: Nối nội dung Q2 (L07-L14, Chương 3-5) vào trước Mục lục...")
    p_toc_heading = None
    for p in doc.paragraphs:
        if p.text.strip() == "Mục lục" and p.style.name == "Heading 1":
            p_toc_heading = p
            break

    if not p_toc_heading:
        print("❌ Không tìm thấy Heading 1 'Mục lục'!")
        sys.exit(1)

    # Dọn các dòng mục lục cũ phía sau Heading 'Mục lục' (bảo toàn sectPr ở cuối body)
    curr = p_toc_heading._p.getnext()
    removed_toc_count = 0
    while curr is not None:
        nxt = curr.getnext()
        if curr.tag.split('}')[-1] != 'sectPr':
            curr.getparent().remove(curr)
            removed_toc_count += 1
        curr = nxt
    print(f"  → Đã dọn {removed_toc_count} dòng mục lục cũ phía sau Heading 'Mục lục'.")

    # Chèn các element của doc_q2 vào ngay trước p_toc_heading._p
    q2_body_elements = list(doc_q2._body._element)
    insert_target = p_toc_heading._p

    inserted_elements_count = 0
    for elem in q2_body_elements:
        if elem.tag.split("}")[-1] == "sectPr":
            continue
        insert_target.addprevious(elem)
        inserted_elements_count += 1

    print(f"  ✅ Đã chèn thành công {inserted_elements_count} elements của Q2 vào trước Mục lục.")

    # --- GẮN CHUẨN 30 HÌNH ẢNH MINH HỌA TRỰC QUAN VÀO ĐÚNG BÀI TOÁN TƯƠNG ỨNG ---
    print(f"\n🖼️ Đang gắn trực quan {len(PROBLEM_IMAGES_MAP)} hình ảnh minh họa vào đúng từng bài toán tương ứng...")
    for prob_code, (img_filename, caption_text) in PROBLEM_IMAGES_MAP.items():
        # Find the Heading 3 paragraph for this problem
        h3_idx = None
        for i, p in enumerate(doc.paragraphs):
            if prob_code in p.text and p.style.name == "Heading 3":
                h3_idx = i
                break
        
        if h3_idx is None:
            print(f"  ⚠️ Không tìm thấy bài toán [{prob_code}]")
            continue

        # Find the 'Bối cảnh' paragraph following this Heading 3
        # We will insert the diagram immediately after Bối cảnh (or after Heading 3 if no Bối cảnh)
        target_p = None
        for j in range(h3_idx + 1, min(len(doc.paragraphs), h3_idx + 6)):
            p_curr = doc.paragraphs[j]
            if p_curr.style.name == "Heading 3":
                break
            if p_curr.text.strip().startswith("Bối cảnh:"):
                # Insert immediately after Bối cảnh: so target_elem is the next paragraph's element
                next_p = doc.paragraphs[j + 1] if j + 1 < len(doc.paragraphs) else p_curr
                target_p = next_p
                break

        if target_p is None:
            target_p = doc.paragraphs[h3_idx + 1] if h3_idx + 1 < len(doc.paragraphs) else doc.paragraphs[h3_idx]

        insert_picture_with_caption(doc, img_filename, caption_text, target_p._p)
        print(f"  → Đã gắn ảnh {img_filename} vào bài [{prob_code}]")

    # --- TÁI TẠO MỤC LỤC TINH GỌN (5 CHƯƠNG + 14 BÀI HỌC, VỪA VẶN 1 TRANG) ---
    print("\n📚 Đang tái tạo Mục lục tinh gọn (5 Chương + 14 Bài học)...")
    # Thu thập Chương và Bài học từ toàn bộ tài liệu
    toc_items = []
    current_chap_toc = None
    bm_counter = 50000

    # Lessons mapping from manifest
    all_lessons = manifest_data["lessons"]

    # We will build clean bookmarks for all 5 Chapters and 14 Lessons
    # 1. Identify paragraphs in doc corresponding to Chapter and Lesson headings
    for p in doc.paragraphs:
        style_name = p.style.name if p.style else ""
        text = p.text.strip()
        if style_name == "Heading 1":
            if text.startswith("CHƯƠNG"):
                bm_counter += 1
                bm_name = f"_toc_chap_{bm_counter}"
                p._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{bm_name}"/>'))
                p._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>'))
                toc_items.append({
                    "type": "chapter",
                    "text": text,
                    "bm": bm_name
                })
            elif text.startswith("Bài ") and ":" in text:
                bm_counter += 1
                bm_name = f"_toc_les_{bm_counter}"
                p._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{bm_name}"/>'))
                p._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>'))
                toc_items.append({
                    "type": "lesson",
                    "text": text,
                    "bm": bm_name
                })

    # If Q1 did not have explicit Lesson H1s, add Lesson TOC entries pointing to their first problem!
    # Let us verify if L1-L6 lessons are in toc_items
    existing_lesson_nums = set()
    for item in toc_items:
        if item["type"] == "lesson":
            m = re.search(r'Bài (\d+)', item["text"])
            if m:
                existing_lesson_nums.add(int(m.group(1)))

    print(f"  → Các bài học đã có tiêu đề H1 trong text: {sorted(existing_lesson_nums)}")
    
    # If L1-L6 are missing lesson H1s, let's create TOC items pointing to the first problem of each lesson!
    final_toc_entries = []
    # Build complete structure from manifest:
    current_c = None
    for l_info in all_lessons:
        c_num = l_info["chapter"]
        c_title = CHAPTER_NAMES[c_num]
        l_num = l_info["lesson"]
        l_title = l_info["title"]
        first_prob_code = l_info["problems"][0]["code"]

        if c_num != current_c:
            current_c = c_num
            # Find chapter bookmark
            c_bm = next((item["bm"] for item in toc_items if item["type"] == "chapter" and c_title in item["text"]), f"_toc_chap_{c_num}")
            final_toc_entries.append({
                "type": "chapter",
                "text": c_title,
                "bm": c_bm
            })

        # Find bookmark for this lesson (either lesson H1 or first problem)
        l_bm = next((item["bm"] for item in toc_items if item["type"] == "lesson" and f"Bài {l_num:02d}" in item["text"]), None)
        if not l_bm:
            # Find first problem paragraph to attach bookmark
            for p in doc.paragraphs:
                if first_prob_code in p.text and p.style.name == "Heading 3":
                    bm_counter += 1
                    l_bm = f"_toc_les_p_{bm_counter}"
                    p._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{l_bm}"/>'))
                    p._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>'))
                    break
        if not l_bm:
            l_bm = f"_toc_les_{l_num}"

        final_toc_entries.append({
            "type": "lesson",
            "text": l_title,
            "bm": l_bm
        })

    # Render TOC entries sau p_toc_heading._p
    last_elem = p_toc_heading._p
    for item in final_toc_entries:
        title = html.escape(item["text"])
        bm = item["bm"]

        if item["type"] == "chapter":
            p_xml = f'''<w:p {nsdecls("w")}>
                <w:pPr>
                    <w:spacing w:before="160" w:after="40"/>
                </w:pPr>
                <w:hyperlink w:anchor="{bm}">
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                            <w:b/>
                            <w:sz w:val="23"/>
                            <w:color w:val="0F2A44"/>
                        </w:rPr>
                        <w:t>{title}</w:t>
                    </w:r>
                </w:hyperlink>
            </w:p>'''
        else:
            p_xml = f'''<w:p {nsdecls("w")}>
                <w:pPr>
                    <w:ind w:left="280"/>
                    <w:spacing w:before="20" w:after="20"/>
                </w:pPr>
                <w:hyperlink w:anchor="{bm}">
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                            <w:sz w:val="22"/>
                            <w:color w:val="1A4A6B"/>
                        </w:rPr>
                        <w:t>•  {title}</w:t>
                    </w:r>
                </w:hyperlink>
            </w:p>'''

        p_elem = parse_xml(p_xml)
        last_elem.addnext(p_elem)
        last_elem = p_elem

    print(f"  ✅ Đã tạo Mục lục tinh gọn gồm {len(final_toc_entries)} mục (5 Chương + 14 Bài học).")

    # 5. Lưu file xuất bản python-giaovien-full.docx
    print(f"\n💾 Đang lưu file xuất bản: {FULL_DOCX.name}...")
    doc.save(str(FULL_DOCX))
    print(f"  ✅ Đã lưu {FULL_DOCX.name} ({FULL_DOCX.stat().st_size:,} bytes)")

    # Dọn dẹp file tạm
    if inter_q2_docx.exists():
        inter_q2_docx.unlink()

    # Dọn lock file ~$* nếu còn
    for lock_f in PYTHON_DIR.glob("~$*.docx"):
        try:
            lock_f.unlink()
            print(f"  🧹 Đã xóa lock file: {lock_f.name}")
        except Exception:
            pass

    # 6. Cập nhật số trang Microsoft Word
    update_docx_pages(FULL_DOCX)

def update_docx_pages(docx_path):
    """Open docx in Word via AppleScript to paginate and save."""
    print(f"  📄 Đang cập nhật số trang chuẩn xác qua Microsoft Word...")
    scpt = f'''
tell application "Microsoft Word"
    set doc to open file name POSIX file "{docx_path.resolve()}"
    delay 3
    save doc
    close doc
end tell
'''
    try:
        res = subprocess.run(["osascript", "-e", scpt], capture_output=True, text=True, timeout=40)
        if res.returncode == 0:
            print(f"  ✅ Microsoft Word đã cập nhật pagination thành công!")
        else:
            print(f"  ⚠️ AppleScript thông báo: {res.stderr.strip()}")
    except Exception as e:
        print(f"  ⚠️ Không thể gọi Microsoft Word: {e}")

if __name__ == "__main__":
    main()
