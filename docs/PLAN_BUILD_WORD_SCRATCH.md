# Kế Hoạch Chuẩn Hóa & Build File Word In Ấn Khóa Scratch Bảng A (Level 1)

**Mã tài liệu:** `PLAN-SCRATCH-WORD-BUILD-v1.0`  
**Ngày lập:** 21/09/2026  
**Trạng thái:** DRAFT — Chờ phê duyệt (User Approval)  
**Tài liệu tham chiếu chuẩn:**
1. `docs/MASTER_WORD_BUILD_SPECIFICATION.md` (`IKHEDU-DOCX-SPEC-v2.1`)
2. `docs/PLAN_CHINH_WORD_IN_MAU.md` (Quy chuẩn in màu, xử lý bảng & hình ảnh)
3. `courses/cpp-bang-b/c++-level-1-quyen-1.docx` (Tệp Word khuôn chuẩn gốc)
4. `courses/python-bang-a/tools/build_word_python.py` (Script chuẩn hóa mẫu)

---

## 1. Mục Tiêu & Bản Chất Khóa Học

- **Đối tượng học viên:** Học sinh Tiểu học 8–11 tuổi (Lớp 3, 4, 5).
- **Quy mô khóa học:** 6 Chương, 16 Bài học lớn, kho **324 bài tập thực hành thật 100%** (21 bài đồ họa Pen trích từ `CHỦ ĐỀ VẼ HÌNH TRÊN SCRATCH.docx` + 303 bài toán thuật toán Tin học trẻ có đối chiếu tương thích với Python).
- **Mục tiêu đầu ra:** Xuất bản bộ file Word `.docx` chuẩn in màu offset/laser sắc nét, sang trọng, thống nhất 100% với hệ thống giáo trình iKHEDU (C++ và Python), thân thiện tối đa với thị giác trẻ em.

---

## 2. Bảng Ma Trận Định Dạng Chi Tiết (Typography, Font Size, Line Height, Color & Alignment)

Để khắc phục triệt để hiện tượng không đồng đều kích thước, dãn cách chữ bất thường, hoặc lệch màu khi in ấn, toàn bộ các phần tử trong tài liệu Scratch Word bắt buộc tuân thủ đúng bảng thông số kỹ thuật sau:

### 2.1. Ma trận phân cấp Tiêu đề & Văn bản nội dung

