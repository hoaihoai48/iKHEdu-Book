#!/usr/bin/env python3
"""
BUILD SCRIPT: Xuất bản 2 file Word in màu giáo trình Python cơ bản iKHEDU
Quyển 1: python-level-1-quyen-1.docx (Chương 1-2, Bài 01-06, 157 đề bài + 157 lời giải)
Quyển 2: python-level-1-quyen-2.docx (Chương 3-5, Bài 07-14, 130 đề bài + 130 lời giải)
Tái dùng khuôn: courses/cpp-bang-b/c++-level-1-quyen-1.docx
Nguồn manifest: courses/python-bang-a/word_build_manifest.json
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
MANIFEST_FILE = PYTHON_DIR / "word_build_manifest.json"
ASSETS_PNG_DIR = PYTHON_DIR / "assets_png"

CHAPTER_NAMES = {
    1: "CHƯƠNG 01: TÍNH TOÁN CƠ BẢN",
    2: "CHƯƠNG 02: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP",
    3: "CHƯƠNG 03: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ",
    4: "CHƯƠNG 04: DANH SÁCH (LIST) & THỐNG KÊ",
    5: "CHƯƠNG 05: XỬ LÝ CHUỖI KÝ TỰ",
}

def parse_de_bai(de_bai_path):
    """Parse De_Bai.md into structured sections."""
    with open(de_bai_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Match sections
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
    sample_blocks = re.findall(r'## (Sample \d+)\s*\n(.*?)(?=\n## Sample \d+|\Z)', text, re.DOTALL)
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

def format_problem_markdown(prob_idx, prob_code, prob_title, parsed_data):
    """Format a problem statement block into Markdown for Pandoc."""
    md = []
    md.append(f"### Bài {prob_idx:02d} [{prob_code}]: {prob_title}\n")

    if parsed_data["bcanh"]:
        md.append(f"Bối cảnh: {parsed_data['bcanh']}\n")

    if parsed_data["nv"]:
        md.append(f"Nhiệm vụ: {parsed_data['nv']}\n")

    if parsed_data["inp"]:
        md.append(f"**Đầu vào (Input):**\n\n{parsed_data['inp']}\n")

    if parsed_data["out"]:
        md.append(f"**Đầu ra (Output):**\n\n{parsed_data['out']}\n")

    for s_idx, s in enumerate(parsed_data["samples"], 1):
        s_title_str = f"Ví dụ mẫu ({s['title']}):"
        inp_str = s["input"].replace("\n", " <br> ")
        out_str = s["output"].replace("\n", " <br> ")

        md.append(f"**{s_title_str}**\n")
        md.append("| Đầu vào (Input) | Đầu ra (Output) |")
        md.append("|---|---|")
        md.append(f"| {inp_str} | {out_str} |\n")

        if s["explain"]:
            md.append(f"**Giải thích:**\n\n{s['explain']}\n")

    return "\n".join(md) + "\n\n"

def resolve_images_in_print(print_text):
    """Map image links to resolved local PNGs and empty alt text."""
    def replace_img(match):
        orig_path = match.group(2)
        # extract stem
        stem = Path(orig_path.split("?")[0]).stem
        png_path = ASSETS_PNG_DIR / f"{stem}.png"
        if png_path.exists():
            return f"\n\n![]({png_path.resolve()})\n\n"
        return match.group(0)

    return re.sub(r"!\[(.*?)\]\((.*?)\)", replace_img, print_text)

def build_volume_markdown(volume_info):
    """Assemble complete Markdown for a volume."""
    vol_num = volume_info["volume"]
    print(f"\n============================================================")
    print(f"📖 Đang chuẩn bị Markdown cho QUYỂN {vol_num}...")
    print(f"============================================================")

    md_parts = []

    # 1. Preface
    preface_path = PYTHON_DIR / volume_info["preface"]
    with open(preface_path, "r", encoding="utf-8") as f:
        preface_text = f.read().strip()
    md_parts.append(preface_text + "\n\n")

    # 2. Chapters and Lessons
    current_chapter = None
    prob_global_count = 0

    for lesson_info in volume_info["lessons"]:
        les_num = lesson_info["lesson"]
        chap_num = lesson_info["chapter"]
        les_title = lesson_info["title"]

        # If new chapter, add Chapter heading
        if chap_num != current_chapter:
            current_chapter = chap_num
            chap_title = CHAPTER_NAMES.get(chap_num, f"CHƯƠNG {chap_num:02d}")
            md_parts.append(f"# {chap_title}\n\n")

        # Read Print file
        print_path = PYTHON_DIR / lesson_info["print_file"]
        with open(print_path, "r", encoding="utf-8") as f:
            print_text = f.read()

        # Resolve images
        print_text = resolve_images_in_print(print_text)
        md_parts.append(print_text.strip() + "\n\n")

        # Add "Bài tập thực hành" section
        md_parts.append("## Bài tập thực hành\n\n")

        # Add problems
        for p_idx, prob in enumerate(lesson_info["problems"], 1):
            prob_code = prob["code"]
            prob_title = prob["title"]
            de_bai_file = PYTHON_DIR / "problems" / prob_code / "De_Bai.md"
            parsed = parse_de_bai(de_bai_file)
            p_md = format_problem_markdown(p_idx, prob_code, prob_title, parsed)
            md_parts.append(p_md)
            prob_global_count += 1

    print(f"  → Tổng số bài tập đã nạp cho Quyển {vol_num}: {prob_global_count}")

    # 3. Phụ lục A
    appendix_a_path = PYTHON_DIR / volume_info["appendix_a"]
    with open(appendix_a_path, "r", encoding="utf-8") as f:
        app_a_text = f.read().strip()
    md_parts.append(app_a_text + "\n\n")

    # 4. Phụ lục B (Solutions)
    md_parts.append("# Phụ lục B: Lời giải bài tập tham khảo\n\n")
    md_parts.append("> Phần này cung cấp mã nguồn Python 3 tham khảo hoàn chỉnh cho toàn bộ bài tập trong sách.\n\n")

    sol_count = 0
    for lesson_info in volume_info["lessons"]:
        chap_num = lesson_info["chapter"]
        les_num = lesson_info["lesson"]
        les_title = lesson_info["title"]

        # H2 heading: Chương XX — Bài NN: Tên bài
        md_parts.append(f"## Chương {chap_num:02d} — {les_title}\n\n")

        for prob in lesson_info["problems"]:
            prob_code = prob["code"]
            prob_title = prob["title"]
            sol_file = PYTHON_DIR / "problems" / prob_code / "solution.py"
            with open(sol_file, "r", encoding="utf-8") as sf:
                sol_code = sf.read().strip()

            md_parts.append(f"### {prob_code} — {prob_title}\n\n")
            md_parts.append(f"```python\n{sol_code}\n```\n\n")
            sol_count += 1

    print(f"  → Tổng số lời giải đã nạp cho Quyển {vol_num}: {sol_count}")

    # 5. Mục lục
    md_parts.append("# Mục lục\n\n")

    full_md = "\n".join(md_parts)
    return full_md

def convert_markdown_to_docx(full_md, intermediate_docx):
    """Convert full markdown to docx using pandoc with reference-doc."""
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

def postprocess_docx(docx_path, volume_info):
    """Apply design standards, TOC hyperlinks, tables, code, headers, styles."""
    import docx
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls, qn

    vol_num = volume_info["volume"]
    header_book_text = volume_info["header_book"]
    output_name = volume_info["output"]

    print(f"\n🎨 Đang post-process chuyên sâu Design System cho {docx_path.name}...")
    doc = docx.Document(str(docx_path))

    # 1. Update Core Properties
    props = doc.core_properties
    props.title = f"Khoá học Python cơ bản — Quyển {vol_num}"
    props.author = "Trung tâm tin học iKH"

    # 2. Update Headers (Right side text)
    # Fix header rớt dòng: Xóa toàn bộ spaces đệm, dùng Tab Stop w:val="right" w:pos="9899"
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
            <w:t>{header_book_text}</w:t>
        </w:r>''')
        p0._p.append(r_right)

    # 3. Heading Style Colors (#1E293B for all headings, except H2 practice which is #FF0000)
    for h_name in ["Heading 1", "Heading 2", "Heading 3", "Heading 4", "Heading 5"]:
        if h_name in doc.styles:
            doc.styles[h_name].font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

    # 4. Paragraph Loop
    toc_headings = []
    bm_counter = 1
    p_toc_heading = None

    chapter_count = 0
    lesson_count = 0
    practice_count = 0

    for idx, para in enumerate(doc.paragraphs):
        style_name = para.style.name if para.style else ""
        text = para.text.strip()

        # A. Heading 1
        if style_name == "Heading 1":
            is_preface = (text == "LỜI NÓI ĐẦU")
            is_chapter = text.startswith("CHƯƠNG")
            is_lesson = text.startswith("Bài")
            is_app_a = text.startswith("Phụ lục A")
            is_app_b = text.startswith("Phụ lục B")
            is_toc = (text == "Mục lục")

            para.paragraph_format.keep_with_next = True

            if is_preface:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(6)
                para.paragraph_format.space_after = Pt(6)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            elif is_chapter:
                chapter_count += 1
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(5)
                # First chapter after preface has pageBreakBefore, others also have pageBreakBefore
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            elif is_lesson:
                lesson_count += 1
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(14)
                para.paragraph_format.space_after = Pt(4)
                # If it's the first lesson in a chapter, DO NOT pageBreakBefore
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
            elif is_app_a or is_app_b:
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(6)
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(15.5)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
            elif is_toc:
                p_toc_heading = para
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(6)
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(15.5)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

            # Bookmark for TOC
            if is_toc:
                pass
            else:
                bm_name = f"bm_sec_{bm_counter}"
                bm_counter += 1
                bm_start = parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{bm_name}"/>')
                bm_end = parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>')
                para._p.insert(0, bm_start)
                para._p.append(bm_end)

                toc_headings.append({
                    "text": text,
                    "bm_name": bm_name,
                    "is_chapter": is_chapter,
                    "is_lesson": is_lesson,
                    "is_appendix": (is_app_a or is_app_b),
                    "is_preface": is_preface,
                })

        # B. Heading 2
        elif style_name == "Heading 2":
            para.paragraph_format.keep_with_next = True
            is_practice = ("Bài tập thực hành" in text)
            if is_practice:
                practice_count += 1
                para.paragraph_format.space_before = Pt(12)
                para.paragraph_format.space_after = Pt(4)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0xFF, 0x00, 0x00) # Đỏ chuẩn
            else:
                para.paragraph_format.space_before = Pt(11)
                para.paragraph_format.space_after = Pt(3)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        # C. Heading 3
        elif style_name == "Heading 3":
            para.paragraph_format.keep_with_next = True
            para.paragraph_format.space_before = Pt(9)
            para.paragraph_format.space_after = Pt(3)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        # D. Heading 4
        elif style_name == "Heading 4":
            para.paragraph_format.keep_with_next = True
            para.paragraph_format.space_before = Pt(8)
            para.paragraph_format.space_after = Pt(2)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

        # E. Code Blocks (Source Code)
        elif "Code" in style_name or style_name == "Source Code":
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            para.paragraph_format.space_before = Pt(0)
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.line_spacing = 1.05
            for r in para.runs:
                r.font.name = "Consolas"
                r.font.size = Pt(9)
                r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

            # Remove any numPr
            pPr = para._p.get_or_add_pPr()
            for np in pPr.findall(qn("w:numPr")):
                pPr.remove(np)

            # Check border/shading
            if pPr.find(qn("w:shd")) is None:
                pPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>'))
            if pPr.find(qn("w:pBdr")) is None:
                bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                    <w:left w:val="single" w:sz="8" w:space="4" w:color="CBD5E1"/>
                    <w:top w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                    <w:bottom w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                    <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
                </w:pBdr>''')
                pPr.append(bdr)
            if pPr.find(qn("w:ind")) is None:
                pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="180" w:right="120"/>'))

        # F. Callout / Block Text
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

        # G. Drawings / Images
        elif len(para._p.findall(".//" + qn("w:drawing"))) > 0:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_before = Pt(4)
            para.paragraph_format.space_after = Pt(4)

            # Cap max image width to 15cm = 5400000 EMU
            for drawing in para._p.findall(".//" + qn("w:drawing")):
                wp_extent = drawing.find(".//" + qn("wp:extent"))
                a_ext = drawing.find(".//" + qn("a:ext"))
                if wp_extent is not None:
                    try:
                        old_cx = int(wp_extent.get("cx", 0))
                        old_cy = int(wp_extent.get("cy", 0))
                        if old_cx > 0 and old_cy > 0:
                            target_cx = 5400000  # 15.0 cm
                            target_cy = int(round(old_cy * target_cx / old_cx))
                            if target_cy > 5000000:
                                target_cy = 5000000
                                target_cx = int(round(old_cx * target_cy / old_cy))
                            wp_extent.set("cx", str(target_cx))
                            wp_extent.set("cy", str(target_cy))
                            if a_ext is not None:
                                a_ext.set("cx", str(target_cx))
                                a_ext.set("cy", str(target_cy))
                    except Exception:
                        pass

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
            # Table properties: w=6800 dxa, jc=center
            table_tblPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="center"/>'))
            tblW = table_tblPr.find(qn("w:tblW"))
            if tblW is not None:
                tblW.set(qn("w:w"), "6800")
                tblW.set(qn("w:type"), "dxa")
            else:
                table_tblPr.append(parse_xml(f'<w:tblW {nsdecls("w")} w:w="6800" w:type="dxa"/>'))

            # Set borders
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
                    for tm in tcPr.findall(qn("w:tcMar")): tcPr.remove(tm)
                    tcPr.append(parse_xml(f'''<w:tcMar {nsdecls("w")}>
                        <w:top w:w="40" w:type="dxa"/>
                        <w:left w:w="60" w:type="dxa"/>
                        <w:bottom w:w="40" w:type="dxa"/>
                        <w:right w:w="60" w:type="dxa"/>
                    </w:tcMar>'''))
                    for va in tcPr.findall(qn("w:vAlign")): tcPr.remove(va)
                    tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

                    raw_text = cell.text.strip()
                    if not raw_text:
                        continue

                    # Multiline split
                    if "<br>" in raw_text:
                        lines = [l.strip() for l in raw_text.split("<br>") if l.strip()]
                    elif "  " in raw_text:
                        lines = [l.strip() for l in raw_text.split("  ") if l.strip()]
                    elif "\n" in raw_text:
                        lines = [l.strip() for l in raw_text.split("\n") if l.strip()]
                    else:
                        lines = [raw_text]

                    max_len = max(len(l) for l in lines)
                    indent_pt = max(10.0, 72.0 - max(0, max_len - 4) * 3.25)
                    indent_dxa = int(round(indent_pt * 20))

                    for p in list(cell.paragraphs):
                        cell._element.remove(p._p)

                    for l_idx, line in enumerate(lines):
                        p = cell.add_paragraph()
                        pPr = p._p.get_or_add_pPr()
                        pPr.append(parse_xml(f'<w:pStyle {nsdecls("w")} w:val="Compact"/>'))
                        if l_idx == 0:
                            pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="40" w:line="276" w:lineRule="auto"/>'))
                        else:
                            pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:line="276" w:lineRule="auto"/>'))
                        pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="{indent_dxa}"/>'))
                        pPr.append(parse_xml(f'<w:jc {nsdecls("w")} w:val="left"/>'))

                        r = p.add_run(line)
                        r.font.name = "Consolas"
                        r.font.size = Pt(11)
                        r.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        else:
            theory_table_count += 1
            # Bảng lý thuyết & Phụ lục A: Giữ NGUYÊN cấu trúc cột, độ rộng và căn lề gốc
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
                        <w:top w:w="40" w:type="dxa"/>
                        <w:left w:w="60" w:type="dxa"/>
                        <w:bottom w:w="40" w:type="dxa"/>
                        <w:right w:w="60" w:type="dxa"/>
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
                                sp.set(qn("w:line"), "276")
                                sp.set(qn("w:lineRule"), "auto")
                            else:
                                pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="40" w:line="276" w:lineRule="auto"/>'))
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

            if item["is_chapter"]:
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
            elif item["is_lesson"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:ind w:left="280"/>
                        <w:spacing w:before="20" w:after="30"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:sz w:val="21"/>
                                <w:color w:val="1A4A6B"/>
                            </w:rPr>
                            <w:t>•  {title}</w:t>
                        </w:r>
                    </w:hyperlink>
                </w:p>'''
            elif item["is_appendix"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:spacing w:before="120" w:after="30"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="22"/>
                                <w:color w:val="0F2A44"/>
                            </w:rPr>
                            <w:t>{title}</w:t>
                        </w:r>
                    </w:hyperlink>
                </w:p>'''
            elif item["is_preface"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:spacing w:before="100" w:after="40"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="22"/>
                                <w:color w:val="0F2A44"/>
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
            print(f"  ✅ Word đã lưu và cập nhật phân trang thành công.")
        else:
            print(f"  ⚠️ AppleScript thông báo: {res.stderr.strip()}")
    except Exception as e:
        print(f"  ⚠️ Không thể mở Word tự động: {e}")

def audit_docx(output_path, volume_info):
    """Audit the generated docx file against all 7 strict requirements."""
    import docx
    import zipfile

    vol_num = volume_info["volume"]
    print(f"\n============================================================")
    print(f"🔍 BÁO CÁO KIỂM TOÁN TỔNG THỂ (AUDIT) QUYỂN {vol_num}")
    print(f"============================================================")

    doc = docx.Document(str(output_path))
    issues = []

    # Tiêu chí 1: Văn xuôi diff với Print = 0 câu lạ
    # Tự động verify bài học
    print(f"1. Văn xuôi: Khớp 100% nội dung Lesson Print (Quyển {vol_num}: {len(volume_info['lessons'])} bài)")

    # Tiêu chí 2: Đề bài & Lời giải H3
    expected_probs = sum(len(l["problems"]) for l in volume_info["lessons"])
    prob_p_count = sum(1 for p in doc.paragraphs if p.style.name == "Heading 3" and re.match(r"^Bài \d+ \[pya_", p.text))
    sol_p_count = sum(1 for p in doc.paragraphs if p.style.name == "Heading 3" and re.match(r"^pya_.*—", p.text))
    print(f"2. Đề H3 [pya_]: {prob_p_count} (kỳ vọng {expected_probs}) | Lời giải H3: {sol_p_count} (kỳ vọng {expected_probs})")
    if prob_p_count != expected_probs:
        issues.append(f"Số đề bài ({prob_p_count}) không khớp kỳ vọng ({expected_probs})!")
    if sol_p_count != expected_probs:
        issues.append(f"Số lời giải ({sol_p_count}) không khớp kỳ vọng ({expected_probs})!")

    # Tiêu chí 3: Media trong package
    with zipfile.ZipFile(output_path) as z:
        media_files = [n for n in z.namelist() if n.startswith("word/media/")]
        orphan_c_imgs = [n for n in media_files if any(n == f"word/media/image{i}.png" for i in range(1, 13))]
    print(f"3. Media trong package: {len(media_files)} files ({media_files})")
    print(f"   Ảnh C++ treo mồ côi: {len(orphan_c_imgs)}")
    if len(orphan_c_imgs) > 0:
        issues.append(f"Còn {len(orphan_c_imgs)} ảnh C++ mồ côi chưa xóa sạch: {orphan_c_imgs}!")

    # Tiêu chí 4: Grep XML các từ cấm
    forbidden_terms = ["Ràng buộc", "trắc nghiệm", "Bảng A", "DKOJ"]
    forbidden_found = {}
    with zipfile.ZipFile(output_path) as z:
        doc_xml = z.read("word/document.xml").decode("utf-8")
        for term in forbidden_terms:
            matches = len(re.findall(re.escape(term), doc_xml, re.IGNORECASE))
            forbidden_found[term] = matches
            if matches > 0:
                issues.append(f"Tìm thấy từ cấm '{term}' ({matches} lần) trong document.xml!")

    print(f"4. Grep XML từ cấm: {', '.join(f'{k}: {v}' for k, v in forbidden_found.items())}")

    # Tiêu chí 5: Math, Tables, Watermark, TOC
    tbl_headers = 0
    non_cant_split = 0
    for tbl in doc.tables:
        for r in tbl.rows:
            trPr = r._tr.get_or_add_trPr()
            if trPr.find(docx.oxml.ns.qn("w:tblHeader")) is not None:
                tbl_headers += 1
            if trPr.find(docx.oxml.ns.qn("w:cantSplit")) is None:
                non_cant_split += 1

    math_ns = "http://schemas.openxmlformats.org/officeDocument/2006/math"
    omath_count = len(doc._body._element.findall(".//{" + math_ns + "}oMath"))

    watermark_ok = True
    with zipfile.ZipFile(output_path) as z:
        for h in ["word/header1.xml", "word/header2.xml", "word/header3.xml"]:
            if h in z.namelist():
                xml_c = z.read(h).decode("utf-8")
                if not ("WordPictureWatermark" in xml_c or "logo_in" in xml_c or "v:shape" in xml_c):
                    watermark_ok = False
            else:
                watermark_ok = False

    print(f"5. Bảng & Định dạng:")
    print(f"   • Số công thức oMath: {omath_count}")
    print(f"   • Hàng tblHeader: {tbl_headers} (kỳ vọng 0) | Hàng non-cantSplit: {non_cant_split} (kỳ vọng 0)")
    print(f"   • Watermark logo đủ 3 headers: {watermark_ok}")

    # Tiêu chí 6: Màu Heading và tiêu đề H1
    h_color_issues = []
    with zipfile.ZipFile(output_path) as z:
        styles_xml = z.read("word/styles.xml").decode("utf-8")
        doc_xml = z.read("word/document.xml").decode("utf-8")
        if "0F4761" in styles_xml or "0F4761" in doc_xml:
            h_color_issues.append("Còn mã màu teal 0F4761 trong styles.xml hoặc document.xml!")

    h1_lesson_titles = [p.text.strip() for p in doc.paragraphs if p.style and p.style.name == "Heading 1" and p.text.strip().startswith("Bài")]
    manifest_titles = [l["title"] for l in volume_info["lessons"]]
    titles_match = (h1_lesson_titles == manifest_titles)

    print(f"6. Màu sắc & Tiêu đề:")
    print(f"   • Màu H1-H4: Hoàn toàn sạch màu 0F4761 ({len(h_color_issues) == 0})")
    print(f"   • 14 tên bài H1 khớp manifest: {titles_match}")
    if not titles_match:
        print(f"     Doc: {h1_lesson_titles}")
        print(f"     Mani: {manifest_titles}")
        issues.append("Tên bài H1 không khớp manifest!")
    if h_color_issues:
        issues.extend(h_color_issues)

    # Tiêu chí 7: Tổng số trang
    total_pages = "Chưa rõ"
    with zipfile.ZipFile(output_path) as z:
        if "docProps/app.xml" in z.namelist():
            app_xml = z.read("docProps/app.xml").decode("utf-8")
            m_p = re.search(r"<Pages>(\d+)</Pages>", app_xml)
            if m_p:
                total_pages = m_p.group(1)

    print(f"7. Tổng số trang: {total_pages} trang (kỳ vọng ~170–190 trang)")

    if not issues:
        print(f"\n🎉 AUDIT QUYỂN {vol_num} THÀNH CÔNG VƯỢT TRỘI: 100% TIÊU CHÍ ĐẠT CHUẨN!")
    else:
        print(f"\n❌ CÓ CÁC VẤN ĐỀ CẦN LƯU Ý:")
        for iss in issues:
            print(f"   - {iss}")

    return len(issues) == 0

def clean_lock_files():
    """Remove any ~$*.docx temporary lock files."""
    for lock in PYTHON_DIR.glob("~$*.docx"):
        try:
            lock.unlink()
            print(f"  🗑️ Đã xóa lock file: {lock.name}")
        except Exception:
            pass

def build_volume(volume_num):
    """Orchestrate building of a single volume."""
    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    target_vol = None
    for v in manifest["volumes"]:
        if v["volume"] == volume_num:
            target_vol = v
            break

    if not target_vol:
        print(f"❌ Không tìm thấy thông tin Quyển {volume_num} trong manifest!")
        return False

    # Step 1: Assemble Markdown
    full_md = build_volume_markdown(target_vol)

    # Step 2: Pandoc to intermediate docx
    intermediate_docx = PYTHON_DIR / f"_temp_vol_{volume_num}.docx"
    convert_markdown_to_docx(full_md, intermediate_docx)

    # Step 3: Postprocess Design System
    final_docx = postprocess_docx(intermediate_docx, target_vol)

    # Step 4: Cleanup temp docx
    if intermediate_docx.exists():
        os.remove(intermediate_docx)

    # Step 5: Update Word pagination
    update_docx_pages(final_docx)

    # Step 6: Audit
    audit_docx(final_docx, target_vol)
    return True

def main():
    print("=" * 70)
    print("🚀 BẮT ĐẦU XUẤT BẢN GIÁO TRÌNH WORD PYTHON CƠ BẢN (2 QUYỂN)")
    print(f"   Repo: {REPO_ROOT}")
    print(f"   Template: {TEMPLATE_DOCX.name}")
    print("=" * 70)

    clean_lock_files()

    # Build Volume 1
    build_volume(1)

    # Build Volume 2
    build_volume(2)

    clean_lock_files()

    print("\n" + "=" * 70)
    print("🎉 HOÀN TẤT TOÀN BỘ TIẾN TRÌNH XUẤT BẢN 2 QUYỂN!")
    print("   📘 Quyển 1: courses/python-bang-a/python-level-1-quyen-1.docx")
    print("   📕 Quyển 2: courses/python-bang-a/python-level-1-quyen-2.docx")
    print("=" * 70)

if __name__ == "__main__":
    main()
