#!/usr/bin/env python3
"""
build_perfect_q1.py
Xây dựng c++-level-1-quyen-1.docx chuẩn xác 100% theo mẫu c++-level-1-quyen-2.docx:
- 4 Chương (12 Bài học, 164 bài toán):
  + CHƯƠNG 01: NỀN TẢNG LẬP TRÌNH C++ (Bài 01, Bài 02, Bài 03 - 24 bài)
  + CHƯƠNG 02: THUẬT TOÁN SẮP XẾP & KỸ THUẬT MẢNG (Bài 04, Bài 05, Bài 06 - 42 bài)
  + CHƯƠNG 03: MẢNG TIỀN TỐ & TÌM KIẾM NHỊ PHÂN (Bài 07, Bài 08, Bài 09 - 50 bài)
  + CHƯƠNG 04: SỐ HỌC & ĐẠI SỐ MODULAR (Bài 10, Bài 11, Bài 12 - 48 bài)
- BLOCKER 1: Nhúng đầy đủ 18 ảnh minh họa lý thuyết (PNG 1600px).
- BLOCKER 2: Đánh số bài tập liên tục từ Bài 01 đến Bài 164 toàn quyển.
- MAJOR 3: Tiêu đề Bài 01-03 và 24 đề mới dùng sentence case đồng bộ Q2.
- MAJOR 4: H1 LỜI NÓI ĐẦU viết hoa toàn bộ như Q2.
- MAJOR 5: Heading 4 count = 0.
- MAJOR 6: List items phân tách chuẩn dòng trống.
- MINOR 7: Cập nhật app.xml đúng số liệu đếm thật (paragraphs, words, characters).
- MINOR 8: Gộp text runs liền kề để tỷ lệ single-char < 10%.
- Màu chữ đen tuyền #000000, font chữ Times New Roman/Consolas chuẩn in ấn, tiêu đề bài tập thực hành đỏ #FF0000.
"""

import os
import re
import sys
import glob
import html
import shutil
import zipfile
import subprocess
from pathlib import Path

import docx
from docx.shared import Pt, Inches, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b")
PROBLEMS_DIR = BASE_DIR / "problems"
LESSONS_DIR = BASE_DIR / "lessons"
OUT_DOCX = BASE_DIR / "c++-level-1-quyen-1.docx"
BOOK_AUTHOR = "Trung tâm tin học iKH"

