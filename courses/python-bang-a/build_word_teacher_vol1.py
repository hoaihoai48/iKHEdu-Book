#!/usr/bin/env python3
"""
BUILD SCRIPT: Sách Giáo Viên Quyển 1 (Sách Lời Giải) - Khóa Học Python Cơ Bản iKHEDU
Nguồn manifest: courses/python-bang-a/word_build_manifest_gv.json
Output: courses/python-bang-a/python-giaovien-quyen-1.docx
Khuôn: courses/cpp-bang-b/c++-level-1-quyen-1.docx
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

REPO_ROOT = Path("/Users/vu/Developer/ikhEdu_lessons")
PYTHON_DIR = REPO_ROOT / "courses" / "python-bang-a"
TEMPLATE_DOCX = REPO_ROOT / "courses" / "cpp-bang-b" / "c++-level-1-quyen-1.docx"
MANIFEST_FILE = PYTHON_DIR / "word_build_manifest_gv.json"

CHAPTER_NAMES = {
    1: "CHƯƠNG 01: TÍNH TOÁN CƠ BẢN",
    2: "CHƯƠNG 02: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP",
}

def parse_de_bai(de_bai_path):
    """Parse De_Bai.md into structured sections without Ràng buộc."""
    with open(de_bai_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Match sections (exclude Ràng buộc)
    bcanh_m = re.search(r'## Bối cảnh\s*\n(.*?)(?=\n## Nhiệm vụ|\n## Input|\Z)', text, re.DOTALL)
    nv_m = re.search(r'## Nhiệm vụ\s*\n(.*?)(?=\n## Input|\n## Output|\Z)', text, re.DOTALL)
    inp_m = re.search(r'## Input\s*\n(.*?)(?=\n## Output|\n## Sample|\Z)', text, re.DOTALL)
    out_m = re.search(r'## Output\s*\n(.*?)(?=\n## Sample|\Z)', text, re.DOTALL)

    bcanh = bcanh_m.group(1).strip() if bcanh_m else ""
    nv = nv_m.group(1).strip() if nv_m else ""
    inp = inp_m.group(1).strip() if inp_m else ""
    out = out_m.group(1).strip() if out_m else ""

    # Parse Samples
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
    """Parse Huong_Dan_Giang_Day.md into 9 sections (Heading 4)."""
    with open(guide_path, "r", encoding="utf-8") as f:
        text = f.read()

    sections = []
    raw_secs = re.split(r'\n(?=##\s+\d+\.)', text)
    
    for raw in raw_secs:
        m = re.match(r'##\s+(\d+\.\s+[^\n]+)\n(.*)', raw.strip(), re.DOTALL)
        if m:
            sec_title = m.group(1).strip()
            sec_body = m.group(2).strip()
            # Clean forbidden phrasing "chuẩn thi đấu" in section title
            sec_title = re.sub(r'\s+Chuẩn Thi Đấu', '', sec_title, flags=re.IGNORECASE)
            sec_title = re.sub(r'\s+Thi Đấu', '', sec_title, flags=re.IGNORECASE)
            
            # Clean any trailing ---
            sec_body = re.sub(r'\n---\s*$', '', sec_body).strip()
            
            # Demote any internal H3 ### inside section body to H5 #####
            # to preserve H4 as the section level
            sec_body = re.sub(r'^(#{1,3})\s+', '##### ', sec_body, flags=re.MULTILINE)
            
            sections.append({
                "title": sec_title,
                "body": sec_body
            })

    return sections

def format_teacher_problem_markdown(prob_idx, prob_code, prob_title, parsed_de_bai, sol_code, parsed_guide):
    """Format full problem block for teacher book.
    Order: Statement -> Samples & Explanations -> Guide Sections (1. Ý tưởng, 2. Dry Run, 3. Bẫy lỗi) -> Code (4. Lời giải tham khảo)
    """
    md = []
    # 1. Heading 3: Bài NN [code]: Tên
    md.append(f"### Bài {prob_idx:02d} [{prob_code}]: {prob_title}\n\n")

    # 2. Bối cảnh
    if parsed_de_bai["bcanh"]:
        md.append(f"Bối cảnh: {parsed_de_bai['bcanh']}\n\n")

    # 3. Nhiệm vụ
    if parsed_de_bai["nv"]:
        md.append(f"Nhiệm vụ: {parsed_de_bai['nv']}\n\n")

    # 4. Input & Output
    if parsed_de_bai["inp"]:
        md.append(f"**Đầu vào (Input):**\n\n{parsed_de_bai['inp']}\n\n")

    if parsed_de_bai["out"]:
        md.append(f"**Đầu ra (Output):**\n\n{parsed_de_bai['out']}\n\n")

    # 5. Samples & Explanations
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

    # 6. Các mục Hướng dẫn giảng dạy (1. Ý tưởng & Phân tích, 2. Bảng chạy tay, 3. Lưu ý & Bẫy lỗi)
    # Lọc bỏ mục Lời giải tham khảo từ parsed_guide vì ta sẽ xuất 1 khối code chuẩn ở cuối
    for g_sec in parsed_guide:
        if "Lời giải tham khảo" in g_sec["title"]:
            continue
        md.append(f"#### {g_sec['title']}\n\n")
        md.append(f"{g_sec['body']}\n\n")

    # 7. Lời giải tham khảo (Khối code duy nhất, đặt ở cuối cùng của đề bài)
    md.append("#### 4. Lời giải tham khảo\n\n")
    md.append(f"```python\n{sol_code}\n```\n\n")

    return "".join(md)

def build_full_teacher_markdown(manifest_data):
    """Build complete Markdown string for Teacher Book Volume 1."""
    md_parts = []
    
    # Preface
    md_parts.append("# Lời nói đầu\n\n")
    md_parts.append(
        "Cuốn **Giáo trình Python — Sách giáo viên — Quyển 1** được biên soạn đồng bộ cùng bộ giáo trình lập trình "
        "Python cơ bản iKHEDU, dành riêng cho quý thầy cô giáo và các huấn luyện viên chuyên trách. "
        "Tài liệu này cung cấp toàn bộ lời giải chi tiết, chuẩn mực và hệ thống **hướng dẫn sư phạm thực chiến chuyên sâu** "
        "(ý tưởng và phân tích thuật toán, bảng mô phỏng chạy tay từng bước trên số liệu mẫu thực tế, lưu ý và các bẫy lỗi kinh điển thường gặp) "
        "cho toàn bộ **157 bài toán thực hành** thuộc Chương 01 và Chương 02.\n\n"
        "Mỗi bài toán trong sách đều được cấu trúc thống nhất từ đề bài học sinh, phân tích tư duy giải pháp, bảng theo dõi biến số trực quan "
        "đến mã nguồn tham khảo tối ưu nhất, giúp thầy cô dễ dàng tổ chức giờ học chất lượng cao và đồng hành hiệu quả cùng học sinh.\n\n"
    )

    current_chapter = None
    prob_count = 0
    guide_h4_count = 0

    for lesson_info in manifest_data["lessons"]:
        chap_num = lesson_info["chapter"]
        chap_title = CHAPTER_NAMES.get(chap_num, f"CHƯƠNG {chap_num:02d}")

        # If new chapter, emit Chapter H1
        if chap_num != current_chapter:
            current_chapter = chap_num
            md_parts.append(f"# {chap_title}\n\n")

        # Emit problems
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
            guide_h4_count += len(parsed_guide)

    # TOC marker
    md_parts.append("# Mục lục\n\n")

    print(f"  → Tổng số bài toán đã nạp: {prob_count} bài")
    print(f"  → Tổng số mục H4 guide đã nạp: {guide_h4_count} mục")

    return "".join(md_parts)

def convert_markdown_to_docx(full_md, intermediate_docx):
    """Convert markdown to docx using pandoc with reference-doc."""
    print(f"\n🔧 Đang chạy Pandoc chuyển đổi Markdown → DOCX...")
    intermediate_md = PYTHON_DIR / f"_build_intermediate_{intermediate_docx.stem}.md"
    with open(intermediate_md, "w", encoding="utf-8") as f:
        f.write(full_md)

    cmd = [
        "pandoc",
        str(intermediate_md),
        "-o", str(intermediate_docx),
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

    print(f"  ✅ Pandoc thành công: {intermediate_docx.name} ({intermediate_docx.stat().st_size:,} bytes)")
    return True

def postprocess_teacher_docx(docx_path, manifest_data):
    """Apply design standards, TOC hyperlinks, tables, code, headers, styles."""
    import docx
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls, qn

    header_book_text = manifest_data.get("header_book", "Giáo trình Python - Sách giáo viên - quyển 1")
    output_name = manifest_data.get("output", "python-giaovien-quyen-1.docx")

    print(f"\n🎨 Đang post-process chuyên sâu Design System cho {docx_path.name}...")
    doc = docx.Document(str(docx_path))

    # 1. Update Core Properties
    props = doc.core_properties
    props.title = "Giáo trình Python — Sách giáo viên — Quyển 1"
    props.author = "Trung tâm tin học iKH"

    # 2. Update Headers (Right side text)
    # Fix header rớt dòng: Tab Stop w:val="right" w:pos="9899"
    s = doc.sections[0]
    for h in [s.even_page_header, s.header, s.first_page_header]:
        p0 = h.paragraphs[0]
        pPr = p0._p.get_or_add_pPr()
        for tb in pPr.findall(qn("w:tabs")):
            pPr.remove(tb)
        pPr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab {nsdecls("w")} w:val="right" w:pos="9899"/></w:tabs>'))

        # Giữ lại các run chứa watermark pict
        watermark_runs = []
        for r in p0.runs:
            if r._r.find(qn("w:pict")) is not None:
                watermark_runs.append(r._r)

        # Xóa các run cũ
        for child in list(p0._p):
            if child.tag.split("}")[-1] != "pPr":
                p0._p.remove(child)

        # Chèn lại watermark shape
        for wr in watermark_runs:
            p0._p.append(wr)

        # Cấu trúc chuẩn: [Left text] + <w:tab/> + [Right text]
        r_left = parse_xml(f'''<w:r {nsdecls("w")}>
            <w:rPr>
                <w:rFonts w:cs="Times New Roman"/>
                <w:b/>
                <w:bCs/>
                <w:i/>
                <w:iCs/>
                <w:sz w:val="22"/>
                <w:szCs w:val="22"/>
            </w:rPr>
            <w:t>Trung tâm giáo dục &amp; đào tạo tin học iKH</w:t>
        </w:r>''')
        p0._p.append(r_left)

        r_tab = parse_xml(f'''<w:r {nsdecls("w")}>
            <w:rPr>
                <w:rFonts w:cs="Times New Roman"/>
                <w:sz w:val="22"/>
                <w:szCs w:val="22"/>
            </w:rPr>
            <w:tab/>
        </w:r>''')
        p0._p.append(r_tab)

        r_right = parse_xml(f'''<w:r {nsdecls("w")}>
            <w:rPr>
                <w:rFonts w:cs="Times New Roman"/>
                <w:i/>
                <w:iCs/>
                <w:noProof/>
                <w:sz w:val="22"/>
                <w:szCs w:val="22"/>
                <w:lang w:val="vi-VN"/>
            </w:rPr>
            <w:t>{html.escape(header_book_text)}</w:t>
        </w:r>''')
        p0._p.append(r_right)

    # 3. Apply Page Margins
    s.top_margin = Pt(36)
    s.bottom_margin = Pt(36)
    s.left_margin = Pt(64.35)  # gáy sách
    s.right_margin = Pt(36)

    # 4. Process Paragraphs & Headings
    toc_headings = []
    p_toc_heading = None
    first_chapter_done = False

    for idx, para in enumerate(doc.paragraphs):
        style_name = para.style.name if para.style else ""
        text = para.text.strip()

        # A. Heading 1
        if style_name == "Heading 1" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading1"):
            para.paragraph_format.keep_with_next = True
            is_chapter = "CHƯƠNG" in text.upper()
            is_preface = "LỜI NÓI ĐẦU" in text.upper()
            is_toc = "MỤC LỤC" in text.upper()

            if is_toc:
                p_toc_heading = para
                para.paragraph_format.page_break_before = True
                continue

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
            elif is_preface:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(6)
                para.paragraph_format.space_after = Pt(6)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            else:
                # Lesson H1
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(14)
                para.paragraph_format.space_after = Pt(4)
                # If it is the first lesson immediately following a Chapter heading, DO NOT break page
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

            # Add bookmark for TOC
            if not is_preface and text:
                bm_name = f"_toc_h1_{idx}"
                pPr = para._p.get_or_add_pPr()
                para._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{idx}" w:name="{bm_name}"/>'))
                para._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{idx}"/>'))
                toc_headings.append({
                    "text": text,
                    "bm_name": bm_name,
                    "level": 1,
                    "is_chapter": is_chapter,
                    "is_lesson": not is_chapter
                })

        # B. Heading 2
        elif style_name == "Heading 2" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading2"):
            para.paragraph_format.keep_with_next = True
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            para.paragraph_format.space_before = Pt(8)
            para.paragraph_format.space_after = Pt(4)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(16)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        # C. Heading 3: Từng đề bài (Bài NN [code]: Tên)
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

            # Bookmark for TOC
            if text:
                bm_name = f"_toc_h3_{idx}"
                pPr = para._p.get_or_add_pPr()
                para._p.insert(0, parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{idx}" w:name="{bm_name}"/>'))
                para._p.append(parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{idx}"/>'))
                toc_headings.append({
                    "text": text,
                    "bm_name": bm_name,
                    "level": 3,
                    "is_chapter": False,
                    "is_problem": True
                })

        # D. Heading 4: 9 Mục Hướng dẫn giảng dạy
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

        # E. Heading 5 (sub-items in guide)
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

        # F. Code Blocks (Source Code)
        elif style_name == "Source Code" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "SourceCode"):
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            pPr = para._p.get_or_add_pPr()

            # Remove any unwanted numbering
            for numPr in pPr.findall(qn("w:numPr")):
                pPr.remove(numPr)

            for r in para.runs:
                r.font.name = "Consolas"
                r.font.size = Pt(9.0)
                r.font.color.rgb = RGBColor(0x0F, 0x2A, 0x44)

            # Line spacing line=252 (1.05)
            sp = pPr.find(qn("w:spacing"))
            if sp is not None:
                sp.set(qn("w:before"), "20")
                sp.set(qn("w:after"), "20")
                sp.set(qn("w:line"), "252")
                sp.set(qn("w:lineRule"), "auto")
            else:
                pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="20" w:after="20" w:line="252" w:lineRule="auto"/>'))

            if pPr.find(qn("w:shd")) is None:
                pPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>'))
            if pPr.find(qn("w:pBdr")) is None:
                bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                    <w:left w:val="single" w:sz="6" w:space="4" w:color="E2E8F0"/>
                    <w:top w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                    <w:bottom w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                    <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
                </w:pBdr>''')
                pPr.append(bdr)
            if pPr.find(qn("w:ind")) is None:
                pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="180" w:right="120"/>'))

        # G. Callout / Block Text
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

        # H. Normal text & Preface content
        else:
            if idx <= 10:
                # Preface body: 14pt, 1.5 line spacing, Justify
                para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                para.paragraph_format.line_spacing = 1.5
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            else:
                # Check if "Giải thích:" -> align left
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

    # 5. Tables Processing
    sample_table_count = 0
    theory_table_count = 0

    # Ensure spacing before/after tables in document body
    body_element = doc._body._element
    for i, child in enumerate(body_element):
        if child.tag.split("}")[-1] == "tbl":
            # Check element immediately preceding the table
            prev_el = body_element[i - 1] if i > 0 else None
            if prev_el is not None and prev_el.tag.split("}")[-1] == "p":
                prev_pPr = prev_el.find(qn("w:pPr"))
                if prev_pPr is not None:
                    sp = prev_pPr.find(qn("w:spacing"))
                    if sp is not None:
                        curr_after = sp.attrib.get(qn("w:after"), None)
                        if curr_after is None or int(curr_after) < 120:
                            sp.set(qn("w:after"), "120")
                    else:
                        prev_pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:after="120"/>'))

            # Check element immediately following the table
            next_el = body_element[i + 1] if i + 1 < len(body_element) else None
            if next_el is not None and next_el.tag.split("}")[-1] == "p":
                next_pPr = next_el.find(qn("w:pPr"))
                if next_pPr is not None:
                    sp = next_pPr.find(qn("w:spacing"))
                    if sp is not None:
                        curr_before = sp.attrib.get(qn("w:before"), None)
                        if curr_before is None or int(curr_before) < 120:
                            sp.set(qn("w:before"), "120")
                    else:
                        next_pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="120"/>'))

    for table in doc.tables:
        table_tblPr = table._tbl.tblPr

        # Remove all tblHeader, ensure cantSplit
        for row in table.rows:
            trPr = row._tr.get_or_add_trPr()
            for h in trPr.findall(qn("w:tblHeader")):
                trPr.remove(h)
            if trPr.find(qn("w:cantSplit")) is None:
                trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

        # Sync Math in table to 12pt (sz val="24")
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

        # Check if Sample Table
        is_sample = False
        if len(table.rows) >= 2 and len(table.rows[0].cells) == 2:
            c0_t = table.rows[0].cells[0].text.strip()
            c1_t = table.rows[0].cells[1].text.strip()
            if ("Đầu vào" in c0_t or "Input" in c0_t) and ("Đầu ra" in c1_t or "Output" in c1_t):
                is_sample = True

        if is_sample:
            sample_table_count += 1
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

            # Row 0: Headers
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

            # Row 1+: Testcase data
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

                    # Process <br> into separate paragraphs
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

                    # Dynamic left indent
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
            # Guide / Dry Run Table
            theory_table_count += 1
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

    # 6. Build Interactive Hyperlinked TOC at End
    if p_toc_heading:
        print(f"  → Đang tạo Mục lục tương tác với {len(toc_headings)} liên kết...")
        last_elem = p_toc_heading._p

        for item in toc_headings:
            title = html.escape(item["text"])
            bm = item["bm_name"]

            if item.get("is_chapter"):
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:spacing w:before="180" w:after="40"/>
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
            elif item.get("is_problem"):
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:ind w:left="280"/>
                        <w:spacing w:before="20" w:after="20"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:sz w:val="21"/>
                                <w:color w:val="1E293B"/>
                            </w:rPr>
                            <w:t>{title}</w:t>
                        </w:r>
                    </w:hyperlink>
                </w:p>'''
            else:
                continue

            p_elem = parse_xml(p_xml)
            last_elem.addnext(p_elem)
            last_elem = p_elem

    # Save post-processed docx
    final_output = PYTHON_DIR / output_name
    doc.save(str(final_output))
    print(f"  ✅ Đã lưu file trung gian: {final_output.name} ({final_output.stat().st_size:,} bytes)")

    # 7. Clean package: remove orphan C++ media image1-12.png and their rels
    clean_docx_package(final_output)

    return final_output

def clean_docx_package(docx_path):
    """Remove template orphan C++ images (image1.png to image12.png) and clean document.xml.rels."""
    print(f"  🧹 Đang dọn dẹp package docx: loại bỏ ảnh thừa C++ (image1..12) và rels mồ côi...")
    temp_zip_path = docx_path.parent / f"_temp_clean_{docx_path.name}"
    with zipfile.ZipFile(docx_path, "r") as zin:
        with zipfile.ZipFile(temp_zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if any(item.filename == f"word/media/image{i}.png" for i in range(1, 13)):
                    continue
                data = zin.read(item.filename)
                if item.filename == "word/_rels/document.xml.rels":
                    text = data.decode("utf-8")
                    for i in range(1, 13):
                        text = re.sub(rf'<Relationship[^>]*Target="media/image{i}\.png"[^>]*/>', '', text)
                    data = text.encode("utf-8")
                elif item.filename == "word/styles.xml":
                    text = data.decode("utf-8")
                    # Replace teal 0F4761 in styles with 1E293B
                    text = text.replace('w:val="0F4761"', 'w:val="1E293B"')
                    # Remove themeColor/themeShade on those heading colors to avoid Office theme overriding
                    text = re.sub(r'w:color\s+w:themeColor="[^"]*"\s+w:themeShade="[^"]*"\s+w:val="1E293B"', 'w:color w:val="1E293B"', text)
                    data = text.encode("utf-8")
                zout.writestr(item, data)

    temp_zip_path.replace(docx_path)
    print(f"  ✅ Dọn dẹp hoàn tất: {docx_path.name} ({docx_path.stat().st_size:,} bytes)")

def update_docx_pages(docx_path):
    """Open docx in Word via AppleScript to paginate and save, updating docProps/app.xml."""
    print(f"  📄 Đang cập nhật số trang chuẩn xác qua Microsoft Word...")
    scpt = f'''
tell application "Microsoft Word"
    set doc to open file name POSIX file "{docx_path.resolve()}"
    delay 2
    save doc
    close doc
end tell
'''
    try:
        res = subprocess.run(["osascript", "-e", scpt], capture_output=True, text=True, timeout=30)
        if res.returncode == 0:
            print(f"  ✅ Microsoft Word đã cập nhật pagination thành công!")
        else:
            print(f"  ⚠️ AppleScript thông báo: {res.stderr.strip()}")
    except Exception as e:
        print(f"  ⚠️ Không thể gọi Microsoft Word (có thể do timeout): {e}")

def main():
    print("================================================================================")
    print("🚀 BẮT ĐẦU BUILD SÁCH GIÁO VIÊN QUYỂN 1 (SÁCH LỜI GIẢI PYTHON BẢNG A)")
    print("================================================================================")

    # 1. Load manifest
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    # 2. Build Markdown
    full_md = build_full_teacher_markdown(manifest_data)

    # 3. Convert to DOCX
    intermediate_docx = PYTHON_DIR / "_intermediate_teacher_vol1.docx"
    convert_markdown_to_docx(full_md, intermediate_docx)

    # 4. Post-process DOCX
    final_output = postprocess_teacher_docx(intermediate_docx, manifest_data)

    # 5. Clean intermediate docx
    if intermediate_docx.exists() and intermediate_docx != final_output:
        intermediate_docx.unlink()

    # 6. Update Word pagination
    update_docx_pages(final_output)

    print("\n================================================================================")
    print(f"🎉 HOÀN THÀNH XUẤT BẢN SÁCH GIÁO VIÊN QUYỂN 1: {final_output.name}")
    print(f"   Dung lượng: {final_output.stat().st_size:,} bytes")
    print("================================================================================")

if __name__ == "__main__":
    main()