| Phần tử (Element / Style) | Font chữ | Cỡ chữ (Font Size) | Dãn dòng (Line Spacing) | Cách đoạn (Spacing Before / After) | Mã màu chuẩn (Hex) | Căn lề (Alignment) | Quy tắc OpenXML bắt buộc |
|---|---|---|---|---|---|---|---|
| **Tiêu đề Lời nói đầu (`P0`)** | Times New Roman | **14.0 pt Bold** | `1.5 line` | Before: `6.0 pt` (`120 dxa`), After: `6.0 pt` | **`#000000` (Đen tuyền in laser)** | **Căn giữa (`Center`)** | Không pageBreakBefore, không numbering |
| **Nội dung Lời nói đầu (`P1`–`P10`)** | Times New Roman | **14.0 pt** | **`1.5 line`** | Before: `0 pt`, After: `6.0 pt` | **`#000000`** | **Căn đều (`Justify`)** | Thoáng đãng, trang trọng theo chuẩn xuất bản |
| **Heading 1 — Tên Chương** | Times New Roman | **18.0 pt Bold** | `1.15 line` | Before: `18.0 pt` (`360 dxa`), After: `8.0 pt` | **`#000000`** | **Căn giữa (`Center`)** | `pageBreakBefore = True` (mọi Chương bắt đầu trang mới) |
| **Heading 1 — Tên Bài học** | Times New Roman | **15.5 pt Bold** | `1.15 line` | Before: `14.0 pt` (`280 dxa`), After: `4.0 pt` | **`#000000`** | **Căn trái (`Left`)** | Nếu là bài đầu tiên của Chương thì không ngắt trang; các bài sau ngắt trang |
| **Heading 2 — Mục Lý thuyết lớn** | Times New Roman | **14.0 pt Bold** | `1.15 line` | Before: `11.0 pt` (`220 dxa`), After: `3.0 pt` | **`#000000`** | **Căn trái (`Left`)** | `keep_with_next = True`, cấm căn Justify |
| **Heading 2 — "Bài tập thực hành"** | Times New Roman | **14.0 pt Bold** | `1.15 line` | Before: `12.0 pt` (`240 dxa`), After: `4.0 pt` | **`#FF0000` (Đỏ cờ tươi)** | **Căn trái (`Left`)** | Điểm nhấn thị giác chuyển phần bài tập, `keep_with_next = True` |
| **Heading 3 — Tên Bài tập (`Bài XX [CODE]: Tên`)** | Times New Roman | **13.0 pt Bold** | `1.15 line` | Before: `8.0 pt` (`160 dxa`), After: `2.0 pt` | **`#000000`** | **Căn trái (`Left`)** | `keep_with_next = True`, cấm căn Justify |
| **Heading 4 — Tiêu đề mục nhỏ** | Times New Roman | **12.5 pt Bold** | `1.15 line` | Before: `4.0 pt`, After: `2.0 pt` | **`#000000`** | **Căn trái (`Left`)** | Chỉ dùng khi chia mục con trong lý thuyết |
| **Văn bản nội dung (Body / Normal / First Para)** | Times New Roman | **12.5 pt** | **`1.15 line`** | Before: `0 pt`, After: `4.0 pt` (`80 dxa`) | **`#000000`** | **Căn đều (`Justify`) 100%** | Vuông vức hai mép trang in, cấm thụt lề dạt chữ |
| **Mục gạch đầu dòng / Đoạn ngắn (`Compact`)** | Times New Roman | **12.0 pt** | `1.15 line` | Before: `0 pt`, After: `2.0 pt` | **`#000000`** | **Căn đều (`Justify`)** | Dùng trong danh sách và mô tả tham số |
| **Khung Ghi chú / Callout (`Block Text`)** | Times New Roman | **12.0 pt** | `1.15 line` | Before: `4.0 pt`, After: `4.0 pt` | `#1E3A8A` (Chữ xanh đậm) | **Căn đều (`Justify`)** | Nền xanh pastel `#EFF6FF`, viền trái dày `#3B82F6` |
| **Khung Kịch bản Khối lệnh / Code (`Source Code`)** | Consolas | **9.0 pt** | **`1.05 line`** (`line=252`) | Before: `3.0 pt`, After: `3.0 pt` | **`#000000` (Đen sắc nét)** | **Căn trái (`Left`) 100%** | Nền `#F8FAFC`, viền `#CBD5E1`/`#E2E8F0`, thụt lề trái `180 dxa`. CẤM Justify |
| **Header Text (Đầu trang)** | Times New Roman | **9.5 pt Italic** | Single | Bottom border mờ | `#000000` | Trái: `iKHEDU` — Phải: Tên tập sách | Xuất hiện ở header trang chẵn/lẻ |
| **Footer Text (Số trang)** | Times New Roman | **10.0 pt** | Single | Before: `0 pt`, After: `0 pt` | `#000000` | **Căn giữa (`Center`)** | Trường tự động `— PAGE —` (`<w:fldSimple w:instr="PAGE"/>`) |

---

## 3. Quy Chuẩn Bảng Biểu (Tables) — Triệt Tiêu 3 Lỗi Kinh Điển

Tài liệu Scratch có nhiều bảng mô phỏng tọa độ, bảng khối lệnh tương đương, và bảng Sample IO. Bắt buộc xử lý đồng bộ:

### 3.1. Bảng Sample Input / Output của Bài tập thực hành
- **Căn giữa bảng**: Thẻ thuộc tính `<w:jc w:val="center"/>`.
- **Độ rộng chuẩn mực (Compact Table Width)**:
  - Tổng chiều rộng bảng cố định: `w=6800 dxa` (~$12.0\text{ cm}$).
  - Cột `Đầu vào (Input)`: `w=3400 dxa` (~$6.0\text{ cm}$).
  - Cột `Đầu ra (Output)`: `w=3400 dxa` (~$6.0\text{ cm}$).
  - Viền bảng mảnh màu xám `#CBD5E1` và `#E2E8F0`.