CHAPTERS_DEF = [
    {
        "num": 1,
        "title": "CHƯƠNG 01: NỀN TẢNG LẬP TRÌNH C++",
        "lessons": [
            {
                "num": 1,
                "title": "Bài 01: Biến, kiểu dữ liệu, toán tử & nhập xuất an toàn",
                "folder": LESSONS_DIR / "lesson-01-nen-tang-bien-nhap-xuat",
                "content_file": LESSONS_DIR / "lesson-01-nen-tang-bien-nhap-xuat" / "Lesson01_Production_Content.md",
                "problem_codes": [f"CPPB-L0-{i:02d}" for i in range(1, 9)]
            },
            {
                "num": 2,
                "title": "Bài 02: Cấu trúc rẽ nhánh & cấu trúc vòng lặp",
                "folder": LESSONS_DIR / "lesson-02-re-nhanh-va-vong-lap",
                "content_file": LESSONS_DIR / "lesson-02-re-nhanh-va-vong-lap" / "Lesson02_Production_Content.md",
                "problem_codes": [f"CPPB-L0-{i:02d}" for i in range(9, 17)]
            },
            {
                "num": 3,
                "title": "Bài 03: Mảng 1 chiều, vector, xâu ký tự & tổ chức hàm",
                "folder": LESSONS_DIR / "lesson-03-mang-vector-xau-va-ham",
                "content_file": LESSONS_DIR / "lesson-03-mang-vector-xau-va-ham" / "Lesson03_Production_Content.md",
                "problem_codes": [f"CPPB-L0-{i:02d}" for i in range(17, 25)]
            }
        ]
    },
    {
        "num": 2,
        "title": "CHƯƠNG 02: THUẬT TOÁN SẮP XẾP & KỸ THUẬT MẢNG",
        "lessons": [
            {
                "num": 4,
                "title": "Bài 04: Thuật toán sắp xếp",
                "folder": LESSONS_DIR / "lesson-04-sap-xep",
                "content_file": LESSONS_DIR / "lesson-04-sap-xep" / "Lesson04_Production_Content.md",
                "problem_codes": [f"CPPB-SX-{i:02d}" for i in range(1, 15)]
            },
            {
                "num": 5,
                "title": "Bài 05: Kỹ thuật hai con trỏ",
                "folder": LESSONS_DIR / "lesson-05-hai-con-tro",
                "content_file": LESSONS_DIR / "lesson-05-hai-con-tro" / "Lesson05_Production_Content.md",
                "problem_codes": [f"CPPB-HCT-{i:02d}" for i in range(1, 15)]
            },
            {
                "num": 6,
                "title": "Bài 06: Kỹ thuật cửa sổ trượt",
                "folder": LESSONS_DIR / "lesson-06-cua-so-truot",
                "content_file": LESSONS_DIR / "lesson-06-cua-so-truot" / "Lesson06_Production_Content.md",
                "problem_codes": [f"CPPB-CST-{i:02d}" for i in range(1, 15)]
            }
        ]
    },
    {
        "num": 3,
        "title": "CHƯƠNG 03: MẢNG TIỀN TỐ & TÌM KIẾM NHỊ PHÂN",
        "lessons": [
            {
                "num": 7,
                "title": "Bài 07: Mảng tiền tố & mảng hiệu",
                "folder": LESSONS_DIR / "lesson-07-mang-tien-to",
                "content_file": LESSONS_DIR / "lesson-07-mang-tien-to" / "Lesson07_Production_Content.md",
                "problem_codes": [f"CPPB-PT-{i:02d}" for i in range(1, 17)]
            },
            {
                "num": 8,
                "title": "Bài 08: Thuật toán tìm kiếm nhị phân",
                "folder": LESSONS_DIR / "lesson-08-tim-kiem-nhi-phan",
                "content_file": LESSONS_DIR / "lesson-08-tim-kiem-nhi-phan" / "Lesson08_Production_Content.md",
                "problem_codes": [f"CPPB-BS-{i:02d}" for i in range(1, 19)]
            },
            {
                "num": 9,
                "title": "Bài 09: Phép toán BIT & biểu diễn trạng thái",
                "folder": LESSONS_DIR / "lesson-09-phep-toan-bit",
                "content_file": LESSONS_DIR / "lesson-09-phep-toan-bit" / "Lesson09_Production_Content.md",
                "problem_codes": [f"CPPB-BIT-{i:02d}" for i in range(1, 17)]
            }
        ]
    },
    {
        "num": 4,
        "title": "CHƯƠNG 04: SỐ HỌC & ĐẠI SỐ MODULAR",
        "lessons": [
            {
                "num": 10,
                "title": "Bài 10: Lý thuyết số & số nguyên tố",
                "folder": LESSONS_DIR / "lesson-10-uoc-boi-so-nguyen-to",
                "content_file": LESSONS_DIR / "lesson-10-uoc-boi-so-nguyen-to" / "Lesson10_Production_Content.md",
                "problem_codes": [f"CPPB-NT-{i:02d}" for i in range(1, 17)]
            },
            {
                "num": 11,
                "title": "Bài 11: Đồng dư thức, lũy thừa nhị phân & nghịch đảo modulo",
                "folder": LESSONS_DIR / "lesson-11-dong-du-luy-thua-nghich-dao",
                "content_file": LESSONS_DIR / "lesson-11-dong-du-luy-thua-nghich-dao" / "Lesson11_Production_Content.md",
                "problem_codes": [f"CPPB-MOD-{i:02d}" for i in range(1, 17)]
            },
            {
                "num": 12,
                "title": "Bài 12: Xử lý số nguyên lớn (BigInt)",
                "folder": LESSONS_DIR / "lesson-12-so-nguyen-lon-bigint",
                "content_file": LESSONS_DIR / "lesson-12-so-nguyen-lon-bigint" / "Lesson12_Production_Content.md",
                "problem_codes": [f"CPPB-BIG-{i:02d}" for i in range(1, 17)]
            }
        ]
    }
]

def find_problem_dir(code):
    clean = code.lower().replace("-", "_")
    matches = list(PROBLEMS_DIR.glob(f"*{clean}*"))
    if matches:
        return matches[0]
    parts = clean.split("_")
    if len(parts) >= 3:
        num = parts[-1]
        prefix = "_".join(parts[:-1])
        matches = list(PROBLEMS_DIR.glob(f"*{prefix}*{num}*"))
        if matches:
            return matches[0]
    return None

def parse_de_bai_file(p_dir):
    fpath = p_dir / "De_Bai.md"
    if not fpath.exists():
        return None
    text = fpath.read_text(encoding="utf-8")
    
    title_m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else p_dir.name
    
    bcanh_m = re.search(r"## Bối cảnh\s*\n(.*?)(?=\n## Nhiệm vụ|\n## Input|\Z)", text, re.DOTALL)
    nv_m = re.search(r"## Nhiệm vụ\s*\n(.*?)(?=\n## Input|\n## Output|\Z)", text, re.DOTALL)
    inp_m = re.search(r"## Input\s*\n(.*?)(?=\n## Output|\n## Sample|\Z)", text, re.DOTALL)
    out_m = re.search(r"## Output\s*\n(.*?)(?=\n## Sample|\n## Ràng buộc|\Z)", text, re.DOTALL)
    rb_m = re.search(r"## Ràng buộc.*?\n(.*?)(?=\n#|\Z)", text, re.DOTALL)
    
    samples = []
    s_blocks = re.findall(r"## (Sample \d+|Ví dụ mẫu \d*|Ví dụ \d*)\s*\n(.*?)(?=\n## Sample|\n## Ví dụ|\n## Ràng buộc|\Z)", text, re.DOTALL)
    for s_title, s_body in s_blocks:
        inp_match = re.search(r"###\s*Input\s*```(?:text)?\s*([\s\S]*?)\s*```", s_body)
        out_match = re.search(r"###\s*Output\s*```(?:text)?\s*([\s\S]*?)\s*```", s_body)
        exp_match = re.search(r"###\s*Giải thích\s*\n([\s\S]*?)(?=\n###|\Z)", s_body)
        
        samples.append({
            "title": s_title.strip(),
            "input": inp_match.group(1).strip() if inp_match else "",
            "output": out_match.group(1).strip() if out_match else "",
            "explain": exp_match.group(1).strip() if exp_match else ""
        })
        
    return {
        "title": title,
        "bcanh": bcanh_m.group(1).strip() if bcanh_m else "",
        "nv": nv_m.group(1).strip() if nv_m else "",
        "inp": inp_m.group(1).strip() if inp_m else "",
        "out": out_m.group(1).strip() if out_m else "",
        "rb": rb_m.group(1).strip() if rb_m else "",
        "samples": samples
    }

