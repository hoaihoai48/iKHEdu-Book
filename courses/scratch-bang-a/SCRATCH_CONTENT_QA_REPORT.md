# BÁO CÁO TỔNG THỂ QA VÀ REBUILD NỘI DUNG SCRATCH BẢNG A
*(Thực hiện và cập nhật đầy đủ theo đặc tả SPEC_ANTI_REBUILD_QA.md)*

## A. TỔNG QUAN (SUMMARY)
- **Số bài học đã kiểm tra:** 16 / 16 bài học (Lesson 01 đến Lesson 16).
- **Số bài tập thực hành đã kiểm tra:** 324 / 324 bài tập (37 bài Pen đồ họa + 287 bài Thuật toán).
- **Số câu hỏi trắc nghiệm đã kiểm tra:** 182 / 182 câu Quiz (Chi tiết: L01: 10, L02: 10, L03: 13, L04: 10, L05: 14, L06: 10, L07: 13, L08: 10, L09: 10, L10: 10, L11: 12, L12: 10, L13: 13, L14: 13, L15: 14, L16: 10).
- **Hình ảnh đã rà soát:** Hơn 670 assets hình ảnh (bao gồm ảnh trắc nghiệm, sơ đồ khối lệnh render và ảnh kết quả vẽ hình Pen).
- **Broken Image Links:** 0 (Đã sửa dứt điểm 31 relative paths trong 14 file Production Content).
- **Tình trạng file Word xuất bản:** Đã rebuild thành công toàn bộ 4 file Word (`scratch-full.docx` và 3 quyển giáo viên).

---

## B. CHI TIẾT CÁC LỖI ĐÃ KHẮC PHỤC (FIXED ISSUES)

| ID | Bài học | Phân loại | Thành phần ảnh hưởng | Trước khi sửa (Before) | Sau khi sửa (After) |
|:---:|:---:|:---:|:---:|---|---|
| **ISS-01** | L15 | Thuật toán & Dry-run | `Lesson15_Production_Content.md` | Cắt chuỗi `"SCRATCH"` từ $L=2$ đến $R=4$ ghi kết quả sai thành `"YTH"` (do copy từ Python). | Đã sửa thành **`"CRA"`** (ký tự 2: C, 3: R, 4: A), độ dài chuẩn 7 ký tự. |
| **ISS-02** | L15 | Nhất quán dữ liệu mẫu | `Bai_Tap.md` (Bài 1, 6, 10) | Sample Input ghi `SCRATCH` nhưng Output ghi `P N` và `PYT / HON`. | Đã đồng bộ Input thành **`PYTHON`** khớp 100% với `De_Bai.md` và Output mẫu. |
| **ISS-03** | L02 | Hình học & Khối lệnh | `Lesson02_Production_Content.md` | Hướng dẫn xoay trái 90 độ rồi lùi $-R$ bước làm lệch hướng về tâm. | Đã chuẩn hóa: Xoay trái 90° để đầu bút hướng tâm rồi đi tới $R$ bước, hoặc dùng tọa độ tâm `(x0, y0)`. |
| **ISS-04** | L02 | Trắc nghiệm đồng bộ | `Lesson02_Production_Content.md` (Quiz 10) | Câu hỏi về quay về tâm mâu thuẫn giữa hướng nhìn tiếp tuyến và lùi $-R$. | Đã chuẩn hóa ăn khớp: Quiz 10 xác định rõ trường hợp vẽ tia nan hoa từ tâm tỏa ra mép thì đi lùi $-R$ bước dọc theo tia để về tâm mà không đổi hướng nhìn. |
| **ISS-05** | L03 | Sư phạm & Tiêu đề | `Lesson03_Production_Content.md` | Dùng thuật ngữ RAM/CPU; tiêu đề thiếu "Kiểu dữ liệu". | Đã loại bỏ RAM/CPU; bổ sung giải thích 3 kiểu dữ liệu cốt lõi (Số, Chuỗi, Boolean); khôi phục tiêu đề *"Lệnh xuất nhập, biến số và kiểu dữ liệu"*. |
| **ISS-06** | L07 | Thuật ngữ & Trực quan | `Lesson07_Production_Content.md` | Tiêu đề "Vòng lặp for và hàm range" khiến học sinh nhầm Scratch có hàm `range()`. | Đã đổi tiêu đề thành *"Vòng lặp biết trước số lần và biến đếm"*, thêm góc liên hệ Scratch `repeat` vs Python `for`. |
| **ISS-07** | L08 | Sư phạm & Tiêu đề | `Lesson08_Production_Content.md` | Khẳng định Collatz như định lý; tiêu đề ghi "while". | Đổi tiêu đề thành *"Vòng lặp until, biến cờ và điều khiển vòng lặp"*; framing Collatz là bài toán mô phỏng chuỗi số. |
| **ISS-08** | L01 | Ảnh minh họa kết quả | `sca_pen_p08_tam_giac_xoay_chong` | Bị gán nhầm 2 hình vuông nan hoa và hoa thị mũi tên không liên quan. | Đã tạo và gán đúng 1 hình chuẩn: **12 tam giác đều lồng nhau xoay quanh 1 đỉnh**. |
| **ISS-09** | L01 | Ảnh minh họa kết quả | `sca_pen_p04_cap_tam_giac_doi_xung` | Đính kèm cả tam giác Sierpinski fractal và hình ngôi sao. | Đã giữ lại duy nhất hình mẫu chuẩn: **Ngôi sao 6 cánh tạo từ 2 tam giác đều đối xứng**. |
| **ISS-10** | L01–16| Đường dẫn tài nguyên | 14 file `Production_Content.md` | 31 đường dẫn ảnh dùng `assets/rendered_blocks/...` bị lỗi hiển thị. | Đã sửa thành đường dẫn tương đối chuẩn `../../assets/rendered_blocks/...`, đạt 0 broken link. |
| **ISS-11** | Toàn khóa | Metadata & Tài liệu | `README.md` | Số liệu cũ (308 bài, 21 bài Pen, L01=22, L02=15; tổng Quiz 190 / 184 lệch chi tiết). | Đã đồng bộ chuẩn 100%: **324 bài tập** (37 Pen + 287 Thuật toán), L01=16, L02=21, tổng **182 câu Concept Quiz** khớp từng dòng trong bảng. |

