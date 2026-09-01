#!/usr/bin/env python3
"""
Build script: Tạo file Word (.docx) xuất bản từ MASTER_ALL_LESSONS.md
Khoá học C++ cơ bản — Trung tâm tin học iKH

Hỗ trợ xuất bản theo 2 Quyển độc lập chuẩn in ấn (hoặc Bản trọn bộ):
- QUYỂN 1: Chương 01 -> 04 (Bài 01 -> 12) + Phụ lục A + Bài giải 1–12 (~210 trang / ~105 tờ A4)
- QUYỂN 2: Chương 05 -> 07 (Bài 13 -> 21) + Bài giải 13–21 (~205 trang / ~102 tờ A4)

Đặc điểm thiết kế xuất bản chuẩn SGK:
- Nhúng trọn bộ 39 hình ảnh minh họa độ nét cao (1600px PNG)
- Không có trang trắng đơn độc sau tiêu đề Chương (Chương + Bài 1 nằm cùng trang)
- Bảng biểu: căn giữa 2 chiều, viền mảnh phẳng, tiêu đề & công thức toán chữ trắng tinh khiết
- Bỏ dòng thời gian/bộ nhớ trong đề bài
- Mục lục tương tác (Clickable Hyperlinks) độc lập cho từng quyển
"""

import os
import re
import sys
import glob
import html
import argparse
import subprocess
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================
BOOK_AUTHOR = "Trung tâm tin học iKH"

BASE_DIR = Path(__file__).parent
MASTER_FILE = BASE_DIR / "MASTER_ALL_LESSONS.md"
FOUNDATION_FILE = BASE_DIR / "source" / "level0" / "IKHEDU_Level0_Foundation.md"
PROBLEMS_DIR = BASE_DIR / "problems"

# Topic metadata
ALL_TOPICS = [
    # Volume 1
    ("Chương 01 — Bài 01: Sắp xếp", "cppb_sx", 1),
    ("Chương 01 — Bài 02: Hai con trỏ", "cppb_hct", 1),
    ("Chương 01 — Bài 03: Cửa sổ trượt", "cppb_cst", 1),
    ("Chương 02 — Bài 04: Mảng tiền tố", "cppb_pt", 1),
    ("Chương 02 — Bài 05: Tìm kiếm nhị phân", "cppb_bs", 1),
    ("Chương 02 — Bài 06: Phép toán bit", "cppb_bit", 1),
    ("Chương 03 — Bài 07: Ước, bội & số nguyên tố", "cppb_nt", 1),
    ("Chương 03 — Bài 08: Đồng dư & lũy thừa", "cppb_mod", 1),
    ("Chương 03 — Bài 09: Số nguyên lớn", "cppb_big", 1),
    ("Chương 04 — Bài 10: Đệ quy", "cppb_rec", 1),
    ("Chương 04 — Bài 11: Chia để trị", "cppb_dac", 1),
    ("Chương 04 — Bài 12: Quay lui & nhánh cận", "cppb_bkt", 1),
    # Volume 2
    ("Chương 05 — Bài 13: QHĐ 1D & LIS", "cppb_dp1", 2),
    ("Chương 05 — Bài 14: QHĐ 2D & Knapsack", "cppb_dp2", 2),
    ("Chương 05 — Bài 15: QHĐ chuỗi & LCS", "cppb_dps", 2),
    ("Chương 06 — Bài 16: STL nâng cao", "cppb_stl", 2),
    ("Chương 06 — Bài 17: Stack & Monotonic Stack", "cppb_stk", 2),
    ("Chương 06 — Bài 18: Queue & Deque", "cppb_que", 2),
    ("Chương 07 — Bài 19: Đồ thị BFS & DFS", "cppb_gra", 2),
    ("Chương 07 — Bài 20: Đồ thị lưới 2D", "cppb_grd", 2),
    ("Chương 07 — Bài 21: Segment Tree & Fenwick Tree", "cppb_rng", 2),
]

CODE_TO_DIR_PREFIX = {t[1].upper().replace("_", "-"): t[1] for t in ALL_TOPICS}


# ============================================================
# PHASE 0: Ensure all SVG illustrations are converted to high-res PNG
# ============================================================