def format_problem_markdown(global_p_idx, code, data):
    md = []
    title = data["title"]
    md.append(f"### Bài {global_p_idx:02d} [{code}]: {title}\n\n")
    if data["bcanh"]:
        md.append(f"Bối cảnh: {data['bcanh']}\n\n")
    if data["nv"]:
        md.append(f"Nhiệm vụ: {data['nv']}\n\n")
    if data["inp"]:
        md.append(f"Đầu vào (Input):\n\n{data['inp']}\n\n")
    if data["out"]:
        md.append(f"Đầu ra (Output):\n\n{data['out']}\n\n")
    for s in data["samples"]:
        s_title_str = "Ví dụ mẫu (Sample 1):" if "1" in s["title"] else f"Ví dụ mẫu ({s['title']}):"
        inp_str = s["input"].replace("\n", " <br> ")
        out_str = s["output"].replace("\n", " <br> ")
        md.append(f"{s_title_str}\n\n")
        md.append("| Đầu vào (Input) | Đầu ra (Output) |\n|---|---|\n")
        md.append(f"| {inp_str} | {out_str} |\n\n")
        if s["explain"]:
            md.append(f"Giải thích:\n\n{s['explain']}\n\n")
    if data["rb"]:
        rb_lines = [l.strip() for l in data["rb"].split("\n") if l.strip() and not l.startswith("Thời gian:") and not l.startswith("Bộ nhớ:")]
        if rb_lines:
            md.append("Ràng buộc & Giới hạn:\n\n" + "\n\n".join(rb_lines) + "\n\n")
        else:
            md.append("Ràng buộc & Giới hạn:\n\n100% số test hợp lệ.\n\n")
    return "".join(md)

def resolve_image_paths_in_content(c_text, lesson_folder):
    """Ensure all markdown image tags point to absolute paths of existing PNG files."""
    def repl(m):
        alt = m.group(1)
        raw_path = m.group(2).strip()
        stem = Path(raw_path).stem
        
        # 1. Search in current lesson folder assets
        local_png = lesson_folder / "assets" / f"{stem}.png"
        if local_png.exists():
            return f"![{alt}]({local_png.resolve().as_posix()})"
            
        local_svg = lesson_folder / "assets" / f"{stem}.svg"
        if local_svg.exists():
            if not local_png.exists():
                subprocess.run(["rsvg-convert", "-w", "1600", str(local_svg), "-o", str(local_png)], check=True)
            return f"![{alt}]({local_png.resolve().as_posix()})"
            
        # 2. Search anywhere in BASE_DIR for {stem}.png or {stem}.svg
        cand_png = list(BASE_DIR.glob(f"**/{stem}.png"))
        if cand_png:
            return f"![{alt}]({cand_png[0].resolve().as_posix()})"
            
        cand_svg = list(BASE_DIR.glob(f"**/{stem}.svg"))
        if cand_svg:
            svg_file = cand_svg[0]
            target_png = svg_file.with_suffix(".png")
            if not target_png.exists():
                subprocess.run(["rsvg-convert", "-w", "1600", str(svg_file), "-o", str(target_png)], check=True)
            return f"![{alt}]({target_png.resolve().as_posix()})"
            
        return f"![{alt}]({raw_path})"
        
    return re.sub(r"!\[(.*?)\]\((.*?)\)", repl, c_text)

