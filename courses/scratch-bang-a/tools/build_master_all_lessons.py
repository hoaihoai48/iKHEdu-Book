import os
import glob

# Cấu trúc 16 bài học trong 6 chương của Scratch Bảng A
chapters = [
    {
        "name": "CHƯƠNG 01: BÚT VẼ PEN & ĐỒ HỌA HÌNH HỌC CƠ BẢN",
        "lessons": [
            ("lesson-01-ve-hinh-pen-repeat", "Bài 01: Vẽ hình với Pen và Repeat"),
            ("lesson-02-hinh-tron-cung-tron-hoa-van", "Bài 02: Hình tròn, Cung tròn & Nghệ thuật hoa văn")
        ]
    },
    {
        "name": "CHƯƠNG 02: TÍNH TOÁN CƠ BẢN & BIẾN SỐ",
        "lessons": [
            ("lesson-03-lenh-xuat-nhap-bien-so-kieu-du-lieu", "Bài 03: Lệnh xuất nhập, biến số và kiểu dữ liệu"),
            ("lesson-04-toan-tu-va-bieu-thuc", "Bài 04: Toán tử và biểu thức"),
            ("lesson-05-phep-chia-nguyen-chia-du-luy-thua", "Bài 05: Phép chia nguyên, chia dư và lũy thừa")
        ]
    },
    {
        "name": "CHƯƠNG 03: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP",
        "lessons": [
            ("lesson-06-cau-truc-re-nhanh-va-dieu-kien-logic", "Bài 06: Cấu trúc rẽ nhánh"),
            ("lesson-07-vong-lap-for-va-dem-tay", "Bài 07: Vòng lặp for và hàm range"),
            ("lesson-08-vong-lap-until-va-bien-co", "Bài 08: Vòng lặp while và biến cờ")
        ]
    },
    {
        "name": "CHƯƠNG 04: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ",
        "lessons": [
            ("lesson-09-quy-luat-day-so-va-tam-giac-so", "Bài 09: Quy luật dãy số và tam giác số"),
            ("lesson-10-ky-thuat-tach-chu-so-so-nguyen", "Bài 10: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while"),
            ("lesson-11-uoc-so-boi-so-va-so-nguyen-to", "Bài 11: Ước số, Bội số và Số nguyên tố"),
            ("lesson-12-dem-so-theo-quy-luat-va-so-dac-biet", "Bài 12: Đếm số theo quy luật và số đặc biệt")
        ]
    },
    {
        "name": "CHƯƠNG 05: DANH SÁCH (LIST) & THỐNG KÊ DỮ LIỆU",
        "lessons": [
            ("lesson-13-danh-sach-list-va-thao-tac-co-ban", "Bài 13: Danh sách và thao tác cơ bản"),
            ("lesson-14-thong-ke-danh-sach-va-sap-xep", "Bài 14: Thống kê danh sách và thuật toán sắp xếp")
        ]
    },
    {
        "name": "CHƯƠNG 06: XỬ LÝ CHUỖI KÝ TỰ",
        "lessons": [
            ("lesson-15-chuoi-ky-tu-chi-so-cat-lat", "Bài 15: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự"),
            ("lesson-16-duyet-chuoi-bien-doi-ky-tu-tach-tu", "Bài 16: Duyệt chuỗi, biến đổi ký tự và tách từ")
        ]
    }
]

out_lines = []
out_lines.append("# iKHEDU SCRATCH — TỔNG HỢP NỘI DUNG 6 CHƯƠNG")
out_lines.append("")
out_lines.append("> File tổng hợp tự động toàn bộ nội dung lý thuyết và bài tập của khóa Scratch — Bảng A (Level 1).")
out_lines.append("> Nguồn canonical vẫn là các file trong `lessons/`; không chỉnh sửa trực tiếp file này.")
out_lines.append("")
out_lines.append("## MỤC LỤC TỔNG QUAN")
out_lines.append("")

for ch in chapters:
    out_lines.append(f"### {ch['name']}")
    for l_dir, l_title in ch["lessons"]:
        out_lines.append(f"- {l_title}")
out_lines.append("")

