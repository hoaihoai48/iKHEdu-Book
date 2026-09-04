# BÁO CÁO PHÂN TÍCH & ĐỀ XUẤT KHUÔN MẪU TÁI THIẾT KẾ (REBUILD)
## BỘ SÁCH GIÁO TRÌNH C++ LEVEL 2 (QUYỂN 1 & QUYỂN 2)
*(Dựa trên khuôn mẫu chuẩn in ấn thực tế của `courses/cpp-bang-b/c++-level-1.docx` và các yêu cầu chốt của dự án)*

---

### 1. TỔNG QUAN PHÂN TÍCH KHUÔN MẪU THỰC TẾ (`c++-level-1.docx`)

Qua khảo sát sâu từng tầng cấu trúc OpenXML của file khuôn mẫu `c++-level-1.docx`, các đặc điểm kỹ thuật cốt lõi được làm sáng tỏ:

#### 1.1. BỎ TRANG BÌA (Cover Page Elimination)
* **Khuôn mẫu `c++-level-1.docx`**: **HOÀN TOÀN KHÔNG CÓ TRANG BÌA**.
  * Trang đầu tiên mở sách ra là bắt đầu ngay bằng **`P0 [Heading 1]: LỜI NÓI ĐẦU`** (có `<w:pageBreakBefore/>`), sau đó đi thẳng vào nội dung Lời nói đầu và `CHƯƠNG 01`.
  * Không có các đoạn văn tiêu đề sách, subtitle, tác giả, đường kẻ phân cách `────────` ở đầu file.
* **Hiện trạng Level 2 (`IKHEDU_CPP_Nang_Cao_Quyen_1/Q2.docx`)**:
  * Đang có 7 đoạn văn trang bìa ở đầu (`P0: Title`, `P1: Subtitle`, `P2: Author`, `P3: ─────`, `P4: Tagline`, `P5: TRUNG TÂM TIN HỌC iKH`, `P6: Phiên bản xuất bản 2026`).
  * **Giải pháp khi Rebuild**:
    * Trong hàm tạo Markdown: Bỏ khối YAML Metadata (`title`, `subtitle`, `author`) hoặc cấu hình Pandoc/Post-process để **xóa sạch toàn bộ 7 đoạn văn trang bìa**, bắt đầu trực tiếp từ **`Lời nói đầu`** đúng y hệt như khuôn mẫu `c++-level-1.docx`.

#### 1.2. HÌNH CHÌM / LOGO NỀN (Watermark / Background Logo)
* **Khuôn mẫu `c++-level-1.docx`**:
  * Được nhúng một hình chìm logo vector dạng VML Watermark (`<v:shape type="#_x0000_t75" id="WordPictureWatermark1286990223" alt="logo_in">`) đặt trong header của tài liệu (`word/header1.xml`, `header2.xml`, `header3.xml`).
  * File ảnh logo: `media/image13.jpeg` (kích thước $572 \times 572\text{ px}$, logo trung tâm iKH).
  * Vị trí & hiệu ứng hiển thị:
    * Căn chính giữa trang (`mso-position-horizontal: center; mso-position-vertical: center`).
    * Chiều rộng & chiều cao: `width: 286pt; height: 286pt` (~ $10 \times 10\text{ cm}$).
    * Lớp hiển thị: Nằm chìm hoàn toàn dưới văn bản (`z-index: -251650048`).
    * Độ sáng / độ trong suốt: `gain="19661f" blacklevel="22938f"` (làm mờ nhạt chuẩn watermark in màu/in offset, không che khuất chữ nội dung).
* **Hiện trạng Level 2**:
  * Hiện tại cả 2 quyển Level 2 **hoàn toàn chưa có logo nền / watermark**.
  * **Giải pháp khi Rebuild**:
    * Lưu trữ sẵn asset `logo_in.jpeg` trong codebase (lấy từ khuôn mẫu `image13.jpeg`).
    * Trong `postprocess_docx()` của Level 2: Tự động nhúng `logo_in.jpeg` vào Header phần Section, liên kết qua `rId` và chèn khối XML `<w:pict><v:shape id="WordPictureWatermark..." ...>` để **100% các trang sách của Level 2 đều có logo nền mờ iKH sang trọng, chống sao chép và đồng bộ thương hiệu**.

---

### 2. TỔNG HỢP CÁC HẠNG MỤC CẦN ĐIỀU CHỈNH KHI REBUILD LEVEL 2