- **Hàng tiêu đề (Hàng 0)**:
  - Nền xám nhạt `#F1F5F9`, chữ **Consolas 11.0 pt Bold**, màu **`#000000`**, **căn giữa ô (`Center`)**.
- **Hàng dữ liệu Testcase (Hàng 1+) — Thuật toán Căn Lề Động (Dynamic Left Indent)**:
  - Font chữ: **Consolas 11.0 pt Regular**, màu **`#000000`**.
  - Căn lề văn bản bên trong ô: Luôn giữ **căn trái (`Left`)** để các cột số thẳng hàng dọc.
  - Độ thụt lề trái tự động tính theo độ dài chuỗi dài nhất (`max_len`):
    $$\text{left\_indent}(\text{max\_len}) = \max\left(10.0\text{ pt},\, 72.0\text{ pt} - \max(0, \text{max\_len} - 4) \times 3.25\text{ pt}\right)$$
    *(Đảm bảo khi output ngắn như số `4` hay `10` thì khối text được đẩy vào đúng tâm giữa cột 6 cm, không bị lệch sát mép trái)*.
  - **Multiline Testcase**: Nếu testcase gồm nhiều dòng, tách thành từng thẻ `<w:p>` riêng biệt trong ô bảng, cùng thừa hưởng mức `left_indent` để các số thẳng cột chằn chặn.

### 3.2. Bảng Mô phỏng & Bảng Tra cứu Lý thuyết
- **Font chữ & Kích cỡ**:
  - Tiêu đề cột: Times New Roman **12.0 pt Bold**, màu **`#000000`**, căn giữa ô (`Center`), nền `#F1F5F9`.
  - Nội dung các hàng: Times New Roman **12.0 pt Regular**, màu **`#000000`**, căn đều (`Justify`) hoặc căn giữa với cột số ngắn.
  - **Đồng bộ công thức toán (`m:oMath`)**: Quét 100% các node `m:rPr`, ép cứng `w:sz val="24"` và `w:szCs val="24"` (chuẩn **12.0 pt**) để chữ số trong công thức to đều chằn chặn với văn bản thường, không bị co nhỏ thành 9.5 pt.
- **Xử lý ngắt trang bảng**:
  - **Xóa sạch thẻ `<w:tblHeader/>`** trên 100% các bảng (chống duplicate tiêu đề bảng khi ngắt trang).
  - Thêm thẻ `<w:cantSplit/>` cho mọi hàng `<w:trPr>` để không xé đôi dòng văn bản.
  - Độ rộng cột tự động giãn theo nội dung (Autofit) để tiết kiệm diện tích trang giấy.

---

## 4. Quy Chuẩn Xử Lý Hình Ảnh Khối Lệnh & Sơ Đồ Đồ Họa (Images & Blocks)

Khóa học Scratch có đặc thù là sử dụng **rất nhiều hình ảnh khối lệnh trực quan (hơn 670 ảnh)**:

1. **Giới hạn kích thước ảnh (Scale & Bounds Protection)**:
   - Toàn bộ ảnh chèn vào văn bản (sơ đồ sân khấu, khối lệnh bài học, ảnh bài giải) bắt buộc được scale tự động với giới hạn chiều rộng tối đa:
     $$\text{Width}_{\max} = 15.0\text{ cm} \quad (5.400.000\text{ EMU})$$
     $$\text{Height}_{\max} = 5.000.000\text{ EMU}$$
   - Giữ nguyên tỉ lệ khung hình (Aspect Ratio), căn giữa trang in (`WD_ALIGN_PARAGRAPH.CENTER`), khoảng cách trên dưới `4.0 pt`.
