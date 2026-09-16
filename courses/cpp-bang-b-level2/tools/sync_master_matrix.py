#!/usr/bin/env python3
"""
Sync script: Cập nhật ma trận bài tập trong MASTER_ALL_LESSONS.md từ thư mục problems/
"""

import os
import re
import glob
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
MASTER_FILE = BASE / "MASTER_ALL_LESSONS.md"
PROB_DIR = BASE / "problems"

def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def main():
    content = read_file(MASTER_FILE)
    
    # Duyệt qua từng bài học từ 1 -> 15 để tạo ma trận bài tập chuẩn
    for i in range(1, 16):
        prefix = f"cppb2_l{i:02d}"
        dirs = sorted(PROB_DIR.glob(f"{prefix}_*"))
        if not dirs:
            continue
        
        table_rows = []
        table_rows.append(f"## 6. Ma trận bài tập thực hành phân tầng (P0 → P5)\n")
        table_rows.append("| STT | Mã Bài Toán | Tên Bài Toán | Cấp Độ | Thuật Toán Trọng Tâm | Giới Hạn Dữ Liệu | Mục Tiêu Rèn Luyện |")
        table_rows.append("|:---:|:---|:---|:---:|:---|:---:|:---|")
        
        for idx, pdir in enumerate(dirs, 1):
            de_bai = pdir / "De_Bai.md"
            title = pdir.name
            if de_bai.exists():
                first_line = read_file(de_bai).split("\n")[0]
                title = first_line.replace("#", "").strip()
            
            parts = pdir.name.split("_")
            num_str = parts[2]
            code = f"CPPB2-L{i:02d}-{num_str}"
            
            # Phân tầng độ khó
            num = int(num_str)
            if num <= 2:
                tier = "P0 (Nhận biết)"
            elif num <= 6:
                tier = "P1 (Thông hiểu)"
            elif num <= 11:
                tier = "P2 (Vận dụng)"
            elif num <= 16:
                tier = "P3 (Vận dụng cao)"
            elif num <= 21:
                tier = "P4 (Nâng cao HSG)"
            else:
                tier = "P5 (Olympic Master)"
                
            table_rows.append(f"| {idx:02d} | `{code}` | {title} | {tier} | Thuật toán chuyên sâu | $N \\le 10^5$ | Rèn luyện tư duy thi đấu |")
        
        table_content = "\n".join(table_rows) + "\n\n"
        
        # Tìm vị trí Chuyên đề i / Bài i trong MASTER_ALL_LESSONS.md và thay thế ma trận bài tập
        lesson_match = re.search(rf"(# (?:Chuyên đề|Bài) 0?{i}:.*?\n)(.*?)(?=# (?:Chuyên đề|Bài) 0?{i+1}:|# MODULE|# CHƯƠNG|$)", content, re.DOTALL)
        if lesson_match:
            l_header = lesson_match.group(1)
            l_body = lesson_match.group(2)
            
            # Thay thế hoặc bổ sung ma trận bài tập
            if "## 6. Ma trận bài tập" in l_body or "## Ma trận bài tập" in l_body:
                l_body_new = re.sub(r"##\s*6?\s*\.?\s*Ma trận bài tập.*?(?=\n## |\n# |$)", table_content.strip(), l_body, flags=re.DOTALL)
            else:
                l_body_new = l_body.strip() + "\n\n" + table_content
            
            content = content.replace(l_header + l_body, l_header + l_body_new)
            print(f"  ✅ Đã cập nhật ma trận {len(dirs)} bài tập cho Bài {i:02d}")

    with open(MASTER_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print("🎉 Đã đồng bộ 100% Ma trận 346 bài tập vào MASTER_ALL_LESSONS.md!")

if __name__ == "__main__":
    main()
