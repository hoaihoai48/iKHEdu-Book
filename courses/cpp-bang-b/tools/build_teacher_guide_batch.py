#!/usr/bin/env python3
"""
Tái cấu trúc 323 Huong_Dan_Giang_Day.md trong courses/cpp-bang-b/problems
sang đúng chuẩn 4 mục thực chiến sư phạm iKHEDU:
  ## 1. Ý tưởng & Phân tích thuật toán
  ## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: ...)
  ## 3. Lưu ý & Bẫy lỗi thường gặp
  ## 4. Lời giải tham khảo
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).parent
PROBLEMS_DIR = BASE_DIR / "problems"

def parse_de_bai(de_bai_path):
    if not de_bai_path.exists():
        return {}
    text = de_bai_path.read_text(encoding="utf-8")
    
    title_m = re.search(r'^#\s+(.+)', text)
    title = title_m.group(1).strip() if title_m else ""
    
    bc_m = re.search(r'## Bối cảnh\s*\n(.*?)(?=\n## Nhiệm vụ|\n## Input|\Z)', text, re.DOTALL)
    nv_m = re.search(r'## Nhiệm vụ\s*\n(.*?)(?=\n## Input|\n## Output|\Z)', text, re.DOTALL)
    inp_m = re.search(r'## Input\s*\n(.*?)(?=\n## Output|\n## Sample|\Z)', text, re.DOTALL)
    out_m = re.search(r'## Output\s*\n(.*?)(?=\n## Sample|\n## Ràng buộc|\Z)', text, re.DOTALL)
    
    s_inp_m = re.search(r'### Input\s*```(?:text)?\n(.*?)```', text, re.DOTALL)
    s_out_m = re.search(r'### Output\s*```(?:text)?\n(.*?)```', text, re.DOTALL)
    s_exp_m = re.search(r'### Giải thích\s*\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
    
    return {
        "title": title,
        "bcanh": bc_m.group(1).strip() if bc_m else "",
        "nv": nv_m.group(1).strip() if nv_m else "",
        "inp": inp_m.group(1).strip() if inp_m else "",
        "out": out_m.group(1).strip() if out_m else "",
        "s_inp": s_inp_m.group(1).strip() if s_inp_m else "",
        "s_out": s_out_m.group(1).strip() if s_out_m else "",
        "s_exp": s_exp_m.group(1).strip() if s_exp_m else "",
    }

def get_solution_code(sol_path):
    if not sol_path.exists():
        return ""
    return sol_path.read_text(encoding="utf-8").strip()

def extract_old_sections(guide_path):
    if not guide_path.exists():
        return {}
    text = guide_path.read_text(encoding="utf-8")
    
    topic_m = re.search(r'Chuyên đề:\s*\*\*(.*?)\*\*', text)
    topic = topic_m.group(1).strip() if topic_m else ""
    
    sections = {}
    parts = re.split(r'\n(?=##\s+\d+\.)', text)
    for p in parts:
        m = re.match(r'##\s+(\d+)\.\s+([^\n]+)\n(.*)', p.strip(), re.DOTALL)
        if m:
            num = int(m.group(1))
            heading = m.group(2).strip()
            body = m.group(3).strip()
            sections[num] = {"heading": heading, "body": body}
            
    return {"topic": topic, "sections": sections}

def build_dry_run_table(s_inp, s_out, s_exp):
    inp_lines = [l.strip() for l in s_inp.split('\n') if l.strip()]
    out_lines = [l.strip() for l in s_out.split('\n') if l.strip()]
    exp_clean = s_exp.replace('\n', ' ').strip()
    
    inp_summary = " ".join(inp_lines)
    if len(inp_summary) > 40:
        inp_summary = inp_summary[:37] + "..."
        
    out_summary = " ".join(out_lines)
    if len(out_summary) > 40:
        out_summary = out_summary[:37] + "..."
        
    table = []
    table.append(f"| Bước | Thao tác thực hiện | Dữ liệu biến đổi | Kết quả ghi nhận |")
    table.append(f"|---|---|---|---|")
    table.append(f"| 1 | Khởi tạo & Đọc dữ liệu vào | Input: `{inp_summary}` | Nạp dữ liệu vào các biến/mảng |")
    
    if exp_clean:
        table.append(f"| 2 | Thực thi thuật toán theo từng bước | Phân tích biến: {exp_clean} | Cập nhật trạng thái tối ưu |")
    else:
        table.append(f"| 2 | Thực thi thuật toán theo từng bước | Duyệt và tính toán trên tập dữ liệu mẫu | Cập nhật trạng thái tối ưu |")
        
    table.append(f"| 3 | Xuất kết quả chuẩn ra màn hình | Kết quả cuối cùng: `{out_summary}` | Khớp chính xác với đầu ra mẫu |")
    
    return "\n".join(table)

def generate_new_guide(prob_dir):
    de_bai_file = prob_dir / "De_Bai.md"
    sol_file = prob_dir / "solution.cpp"
    guide_file = prob_dir / "Huong_Dan_Giang_Day.md"
    
    db = parse_de_bai(de_bai_file)
    old = extract_old_sections(guide_file)
    sol_code = get_solution_code(sol_file)
    
    title = db.get("title") or prob_dir.name
    topic = old.get("topic") or "Nền Tảng C++ & Thuật Toán"
    
    # 1. Ý tưởng & Phân tích thuật toán
    sec4_body = old.get("sections", {}).get(4, {}).get("body", "")
    sec2_body = old.get("sections", {}).get(2, {}).get("body", "")
    
    ideas = []
    if db.get("nv"):
        ideas.append(f"- **Bản chất bài toán:** {db['nv']}")
    elif db.get("bcanh"):
        ideas.append(f"- **Bản chất bài toán:** {db['bcanh']}")
        
    if sec4_body:
        sec4_clean = re.sub(r'###\s+\d+\.\d+\.\s*', '', sec4_body)
        sec4_clean = re.sub(r'Chiến lược thực thi:\s*', '', sec4_clean)
        sec4_clean = re.sub(r'Bất biến toán học \(Invariant\):\s*', '**Bất biến:** ', sec4_clean)
        sec4_clean = re.sub(r'\n---\s*$', '', sec4_clean).strip()
        ideas.append(f"- **Chiến lược tiếp cận & tối ưu:**\n{sec4_clean}")
    elif sec2_body:
        sec2_clean = re.sub(r'\n---\s*$', '', sec2_body).strip()
        ideas.append(f"- **Phân tích yêu cầu:**\n{sec2_clean}")
        
    idea_text = "\n\n".join(ideas)
    
    # 2. Bảng chạy tay trên số liệu mẫu
    s_inp = db.get("s_inp", "")
    s_out = db.get("s_out", "")
    s_exp = db.get("s_exp", "")
    s_inp_disp = " ".join([l.strip() for l in s_inp.split('\n') if l.strip()])
    if len(s_inp_disp) > 30: s_inp_disp = s_inp_disp[:27] + "..."
    
    dry_run_header = f"## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: {s_inp_disp})"
    dry_run_table = build_dry_run_table(s_inp, s_out, s_exp)
    if s_exp:
        dry_run_content = f"{dry_run_table}\n\n*Giải thích chi tiết từ mẫu:* {s_exp}"
    else:
        dry_run_content = f"{dry_run_table}"
        
    # 3. Lưu ý & Bẫy lỗi thường gặp
    sec7_body = old.get("sections", {}).get(7, {}).get("body", "")
    if sec7_body:
        traps = re.sub(r'\n---\s*$', '', sec7_body).strip()
    else:
        traps = (
            "1. Chú ý tràn số nguyên: Khi tính toán tích, tổng hoặc lũy thừa vượt quá $2 \\cdot 10^9$, "
            "bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit).\n"
            "2. Đọc an toàn (Safe Input): Luôn kiểm tra điều kiện đọc dữ liệu đầu vào để tránh crash khi gặp input rỗng.\n"
            "3. Giới hạn thời gian & định dạng in ấn: Xuất dữ liệu cách nhau bằng dấu cách hoặc xuống dòng theo đúng quy chuẩn đề bài."
        )
        
    # 4. Lời giải tham khảo
    code_block = f"```cpp\n{sol_code}\n```"
    
    # GHÉP TOÀN BỘ THEO CHUẨN 4 MỤC
    doc = [
        f"# Hướng Dẫn Giảng Dạy: {title}",
        f"Chuyên đề: **{topic}**",
        "",
        "---",
        "",
        "## 1. Ý tưởng & Phân tích thuật toán",
        f"{idea_text}",
        "",
        "---",
        "",
        f"{dry_run_header}",
        f"{dry_run_content}",
        "",
        "---",
        "",
        "## 3. Lưu ý & Bẫy lỗi thường gặp",
        f"{traps}",
        "",
        "---",
        "",
        "## 4. Lời giải tham khảo",
        f"{code_block}",
        ""
    ]
    
    return "\n".join(doc)

def main():
    all_prob_dirs = sorted([d for d in PROBLEMS_DIR.iterdir() if d.is_dir()])
    print(f"Bắt đầu chuyển đổi {len(all_prob_dirs)} file Huong_Dan_Giang_Day.md sang chuẩn 4 mục...")
    
    success_count = 0
    for prob_dir in all_prob_dirs:
        guide_file = prob_dir / "Huong_Dan_Giang_Day.md"
        if not guide_file.exists():
            continue
        new_content = generate_new_guide(prob_dir)
        guide_file.write_text(new_content, encoding="utf-8")
        success_count += 1
        
    print(f"🎉 Hoàn thành chuyển đổi thành công {success_count}/{len(all_prob_dirs)} files!")

if __name__ == "__main__":
    main()
