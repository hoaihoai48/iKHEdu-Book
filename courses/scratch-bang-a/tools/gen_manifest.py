import os
import re
import json
from pathlib import Path

REPO_ROOT = Path("/Users/vu/Developer/ikhEdu_lessons")
SCRATCH_DIR = REPO_ROOT / "courses" / "scratch-bang-a"
LESSONS_DIR = SCRATCH_DIR / "lessons"

LESSON_DIRS = [
    ("lesson-01-ve-hinh-pen-repeat", 1, 1, "Bài 01: Vẽ hình với Pen và Repeat"),
    ("lesson-02-hinh-tron-cung-tron-hoa-van", 1, 2, "Bài 02: Hình tròn, cung tròn và hoa văn"),
    ("lesson-03-lenh-xuat-nhap-bien-so-kieu-du-lieu", 2, 3, "Bài 03: Lệnh xuất nhập, biến số và kiểu dữ liệu"),
    ("lesson-04-toan-tu-va-bieu-thuc", 2, 4, "Bài 04: Toán tử và biểu thức"),
    ("lesson-05-phep-chia-nguyen-chia-du-luy-thua", 2, 5, "Bài 05: Phép chia nguyên, chia dư và lũy thừa"),
    ("lesson-06-cau-truc-re-nhanh-va-dieu-kien-logic", 3, 6, "Bài 06: Cấu trúc rẽ nhánh và điều kiện logic"),
    ("lesson-07-vong-lap-for-va-dem-tay", 3, 7, "Bài 07: Vòng lặp for và đếm tay"),
    ("lesson-08-vong-lap-until-va-bien-co", 3, 8, "Bài 08: Vòng lặp until và biến cờ"),
    ("lesson-09-quy-luat-day-so-va-tam-giac-so", 4, 9, "Bài 09: Quy luật dãy số và tam giác số"),
    ("lesson-10-ky-thuat-tach-chu-so-so-nguyen", 4, 10, "Bài 10: Kỹ thuật tách chữ số và xử lý số nguyên"),
    ("lesson-11-uoc-so-boi-so-va-so-nguyen-to", 4, 11, "Bài 11: Ước số, bội số và số nguyên tố"),
    ("lesson-12-dem-so-theo-quy-luat-va-so-dac-biet", 4, 12, "Bài 12: Đếm số theo quy luật và số đặc biệt"),
    ("lesson-13-danh-sach-list-va-thao-tac-co-ban", 5, 13, "Bài 13: Danh sách (List) và thao tác cơ bản"),
    ("lesson-14-thong-ke-danh-sach-va-sap-xep", 5, 14, "Bài 14: Thống kê danh sách và sắp xếp"),
    ("lesson-15-chuoi-ky-tu-chi-so-cat-lat", 6, 15, "Bài 15: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự"),
    ("lesson-16-duyet-chuoi-bien-doi-ky-tu-tach-tu", 6, 16, "Bài 16: Duyệt chuỗi, biến đổi ký tự và tách từ"),
]

volumes = [
    {
        "volume": 1,
        "title": "Giáo trình Scratch Bảng A — Quyển 1: Bút Vẽ Đồ Họa & Nền Tảng Khối Lệnh",
        "header_book": "Giáo trình Scratch Bảng A - quyển 1",
        "preface": "reference/Loi_Noi_Dau_Scratch_Quyen1.md",
        "appendix_a": "reference/Phu_Luc_A_Scratch.md",
        "output": "scratch-level-1-quyen-1.docx",
        "lessons": []
    },
    {
        "volume": 2,
        "title": "Giáo trình Scratch Bảng A — Quyển 2: Thuật Toán Số Học, Danh Sách & Chuỗi Ký Tự",
        "header_book": "Giáo trình Scratch Bảng A - quyển 2",
        "preface": "reference/Loi_Noi_Dau_Scratch_Quyen2.md",
        "appendix_a": "reference/Phu_Luc_A_Scratch.md",
        "output": "scratch-level-1-quyen-2.docx",
        "lessons": []
    }
]

total_problems = 0
for folder, chap, les_num, les_title in LESSON_DIRS:
    bt_file = LESSONS_DIR / folder / "Bai_Tap.md"
    prod_file = LESSONS_DIR / folder / f"Lesson{les_num:02d}_Production_Content.md"
    if not prod_file.exists():
        matches = list((LESSONS_DIR / folder).glob("*Production*.md"))
        prod_file = matches[0] if matches else None

    bt_text = bt_file.read_text(encoding="utf-8") if bt_file.exists() else ""
    
    # Fast parser: read matrix table lines | STT | `code` | Title |
    problem_entries = []
    for line in bt_text.splitlines():
        line_str = line.strip()
        if line_str.startswith("|") and "`" in line_str:
            m = re.search(r"\|\s*\d+\s*\|\s*`([^`]+)`\s*\|\s*([^\|]+)\|", line_str)
            if m:
                code = m.group(1).strip()
                title = m.group(2).strip()
                problem_entries.append({"code": code, "title": title})

    seen = set()
    dedup_problems = []
    for p in problem_entries:
        if p["code"] not in seen:
            seen.add(p["code"])
            dedup_problems.append(p)

    lesson_obj = {
        "lesson": les_num,
        "chapter": chap,
        "folder": folder,
        "title": les_title,
        "content_file": str(prod_file.relative_to(SCRATCH_DIR)) if prod_file else "",
        "problems": dedup_problems
    }
    
    if les_num <= 8:
        volumes[0]["lessons"].append(lesson_obj)
    else:
        volumes[1]["lessons"].append(lesson_obj)
    total_problems += len(dedup_problems)

manifest = {
    "course": "scratch-bang-a",
    "total_problems": total_problems,
    "volumes": volumes
}

out_manifest = SCRATCH_DIR / "tools" / "word_build_manifest.json"
out_manifest.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Manifest written successfully: {out_manifest}")
print(f"Total problems mapped: {total_problems}")
print("Volume 1:", len(volumes[0]["lessons"]), "lessons,", sum(len(l["problems"]) for l in volumes[0]["lessons"]), "problems")
print("Volume 2:", len(volumes[1]["lessons"]), "lessons,", sum(len(l["problems"]) for l in volumes[1]["lessons"]), "problems")
