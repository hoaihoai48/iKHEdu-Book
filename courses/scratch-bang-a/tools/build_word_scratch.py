#!/usr/bin/env python3
"""
BUILD SCRIPT: Xuất bản 2 file Word in màu giáo trình Scratch 3.0 cơ bản iKHEDU
Quyển 1: scratch-quyen-1.docx (Chương 1-3, Bài 01-08, 194 đề bài + 194 ảnh lời giải khối lệnh)
Quyển 2: scratch-quyen-2.docx (Chương 4-6, Bài 09-16, 130 đề bài + 130 ảnh lời giải khối lệnh)
Tái dùng khuôn chuẩn: courses/cpp-bang-b/c++-level-1-quyen-1.docx
Nguồn manifest: courses/scratch-bang-a/tools/word_build_manifest.json
Quy chuẩn áp dụng: docs/PLAN_BUILD_WORD_SCRATCH.md & docs/MASTER_WORD_BUILD_SPECIFICATION.md
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
SCRATCH_DIR = REPO_ROOT / "courses" / "scratch-bang-a"
TEMPLATE_DOCX = REPO_ROOT / "courses" / "cpp-bang-b" / "c++-level-1-quyen-1.docx"
MANIFEST_FILE = SCRATCH_DIR / "tools" / "word_build_manifest.json"
PROBLEMS_DIR = SCRATCH_DIR / "problems"

CHAPTER_NAMES = {
    1: "CHƯƠNG 01: BÚT VẼ PEN & ĐỒ HỌA",
    2: "CHƯƠNG 02: TÍNH TOÁN CƠ BẢN",
    3: "CHƯƠNG 03: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP",
    4: "CHƯƠNG 04: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ",
    5: "CHƯƠNG 05: DANH SÁCH (LIST) & THỐNG KÊ",
    6: "CHƯƠNG 06: XỬ LÝ CHUỖI KÝ TỰ",
}

def parse_de_bai(de_bai_path):
    """Parse De_Bai.md into structured sections (both algo and pen format)."""
    with open(de_bai_path, "r", encoding="utf-8") as f:
        text = f.read()

    bcanh_m = re.search(r'## Bối cảnh\s*\n(.*?)(?=\n## Nhiệm vụ|\n## Input|\n## Kịch bản|\Z)', text, re.DOTALL)
    nv_m = re.search(r'## Nhiệm vụ\s*\n(.*?)(?=\n## Input|\n## Kịch bản|\n## Output|\n## Kết quả|\Z)', text, re.DOTALL)
    
    # Input / Kịch bản tương tác
    inp_m = re.search(r'## (?:Input|Kịch bản tương tác.*?)\s*\n(.*?)(?=\n## Output|\n## Kết quả|\n## Sample|\Z)', text, re.DOTALL)
    # Output / Kết quả mong đợi
    out_m = re.search(r'## (?:Output|Kết quả mong đợi.*?)\s*\n(.*?)(?=\n## Sample|\n## Ràng buộc|\Z)', text, re.DOTALL)

    bcanh = bcanh_m.group(1).strip() if bcanh_m else ""
    nv = nv_m.group(1).strip() if nv_m else ""
    inp = inp_m.group(1).strip() if inp_m else ""
    out = out_m.group(1).strip() if out_m else ""

    # Samples
    samples = []
    sample_blocks = re.findall(r'## (Sample \d+)\s*\n(.*?)(?=\n## Sample \d+|\n## Ràng buộc|\Z)', text, re.DOTALL)
    for s_title, s_body in sample_blocks:
        sinp_m = re.search(r'### (?:Input|Kịch bản chạy)\s*```(?:text)?\n(.*?)```', s_body, re.DOTALL)
        sout_m = re.search(r'### (?:Output|Kết quả.*?)\s*(?:```(?:text)?\n(.*?)\n```|(.*?)(?=\n###|\Z))', s_body, re.DOTALL)
        sexpl_m = re.search(r'### Giải thích\s*\n(.*)', s_body, re.DOTALL)

        sinp = sinp_m.group(1).strip() if sinp_m else ""
        if sout_m:
            sout = (sout_m.group(1) or sout_m.group(2) or "").strip()
        else:
            sout = ""
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
        md.append(f"Bối cảnh: {parsed_data['bcanh']}\n\n")

    if parsed_data["nv"]:
        nv_text = parsed_data["nv"]
        # Ensure ordered/bullet lists within nv have blank line before first item
        nv_text = re.sub(r'([^\n]+[^\s|])\n(\d+\.[ \t])', lambda m: m.group(1) + '\n\n' + m.group(2), nv_text)
        md.append(f"Nhiệm vụ: {nv_text}\n\n")

    if parsed_data["inp"]:
        md.append(f"**Đầu vào (Input):**\n\n{parsed_data['inp']}\n\n")

    if parsed_data["out"]:
        md.append(f"**Đầu ra (Output):**\n\n{parsed_data['out']}\n\n")

    for s_idx, s in enumerate(parsed_data["samples"], 1):
        s_title_str = f"Ví dụ mẫu ({s['title']}):"
        inp_str = s["input"].replace("\n", " <br> ") if s["input"] else "(Nhấn cờ xanh)"
        out_str = s["output"].replace("\n", " <br> ") if s["output"] else "(Hiển thị kết quả)"

        md.append(f"**{s_title_str}**\n")
        md.append("| Đầu vào (Input) | Đầu ra (Output) |")
        md.append("|---|---|")
        md.append(f"| {inp_str} | {out_str} |\n")

        if s["explain"]:
            md.append(f"**Giải thích:**\n\n{s['explain']}\n")

    return "\n".join(md) + "\n\n"

def resolve_images_in_theory(content_text, lesson_folder):
    """Map relative image links to absolute filesystem paths."""
    def replace_img(match):
        alt = match.group(1)
        orig_path = match.group(2)
        # Handle relative paths like ../../assets/...
        raw_path = orig_path.split("?")[0]
        # Use empty alt to prevent Pandoc from generating figure captions
        if raw_path.startswith("../../assets/"):
            rel_sub = raw_path[len("../../assets/"):]
            abs_p = SCRATCH_DIR / "assets" / rel_sub
            if abs_p.exists():
                return f"\n\n![]({abs_p.resolve()})\n\n"
        elif raw_path.startswith("assets/"):
            # relative to SCRATCH_DIR (some lessons use this form)
            abs_p = SCRATCH_DIR / raw_path
            if abs_p.exists():
                return f"\n\n![]({abs_p.resolve()})\n\n"
        elif not Path(raw_path).is_absolute():
            abs_p = (lesson_folder / raw_path).resolve()
            if abs_p.exists():
                return f"\n\n![]({abs_p})\n\n"
        return match.group(0)

    # Filter out ALL quiz/concept quiz sections regardless of number prefix (## 6., ## 7., ## 8. etc.)
    clean_text = re.sub(
        r'\n## \d+\.\s*(?:Bộ Câu Hỏi Trắc Nghiệm|Câu Hỏi Trắc Nghiệm|Concept Quiz).*?(?=\n## |\n# |\Z)',
        '',
        content_text,
        flags=re.DOTALL
    )
    # Filter out navigation line at end
    clean_text = re.sub(r'👉\s*\*\*Tiếp theo:\*\*.*', '', clean_text)
    
    return re.sub(r'!\[(.*?)\]\((.*?)\)', replace_img, clean_text)

def build_volume_markdown(volume_info):
    """Assemble complete Markdown for a volume."""
    vol_num = volume_info["volume"]
    print(f"\n============================================================")
    print(f"📖 Đang chuẩn bị Markdown cho QUYỂN {vol_num}: {volume_info['title']}...")
    print(f"============================================================")

    md_parts = []

    # 1. Preface (Lời nói đầu)
    preface_path = SCRATCH_DIR / volume_info["preface"]
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
        les_folder = SCRATCH_DIR / "lessons" / lesson_info["folder"]

        # If new chapter, add Chapter heading
        if chap_num != current_chapter:
            current_chapter = chap_num
            chap_title = CHAPTER_NAMES.get(chap_num, f"CHƯƠNG {chap_num:02d}")
            md_parts.append(f"# {chap_title}\n\n")

        # Read Theory file
        theory_file = SCRATCH_DIR / lesson_info["content_file"]
        if theory_file.exists():
            with open(theory_file, "r", encoding="utf-8") as f:
                theory_text = f.read()
            theory_text = resolve_images_in_theory(theory_text, les_folder)
            md_parts.append(theory_text.strip() + "\n\n")

        # Add "Bài tập thực hành" section (Heading 2)
        md_parts.append("## Bài tập thực hành\n\n")

        # Add problems
        for p_idx, prob in enumerate(lesson_info["problems"], 1):
            prob_code = prob["code"]
            prob_title = prob["title"]
            de_bai_file = PROBLEMS_DIR / prob_code / "De_Bai.md"
            if de_bai_file.exists():
                parsed = parse_de_bai(de_bai_file)
                p_md = format_problem_markdown(p_idx, prob_code, prob_title, parsed)
                md_parts.append(p_md)
                prob_global_count += 1
            else:
                print(f"  ⚠️ Thiếu De_Bai.md: {prob_code}")

    print(f"  → Tổng số bài tập đã nạp cho Quyển {vol_num}: {prob_global_count}")

    # 3. Phụ lục A
    appendix_a_path = SCRATCH_DIR / volume_info["appendix_a"]
    with open(appendix_a_path, "r", encoding="utf-8") as f:
        app_a_text = f.read().strip()
    # Resolve relative images in appendix A
    def resolve_app_img(m):
        alt = m.group(1)
        src = m.group(2).strip()
        abs_p = (REPO_ROOT / src).resolve() if not Path(src).is_absolute() else Path(src)
        if abs_p.exists():
            return f"\n\n![]({abs_p})\n\n"  # empty alt = no Pandoc caption
        return m.group(0)
    app_a_text = re.sub(r'!\[(.*?)\]\((.*?)\)', resolve_app_img, app_a_text)
    md_parts.append(app_a_text + "\n\n")

    # 4. Phụ lục B (Solutions with Block PNGs - Chuẩn 3 bài đầu + câu tương tự như Python)
    md_parts.append("# Phụ lục B: Lời giải bài tập tham khảo\n\n")
    md_parts.append("> Phần này cung cấp ảnh chụp khối lệnh Scratch 3.0 Tiếng Việt tham khảo cho các bài tập tiêu biểu của mỗi bài học.\n\n")

    sol_count = 0
    for lesson_info in volume_info["lessons"]:
        chap_num = lesson_info["chapter"]
        les_title = lesson_info["title"]

        md_parts.append(f"## Chương {chap_num:02d} — {les_title}\n\n")

        # Chỉ lấy 3 bài đầu tiên của mỗi bài học
        sample_problems = lesson_info["problems"][:3]

        for prob in sample_problems:
            prob_code = prob["code"]
            prob_title = prob["title"]
            img_file = PROBLEMS_DIR / prob_code / "solution_blocks_vi.png"
            
            md_parts.append(f"### {prob_code} — {prob_title}\n\n")
            if img_file.exists():
                md_parts.append(f"![]({img_file.resolve()})\n\n")
                sol_count += 1
            else:
                md_parts.append(f"*(Khối lệnh giải mẫu của bài {prob_code})*\n\n")

        md_parts.append("Các bài tập còn lại có phương pháp và cấu trúc tương tự, học sinh tự suy luận và cài đặt.\n\n")

    print(f"  → Tổng số lời giải đã nạp cho Quyển {vol_num}: {sol_count} (chuẩn 3 bài tiêu biểu/bài học)")

    # 5. Mục lục
    md_parts.append("# Mục lục\n\n")

    full_md = "\n".join(md_parts)
    return full_md

def convert_markdown_to_docx(full_md, intermediate_docx):
    """Convert full markdown to docx using pandoc with reference-doc."""
    print(f"\n🔧 Đang chạy Pandoc chuyển đổi Markdown → DOCX...")
    # Fix pandoc: dòng `> - item` sau `> tieu de` bị gộp thành 1 đoạn
    # nếu thiếu dòng `>` trống ngăn cách → chèn dòng `>` trống vào
    full_md = re.sub(r'(?m)^(> [^\s>\-#|].*)\n(> - )', r'\1\n>\n\2', full_md)
    intermediate_md = SCRATCH_DIR / f"_build_intermediate_{intermediate_docx.stem}.md"
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
    """Apply typography (#000000, 18/14/13pt TOC), tables, code, headers, watermark."""
    import docx
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls, qn

    vol_num = volume_info["volume"]
    header_book_title = volume_info["header_book"]
    output_name = volume_info["output"]

    print(f"\n🎨 Đang xử lý hậu kỳ hoàn thiện OpenXML & Typography cho Quyển {vol_num}...")
    doc = docx.Document(str(docx_path))

    # 1. Page Setup & Margins
    for section in doc.sections:
        section.top_margin = Pt(36.0)
        section.bottom_margin = Pt(36.0)
        section.left_margin = Pt(64.35)
        section.right_margin = Pt(36.0)
        section.page_width = Pt(595.3)   # A4
        section.page_height = Pt(841.9)
        section.different_first_page_header_footer = True

        # Header Text Right
        if section.header is not None:
            for p in section.header.paragraphs:
                for r in p.runs:
                    if "Giáo trình" in r.text or "quyển" in r.text:
                        r.text = f"  {header_book_title}"

    # 2. Track Headings for Interactive TOC
    toc_headings = []
    bm_counter = 1
    p_toc_heading = None
    practice_count = 0

    # 3. Paragraphs Processing
    in_preface = False
    in_appendix_b = False
    for idx, para in enumerate(doc.paragraphs):
        style_name = para.style.name if para.style else ""
        text = para.text.strip()

        # A. Heading 1
        if style_name == "Heading 1":
            para.paragraph_format.keep_with_next = True
            is_chapter = text.startswith("CHƯƠNG")
            is_lesson = text.startswith("Bài") or text.startswith("BÀI")
            is_app_a = "Phụ lục A" in text
            is_app_b = "Phụ lục B" in text
            is_toc = ("Mục lục" in text or "MỤC LỤC" in text)
            is_preface = ("LỜI NÓI ĐẦU" in text)

            if is_preface:
                in_preface = True
                in_appendix_b = False
            elif is_app_b:
                in_appendix_b = True
                in_preface = False
            elif is_chapter or is_lesson or is_app_a or is_toc:
                in_preface = False
                in_appendix_b = False

            if is_chapter:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(8)
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00) # Đen tuyền #000000
            elif is_preface:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(6)
                para.paragraph_format.space_after = Pt(6)
                para.paragraph_format.page_break_before = False
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            elif is_lesson:
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(14)
                para.paragraph_format.space_after = Pt(4)
                # First lesson in chapter does not pageBreakBefore
                prev_text = doc.paragraphs[idx - 1].text.strip() if idx > 0 else ""
                if prev_text.startswith("CHƯƠNG"):
                    para.paragraph_format.page_break_before = False
                else:
                    para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(15.5)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            elif is_app_a or is_app_b:
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(6)
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(15.5)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            elif is_toc:
                p_toc_heading = para
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(7) # 140 dxa
                para.paragraph_format.page_break_before = True
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18) # 18.0pt chuẩn
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

            # Bookmark for TOC
            if not is_toc:
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
                    r.font.color.rgb = RGBColor(0xFF, 0x00, 0x00) # Đỏ cờ #FF0000
            else:
                para.paragraph_format.space_before = Pt(11)
                para.paragraph_format.space_after = Pt(3)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # C. Heading 3
        elif style_name == "Heading 3":
            para.paragraph_format.keep_with_next = True
            para.paragraph_format.space_before = Pt(8)
            para.paragraph_format.space_after = Pt(2)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # D. Source Code
        elif style_name == "Source Code":
            para.alignment = WD_ALIGN_PARAGRAPH.LEFT
            para.paragraph_format.line_spacing = 1.05
            para.paragraph_format.space_before = Pt(3)
            para.paragraph_format.space_after = Pt(3)
            for r in para.runs:
                r.font.name = "Consolas"
                r.font.size = Pt(9.0)
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # E. Block Text (Callout)
        elif style_name == "Block Text":
            para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            para.paragraph_format.line_spacing = 1.15
            para.paragraph_format.space_before = Pt(4)
            para.paragraph_format.space_after = Pt(4)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00) # Đen tuyền chuẩn in

        # F. Image Caption
        elif style_name in ["Image Caption", "Caption"] or (idx > 0 and len(doc.paragraphs[idx - 1]._p.findall(".//" + qn("w:drawing"))) > 0 and len(text) > 0 and len(text) < 120 and not text.startswith("Bài") and not text.startswith("CHƯƠNG")):
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.line_spacing = 1.15
            para.paragraph_format.space_before = Pt(2)
            para.paragraph_format.space_after = Pt(6)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.5)
                r.font.italic = True
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # G. Compact
        elif style_name == "Compact":
            if in_preface:
                # Preface bullet lists: 14pt, 1.5 line spacing, clean spacing
                para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                para.paragraph_format.line_spacing = 1.5
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after = Pt(3)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            else:
                para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                para.paragraph_format.line_spacing = 1.15
                para.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after = Pt(4)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(12)
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # H. Drawings / Images
        elif len(para._p.findall(".//" + qn("w:drawing"))) > 0:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_before = Pt(4)
            para.paragraph_format.space_after = Pt(4)

            # Image scaling: Phụ lục B dùng max 4cm, lý thuyết cap tại 9cm
            if in_appendix_b:
                max_cx = 1440000   # 4.0 cm — solution blocks nhỏ gọn
            else:
                max_cx = 2340000   # 6.5 cm — ảnh khối lệnh lý thuyết vừa trang

            for drawing in para._p.findall(".//"+qn("w:drawing")):
                wp_extent = drawing.find(".//"+qn("wp:extent"))
                a_ext = drawing.find(".//"+qn("a:ext"))
                if wp_extent is not None:
                    try:
                        old_cx = int(wp_extent.get("cx", 0))
                        old_cy = int(wp_extent.get("cy", 0))
                        if old_cx > max_cx:
                            target_cx = max_cx
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

        # I. Normal text & Preface content
        else:
            # Check for Pandoc horizontal rule (<w:pict><v:rect ... o:hr="t"/></w:pict>) and remove it
            from xml.etree import ElementTree as ET
            from docx.oxml import xmlchemy
            hr_pict = para._p.findall(".//" + qn("w:pict"))
            is_hr = False
            for pict in hr_pict:
                from lxml import etree
                pict_xml = etree.tostring(pict, encoding="unicode")
                if "o:hr=\"t\"" in pict_xml or "o:hr" in pict_xml:
                    is_hr = True
                    break
            if is_hr:
                # Remove horizontal line by clearing paragraph contents and setting spacing to 0
                for r in list(para.runs):
                    para._p.remove(r._r)
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after = Pt(0)
                para.paragraph_format.line_spacing = 0
                continue

            if in_preface:
                # Preface body: 14pt, 1.5 line spacing, Justify
                para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                para.paragraph_format.line_spacing = 1.5
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after = Pt(4)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(14)
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            else:
                para.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                para.paragraph_format.line_spacing = 1.15
                para.paragraph_format.space_before = Pt(0)
                para.paragraph_format.space_after = Pt(4)
                for r in para.runs:
                    if not r.font.name:
                        r.font.name = "Times New Roman"
                    r.font.size = Pt(12.5)
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    # 4. Tables Processing
    sample_table_count = 0
    theory_table_count = 0

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

            # Header row 0
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
                        r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

            # Data rows 1+ (Dynamic Left Indent)
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

                    if "<br>" in raw_text:
                        lines = [l.strip() for l in raw_text.split("<br>") if l.strip()]
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
                        sp = pPr.find(qn("w:spacing"))
                        if sp is not None:
                            sp.set(qn("w:before"), "20")
                            sp.set(qn("w:after"), "20")
                            sp.set(qn("w:line"), "252")
                            sp.set(qn("w:lineRule"), "auto")
                        else:
                            pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="20" w:after="20" w:line="252" w:lineRule="auto"/>'))
                        pPr.append(parse_xml(f'<w:ind {nsdecls("w")} w:left="{indent_dxa}"/>'))
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        r = p.add_run(line)
                        r.font.name = "Consolas"
                        r.font.size = Pt(11)
                        r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
        else:
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
                            
                            p_t = p.text.strip()
                            if len(p_t) <= 4 and not " " in p_t:
                                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            else:
                                p.alignment = WD_ALIGN_PARAGRAPH.LEFT

                            for r in p.runs:
                                r.font.name = "Times New Roman"
                                r.font.size = Pt(12)
                                r.font.bold = True
                                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
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
                                pPr.append(parse_xml(f'<w:spacing {nsdecls("w")} w:before="40" w:line="276" w:lineRule="auto"/>'))
                            
                            p_t = p.text.strip()
                            # If cell contains short number or symbol (<= 3 chars, e.g. 3, 4, 120°, 90°), center it; otherwise left-align
                            if len(p_t) <= 3 and not " " in p_t:
                                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                            else:
                                p.alignment = WD_ALIGN_PARAGRAPH.LEFT

                            for r in p.runs:
                                r.font.name = "Times New Roman"
                                r.font.size = Pt(12)
                                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    # 5. Build Table of Contents with Exact Font & Spacing
    if p_toc_heading and not volume_info.get("merged"):
        print(f"  → Đang xây dựng Mục lục tương tác chuẩn (18pt/14pt/13pt, tab 9899) gồm {len(toc_headings)} mục...")
        last_elem = p_toc_heading._p

        for item in toc_headings:
            title = html.escape(item["text"])
            bm = item["bm_name"]

            if item["is_chapter"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:tabs>
                            <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
                        </w:tabs>
                        <w:spacing w:before="160" w:after="40"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="28"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:t>{title}</w:t>
                        </w:r>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="28"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:tab/>
                        </w:r>
                        <w:fldSimple w:instr="PAGEREF {bm} \\h">
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                    <w:b/>
                                    <w:sz w:val="28"/>
                                    <w:color w:val="000000"/>
                                    <w:noProof/>
                                </w:rPr>
                                <w:t>1</w:t>
                            </w:r>
                        </w:fldSimple>
                    </w:hyperlink>
                </w:p>'''
            elif item["is_lesson"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:tabs>
                            <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
                        </w:tabs>
                        <w:ind w:left="320"/>
                        <w:spacing w:before="24" w:after="24"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:sz w:val="26"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:t>•  {title}</w:t>
                        </w:r>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:sz w:val="26"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:tab/>
                        </w:r>
                        <w:fldSimple w:instr="PAGEREF {bm} \\h">
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                    <w:sz w:val="26"/>
                                    <w:color w:val="000000"/>
                                    <w:noProof/>
                                </w:rPr>
                                <w:t>1</w:t>
                            </w:r>
                        </w:fldSimple>
                    </w:hyperlink>
                </w:p>'''
            elif item["is_appendix"] or item["is_preface"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:tabs>
                            <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
                        </w:tabs>
                        <w:spacing w:before="160" w:after="40"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="28"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:t>{title}</w:t>
                        </w:r>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="28"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:tab/>
                        </w:r>
                        <w:fldSimple w:instr="PAGEREF {bm} \\h">
                            <w:r>
                                <w:rPr>
                                    <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                    <w:b/>
                                    <w:sz w:val="28"/>
                                    <w:color w:val="000000"/>
                                    <w:noProof/>
                                </w:rPr>
                                <w:t>1</w:t>
                            </w:r>
                        </w:fldSimple>
                    </w:hyperlink>
                </w:p>'''
            else:
                continue

            p_elem = parse_xml(p_xml)
            last_elem.addnext(p_elem)
            last_elem = p_elem

    # 5b. Merged volume: restructure outline levels + real TOC field
    # (bản gộp 1 quyển: Bài học → Heading 2, mục con → Normal,
    #  Mục lục = TOC field thật để Update Field cập nhật đúng số trang)
    if p_toc_heading and volume_info.get("merged"):
        import re as _re
        for para in doc.paragraphs:
            st = para.style.name if para.style else ""
            tx = para.text.strip()
            if st == "Heading 1" and _re.match(r"Bài \d+:", tx):
                para.style = doc.styles["Heading 2"]
            elif st == "Heading 2" and not _re.match(r"Bài \d+:", tx):
                para.style = doc.styles["Normal"]
            elif st == "Heading 3":
                para.style = doc.styles["Normal"]
        try:
            p_toc_heading.style = doc.styles["TOC Heading"]
        except Exception:
            pass
        ns = nsdecls("w")
        import html as _html

        def _toc_entry(title, bm, big):
            title = _html.escape(title)
            sz = "28" if big else "26"
            head = "•  " if not big else ""
            return (
                f'<w:p {ns}>'
                '<w:pPr><w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9899"/>'
                '</w:tabs>' + ('' if big else '<w:ind w:left="320"/>') + '</w:pPr>'
                f'<w:hyperlink w:anchor="{bm}">'
                f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>'
                + (f'<w:b/>' if big else '') + f'<w:sz w:val="{sz}"/><w:color w:val="000000"/>'
                f'</w:rPr><w:t>{head}{title}</w:t></w:r>'
                f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>'
                + (f'<w:b/>' if big else '') + f'<w:sz w:val="{sz}"/><w:color w:val="000000"/>'
                '</w:rPr><w:tab/></w:r>'
                f'<w:fldSimple w:instr="PAGEREF {bm} \\h">'
                f'<w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>'
                + (f'<w:b/>' if big else '') + f'<w:sz w:val="{sz}"/><w:color w:val="000000"/>'
                '<w:noProof/></w:rPr><w:t>1</w:t></w:r>'
                '</w:fldSimple></w:hyperlink></w:p>'
            )

        fld = [
            f'<w:p {ns}><w:r><w:fldChar {ns} w:fldCharType="begin"/></w:r></w:p>',
            f'<w:p {ns}><w:r><w:instrText {ns} xml:space="preserve"> TOC \\o "1-2" \\h \\z \\u </w:instrText></w:r></w:p>',
            f'<w:p {ns}><w:r><w:fldChar {ns} w:fldCharType="separate"/></w:r></w:p>',
        ]
        kept = 0
        for item in toc_headings:
            tx = item["text"]
            big = bool(item["is_chapter"] or item["is_appendix"] or item["is_preface"])
            small = bool(item["is_lesson"]) and ("[" not in tx)
            if not (big or small):
                continue
            fld.append(_toc_entry(tx, item["bm_name"], big))
            kept += 1
        fld.append(
            f'<w:p {ns}><w:r><w:fldChar {ns} w:fldCharType="end"/></w:r></w:p>'
        )
        anchor = p_toc_heading._p
        for frag in fld:
            elem = parse_xml(frag)
            anchor.addnext(elem)
            anchor = elem
        print("  → Đã chèn TOC field thật (Update Field/F9 cập nhật đúng số trang).")

    # Save post-processed docx
    final_output = SCRATCH_DIR / output_name
    doc.save(str(final_output))
    print(f"  ✅ Đã lưu file hoàn thiện: {final_output.name} ({final_output.stat().st_size:,} bytes)")

    # 6. Clean docx package (remove orphan C++ media image1-12, sync header title, and remove updateFields)
    clean_docx_package(
        final_output, header_book_title,
        update_fields=bool(volume_info.get("merged")),
    )

    return final_output

def clean_docx_package(docx_path, header_book_title, update_fields=False):
    """Remove template orphan C++ images (image1..12), update header titles across all header XMLs, and ensure NO updateFields."""
    print(f"  🧹 Dọn dẹp package docx: loại bỏ ảnh mồ côi C++, đồng bộ header '{header_book_title}' và kiểm tra an toàn OpenXML...")
    temp_zip_path = docx_path.parent / f"_temp_clean_{docx_path.name}"
    with zipfile.ZipFile(docx_path, "r") as zin:
        with zipfile.ZipFile(temp_zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                if any(item.filename == f"word/media/image{i}.png" for i in range(1, 13)):
                    continue
                data = zin.read(item.filename)
                
                # Clean document.xml.rels
                if item.filename == "word/_rels/document.xml.rels":
                    rels_text = data.decode("utf-8")
                    for i in range(1, 13):
                        rels_text = re.sub(rf'<Relationship[^>]*Target="media/image{i}\.png"[^>]*/>', '', rels_text)
                    data = rels_text.encode("utf-8")

                # Ensure word/settings.xml DOES NOT have updateFields
                # (rule repo: user tu Update Field tay trong Word, khong hien prompt)
                if item.filename == "word/settings.xml":
                    settings_text = data.decode("utf-8")
                    settings_text = re.sub(r'<w:updateFields[^>]*/>', '', settings_text)
                    data = settings_text.encode("utf-8")

                # Ensure ALL header XML files have the correct Scratch book title
                if item.filename.startswith("word/header") and item.filename.endswith(".xml"):
                    header_text = data.decode("utf-8")
                    # Replace any existing "Giáo trình ... - quyển ..." with header_book_title
                    header_text = re.sub(
                        r'Giáo trình [^<]+ - quyển \d+',
                        header_book_title,
                        header_text
                    )
                    data = header_text.encode("utf-8")

                zout.writestr(item, data)

    shutil.move(str(temp_zip_path), str(docx_path))
    print(f"  ✅ Hoàn tất đóng gói an toàn: {docx_path.name} ({docx_path.stat().st_size:,} bytes)")

def main():
    print(f"🚀 BẮT ĐẦU QUY TRÌNH BUILD 2 QUYỂN WORD GIÁO TRÌNH SCRATCH BẢNG A...")
    if not MANIFEST_FILE.exists():
        print(f"❌ Không tìm thấy manifest: {MANIFEST_FILE}")
        sys.exit(1)

    with open(MANIFEST_FILE, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    # Allow building specific volume via CLI argument (1, 2, or "full" = gộp 1 quyển)
    target_vol = sys.argv[1] if len(sys.argv) > 1 else None
    if target_vol not in (None, "1", "2", "full"):
        try:
            target_vol = int(target_vol)
        except ValueError:
            pass

    if target_vol == "full":
        vols = {v["volume"]: v for v in manifest_data["volumes"]}
        full_vol = {
            "volume": 0,
            "merged": True,
            "title": "Giáo trình Scratch cơ bản (bản gộp 1 quyển: Chương 01–06, Bài 01–16)",
            "header_book": "Giáo trình Scratch cơ bản",
            "preface": "reference/Loi_Noi_Dau_Scratch_Full.md",
            "appendix_a": vols[1]["appendix_a"],
            "output": "scratch-full.docx",
            "lessons": vols[1]["lessons"] + vols[2]["lessons"],
        }
        intermediate_docx = SCRATCH_DIR / "_temp_raw_full.docx"
        full_md = build_volume_markdown(full_vol)
        convert_markdown_to_docx(full_md, intermediate_docx)
        postprocess_docx(intermediate_docx, full_vol)
        if intermediate_docx.exists():
            intermediate_docx.unlink()
        temp_md = SCRATCH_DIR / f"_build_intermediate_{intermediate_docx.stem}.md"
        if temp_md.exists():
            temp_md.unlink()
        print("\n🎉 HOÀN THÀNH BẢN GỘP 1 QUYỂN (mục lục TOC field — mở file và cập nhật Field để có số trang)!")
        return

    for vol in manifest_data["volumes"]:
        if target_vol and vol["volume"] != target_vol:
            continue

        vol_num = vol["volume"]
        intermediate_docx = SCRATCH_DIR / f"_temp_raw_quyen_{vol_num}.docx"

        # 1. Assemble Markdown
        full_md = build_volume_markdown(vol)

        # 2. Pandoc conversion
        convert_markdown_to_docx(full_md, intermediate_docx)

        # 3. Post-process
        postprocess_docx(intermediate_docx, vol)

        # 4. Clean intermediate
        if intermediate_docx.exists():
            intermediate_docx.unlink()
        temp_md = SCRATCH_DIR / f"_build_intermediate_{intermediate_docx.stem}.md"
        if temp_md.exists():
            temp_md.unlink()

    print(f"\n🎉 HOÀN THÀNH XUẤT BẢN GIÁO TRÌNH WORD SCRATCH CƠ BẢN THÀNH CÔNG RỰC RỠ!")

if __name__ == "__main__":
    main()
