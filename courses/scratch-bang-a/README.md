# iKHEDU SCRATCH — BẢNG A (LEVEL 1)

## Tư Duy Khối Lệnh, Đồ Họa & Thuật Toán Thi Đấu

> **Trang chủ quản trị khóa học**: Khóa học lập trình khối lệnh Scratch dành cho học sinh Tiểu học (8–11 tuổi), chuẩn bị nền tảng vững chắc cho kỳ thi **Tin học trẻ Bảng A**, gồm **6 Chương — 16 Bài học chuyên sâu**, kho **308 Bài tập thực hành thật** và hệ thống hình ảnh trực quan 100%.

---

## 1. Thông Tin Tổng Quan

| Trường | Giá trị |
|---|---|
| **Tên khóa học** | iKHEDU Scratch — Level 1 (Bảng A) |
| **Mã khóa học** | `scratch-bang-a` |
| **Đối tượng** | Học sinh Tiểu học 8–11 tuổi (Lớp 3, 4, 5) |
| **Mục tiêu đầu ra** | Làm chủ kỹ thuật đồ họa Bút vẽ Pen; chuyển giao và làm chủ toàn bộ các cấu trúc thuật toán kinh điển (I/O, biến số, rẽ nhánh, vòng lặp, tách chữ số, ước/nguyên tố, danh sách 1-based, chuỗi ký tự) trên môi trường khối lệnh Scratch 3.0 |
| **Ngôn ngữ / Nền tảng** | Scratch 3.0 (Khối lệnh) & Scratchblocks DSL text format |
| **Giọng điệu sư phạm** | Trực quan, gợi hình, gần gũi với lứa tuổi thiếu nhi, khoa học, trực diện bản chất máy tính |
| **Chu trình học tập** | `Vấn đề thực tế sân khấu → Mô phỏng bảng chạy biến / tọa độ → Khối lệnh tiêu điểm → Bẫy lỗi kinh điển → Concept Quiz (>=10 câu) → Bài tập 2 trục P0-P3 x 4 mức nhận thức` |
| **Quy chuẩn bài tập** | **100% Bài tập thật (Zero Dummy / Zero Placeholder)**: 21 bài đồ họa Pen + 287 bài toán thuật toán Tin học trẻ có nguồn trace 1-1 về Python Bảng A |
| **Trạng thái** | `v1.0.0` — Production |

---

## 2. Bản Đồ 6 Chương & 16 Bài Học

```text
PROGRAM: Scratch Bảng A (Level 1)
 ├── CHƯƠNG 1: BÚT VẼ PEN & ĐỒ HỌA (Bài 01 – 02) [TRACK 1: NATIVE FOUNDATION]
 │    ├── Bài 01: Vẽ hình với Pen và Repeat
 │    └── Bài 02: Hình tròn, cung tròn và hoa văn
 │
 ├── CHƯƠNG 2: TÍNH TOÁN CƠ BẢN (Bài 03 – 05) [TRACK 2: KHỚP CHƯƠNG 1 PYTHON]
 │    ├── Bài 03: Lệnh xuất nhập, biến số và kiểu dữ liệu
 │    ├── Bài 04: Toán tử và biểu thức
 │    └── Bài 05: Phép chia nguyên, chia dư và lũy thừa
 │
 ├── CHƯƠNG 3: CẤU TRÚC RẼ NHÁNH & CẤU TRÚC VÒNG LẶP (Bài 06 – 08) [KHỚP CHƯƠNG 2 PYTHON]
 │    ├── Bài 06: Cấu trúc rẽ nhánh và điều kiện logic
 │    ├── Bài 07: Vòng lặp for và hàm range
 │    └── Bài 08: Vòng lặp while, biến cờ và điều khiển vòng lặp
 │
 ├── CHƯƠNG 4: BÀI TOÁN SỐ HỌC & TÁCH CHỮ SỐ (Bài 09 – 12) [KHỚP CHƯƠNG 3 PYTHON]
 │    ├── Bài 09: Quy luật dãy số và tam giác số
 │    ├── Bài 10: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while
 │    ├── Bài 11: Ước số, bội số và số nguyên tố
 │    └── Bài 12: Đếm số theo quy luật và số đặc biệt
 │
 ├── CHƯƠNG 5: DANH SÁCH (LIST) & THỐNG KÊ (Bài 13 – 14) [KHỚP CHƯƠNG 4 PYTHON]
 │    ├── Bài 13: Danh sách và thao tác cơ bản
 │    └── Bài 14: Thống kê danh sách và sắp xếp
 │
 └── CHƯƠNG 6: XỬ LÝ CHUỖI KÝ TỰ (Bài 15 – 16) [KHỚP CHƯƠNG 5 PYTHON]
      ├── Bài 15: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự
      └── Bài 16: Duyệt chuỗi, biến đổi ký tự và tách từ
```

---

## 3. Bảng Chi Tiết 16 Bài Học & Định Mức Học Liệu

