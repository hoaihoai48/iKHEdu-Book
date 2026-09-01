#!/usr/bin/env python3
"""
Build script: Tạo file Word (.docx) xuất bản từ MASTER_ALL_LESSONS.md
Khoá học C++ cơ bản — Trung tâm tin học iKH

Chuẩn cấu trúc Sách Giáo Khoa (SGK):
- CHƯƠNG 01 -> 07 (thay vì Module)
- Bài 01 -> 21 (thay vì Chuyên đề)
- Nhúng trọn bộ 39 hình ảnh minh họa độ phân giải cao (SVG -> PNG)
- Loại bỏ trang trắng đơn độc sau tiêu đề Chương (Chương + Bài 1 nằm cùng trang)
- Bảng biểu: căn giữa 2 chiều (vertical & horizontal), chữ/toán Header trắng tinh khiết, viền mảnh
- Bỏ dòng thời gian/bộ nhớ trong đề bài
- Mục lục: Interactive Hyperlinks (bấm vào là nhảy ngay tới Chương/Bài đó)
"""

import os
import re
import sys
import glob
import html
import subprocess
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================
BOOK_TITLE = "Khoá học C++ cơ bản"
BOOK_SUBTITLE = "Từ nền tảng lập trình đến thuật toán thi đấu"
BOOK_AUTHOR = "Trung tâm tin học iKH"

BASE_DIR = Path(__file__).parent
MASTER_FILE = BASE_DIR / "MASTER_ALL_LESSONS.md"
FOUNDATION_FILE = BASE_DIR / "source" / "level0" / "IKHEDU_Level0_Foundation.md"
PROBLEMS_DIR = BASE_DIR / "problems"
OUTPUT_FILE = BASE_DIR / "IKHEDU_CPP_Co_Ban_Xuat_Ban.docx"

# Problem code prefix mapping to directory prefix
CODE_TO_DIR_PREFIX = {
    "CPPB-SX": "cppb_sx",
    "CPPB-HCT": "cppb_hct",
    "CPPB-CST": "cppb_cst",
    "CPPB-PT": "cppb_pt",
    "CPPB-BS": "cppb_bs",
    "CPPB-BIT": "cppb_bit",
    "CPPB-NT": "cppb_nt",
    "CPPB-MOD": "cppb_mod",
    "CPPB-BIG": "cppb_big",
    "CPPB-REC": "cppb_rec",
    "CPPB-DAC": "cppb_dac",
    "CPPB-BKT": "cppb_bkt",
    "CPPB-DP1": "cppb_dp1",
    "CPPB-DP2": "cppb_dp2",
    "CPPB-DPS": "cppb_dps",
    "CPPB-STL": "cppb_stl",
    "CPPB-STK": "cppb_stk",
    "CPPB-QUE": "cppb_que",
    "CPPB-GRA": "cppb_gra",
    "CPPB-GRD": "cppb_grd",
    "CPPB-RNG": "cppb_rng",
}

# ============================================================
# PHASE 0: Ensure all SVG illustrations are converted to high-res PNG
# ============================================================

def convert_svg_to_png():
    """Convert all SVG files in lessons to 1600px high-res PNGs for Word embedding."""
    svg_files = list(BASE_DIR.glob("lessons/**/assets/*.svg"))
    converted_count = 0

    for svg in svg_files:
        png = svg.with_suffix(".png")
        if not png.exists() or png.stat().st_mtime < svg.stat().st_mtime:
            cmd = ["qlmanage", "-t", "-s", "1600", "-o", str(svg.parent), str(svg)]
            subprocess.run(cmd, capture_output=True)
            ql_out = svg.parent / f"{svg.name}.png"
            if ql_out.exists():
                ql_out.rename(png)
                converted_count += 1

    if converted_count > 0:
        print(f"  → Đã chuyển đổi {converted_count} hình ảnh SVG sang PNG độ phân giải cao")


def resolve_and_embed_images(content):
    """Map any image links in Markdown to their absolute high-res PNG file paths."""
    png_map = {}
    for p in BASE_DIR.glob("lessons/**/assets/*.png"):
        png_map[p.name] = str(p)
        svg_name = p.stem + ".svg"
        png_map[svg_name] = str(p)

    def replace_img(match):
        alt = match.group(1)
        orig_path = match.group(2)
        filename = Path(orig_path).name

        if filename in png_map:
            return f"\n\n![{alt}]({png_map[filename]})\n\n"
        return match.group(0)

    content = re.sub(r"!\[(.*?)\]\((.*?)\)", replace_img, content)
    return content


# ============================================================
# PHASE 1: Pre-process markdown
# ============================================================

