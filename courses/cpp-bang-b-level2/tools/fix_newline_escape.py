#!/usr/bin/env python3
"""
Sửa lỗi escape ký tự "\n" trong các file solution.cpp và Huong_Dan_Giang_Day.md
"""

import glob
import re
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2/problems")

def fix_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Sửa các chuỗi bị tách dòng lỗi " << "\n";
    fixed = re.sub(r'<< "\s*\n\s*";', r'<< "\\n";', content)
    fixed = fixed.replace('<< "\n";', '<< "\\n";')

    if fixed != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(fixed)
        print(f"  ✅ Đã sửa lỗi xuống dòng trong: {fpath.name}")

def main():
    print("🚀 Bắt đầu quét và sửa lỗi định dạng chuỗi xuống dòng trong toàn bộ problems...")
    for p in BASE.glob("**/*.*"):
        if p.suffix in [".cpp", ".md"]:
            fix_file(p)
    print("🎉 Hoàn tất sửa lỗi định dạng chuỗi!")

if __name__ == "__main__":
    main()
