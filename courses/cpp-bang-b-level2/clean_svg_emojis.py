#!/usr/bin/env python3
"""
Quét sạch 100% các ký tự emoji và ký hiệu đặc biệt ngoài bảng mã Unicode cơ bản trong toàn bộ các file SVG:
- Thay 📌, 👉, 💡, ⚠️, ⭐, ✨, 🚀, 🔥, ⚙️, 📥, 📤, 📖 bằng các ký hiệu text chuẩn:
  - '📌' -> '(*)'
  - '👉' -> '->'
  - '💡' -> '[Ghi nhớ]'
  - '⚠️' -> '[Lưu ý]'
- Đặt font-family đồng bộ thành "Arial, sans-serif" để tương thích 100% font tiếng Việt không bị lỗi.
"""

import re
from pathlib import Path

BASE = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
SVG_FILES = list(BASE.glob("lessons/**/assets/*.svg"))

REPLACEMENTS = {
    "📌": "(*)",
    "👉": "->",
    "💡": "[Ghi nhớ]",
    "⚠️": "[Lưu ý]",
    "⭐": "*",
    "✨": "*",
    "🚀": "=>",
    "🔥": "[Quan trọng]",
    "⚙️": "[Kỹ thuật]",
    "📥": "[Input]",
    "📤": "[Output]",
    "📖": "[Lý thuyết]"
}

def clean_svg(svg_path):
    with open(svg_path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content

    # 1. Thay thế emoji
    for emoji, rep in REPLACEMENTS.items():
        content = content.replace(emoji, rep)

    # 2. Xóa các emoji Unicode khác nếu còn sót
    emoji_pattern = re.compile(r"[\U00010000-\U0010ffff]", flags=re.UNICODE)
    content = emoji_pattern.sub("", content)

    # 3. Chuẩn hóa font-family sang Arial, sans-serif
    content = re.sub(r"font-family=\"'Times New Roman', serif\"", 'font-family="Arial, sans-serif"', content)
    content = re.sub(r"font-family=\"'Times New Roman'\"", 'font-family="Arial, sans-serif"', content)

    if content != original:
        with open(svg_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  ✅ Đã làm sạch SVG: {svg_path.name}")

def main():
    print(f"🚀 Bắt đầu quét và làm sạch lỗi font/emoji trong {len(SVG_FILES)} file SVG...")
    for svg in SVG_FILES:
        clean_svg(svg)
    print("🎉 Hoàn tất làm sạch toàn bộ 17 file SVG!")

if __name__ == "__main__":
    main()