def read_file(path):
    """Read file content with UTF-8 encoding."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def find_problem_dir(code):
    """Find the problem directory for a given problem code like CPPB-SX-01."""
    match = re.match(r"(CPPB-[A-Z]+\d*)-(\d+)", code)
    if not match:
        return None
    prefix = match.group(1)
    num = match.group(2)

    dir_prefix = CODE_TO_DIR_PREFIX.get(prefix)
    if not dir_prefix:
        return None

    pattern = f"{dir_prefix}_{num}_*"
    matches = list(PROBLEMS_DIR.glob(pattern))
    if matches:
        return matches[0]
    return None


def read_problem_statement(problem_dir):
    """Read De_Bai.md from a problem directory."""
    de_bai = problem_dir / "De_Bai.md"
    if de_bai.exists():
        return read_file(de_bai)
    return None


def read_solution(problem_dir):
    """Read solution.cpp from a problem directory."""
    sol = problem_dir / "solution.cpp"
    if sol.exists():
        return read_file(sol)
    return None


def extract_problem_codes_from_table(table_text):
    """Extract problem codes like CPPB-SX-01 from a markdown table."""
    return re.findall(r"`(CPPB-[A-Z]+\d*-\d+)`", table_text)


def remove_quiz_sections(lines):
    """Remove all quiz sections from the content."""
    result = []
    skip = False
    i = 0

    while i < len(lines):
        line = lines[i]

        if re.match(r"^##\s+.*(?:Câu hỏi trắc nghiệm|Hệ thống câu hỏi kiểm tra khái niệm)", line):
            skip = True
            i += 1
            continue

        if skip:
            if re.match(r"^#{1,2}\s", line) and not re.match(r"^###", line):
                skip = False
                result.append(line)
            i += 1
            continue

        result.append(line)
        i += 1

    return result


def remove_overview_toc(lines):
    """Remove the overview TOC section."""
    result = []
    skip = False
    i = 0

    while i < len(lines):
        line = lines[i]

        if line.strip() == "## MỤC LỤC TỔNG QUAN":
            skip = True
            i += 1
            continue

        if skip:
            if line.startswith("===") or line.startswith("# MODULE") or line.startswith("# CHƯƠNG") or "BẮT ĐẦU NỘI DUNG" in line:
                skip = False
                result.append(line)
            i += 1
            continue

        result.append(line)
        i += 1

    return result


def format_problem_statement(statement, code, idx=1):
    """Format a problem statement cleanly for textbook publishing:
    - Combine problem number, code, and title into a single Heading 3: '### Bài 01 [CPPB-SX-01]: Xếp Hàng Điểm Danh'
    - Format Sample I/O into a clean 2-column Table (Đầu vào | Đầu ra)
    - Ensure bullet lists (Input, Output, Ràng buộc) have proper blank lines so lines never collapse into a single line
    - Filter out boilerplate lines like 'Thời gian: 1.0s, Bộ nhớ: 256MB'
    - Convert internal ## headings into bold inline labels
    """
    lines = statement.strip().split("\n")
    title = ""
    sections = {}
    current_sec = "other"
    sec_content = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("# "):
            title = line[2:].strip()
            i += 1
            continue
            
        m_h2 = re.match(r"^##\s+(.+)$", line)
        if m_h2:
            if sec_content:
                sections[current_sec] = "\n".join(sec_content).strip()
            current_sec = m_h2.group(1).strip()
            sec_content = []
            i += 1
            continue
            
        sec_content.append(line)
        i += 1
        
    if sec_content:
        sections[current_sec] = "\n".join(sec_content).strip()
        
    out = []
    out.append(f"### Bài {idx:02d} [{code}]: {title}\n")
    
    if "Bối cảnh" in sections and sections["Bối cảnh"]:
        out.append(f"**Bối cảnh:** {sections['Bối cảnh']}\n")
        
    if "Nhiệm vụ" in sections and sections["Nhiệm vụ"]:
        out.append(f"**Nhiệm vụ:** {sections['Nhiệm vụ']}\n")
        
    if "Input" in sections and sections["Input"]:
        input_text = sections["Input"].strip()
        out.append(f"**Đầu vào (Input):**\n\n{input_text}\n")
        
    if "Output" in sections and sections["Output"]:
        output_text = sections["Output"].strip()
        out.append(f"**Đầu ra (Output):**\n\n{output_text}\n")
        
    # Handle Sample -> Format as clean 2-column Table
    sample_key = next((k for k in sections if "Sample" in k or "Ví dụ" in k), None)
    if sample_key:
        sample_text = sections[sample_key]
        inp_match = re.search(r"###\s*Input\s*```(?:text)?\s*([\s\S]*?)\s*```", sample_text)
        out_match = re.search(r"###\s*Output\s*```(?:text)?\s*([\s\S]*?)\s*```", sample_text)
        
        if inp_match and out_match:
            inp_lines = inp_match.group(1).strip().replace("\n", " <br> ")
            out_lines = out_match.group(1).strip().replace("\n", " <br> ")
            out.append(f"**Ví dụ mẫu ({sample_key}):**\n\n| Đầu vào (Input) | Đầu ra (Output) |\n|---|---|\n| {inp_lines} | {out_lines} |\n")
        else:
            out.append(f"**Ví dụ mẫu ({sample_key}):**\n\n{sample_text}\n")
            
    if "Ràng buộc" in sections and sections["Ràng buộc"]:
        rb_text = sections["Ràng buộc"].strip()
        rb_lines = [l for l in rb_text.split("\n") if not re.search(r"Thời gian|Bộ nhớ", l, re.IGNORECASE)]
        clean_rb = "\n".join(rb_lines).strip()
        if clean_rb:
            out.append(f"**Ràng buộc & Giới hạn:**\n\n{clean_rb}\n")
    elif "Giới hạn" in sections and sections["Giới hạn"]:
        gh_text = sections["Giới hạn"].strip()
        gh_lines = [l for l in gh_text.split("\n") if not re.search(r"Thời gian|Bộ nhớ", l, re.IGNORECASE)]
        clean_gh = "\n".join(gh_lines).strip()
        if clean_gh:
            out.append(f"**Ràng buộc & Giới hạn:**\n\n{clean_gh}\n")
        
    return "\n".join(out) + "\n\n"


def replace_exercise_matrices_with_problems(lines):
    """Replace exercise matrix sections (including 'Phân tầng lộ trình', 'Ghi chú', and table)
    with clean '## Bài tập thực hành' and full problem statements from De_Bai.md.
    """
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Match exercise matrix heading
        if re.match(r"^##\s+(?:\d+\.\s+)?Ma trận bài tập thực hành", line):
            section_lines = [line]
            i += 1
            while i < len(lines):
                next_line = lines[i]
                if (
                    next_line.startswith("# ")
                    or next_line.startswith("# CHƯƠNG")
                    or next_line.startswith("# Bài")
                    or next_line.startswith("<!--")
                    or re.match(r"^={3,}$", next_line.strip())
                ):
                    break
                section_lines.append(next_line)
                i += 1

            section_text = "\n".join(section_lines)
            codes = extract_problem_codes_from_table(section_text)

            result.append("## Bài tập thực hành\n\n")

            for idx, code in enumerate(codes, 1):
                problem_dir = find_problem_dir(code)
                if problem_dir:
                    statement = read_problem_statement(problem_dir)
                    if statement:
                        formatted = format_problem_statement(statement, code, idx)
                        result.append(formatted)
                    else:
                        result.append(f"### Bài {idx:02d} [{code}]\n\n*Đề bài chưa có.*\n\n")
                else:
                    result.append(f"### Bài {idx:02d} [{code}]\n\n*Đề bài chưa có.*\n\n")

            continue

        result.append(line)
        i += 1

    return result


def ensure_markdown_list_blank_lines(lines):
    """Ensure all Markdown bullet lists (*, -, +) and numbered lists (1., 2., ...)
    have a blank line before them, so Pandoc never merges list items into a single paragraph line.
    """
    result = []
    list_pattern = re.compile(r"^(?:[\*\-\+]|\d+\.)\s+")
    bq_list_pattern = re.compile(r"^>\s*(?:[\*\-\+]|\d+\.)\s+")

    for i, line in enumerate(lines):
        stripped = line.strip()

        is_list = bool(list_pattern.match(stripped))
        is_bq_list = bool(bq_list_pattern.match(stripped))

        if is_list and len(result) > 0:
            prev = result[-1].strip()
            prev_is_list = bool(list_pattern.match(prev))
            if prev and not prev_is_list and not prev.startswith("```"):
                result.append("")

        elif is_bq_list and len(result) > 0:
            prev = result[-1].strip()
            prev_is_bq_list = bool(bq_list_pattern.match(prev))
            if prev and not prev_is_bq_list and not prev.startswith("```") and not prev.startswith("> ```"):
                result.append(">")

        result.append(line)

    return result


def clean_separators(lines):
    """Clean up separator lines (===, ----, <!-- ... -->) completely to avoid clutter lines."""
    result = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^={3,}$", stripped) or re.match(r"^-{3,}$", stripped):
            continue
        if re.match(r"^<!--.*-->$", stripped):
            continue
        result.append(line)

    return result


def build_front_matter():
    """Build front matter markdown: Lời nói đầu."""
    preface = f"""