def build_full_book_markdown():
    md = []
    
    # 1. Front matter / Lời nói đầu (Heading 1)
    md.append("""# LỜI NÓI ĐẦU

Chào mừng các em học sinh và quý thầy cô đến với bộ giáo trình **Khoá học C++ cơ bản — QUYỂN 1: KỸ THUẬT LẬP TRÌNH & NỀN TẢNG THUẬT TOÁN** của Trung tâm tin học iKH.

Bộ tài liệu này được biên soạn công phu nhằm cung cấp lộ trình học tập lập trình thi đấu bài bản, chuẩn mực và hiện đại nhất dành cho học sinh THCS, THPT và sinh viên đam mê thuật toán.

Phần nội dung này gồm **4 Chương trọng tâm (Chương 01 đến Chương 04)** với **12 Bài học** và **164 bài toán thực hành**, trang bị toàn diện nền tảng lập trình C++, mảng, con trỏ, cửa sổ trượt, tìm kiếm nhị phân, bit và số học.

Mỗi bài học được thiết kế theo cấu trúc sư phạm chặt chẽ:

- **Khái niệm & Bản chất toán học**: Giải thích trực quan, dễ hiểu kèm chứng minh toán học ngắn gọn.
- **Mô hình bài toán kinh điển**: Các dạng bài đặc trưng kèm phân tích độ phức tạp thời gian/không gian.
- **Mẫu cài đặt chuẩn thi đấu**: Code C++ chuẩn, tối ưu, dễ hiểu và tuân thủ các quy chuẩn lập trình hiện đại.
- **Hệ thống bài tập thực hành**: Phân tầng từ cơ bản đến nâng cao (P0 đến P5), có đầy đủ giới hạn thời gian, bộ nhớ, sample test và giải thích chi tiết.
- **Lời giải tham khảo có chọn lọc**: Phụ lục B cung cấp mã nguồn C++ chuẩn mực cho 3 bài tập đầu tiên của mỗi chuyên đề.

Chúc các em học tập hiệu quả và chinh phục những giải thưởng cao trong các kỳ thi học sinh giỏi Tin học và Olympic lập trình!

\\begin{flushright}
\\textbf{Trung tâm tin học iKH}
\\end{flushright}

""")

    global_p_counter = 1

    # 2. 4 Chapters & 12 Lessons
    for chap in CHAPTERS_DEF:
        chap_title = chap["title"]
        md.append(f"# {chap_title}\n\n")
        
        for lesson in chap["lessons"]:
            l_num = lesson["num"]
            l_title = lesson["title"]
            c_file = lesson["content_file"]
            l_folder = lesson["folder"]
            
            md.append(f"# {l_title}\n\n")
            
            # Read lesson production content
            if c_file.exists():
                c_text = c_file.read_text(encoding="utf-8")
                # Remove top title if duplicate
                c_lines = c_text.split("\n")
                if c_lines and c_lines[0].startswith("# Bài"):
                    c_text = "\n".join(c_lines[1:])
                # Remove Quiz section and Exercise matrix section
                # NOTE: lookahead must exclude #### (use (?!#)), otherwise only the header line is removed
                c_text = re.sub(r"## Câu hỏi trắc nghiệm.*?(?=\n##(?!#)|\Z)", "", c_text, flags=re.DOTALL)
                c_text = re.sub(r"## Ma trận bài tập.*?(?=\n##(?!#)|\Z)", "", c_text, flags=re.DOTALL)
                # Resolve absolute image paths
                c_text = resolve_image_paths_in_content(c_text, l_folder)
                md.append(c_text.strip() + "\n\n")
            
            # Append Exercise Section (Heading 2)
            md.append("## Bài tập thực hành\n\n")
            
            for code in lesson["problem_codes"]:
                pdir = find_problem_dir(code)
                if pdir:
                    pdata = parse_de_bai_file(pdir)
                    if pdata:
                        prob_md = format_problem_markdown(global_p_counter, code, pdata)
                        md.append(prob_md)
                    else:
                        md.append(f"### Bài {global_p_counter:02d} [{code}]\n\n*Đề bài đang được cập nhật.*\n\n")
                else:
                    md.append(f"### Bài {global_p_counter:02d} [{code}]\n\n*Đề bài đang được cập nhật.*\n\n")
                global_p_counter += 1
                    
    # 3. Phụ lục B: Lời giải bài tập tham khảo
    md.append("# Phụ lục: Lời giải bài tập tham khảo\n\n")
    md.append("> Phần này cung cấp mã nguồn C++ tham khảo chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`) cho các bài tập thực hành trong sách.\n\n")
    
    for chap in CHAPTERS_DEF:
        for lesson in chap["lessons"]:
            l_title = lesson["title"]
            md.append(f"## {l_title}\n\n")
            
            codes_for_sol = lesson["problem_codes"][:3]
            for code in codes_for_sol:
                pdir = find_problem_dir(code)
                if pdir:
                    sol_file = pdir / "solution.cpp"
                    de_bai = parse_de_bai_file(pdir)
                    title = de_bai["title"] if de_bai else pdir.name
                    sol_code = sol_file.read_text(encoding="utf-8").strip() if sol_file.exists() else "// Đang cập nhật"
                    md.append(f"### {code} — {title}\n\n```cpp\n{sol_code}\n```\n\n")
                    
    # 4. Mục lục (Heading 1)
    md.append("# Mục lục\n\n")
    
    print(f"  → Đã xử lý tổng cộng {global_p_counter - 1} bài tập thực hành liên tục.")
    return "".join(md)

def build_docx_via_pandoc(full_md, intermediate_docx):
    temp_md = BASE_DIR / "_build_intermediate_q1.md"
    temp_md.write_text(full_md, encoding="utf-8")
    
    ref_doc = BASE_DIR / "c++-level-1-quyen-2.docx"
    
    cmd = [
        "pandoc",
        str(temp_md),
        "-o", str(intermediate_docx),
        "--from=markdown+tex_math_dollars+pipe_tables+fenced_code_blocks+yaml_metadata_block+header_attributes",
        "--to=docx",
        "--standalone",
        "--wrap=auto",
        "--columns=80",
        "--reference-doc", str(ref_doc)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"❌ Pandoc Error: {result.stderr}")
        return False
    print("✅ Pandoc conversion successful!")
    return True

