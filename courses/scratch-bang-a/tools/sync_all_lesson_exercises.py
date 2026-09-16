"""
TỰ ĐỘNG ĐỒNG BỘ 100% BÀI TẬP VÀO BAI_TAP.MD CỦA TỪNG BÀI HỌC
Đọc trực tiếp từ kho courses/scratch-bang-a/problems/
Phân bổ đầy đủ 100% số bài toán vào ma trận phân tầng P0, P1, P2, P3
kèm đề bài, bối cảnh, nhiệm vụ, input/output và sample.
"""

import os
import re
from pathlib import Path

PROBLEMS_DIR = Path("courses/scratch-bang-a/problems")
LESSONS_DIR = Path("courses/scratch-bang-a/lessons")

LESSON_CONFIG = [
    ("lesson-01-ve-hinh-pen-repeat", ("sca_pen_p0", "sca_pen_p10", "sca_pen_p11", "sca_pen_p12", "sca_pen_p13", "sca_pen_p14", "sca_pen_p15", "sca_pen_p16", "sca_pen_p17", "sca_pen_p18", "sca_pen_p19", "sca_pen_p20"), "BÀI 01 — VẼ HÌNH VỚI PEN VÀ REPEAT", "Chương 1: Bút Vẽ Pen & Đồ Họa"),
    ("lesson-02-hinh-tron-cung-tron-hoa-van", ("sca_pen_p2", "sca_pen_p3", "sca_pen_p4"), "BÀI 02 — HÌNH TRÒN, CUNG TRÒN VÀ HOA VĂN", "Chương 1: Bút Vẽ Pen & Đồ Họa"),
    ("lesson-03-lenh-xuat-nhap-bien-so-kieu-du-lieu", "sca_l03", "BÀI 03 — LỆNH XUẤT NHẬP, BIẾN SỐ VÀ KIỂU DỮ LIỆU", "Chương 2: Lập Trình Tính Toán Cơ Bản & Biến Số"),
    ("lesson-04-toan-tu-va-bieu-thuc", "sca_l04", "BÀI 04 — TOÁN TỬ VÀ BIỂU THỨC SỐ HỌC", "Chương 2: Lập Trình Tính Toán Cơ Bản & Biến Số"),
    ("lesson-05-phep-chia-nguyen-chia-du-luy-thua", "sca_l05", "BÀI 05 — PHÉP CHIA NGUYÊN, CHIA DƯ VÀ LUỸ THỪA", "Chương 2: Lập Trình Tính Toán Cơ Bản & Biến Số"),
    ("lesson-06-cau-truc-re-nhanh-va-dieu-kien-logic", "sca_l06", "BÀI 06 — CẤU TRÚC RẼ NHÁNH VÀ ĐIỀU KIỆN LOGIC", "Chương 3: Cấu Trúc Rẽ Nhánh & Vòng Lặp"),
    ("lesson-07-vong-lap-for-va-dem-tay", "sca_l07", "BÀI 07 — VÒNG LẶP ĐẾM LẦN VÀ BIẾN ĐẾM THỦ CÔNG", "Chương 3: Cấu Trúc Rẽ Nhánh & Vòng Lặp"),
    ("lesson-08-vong-lap-until-va-bien-co", "sca_l08", "BÀI 08 — VÒNG LẶP CHO ĐẾN KHI VÀ BIẾN CỜ DỪNG", "Chương 3: Cấu Trúc Rẽ Nhánh & Vòng Lặp"),
    ("lesson-09-quy-luat-day-so-va-tam-giac-so", "sca_l09", "BÀI 09 — QUY LUẬT DÃY SỐ VÀ TAM GIÁC SỐ", "Chương 4: Số Học & Thuật Toán Tách Số"),
    ("lesson-10-ky-thuat-tach-chu-so-so-nguyen", "sca_l10", "BÀI 10 — KỸ THUẬT TÁCH CHỮ SỐ CỦA SỐ NGUYÊN", "Chương 4: Số Học & Thuật Toán Tách Số"),
    ("lesson-11-uoc-so-boi-so-va-so-nguyen-to", "sca_l11", "BÀI 11 — ƯỚC SỐ, BỘI SỐ VÀ SỐ NGUYÊN TỐ", "Chương 4: Số Học & Thuật Toán Tách Số"),
    ("lesson-12-dem-so-theo-quy-luat-va-so-dac-biet", "sca_l12", "BÀI 12 — ĐẾM SỐ THEO QUY LUẬT VÀ SỐ ĐẶC BIỆT", "Chương 4: Số Học & Thuật Toán Tách Số"),
    ("lesson-13-danh-sach-list-va-thao-tac-co-ban", "sca_l13", "BÀI 13 — DANH SÁCH (LIST) VÀ CÁC THAO TÁC CƠ BẢN", "Chương 5: Danh Sách & Thống Kê Dữ Liệu"),
    ("lesson-14-thong-ke-danh-sach-va-sap-xep", "sca_l14", "BÀI 14 — THỐNG KÊ DANH SÁCH VÀ THUẬT TOÁN SẮP XẾP", "Chương 5: Danh Sách & Thống Kê Dữ Liệu"),
    ("lesson-15-chuoi-ky-tu-chi-so-cat-lat", "sca_l15", "BÀI 15 — CHUỖI KÝ TỰ, CHỈ SỐ VÀ TRÍCH XUẤT", "Chương 6: Xử Lý Chuỗi Ký Tự"),
    ("lesson-16-duyet-chuoi-bien-doi-ky-tu-tach-tu", "sca_l16", "BÀI 16 — DUYỆT CHUỖI, BIẾN ĐỔI KÝ TỰ VÀ TÁCH TỪ", "Chương 6: Xử Lý Chuỗi Ký Tự"),
]

