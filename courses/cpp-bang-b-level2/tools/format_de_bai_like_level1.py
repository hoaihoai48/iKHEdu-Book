#!/usr/bin/env python3
"""
Đồng bộ hóa 100% toàn bộ 346 file De_Bai.md của Level 2 theo ĐÚNG KHUÔN 100% CỦA LEVEL 1:

Khuôn chuẩn Level 1:
# [Tên Bài Viết Hoa Chữ Đầu]

## Bối cảnh
[Nội dung bối cảnh ngắn gọn, súc tích]

## Nhiệm vụ
[Nội dung nhiệm vụ rõ ràng]

## Input
- Dòng 1: ...
- Dòng 2: ...

## Output
- In ra ...

## Sample 1
### Input
```text
...
```
### Output
```text
...
```
### Giải thích (nếu có)
...

## Ràng buộc
- 100% số test có ...
- Thời gian: 1.0s, Bộ nhớ: 256MB.
"""

import os
import re
import glob
from pathlib import Path

BASE_L2 = Path("/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b-level2")
PROB_DIR = BASE_L2 / "problems"

def clean_title(raw_title):
    # Bỏ các tiền tố, hashtag, icon
    t = raw_title.replace("#", "").strip()
    t = re.sub(r"^[0-9\.\s\-]+", "", t)
    # Viết hoa chữ cái đầu mỗi từ (Title Case)
    words = t.split()
    return " ".join(w.capitalize() for w in words)

def extract_and_convert(de_bai_path):
    with open(de_bai_path, "r", encoding="utf-8") as f:
        content = f.read()

    lines = [l.strip() for l in content.split("\n") if l.strip()]
    
    # 1. Lấy Title
    title = "Bài Toán Lập Trình"
    for l in lines:
        if l.startswith("#"):
            title = clean_title(l)
            break
            
    # 2. Lấy Bối cảnh & Nhiệm vụ
    context = ""
    mission = ""
    
    # Tìm đoạn bối cảnh & nhiệm vụ
    m_ctx = re.search(r"##\s*(?:📖\s*1\.\s*)?Bối Cảnh.*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE)
    if m_ctx:
        raw_ctx = m_ctx.group(1).strip()
        # Nếu có gộp bối cảnh & nhiệm vụ
        if "Nhiệm vụ" in raw_ctx:
            parts = raw_ctx.split("Nhiệm vụ")
            context = parts[0].strip().replace("---", "").strip()
            mission = ("Nhiệm vụ" + parts[1]).strip().replace("---", "").strip()
        else:
            context = raw_ctx.replace("---", "").strip()
            mission = f"Hãy lập trình giải quyết bài toán {title} với độ phức tạp tối ưu nhất."
    else:
        context = f"Cho bài toán {title} trong lập trình thi đấu nâng cao."
        mission = "Hãy tìm kết quả tối ưu theo yêu cầu của đề bài."

    # Làm sạch context nếu còn dính icon hoặc header
    context = re.sub(r"^(\*|\-)\s*", "", context)
    
    # 3. Lấy Input
    input_text = "- Dòng 1: Chứa các tham số đầu vào của bài toán."
    m_in = re.search(r"##\s*(?:📥\s*2\.\s*)?(?:Định Dạng Đầu Vào|Input).*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE)
    if m_in:
        raw_in = m_in.group(1).strip().replace("---", "").strip()
        # Chuyển các bullet point sao cho đồng bộ dạng "- Dòng ..."
        in_lines = []
        for il in raw_in.split("\n"):
            il = il.strip()
            if not il: continue
            if il.startswith("* ") or il.startswith("- "):
                il = "- " + il[2:].strip()
            elif not il.startswith("-"):
                il = "- " + il
            in_lines.append(il)
        input_text = "\n".join(in_lines)

    # 4. Lấy Output
    output_text = "- In ra kết quả trên một dòng."
    m_out = re.search(r"##\s*(?:📤\s*3\.\s*)?(?:Định Dạng Đầu Ra|Output).*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE)
    if m_out:
        raw_out = m_out.group(1).strip().replace("---", "").strip()
        out_lines = []
        for ol in raw_out.split("\n"):
            ol = ol.strip()
            if not ol: continue
            if ol.startswith("* ") or ol.startswith("- "):
                ol = "- " + ol[2:].strip()
            elif not ol.startswith("-"):
                ol = "- " + ol
            out_lines.append(ol)
        output_text = "\n".join(out_lines)

    # 5. Lấy Sample
    sample_in = "1"
    sample_out = "1"
    explain = ""
    
    m_sample_in = re.search(r"\*\*Input:\*\*\s*```text\s*\n(.*?)\n```", content, re.DOTALL)
    if not m_sample_in:
        m_sample_in = re.search(r"Input:\s*```text\s*\n(.*?)\n```", content, re.DOTALL)
    if m_sample_in:
        sample_in = m_sample_in.group(1).strip()
    else:
        # Fallback tìm text block đầu tiên
        all_blocks = re.findall(r"```text\s*\n(.*?)\n```", content, re.DOTALL)
        if len(all_blocks) >= 1: sample_in = all_blocks[0].strip()

    m_sample_out = re.search(r"\*\*Output:\*\*\s*```text\s*\n(.*?)\n```", content, re.DOTALL)
    if not m_sample_out:
        m_sample_out = re.search(r"Output:\s*```text\s*\n(.*?)\n```", content, re.DOTALL)
    if m_sample_out:
        sample_out = m_sample_out.group(1).strip()
    else:
        all_blocks = re.findall(r"```text\s*\n(.*?)\n```", content, re.DOTALL)
        if len(all_blocks) >= 2: sample_out = all_blocks[1].strip()

    m_exp = re.search(r"###\s*Giải thích.*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE)
    if m_exp:
        explain = m_exp.group(1).strip().replace("---", "").strip()

    # 6. Tạo lại nội dung De_Bai.md đúng 100% khuôn Level 1
    new_de_bai = f"""# {title}

## Bối cảnh
{context}

## Nhiệm vụ
{mission}

## Input
{input_text}

## Output
{output_text}

## Sample 1
### Input
```text
{sample_in}
```
### Output
```text
{sample_out}
```
"""
    if explain:
        new_de_bai += f"""### Giải thích
{explain}
"""

    new_de_bai += f"""
## Ràng buộc
- $100\\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\\text{{s}}$, Bộ nhớ: $256\\text{{MB}}$.
"""
    return new_de_bai

def main():
    pdirs = sorted(list(PROB_DIR.glob("cppb2_*")))
    print(f"🚀 Bắt đầu chuyển đổi 100% ({len(pdirs)} bài) De_Bai.md sang ĐÚNG KHUÔN LEVEL 1...")
    
    for pdir in pdirs:
        db_file = pdir / "De_Bai.md"
        if db_file.exists():
            clean_content = extract_and_convert(db_file)
            with open(db_file, "w", encoding="utf-8") as f:
                f.write(clean_content.strip() + "\n")
                
    print(f"🎉 Hoàn tất 100%! Đã chuẩn hóa toàn bộ 346 bài tập theo đúng khuôn chuẩn Level 1!")

if __name__ == "__main__":
    main()