# Lời nói đầu

Cuốn sách **{BOOK_TITLE}** được biên soạn bởi **{BOOK_AUTHOR}** nhằm cung cấp cho các em học sinh một lộ trình học tập toàn diện, hệ thống và chuyên sâu về lập trình C++ — từ nền tảng cơ bản đến các thuật toán nâng cao trong lập trình thi đấu.

Sách được thiết kế dành cho học sinh chuẩn bị tham gia các kỳ thi **Tin học trẻ Bảng B**, **Học sinh giỏi THCS** và các cuộc thi lập trình thuật toán. Nội dung được tổ chức theo **7 Chương trọng tâm** với **21 Bài học** bao phủ toàn bộ kiến thức cần thiết, từ thuật toán sắp xếp, kỹ thuật hai con trỏ, cửa sổ trượt, mảng tiền tố, tìm kiếm nhị phân cho đến quy hoạch động, cấu trúc dữ liệu nâng cao, đồ thị và cây truy vấn đoạn.

Mỗi bài học trong sách tuân theo một khung logic sư phạm nhất quán:

- **Khái niệm & bản chất toán học** — giúp học sinh hiểu sâu thay vì chỉ nhớ cú pháp.
- **Chứng minh & bất biến thuật toán** — rèn tư duy phân tích nghiêm ngặt.
- **Mẫu cài đặt chuẩn thi đấu** — code C++ sạch, tối ưu, sẵn sàng nộp bài.
- **Bẫy lỗi lập trình kinh điển** — cảnh báo những sai lầm phổ biến nhất.
- **Bài tập thực hành phân tầng** — từ cơ bản đến nâng cao, mỗi bài có đề bài chi tiết.