def parse_de_bai(de_bai_path: Path):
    if not de_bai_path.exists():
        return {}
    content = de_bai_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    title = lines[0].replace("#", "").strip() if lines else ""
    
    # Extract sections
    def extract_section(header):
        pat = rf"## {header}\s*\n(.*?)(?=\n## |\Z)"
        m = re.search(pat, content, re.DOTALL)
        return m.group(1).strip() if m else ""

    return {
        "title": title,
        "context": extract_section("Bối cảnh"),
        "task": extract_section("Nhiệm vụ"),
        "input": extract_section("Input"),
        "output": extract_section("Output"),
        "sample": extract_section("Sample 1") or extract_section("Sample"),
    }

def sync_all():
    all_problems = sorted(os.listdir(PROBLEMS_DIR))
    
    for l_dir, sca_pref, title, chapter in LESSON_CONFIG:
        if isinstance(sca_pref, tuple):
            matching = [p for p in all_problems if any(p.startswith(pref) for pref in sca_pref)]
        else:
            matching = [p for p in all_problems if p.startswith(sca_pref)]
        total = len(matching)
        print(f"Syncing {l_dir}: {total} problems...")
        
        # Determine tier ranges
        # P0: first ~25%, P1: next ~25%, P2: next ~25%, P3: rest
        q1 = max(1, total // 4)
        q2 = max(2, total // 2)
        q3 = max(3, (total * 3) // 4)
        
        md = []
        md.append(f"# DANH SÁCH BÀI TẬP THỰC HÀNH: {title}")
        md.append("")
        md.append(f"**Khóa học:** iKHEDU Scratch — Bảng A (Level 1)  ")
        md.append(f"**Chuyên đề:** {chapter}  ")
        md.append(f"> **Tổng số bài tập thực hành:** `{total} bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  ")
        md.append("")
        md.append("---")
        md.append("")
        md.append("## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện")
        md.append("")
        md.append("| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |")
        md.append("|:---:|---|---|:---:|:---:|---|")
        
        parsed_list = []
        for idx, p_name in enumerate(matching, 1):
            p_dir = PROBLEMS_DIR / p_name
            parsed = parse_de_bai(p_dir / "De_Bai.md")
            parsed["code"] = p_name
            
            if idx <= q1:
                tier = "P0"
                cognitive = "Khởi động & Quan sát"
            elif idx <= q2:
                tier = "P1"
                cognitive = "Cơ bản & Hoàn thành"
            elif idx <= q3:
                tier = "P2"
                cognitive = "Luyện tập & Vận dụng"
            else:
                tier = "P3"
                cognitive = "Vận dụng cao & Sáng tạo"
            
            parsed["tier"] = tier
            parsed["cognitive"] = cognitive
            clean_title = parsed["title"] or p_name
            task_short = (parsed["task"][:60] + "...") if len(parsed["task"]) > 60 else parsed["task"]
            md.append(f"| {idx} | `{p_name}` | {clean_title} | **{tier}** | {cognitive} | {task_short} |")
            parsed_list.append(parsed)
            
        md.append("")
        md.append("---")
        md.append("")
        md.append("## 2. Chi Tiết Từng Bài Tập Thực Hành")
        md.append("")
        
        for idx, p in enumerate(parsed_list, 1):
            md.append(f"### Bài {idx} ({p['tier']}): {p['title']}")
            md.append(f"* **Mã bài toán:** `{p['code']}`")
            md.append(f"* **Độ khó & Phân tầng:** {p['tier']} ({p['cognitive']})")
            if p["context"]:
                md.append(f"* **Bối cảnh:** {p['context']}")
            if p["task"]:
                md.append(f"* **Nhiệm vụ:** {p['task']}")
            if p["input"]:
                md.append(f"* **Dữ liệu vào (Input):** {p['input']}")
            if p["output"]:
                md.append(f"* **Kết quả ra (Output):** {p['output']}")
            if p["sample"]:
                md.append(f"* **Dữ liệu mẫu (Sample):**\n\n{p['sample']}\n")
            md.append("---")
            md.append("")
            
        out_file = LESSONS_DIR / l_dir / "Bai_Tap.md"
        out_file.write_text("\n".join(md), encoding="utf-8")
        print(f"-> Wrote {len(md)} lines to {out_file}")

if __name__ == "__main__":
    sync_all()
