# KẾ HOẠCH MASTER REBUILD TOÀN DIỆN BỘ GIÁO TRÌNH C++ LEVEL 2 (QUYỂN 1 & QUYỂN 2)
*(Universal Rebuild Specification & Action Plan for Level 2 Coursebooks)*

**Mã kế hoạch:** `IKHEDU-REBUILD-L2-v3.0`  
**Căn cứ pháp lý & Nguồn đối chiếu chuẩn mực:**
1. [docs/MASTER_WORD_BUILD_SPECIFICATION.md](file:///Users/vu/Developer/ikhEdu_lessons/docs/MASTER_WORD_BUILD_SPECIFICATION.md) *(Đặc tả master xuất bản Word chuẩn in ấn v2.1)*
2. [docs/PLAN_CHINH_WORD_IN_MAU.md](file:///Users/vu/Developer/ikhEdu_lessons/docs/PLAN_CHINH_WORD_IN_MAU.md) *(Quy chuẩn thiết kế in màu & xử lý bảng)*
3. [courses/cpp-bang-b/c++-level-1-quyen-1.docx](file:///Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/c++-level-1-quyen-1.docx) *(Tệp Word mẫu đối chiếu chuẩn của Quyển 1)*
4. [courses/cpp-bang-b/KE_HOACH_REBUILD_QUYEN_2.md](file:///Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/KE_HOACH_REBUILD_QUYEN_2.md) *(Bài học & kinh nghiệm thực chiến từ Rebuild Quyển 2 Cơ bản)*
5. [.agent/rules/academic-authoring-always-on.md](file:///Users/vu/Developer/ikhEdu_lessons/.agent/rules/academic-authoring-always-on.md) *(Bộ quy tắc đào tạo iKHEDU — §7 Problem Package, §8 Print-Ready Word DOCX)*

---

## 1. BẢNG ĐỐI CHIẾU CHI TIẾT TỪNG HẠNG MỤC (AUDIT MATRIX)

| STT | Hạng mục kỹ thuật | Quy chuẩn Khuôn mẫu Mẫu (`c++-level-1-quyen-1.docx` & Master Spec) | Hiện trạng Level 2 (`IKHEDU_CPP_Nang_Cao_Q1/Q2`) | Kế hoạch Rebuild Chuẩn xác |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Trang bìa** | **Bỏ hoàn toàn trang bìa**, tài liệu vào thẳng **`LỜI NÓI ĐẦU`** tại trang 1. Tiêu đề Chương 01 mang `pageBreakBefore = True`. | Đang có 7 đoạn văn bìa thô (`Title`, `Subtitle`, `Author`, đường kẻ `────`, `Tagline`, `TRUNG TÂM TIN HỌC iKH`, `Phiên bản 2026`). | **Xóa sạch 100% trang bìa**, mở đầu ngay bằng `Lời nói đầu`. Đặt `pageBreakBefore = True` cho Chương 01. |
| **2** | **Watermark Logo** | **100% các trang** đều có logo mờ iKH ở chính giữa. Cấu hình đủ **3 Header References** (`even`, `default`, `first`) chứa VML Watermark shape `alt="logo_in"` trỏ tới `media/image13.jpeg`. | **0% trang có Watermark Logo** (hoàn toàn chưa nhúng). | **Nhúng tự động Watermark logo iKH** vào cả 3 header (`even`, `default`, `first`) để phủ đều 100% trang in. |
| **3** | **Định dạng Lời nói đầu** | Tiêu đề: `Heading 1` Center **14.0pt Bold** `#1E293B`. Nội dung: Cỡ **14.0pt**, dãn dòng **1.5 line spacing**, Căn đều **Justify** 100%. | Đang để font 12.5pt, dãn dòng 1.1 line spacing mặc định. | **Đồng bộ chuẩn Lời nói đầu**: Tiêu đề Center 14pt Bold, nội dung Justify 14pt với dãn dòng 1.5. |
| **4** | **Lề trang in (Margins)** | Chuẩn in offset tiết kiệm: **Top = 36pt (1.27cm), Bottom = 36pt (1.27cm), Right = 36pt (1.27cm), Left = 64.35pt (2.27cm)** (gáy đóng sách). | Đang để lề mặc định thoáng: Top/Bottom/Right = 2.0 cm, Left = 2.2 cm. | **Đồng bộ lề chuẩn**: Top `36pt`, Bottom `36pt`, Right `36pt`, Left `64.35pt` giúp sách vuông vức và tiết kiệm giấy. |
| **5** | **Căn lề văn bản** | **`JUSTIFY`** (Căn đều 2 bên 100% cho `Body Text`, `First Paragraph`, `Normal`, `Compact`, `Block Text`). | Đang để căn trái mặc định (`None`), mép phải trang chưa thẳng. | **Căn đều `Justify` 100%** toàn bộ các đoạn văn bài học và bài tập. |
| **6** | **Tiêu đề "Bài tập thực hành"** | Bắt buộc đổi sang **Màu đỏ chuẩn `#FF0000` (Bold, 14pt, Heading 2)** ở toàn bộ các bài học. | Đang mang màu xám sẫm `#1E293B`. | **Đổi màu sang Đỏ `#FF0000` Bold 14pt** ở 100% các bài học để tạo điểm nhấn thị giác. |
| **7** | **Bảng Sample IO (Đầu vào/ra)** | **Bảng 2 cột** rộng `6800 dxa` (~12cm), căn giữa trang (`w:jc="center"`). Header căn giữa Consolas 11pt Bold `#F1F5F9`. Testcase căn trái có **Thuật toán Dynamic Left Indent** (`10pt` - `72pt`). | Đang là text thô `### Input` / `### Output` kèm code block riêng rẽ, chiếm nhiều dòng dọc gây vỡ trang. | **Chuyển toàn bộ 346 bài tập thành Bảng 2 cột Sample IO**, căn giữa trang và áp dụng Dynamic Left Indent. |
| **8** | **Xuống dòng Testcase (Multiline)** | Mọi testcase ma trận, mảng hay danh sách nhiều dòng **bắt buộc tách thành từng đoạn riêng biệt (`<w:p>`) trong ô bảng**, mỗi dòng kế thừa cùng mức `left_indent`. | Đang hiển thị code block thô. | **Tách đa dòng thành từng thẻ `<w:p>` độc lập** trong cell bảng, loại bỏ dồn dòng ngang bằng dấu cách hay `...`. |
| **9** | **Khung mã nguồn (`Source Code`)** | Font `Consolas 9.0pt`, dãn dòng `1.05` (`line=252`), nền `#F8FAFC`, viền `#CBD5E1`/`#E2E8F0`. **Bắt buộc Căn trái (`Left`) 100%**, cấm numbering rác (`w:numPr`). | Đã có styling nhưng cần bảo đảm không kế thừa Justify từ Normal và sạch `numPr`. | **Kiểm soát chặt chẽ `<w:jc w:val="left"/>`** trên 100% khối code giải thuật, cấm dính Justify làm dãn chữ. |
| **10** | **Bảng: Duplicate Title & Vỡ hàng** | **Xóa sạch 100% `<w:tblHeader/>`**, bổ sung `<w:cantSplit/>` cho mọi hàng để chống lặp header và chống xé đôi chữ. | Còn nguyên `<w:tblHeader/>` trên 54 bảng ở 2 quyển (28 ở Q1, 26 ở Q2). | **Xóa sạch thẻ `tblHeader` trên 100% bảng** và thêm `cantSplit` cho toàn bộ các hàng. |
| **11** | **Bảng: Font Math & Bảng Phụ lục A** | Ép cứng font size công thức toán `m:oMath` trong bảng thành **12.0pt** (`w:sz val="24"`). Toàn bộ bảng tra cứu Phụ lục A có font chữ chuẩn **12.0pt**. | Công thức toán trong bảng đang bị co nhỏ thành `9.5pt` / `10.5pt` khấp khểnh. | **Ép cứng `w:sz val="24"` (12pt)** cho toàn bộ `m:oMath` và đồng bộ font bảng tra cứu Phụ lục A lên 12pt. |
| **12** | **Quy chuẩn Đề bài (`De_Bai.md`)** | **Bắt buộc chuẩn 100% theo Rule §7**: Tiêu đề ngữ pháp tự nhiên, Bối cảnh thực tế giàu tính ứng dụng, Nhiệm vụ kỹ thuật rõ ràng (*"Cho... Hãy lập trình..."*), Input/Output chuẩn kích thước, Sample thật, **Giải thích trace tay cấm tuyệt đối spoil thuật toán**, Ràng buộc chuẩn. Tuyệt đối không đưa mã bài/code vào statement. | **Tồn tại 4 tử huyệt lớn**: 210/346 bài dính bối cảnh template rập khuôn; 336/346 bài có câu nhiệm vụ sáo rỗng; 210/346 bài có Sample rác (`15`) và 15 bài thiếu hoàn toàn phần Giải thích. | **Tái cấu trúc và chuẩn hóa toàn bộ 346 bài** theo đúng cấu trúc chuẩn 7 phần tại Rule §7, viết lại bối cảnh, nhiệm vụ cụ thể và bổ sung giải thích trace tay từng bước sạch spoil. |
| **13** | **Hình ảnh minh họa** | 100% hình ảnh minh họa vector Light Theme 300 DPI, nền sáng $\ge 232/255$, font Arial an toàn (không lỗi font `???`). | 17 hình minh họa đã chuyển đổi Light Theme Arial sạch sẽ. | **Nhúng trực tiếp 17 hình PNG 300 DPI** vào đúng các vị trí bài giảng tương ứng. |
| **14** | **Tính toàn vẹn Server (DKOJ)** | Giữ nguyên 100% testcase, Input schema, Output schema và ràng buộc. | Giữ nguyên 100%. | **Bảo toàn tuyệt đối 100% logic testcase và ràng buộc thi đấu**. |

---

## 2. QUY CHUẨN ĐẶC TẢ ĐỀ BÀI (`DE_BAI.MD`) THEO RULE §7 & HIỆN TRẠNG 346 BÀI LEVEL 2

Căn cứ theo **Section 7 trong `.agent/rules/academic-authoring-always-on.md`**, mọi tệp `De_Bai.md` trong hệ thống học liệu iKHEDU bắt buộc phải tuân thủ nghiêm ngặt 7 tiêu chuẩn sư phạm cốt lõi:

### 2.1. Bảy Tiêu Chuẩn Vàng Của Đề Bài Student-Facing (Rule §7)

```text
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│  CẤU TRÚC CHUẨN CỦA TỆP De_Bai.md THEO RULE §7                                                   │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│  1. # [Tiêu đề]         : Gợi hình, gắn với thực tế đời sống; viết hoa chữ đầu (Sentence Case)   │
│  2. ## Bối cảnh         : Cốt truyện thực tế, giàu tính ứng dụng, khơi gợi cảm hứng              │
│                           ⚠️ TUYỆT ĐỐI KHÔNG viết cụt lủn toán học 1 dòng hoặc template rập khuôn│
│  3. ## Nhiệm vụ         : Tách bạch nhiệm vụ kỹ thuật rõ ràng: "Cho... Hãy lập trình..."         │
│                           ⚠️ CẤM câu sáo rỗng: "Hãy lập trình giải quyết bài toán với O tối ưu" │
│  4. ## Input            : Mô tả chi tiết từng dòng, số lượng phần tử N, M, kiểu dữ liệu          │
│                           ⚠️ TUYỆT ĐỐI KHÔNG viết câu cụt lủn thiếu kích thước ma trận/mảng      │
│  5. ## Output           : Định dạng kết quả trả về, cách nhau dấu cách/xuống dòng, vô nghiệm (-1)│
│  6. ## Sample 1         : Gồm ### Input, ### Output và ### Giải thích:                           │
│      * ### Giải thích   : Mô phỏng trace dữ liệu mẫu từng bước bằng tay (walkthrough chi tiết)  │
│      * ⚠️ CẤM SPOIL    : TUYỆT ĐỐI CẤM tiết lộ tên thuật toán (DP, BFS, Dijkstra, CHT, Fenwick),│
│                           công thức DP, cấu trúc dữ liệu kỹ thuật hoặc O(...) trong đề bài       │
│  7. ## Ràng buộc        : Giới hạn test, thời gian 1.0s, bộ nhớ 256MB                            │
│  ⚠️ NGUYÊN TẮC CỐT TỬ   : Tuyệt đối không đưa dòng "Mã bài toán" hay mã nguồn code vào statement│
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2. Kiểm Toán Thực Tế Tử Huyệt Đề Bài Trên Toàn Bộ 346 Bài Level 2

Qua kết quả quét tự động (`Automated Deep Audit`) trên toàn bộ 346 thư mục bài tập của `courses/cpp-bang-b-level2/problems/`, hiện trạng đề bài đang tồn tại các lỗi nghiêm trọng sau:

1. **336 / 346 bài (97.1%) dính câu Nhiệm vụ rập khuôn sáo rỗng**:
   * *Nội dung hiện tại:* `"Hãy lập trình giải quyết bài toán [Tên bài] với độ phức tạp tối ưu nhất."`
   * *Vi phạm:* Trực tiếp vi phạm Rule §7 yêu cầu tách bạch nhiệm vụ kỹ thuật rõ ràng: *"Cho... Hãy lập trình..."*. Câu sáo rỗng này không cung cấp thông tin kỹ thuật gì cho học sinh.
2. **210 / 346 bài (60.7%) dính Bối cảnh template copy-paste hàng loạt**:
   * *Nội dung hiện tại:* `"Trong lập trình thi đấu và giải quyết bài toán tối ưu, [Tên bài] là bài toán trọng tâm thuộc cấp độ Px nhằm rèn luyện: ... Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu."`
   * *Vi phạm:* Vi phạm Rule §7 (*"Cốt truyện thực tế, giàu tính ứng dụng, khơi gợi cảm hứng; tuyệt đối không viết cụt lủn toán học 1 dòng"*). Học sinh đọc vào chỉ thấy một khuôn đúc vô hồn, không có bối cảnh bài toán thật.
3. **210 / 346 bài (60.7%) có Sample giả lập rác (`1 2 3 4 5` $\to$ `15`)**:
   * *Nội dung hiện tại:* Input là `5\n1 2 3 4 5`, Output là `15` và phần Giải thích ghi: *"Kết quả tính toán phù hợp với yêu cầu của bài toán..."* (trong khi code `solution.cpp` của bài đó lại giải bài toán khác hoàn toàn, ví dụ bài đếm tần suất nén tọa độ in ra `vals[i]: freq[i]`).
   * *Vi phạm:* Đây là dữ liệu sinh tự động lỗi từ trước, làm sai lệch hoàn toàn hiểu biết của học sinh khi đối chiếu mẫu.
4. **15 / 136 bài viết riêng chưa có phần `### Giải thích`**:
   * Bao gồm các bài nền tảng của từng Lesson: `cppb2_l02_01`, `cppb2_l03_01`, `cppb2_l04_01`, `cppb2_l05_01`, `cppb2_l06_01`, `cppb2_l07_01`, `cppb2_l08_01`, `cppb2_l09_01`, `cppb2_l10_01`, `cppb2_l11_01`, `cppb2_l12_01`, `cppb2_l13_01`, `cppb2_l14_01`, `cppb2_l15_01`.
5. **Tiêu đề bài toán**:
   * Trước đây bị lỗi viết hoa toàn bộ chữ cái đầu như tiếng Anh (`Title Case`: *"Ước Chung & Bội Chung Cơ Bản"*). Cần tiếp tục bảo đảm chuẩn hóa Sentence case tự nhiên theo tiếng Việt (*"Ước chung & bội chung cơ bản"*), chỉ viết hoa các thuật ngữ chuẩn (`SPF`, `GCD`, `LCM`, `CRT`, `DP`, `LIS`, `BIT`...).

---

## 3. PHÂN TÍCH CHUYÊN SÂU CÁC TỬ HUYỆT KỸ THUẬT WORD (RULE §8)

### 3.1. Tử huyệt 1: Cơ chế Watermark Logo 100% Trang In trong OpenXML
* **Nguyên nhân gốc rễ**: Khi kích hoạt `different_first_page_header_footer`, Word chia section thành 2 phân hệ header: `first` (cho trang 1) và `default`/`even` (cho các trang tiếp theo). Nếu chỉ cấu hình Watermark trên `default`, trang 1 (`Lời nói đầu`) sẽ bị trắng tinh không có logo.
* **Giải pháp chuẩn Quyển 1**:
  * Tạo tệp `logo_in.jpeg` tại `word/media/image13.jpeg`.
  * Cấu hình đủ cả 3 header part: `word/header1.xml` (`first`), `word/header2.xml` (`default`), `word/header3.xml` (`even`).
  * Trong mỗi header XML, nhúng khối VML Shape:
    ```xml
    <w:p>
      <w:r>
        <w:pict>
          <v:shape id="WordPictureWatermark128699022X" type="#_x0000_t75" alt="logo_in" 
                   style="position:absolute;margin-left:0;margin-top:0;width:286pt;height:286pt;z-index:-251650048;mso-position-horizontal:center;mso-position-horizontal-relative:margin;mso-position-vertical:center;mso-position-vertical-relative:margin" 
                   o:allowincell="f">
            <v:imagedata r:id="rId1" o:title="logo_in" gain="19661f" blacklevel="22938f"/>
            <w10:wrap anchorx="margin" anchory="margin"/>
          </v:shape>
        </w:pict>
      </w:r>
    </w:p>
    ```
  * Mọi quan hệ `.rels` của header đều trỏ `rId1` tới `media/image13.jpeg`. Đảm bảo trang nào cũng có logo mờ ở trung tâm.

### 3.2. Tử huyệt 2: Thuật toán Căn Lề Động (Dynamic Left Indent) cho Bảng Sample IO
* **Vấn đề thực tế (Hình 2 trong bài học kinh nghiệm)**: Khi bảng rộng $12\text{ cm}$ ($6\text{ cm}$ mỗi cột), nếu đặt thụt lề tĩnh `10pt` thì với testcase output ngắn (ví dụ số `4` hoặc `YES`), kết quả bị dính sát vào mép trái của ô, để lại khoảng trống mênh mông bên phải. Nếu căn giữa `Center` text thì các số nhiều chữ số bị lệch trục hàng đơn vị, hàng chục.
* **Giải thuật Dynamic Indent của iKHEDU**:
  $$\text{left\_indent}(\text{max\_len}) = \max\left(10.0\text{ pt},\, 72.0\text{ pt} - \max(0, \text{max\_len} - 4) \times 3.25\text{ pt}\right)$$
  * Khi $\text{max\_len} \le 4$ (ví dụ: `4`, `12`): $\text{left\_indent} = \mathbf{72.0\text{ pt}}$ $\to$ đẩy số `4` nằm cân giữa cột Output.
  * Khi chuỗi dài hơn, khoảng thụt giảm dần về `10.0pt`.
  * Văn bản giữ nguyên căn trái nội bộ (`Left`) để các dòng thẳng hàng dọc chằn chặn.

### 3.3. Tử huyệt 3: Tránh lỗi Dãn Cách Chữ (Stretching Bug) trong Khối Code C++
* **Nguyên nhân gốc rễ**: Khi áp dụng lệnh căn đều hai bên (`Justify`) lên style `Normal`, các khối mã nguồn (`Source Code`) nếu kế thừa từ `Normal` sẽ bị Word tự động giãn khoảng cách giữa từng ký tự trên các dòng ngắn (ví dụ dòng `#include <bits/stdc++.h>` bị giãn thành `#   i   n   c   l   u   d   e`).
* **Giải pháp**:
  * Không bao giờ can thiệp `Justify` trực tiếp vào style `Normal`.
  * Chỉ gán `Justify` cho các style nội dung: `Body Text`, `First Paragraph`, `Compact`, `Block Text`.
  * Khối `Source Code` bắt buộc có thuộc tính rõ ràng `<w:jc w:val="left"/>` trên mọi thẻ `<w:p>`.

### 3.4. Tử huyệt 4: Định dạng Xuống Dòng (Multiline) trong Bảng Testcase
* **Nguyên nhân gốc rễ**: Khi chuyển đổi từ Markdown bảng sang Word, các testcase có nhiều dòng (như ma trận 2D, đồ thị $M$ cạnh) nếu bị dồn vào 1 đoạn văn ngăn cách bằng khoảng trắng hoặc dấu ba chấm sẽ làm học sinh không hiểu định dạng input.
* **Giải pháp chuẩn Quyển 1**:
  * Trong mỗi ô dữ liệu của Bảng Sample IO, mỗi dòng dữ liệu là một thẻ đoạn văn `<w:p>` độc lập:
    * Style: `Compact`.
    * Font: `Consolas 11.0pt`, màu `#1E293B`.
    * Spacing: `line="276"` (1.15), dòng đầu tiên có `space_before = 40` (2pt).
    * Indent: cùng mang giá trị `left_indent` động đã tính toán.
    * *(Nguồn áp dụng: `docs/MASTER_WORD_BUILD_SPECIFICATION.md` §5.3 — rule §8 chỉ quy định nguyên tắc multiline `<w:p>`, chi tiết cỡ chữ/spacing theo MASTER spec và thực tiễn Quyển 1.)*

---

## 4. CHIẾN LƯỢC LÀM SẠCH VÀ CHUẨN HÓA DỮ LIỆU ĐỀ BÀI (RULE §7)

1. **Chuẩn hóa 210 bài dính template bối cảnh rập khuôn & sample dummy**:
   - Viết lại Bối cảnh thực tế gắn liền với ứng dụng toán tin và đời sống cho từng bài toán.
   - Thay thế toàn bộ Sample dummy `1 2 3 4 5 -> 15` bằng bộ Sample Input/Output thật, khớp 100% với giải thuật chuẩn trong `solution.cpp`.
   - Viết phần `### Giải thích` mô phỏng từng bước tính toán bằng tay (trace tay trên các con số cụ thể).
   - **Tuyệt đối cấm spoil thuật toán**: Không nhắc tên DP, Dijkstra, Segment Tree, cấu trúc dữ liệu kỹ thuật hay công thức quy hoạch động trong phần Giải thích đề bài học sinh.
2. **Loại bỏ câu Nhiệm vụ sáo rỗng trên 336 bài**:
   - Thay thế toàn bộ câu *"Hãy lập trình giải quyết bài toán [Tên bài] với độ phức tạp tối ưu nhất"* bằng nhiệm vụ kỹ thuật cụ thể theo đúng cú pháp Rule §7: *"Cho... Hãy lập trình..."*.
3. **Bổ sung phần Giải thích cho 15 bài nền tảng**:
   - Cung cấp trace tay walkthrough chi tiết cho: `cppb2_l02_01`, `cppb2_l03_01`, `cppb2_l04_01`, `cppb2_l05_01`, `cppb2_l06_01`, `cppb2_l07_01`, `cppb2_l08_01`, `cppb2_l09_01`, `cppb2_l10_01`, `cppb2_l11_01`, `cppb2_l12_01`, `cppb2_l13_01`, `cppb2_l14_01`, `cppb2_l15_01`.
4. **Bảo đảm chuẩn hóa mô tả Input**:
   - Đầy đủ số dòng, kích thước ma trận $N, M$, phạm vi giá trị và kiểu dữ liệu, không có câu cụt lủn thiếu kích thước.

---

## 5. LỘ TRÌNH TRIỂN KHAI 4 GIAI ĐOẠN REBUILD LEVEL 2

```text
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 1: Chuẩn hóa Toàn Diện Dữ Liệu Đề Bài (Theo Rule §7)         │
│  - Thay thế 210 bài dính template rập khuôn bằng bối cảnh thực tế       │
│  - Thay thế 336 câu Nhiệm vụ sáo rỗng bằng nhiệm vụ kỹ thuật "Cho... Hãy"│
│  - Thay thế toàn bộ 210 Sample rác (dummy 15) bằng Sample thật khớp code │
│  - Bổ sung Giải thích Sample trace tay cho 15 bài còn thiếu             │
│  - Rà soát 100% Giải thích: CẤM TUYỆT ĐỐI spoil thuật toán/công thức DP  │
│  - Chuẩn hóa mô tả Input đầy đủ số dòng, kích thước N, M               │
│  - Bảo toàn tuyệt đối 100% logic nghiệm và testcase trên server DKOJ   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 2: Nâng Cấp Build Script (courses/cpp-bang-b-level2/build_docx.py)
│  - Bỏ 100% logic sinh trang bìa thô (bắt đầu ngay từ Lời nói đầu)       │
│  - Nâng cấp format_problem_statement: Chuyển Sample thành Bảng 2 cột    │
│  - Tách đa dòng (multiline) thành các thẻ <w:p> độc lập                 │
│  - Cấu hình Margins: Top 36pt, Bottom 36pt, Right 36pt, Left 64.35pt   │
│  - Chuẩn hóa Lời nói đầu: Heading 1 Center 14pt Bold, Body Justify 14pt │
│    dãn dòng 1.5, pageBreakBefore cho Chương 01                          │
│  - Đổi màu tiêu đề mục "Bài tập thực hành" sang Đỏ #FF0000 Bold 14pt    │
│  - Căn đều Justify 100% cho toàn bộ Body Text, Compact, First Paragraph │
│  - Khung Source Code: Consolas 9pt, line 252, Căn trái Left tuyệt đối   │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 3: Xử Lý OpenXML Post-process & Watermark Logo               │
│  - Nhúng VML Watermark logo iKH vào cả 3 header (First, Default, Even)  │
│  - Xóa sạch 100% <w:tblHeader/> trên tất cả các bảng (chống lặp header) │
│  - Bổ sung <w:cantSplit/> cho toàn bộ các hàng bảng (chống xé đôi chữ)  │
│  - Ép cứng font size công thức toán m:oMath trong bảng lên 12.0pt       │
│  - Nâng font chữ bảng tra cứu Phụ lục A lên chuẩn 12.0pt                │
│  - Áp dụng Thuật toán Dynamic Left Indent (10pt - 72pt) cho bảng Sample │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 4: Thực thi Rebuild, Kiểm toán Toàn diện & Bàn giao          │
│  - Rebuild Quyển 1: IKHEDU_CPP_Nang_Cao_Quyen_1.docx (134 bài)          │
│  - Rebuild Quyển 2: IKHEDU_CPP_Nang_Cao_Quyen_2.docx (212 bài)          │
│  - Chạy script kiểm toán tự động (Audit Script):                        │
│    + Xác nhận 0 trang bìa thô                                           │
│    + Xác nhận 100% trang có Watermark Logo iKH                          │
│    + Xác nhận 100% đoạn văn nội dung căn Justify                        │
│    + Xác nhận 100% bảng Sample IO căn giữa và có Dynamic Indent         │
│    + Xác nhận 0 bảng dính tblHeader, 100% cantSplit                     │
│    + Xác nhận 100% khối Source Code căn trái Left, 0 numPr              │
│  - Chốt QA theo rule: chạy qa-checklist, cập nhật evidence ledger /     │
│    decision log trước khi bàn giao (theo rule §8 câu cuối)               │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 6. KẾT LUẬN & CAM KẾT HÀNH ĐỘNG
Kế hoạch này đảm bảo khi thực thi rebuild, **hai quyển giáo trình C++ Level 2** sẽ đạt chất lượng xuất bản tương đương 100% với Quyển 1 mẫu (`c++-level-1-quyen-1.docx`), tuân thủ tuyệt đối đặc tả `MASTER_WORD_BUILD_SPECIFICATION.md` và bảo toàn toàn vẹn hệ thống chấm thi DKOJ.

Kế hoạch đã sẵn sàng và đang chờ phê duyệt từ chủ dự án trước khi tiến hành thực hiện.

