# QUY CHUẨN ĐẶC TẢ MASTER REBUILD & BUILD GIÁO TRÌNH WORD iKHEDU
*(Universal Master Specification & Build Pipeline for iKHEDU Coursebooks)*

**Mã tài liệu:** `IKHEDU-DOCX-SPEC-v2.1`  
**Cơ sở thẩm quyền & Nguồn tham chiếu:**
1. [docs/PLAN_CHINH_WORD_IN_MAU.md](file:///Users/vu/Developer/ikhEdu_lessons/docs/PLAN_CHINH_WORD_IN_MAU.md) *(Quy chuẩn thiết kế in màu & xử lý bảng)*
2. [docs/MASTER_MODULE_01_DESIGN.md](file:///Users/vu/Developer/ikhEdu_lessons/docs/MASTER_MODULE_01_DESIGN.md) *(Kiến trúc phân cấp 5 tầng & Problem Identity)*
3. [courses/cpp-bang-b/c++-level-1-quyen-1.docx](file:///Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/c++-level-1-quyen-1.docx) *(Tệp Word mẫu đối chiếu chuẩn)*

**Phạm vi áp dụng:** Áp dụng bắt buộc cho toàn bộ các tập giáo trình Word hiện tại và tương lai của hệ thống đào tạo iKHEDU (Quyển 1, Quyển 2, Level 2, Python, v.v.).

---

## 1. Kiến Trúc Khổ Giấy, Căn Lề & Ngắt Trang (Page Setup & Margins)

* **Loại bỏ hoàn toàn trang bìa**: Tài liệu bắt đầu trực tiếp từ **LỜI NÓI ĐẦU** tại trang 1.
* **Kích thước lề trang in chuẩn (Margins)**:
  * **Lề trên (Top)**: `36.0pt` ($1.27\text{ cm}$)
  * **Lề dưới (Bottom)**: `36.0pt` ($1.27\text{ cm}$)
  * **Lề trái (Left / Gáy sách)**: `64.35pt` ($2.27\text{ cm}$)
  * **Lề phải (Right)**: `36.0pt` ($1.27\text{ cm}$)
* **Quy tắc ngắt trang (Page Break Rule)**:
  * Tiêu đề Chương đầu tiên (`Heading 1`) liền kề sau Lời nói đầu bắt buộc mang thuộc tính **`pageBreakBefore = True`** (`<w:pageBreakBefore/>`) để nội dung học thuật luôn bắt đầu ở đầu một trang mới độc lập.
  * Mọi Chương sách tiếp theo đều phải ngắt trang ở đầu chương.

---

## 2. Quy Chuẩn Đầu Trang (Header), Chân Trang (Footer) & Watermark Logo trên 100% Trang In

### 2.1. Cấu hình Watermark Logo iKHEDU (Mọi Trang Đều Có Logo)
* **Nguyên tắc kỹ thuật OpenXML**:
  * Khi thẻ `<w:titlePg/>` (`different_first_page_header_footer`) được kích hoạt, OpenXML yêu cầu định nghĩa riêng biệt cho trang đầu tiên. Để **100% các trang từ trang 1 đến trang cuối cùng đều có Watermark Logo**, tài liệu Word bắt buộc cấu hình đầy đủ cả 3 Header Reference trong `sectPr`:
    1. `w:type="even"` $\to$ trỏ tới header trang chẵn (chứa Watermark).
    2. `w:type="default"` $\to$ trỏ tới header mặc định / trang lẻ (chứa Watermark + Header Text).
    3. `w:type="first"` $\to$ trỏ tới header trang đầu tiên (chứa Watermark).
* **Cấu trúc VML Vector Shape Watermark**:
  ```xml
  <w:pict>
    <v:shape id="WordPictureWatermark" type="#_x0000_t75" 
             style="position:absolute;margin-left:0;margin-top:0;width:286pt;height:286pt;z-index:-251656192;mso-position-horizontal:center;mso-position-horizontal-relative:margin;mso-position-vertical:center;mso-position-vertical-relative:margin" 
             o:allowincell="f">
      <v:imagedata r:id="rId1" o:title="logo_in" gain="19661f" blacklevel="22938f"/>
      <w10:wrap anchorx="margin" anchory="margin"/>
    </v:shape>
  </w:pict>
  ```
  * Mối quan hệ `.rels` của cả 3 header trỏ tới tệp ảnh mờ: `media/image13.jpeg`.

### 2.2. Header Text (Tiêu đề đầu trang)
* Dòng chữ mảnh `9.5pt`, in nghiêng mờ kèm đường gạch ngang ngăn cách:
  * Bên trái: Tên Trung tâm / Học liệu (`iKHEDU`).
  * Bên phải: Tên Tập sách / Tên Giáo trình tương ứng.

### 2.3. Chân Trang (Footer) & Số Trang Tự Động
* Căn giữa trang (**`Center`**).
* Sử dụng trường số trang tự động `PAGE`:
  ```xml
  <w:p>
    <w:pPr><w:jc w:val="center"/></w:pPr>
    <w:r><w:t>—  </w:t></w:r>
    <w:fldSimple w:instr="PAGE"/>
    <w:r><w:t>  —</w:t></w:r>
  </w:p>
  ```

---

## 3. Quy Chuẩn Phần "Lời Nói Đầu" (Preface Format)

* **Tiêu đề (`P0`)**:
  * Nội dung: `LỜI NÓI ĐẦU`
  * Kiểu dáng: `Heading 1`
  * Căn lề: Căn giữa (**`Center`**)
  * Font & Kích cỡ: `Times New Roman 14.0pt Bold`
  * Màu sắc: `#1E293B`
  * Khoảng cách trên: `space_before = 120` ($6\text{pt}$)
* **Các đoạn văn nội dung (`P1` – `P10`)**:
  * Cỡ chữ chuẩn: **`14.0pt`**
  * Dãn dòng chuẩn: **`1.5 line spacing`** (trang trọng, thoáng đãng theo chuẩn mở đầu sách xuất bản)
  * Căn lề: Căn đều 2 bên (**`Justify`**) 100%
  * Các đề mục gạch đầu dòng cấu trúc bài học: In đậm (`bold=True`), cỡ `14pt`:
    * `Khái niệm & Bản chất toán học:`
    * `Mô hình bài toán kinh điển:`
    * `Mẫu cài đặt chuẩn thi đấu:`
    * `Hệ thống bài tập thực hành:`
    * `Lời giải tham khảo chi tiết:`

---

## 4. Bảng Màu & Hệ Thống Typography Chuẩn In Ấn

### 4.1. Bảng màu in ấn tiết kiệm mực & tương phản cao
* **Chữ nội dung**: Đen tuyền **`#000000`** (Times New Roman / Inter) — bắt buộc 100% để in ấn laser/offset rõ nét, không bị nhạt/xám nét khi in màu.
* **Tiêu đề mục "Bài tập thực hành"**:
  * Bắt buộc đổi sang **Màu đỏ chuẩn `#FF0000` (Bold, 14pt, Heading 2)** ở toàn bộ các bài học trong giáo trình.
* **Tiêu đề các cấp (Headings)**:
  * `Heading 1` (Chương): `18pt Bold`, căn giữa `Center`, màu đen tuyền `#000000`.
  * `Heading 1` (Bài học): `15.5pt Bold`, căn trái `Left`, màu đen tuyền `#000000`.
  * `Heading 2` (Mục lý thuyết lớn): `14pt Bold`, căn trái `Left`, màu đen tuyền `#000000`.
  * `Heading 2` (Mục Bài tập thực hành): `14pt Bold`, căn trái `Left`, màu đỏ `#FF0000`.
  * `Heading 3` (Tên bài toán / Dạng bài): `13pt Bold`, căn trái `Left`, màu đen tuyền `#000000`.
  * `Heading 4`: Đã loại bỏ hoàn toàn (`Heading 4 = 0`).
  * *Lưu ý tuyệt đối:* **Cấm áp dụng căn Justify cho Headings** để tránh bị dãn khoảng cách chữ bất thường. Cấm dùng màu xanh đen `#1E293B`, `#0F2A44`, `#1A4A6B`.

### 4.2. Thân bài & Khung chuyên biệt (Quy Chuẩn Chống Bể Khung & Tràn Chữ)
* **Văn bản nội dung (Body Text, First Paragraph, Compact, Normal)**:
  * Cỡ chữ chuẩn: **`12.5pt`**.
  * Dãn dòng chuẩn: **`line-height = 1.15`** (khoảng cách chuẩn sách giáo trình in ấn).
  * Căn lề: Căn đều 2 bên (**`Justify`**) 100%.
* **Khung ghi chú / Callout (`Block Text`)**:
  * Cỡ chữ: `12pt`, dãn dòng `1.15`, căn đều `Justify`. Nền xanh lam nhạt `#EFF6FF`, viền xanh `#3B82F6`, chữ `#1E3A8A`.
* **Khung mã nguồn (`Source Code`) — Quy Chuẩn Cốt Lõi**:
  * **Font chữ & Cỡ chữ**: Font `Consolas` chuẩn **`9.0pt`** (tuyệt đối không để cỡ chữ lớn hơn gây tràn khối code), dãn dòng `1.05` (`line=252`).
  * **Màu sắc & Viền nền**: Nền xám nhạt `#F8FAFC`, viền trái dày `#CBD5E1` (`w:sz="8"`), viền trên/dưới/phải `#E2E8F0` (`w:sz="4"`).
  * **Khoảng thụt khối (Indentation)**: `w:ind w:left="180" w:right="120"`.
  * **Căn lề bắt buộc (Alignment Rule)**:
    * **100% CĂN TRÁI (`Left-aligned`)**: Bắt buộc `<w:jc w:val="left"/>` trên mọi đoạn code.
    * **TUYỆT ĐỐI KHÔNG ÁP DỤNG JUSTIFY**: Không bao giờ gán Justify vào style `Normal` (vì `Source Code` kế thừa từ `Normal`), tránh tình trạng chữ cái bị Word kéo dãn cách xa nhau (`#   i   n   c   l   u   d   e`).
  * **Không để numbering/list dính vào code**: Loại bỏ các thẻ `<w:numPr>` rác nếu có.

---

## 5. Quy Chuẩn Toàn Diện Cho Bảng Dữ Liệu (Tables)

Mọi bảng biểu trong tài liệu bắt buộc phải giải quyết triệt để các vấn đề OpenXML sau:

### 5.1. Vấn đề 1: Triệt tiêu hiện tượng Duplicate Title khi ngắt trang
* **Xóa bỏ hoàn toàn thẻ `<w:tblHeader/>`** trên tất cả các bảng. Khi bảng dài vượt trang, các hàng dữ liệu tiếp nối tự nhiên mà không in lặp lại hàng tiêu đề.
* **Chống vỡ hàng**: Bổ sung thẻ `<w:cantSplit/>` cho từng hàng `<w:trPr>` trong bảng để bảo đảm không bị xé đôi chữ ngang trang.

### 5.2. Vấn đề 2: Đồng bộ Font Size công thức toán & bảng tra cứu Phụ lục
* **Công thức Word Math (`m:oMath`)**: Ép cứng kích thước `<w:sz w:val="24"/>` và `<w:szCs w:val="24"/>` (chuẩn **12.0pt**) cho toàn bộ `<w:rPr>` bên trong `m:r`. Chữ số và ký hiệu toán học to đều chằn chặn 12pt, không bị co nhỏ thành 9.5pt.
* **Bảng tra cứu lý thuyết & Phụ lục A**: Toàn bộ chữ trong các ô bảng tra cứu phải có cỡ chữ chuẩn **`12.0pt`** (font size của bảng tra cứu cú pháp trong Quyển 1 chuẩn là 12pt, không để 10pt hay 9.5pt). Hàng tiêu đề căn giữa (`Center`), các hàng nội dung căn đều (`Justify`).

### 5.3. Vấn đề 3: Bảng Sample Input / Output căn giữa & Căn lề ĐỘNG (Dynamic Left Indent)
Bảng Sample IO trong Quyển 1 chuẩn vận hành theo thuật toán căn lề động như sau:
* **Căn giữa toàn bộ bảng**: Thẻ thuộc tính bảng mang `<w:jc w:val="center"/>`.
* **Thu gọn chiều rộng**: Tổng chiều rộng bảng đặt cứng `<w:tblW w:w="6800" w:type="dxa"/>` (~$12.0\text{ cm}$), mỗi cột đặt `<w:tcW w:w="3400" w:type="dxa"/>` (~$6.0\text{ cm}$).
* **Tiêu đề cột (Hàng 0)**:
  * Ô `Đầu vào (Input)` và `Đầu ra (Output)`: Căn giữa ô 100% (**`Center`**), font **`Consolas 11pt Bold`** (đồng bộ font Consolas chuẩn với toàn bộ bảng testcase trong Quyển 1), màu nền xám nhạt `#F1F5F9`.
* **Dữ liệu Testcase (Hàng 1+) — Thuật toán Căn Lề Động (Dynamic Indent)**:
  * **Font chữ**: Bắt buộc font `Consolas`, cỡ chữ **`11.0pt`**, màu chữ `#1E293B`.
  * **Căn lề nội bộ**: Luôn giữ căn trái (**`Left`**) để các cột số thẳng hàng dọc chằn chặn, tuyệt đối không dùng `Center` text làm lệch trục số.
  * **Công thức tính độ thụt lề trái (`left_indent`) động theo độ dài chuỗi dài nhất (`max_len`)**:
    * Nhằm đưa khối dữ liệu vào chính giữa cột rộng $6\text{ cm}$ ($170\text{pt}$), áp dụng bảng tính `left_indent`:
      $$\text{left\_indent}(\text{max\_len}) = \max\left(10.0\text{ pt},\, 72.0\text{ pt} - \max(0, \text{max\_len} - 4) \times 3.25\text{ pt}\right)$$
    * **Chi tiết mapping chuẩn đối chiếu Quyển 1**:
      * $\text{max\_len} \le 4$ ký tự (ví dụ: `4`, `300`, `12`): $\text{left\_indent} = \mathbf{72.0\text{ pt}}$ (đẩy thẳng vào trung tâm cột).
      * $\text{max\_len} = 5$: $\text{left\_indent} = \mathbf{68.75\text{ pt}}$.
      * $\text{max\_len} = 6$: $\text{left\_indent} = \mathbf{65.5\text{ pt}}$.
      * $\text{max\_len} = 7$: $\text{left\_indent} = \mathbf{62.25\text{ pt}}$.
      * $\text{max\_len} = 9$: $\text{left\_indent} = \mathbf{55.75\text{ pt}}$.
      * $\text{max\_len} = 11$: $\text{left\_indent} = \mathbf{49.25\text{ pt}}$.
      * $\text{max\_len} = 14$: $\text{left\_indent} = \mathbf{39.5\text{ pt}}$.
      * $\text{max\_len} \ge 24$ ký tự: $\text{left\_indent} = \mathbf{10.0\text{ pt}}$ (giữ cách mép trái an toàn).
    * *Giải quyết triệt để lỗi Hình 2*: Khi output ngắn (như số `4`), `left_indent` sẽ tự động nhảy lên `72.0pt` để số `4` nằm cân xứng ở chính giữa cột Output, không bị dính sát mép trái như hiện tại!

### 5.4. Quy chuẩn Mục lục (Table of Contents), Đánh số trang & Cơ chế Update Field (PAGEREF)
* **Vị trí & Ngắt trang**: Mục lục đặt ở cuối tài liệu, tiêu đề mang thuộc tính **`pageBreakBefore = True`** để nằm trên trang mới riêng biệt.
* **Typography chuẩn in ấn**:
  * **Tiêu đề `Mục lục`**: Font `Times New Roman 18.0pt Bold`, màu đen tuyền `#000000`, căn trái `Left`, khoảng cách dưới `after = 140 dxa` (7pt).
  * **Đầu mục Lời nói đầu, Chương, Phụ lục**: Font `Times New Roman 14.0pt Bold`, màu đen `#000000`, khoảng cách trên `before = 140 - 160 dxa`, dưới `after = 30 - 40 dxa`.
  * **Đầu mục Bài học**: Font `Times New Roman 13.0pt Regular`, màu đen `#000000`, thụt lề trái `left = 280 - 320 dxa`, khoảng cách `before = 20 - 24 dxa`, `after = 20 - 24 dxa`.
* **Căn chỉnh dòng & Tab Leader**:
  * Bắt buộc có thẻ `<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="9899"/></w:tabs>` trên mỗi đoạn văn mục lục để các dấu chấm `....` kéo dài đều tăm tắp sát lề phải.
* **Cấu trúc trường số trang động `PAGEREF` chuẩn xác**:
  * Bắt buộc dùng cấu trúc thẻ phân rã OpenXML độc lập, chuẩn hoá thẻ `<w:noProof/>` cho số trang ban đầu:
    ```xml
    <w:r><w:tab/></w:r>
    <w:r><w:fldChar w:fldCharType="begin"/></w:r>
    <w:r><w:instrText>PAGEREF <bookmark_name> \h</w:instrText></w:r>
    <w:r><w:fldChar w:fldCharType="separate"/></w:r>
    <w:r><w:rPr><w:noProof/></w:rPr><w:t><page_init></w:t></w:r>
    <w:r><w:fldChar w:fldCharType="end"/></w:r>
    ```
* **QUY TẮC BẢO VỆ TỆP (CẤM GÂY POPUP CẢNH BÁO TRÊN WORD)**:
  * **Tuyệt đối CẤM chèn thẻ `<w:updateFields w:val="true"/>` vào `word/settings.xml`**.
  * **Lý do**: Thẻ `updateFields` sẽ kích hoạt cảnh báo bảo mật của Microsoft Word (*"This document contains fields that may refer to other files. Do you want to update..."*) mỗi khi người dùng mở tệp, gây gián đoạn và lo ngại lỗi file. Trường `PAGEREF` cục bộ tự nó đã hỗ trợ bấm `F9` (Update Field) khi người dùng cần mà không cần bật cờ hệ thống này.

---

## 6. Quy Chuẩn Đề Bài Lập Trình & Tính Toàn Vẹn Hệ Thống (Server Integrity)

Mọi bài tập thực hành trong giáo trình (`.docx`) và trong các tệp `De_Bai.md` thuộc thư mục `problems/` **BẮT BUỘC** tuân thủ tuyệt đối cấu trúc 7 phần sư phạm chuẩn mực của Quyển 1:

### 6.1. Cấu Trúc 7 Phần Bắt Buộc Của Đề Bài (`De_Bai.md`)
1. **`# Tiêu Đề`**: Tên bài toán hấp dẫn, gợi hình, mang tính ứng dụng thực tế cao (không gắn mã hiệu vào tiêu đề H1).
2. **`## Bối cảnh` (Storytelling & Real-world Motivation)**:
   * 1–2 đoạn văn khơi gợi tình huống thực tế sinh động (trường học, kỳ thi, giao thông đô thị, hệ thống phân loại, cảm biến IoT, chuỗi cung ứng, robot, hệ thống xếp hạng online DKOJ...).
   * Tuyệt đối không viết cụt lủn 1 dòng thô thiển dạng toán học máy móc. Học sinh đọc vào phải thấy được sự liên kết giữa thuật toán và đời sống.
3. **`## Nhiệm vụ` (Clear Technical Mission)**:
   * Tách bạch rõ ràng mục tiêu kỹ thuật cần giải quyết bằng lời văn sư phạm chuẩn: *"Cho danh sách... Bạn hãy lập trình tìm/tính/xác định/in ra..."*.
4. **`## Input` (Đặc tả dữ liệu đầu vào chi tiết & chuẩn chỉnh)**:
   * Phải ghi rõ từng dòng dữ liệu:
     * Dòng 1: Chứa số lượng phần tử $N$ (hoặc $N, M, Q$) cùng phạm vi giá trị.
     * Các dòng tiếp theo: Đặc tả cụ thể kiểu dữ liệu, các giá trị trên dòng cách nhau bởi khoảng trắng.
   * Tuyệt đối không viết câu cụt lủn thiếu kích thước (ví dụ cấm viết: `- $Q$ dòng tiếp theo chứa các truy vấn`).
5. **`## Output` (Đặc tả dữ liệu đầu ra)**:
   * Ghi rõ số dòng xuất ra, định dạng các phần tử (cách nhau bởi dấu cách hay xuống dòng), trường hợp vô nghiệm/không tìm thấy in ra giá trị gì (ví dụ: `-1`).
6. **`## Sample 1` (Ví dụ mẫu: Input & Output)**:
   * Khối text Input và Output mẫu chuẩn xác.
7. **`### Giải thích` (Pedagogical Step-by-Step Trace — TUYỆT ĐỐI KHÔNG SPOIL THUẬT TOÁN)**:
   * **Mục đích**: Giúp học sinh hiểu tường tận *tại sao dữ liệu đầu vào đó lại sinh ra kết quả đầu ra đó*.
   * **Nguyên tắc Sư phạm Bất di bất dịch**:
     * **BẮT BUỘC TRACE DỮ LIỆU TAY (Walkthrough)**: Diễn giải từng bước biến đổi của các con số/chuỗi cụ thể trên Sample 1.
     * **TUYỆT ĐỐI CẤM SPOIL THUẬT TOÁN**: Cấm tiết lộ tên thuật toán, công thức quy hoạch động ($dp[i][j]$), tên cấu trúc dữ liệu kỹ thuật cao siêu (`map`, `set`, `Segment Tree`, `id -> score`, độ phức tạp $\mathcal{O}(N \log N)$) vào phần `Giải thích` của đề bài. Phần đề bài là student-facing, việc phân tích thuật toán chuyên sâu thuộc về `Huong_Dan_Giang_Day.md`.
   * **Quy chuẩn Format trình bày trong Word (Chống dãn chữ & Bể layout)**:
     * **Tiêu đề `Giải thích:`**: Đoạn văn riêng biệt mang style `Compact` (in đậm `Bold`, `<w:b/>`).
     * **Nội dung diễn giải**: **Mỗi dòng là một đoạn văn riêng biệt (`<w:p>`) độc lập mang style `Normal`**, font **`Times New Roman 12.5pt`**.
     * **CĂN TRÁI TỰ NHIÊN (`Left-aligned`)**: **TUYỆT ĐỐI CẤM CĂN `Justify`** cho các đoạn văn trong khối Giải thích, và **TUYỆT ĐỐI CẤM DÙNG THẺ `<w:br/>`** để dồn các dòng vào chung một đoạn văn, vì sẽ làm Word kéo dãn khoảng cách giữa các chữ cái (`1.   Bước   từng   bậc...`).
     * Ký hiệu toán học Unicode sạch sẽ (`≤`, `≥`, `...`, không để lọt tag LaTeX thô `\le`, `\ge`).
8. **`## Ràng buộc`**:
   * Tỉ lệ subtask / testcases, các ngưỡng giá trị và giới hạn: Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.


> 🔒 **Cam kết bất biến về Máy chủ Chấm thi (DKOJ Server Integrity)**:
> Tuyệt đối **không thay đổi** bất kỳ thông số nào thuộc về Input schema, Output schema, giá trị trong Sample Testcase và các ngưỡng Ràng buộc ($N$, thời gian $1.0\text{s}$, bộ nhớ $256\text{MB}$) vì toàn bộ đã được đồng bộ chuẩn hóa trên hệ thống chấm tự động DKOJ.

---

## 7. Pipeline Tự Động Hóa Rebuild / Build File Word (Build Pipeline)

Khi triển khai build hoặc rebuild một file giáo trình Word, kịch bản tự động hóa phải chạy qua 4 bước khép kín:

```text
┌─────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 1: Form Khổ giấy, Lời nói đầu & Watermark 100% Trang             │
│  - Bỏ trang bìa, thiết lập Margins: 36pt (Top/Bottom/Right), 64.35pt (L)│
│  - Format Lời nói đầu: P0 Center 14pt Bold, P1-P10 Justify 14pt 1.5 sp  │
│  - pageBreakBefore cho Chương đầu tiên                                  │
│  - Cấu hình 3 Header (First, Default, Even) kèm Watermark mờ image13    │
│  - Footer: Đánh số trang tự động dạng "— [Page] —"                     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 2: Chuẩn hóa Typography & Bảng theo PLAN_CHINH_WORD_IN_MAU        │
│  - Body text: 12.5pt, line-height 1.15, Justify 100%                   │
│  - Tiêu đề "Bài tập thực hành": Chuyển màu Đỏ #FF0000 Bold 14pt         │
│  - Headings: #1E293B (H1 18/15.5pt, H2 14pt, H3 13pt)                   │
│  - Khung Source Code: Font Consolas 9pt, line=252, Căn trái Left        │
│  - Bảng: Xóa tblHeader, thêm cantSplit cho mọi dòng                    │
│  - Bảng tra cứu Phụ lục A: Đồng bộ font 12pt                           │
│  - Bảng Sample IO: Căn giữa bảng w=6800, thụt lề ĐỘNG Dynamic Indent    │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 3: Làm giàu & Đồng bộ Đề bài (Bối cảnh, Nhiệm vụ, Giải thích)     │
│  - Đọc từ các thư mục problems/ hoặc tệp De_Bai.md tương ứng            │
│  - Cập nhật đủ 3 khối: Bối cảnh, Nhiệm vụ, Giải thích chi tiết          │
│  - Chuyển đổi toàn bộ công thức sang Unicode sạch (không $, không \le)  │
│  - Đảm bảo "Giải thích: " có khoảng trắng chuẩn                         │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  BƯỚC 4: Kiểm toán Kỹ thuật (Audit & Verification)                      │
│  - Kiểm tra 100% trang có Logo Watermark ở trung tâm                   │
│  - Kiểm tra 100% bài có Bối cảnh, Nhiệm vụ, Giải thích                  │
│  - Kiểm tra 100% bảng: 0 tblHeader, 100% cantSplit, Math 12pt          │
│  - Kiểm tra số trang footer và thẩm mỹ ngắt trang                       │
└─────────────────────────────────────────────────────────────────────────┘
```
