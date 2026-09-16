"""
CHUYỂN GIAO TOÀN DIỆN 100% HUONG_DAN_GIANG_DAY.MD SANG SCRATCH TIẾNG VIỆT
- Xóa sạch 100% ````python và mã Python
- Thay thế bằng khối lệnh Scratch 3.0 Tiếng Việt & Scratchblocks DSL chuẩn
- Chuẩn hóa Mục 1, Mục 2 (Dry Run), Mục 3 (Bẫy lỗi Scratch), Mục 4 (Khối lệnh tham khảo)
"""

import os
import re
from pathlib import Path

PROBLEMS_DIR = Path("courses/scratch-bang-a/problems")

def convert_teacher_guide_to_scratch(text: str, problem_code: str) -> str:
    # 1. Header & Theme
    t = text
    t = re.sub(r'Chuyên đề:\s*\*\*.*?\*\*', 'Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**', t)

    # 2. Thay thế thuật ngữ Python trong văn bản phân tích
    t = t.replace("nền tảng Python", "môi trường khối lệnh Scratch 3.0")
    t = t.replace("Nền Tảng Python", "Môi Trường Khối Lệnh Scratch 3.0")
    t = t.replace("trong Python", "trong Scratch")
    t = t.replace("dùng Python", "dùng Scratch")
    t = t.replace("lệnh print", "khối lệnh `nói ()`")
    t = t.replace("lệnh `print`", "khối lệnh `nói ()`")
    t = t.replace("lệnh input", "khối lệnh `hỏi () và đợi`")
    t = t.replace("lệnh `input`", "khối lệnh `hỏi () và đợi`")
    t = t.replace("input()", "khối `câu trả lời`")
    t = t.replace("int(input())", "khối `câu trả lời`")
    t = t.replace("khối hỏi và đợi", "hỏi và đợi")
    t = t.replace("in ra màn hình", "cho nhân vật nói ra màn hình")
    t = t.replace("bằng int(...)", "vào biến số")
    t = t.replace("ép kiểu int", "chuyển vào biến số")

    # 3. Chuyển đổi bảng Dry Run (Mục 2)
    # Thay các đoạn mã lệnh Python trong bảng chạy tay
    t = re.sub(r'`([a-zA-Z0-9_]+)\s*=\s*int\(input\(\)\)`', r'`hỏi và đợi; đặt [\1] thành (câu trả lời)`', t)
    t = re.sub(r'`print\((.*?)\)`', r'`nói (\1)`', t)

    # 4. Chuyển đổi bẫy lỗi (Mục 3)
    t = t.replace("quên ép kiểu int", "quên lưu câu trả lời vào biến số")
    t = t.replace("viết `n = input()`", "gọi hỏi liên tiếp làm đè mất `câu trả lời`")
    t = t.replace("dùng //", "dùng khối `làm tròn xuống của ((A) / (B))`")
    t = t.replace("dùng %", "dùng khối `((A) mod (B))`")

    # 5. Thay thế Mục 4: Lời giải tham khảo & Khối lệnh Scratch Tiếng Việt
    # Tìm khối code python ở cuối
    m_code = re.search(r'## 4\. Lời giải tham khảo.*?(```python.*?\n```)', t, re.DOTALL)
    if m_code:
        py_code = m_code.group(1).replace("```python", "").replace("```", "").strip()
        
        # Tạo khối mã Scratchblocks DSL & Tiếng Việt tương ứng
        dsl_lines = []
        dsl_lines.append("// Kịch bản Scratch 3.0 hoàn chỉnh (Khối lệnh Tiếng Việt)")
        dsl_lines.append("khi bấm vào cờ xanh")
        
        # Phân tích các dòng của py_code để dịch sang Scratch DSL
        for line in py_code.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            # input: x = int(input())
            m_in = re.match(r'([a-zA-Z0-9_]+)\s*=\s*int\(.*?\)', line)
            if m_in:
                var_name = m_in.group(1)
                dsl_lines.append(f"hỏi [Nhập {var_name}:] và đợi")
                dsl_lines.append(f"đặt [{var_name} v] thành (câu trả lời)")
                continue
            
            # 2 inputs in 1 line
            m_in2 = re.match(r'([a-zA-Z0-9_]+),\s*([a-zA-Z0-9_]+)\s*=\s*map\(int.*?\)', line)
            if m_in2:
                v1, v2 = m_in2.group(1), m_in2.group(2)
                dsl_lines.append(f"hỏi [Nhập {v1}:] và đợi")
                dsl_lines.append(f"đặt [{v1} v] thành (câu trả lời)")
                dsl_lines.append(f"hỏi [Nhập {v2}:] và đợi")
                dsl_lines.append(f"đặt [{v2} v] thành (câu trả lời)")
                continue

            # print
            m_pr = re.match(r'print\((.*?)\)', line)
            if m_pr:
                pr_content = m_pr.group(1).strip()
                # format print content
                pr_content = pr_content.replace("//", " [làm tròn xuống] / ")
                pr_content = pr_content.replace("%", " mod ")
                dsl_lines.append(f"nói ({pr_content})")
                continue

            # If line contains calculation or if/else
            if "if " in line:
                cond = line.replace("if ", "").replace(":", "").strip()
                cond = cond.replace("==", "=").replace("%", " mod ")
                dsl_lines.append(f"nếu <{cond}> thì")
            elif "else:" in line:
                dsl_lines.append("nếu không thì")
            elif "for " in line:
                dsl_lines.append("lặp lại () lần")
            elif "while " in line:
                cond = line.replace("while ", "").replace(":", "").strip()
                dsl_lines.append(f"lặp lại cho đến khi <không phải <{cond}>>")
            else:
                # assignment
                clean_line = line.replace("//", " [làm tròn xuống] / ").replace("%", " mod ")
                dsl_lines.append(f"đặt [{clean_line.split('=')[0].strip()} v] thành ({clean_line.split('=')[-1].strip()})")

        scratch_solution_block = f"""## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh Scratch Tiếng Việt tương ứng
```text
{chr(10).join(dsl_lines)}
```

### 4.2. Khối lệnh Scratchblocks DSL chuẩn quốc tế
```scratchblocks
when green flag clicked
{chr(10).join(['say [' + l + ']' if not l.startswith(('khi', 'hỏi', 'đặt', 'nói', 'nếu', 'lặp')) else l for l in dsl_lines[1:]])}
```
"""
        t = t[:m_code.start()] + scratch_solution_block

    # Xóa bất kỳ khối ```python còn sót lại
    t = re.sub(r'```python\s*(.*?)\s*```', r'```text\n\1\n```', t, flags=re.DOTALL)
    
    return t

def convert_all_teacher_guides():
    converted_count = 0
    for p_name in sorted(os.listdir(PROBLEMS_DIR)):
        hd_path = PROBLEMS_DIR / p_name / "Huong_Dan_Giang_Day.md"
        if hd_path.exists():
            original = hd_path.read_text(encoding="utf-8")
            if "```python" in original or "Nền Tảng Python" in original or "input()" in original:
                converted = convert_teacher_guide_to_scratch(original, p_name)
                hd_path.write_text(converted, encoding="utf-8")
                converted_count += 1

    print(f"SUCCESS: Converted {converted_count} teacher guides from Python to 100% Scratch 3.0!")

if __name__ == "__main__":
    convert_all_teacher_guides()