2. **Hình ảnh trong phần Lý thuyết (`LessonXX_Production_Content.md`)**:
   - Tự động map các đường dẫn tương đối `../../assets/rendered_blocks/` và `../../assets/pen_drawings/` về thư mục ảnh tuyệt đối.
3. **Hình ảnh Lời giải trong Phụ lục B**:
   - Toàn bộ 324 bài tập đều đã có ảnh kết xuất khối lệnh Scratch 3.0 Tiếng Việt độ phân giải cao `solution_blocks_vi.png`.
   - Trong Phụ lục B, dưới mỗi tiêu đề bài toán sẽ chèn trực tiếp ảnh `solution_blocks_vi.png` (kèm kịch bản chữ tóm tắt), giúp học sinh và phụ huynh nhìn trực quan cấu trúc khối lệnh mà không cần mở máy tính.

---

## 5. Quy Chuẩn Khổ Giấy, Watermark & Hệ Thống Mục Lục (TOC)

1. **Khổ giấy & Căn lề chuẩn in**:
   - Khổ A4 đứng ($210 \times 297\text{ mm}$).
   - Lề trên (Top): `36.0 pt` ($1.27\text{ cm}$).
   - Lề dưới (Bottom): `36.0 pt` ($1.27\text{ cm}$).
   - Lề trái (Left / Gáy sách dập kim): **`64.35 pt`** ($2.27\text{ cm}$).
   - Lề phải (Right): `36.0 pt` ($1.27\text{ cm}$).
2. **Watermark Logo iKHEDU 100% các trang**:
   - Đảm bảo cấu hình đầy đủ cả 3 Header (`even`, `default`, `first`) trong `sectPr`.
   - Nhúng khối VML Vector Watermark `alt="logo_in"` trỏ tới `media/image13.jpeg`, căn giữa trang in, độ mờ chuẩn in.
3. **Hệ thống Mục lục tương tác (Table of Contents — TOC) chuẩn in ấn**:
   - **Vị trí đặt**: Đặt tại **cuối mỗi quyển sách** (sau Phụ lục B), luôn bắt đầu ở đầu một trang mới độc lập (`pageBreakBefore = True`).
   - **Tiêu đề Mục lục**: 
     - Nội dung: `MỤC LỤC`
     - Cỡ chữ: **`18.0 pt Bold`** (`sz val="36"`), màu đen tuyền **`#000000`**.
     - Căn lề: Căn giữa (**`Center`**).
     - Khoảng cách: Cách dưới **`140 dxa`** ($7.0\text{ pt}$), cách trên `360 dxa` ($18\text{ pt}$) $\to$ *Tạo vẻ nổi bật, trang trọng ở đầu trang*.
   - **Cơ chế liên kết Hyperlink & Bookmarks**: Mọi đề mục (Chương, Bài học, Phụ lục, Lời nói đầu) đều được gắn Bookmark tự động dạng `bm_sec_N` trong OpenXML, người đọc bấm vào tên bài trong Mục lục sẽ nhảy ngay tới trang nội dung tương ứng.
   - **Đường chấm dính kết nối (Leader Dots Tab Stop)**: Cấu hình Tab Stop căn phải có đường chấm dính nối thẳng từ tên bài sang số trang:
     ```xml
     <w:tabs>
         <w:tab w:val="right" w:leader="dot" w:pos="9899"/>
     </w:tabs>
     ```
     *(Vị trí tab `9899 dxa` khớp chuẩn xác với mép lề phải trang giấy A4 trừ đi margins)*.
   - **Định dạng phân cấp chi tiết trong Mục lục**:
     - **Chương / Lời nói đầu / Phụ lục**:
       - Cỡ chữ: **`14.0 pt Bold`** (`sz val="28"`), màu đen tuyền **`#000000`**.
       - Căn lề: Căn trái sát lề.
       - Khoảng cách: Cách trên **`160 dxa`** ($8.0\text{ pt}$), cách dưới **`40 dxa`** ($2.0\text{ pt}$).
       - *Hiệu quả*: Rõ ràng, phân tách từng chương mạch lạc.
     - **Tên Bài học**:
       - Cỡ chữ: **`13.0 pt Regular`** (`sz val="26"`), màu đen tuyền **`#000000`**.
       - Thụt lề trái cấp con: **`left_indent = 320 dxa`** ($16.0\text{ pt}$).
       - Ký tự đầu dòng: `• ` (bullet tròn).
       - Khoảng cách: Cách dòng **`24 dxa`** ($1.2\text{ pt}$), dãn dòng đơn.
       - *Hiệu quả*: Cỡ chữ to rõ, rất vừa mắt các em học sinh Tiểu học, số trang thẳng hàng bằng tab chấm `....` nối sang mép phải.
     - **Số trang hiển thị**: Căn thẳng hàng dọc sát mép phải nhờ tab stop `9899 dxa`, màu đen tuyền **`#000000`**, cùng font Times New Roman và cỡ chữ tương ứng với từng cấp đề mục (`14pt Bold` cho Chương, `13pt Regular` cho Bài học).

