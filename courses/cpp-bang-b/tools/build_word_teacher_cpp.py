#!/usr/bin/env python3
"""
BUILD SCRIPT: Sách Giáo Viên C++ (Teacher Solutions Book)
Tạo file Word cpp-giaovien-full.docx (323 bài toán, 21 bài học, 7 chương)
Chuẩn in ấn iKHEDU:
- Lời nói đầu trang 1 (không trang bìa), margin: Top 36pt, Bottom 36pt, Left 64.35pt, Right 36pt
- Watermark VML Logo chìm 100% trang (default, even, first)
- Heading 1: Chương (18pt Bold Center), Bài học (15.5pt Bold Left)
- Heading 3: Tên bài toán (14pt Bold Left)
- Heading 4: 4 mục sư phạm (13pt Bold Left)
- Bảng Sample IO: Dynamic Left Indent cho testcase ngắn/dài
- Khung Code: Consolas 9pt, line 1.05, nền #F8FAFC, viền #E2E8F0, căn trái 100%
- Mục lục: Tinh gọn 7 Chương + 21 Bài học với bookmark và leader dots.
"""

import os
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

BASE_DIR = Path(__file__).parent
PROBLEMS_DIR = BASE_DIR / "problems"
MANIFEST_FILE = BASE_DIR / "word_build_manifest_gv.json"
PREFACE_FILE = BASE_DIR / "reference" / "Loi_Noi_Dau_GV.md"
TEMPLATE_DOCX = BASE_DIR / "c++-level-1-quyen-1.docx"
OUT_DOCX = BASE_DIR / "cpp-giaovien-full.docx"

CHAPTER_NAMES = {
    1: "CHƯƠNG 01: THUẬT TOÁN SẮP XẾP & KỸ THUẬT MẢNG",
    2: "CHƯƠNG 02: MẢNG TIỀN TỐ & TÌM KIẾM NHỊ PHÂN",
    3: "CHƯƠNG 03: SỐ HỌC & ĐẠI SỐ MODULAR",
    4: "CHƯƠNG 04: ĐỆ QUY, CHIA ĐỂ TRỊ & QUAY LUI",
    5: "CHƯƠNG 05: QUY HOẠCH ĐỘNG (DYNAMIC PROGRAMMING)",
    6: "CHƯƠNG 06: CẤU TRÚC DỮ LIỆU NÂNG CAO",
    7: "CHƯƠNG 07: ĐỒ THỊ & CÂY TRUY VẤN ĐOẠN"
}

def parse_de_bai(de_bai_path):
    if not de_bai_path.exists():
        return {"bcanh": "", "nv": "", "inp": "", "out": "", "samples": []}
    text = de_bai_path.read_text(encoding="utf-8")

    bcanh_m = re.search(r'## Bối cảnh\s*\n(.*?)(?=\n## Nhiệm vụ|\n## Input|\Z)', text, re.DOTALL)
    nv_m = re.search(r'## Nhiệm vụ\s*\n(.*?)(?=\n## Input|\n## Output|\Z)', text, re.DOTALL)
    inp_m = re.search(r'## Input\s*\n(.*?)(?=\n## Output|\n## Sample|\Z)', text, re.DOTALL)
    out_m = re.search(r'## Output\s*\n(.*?)(?=\n## Sample|\n## Ràng buộc|\Z)', text, re.DOTALL)

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
    if not guide_path.exists():
        return []
    text = guide_path.read_text(encoding="utf-8")

    sections = []
    raw_secs = re.split(r'\n(?=##\s+\d+\.)', text)

    for raw in raw_secs:
        m = re.match(r'##\s+(\d+\.\s+[^\n]+)\n(.*)', raw.strip(), re.DOTALL)
        if m:
            sec_title = m.group(1).strip()
            sec_body = m.group(2).strip()
            sec_body = re.sub(r'\n---\s*$', '', sec_body).strip()
            sec_body = re.sub(r'^(#{1,3})\s+', '##### ', sec_body, flags=re.MULTILINE)
            sections.append({
                "title": sec_title,
                "body": sec_body
            })

    return sections

def format_teacher_problem_markdown(prob_idx, prob_code, prob_title, parsed_de_bai, sol_code, parsed_guide):
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
    md.append(f"```cpp\n{sol_code}\n```\n\n")

    return "".join(md)

def build_full_markdown(manifest_data):
    md_parts = []
    
    # Lời nói đầu
    preface_text = PREFACE_FILE.read_text(encoding="utf-8")
    md_parts.append(f"{preface_text}\n\n")

    current_chapter = None
    all_lessons = manifest_data["lessons"]
    prob_count = 0

    for lesson_info in all_lessons:
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
            de_bai_file = BASE_DIR / prob["de_bai"]
            sol_file = BASE_DIR / prob["solution"]
            guide_file = BASE_DIR / prob["guide"]

            parsed_de_bai = parse_de_bai(de_bai_file)
            sol_code = sol_file.read_text(encoding="utf-8").strip() if sol_file.exists() else ""
            parsed_guide = parse_guide(guide_file)

            p_md = format_teacher_problem_markdown(p_idx, prob_code, prob_title, parsed_de_bai, sol_code, parsed_guide)
            md_parts.append(p_md)
            prob_count += 1

    # Mục lục heading placeholder
    md_parts.append("# Mục lục\n\n")
    print(f"  → Tổng hợp Markdown hoàn tất: {len(all_lessons)} bài học, {prob_count} bài toán.")
    return "".join(md_parts)

