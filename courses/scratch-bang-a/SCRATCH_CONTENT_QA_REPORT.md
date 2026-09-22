# BÁO CÁO TỔNG THỂ QA VÀ REBUILD NỘI DUNG SCRATCH BẢNG A
*(Thực hiện theo đặc tả SPEC_ANTI_REBUILD_QA.md)*

## A. TỔNG QUAN (SUMMARY)
- **Số bài học đã kiểm tra:** 16 / 16 bài học (Lesson 01 đến Lesson 16).
- **Số bài tập thực hành đã kiểm tra:** 324 / 324 bài tập (37 bài Pen + 287 bài Thuật toán).
- **Số câu hỏi trắc nghiệm đã kiểm tra:** 184 / 184 câu Quiz.
- **Tình trạng file Word xuất bản:** Đã rebuild thành công toàn bộ 4 file Word (`scratch-full.docx` và 3 quyển giáo viên).

---

## B. CHI TIẾT CÁC LỖI ĐÃ KHẮC PHỤC (FIXED ISSUES)

| ID | Bài học | Phân loại | Thành phần ảnh hưởng | Trước khi sửa (Before) | Sau khi sửa (After) |
|:---:|:---:|:---:|:---:|---|---|
| **ISS-01** | L15 | Thuật toán & Dry-run | `Lesson15_Production_Content.md` | Cắt chuỗi `"SCRATCH"` từ $L=2$ đến $R=4$ ghi kết quả sai thành `"YTH"` (do copy từ Python). | Đã sửa thành **`"CRA"`** (ký tự 2: C, 3: R, 4: A), độ dài chuẩn 7 ký tự. |
| **ISS-02** | L15 | Nhất quán dữ liệu mẫu | `Bai_Tap.md` (Bài 1, 6, 10) | Sample Input ghi `SCRATCH` nhưng Output ghi `P N` và `PYT / HON`. | Đã đồng bộ Input thành **`PYTHON`** khớp 100% với `De_Bai.md` và Output mẫu. |
| **ISS-03** | L02 | Hình học & Khối lệnh | `Lesson02_Production_Content.md` | Hướng dẫn xoay trái 90 độ rồi lùi $-R$ bước làm lệch hướng về tâm. | Đã chuẩn hóa: Xoay trái 90° để đầu bút hướng tâm rồi đi tới $R$ bước, hoặc dùng tọa độ tâm `(x0, y0)`. |
| **ISS-04** | L02 | Trắc nghiệm | `Lesson02_Production_Content.md` (Quiz 10) | Câu hỏi về quay về tâm chưa rõ ràng về hướng nhìn. | Đã sửa thành câu hỏi chuẩn về lùi $-R$ bước theo phương nan hoa vừa vẽ. |
| **ISS-05** | L03 | Sư phạm & Khái niệm | `Lesson03_Production_Content.md` | Dùng thuật ngữ kỹ thuật RAM, CPU; chưa có mục kiểu dữ liệu. | Đã loại bỏ RAM/CPU, bổ sung mục Kiểu dữ liệu trực quan: Số, Chuỗi văn bản, Boolean. |
| **ISS-06** | L07 | Thuật ngữ & Trực quan | `Lesson07_Production_Content.md` | Tiêu đề "Vòng lặp for và hàm range" khiến học sinh nhầm Scratch có hàm `range()`. | Đã đổi tiêu đề thành *"Vòng lặp biết trước số lần và biến đếm"*, thêm góc liên hệ Scratch `repeat` vs Python `for`. |
| **ISS-07** | L08 | Sư phạm & Toán học | `Lesson08_Production_Content.md` | Khẳng định thuật toán Collatz như định lý chắc chắn về 1. | Đã chuyển sang góc độ mô phỏng quy tắc biến đổi số $3n+1$ cho số đầu vào cụ thể. |
| **ISS-08** | L01 | Ảnh minh họa kết quả | `sca_pen_p08_tam_giac_xoay_chong` | Bị gán nhầm 2 hình vuông nan hoa và hoa thị mũi tên không liên quan. | Đã tạo và gán đúng 1 hình chuẩn: **12 tam giác đều lồng nhau xoay quanh 1 đỉnh**. |
| **ISS-09** | L01 | Ảnh minh họa kết quả | `sca_pen_p04_cap_tam_giac_doi_xung` | Đính kèm cả tam giác Sierpinski fractal và hình ngôi sao. | Đã giữ lại duy nhất hình mẫu chuẩn: **Ngôi sao 6 cánh tạo từ 2 tam giác đều đối xứng**. |
| **ISS-10** | L01–16| Đường dẫn tài nguyên | 14 file `Production_Content.md` | 31 đường dẫn ảnh dùng `assets/rendered_blocks/...` bị lỗi hiển thị. | Đã sửa thành đường dẫn tương đối chuẩn `../../assets/rendered_blocks/...`, đạt 0 broken link. |
| **ISS-11** | Toàn khóa | Metadata & Tài liệu | `README.md` | Số liệu cũ (308 bài, 21 bài Pen, L01=22, L02=15). | Đã cập nhật đúng thực tế: **324 bài tập** (37 Pen + 287 Thuật toán), L01=16, L02=21, 184 Quiz. |

---

## C. DANH SÁCH FILE WORD ĐÃ REBUILD VÀ SẴN SÀNG
1. **`courses/scratch-bang-a/scratch-full.docx`** (7.8 MB) — Bản gộp đầy đủ 16 bài học, 324 bài tập.
2. **`courses/scratch-bang-a/scratch-giaovien-quyen-1.docx`** (6.0 MB) — Sách giáo viên Quyển 1 (Bút vẽ & Nền tảng khối lệnh).
3. **`courses/scratch-bang-a/scratch-giaovien-quyen-2.docx`** (10.5 MB) — Sách giáo viên Quyển 2 (Rẽ nhánh, Vòng lặp & Số học).
4. **`courses/scratch-bang-a/scratch-giaovien-quyen-3.docx`** (5.6 MB) — Sách giáo viên Quyển 3 (Danh sách List & Chuỗi ký tự).
