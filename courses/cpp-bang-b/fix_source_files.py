#!/usr/bin/env python3
"""
fix_source_files.py
Sửa các file nguồn theo đúng yêu cầu:
1. MAJOR 3: Sentence case cho tiêu đề Bài 01-03 và 24 đề cppb_l0_* (giữ tên riêng C++/Python/ASCII/Vector/Safe Input/Modulo/Swap/Palindrome).
2. MAJOR 5: Sửa dòng #### trong Lesson03 thành body text để Heading 4 count = 0.
3. MAJOR 6: Đảm bảo có dòng trống trước mọi list markdown (- / 1. / *) để pandoc không gộp dòng list.
"""

import os
import re
from pathlib import Path

BASE_DIR = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b")
LESSONS_DIR = BASE_DIR / "lessons"
PROBLEMS_DIR = BASE_DIR / "problems"

# 1. FIX LESSON 01-03 TITLES & LESSON 03 HEADING 4 & LIST BLANK LINES
lesson_title_map = {
    1: "Bài 01: Biến, kiểu dữ liệu, toán tử & nhập xuất an toàn",
    2: "Bài 02: Cấu trúc rẽ nhánh & cấu trúc vòng lặp",
    3: "Bài 03: Mảng 1 chiều, vector, xâu ký tự & tổ chức hàm",
}

for l_num in range(1, 4):
    ldir = list(LESSONS_DIR.glob(f"lesson-{l_num:02d}*"))[0]
    md_file = list(ldir.glob("*.md"))[0]
    content = md_file.read_text(encoding="utf-8")
    
    # Fix top H1 title
    lines = content.split("\n")
    if lines and lines[0].startswith("# Bài"):
        lines[0] = f"# {lesson_title_map[l_num]}"
    
    # Fix MAJOR 5: #### in Lesson 03
    fixed_lines = []
    for line in lines:
        if line.startswith("#### Ứng dụng: Mảng đếm tần suất 26 chữ cái"):
            fixed_lines.append("> **Ứng dụng thực tế:** Mảng đếm tần suất 26 chữ cái trong $\\mathcal{O}(|S|)$:")
        else:
            fixed_lines.append(line)
            
    # Fix MAJOR 6: Ensure blank line before list items
    content_fixed = "\n".join(fixed_lines)
    
    # Insert blank line before list items (- / * / 1. ) if preceding line is non-blank and not already list
    fixed_lines_2 = []
    in_code_block = False
    for i, line in enumerate(fixed_lines):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        
        if not in_code_block and (re.match(r"^\s*[\-\*]\s+", line) or re.match(r"^\s*\d+\.\s+", line)):
            if fixed_lines_2:
                prev = fixed_lines_2[-1].strip()
                if prev and not (re.match(r"^\s*[\-\*]\s+", prev) or re.match(r"^\s*\d+\.\s+", prev)) and not prev.startswith("```"):
                    fixed_lines_2.append("")
        fixed_lines_2.append(line)
        
    md_file.write_text("\n".join(fixed_lines_2), encoding="utf-8")
    print(f"✅ Fixed Lesson {l_num:02d} source file: {md_file.name}")

# Also fix list blank lines for lessons 04-15
for l_num in range(4, 16):
    ldir_matches = list(LESSONS_DIR.glob(f"lesson-{l_num:02d}*"))
    if not ldir_matches:
        continue
    ldir = ldir_matches[0]
    md_files = list(ldir.glob("*.md"))
    if not md_files:
        continue
    md_file = md_files[0]
    content = md_file.read_text(encoding="utf-8")
    lines = content.split("\n")
    fixed_lines = []
    in_code_block = False
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
        if not in_code_block and (re.match(r"^\s*[\-\*]\s+", line) or re.match(r"^\s*\d+\.\s+", line)):
            if fixed_lines:
                prev = fixed_lines[-1].strip()
                if prev and not (re.match(r"^\s*[\-\*]\s+", prev) or re.match(r"^\s*\d+\.\s+", prev)) and not prev.startswith("```"):
                    fixed_lines.append("")
        fixed_lines.append(line)
    md_file.write_text("\n".join(fixed_lines), encoding="utf-8")
    print(f"✅ Fixed lists in Lesson {l_num:02d}: {md_file.name}")

# 2. FIX 24 PROBLEM DE_BAI.MD TITLES TO SENTENCE CASE
problem_titles_sentence_case = {
    "cppb_l0_01": "Tính tổng hai số",
    "cppb_l0_02": "Tính chu vi và diện tích hình chữ nhật",
    "cppb_l0_03": "Tính giá trị trung bình cộng ba số",
    "cppb_l0_04": "Tìm chữ số hàng đơn vị",
    "cppb_l0_05": "Chia kẹo công bằng và tính kẹo dư",
    "cppb_l0_06": "Đổi đơn vị độ dài từ mét sang centimet",
    "cppb_l0_07": "Đổi thời gian từ giờ phút sang giây",
    "cppb_l0_08": "Tính tiền mua vở có chương trình khuyến mãi",
    "cppb_l0_09": "Tìm số lớn hơn trong hai số",
    "cppb_l0_10": "Kiểm tra tính chẵn lẻ của số nguyên",
    "cppb_l0_11": "Kiểm tra điều kiện ba cạnh tam giác",
    "cppb_l0_12": "Xếp loại học lực theo điểm số",
    "cppb_l0_13": "Tính tổng các số từ 1 đến N",
    "cppb_l0_14": "Đếm số lượng ước số nguyên dương",
    "cppb_l0_15": "Kiểm tra năm nhuận theo dương lịch",
    "cppb_l0_16": "Đếm số chữ số và tính tổng các chữ số",
    "cppb_l0_17": "Đọc và in mảng số nguyên theo thứ tự ngược",
    "cppb_l0_18": "Đếm số lượng số chẵn trong vector",
    "cppb_l0_19": "Tìm giá trị lớn nhất và vị trí xuất hiện",
    "cppb_l0_20": "Viết hàm kiểm tra mảng tăng dần nghiêm ngặt",
    "cppb_l0_21": "Đếm số lần xuất hiện của ký tự trong xâu",
    "cppb_l0_22": "Lập bảng đếm tần suất các chữ cái thường",
    "cppb_l0_23": "Đảo ngược mảng bằng kỹ thuật swap hai đầu",
    "cppb_l0_24": "Kiểm tra xâu đối xứng (Palindrome)",
}

for code_prefix, s_title in problem_titles_sentence_case.items():
    p_dirs = list(PROBLEMS_DIR.glob(f"{code_prefix}*"))
    if not p_dirs:
        continue
    p_dir = p_dirs[0]
    de_bai_file = p_dir / "De_Bai.md"
    if de_bai_file.exists():
        content = de_bai_file.read_text(encoding="utf-8")
        lines = content.split("\n")
        if lines and lines[0].startswith("# "):
            lines[0] = f"# {s_title}"
        de_bai_file.write_text("\n".join(lines), encoding="utf-8")
        print(f"✅ Fixed problem title {code_prefix}: {s_title}")

print("\n🎉 Hoàn tất sửa nguồn sentence case, heading 4 và list blank lines!")