def convert_svg_to_png():
    """Convert all SVG files in lessons to 2800px ultra-high-res 300 DPI PNGs for Word embedding."""
    svg_files = list(BASE_DIR.glob("lessons/**/assets/*.svg"))
    converted_count = 0

    for svg in svg_files:
        png = svg.with_suffix(".png")
        if not png.exists() or png.stat().st_mtime < svg.stat().st_mtime:
            cmd = [
                "npx", "-y", "@resvg/resvg-js-cli",
                "--fit-width", "2800",
                "--dpi", "300",
                "--text-rendering", "2",
                "--shape-rendering", "2",
                str(svg),
                str(png)
            ]
            res = subprocess.run(cmd, capture_output=True)
            if res.returncode == 0 and png.exists():
                converted_count += 1

    if converted_count > 0:
        print(f"  → Đã chuyển đổi {converted_count} hình ảnh SVG sang PNG siêu nét 2800px (300 DPI)")


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
    return re.findall(r"(CPPB-[A-Z0-9]+-\d+)", table_text)


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


def format_problem_statement(statement, code, idx=1):
    """Format a problem statement cleanly for textbook publishing."""
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
    """Replace exercise matrix sections with full problem statements."""
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        if re.match(r"^##\s+(?:\d+\.\s+)?Ma trận.*bài tập thực hành", line, re.IGNORECASE):
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
    """Ensure all Markdown lists have a blank line before them."""
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
    """Clean up separator lines."""
    result = []
    for line in lines:
        stripped = line.strip()
        if re.match(r"^={3,}$", stripped) or re.match(r"^-{3,}$", stripped):
            continue
        if re.match(r"^<!--.*-->$", stripped):
            continue
        result.append(line)

    return result


