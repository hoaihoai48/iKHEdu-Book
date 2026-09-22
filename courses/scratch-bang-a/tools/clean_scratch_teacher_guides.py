import os
import re
from pathlib import Path

PROBLEMS_DIR = Path("courses/scratch-bang-a/problems")

def clean_file(path):
    text = path.read_text(encoding="utf-8")
    
    # 1. Clean header metadata before "## 1."
    m = re.search(r'(##\s+1\.\s+.*)', text, re.DOTALL)
    if m:
        body = m.group(1)
    else:
        body = text

    # 2. Replace Python keywords and syntax in text
    body = body.replace("map(int, hỏi và đợi.split())", "các khối hỏi và đợi cho từng biến")
    body = body.replace("map(int, câu trả lời.split())", "các khối hỏi và đợi cho từng biến")
    body = body.replace("hỏi và đợi.split()", "câu trả lời")
    body = body.replace("câu trả lời.split()", "câu trả lời")
    body = body.replace("int(hỏi và đợi.strip())", "câu trả lời")
    body = body.replace("hỏi và đợi.strip()", "câu trả lời")
    body = body.replace("int(câu trả lời)", "câu trả lời")
    body = body.replace("câu trả lời.strip()", "câu trả lời")

    # Replace print(...)
    body = re.sub(r'\bprint\((.*?)\)', r'nói (\1)', body)

    # Replace // and % in mathematical descriptions
    body = re.sub(r'(\b\w+)\s*//\s*(\w+\b)', r'làm tròn xuống của (\1 / \2)', body)
    body = re.sub(r'(\b\w+)\s*%\s*(\w+\b)', r'(\1 mod \2)', body)

    # 3. Clean python text blocks
    def fix_code_block(match):
        code = match.group(1)
        code = code.replace("print(", "nói (")
        code = code.replace("int(câu trả lời)", "câu trả lời")
        code = code.replace("int(input())", "câu trả lời")
        code = code.replace("map(int, câu trả lời.split())", "câu trả lời")
        return f"```text\n{code}\n```"

    body = re.sub(r'```(?:text|python)?\n(.*?)```', fix_code_block, body, flags=re.DOTALL)

    new_text = f"# Hướng Dẫn Giảng Dạy\n\n{body.strip()}\n"
    if new_text != text:
        path.write_text(new_text, encoding="utf-8")
        return True
    return False

total_changed = 0
for p in sorted(PROBLEMS_DIR.iterdir()):
    if not p.is_dir(): continue
    hd = p / "Huong_Dan_Giang_Day.md"
    if hd.exists():
        if clean_file(hd):
            total_changed += 1

print(f"CLEANED: {total_changed} problems updated successfully!")