out_lines.append("=" * 80)
out_lines.append("# PHẦN I — LỘ TRÌNH ĐẶC TẢ & QUY CHUẨN SƯ PHẠM SCRATCH")
out_lines.append("=" * 80)
out_lines.append("")
out_lines.append("## 1. Bản chất khóa học & Định hướng năng lực")
out_lines.append("")
out_lines.append("- **Đối tượng:** Học sinh Tiểu học (8–11 tuổi) bắt đầu học lập trình tư duy giải quyết vấn đề.")
out_lines.append("- **Quy mô:** 6 Chương — 16 Bài học (324 bài tập thực hành phân tầng P0–P3).")
out_lines.append("- **Mô hình Dual-Track:**")
out_lines.append("  - Track 1 (Bài 01–02): Native Scratch Foundation — Bút vẽ Pen & Đồ họa hình học đối xứng.")
out_lines.append("  - Track 2 (Bài 03–16): Algorithmic Thinking — Kỹ thuật tư duy giải thuật toán trực quan với khối lệnh Scratch 3.0.")
out_lines.append("")
out_lines.append("## 2. Các Quy Chuẩn Lập Trình Khối Lệnh Scratch 3.0 Tiếng Việt")
out_lines.append("")
out_lines.append("| Khái niệm lập trình | Khối lệnh Scratch 3.0 Tiếng Việt | Lưu ý sư phạm & Bẫy lỗi |")
out_lines.append("|---|---|---|")
out_lines.append("| Nhập dữ liệu | `hỏi [Nhập...] và đợi` + `đặt [biến v] thành (câu trả lời)` | Luôn cất `câu trả lời` vào biến số riêng ngay trước khi hỏi câu tiếp theo |")
out_lines.append("| Xuất kết quả | `nói (kết quả)` | Ghép nhiều thông tin bằng khối `kết hợp () ()` |")
out_lines.append("| Hoán đổi 2 biến | `đặt [tam v] thành (a)` -> `đặt [a v] thành (b)` -> `đặt [b v] thành (tam)` | Dùng biến trung gian `tam` như một chiếc cốc phụ |")
out_lines.append("| Chia nguyên, chia dư | `[làm tròn xuống v] của ((A) / (B))`, `(A) mod (B)` | Khối phép toán màu xanh lá cây |")
out_lines.append("| Vòng lặp đếm lần | `đặt [i v] thành (1)` + `lặp lại (n) lần { ... thay đổi [i v] một lượng (1) }` | Khởi tạo biến đếm và luôn tăng biến ở cuối mỗi vòng lặp |")
out_lines.append("| Vòng lặp điều kiện | `lặp lại cho đến khi <điều kiện dừng>` | Chú ý: Vòng lặp sẽ dừng ngay khi điều kiện bên trong trở thành ĐÚNG |")
out_lines.append("| Phần tử danh sách | `phần tử (1) của [Dãy số v]` | **Bẫy 1-based index:** Danh sách Scratch bắt đầu từ vị trí số 1 |")
out_lines.append("| Độ dài / Kích thước | `độ dài của (chuỗi)` / `kích thước của [danh sách v]` | Khối tròn giá trị màu xanh lá / màu cam |")
out_lines.append("| Ký tự trong chuỗi | `ký tự (1) của (chuỗi)` | Ký tự đầu tiên trong chuỗi luôn ở vị trí số 1 |")
out_lines.append("")

out_lines.append("=" * 80)
out_lines.append("# PHẦN II — NỘI DUNG CHI TIẾT 16 BÀI HỌC (LÝ THUYẾT & BÀI TẬP)")
out_lines.append("=" * 80)
out_lines.append("")

base_dir = "courses/scratch-bang-a/lessons"

for ch in chapters:
    out_lines.append("=" * 80)
    out_lines.append(f"# {ch['name']}")
    out_lines.append("=" * 80)
    out_lines.append("")
    
    for l_dir, l_title in ch["lessons"]:
        l_path = f"{base_dir}/{l_dir}"
        lesson_files = glob.glob(f"{l_path}/Lesson*.md")
        if not lesson_files:
            continue
        content_path = lesson_files[0]
        baitap_path = f"{l_path}/Bai_Tap.md"
        
        out_lines.append("-" * 80)
        out_lines.append(f"<!-- {l_title} -->")
        out_lines.append("-" * 80)
        out_lines.append("")
        out_lines.append("## Lý thuyết và Concept Quiz")
        out_lines.append("")
        
        if os.path.exists(content_path):
            with open(content_path, "r", encoding="utf-8") as f:
                c_text = f.read().strip()
                c_text = c_text.replace("../../assets/", "assets/")
                out_lines.append(c_text)
            
        out_lines.append("")
        out_lines.append("## Bài tập lesson")
        out_lines.append("")
        
        if os.path.exists(baitap_path):
            with open(baitap_path, "r", encoding="utf-8") as f:
                b_text = f.read().strip()
                b_text = b_text.replace("../../assets/", "assets/")
                out_lines.append(b_text)
            
        out_lines.append("")

target_master = "courses/scratch-bang-a/MASTER_ALL_LESSONS.md"
with open(target_master, "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(f"Master file created: {target_master}")
with open(target_master, "r", encoding="utf-8") as f:
    line_count = len(f.readlines())
print(f"Total lines in {target_master}: {line_count}")