---

## 6. Phương Án Phân Chia Tập Sách (2 Quyển Cân Đối)

| Quyển | Tên giáo trình đề xuất | Phạm vi Chương / Bài | Số bài tập thực hành | Số trang dự kiến | Trọng tâm học thuật & Sư phạm |
|---|---|---|:---:|:---:|---|
| **Quyển 1** | **Giáo trình Scratch Bảng A — Quyển 1: Bút Vẽ Đồ Họa & Nền Tảng Khối Lệnh** | **Chương 1 – 3** (Bài 01 đến Bài 08) | **194 bài** | ~210 trang | Làm chủ Pen, vẽ đa giác, hoa văn nghệ thuật, biến số, biểu thức, phép chia nguyên/dư và 2 cấu trúc điều khiển rẽ nhánh & vòng lặp. |
| **Quyển 2** | **Giáo trình Scratch Bảng A — Quyển 2: Thuật Toán Số Học, Danh Sách & Chuỗi Ký Tự** | **Chương 4 – 6** (Bài 09 đến Bài 16) | **130 bài** | ~185 trang | Thuật toán Tin học trẻ: Tách chữ số, ước/nguyên tố, số đặc biệt, danh sách 1-based, sắp xếp và xử lý chuỗi ký tự. |

*Tên file Word đầu ra:*
- `courses/scratch-bang-a/scratch-level-1-quyen-1.docx`
- `courses/scratch-bang-a/scratch-level-1-quyen-2.docx`

---

## 7. Các Bước Triển Khai Tiếp Theo (Sau Khi Phê Duyệt Plan)

1. **Bước 1 — Soạn thảo tư liệu chuẩn**:
   - Viết `reference/Loi_Noi_Dau_Scratch_Quyen1.md` và `Loi_Noi_Dau_Scratch_Quyen2.md` (giọng điệu truyền cảm hứng cho học sinh Tiểu học theo đúng chuẩn mục P0–P10).
   - Viết `reference/Phu_Luc_A_Scratch.md` (Cẩm nang bảng khối lệnh Tiếng Việt, công thức góc quay đa giác, hệ trục tọa độ sân khấu).
   - Tạo file `courses/scratch-bang-a/tools/word_build_manifest.json` ánh xạ đầy đủ 16 bài học và 324 bài tập.
2. **Bước 2 — Xây dựng công cụ chuyển đổi & xử lý hậu kỳ**:
   - Viết script `courses/scratch-bang-a/tools/build_word_scratch.py` kế thừa engine xử lý XML/OXML từ `build_word_python.py` và template gốc `c++-level-1-quyen-1.docx`.
   - Tích hợp bộ lọc Markdown loại bỏ Quiz khỏi bản in (chỉ in phần lý thuyết tinh gọn + bài tập thực hành).
3. **Bước 3 — Build DOCX & Kiểm định (QA Audit)**:
   - Chạy build cả 2 quyển.
   - Chạy script audit kiểm tra Watermark 100% trang, 0 lỗi `tblHeader`, cỡ chữ Math 12pt, bảng Sample căn giữa và Dynamic Left Indent.
