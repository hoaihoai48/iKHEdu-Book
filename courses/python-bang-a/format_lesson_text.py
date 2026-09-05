#!/usr/bin/env python3
"""Normalize Vietnamese Markdown headings without changing code or formulas."""

import re
from pathlib import Path

BASE_DIR = Path(__file__).parent
LESSONS_DIR = BASE_DIR / "lessons"

PROPER_TERMS = {
    "python": "Python",
    "ikhedu": "iKHEDU",
    "thta": "THTA",
    "lập trình Python": "Lập trình Python",
    "olympic": "Olympic",
    "doraemon": "Doraemon",
    "mario": "Mario",
    "fibonacci": "Fibonacci",
    "caesar": "Caesar",
    "ascii": "ASCII",
    "bảng a": "Bảng A",
    "phổ thông": "phổ thông",
    "level 1": "Level 1",
    "tập a": "Tập A",
    "tht": "PYA",
    "gcd": "GCD",
}


def sentence_case(text):
    saved = []

    def protect(match):
        saved.append(match.group(0))
        return f"\x01{len(saved) - 1}\x02"

    text = re.sub(r"`[^`]*`|\$[^$]*\$", protect, text)
    text = text.lower()
    text = re.sub(
        r"^(\s*#{0,6}\s*(?:\d+\.\s+)?)([a-zà-ỹ])",
        lambda m: m.group(1) + m.group(2).upper(),
        text,
    )
    text = re.sub(
        r"([.!?:]\s+)([a-zà-ỹ])", lambda m: m.group(1) + m.group(2).upper(), text
    )
    for source, target in PROPER_TERMS.items():
        text = re.sub(rf"\b{re.escape(source)}\b", target, text, flags=re.IGNORECASE)
    for variable in ("a", "b", "c", "k", "n", "r"):
        text = re.sub(rf"(?<!\w){variable}(?!\w)", variable.upper(), text)
    text = re.sub(r"\x01(\d+)\x02", lambda m: saved[int(m.group(1))], text)
    text = re.sub(
        r"\((cơ bản|luyện tập|vận dụng|thử thách)\)",
        lambda m: "(" + m.group(1).capitalize() + ")",
        text,
        flags=re.IGNORECASE,
    )
    return text


def format_file(path):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    formatted = []
    in_code = False
    for line in lines:
        if line.lstrip().startswith("```"):
            in_code = not in_code
            formatted.append(line)
            continue
        if not in_code and line.startswith("| STT |"):
            formatted.append(
                "| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |\n"
            )
            continue
        if not in_code and re.match(r"^#{1,6}\s+", line):
            newline = "\n" if line.endswith("\n") else ""
            formatted.append(sentence_case(line.rstrip("\n")) + newline)
        elif not in_code and re.match(r"^\|\s*\d+\s*\|", line):
            newline = "\n" if line.endswith("\n") else ""
            cells = line.rstrip("\n").split("|")
            formatted_cells = [sentence_case(cell.strip()) for cell in cells]
            formatted.append("| " + " | ".join(formatted_cells[1:-1]) + " |" + newline)
        elif not in_code and re.match(r"^###\s+Bài\s+\d+\s+\([^)]*\):", line):
            prefix, title, suffix = re.match(
                r"^(###\s+Bài\s+\d+\s+\([^)]*\):\s*)(.*?)(\s+\(`PYA-.*)$",
                line.rstrip("\n"),
            ).groups()
            newline = "\n" if line.endswith("\n") else ""
            formatted.append(prefix + sentence_case(title) + suffix + newline)
        else:
            formatted.append(line)
    path.write_text("".join(formatted), encoding="utf-8")


for markdown_file in LESSONS_DIR.glob("lesson-*/*.md"):
    format_file(markdown_file)