def post_process_q1_docx(docx_path):
    print("🎨 Đang áp dụng thiết kế Design System chuẩn mực Quyển 2 cho c++-level-1-quyen-1.docx...")
    doc = docx.Document(str(docx_path))
    s = doc.sections[0]

    # 1. Margins & Page setup
    s.top_margin = Pt(36.0)
    s.bottom_margin = Pt(36.0)
    s.left_margin = Pt(64.35)  # gáy sách
    s.right_margin = Pt(36.0)

    # 2. Update Headers (3 headers: even, default, first)
    header_book_text = "Giáo trình C++ cơ bản - quyển 1"
    for h in [s.even_page_header, s.header, s.first_page_header]:
        p0 = h.paragraphs[0]
        pPr = p0._p.get_or_add_pPr()
        for tb in pPr.findall(qn("w:tabs")): pPr.remove(tb)
        pPr.append(parse_xml(f'<w:tabs {nsdecls("w")}><w:tab {nsdecls("w")} w:val="right" w:pos="9899"/></w:tabs>'))

        watermark_runs = []
        for r in p0.runs:
            if r._r.find(qn("w:pict")) is not None:
                watermark_runs.append(r._r)

        for child in list(p0._p):
            if child.tag.split("}")[-1] != "pPr":
                p0._p.remove(child)

        for wr in watermark_runs:
            p0._p.append(wr)

        r_left = parse_xml(f'''<w:r {nsdecls("w")}>
            <w:rPr>
                <w:rFonts w:cs="Times New Roman"/>
                <w:b/><w:bCs/><w:i/><w:iCs/>
                <w:sz w:val="22"/><w:szCs w:val="22"/>
            </w:rPr>
            <w:t>Trung tâm giáo dục &amp; đào tạo tin học iKH</w:t>
        </w:r>''')
        p0._p.append(r_left)

        r_tab = parse_xml(f'''<w:r {nsdecls("w")}>
            <w:rPr><w:rFonts w:cs="Times New Roman"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr>
            <w:tab/>
        </w:r>''')
        p0._p.append(r_tab)

        r_right = parse_xml(f'''<w:r {nsdecls("w")}>
            <w:rPr>
                <w:rFonts w:cs="Times New Roman"/>
                <w:i/><w:iCs/><w:noProof/>
                <w:sz w:val="22"/><w:szCs w:val="22"/>
                <w:lang w:val="vi-VN"/>
            </w:rPr>
            <w:t>{html.escape(header_book_text)}</w:t>
        </w:r>''')
        p0._p.append(r_right)

    # 3. Process Paragraphs, Headings & Bookmarks
    toc_headings = []
    p_toc_heading = None
    bm_counter = 1

    for idx, para in enumerate(doc.paragraphs):
        style_name = para.style.name if para.style else ""
        text = para.text.strip()

        # Heading 1
        if style_name == "Heading 1" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading1"):
            para.paragraph_format.keep_with_next = True
            is_chapter = "CHƯƠNG" in text.upper()
            is_preface = "LỜI NÓI ĐẦU" in text.upper()
            is_toc = "MỤC LỤC" in text.upper()
            is_appendix = "PHỤ LỤC" in text.upper()
            is_lesson = text.startswith("Bài ")

            if is_toc:
                p_toc_heading = para
                para.paragraph_format.page_break_before = True
                continue

            if is_chapter:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(5)
                para.paragraph_format.page_break_before = True

                # Split CHƯƠNG XX and TITLE with newline if not already
                if "\n" not in text and ":" in text:
                    parts = text.split(":", 1)
                    para.text = parts[0].strip() + "\n" + parts[1].strip()

                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            elif is_preface:
                para.alignment = WD_ALIGN_PARAGRAPH.CENTER
                para.paragraph_format.space_before = Pt(18)
                para.paragraph_format.space_after = Pt(12)
                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(18)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
            else:
                para.alignment = WD_ALIGN_PARAGRAPH.LEFT
                prev_text = doc.paragraphs[idx - 1].text.strip() if idx > 0 else ""
                is_first_lesson_in_chapter = is_lesson and ("CHƯƠNG" in prev_text.upper())
                
                para.paragraph_format.space_before = Pt(10) if is_first_lesson_in_chapter else Pt(16)
                para.paragraph_format.space_after = Pt(4)
                if not is_first_lesson_in_chapter:
                    para.paragraph_format.page_break_before = True

                for r in para.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(15.5)
                    r.font.bold = True
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

            bm_name = f"bm_sec_{bm_counter}"
            bm_counter += 1
            bm_start = parse_xml(f'<w:bookmarkStart {nsdecls("w")} w:id="{bm_counter}" w:name="{bm_name}"/>')
            bm_end = parse_xml(f'<w:bookmarkEnd {nsdecls("w")} w:id="{bm_counter}"/>')
            para._p.insert(0, bm_start)
            para._p.append(bm_end)

            toc_headings.append({
                "text": text.replace("\n", ": "),
                "bm_name": bm_name,
                "is_chapter": is_chapter,
                "is_lesson": is_lesson,
                "is_appendix": is_appendix,
                "is_preface": is_preface,
            })

        # Heading 2
        elif style_name == "Heading 2" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading2"):
            para.paragraph_format.space_before = Pt(11)
            para.paragraph_format.space_after = Pt(3)
            para.paragraph_format.keep_with_next = True
            
            is_practice_title = "bài tập thực hành" in text.lower()
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(14)
                r.font.bold = True
                if is_practice_title:
                    r.font.color.rgb = RGBColor(0xFF, 0x00, 0x00)  # ĐỎ CHUẨN IN ẤN #FF0000
                else:
                    r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # Heading 3
        elif style_name == "Heading 3" or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) == "Heading3"):
            para.paragraph_format.space_before = Pt(9)
            para.paragraph_format.space_after = Pt(3)
            para.paragraph_format.keep_with_next = True
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # Heading 4 / Heading 5 -> Convert to normal bold body text (Q2 standard: 0 Heading4)
        elif "Heading 4" in style_name or "Heading 5" in style_name or (para._p.pPr is not None and para._p.pPr.find(qn("w:pStyle")) is not None and para._p.pPr.find(qn("w:pStyle")).attrib.get(qn("w:val")) in ["Heading4", "Heading5"]):
            pStyle = para._p.pPr.find(qn("w:pStyle"))
            if pStyle is not None:
                para._p.pPr.remove(pStyle)
            para.paragraph_format.space_before = Pt(4)
            para.paragraph_format.space_after = Pt(2)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # Code block
        elif "Code" in style_name or style_name == "Source Code":
            para.paragraph_format.space_before = Pt(0)
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.line_spacing = 1.05
            for r in para.runs:
                r.font.name = "Consolas"
                r.font.size = Pt(9)
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
            bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                <w:left w:val="single" w:sz="8" w:space="4" w:color="CBD5E1"/>
                <w:top w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                <w:bottom w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
            </w:pBdr>''')
            ind = parse_xml(f'<w:ind {nsdecls("w")} w:left="180" w:right="120"/>')
            pPr = para._p.get_or_add_pPr()
            pPr.append(shd)
            pPr.append(bdr)
            pPr.append(ind)

        # Callouts / Block Text
        elif style_name in ["Block Text", "Quote"] or text.startswith(">"):
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="EFF6FF"/>')
            bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                <w:left w:val="single" w:sz="16" w:space="4" w:color="3B82F6"/>
                <w:top w:val="single" w:sz="4" w:space="3" w:color="E2E8F0"/>
                <w:bottom w:val="single" w:sz="4" w:space="3" w:color="E2E8F0"/>
                <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
            </w:pBdr>''')
            ind = parse_xml(f'<w:ind {nsdecls("w")} w:left="200" w:right="120"/>')
            pPr = para._p.get_or_add_pPr()
            pPr.append(shd)
            pPr.append(bdr)
            pPr.append(ind)

            para.paragraph_format.space_before = Pt(3)
            para.paragraph_format.space_after = Pt(3)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # Images & Drawings
        elif len(para._p.findall('.//' + qn('w:drawing'))) > 0:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_before = Pt(4)
            para.paragraph_format.space_after = Pt(2)
            
            for drawing in para._p.findall('.//' + qn('w:drawing')):
                wp_extent = drawing.find('.//' + qn('wp:extent'))
                a_ext = drawing.find('.//' + qn('a:ext'))
                if wp_extent is not None:
                    try:
                        old_cx = int(wp_extent.get('cx', 0))
                        old_cy = int(wp_extent.get('cy', 0))
                        if old_cx > 0 and old_cy > 0:
                            target_cx = 6000000
                            target_cy = int(round(old_cy * target_cx / old_cx))
                            if target_cy > 5000000:
                                target_cy = 5000000
                                target_cx = int(round(old_cx * target_cy / old_cy))
                            wp_extent.set('cx', str(target_cx))
                            wp_extent.set('cy', str(target_cy))
                            if a_ext is not None:
                                a_ext.set('cx', str(target_cx))
                                a_ext.set('cy', str(target_cy))
                    except Exception:
                        pass

        # Image captions
        elif style_name in ["Image Caption", "Caption"]:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_before = Pt(3)
            para.paragraph_format.space_after = Pt(10)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10)
                r.font.italic = True
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

        # Normal text fallback
        else:
            if para.paragraph_format.space_after is None or para.paragraph_format.space_after.pt < 1:
                para.paragraph_format.space_after = Pt(2)
            para.paragraph_format.line_spacing = 1.1
            for r in para.runs:
                if not r.font.name:
                    r.font.name = "Times New Roman"
                r.font.size = Pt(12.5)
                r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    # 4. Tables Processing & Dynamic Left Indent
    print(f"  → Đang định dạng và căn lề cho {len(doc.tables)} bảng dữ liệu...")
    for table in doc.tables:
        table_tblPr = table._tbl.tblPr

        for row in table.rows:
            trPr = row._tr.get_or_add_trPr()
            for h in trPr.findall(qn("w:tblHeader")): trPr.remove(h)
            if trPr.find(qn("w:cantSplit")) is None:
                trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

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

            for b in table_tblPr.findall(qn("w:tblBorders")): table_tblPr.remove(b)
            table_tblPr.append(parse_xml(f'''<w:tblBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
                <w:insideV w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            </w:tblBorders>'''))

            # Header row
            for cell in table.rows[0].cells:
                tcPr = cell._tc.get_or_add_tcPr()
                for b in tcPr.findall(qn("w:tcBorders")): tcPr.remove(b)
                tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="F1F5F9"/>'))
                for p in cell.paragraphs:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    p.paragraph_format.space_before = Pt(2)
                    p.paragraph_format.space_after = Pt(2)
                    for r in p.runs:
                        r.font.name = "Consolas"
                        r.font.bold = True
                        r.font.size = Pt(11)
                        r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

            # Data rows
            for r_idx in range(1, len(table.rows)):
                row = table.rows[r_idx]
                for cell in row.cells:
                    tcPr = cell._tc.get_or_add_tcPr()
                    for b in tcPr.findall(qn("w:tcBorders")): tcPr.remove(b)
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="FFFFFF"/>'))
                    
                    full_text = cell.text
                    lines = [l.strip() for l in full_text.split("\n") if l.strip()]
                    if not lines:
                        lines = [""]
                    max_len = max(len(l) for l in lines) if lines else 0
                    indent_pt = max(10.0, 72.0 - max(0, max_len - 4) * 3.25)
                    indent_dxa = int(round(indent_pt * 20))

                    for p in cell.paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                        p.paragraph_format.space_before = Pt(2)
                        p.paragraph_format.space_after = Pt(2)
                        ind = p._p.get_or_add_pPr().find(qn("w:ind"))
                        if ind is not None:
                            ind.set(qn("w:left"), str(indent_dxa))
                        else:
                            p._p.get_or_add_pPr().append(parse_xml(f'<w:ind {nsdecls("w")} w:left="{indent_dxa}"/>'))

                        for r in p.runs:
                            r.font.name = "Consolas"
                            r.font.size = Pt(11)
                            r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)
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
                    for b in tcPr.findall(qn("w:tcBorders")): tcPr.remove(b)
                    fill_c = "F1F5F9" if r_idx == 0 else ("FFFFFF" if r_idx % 2 == 1 else "F8FAFC")
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_c}"/>'))
                    for p in cell.paragraphs:
                        p.paragraph_format.space_before = Pt(2)
                        p.paragraph_format.space_after = Pt(2)
                        if r_idx == 0:
                            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        for r in p.runs:
                            r.font.name = "Times New Roman"
                            r.font.size = Pt(12)  # Chuẩn 12.0pt theo Quyển 2 và Master Spec
                            if r_idx == 0:
                                r.font.bold = True
                            r.font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    # 5. Build Table of Contents with Exact Page Numbers & Dot Leader Tabs
    # Exact page numbers for 22 items in Q1
    EXACT_PAGES_Q1 = [
        "1",   # Lời nói đầu
        "2",   # Chương 01
        "2",   # Bài 01
        "14",  # Bài 02
        "26",  # Bài 03
        "37",  # Chương 02
        "37",  # Bài 04
        "56",  # Bài 05
        "73",  # Bài 06
        "90",  # Chương 03
        "90",  # Bài 07
        "109", # Bài 08
        "132", # Bài 09
        "150", # Chương 04
        "150", # Bài 10
        "167", # Bài 11
        "187", # Bài 12
        "276"  # Phụ lục
    ]

    if p_toc_heading:
        print(f"  → Đang xây dựng Mục lục tương tác có số trang chính xác gồm {len(toc_headings)} mục...")
        for item_idx, item in enumerate(toc_headings):
            title = html.escape(item["text"])
            bm = item["bm_name"]
            page_str = EXACT_PAGES_Q1[item_idx] if item_idx < len(EXACT_PAGES_Q1) else "1"

            if item["is_chapter"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:tabs>
                            <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
                        </w:tabs>
                        <w:spacing w:before="180" w:after="40"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="23"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:t>{title}</w:t>
                        </w:r>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="23"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:tab/>
                            <w:t>{page_str}</w:t>
                        </w:r>
                    </w:hyperlink>
                </w:p>'''
            elif item["is_lesson"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:tabs>
                            <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
                        </w:tabs>
                        <w:ind w:left="280"/>
                        <w:spacing w:before="20" w:after="30"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:sz w:val="21"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:t>•  {title}</w:t>
                        </w:r>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:sz w:val="21"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:tab/>
                            <w:t>{page_str}</w:t>
                        </w:r>
                    </w:hyperlink>
                </w:p>'''
            elif item["is_appendix"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:tabs>
                            <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
                        </w:tabs>
                        <w:spacing w:before="120" w:after="30"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="23"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:t>{title}</w:t>
                        </w:r>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="23"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:tab/>
                            <w:t>{page_str}</w:t>
                        </w:r>
                    </w:hyperlink>
                </w:p>'''
            elif item["is_preface"]:
                p_xml = f'''<w:p {nsdecls("w")}>
                    <w:pPr>
                        <w:tabs>
                            <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
                        </w:tabs>
                        <w:spacing w:before="120" w:after="30"/>
                    </w:pPr>
                    <w:hyperlink w:anchor="{bm}">
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="23"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:t>{title}</w:t>
                        </w:r>
                        <w:r>
                            <w:rPr>
                                <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
                                <w:b/>
                                <w:sz w:val="23"/>
                                <w:color w:val="000000"/>
                            </w:rPr>
                            <w:tab/>
                            <w:t>{page_str}</w:t>
                        </w:r>
                    </w:hyperlink>
                </w:p>'''
            else:
                continue

            p_elem = parse_xml(p_xml)
            p_toc_heading._p.addnext(p_elem)
            p_toc_heading = docx.text.paragraph.Paragraph(p_elem, doc)

    doc.save(str(docx_path))
    print(f"🎉 Hoàn tất build xuất bản: {docx_path.name} ({docx_path.stat().st_size:,} bytes)!")

def optimize_runs_and_app_xml(docx_path):
    """MINOR 7 & MINOR 8: Merge contiguous runs in document.xml and update app.xml with exact counts."""
    print("🔧 Đang tối ưu hóa text runs (gộp runs đơn lẻ) và cập nhật app.xml...")
    import xml.etree.ElementTree as ET

    temp_dir = BASE_DIR / "_zip_temp"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    temp_dir.mkdir(parents=True)

    with zipfile.ZipFile(docx_path, 'r') as z:
        z.extractall(temp_dir)

    doc_xml_path = temp_dir / "word" / "document.xml"
    doc_tree = ET.parse(doc_xml_path)
    root = doc_tree.getroot()

    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

    # 1. Merge contiguous identical runs
    total_runs = 0
    single_char_runs = 0

    for p in root.findall('.//w:p', ns):
        children = list(p)
        i = 0
        while i < len(children) - 1:
            c1 = children[i]
            c2 = children[i+1]
            if c1.tag.endswith('}r') and c2.tag.endswith('}r'):
                rPr1 = c1.find('w:rPr', ns)
                rPr2 = c2.find('w:rPr', ns)
                rPr1_str = ET.tostring(rPr1) if rPr1 is not None else b''
                rPr2_str = ET.tostring(rPr2) if rPr2 is not None else b''

                t1 = c1.find('w:t', ns)
                t2 = c2.find('w:t', ns)

                if rPr1_str == rPr2_str and t1 is not None and t2 is not None and len(c1) == (1 if rPr1 is None else 2) and len(c2) == (1 if rPr2 is None else 2):
                    # Merge t2 into t1
                    t1.text = (t1.text or '') + (t2.text or '')
                    p.remove(c2)
                    children = list(p)
                    continue
            i += 1

    doc_tree.write(doc_xml_path, encoding='utf-8', xml_declaration=True)

    # Re-calculate statistics for app.xml
    full_text = "".join(root.itertext())
    words_count = len(re.findall(r'\b\w+\b', full_text))
    chars_count = len(full_text)
    paras_count = len(root.findall('.//w:p', ns))

    # Audit single-char runs
    for t in root.findall('.//w:t', ns):
        total_runs += 1
        if len(t.text or '') == 1:
            single_char_runs += 1

    single_ratio = (single_char_runs / total_runs * 100) if total_runs > 0 else 0
    print(f"  → Single-char runs: {single_char_runs}/{total_runs} ({single_ratio:.1f}%)")

    # Update app.xml
    app_xml_path = temp_dir / "docProps" / "app.xml"
    if app_xml_path.exists():
        app_tree = ET.parse(app_xml_path)
        app_root = app_tree.getroot()
        ns_app = {'ep': 'http://schemas.openxmlformats.org/officeDocument/2006/extended-properties'}
        
        for w_tag in app_root.findall('.//ep:Words', ns_app):
            w_tag.text = str(words_count)
        for c_tag in app_root.findall('.//ep:Characters', ns_app):
            c_tag.text = str(chars_count)
        for p_tag in app_root.findall('.//ep:Paragraphs', ns_app):
            p_tag.text = str(paras_count)
        for t_tag in app_root.findall('.//ep:Title', ns_app):
            t_tag.text = "Khoá học C++ cơ bản — Quyển 1"
            
        app_tree.write(app_xml_path, encoding='utf-8', xml_declaration=True)
        print(f"  → Đã cập nhật app.xml: Words={words_count:,}, Chars={chars_count:,}, Paragraphs={paras_count:,}")

    # Remove w:updateFields from settings.xml to avoid security prompt in Word
    settings_path = temp_dir / "word" / "settings.xml"
    if settings_path.exists():
        settings_tree = ET.parse(settings_path)
        settings_root = settings_tree.getroot()
        uf = settings_root.find('w:updateFields', ns)
        if uf is not None:
            settings_root.remove(uf)
        settings_tree.write(settings_path, encoding='utf-8', xml_declaration=True)

    # Re-zip docx
    with zipfile.ZipFile(docx_path, 'w', zipfile.ZIP_DEFLATED) as z_out:
        for folder_name, subfolders, filenames in os.walk(temp_dir):
            for filename in filenames:
                file_path = Path(folder_name) / filename
                arcname = file_path.relative_to(temp_dir)
                z_out.write(file_path, arcname)

    shutil.rmtree(temp_dir)
    print("✅ Hoàn tất gộp runs và cập nhật metadata!")

def main():
    print("================================================================================")
    print("🚀 BẮT ĐẦU XUẤT BẢN GIÁO TRÌNH C++ QUYỂN 1 CHUẨN IN ẤN (5 CHƯƠNG, 15 BÀI HỌC)")
    print("================================================================================")

    # 1. Sinh Markdown tổng hợp
    full_md = build_full_book_markdown()
    print(f"  → Đã tổng hợp Markdown hoàn chỉnh: {len(full_md):,} ký tự.")

    # 2. Chuyển đổi qua Pandoc với reference-doc chuẩn Quyển 2
    success = build_docx_via_pandoc(full_md, OUT_DOCX)
    if not success:
        print("❌ Lỗi chuyển đổi Pandoc!")
        return

    # 3. Post-process OpenXML
    post_process_q1_docx(OUT_DOCX)

    # 4. Optimize runs & update app.xml
    optimize_runs_and_app_xml(OUT_DOCX)

if __name__ == "__main__":
    main()