def build_front_matter(volume=1):
    """Build front matter markdown: Lời nói đầu theo Quyển."""
    if volume == 1:
        vol_name = "QUYỂN 1: KỸ THUẬT MẢNG, SỐ HỌC & THUẬT TOÁN VÉT CẠN"
        vol_desc = "gồm **4 Chương trọng tâm (Chương 01 đến Chương 04)** với **12 Bài học** và **180 bài toán thực hành**, trang bị toàn bộ nền tảng cốt lõi từ thuật toán sắp xếp, kỹ thuật hai con trỏ, cửa sổ trượt, mảng tiền tố, tìm kiếm nhị phân, phép toán bit, số học modular, số nguyên lớn cho đến tư duy đệ quy, chia để trị và quay lui vét cạn."
    elif volume == 2:
        vol_name = "QUYỂN 2: QUY HOẠCH ĐỘNG, CẤU TRÚC DỮ LIỆU & THUẬT TOÁN ĐỒ THỊ"
        vol_desc = "gồm **3 Chương chuyên sâu (Chương 05 đến Chương 07)** với **9 Bài học** và **143 bài toán thực hành**, đưa học sinh bước vào thế giới của các kỹ thuật thuật toán đỉnh cao: quy hoạch động 1D/2D/chuỗi, cấu trúc dữ liệu STL nâng cao, ngăn xếp đơn điệu (Monotonic Stack), hàng đợi hai đầu (Deque), lý thuyết đồ thị (BFS, DFS, Flood Fill) và cây truy vấn đoạn (Segment Tree, Fenwick Tree)."
    else:
        vol_name = "TRỌN BỘ 7 CHƯƠNG"
        vol_desc = "bao gồm đầy đủ 7 Chương trọng tâm với 21 Bài học và 323 bài toán thực hành có lời giải chi tiết."

    preface = f"""
# Lời nói đầu

Cuốn sách **Khoá học C++ cơ bản — {vol_name}** được biên soạn bởi **{BOOK_AUTHOR}** nhằm cung cấp cho các em học sinh một lộ trình học tập toàn diện, hệ thống và chuyên sâu về lập trình C++ — từ nền tảng cơ bản đến các thuật toán nâng cao trong lập trình thi đấu.

Sách được thiết kế tối ưu cho học sinh ôn luyện thi **Tin học trẻ Bảng B**, **Học sinh giỏi THCS/THPT** và các kỳ thi lập trình thuật toán. Cuốn sách này {vol_desc}

Mỗi bài học trong sách tuân theo một khung logic sư phạm nhất quán:

- **Khái niệm & bản chất toán học** — giúp học sinh hiểu sâu bản chất thay vì chỉ học vẹt cú pháp.
- **Chứng minh & bất biến thuật toán** — rèn tư duy phân tích toán học nghiêm ngặt.
- **Mẫu cài đặt chuẩn thi đấu** — code C++ sạch, tối ưu, an toàn, sẵn sàng nộp bài.
- **Bẫy lỗi lập trình kinh điển** — cảnh báo những sai lầm và ngộ nhận phổ biến nhất.
- **Bài tập thực hành chi tiết** — mỗi bài toán đều có đề bài chuẩn, ví dụ I/O và ràng buộc toán học rõ ràng.

Toàn bộ code C++ trong sách tuân theo chuẩn thi đấu iKHEDU: sử dụng `#include <bits/stdc++.h>`, Fast I/O và Safe Input, giúp học sinh rèn luyện phong cách lập trình chuyên nghiệp ngay từ đầu.

Chúc các em học tập hiệu quả và chinh phục những giải thưởng cao nhất!

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


def collect_solutions_for_volume(volume=None):
    """Collect solution.cpp files for specific volume or all."""
    if volume == 1:
        target_topics = [t for t in ALL_TOPICS if t[2] == 1]
    elif volume == 2:
        target_topics = [t for t in ALL_TOPICS if t[2] == 2]
    else:
        target_topics = ALL_TOPICS

    result = "\n\\newpage\n\n"
    result += "# Phụ lục B: Bài giải\n\n"
    result += "> Phần này chứa lời giải tham khảo (code C++) cho toàn bộ bài tập trong sách. "
    result += "Hãy tự cố gắng giải bài ít nhất 30 phút trước khi xem bài giải.\n\n"

    total_solutions = 0

    for topic_title, dir_prefix, _ in target_topics:
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

    print(f"  → Đã thu thập {total_solutions} bài giải cho {'Quyển ' + str(volume) if volume else 'Toàn bộ'}")
    return result


def extract_volume_lines(lines, volume=1):
    """Filter lines for Volume 1 (Chương 01 -> 04) or Volume 2 (Chương 05 -> 07)."""
    if volume == 1:
        # From start of content to before CHƯƠNG 05
        vol_lines = []
        for line in lines:
            if line.startswith("# CHƯƠNG 05"):
                break
            vol_lines.append(line)
        return vol_lines
    elif volume == 2:
        # From CHƯƠNG 05 to end
        vol_lines = []
        capture = False
        for line in lines:
            if line.startswith("# CHƯƠNG 05"):
                capture = True
            if capture:
                vol_lines.append(line)
        return vol_lines
    else:
        return lines


def preprocess_markdown_for_volume(volume=1):
    """Main pre-processing pipeline for a specific volume."""
    vol_str = f"QUYỂN {volume}" if volume in [1, 2] else "TRỌN BỘ"
    print(f"\n📖 Đang xử lý nội dung cho {vol_str}...")

    convert_svg_to_png()
    content = read_file(MASTER_FILE)

    content = re.sub(r"# MODULE (\d+)", r"# CHƯƠNG \1", content)
    content = re.sub(r"MODULE (\d+)", r"CHƯƠNG \1", content)
    content = re.sub(r"# Chuyên đề (\d+)", r"# Bài \1", content)
    content = re.sub(r"Chuyên đề (\d+)", r"Bài \1", content)

    # Normalize C++ preprocessor directives (remove spaces like '# include' -> '#include')
    content = re.sub(r"#\s+include\b", "#include", content)
    content = re.sub(r"#\s+define\b", "#define", content)
    content = re.sub(r"#\s+pragma\b", "#pragma", content)
    content = re.sub(r"#\s+ifndef\b", "#ifndef", content)
    content = re.sub(r"#\s+endif\b", "#endif", content)
    content = re.sub(r"#\s+ifdef\b", "#ifdef", content)

    content = resolve_and_embed_images(content)

    lines = content.split("\n")
    lines = remove_overview_toc(lines)
    lines = remove_top_header_and_metadata(lines)
    lines = remove_quiz_sections(lines)
    lines = replace_exercise_matrices_with_problems(lines)
    lines = clean_separators(lines)
    lines = ensure_markdown_list_blank_lines(lines)

    # Filter by volume
    lines = extract_volume_lines(lines, volume)
    print(f"  → Nội dung {vol_str}: {len(lines)} dòng")

    # Front matter
    front = build_front_matter(volume)

    # Back matter
    foundation = build_back_matter_foundation() if volume in [1, None] else ""
    solutions = collect_solutions_for_volume(volume)
    toc_section = "\n\\newpage\n\n# Mục lục\n\n"

    body = "\n".join(lines)

    if volume == 1:
        book_title = "Khoá học C++ cơ bản — Quyển 1"
        book_subtitle = "Kỹ thuật mảng, Số học & Thuật toán vét cạn"
    elif volume == 2:
        book_title = "Khoá học C++ cơ bản — Quyển 2"
        book_subtitle = "Quy hoạch động, Cấu trúc dữ liệu & Thuật toán đồ thị"
    else:
        book_title = "Khoá học C++ cơ bản"
        book_subtitle = "Từ nền tảng lập trình đến thuật toán thi đấu"

    final_md = f"""---