Toàn bộ code C++ trong sách tuân theo chuẩn thi đấu iKHEDU: sử dụng `#include <bits/stdc++.h>`, Fast I/O và Safe Input, giúp học sinh làm quen với phong cách lập trình chuyên nghiệp ngay từ đầu.

Chúng tôi tin rằng lập trình không chỉ là viết code, mà là **tư duy giải quyết vấn đề**. Mỗi bài toán trong sách đều được thiết kế để rèn luyện khả năng phân tích, mô hình hóa và tối ưu hóa — những kỹ năng sẽ đồng hành cùng các em trong suốt hành trình học tập và sự nghiệp.

Chúc các em học tập hiệu quả và đạt kết quả cao!

**{BOOK_AUTHOR}**

\\newpage

"""
    return preface


def build_back_matter_foundation():
    """Build Appendix A: Foundation content."""
    content = read_file(FOUNDATION_FILE)
    result = "\n\\newpage\n\n"
    result += "# Phụ lục A: Nền tảng C++\n\n"
    result += "> Phần này ôn tập nhanh các kiến thức nền tảng C++ cần thiết trước khi học thuật toán.\n\n"
    result += content
    return result


def collect_all_solutions():
    """Collect all solution.cpp files organized by chapter/lesson."""
    topic_order = [
        ("Chương 01 — Bài 01: Sắp xếp", "cppb_sx"),
        ("Chương 01 — Bài 02: Hai con trỏ", "cppb_hct"),
        ("Chương 01 — Bài 03: Cửa sổ trượt", "cppb_cst"),
        ("Chương 02 — Bài 04: Mảng tiền tố", "cppb_pt"),
        ("Chương 02 — Bài 05: Tìm kiếm nhị phân", "cppb_bs"),
        ("Chương 02 — Bài 06: Phép toán bit", "cppb_bit"),
        ("Chương 03 — Bài 07: Ước, bội & số nguyên tố", "cppb_nt"),
        ("Chương 03 — Bài 08: Đồng dư & lũy thừa", "cppb_mod"),
        ("Chương 03 — Bài 09: Số nguyên lớn", "cppb_big"),
        ("Chương 04 — Bài 10: Đệ quy", "cppb_rec"),
        ("Chương 04 — Bài 11: Chia để trị", "cppb_dac"),
        ("Chương 04 — Bài 12: Quay lui & nhánh cận", "cppb_bkt"),
        ("Chương 05 — Bài 13: QHĐ 1D & LIS", "cppb_dp1"),
        ("Chương 05 — Bài 14: QHĐ 2D & Knapsack", "cppb_dp2"),
        ("Chương 05 — Bài 15: QHĐ chuỗi & LCS", "cppb_dps"),
        ("Chương 06 — Bài 16: STL nâng cao", "cppb_stl"),
        ("Chương 06 — Bài 17: Stack & Monotonic Stack", "cppb_stk"),
        ("Chương 06 — Bài 18: Queue & Deque", "cppb_que"),
        ("Chương 07 — Bài 19: Đồ thị BFS & DFS", "cppb_gra"),
        ("Chương 07 — Bài 20: Đồ thị lưới 2D", "cppb_grd"),
        ("Chương 07 — Bài 21: Segment Tree & Fenwick Tree", "cppb_rng"),
    ]

    result = "\n\\newpage\n\n"
    result += "# Phụ lục B: Bài giải\n\n"
    result += "> Phần này chứa lời giải tham khảo (code C++) cho toàn bộ bài tập trong sách. "
    result += "Hãy tự cố gắng giải bài ít nhất 30 phút trước khi xem bài giải.\n\n"

    total_solutions = 0

    for topic_title, dir_prefix in topic_order:
        dirs = sorted(PROBLEMS_DIR.glob(f"{dir_prefix}_*"))

        if not dirs:
            continue

        result += f"## {topic_title}\n\n"

        for pdir in dirs:
            sol_file = pdir / "solution.cpp"
            if not sol_file.exists():
                continue

            dir_name = pdir.name
            parts = dir_name.split("_")
            if len(parts) > 3:
                name_parts = parts[3:]
                problem_name = " ".join(p.capitalize() for p in name_parts)
            else:
                problem_name = dir_name

            prefix_upper = dir_prefix.upper().replace("_", "-")
            num = parts[2] if len(parts) > 2 else "00"
            code = f"{prefix_upper}-{num}"

            solution_code = read_file(sol_file)

            result += f"### `{code}` — {problem_name}\n\n"
            result += f"```cpp\n{solution_code}\n```\n\n"
            total_solutions += 1

    print(f"  → Collected {total_solutions} solutions")
    return result


def remove_top_header_and_metadata(lines):
    """Remove the top-level header and metadata block from MASTER_ALL_LESSONS."""
    result = []
    i = 0
    skip_header = True

    while i < len(lines):
        line = lines[i]

        if skip_header:
            if line.startswith("# MODULE") or line.startswith("# CHƯƠNG") or "BẮT ĐẦU NỘI DUNG" in line:
                skip_header = False
                if "BẮT ĐẦU NỘI DUNG" in line:
                    i += 1
                    continue
                result.append(line)
            i += 1
            continue

        result.append(line)
        i += 1

    return result


def preprocess_markdown():
    """Main pre-processing pipeline."""
    print("📖 Đang xử lý MASTER_ALL_LESSONS.md...")

    # Step 0: Ensure all SVGs are converted to PNG
    convert_svg_to_png()

    content = read_file(MASTER_FILE)

    # Convert MODULE -> CHƯƠNG and Chuyên đề -> Bài
    content = re.sub(r"# MODULE (\d+)", r"# CHƯƠNG \1", content)
    content = re.sub(r"MODULE (\d+)", r"CHƯƠNG \1", content)
    content = re.sub(r"# Chuyên đề (\d+)", r"# Bài \1", content)
    content = re.sub(r"Chuyên đề (\d+)", r"Bài \1", content)

    # Resolve all image links to absolute PNG paths
    content = resolve_and_embed_images(content)

    lines = content.split("\n")
    original_count = len(lines)
    print(f"  → Đọc {original_count} dòng")

    # Step 1: Remove overview TOC
    lines = remove_overview_toc(lines)
    print(f"  → Loại bỏ Mục lục tổng quan: còn {len(lines)} dòng")

    # Step 2: Remove top header and metadata
    lines = remove_top_header_and_metadata(lines)
    print(f"  → Loại bỏ header/metadata: còn {len(lines)} dòng")

    # Step 3: Remove quiz sections
    lines = remove_quiz_sections(lines)
    print(f"  → Loại bỏ Quiz: còn {len(lines)} dòng")

    # Step 4: Replace exercise matrices with full problem statements (removes Phân tầng lộ trình)
    print("  → Đang inject đề bài từ problems/ (bỏ phân tầng, tạo bảng 2 cột)...")
    lines = replace_exercise_matrices_with_problems(lines)
    print(f"  → Inject đề bài xong: {len(lines)} dòng")

    # Step 5: Clean separators
    lines = clean_separators(lines)

    # Step 6: Fix list linebreaks (ensures bullet & numbered lists never collapse onto one line)
    lines = ensure_markdown_list_blank_lines(lines)

    # Build front matter
    front = build_front_matter()

    # Build back matter
    print("  → Đang xây dựng Phụ lục A (Nền tảng C++)...")
    foundation = build_back_matter_foundation()

    print("  → Đang thu thập Phụ lục B (Bài giải)...")
    solutions = collect_all_solutions()

    # Empty placeholder for TOC section (will be populated with interactive hyperlinks in postprocess)
    toc_section = "\n\\newpage\n\n# Mục lục\n\n"

    # Assemble final markdown
    body = "\n".join(lines)

    final_md = f"""---