| Chương | Bài | Mã | Tên bài học | Khối lệnh tiêu điểm | Nguồn bài thật | Quiz | Bài tập |
|:---:|:---:|:---:|---|---|---|:---:|:---:|
| **1** | 01 | `SCA-L01` | Vẽ hình với Pen và Repeat | Pen, Motion, `repeat (n)`, công thức $360^\circ/n$ | `CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx` | 10 | 22 |
| | 02 | `SCA-L02` | Hình tròn, cung tròn và hoa văn | Bước đi cong $(2\pi R)/360$, My Blocks tham số $R$ | `CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx` | 10 | 15 |
| **2** | 03 | `SCA-L03` | Lệnh xuất nhập, biến số và kiểu dữ liệu | `ask/answer`, `set to`, `say join`, biến tạm | `pya_l01_*` (25 bài) | 12 | 25 |
| | 04 | `SCA-L04` | Toán tử và biểu thức | Khối toán `+ - * /`, lồng khối thay dấu ngoặc | `pya_l02_*` (36 bài) | 12 | 36 |
| | 05 | `SCA-L05` | Phép chia nguyên, chia dư và lũy thừa | `floor (A / B)`, `(A) mod (B)`, thời gian $H:M:S$ | `pya_l03_*` (33 bài) | 12 | 33 |
| **3** | 06 | `SCA-L06` | Cấu trúc rẽ nhánh và điều kiện logic | `if <> then`, `if <> then else`, `and / or / not` | `pya_l04/l05/l06_*` (37 bài) | 12 | 37 |
| | 07 | `SCA-L07` | Vòng lặp for và hàm range | `repeat (n)` + biến đếm tay `i`, tích dồn, cửu chương | `pya_l07_*` (14 bài) | 12 | 14 |
| | 08 | `SCA-L08` | Vòng lặp while, biến cờ và điều khiển vòng lặp | `repeat until <phủ định>`, cờ flag $0/1$, bẫy vô tận | `pya_l08_*` (12 bài) | 12 | 12 |
| **4** | 09 | `SCA-L09` | Quy luật dãy số và tam giác số | Cấp số cộng, Fibonacci cuộn chiếu, tam giác Floyd | `pya_l09_*` (14 bài) | 12 | 14 |
| | 10 | `SCA-L10` | Kỹ thuật tách chữ số và xử lý số nguyên | Khung `until N=0`, bóc `mod 10`, cắt `floor(/10)` | `pya_l10_*` (14 bài) | 12 | 14 |
| | 11 | `SCA-L11` | Ước số, bội số và số nguyên tố | Tối ưu $i \times i \le n$, cờ prime, Euclid UCLN | `pya_l11_*` (14 bài) | 12 | 14 |
| | 12 | `SCA-L12` | Đếm số theo quy luật và số đặc biệt | Đếm $O(1)$ đoạn $[A, B]$, số hoàn hảo, Armstrong | `pya_l12_*` (12 bài) | 12 | 12 |
| **5** | 13 | `SCA-L13` | Danh sách và thao tác cơ bản | List 1-based, `add`, `delete`, `insert`, `item of` | `pya_l16_*` (26 bài) | 12 | 26 |
| | 14 | `SCA-L14` | Thống kê danh sách và sắp xếp | Max/Min/Unique, cài đặt Bubble Sort khối lệnh | `pya_l17_*` (14 bài) | 12 | 14 |
| **6** | 15 | `SCA-L15` | Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự | `letter (i) of ()`, `length of ()`, soi Palindrome | `pya_l13_*` (12 bài) | 12 | 12 |
| | 16 | `SCA-L16` | Duyệt chuỗi, biến đổi ký tự và tách từ | Đếm ký tự, tách từ qua dấu cách vào List, Caesar | `pya_l14/l15_*` (24 bài) | 12 | 24 |

*Tổng cộng toàn khóa:* **16 Bài học**, **190 câu Concept Quiz** và **324 Bài tập thực hành thật 100%**.

---

## 4. Cấu Trúc File & Thư Mục

- `lessons/`: Chứa 16 thư mục bài học chính quy. Mỗi bài học gồm:
  - `LessonXX_Production_Content.md`: Văn bản sách giáo trình chuẩn mực (Lý thuyết sư phạm, mô hình hóa, bẫy lỗi kinh điển, Quiz $\ge 10$ câu).
  - `Bai_Tap.md`: Danh mục bài tập 2 trục ($P0 \to P3$ độ khó $\times$ *Quan sát $\to$ Sắp xếp $\to$ Hoàn thành $\to$ Sáng tạo* nhận thức).
- `problems/`: Chứa 308 thư mục bài tập độc lập theo chuẩn iKHEDU (`De_Bai.md`, `Huong_Dan_Giang_Day.md`, `solution.dsl`, `interaction-check.json`).
- `assets/`: Kho hơn 670 hình ảnh thực tế trích xuất từ các kỳ thi Tin học trẻ, tài liệu vẽ hình Pen và ảnh chụp khối lệnh giải mẫu.
- `reference/`: Các cẩm nang chuẩn hóa cú pháp DSL Scratchblocks và từ điển chuyển đổi thuật toán Python $\to$ Scratch.
- `tools/`: Các kịch bản tự động hóa quét dữ liệu, render ảnh khối lệnh và kiểm thử độc lập.