title: "{book_title}"
subtitle: "{book_subtitle}"
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
  - \\fancyhead[L]{{\\textit{{{book_title}}}}}
  - \\fancyhead[R]{{\\textit{{{BOOK_AUTHOR}}}}}
---

{front}

{body}

{foundation}

{solutions}

{toc_section}
"""

    return final_md, book_title, book_subtitle


# ============================================================
# PHASE 2: Build docx via pandoc
# ============================================================

def build_with_pandoc(markdown_content, output_file):
    """Convert markdown to docx using pandoc."""
    print(f"\n🔧 Đang chạy Pandoc chuyển đổi → {output_file.name}...")

    temp_md = BASE_DIR / f"_build_intermediate_{output_file.stem}.md"
    with open(temp_md, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"  → Đã ghi file trung gian: {temp_md.name} ({temp_md.stat().st_size:,} bytes)")

    cmd = [
        "pandoc",
        str(temp_md),
        "-o", str(output_file),
        "--from=markdown+tex_math_dollars+pipe_tables+fenced_code_blocks+yaml_metadata_block+header_attributes",
        "--to=docx",
        "--standalone",
        "--wrap=auto",
        "--columns=80",
    ]

    ref_doc = BASE_DIR / "_reference.docx"
    if ref_doc.exists():
        cmd.extend(["--reference-doc", str(ref_doc)])

    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"  ❌ Pandoc lỗi: {result.stderr}")
        return False

    print(f"  ✅ Pandoc thành công!")
    return True


# ============================================================
# PHASE 3: Post-process with python-docx
# ============================================================

def postprocess_docx(output_file, book_title, book_subtitle, volume=1):
    """Post-process the generated docx for professional publishing aesthetics."""
    print(f"\n🎨 Đang áp dụng Design System xuất bản chuyên nghiệp cho {output_file.name}...")

    from docx import Document
    from docx.shared import Pt, Inches, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.enum.table import WD_TABLE_ALIGNMENT
    from docx.oxml import parse_xml, OxmlElement
    from docx.oxml.ns import nsdecls, qn

    doc = Document(str(output_file))

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
        p_head.text = f"{book_title}  •  {BOOK_AUTHOR}"
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

        vol_badge = f"GIÁO TRÌNH LẬP TRÌNH THI ĐẤU  •  C++ BẢNG B"
        main_title = f"KHOÁ HỌC C++ CƠ BẢN"
        vol_sub_title = f"QUYỂN {volume}: {book_subtitle.upper()}" if volume in [1, 2] else "TỪ NỀN TẢNG LẬP TRÌNH ĐẾN THUẬT TOÁN THI ĐẤU"

        if volume == 1:
            tagline = "Giáo trình 4 Chương trọng tâm & 180 Bài toán thực hành có lời giải chi tiết"
        elif volume == 2:
            tagline = "Giáo trình 3 Chương trọng tâm & 143 Bài toán thực hành có lời giải chi tiết"
        else:
            tagline = "Giáo trình 7 Chương trọng tâm & 323 Bài toán thực hành có lời giải chi tiết"

        p0.text = vol_badge
        p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p0.paragraph_format.space_before = Pt(40)
        p0.paragraph_format.space_after = Pt(90)
        if p0.runs:
            p0.runs[0].font.name = "Times New Roman"
            p0.runs[0].font.size = Pt(10.5)
            p0.runs[0].font.bold = True
            p0.runs[0].font.color.rgb = RGBColor(0x1A, 0x4A, 0x6B)

        p1.text = main_title
        p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p1.paragraph_format.space_before = Pt(0)
        p1.paragraph_format.space_after = Pt(10)
        if p1.runs:
            p1.runs[0].font.name = "Times New Roman"
            p1.runs[0].font.size = Pt(28)
            p1.runs[0].font.bold = True
            p1.runs[0].font.color.rgb = RGBColor(0x0F, 0x2A, 0x44)

        p2.text = vol_sub_title
        p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p2.paragraph_format.space_before = Pt(0)
        p2.paragraph_format.space_after = Pt(14)
        if p2.runs:
            p2.runs[0].font.name = "Times New Roman"
            p2.runs[0].font.size = Pt(13)
            p2.runs[0].font.bold = True
            p2.runs[0].font.color.rgb = RGBColor(0x2E, 0x5E, 0x8A)

        p_div = parse_xml(f'<w:p {nsdecls("w")}><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="200"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="16"/><w:color w:val="94A3B8"/></w:rPr><w:t>──────────────────────────────────────────</w:t></w:r></w:p>')
        p2._p.addnext(p_div)

        p_tag = parse_xml(f'<w:p {nsdecls("w")}><w:pPr><w:jc w:val="center"/><w:spacing w:before="0" w:after="4200"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/><w:sz w:val="21"/><w:color w:val="475569"/></w:rPr><w:t>{html.escape(tagline)}</w:t></w:r></w:p>')
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

            prev_text = doc.paragraphs[idx - 1].text.strip() if idx > 0 else ""
            is_first_lesson_in_chapter = is_lesson and prev_text.startswith("CHƯƠNG")

            para.paragraph_format.space_before = Pt(28) if is_chapter else (Pt(12) if is_first_lesson_in_chapter else Pt(20))
            para.paragraph_format.space_after = Pt(8)
            para.paragraph_format.keep_with_next = True
            
            if not is_first_lesson_in_chapter:
                para._p.get_or_add_pPr().append(parse_xml(f'<w:pageBreakBefore {nsdecls("w")}/>'))

            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(17.5) if is_chapter else Pt(15)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0x0F, 0x2A, 0x44) if is_chapter else RGBColor(0x1A, 0x4A, 0x6B)

            if is_toc:
                p_toc_heading = para
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

        # --- B. CODE BLOCKS ---
        elif "Code" in style_name or style_name == "Source Code":
            para.paragraph_format.space_before = Pt(0)
            para.paragraph_format.space_after = Pt(0)
            para.paragraph_format.line_spacing = 1.05
            for r in para.runs:
                r.font.name = "Consolas"
                r.font.size = Pt(8.5)
                r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

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

        # --- C. CALLOUT / BLOCKQUOTES ---
        elif style_name in ["Block Text", "Quote"] or text.startswith(">") or text.startswith("Định lý:") or text.startswith("Cảnh báo:"):
            is_warning = "⚠️" in text or "Cảnh báo" in text or "Bẫy lỗi" in text
            is_tip = "💡" in text or "Mẹo" in text or "Lưu ý" in text
            is_theorem = "Định lý" in text or "Định nghĩa" in text or "Hệ quả" in text or "Bất biến" in text

            fill_color = "FFFBEB" if is_warning else ("F0FDF4" if is_tip else ("F1F5F9" if is_theorem else "F8FAFC"))
            bdr_color = "F59E0B" if is_warning else ("10B981" if is_tip else ("0F2A44" if is_theorem else "94A3B8"))

            shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_color}"/>')
            bdr = parse_xml(f'''<w:pBdr {nsdecls("w")}>
                <w:left w:val="single" w:sz="16" w:space="4" w:color="{bdr_color}"/>
                <w:top w:val="single" w:sz="4" w:space="3" w:color="E2E8F0"/>
                <w:bottom w:val="single" w:sz="4" w:space="3" w:color="E2E8F0"/>
                <w:right w:val="single" w:sz="4" w:space="4" w:color="E2E8F0"/>
            </w:pBdr>''')
            ind = parse_xml(f'<w:ind {nsdecls("w")} w:left="200" w:right="120"/>')
            pPr = para._p.get_or_add_pPr()
            pPr.append(shd)
            pPr.append(bdr)
            pPr.append(ind)

            para.paragraph_format.space_before = Pt(5)
            para.paragraph_format.space_after = Pt(5)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10.5)

        # --- D. IMAGES & DRAWINGS ---
        elif len(para._p.findall('.//' + qn('w:drawing'))) > 0:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_before = Pt(8)
            para.paragraph_format.space_after = Pt(2)
            
            for drawing in para._p.findall('.//' + qn('w:drawing')):
                wp_extent = drawing.find('.//' + qn('wp:extent'))
                a_ext = drawing.find('.//' + qn('a:ext'))
                if wp_extent is not None:
                    try:
                        old_cx = int(wp_extent.get('cx', 0))
                        old_cy = int(wp_extent.get('cy', 0))
                        if old_cx > 0 and old_cy > 0:
                            target_cx = 6000000  # 6.56 inches (full printable width on A4)
                            target_cy = int(round(old_cy * target_cx / old_cx))
                            # Cap max height to avoid page overflow
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

        # --- E. IMAGE CAPTIONS ---
        elif style_name in ["Image Caption", "Caption"]:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            para.paragraph_format.space_before = Pt(3)
            para.paragraph_format.space_after = Pt(10)
            for r in para.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(10)
                r.font.italic = True
                r.font.color.rgb = RGBColor(0x33, 0x41, 0x55)

        # --- F. NORMAL TEXT ---
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

    # ============================================================
    # 6. TABLES STYLING & BORDERS
    # ============================================================
    print(f"  → Đang định dạng và làm sạch viền cho {len(doc.tables)} bảng dữ liệu...")

    for s in doc.styles:
        if s.name == "Table":
            for el in s._element.findall(qn("w:tblStylePr")):
                s._element.remove(el)

    for table in doc.tables:
        table.alignment = WD_TABLE_ALIGNMENT.CENTER

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
                for b in tcPr.findall(qn("w:tcBorders")):
                    tcPr.remove(b)

                tcPr.append(parse_xml(f'<w:vAlign {nsdecls("w")} w:val="center"/>'))

                if is_header:
                    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="0F2A44"/>'))
                    for p in cell.paragraphs:
                        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                        p.paragraph_format.space_before = Pt(4)
                        p.paragraph_format.space_after = Pt(4)
                        p.paragraph_format.keep_with_next = True
                        for run in p.runs:
                            run.font.name = "Times New Roman"
                            run.font.bold = True
                            run.font.size = Pt(10)
                            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

                        for r_elem in p._p.findall(".//" + qn("w:r")):
                            rPr = r_elem.get_or_add_rPr()
                            for c in rPr.findall(qn("w:color")):
                                rPr.remove(c)
                            rPr.append(parse_xml(f'<w:color {nsdecls("w")} w:val="FFFFFF"/>'))

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

    doc.save(str(output_file))
    print(f"  ✅ Post-process Design System hoàn tất cho {output_file.name}!")


# ============================================================
# MAIN
# ============================================================

def build_single_volume(volume):
    """Build a specific volume or all."""
    if volume == 1:
        output_file = BASE_DIR / "IKHEDU_CPP_Co_Ban_Quyen_1.docx"
    elif volume == 2:
        output_file = BASE_DIR / "IKHEDU_CPP_Co_Ban_Quyen_2.docx"
    else:
        output_file = BASE_DIR / "IKHEDU_CPP_Co_Ban_Xuat_Ban.docx"

    print("\n" + "=" * 60)
    print(f"📚 BẮT ĐẦU BUILD: {'QUYỂN ' + str(volume) if volume else 'BẢN TOÀN TẬP'}")
    print(f"   Đích xuất: {output_file.name}")
    print("=" * 60)

    markdown, book_title, book_subtitle = preprocess_markdown_for_volume(volume)
    success = build_with_pandoc(markdown, output_file)
    if not success:
        print(f"\n❌ Build thất bại cho {output_file.name}!")
        return False

    postprocess_docx(output_file, book_title, book_subtitle, volume)

    file_size = output_file.stat().st_size
    print(f"✅ HOÀN TẤT: {output_file.name} ({file_size / 1024 / 1024:.1f} MB)")
    return True


def main():
    parser = argparse.ArgumentParser(description="Build Word Docx for C++ Curriculum")
    parser.add_argument("--volume", type=int, choices=[1, 2], help="Build only Volume 1 or Volume 2")
    parser.add_argument("--all", action="store_true", help="Build both Volume 1 and Volume 2")
    args = parser.parse_args()

    if args.volume:
        build_single_volume(args.volume)
    else:
        # Default: Build both Quyển 1 and Quyển 2
        print("=" * 60)
        print("📚 BẮT ĐẦU XUẤT BẢN BỘ SÁCH 2 QUYỂN")
        print(f"   Tác giả: {BOOK_AUTHOR}")
        print("=" * 60)

        success1 = build_single_volume(1)
        success2 = build_single_volume(2)

        if success1 and success2:
            print("\n" + "=" * 60)
            print("🎉 TẤT CẢ CÁC QUYỂN ĐÃ ĐƯỢC XUẤT BẢN THÀNH CÔNG!")
            print("   📘 Quyển 1: IKHEDU_CPP_Co_Ban_Quyen_1.docx")
            print("   📕 Quyển 2: IKHEDU_CPP_Co_Ban_Quyen_2.docx")
            print("=" * 60)


if __name__ == "__main__":
    main()