title: "{BOOK_TITLE}"
subtitle: "{BOOK_SUBTITLE}"
author: "{BOOK_AUTHOR}"
lang: vi
documentclass: report
geometry: "a4paper, margin=2.5cm"
fontsize: 12pt
mainfont: "Times New Roman"
monofont: "Courier New"
header-includes:
  - \\usepackage{{fancyhdr}}
  - \\pagestyle{{fancy}}
  - \\fancyhead[L]{{\\textit{{{BOOK_TITLE}}}}}
  - \\fancyhead[R]{{\\textit{{{BOOK_AUTHOR}}}}}
---

{front}

{body}

{foundation}

{solutions}

{toc_section}
"""

    return final_md


# ============================================================
# PHASE 2: Build docx via pandoc
# ============================================================

def build_with_pandoc(markdown_content):
    """Convert markdown to docx using pandoc."""
    print("\n🔧 Đang chạy Pandoc chuyển đổi Markdown → Word...")

    temp_md = BASE_DIR / "_build_intermediate.md"
    with open(temp_md, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"  → Đã ghi file trung gian: {temp_md.name} ({temp_md.stat().st_size:,} bytes)")

    cmd = [
        "pandoc",
        str(temp_md),
        "-o", str(OUTPUT_FILE),
        "--from=markdown+tex_math_dollars+pipe_tables+fenced_code_blocks+yaml_metadata_block+header_attributes",
        "--to=docx",
        "--standalone",
        "--wrap=auto",
        "--columns=80",
    ]

    ref_doc = BASE_DIR / "_reference.docx"
    if ref_doc.exists():
        cmd.extend(["--reference-doc", str(ref_doc)])

    print(f"  → Chạy: {' '.join(cmd[:5])}...")

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  ❌ Pandoc lỗi: {result.stderr}")
        return False

    print(f"  ✅ Pandoc thành công!")
    return True


# ============================================================
# PHASE 3: Post-process with python-docx
# ============================================================

def postprocess_docx():
    """Post-process the generated docx for professional publishing aesthetics."""
    print("\n🎨 Đang áp dụng Design System xuất bản chuyên nghiệp...")

    from docx import Document
    from docx.shared import Pt, Inches, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import parse_xml, OxmlElement
    from docx.oxml.ns import nsdecls, qn

    doc = Document(str(OUTPUT_FILE))

    # ============================================================
    # 1. PAGE SETUP & MARGINS
    # ============================================================
    for section in doc.sections:
        section.page_width = Cm(21)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.2)
        section.right_margin = Cm(2.0)
        section.different_first_page_header_footer = True

        # Header for page 2+
        header = section.header
        p_head = header.paragraphs[0] if header.paragraphs else header.add_paragraph()
        p_head.text = f"{BOOK_TITLE}  •  {BOOK_AUTHOR}"
        p_head.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        for run in p_head.runs:
            run.font.name = "Times New Roman"
            run.font.size = Pt(8.5)
            run.font.italic = True
            run.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

        pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="4" w:space="4" w:color="CBD5E1"/></w:pBdr>')
        p_head._p.get_or_add_pPr().append(pBdr)

        # Footer for page 2+ (Page numbering)
        footer = section.footer
        p_foot = footer.paragraphs[0] if footer.paragraphs else footer.add_paragraph()
        p_foot.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        run_f1 = p_foot.add_run("—  ")
        run_f1.font.name = "Times New Roman"
        run_f1.font.size = Pt(9)
        run_f1.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)
        
        fldSimple = parse_xml(f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"/>')
        p_foot._p.append(fldSimple)
        
        run_f2 = p_foot.add_run("  —")
        run_f2.font.name = "Times New Roman"
        run_f2.font.size = Pt(9)
        run_f2.font.color.rgb = RGBColor(0x64, 0x74, 0x8B)

    # ============================================================
    # 2. STYLES DEFINITION
    # ============================================================
    style = doc.styles

    if "Normal" in [s.name for s in style]:
        normal = style["Normal"]
        normal.font.name = "Times New Roman"
        normal.font.size = Pt(11)
        normal.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)
        normal.paragraph_format.line_spacing = 1.2
        normal.paragraph_format.space_after = Pt(4)

    # ============================================================
    # 3. COVER PAGE TRANSFORMATION
    # ============================================================
    if len(doc.paragraphs) >= 3:
        p0 = doc.paragraphs[0]
        p1 = doc.paragraphs[1]
        p2 = doc.paragraphs[2]

        p0.text = "GIÁO TRÌNH LẬP TRÌNH THI ĐẤU  •  C++ BẢNG B"
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.paragraph_format.space_before = Pt(40)
        p0.paragraph_format.space_after = Pt(90)
        if p0.runs:
            p0.runs[0].font.name = "Times New Roman"
            p0.runs[0].font.size = Pt(10.5)
            p0.runs[0].font.bold = True
            p0.runs[0].font.color.rgb = RGBColor(0x1A, 0x4A, 0x6B)

        p1.text = "KHOÁ HỌC C++ CƠ BẢN"
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(12)
        if p1.runs:
            p1.runs[0].font.name = "Times New Roman"
            p1.runs[0].font.size = Pt(28)
            p1.runs[0].font.bold = True
            p1.runs[0].font.color.rgb = RGBColor(0x0F, 0x2A, 0x44)

        p2.text = "Từ nền tảng lập trình đến thuật toán thi đấu"
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(14)
        if p2.runs:
            p2.runs[0].font.name = "Times New Roman"
            p2.runs[0].font.size = Pt(13.5)
            p2.runs[0].font.italic = True
            p2.runs[0].font.color.rgb = RGBColor(0x2E, 0x5E, 0x8A)

        p_div = parse_xml(f'<w:p {nsdecls("w")}><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="200"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="16"/><w:color w:val="94A3B8"/></w:rPr><w:t>──────────────────────────────────────────</w:t></w:r></w:p>')
        p2._p.addnext(p_div)

        p_tag = parse_xml(f'<w:p {nsdecls("w")}><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="4200"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="21"/><w:color w:val="475569"/></w:rPr><w:t>Giáo trình 7 Chương trọng tâm &amp; 323 Bài toán thực hành có lời giải chi tiết</w:t></w:r></w:p>')
        p_div.addnext(p_tag)

        p_auth = parse_xml(f'<w:p {nsdecls("w")}><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="100"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b/><w:sz w:val="26"/><w:color w:val="0F2A44"/></w:rPr><w:t>TRUNG TÂM TIN HỌC iKH</w:t></w:r></w:p>')
        p_tag.addnext(p_auth)

        p_ver = parse_xml(f'<w:p {nsdecls("w")}><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="0"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="18"/><w:color w:val="64748B"/></w:rPr><w:t>Phiên bản xuất bản 2026  •  Tài liệu lưu hành nội bộ</w:t></w:r></w:p>')
        p_auth.addnext(p_ver)

    # ============================================================
    # 4. BOOKMARKS & PARAGRAPHS STYLING
    # ============================================================
    toc_headings = []
    bm_counter = 1
    p_toc_heading = None

    for idx, para in enumerate(doc.paragraphs):
        style_name = para.style.name if para.style else ""
        text = para.text.strip()

        if idx < 3:
            continue

        # --- A. HEADINGS ---
        if style_name == "Heading 1":
            is_chapter = text.startswith("CHƯƠNG")
            is_lesson = text.startswith("Bài")
            is_preface = "Lời nói đầu" in text
            is_appendix = text.startswith("Phụ lục")
            is_toc = "Mục lục" in text

            # Check if this is the first lesson right below a Chapter
            prev_text = doc.paragraphs[idx - 1].text.strip() if idx > 0 else ""
            is_first_lesson_in_chapter = is_lesson and prev_text.startswith("CHƯƠNG")

            para.paragraph_format.space_before = Pt(28) if is_chapter else (Pt(12) if is_first_lesson_in_chapter else Pt(20))
            para.paragraph_format.space_after = Pt(8)
            para.paragraph_format.keep_with_next = True
            
            # Page break before Chapter, Preface, Appendix, TOC, and subsequent Lessons (NOT first lesson in chapter)
            if not is_first_lesson_in_chapter:
                para._p.get_or_add_pPr().append(parse_xml(f'<w:pageBreakBefore {nsdecls("w")}/>'))

            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(17.5) if is_chapter else Pt(15)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x0F, 0x2A, 0x44) if is_chapter else RGBColor(0x1A, 0x4A, 0x6B)

            # Check if this is the TOC heading
            if is_toc:
                p_toc_heading = para
            else:
                # Add bookmark to this Heading 1 for TOC linking
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
                    "is_appendix": is_appendix,
                    "is_preface": is_preface,
                })

        elif style_name == "Heading 2":
            para.paragraph_format.space_before = Pt(15)
            para.paragraph_format.space_after = Pt(5)
            para.paragraph_format.keep_with_next = True
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(13.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x1A, 0x4A, 0x6B)

        elif style_name == "Heading 3":
            para.paragraph_format.space_before = Pt(13)
            para.paragraph_format.space_after = Pt(4)
            para.paragraph_format.keep_with_next = True
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(11.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x0F, 0x2A, 0x44)

        elif style_name == "Heading 4":
            para.paragraph_format.space_before = Pt(8)
            para.paragraph_format.space_after = Pt(2)
            para.paragraph_format.keep_with_next = True
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.5)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        # --- B. CODE BLOCKS (Solutions & Sample Code) ---
        elif "Code" in style_name or style_name == "Source Code":
            para.paragraph_format.space_before = Pt(0)
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.line_spacing = 1.05
            for r in para.runs:
                r.font.name = "Consolas"
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

            # Elegant uniform code box with subtle border
            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F8FAFC"/>')
            bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                <w:left w:val="single" w:sz="6" w:space="6" w:color="CBD5E1"/>
                <w:top w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                <w:bottom w:val="single" w:sz="4" w:space="2" w:color="E2E8F0"/>
                <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
            </w:pBdr>''')
            ind = parse_xml(f'<w:ind {nsdecls("w")} w:left="100" w:right="100"/>')
            pPr = para._p.get_or_add_pPr()
            pPr.append(shd)
            pPr.append(bdr)
            pPr.append(ind)

        # --- C. CALLOUT / BLOCKQUOTES ---
        elif style_name in ["Block Text", "Quote"] or text.startswith(">") or text.startswith("Định lý:") or text.startswith("Cảnh báo:"):
            is_warning = "⚠️" in text or "Cảnh báo" in text or "Bẫy lỗi" in text
            is_tip = "💡" in text or "Mẹo" in text or "Lưu ý" in text
            is_theorem = "Định lý" in text or "Định nghĩa" in text or "Hệ quả" in text or "Bất biến" in text

            fill_color = "FFFBEB" if is_warning else ("F0FDF4" if is_tip else ("F1F5F9" if is_theorem else "F8FAFC"))
            bdr_color = "F59E0B" if is_warning else ("10B981" if is_tip else ("0F2A44" if is_theorem else "94A3B8"))

            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
            bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                <w:left w:val="single" w:sz="18" w:space="8" w:color="{bdr_color}"/>
                <w:top w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
                <w:bottom w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
                <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
            </w:pBdr>''')
            ind = parse_xml(f'<w:ind {nsdecls("w")} w:left="120" w:right="120"/>')
            pPr = para._p.get_or_add_pPr()
            pPr.append(shd)
            pPr.append(bdr)
            pPr.append(ind)

            para.paragraph_format.space_before = Pt(5)
            para.paragraph_format.space_after = Pt(5)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.5)

        # --- D. NORMAL TEXT ---
        else:
            if para.paragraph_format.space_after is None or para.paragraph_format.space_after.pt < 1:
                para.paragraph_format.space_after = Pt(3.5)
            for r in para.runs:
                if not r.font.name:
                    r.font.name = "Times New Roman"
                if not r.font.size:
                    r.font.size = Pt(11)

    # ============================================================
    # 5. BUILD INTERACTIVE HYPERLINKED TOC AT END
    # ============================================================
    if p_toc_heading:
        print(f"  → Đang tạo Mục lục tương tác (Interactive Clickable TOC) với {len(toc_headings)} liên kết...")
        
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

    # ============================================================
    # 6. TABLES STYLING & BORDERS
    # ============================================================
    print(f"  → Đang định dạng và tạo đường viền (borders) cho {len(doc.tables)} bảng dữ liệu...")

    # Remove any conflicting default table style borders
    for s in doc.styles:
        if s.name == "Table":
            for el in s._element.findall(qn("w:tblStylePr")):
                s._element.remove(el)

    for table in doc.tables:
        table.alignment = WD_TABLE_ALIGNMENT.CENTER

        # Clean existing tblBorders and apply uniform subtle table borders
        tblPr = table._tbl.tblPr
        for b in tblPr.findall(qn("w:tblBorders")):
            tblPr.remove(b)

        tblBorders = parse_xml(f'''<w:tblBorders {nsdecls("w")}>
            <w:top w:val="single" w:sz="6" w:space="0" w:color="0F2A44"/>
            <w:left w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:bottom w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
            <w:right w:val="single" w:sz="4" w:space="0" w:color="CBD5E1"/>
            <w:insideH w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
            <w:insideV w:val="single" w:sz="4" w:space="0" w:color="E2E8F0"/>
        </w:tblBorders>''')
        tblPr.append(tblBorders)

        for r_idx, row in enumerate(table.rows):
            is_header = (r_idx == 0)
            trPr = row._tr.get_or_add_trPr()
            trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

            for c_idx, cell in enumerate(row.cells):
                tcPr = cell._tc.get_or_add_tcPr()
                
                # Clear any conflicting cell-level borders
                for b in tcPr.findall(qn("w:tcBorders")):
                    tcPr.remove(b)

                # Vertically center all cells in the table
                tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

                if is_header:
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="0F2A44"/>'))
                    for p in cell.paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.paragraph_format.space_before = Pt(4)
                        p.paragraph_format.space_after = Pt(4)
                        p.paragraph_format.keep_with_next = True
                        # 1. Normal runs
                        for run in p.runs:
                            run.font.name = "Times New Roman"
                            run.font.bold = True
                            run.font.size = Pt(10)
                            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

                        # 2. All w:r elements in paragraph
                        for r_elem in p._p.findall(".//" + qn("w:r")):
                            rPr = r_elem.get_or_add_rPr()
                            for c in rPr.findall(qn("w:color")):
                                rPr.remove(c)
                            rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="FFFFFF"/>'))

                        # 3. All m:r elements (Office Math runs inside math equations like i, A[0], Sum, Max_Sum)
                        math_ns = "http://schemas.openxmlformats.org/officeDocument/2006/math"
                        for mr in p._p.findall(".//{" + math_ns + "}r"):
                            existing_rPr = mr.find(qn("w:rPr"))
                            if existing_rPr is not None:
                                for c in existing_rPr.findall(qn("w:color")):
                                    existing_rPr.remove(c)
                                existing_rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="FFFFFF"/>'))
                            else:
                                rPr = parse_xml(f'<w:rPr {nsdecls("w")}><w:rFonts {nsdecls("w")} w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:b {nsdecls("w")}/><w:color {nsdecls("w")} w:val="FFFFFF"/><w:sz {nsdecls("w")} w:val="20"/></w:rPr>')
                                mr.insert(0, rPr)
                else:
                    fill_color = "F8FAFC" if r_idx % 2 == 0 else "FFFFFF"
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>'))
                    for p in cell.paragraphs:
                        p.paragraph_format.space_before = Pt(3)
                        p.paragraph_format.space_after = Pt(3)
                        for run in p.runs:
                            run.font.name = "Times New Roman"
                            run.font.size = Pt(10)
                            run.font.color.rgb = RGBColor(0x1E, 0x29, 0x3B)

                tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="80" w:type="dxa"/><w:bottom w:w="80" w:type="dxa"/><w:left w:w="120" w:type="dxa"/><w:right w:w="120" w:type="dxa"/></w:tcMar>')
                tcPr.append(tcMar)

    doc.save(str(OUTPUT_FILE))
    print(f"  ✅ Post-process Design System hoàn tất!")


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 60)
    print(f"📚 Build Word: {BOOK_TITLE}")
    print(f"   Tác giả: {BOOK_AUTHOR}")
    print("=" * 60)

    # Phase 1: Pre-process
    markdown = preprocess_markdown()

    # Phase 2: Pandoc convert
    success = build_with_pandoc(markdown)
    if not success:
        print("\n❌ Build thất bại!")
        sys.exit(1)

    # Phase 3: Post-process
    postprocess_docx()

    # Final stats
    file_size = OUTPUT_FILE.stat().st_size
    print("\n" + "=" * 60)
    print(f"✅ BUILD THÀNH CÔNG!")
    print(f"   📄 Output: {OUTPUT_FILE.name}")
    print(f"   📏 Kích thước: {file_size / 1024 / 1024:.1f} MB")
    print("=" * 60)


if __name__ == "__main__":
    main()