---

## C. PHÂN TẦNG VÀ GIỮ VỮNG PHẠM VI BÀI TẬP (PROBLEMS RECLASSIFIED / SCOPE progression)

Theo đúng nguyên tắc của đặc tả (`SPEC_ANTI_REBUILD_QA.md` mục 2 và 7), **không xóa bài tập hay đổi ID**, mà thực hiện phân tầng nhận thức và độ khó:

1. **Phạm vi Lesson 04 (Toán tử & Biểu thức):**
   - Các bài tập áp dụng toán tử cơ bản cộng, trừ, nhân, chia, biểu thức đại số, đóng gói PEMDAS được giữ ở tầng **CORE (P0, P1)**.
   - Các bài toán tiếp cận sớm phép chia nguyên/dư (chia kẹo, số kẹo còn thừa, lấy chữ số tận cùng $N \pmod{10}$, đổi phút ra giờ phút) được phân loại ở tầng **EXTENSION (P2) & CHALLENGE (P3)**: Đóng vai trò bài toán phát triển tư duy bước đệm, chuẩn bị tiếp nối tự nhiên sang Lesson 05 (`floor` và `mod`).

2. **Phạm vi các bài toán nâng cao (L11, L12, L14, L15, L16):**
   - Các bài toán thuật toán nâng cao như: Số siêu nguyên tố, Ước chung lớn nhất (UCLN/BCNN), Sắp xếp Bubble Sort, Đảo ngược chuỗi, Mã hóa Caesar, Tách từ... đều được phân định rõ ràng ở tầng **P2 (Vận dụng) và P3 (Vận dụng cao & Sáng tạo)**.
   - Học sinh theo học chuẩn nền tảng Bảng A hoàn thành trọn vẹn tầng CORE (P0 - P1), trong khi học sinh ôn luyện đội tuyển Tin học trẻ nâng cao có lộ trình thử thách tại tầng P2 - P3.

3. **Tính nhất quán phân tầng P-level (L01 & L02):**
   - Đã kiểm tra 100% heading `### Bài X (Py): Tiêu đề` và metadata `* **Độ khó & Phân tầng:** Py` trong `Bai_Tap.md` của Bài 01 và Bài 02: **Tất cả các tiêu đề và chi tiết đều khớp nhau 100%**.

---

## D. THỐNG KÊ CHI TIẾT CÂU HỎI TRẮC NGHIỆM (QUIZ AUDIT)

Đã đối chiếu trực tiếp từ source từng bài học, đảm bảo không có câu hỏi dư thừa hay số liệu ảo:

