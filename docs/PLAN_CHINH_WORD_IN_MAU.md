# Kế hoạch biên soạn & In màu Bộ Giáo Trình iKHEDU C++ (2 Quyển)

## 1. Mục đích & Quyết định Chốt
Thống nhất chuẩn in màu toàn diện và phân chia giáo trình thành **2 Quyển độc lập** chuẩn in ấn để đảm bảo mỗi quyển cân đối (~200 – 210 trang), tối ưu chi phí in ấn, tiết kiệm mực và nâng cao trải nghiệm học tập của học sinh.

---

## 2. Cấu Trúc Phân Chia 2 Quyển

| Quyển | Tên Quyển | Phạm vi Bài học | Khối lượng dự kiến | Đối tượng & Trọng tâm sư phạm |
| :--- | :--- | :--- | :--- | :--- |
| **Quyển 1** | **Kỹ Thuật Lập Trình & Nền Tảng Thuật Toán** | **Chương 01 – Chương 04 (Bài 01 – Bài 12)** (12 bài) | **~210 trang** (gồm 188 bài tập & giải) | Nhập môn lập trình & tư duy tối ưu: Mảng, Two Pointers, Sliding Window, Prefix Sum, Binary Search, Bitwise, Số học, Modulo, BigInt, Đệ quy, Chia để trị, Quay lui. |
| **Quyển 2** | **Cấu Trúc Dữ Liệu & Thuật Toán Nâng Cao** | **Chương 05 – Chương 07 (Bài 13 – Bài 21)** (9 bài) | **~205 trang** (gồm 135 bài tập & giải) | Luyện thi HSG/ICPC: Quy hoạch động 1D/2D/chuỗi, Cấu trúc dữ liệu STL nâng cao, Stack, Monotonic Queue, Đồ thị BFS/DFS, Đồ thị lưới 2D, Cây Segment Tree & Fenwick Tree. |

* **Đầu ra file DOCX**:
  1. `IKHEDU_CPP_Co_Ban_Quyen_1.docx` (Quyển 1: Bài 01 – Bài 12)
  2. `IKHEDU_CPP_Co_Ban_Quyen_2.docx` (Quyển 2: Bài 13 – Bài 21)

---

## 3. Quy Chuẩn Thiết Kế & In Màu (Phương Án A)

### 3.1. Bảng màu chuẩn in ấn (Tiết kiệm mực, không bệt màu)
* **Chữ nội dung**: Đen xám đậm `#1E293B` (Times New Roman / Inter).
* **Tiêu đề (Headings) & Tiêu đề Bảng**:
  * Chữ đen xám `#1E293B` (loại bỏ chữ trắng trên nền xanh navy `#0F2A44` để tránh tốn mực và bệt màu).
  * Nền Header bảng: Xám trắng nhạt `#F1F5F9` viền `#CBD5E1`.
* **Khung ghi chú (Callout / Lưu ý)**:
  * Thống nhất 1 tone màu xanh lam nhạt `#EFF6FF`, viền `#3B82F6`, chữ `#1E3A8A`.
* **Khung Code Block**:
  * Nền `#F8FAFC`, viền `#E2E8F0`, chữ đen `#0F172A`, font `Consolas` / `JetBrains Mono`.

### 3.2. Cỡ chữ & Giãn dòng chuẩn
* **Body Text**: Cỡ chữ **`12.5pt`** (áp dụng đồng loạt cả 5 style: `Normal`, `Body Text`, `First Paragraph`, `List Paragraph`, `Compact`).
* **Code C++**: Giữ **`8.5 – 9pt`**.
* **Giãn dòng**: `1.08 – 1.12` line, `space_after 1.5 – 2pt`.
* **Headings**:
  * H1: `16 – 18pt` (space before 16pt / after 4pt).
  * H2: `13.5 – 15pt` (space before 10pt / after 3pt).
  * H3: `12.5 – 13.5pt` (space before 8pt / after 2pt).

### 3.3. Tối ưu bảng dữ liệu dày (6 – 7 cột)
* Padding ô gọn: `tcMar` top/bottom `40 dxa`, left/right `60 dxa`.
* Body bảng >4 cột giảm về `9pt` để không bị nhảy hàng/vỡ dòng.
* Bật `cantSplit false` cho bảng dài để cho phép ngắt trang tự nhiên.

---

## 4. Phụ Lục & Phần Kèm Theo

### 4.1. Phụ lục A: Nền tảng C++ (Dạng Infographic A4)
* Cả 3 Tập đều có đầy đủ **Phụ lục A: Nền tảng C++**.
* Thay vì dàn trải 5 trang text, chuyển thành **2 trang Infographic A4 màu sáng đẹp**:
  * **Trang 1/2**: Khung tư duy 8 bước, Cấu trúc chương trình C++ tối thiểu, Kiểu dữ liệu & Biến, Nhập xuất I/O & Mẹo thi đấu, Toán tử & Chia nguyên, Cấu trúc rẽ nhánh `if-else`.
  * **Trang 2/2**: Vòng lặp `for/while`, 4 Mẫu tích lũy kinh điển, Cấu trúc hàm & Tham chiếu, Mảng/Vector/String, Quy trình gỡ lỗi 7 bước & Bảng đoán độ phức tạp theo $N$.
* Ảnh nguồn chuẩn A4: `source/level0/assets/appendix_a_page1.png` và `appendix_a_page2.png`.

### 4.2. Phụ lục B: Lời giải C++ Chuẩn Thi Đấu
* Mỗi tập chỉ chứa lời giải cho các bài tập thuộc tập đó:
  * **Tập 1**: Lời giải Bài 01 – Bài 06 (~85 bài giải).
  * **Tập 2**: Lời giải Bài 07 – Bài 12 (~100 bài giải).
  * **Tập 3**: Lời giải Bài 13 – Bài 21 (~138 bài giải).

### 4.3. Mục lục tương tác (TOC)
* Đặt ở cuối mỗi tập sách.
* Có số trang chính xác sau khi render Word và hỗ trợ Hyperlink cho bản điện tử.

---

## 5. Các Việc Cần Thực Hiện Tiếp Theo
1. Cập nhật `ALL_TOPICS` và logic tách 3 tập trong `build_docx.py`.
2. Tích hợp 2 trang ảnh Infographic Phụ lục A vào `build_back_matter_foundation()`.
3. Sửa triệt để lỗi màu chữ header bảng (`FFFFFF` $\to$ `1E293B`) và ép style 12.5pt đồng bộ.
4. Build thử nghiệm 3 tập Word (`Quyen_1`, `Quyen_2`, `Quyen_3`) và đo đếm số trang thực tế.