def convert_markdown_to_docx(full_md, out_docx):
    print("🔧 Đang chạy Pandoc Markdown → DOCX...")
    intermediate_md = BASE_DIR / "_build_intermediate_gv.md"
    intermediate_md.write_text(full_md, encoding="utf-8")

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

def post_process_styling(doc, manifest_data):
    print("🎨 Áp dụng chuẩn thiết kế in ấn iKHEDU (Typography, Paragraphs, Code Blocks, Tables)...")
    
    # 1. Margins
    for s in doc.sections:
        s.top_margin = Pt(36.0)
        s.bottom_margin = Pt(36.0)
        s.left_margin = Pt(64.35)
        s.right_margin = Pt(36.0)

    # 2. Paragraphs & Headings
    bm_counter = 1000
    toc_bookmarks = []

    for idx, para in enumerate(doc.paragraphs):
        style_name = para.style.name if para.style else ""
        text = para.text.strip()

        # Heading 1: Chương hoặc Bài học hoặc Lời nói đầu hoặc Mục lục
        if style_name == "Heading 1" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading1"):
            para.paragraph_format.keep_with_next = True
            
            if "Lời nói đầu" in text:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after = Pt(14)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            elif "Mục lục" in text:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(14)
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            elif text.startswith("CHƯƠNG"):
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(6)
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

                bm_counter += 1
                bm_name = f"_toc_chap_{bm_counter}"
                para._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{bm_name}"/>'))
                para._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>'))
                toc_bookmarks.append({"type": "chapter", "text": text, "bm": bm_name})

            elif text.startswith("Bài ") and ":" in text:
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(14)
                para.paragraph_format.space_after = Pt(4)
                prev_text = doc.paragraphs[idx - 1].text.strip() if idx > 0 else ""
                if prev_text.startswith("CHƯƠNG"):
                    para.paragraph_format.page_break_before = False
                else:
                    para.paragraph_format.page_break_before = True

                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(15.5)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

                bm_counter += 1
                bm_name = f"_toc_les_{bm_counter}"
                para._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{bm_name}"/>'))
                para._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>'))
                toc_bookmarks.append({"type": "lesson", "text": text, "bm": bm_name})

        # Heading 3: Tên bài toán
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

        # Heading 4: 4 mục sư phạm
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

        # Source Code
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

        # Body Text / Normal
        elif style_name in ["Normal", "Body Text", "First Paragraph"]:
            para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            para.paragraph_format.line_spacing = 1.15
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    # 3. Tables styling & Dynamic Left Indent
    print("📊 Xử lý bảng dữ liệu (Dry Run, Sample IO, cantSplit, No tblHeader)...")
    for table in doc.tables:
        table_tblPr = table._tbl.tblPr
        for th in table_tblPr.findall(qn("w:tblHeader")):
            table_tblPr.remove(th)

        for row in table.rows:
            trPr = row._tr.get_or_add_trPr()
            if trPr.find(qn("w:cantSplit")) is None:
                trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        first_row_text = "".join(c.text for c in table.rows[0].cells).lower()
        is_sample_io = ("đầu vào" in first_row_text or "input" in first_row_text) and ("đầu ra" in first_row_text or "output" in first_row_text)

        if is_sample_io and len(table.columns) == 2:
            table_tblPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            for b in table_tblPr.findall(qn("w:tblBorders")): table_tblPr.remove(b)
            table_tblPr.append(parse_xml(f'''<w:tblBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                <w:insideV w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            </w:tblBorders>'''))

            for c_idx in range(2):
                table.rows[0].cells[c_idx].width = Inches(3.2)

            for cell in table.rows[0].cells:
                tcPr = cell._tc.get_or_add_tcPr()
                for s in tcPr.findall(qn("w:shd")): tcPr.remove(s)
                tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="1E293B"/>'))
                for tm in tcPr.findall(qn("w:tcMar")): tcPr.remove(tm)
                tcPr.append(parse_xml(f'''<w:tcMar {nsdecls("w")}>
                    <w:top w:w="80" w:type="dxa"/>
                    <w:left w:w="100" w:type="dxa"/>
                    <w:bottom w:w="80" w:type="dxa"/>
                    <w:right w:w="100" w:type="dxa"/>
                </w:tcMar>'''))
                for p in cell.paragraphs:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    for r in p.runs:
                        r.font.name = "Times New Roman"
                        r.font.size = Pt(12)
                        r.font.bold = True
                        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

            for row in table.rows[1:]:
                for cell in row.cells:
                    cell.width = Inches(3.2)
                    tcPr = cell._tc.get_or_add_tcPr()
                    for s in tcPr.findall(qn("w:shd")): tcPr.remove(s)
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>'))
                    for tm in tcPr.findall(qn("w:tcMar")): tcPr.remove(tm)
                    tcPr.append(parse_xml(f'''<w:tcMar {nsdecls("w")}>
                        <w:top w:w="60" w:type="dxa"/>
                        <w:left w:w="80" w:type="dxa"/>
                        <w:bottom w:w="60" w:type="dxa"/>
                        <w:right w:w="80" w:type="dxa"/>
                    </w:tcMar>'''))

                    full_cell_text = "\n".join(p.text for p in cell.paragraphs).strip()
                    lines = [l.strip() for l in re.split(r'<br\s*/?>|\n', full_cell_text) if l.strip()]
                    max_len = max([len(l) for l in lines]) if lines else 1
                    dyn_indent_pt = max(10.0, 72.0 - max(0, max_len - 4) * 3.25)
                    dyn_indent_dxa = int(dyn_indent_pt * 20)

                    for p in list(cell.paragraphs):
                        p_elem = p._p
                        p_parent = p_elem.getparent()
                        if p_parent is not None:
                            p_parent.remove(p_elem)

                    for line_str in lines:
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
            for b in table_tblPr.findall(qn("w:tblBorders")): table_tblPr.remove(b)
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

    # 4. Tạo Mục Lục Tinh Gọn (7 Chương + 21 Bài Học)
    print("📑 Tái tạo Mục lục tinh gọn (7 Chương + 21 Bài học)...")
    p_toc_heading = None
    for p in doc.paragraphs:
        if p.text.strip() == "Mục lục" and p.style.name == "Heading 1":
            p_toc_heading = p
            break

    if p_toc_heading:
        curr = p_toc_heading._p.getnext()
        while curr is not None:
            nxt = curr.getnext()
            if curr.tag.split('}')[-1] != 'sectPr':
                curr.getparent().remove(curr)
            curr = nxt

        for item in toc_bookmarks:
            is_chap = item["type"] == "chapter"
            bm = item["bm"]
            text_val = item["text"]

            p_entry = parse_xml(f'''<w:p {nsdecls("w")}>
                <w:pPr>
                    <w:pStyle w:val="Normal"/>
                    <w:tabs>
                        <w:tab w:val="right" w:leader="dot" w:pos="8900"/>
                    </w:tabs>
                    <w:spacing w:before="{'100' if is_chap else '30'}" w:after="{'40' if is_chap else '30'}" w:line="240" w:lineRule="auto"/>
                    <w:ind w:left="{'0' if is_chap else '300'}"/>
                </w:pPr>
                <w:hyperlink w:anchor="{bm}">
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                            <w:b {f'w:val="1"' if is_chap else 'w:val="0"'}/>
                            <w:sz w:val="{'24' if is_chap else '22'}"/>
                            <w:color w:val="{'1E293B' if is_chap else '334155'}"/>
                        </w:rPr>
                        <w:t>{html.escape(text_val)}</w:t>
                    </w:r>
                    <w:r>
                        <w:rPr>
                            <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                            <w:color w:val="94A3B8"/>
                        </w:rPr>
                        <w:tab/>
                    </w:r>
                    <w:fldSimple w:instr="PAGEREF {bm} \\h">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b {f'w:val="1"' if is_chap else 'w:val="0"'}/>
                                <w:sz w:val="{'24' if is_chap else '22'}"/>
                                <w:color w:val="{'1E293B' if is_chap else '334155'}"/>
                            </w:rPr>
                            <w:t>1</w:t>
                        </w:r>
                    </w:fldSimple>
                </w:hyperlink>
            </w:p>''')
            p_toc_heading._p.getparent().append(p_entry)

    # 5. Header: Sách giáo viên
    print("🏷️ Cập nhật Header: 'Giáo trình C++ — Sách giáo viên'...")
    for s in doc.sections:
        for name, h in [('header', s.header), ('first_header', s.first_page_header), ('even_header', s.even_page_header)]:
            for p in h.paragraphs:
                for r in p.runs:
                    if 'c++' in r.text.lower() or 'quyển' in r.text.lower():
                        r.text = "Giáo trình C++ — Sách giáo viên"

def main():
    print("🚀 Bắt đầu quá trình build Sách Giáo Viên C++ (Teacher Solutions Book)...")
    if not MANIFEST_FILE.exists():
        print(f"❌ Không tìm thấy file manifest: {MANIFEST_FILE}")
        sys.exit(1)

    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    # 1. Ghép Markdown
    full_md = build_full_markdown(manifest_data)

    # 2. Chạy Pandoc
    convert_markdown_to_docx(full_md, OUT_DOCX)

    # 3. Post-processing styling
    doc = docx.Document(str(OUT_DOCX))
    post_process_styling(doc, manifest_data)
    doc.save(str(OUT_DOCX))

    print(f"🎉 XUẤT BẢN THÀNH CÔNG: {OUT_DOCX.name} ({OUT_DOCX.stat().st_size:,} bytes)!")

if __name__ == "__main__":
    main()