| Bài học | Tên bài học | Số Quiz thực tế | Dạng câu hỏi |
|:---:|---|:---:|---|
| **L01** | Vẽ hình với Pen và Repeat | 10 | Nhận diện góc quay đa giác, đặt hướng, lệnh Pen, thủ tục con |
| **L02** | Hình tròn, cung tròn và hoa văn | 10 | Bước đi cong viền ngoài, cung $90^\circ, 180^\circ$, Olympic, quay về tâm |
| **L03** | Lệnh xuất nhập, biến số và kiểu dữ liệu | 13 | Khối hỏi/đợi, biến câu trả lời, 3 kiểu dữ liệu, hoán đổi biến |
| **L04** | Toán tử và biểu thức | 10 | Thứ tự ưu tiên PEMDAS, ghép khối ngoặc, chia thực trong Scratch |
| **L05** | Phép chia nguyên, chia dư và lũy thừa | 14 | `floor`, `mod`, đổi đơn vị thời gian, tuần hoàn kim đồng hồ |
| **L06** | Cấu trúc rẽ nhánh và điều kiện logic | 10 | `if`, `if-else`, toán tử `and/or/not`, tìm Max/Min |
| **L07** | Vòng lặp biết trước số lần và biến đếm | 13 | Cơ chế `lặp lại () lần`, quy tắc 3 bước biến đếm, tích lũy dồn |
| **L08** | Vòng lặp until, biến cờ và điều khiển vòng lặp | 10 | Điều kiện dừng phủ định trong `repeat until`, biến cờ, tránh lặp vô tận |
| **L09** | Quy luật dãy số và tam giác số | 10 | Dãy số cách đều, Fibonacci 3 biến cuộn, vòng lặp lồng nhau |
| **L10** | Kỹ thuật tách chữ số và xử lý số nguyên | 10 | Vòng lặp bóc tách `mod 10`, `floor(/10)`, đảo ngược số, đếm chữ số |
| **L11** | Ước số, bội số và số nguyên tố | 12 | Kiểm tra ước chia hết, cờ nguyên tố, tối ưu $i \times i \le N$, UCLN |
| **L12** | Đếm số theo quy luật và số đặc biệt | 10 | Đếm $O(1)$ khoảng $[A, B]$, số chính phương, số Armstrong |
| **L13** | Danh sách (List) và thao tác cơ bản | 13 | Danh sách 1-based, `thêm`, `xóa`, `chèn`, `phần tử thứ`, `chứa` |
| **L14** | Thống kê danh sách và sắp xếp | 13 | Tìm Max/Min trong List, tính trung bình cộng, thuật toán Bubble Sort |
| **L15** | Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự | 14 | Ký tự 1-based, độ dài chuỗi, vòng lặp trích xuất chuỗi con, Palindrome |
| **L16** | Duyệt chuỗi, biến đổi ký tự và tách từ | 10 | Đếm ký tự, tách từ qua dấu cách vào danh sách, đếm từ |
| **TỔNG CỘNG** | **16 BÀI HỌC TOÀN KHÓA** | **182 CÂU** | **100% ĐÁP ÁN ĐÃ ĐỐI CHIẾU CHUẨN XÁC** |

---

## E. DANH MỤC THAY ĐỔI HÌNH ẢNH (IMAGE CHANGES)
1. **`sca_pen_p08_tam_giac_xoay_chong`**:
   - *Gốc:* Nhúng nhầm `pen_img_160.png` (vuông nan hoa) và `pen_img_161.png` (hoa thị mũi tên).
   - *Khắc phục:* Thay thế bằng duy nhất `pen_img_tam_giac_xoay_chong_chuan.png` (hoa văn 12 tam giác đều chung 1 đỉnh chuẩn xác $100\%$).
2. **`sca_pen_p04_cap_tam_giac_doi_xung`**:
   - *Gốc:* Chứa cả `pen_img_107.png` (tam giác Sierpinski fractal) và hình ngôi sao.
   - *Khắc phục:* Loại bỏ ảnh fractal, giữ đúng 1 hình chuẩn `gen_sao_6_canh.png` (ngôi sao 6 cánh tạo từ 2 tam giác đều lồng nhau đối xứng).
3. **14 Bài học Production Content:**
   - Đã chuẩn hóa 31 đường dẫn ảnh từ `assets/rendered_blocks/...` thành `../../assets/rendered_blocks/...`.

---

## F. CÁC VẤN ĐỀ CÒN LẠI (REMAINING ISSUES)
- Không có vấn đề blocker hay lỗi kỹ thuật thuật toán nào còn tồn đọng trong 16 bài học Scratch Bảng A.
- Toàn bộ 4 file Word đã được biên dịch sạch, mục lục OpenXML cập nhật tự động an toàn.

---

## G. DANH SÁCH FILE WORD ĐÃ REBUILD VÀ SẴN SÀNG
1. **`courses/scratch-bang-a/scratch-full.docx`** (7.8 MB) — Bản gộp đầy đủ 16 bài học, 324 bài tập.
2. **`courses/scratch-bang-a/scratch-giaovien-quyen-1.docx`** (6.0 MB) — Sách giáo viên Quyển 1 (Bút vẽ & Nền tảng khối lệnh).
3. **`courses/scratch-bang-a/scratch-giaovien-quyen-2.docx`** (10.5 MB) — Sách giáo viên Quyển 2 (Rẽ nhánh, Vòng lặp & Số học).
4. **`courses/scratch-bang-a/scratch-giaovien-quyen-3.docx`** (5.6 MB) — Sách giáo viên Quyển 3 (Danh sách List & Chuỗi ký tự).