| STT | Hạng mục | Khuôn mẫu `c++-level-1.docx` | Hiện trạng Level 2 | Giải pháp Rebuild |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Trang bìa** | **Không có trang bìa**, mở đầu ngay bằng `Lời nói đầu` | Đang có 7 đoạn văn bìa thô ở đầu sách | **Xóa bỏ hoàn toàn trang bìa**, bắt đầu trực tiếp từ `Lời nói đầu` |
| **2** | **Logo nền (Watermark)** | **Có logo nền iKH** mờ (`width: 286pt`, `z-index` âm, căn giữa trang) | Chưa có | **Nhúng tự động VML Watermark logo iKH** vào Header toàn bộ các trang |
| **3** | **Căn lề văn bản** | **`JUSTIFY`** (Căn đều 2 bên 100% cho toàn bộ Body Text, First Paragraph, Normal, Compact, Block Text) | Căn Left (`None`), mép phải trang chưa thẳng | **Căn đều `Justify` 100%** toàn bộ các đoạn văn nội dung |
| **4** | **Bảng Sample IO** | **Bảng 2 cột** `Đầu vào (Input)` & `Đầu ra (Output)`, độ rộng `3400 dxa`/cột, căn giữa trang, thụt lề testcase động | Đang là text thô `### Input` + code block, chiếm nhiều dòng dọc | **Chuyển toàn bộ Sample của 346 bài thành Bảng 2 cột**, căn giữa trang và thụt lề testcase |
| **5** | **Tiêu đề Bài tập** | Tiêu đề mục "Bài tập thực hành" mang màu **Đỏ `#FF0000` (Bold)** | Mang màu xám `#1E293B` | **Tô đỏ `#FF0000`** toàn bộ tiêu đề mục bài tập |
| **6** | **Font Math trong bảng** | Ép cứng font size **12pt (`w:sz val="24"`)** cho toàn bộ `m:oMath` trong bảng | Math mang font size `9.5pt` / `10.5pt` khấp khểnh | **Ép cứng `12pt`** cho toàn bộ các công thức toán trong bảng |
| **7** | **Lặp tiêu đề bảng** | Gỡ bỏ `<w:tblHeader/>`, bật `<w:cantSplit/>` trên từng dòng | Còn nguyên `tblHeader` trên 54 bảng (lặp 2 lần khi ngắt trang) | **Xóa sạch `tblHeader` và bật `cantSplit`** để chống lặp header và chống xé chữ |
| **8** | **Khung lề trang in** | **Top = 1.27 cm, Bottom = 1.27 cm, Right = 1.27 cm, Left = 2.27 cm** (trừ gáy sách) | Top = 2.0 cm, Bottom = 2.0 cm, Right = 2.0 cm, Left = 2.2 cm | **Đồng bộ lề trang Top/Bottom/Right = 1.27 cm, Left = 2.27 cm** để tối ưu diện tích in |
| **9** | **Đường kẻ Header** | Header có dòng text `Trung tâm...` + đường kẻ mảnh ngăn cách phía dưới | Đang dùng border paragraph | **Đồng bộ Header và đường kẻ** chuẩn theo Level 1 |

---

### 3. KẾ HOẠCH HÀNH ĐỘNG TRIỂN KHAI (Dự kiến sau khi User duyệt)

1. **Chuẩn bị Asset**:
   * Trích xuất và đặt file `logo_watermark.jpeg` vào thư mục `courses/cpp-bang-b-level2/assets/` làm asset chuẩn.
2. **Cập nhật script `courses/cpp-bang-b-level2/build_docx.py`**:
   * **Bỏ bìa**: Xóa logic sinh trang bìa trong Markdown và hàm `postprocess_docx()`.
   * **Thêm logo nền**: Viết hàm chèn `Watermark` OpenXML chuẩn Microsoft Word vào phần Header của tài liệu.
   * **Bảng Sample IO**: Nâng cấp hàm `format_problem_statement()` tự động tạo bảng 2 cột cho 346 bài tập.
   * **Typography & Table Fixes**: Áp dụng Justify, màu đỏ `#FF0000`, ép font size 12pt cho Math trong bảng, xóa `tblHeader` và chỉnh lề `1.27 cm / 2.27 cm`.
3. **Thực thi Rebuild & Kiểm định**:
   * Build lại `IKHEDU_CPP_Nang_Cao_Quyen_1.docx` và `IKHEDU_CPP_Nang_Cao_Quyen_2.docx`.
   * Kiểm tra tự động bằng script Python để xác nhận 100% các tiêu chí: Không còn bìa, có Watermark logo iKH, văn bản Justify, bảng Sample IO 2 cột căn giữa.

---
*Bản báo cáo này đã cập nhật đầy đủ 2 điểm mấu chốt: **Bỏ bìa** và **Thêm logo nền (Watermark)** cùng toàn bộ các thông số kỹ thuật khác để bạn xem xét.*
