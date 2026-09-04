# Kế Hoạch Rebuild Toàn Diện Quyển 2: C++ Nâng Cao (c++-level-1-quyen-2.docx)
*Được cập nhật và chuẩn hóa tuyệt đối theo: [courses/cpp-bang-b/c++-level-1-quyen-1.docx](file:///Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/c++-level-1-quyen-1.docx) & [docs/MASTER_WORD_BUILD_SPECIFICATION.md](file:///Users/vu/Developer/ikhEdu_lessons/docs/MASTER_WORD_BUILD_SPECIFICATION.md)*

---

## 1. Bảng So Sánh & Đối Chiếu Hiện Trạng Chi Tiết

| Hạng mục | Quyển 1 (`c++-level-1-quyen-1.docx` - MẪU CHUẨN) | Quyển 2 Hiện Tại (`c++-level-1-quyen-2.docx`) | Yêu Cầu Theo Đặc Tả & Khắc Phục |
| :--- | :--- | :--- | :--- |
| **Lời nói đầu** | `Heading 1` Center 14pt, P1-P10 Justify 14pt 1.5 sp, P11 `pageBreakBefore` | Đã hoàn tất ở Bước 1 | Giữ vững chuẩn mực Bước 1 |
| **Watermark Logo** | Có ở 100% trang (`header1`, `header2`, `header3`) | Đã nhúng chuẩn vào 100% trang | Giữ vững chuẩn mực Bước 1 |
| **Tiêu đề "Bài tập thực hành"** | **Màu đỏ chuẩn `#FF0000` (Bold, 14pt)** ở toàn bộ các bài | Đã đổi sang Màu đỏ `#FF0000` Bold | Duy trì chuẩn |
| **Body text các bài học** | Cỡ **12.5pt**, dãn dòng **1.15 line spacing**, Căn đều **Justify** 100% | Đã căn Justify 100% | Duy trì chuẩn |
| **Khung mã nguồn (Hình 1)** | Font `Consolas 9pt`, dãn dòng `1.05`, **Căn trái (`Left`)**, không bị dãn chữ | Đang dính numbering rác `w:numPr`, một số nơi bị gán sai style | Loại bỏ hoàn toàn `w:numPr`, ép chuẩn `Source Code` font `Consolas 9pt`, Căn trái `Left` |
| **Bảng Sample IO (Hình 2)** | Căn giữa bảng `w=6800`, testcase căn trái có **thụt lề ĐỘNG (`Dynamic Left Indent`)** | Đang đặt cứng thụt lề 10pt cho tất cả nên số ngắn như `4` bị lệch sát mép trái | Áp dụng công thức tính `left_indent` động từ `10pt` đến `72pt` theo độ dài chuỗi |
| **Bảng tra cứu Phụ lục A** | Toàn bộ chữ trong bảng tra cứu có cỡ chữ chuẩn **`12.0pt`** | Đang bị nhỏ thành **`10.0pt`** | Nâng toàn bộ font chữ bảng tra cứu lên **`12.0pt`** đồng bộ Quyển 1 |
| **Bảng: Lặp lại tiêu đề khi ngắt trang** | Đã xóa bỏ thẻ `<w:tblHeader/>` trên toàn bộ bảng, thêm `<w:cantSplit/>` | 152/152 bảng đã xóa `tblHeader`, có `cantSplit` | Duy trì chuẩn |
| **Bảng: Cỡ chữ công thức toán** | Ép cứng `w:sz val="24"` (**12pt**) cho toàn bộ ký tự trong `<m:oMath>` | Đã quét và ép chuẩn 12pt | Duy trì chuẩn |
| **Giải thích Sample cho 135 bài** | 100% bài có phần `Giải thích:` chi tiết, toán Unicode sạch | **0 / 135 bài có phần Giải thích** | **Bổ sung 100% Giải thích** cho 135 bài toán trong cả `De_Bai.md` và file Word |
| **Bối cảnh & Nhiệm vụ** | Cốt truyện thực tế phong phú, Nhiệm vụ phân tách rõ | Đề bài toán học khô khan, thiếu cốt truyện | Làm giàu cốt truyện Bối cảnh & Nhiệm vụ cho 135 bài |
| **Tính toàn vẹn Server** | Giữ nguyên 100% testcase và ràng buộc | Giữ nguyên 100% testcase và ràng buộc | **Bảo toàn 100% Input/Output/Constraints trên DKOJ** |

---

## 2. Lộ Trình Triển Khai 4 Giai Đoạn (Chỉ thực thi khi người dùng duyệt)

```text
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 1: Chuẩn hóa Lời nói đầu & Watermark Logo trên từng trang    │
│  [ĐÃ HOÀN TẤT] - 14pt 1.5sp Justify, pageBreakBefore, Watermark 100%     │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 2: Khắc phục triệt để Bảng & Code theo Hình 1 & Hình 2       │
│  [ĐÃ HOÀN TẤT 100%]                                                     │
│  - Khắc phục Hình 1: Chuẩn hóa khung Source Code, Consolas 9pt, line 252│
│    loại bỏ numbering rác numPr, đảm bảo căn trái Left tuyệt đối         │
│  - Khắc phục Hình 2: Áp dụng thuật toán Dynamic Left Indent cho 135     │
│    bảng Sample IO: len <= 4 ký tự -> indent 72pt (cân giữa hoàn hảo),   │
│    len dài hơn giảm dần về 10pt                                         │
│  - Tách đa dòng (multiline) thành từng thẻ <w:p> độc lập                │
│    (140 cell được tách dòng thành công)                                 │
│  - Nâng font bảng tra cứu Phụ lục A lên 12.0pt chuẩn Quyển 1           │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 3: Làm giàu 135 Đề bài (Bối cảnh, Nhiệm vụ, Giải thích)      │
│  - 45 bài Chương 05: DP 1D, DP 2D Knapsack, DP Chuỗi LCS/Edit Distance  │
│  - 45 bài Chương 06: STL Set/Map/Heap, Stack, Queue/Monotonic Deque     │
│  - 45 bài Chương 07: Đồ thị BFS/DFS, Lưới 2D Flood Fill, Segment/BIT    │
│  - Cập nhật song song 135 file De_Bai.md & đưa vào Word                 │
│  - Làm sạch toán học Unicode, space sau dấu hai chấm "Giải thích: "    │
└────────────────────────────────────┬────────────────────────────────────┘
                                     │
                                     ▼
┌─────────────────────────────────────────────────────────────────────────┐
│  GIAI ĐOẠN 4: Kiểm toán Tổng thể (Audit) & Bàn giao                      │
│  - Kiểm tra thẩm mỹ từng trang bằng công cụ render/so sánh              │
│  - Audit 135/135 bài: Đủ Bối cảnh, Nhiệm vụ, Giải thích                 │
│  - Audit 152 bảng: Dynamic Indent chuẩn xác, font 12pt đồng bộ          │
│  - Kiểm tra logo watermark trên từng trang và số trang chính xác        │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Báo Cáo Chi Tiết Căn Nguyên Lỗi Hình 1 & Hình 2 (Theo yêu cầu)

### 3.1. Phân tích lỗi Hình 1 (Khung Code quá rộng & cỡ chữ bất hợp lý)
* **Hiện trạng phát hiện qua phân tích OpenXML đoạn P309**:
  * Đoạn code ngắn 3 dòng `for (int w = W; ...)` đang bị dính thẻ `<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>` (thẻ danh sách/numbering tự động).
  * Khung viền paragraph border `<w:pBdr>` và shading `<w:shd>` theo mặc định của Word chiếm toàn bộ độ rộng lề in ($16.5\text{ cm}$). Khi đoạn code chỉ có 3 dòng ngắn, việc khung viền trải dài hết mép trang tạo cảm giác khung bị "trống trải và quá bè".
  * Font chữ trong đoạn code bị chia vụn thành 49 run nhỏ, một số run bị mất font `Consolas` làm chữ trông thô và không đồng đều.
* **Giải pháp khắc phục**:
  * Loại bỏ triệt để thẻ `<w:numPr>` rác khỏi mọi đoạn code.
  * Đồng bộ toàn bộ các run trong khối code về font `Consolas 9.0pt` chuẩn mực.
  * Áp dụng thụt lề khối code cân đối hoặc cấu hình bảng code thu gọn cho các đoạn mã ngắn.

### 3.2. Phân tích lỗi Hình 2 (Phần Input / Output chưa giống Quyển 1)
* **Hiện trạng phát hiện qua so sánh Table 30 của Q2 với Table 3**:
  * **Căn lề ô**:
    * Tiêu đề `Đầu vào (Input)` và `Đầu ra (Output)`: Căn giữa ô 100% (**`Center`**), font **`Consolas 11pt Bold`** (đồng bộ chuẩn 100% với Quyển 1), màu nền xám nhạt `#F1F5F9`.
    * Dữ liệu testcase bên trong: Giữ nguyên căn trái nội bộ (**`Left`**) và áp dụng khoảng thụt đầu dòng động (`left_indent`) để khối testcase nằm cân xứng ở chính giữa ô mà không làm lệch trục các con số.
    * Font testcase: `Consolas 11pt`.
  * Ở Hình 2, ô Output chỉ chứa duy nhất một con số ngắn: `4`. Trong bước trước, tôi đã áp dụng khoảng thụt lề tĩnh `left_indent = 10.0pt` cho tất cả các bảng. Khoảng thụt này chỉ cách mép trái $0.35\text{ cm}$, nên khi gặp số ngắn như `4`, con số này bị **dính sát vào mép trái của ô**, để trống một khoảng mênh mông bên phải!
* **Quy chuẩn chuẩn mực tại Quyển 1 (`docs/PLAN_CHINH_WORD_IN_MAU.md` mục 3.3 & 5.3)**:
  * Quyển 1 sử dụng **Thuật toán Thụt Lề Động (Dynamic Left Indent)**:
    * Khi nội dung ngắn ($\text{max\_len} \le 4$ ký tự, ví dụ số `4`), `left_indent` trong Quyển 1 được tính toán tự động bằng **`72.0pt`** ($2.54\text{ cm}$).
    * Khoảng thụt `72.0pt` đẩy con số `4` vào **chính giữa cột Output** một cách cực kỳ cân đối, vuông vức và chuyên nghiệp!
    * Khi nội dung dài hơn, `left_indent` giảm dần theo công thức:
      $$\text{left\_indent}(\text{max\_len}) = \max\left(10.0\text{ pt},\, 72.0\text{ pt} - \max(0, \text{max\_len} - 4) \times 3.25\text{ pt}\right)$$
    * Các cột số vẫn giữ nguyên căn trái nội bộ (`Left-aligned`) để các chữ số hàng chục, hàng đơn vị thẳng hàng dọc chằn chặn.
* **Giải pháp khắc phục**: Áp dụng chuẩn xác thuật toán Dynamic Indent của Quyển 1 cho toàn bộ 135 bảng Sample IO.

### 3.4. Quy Chuẩn Đề Bài Lập Trình (De_Bai.md & File Word)
* **Lỗi hiện tại**:
  * Bối cảnh viết quá ngắn (1 dòng), khô khan như đề thi toán học hàn lâm, thiếu cốt truyện thực tế (59/135 bài chỉ có 1 dòng cụt ngủn).
  * 43 bài dính lỗi spoil thuật toán trong `Giải thích` (tiết lộ tên thuật toán, công thức quy hoạch động, tên cấu trúc dữ liệu `map`, `set`, `Segment Tree`, `O(log N)`).
* **Quy chuẩn chuẩn mực theo Quyển 1 & MASTER_WORD_BUILD_SPECIFICATION**:
  * **Bối cảnh (Storytelling)**: 1–2 đoạn văn khơi gợi tình huống thực tế sinh động (hệ thống máy chủ, kỳ thi trực tuyến DKOJ, dây chuyền sản xuất, logistics, cảm biến, robot, ngân hàng...).
  * **Nhiệm vụ (Mission)**: Nêu rõ mục tiêu kỹ thuật rõ ràng bằng lời văn sư phạm: *"Cho... Bạn hãy lập trình..."*.
  * **Input/Output**: Đặc tả tường minh từng dòng, định dạng khoảng trắng/xuống dòng, trường hợp vô nghiệm.
  * **Giải thích Sample (Step-by-step Trace)**: Bắt buộc mô phỏng trace dữ liệu mẫu từng bước bằng tay. **Tuyệt đối cấm spoil thuật toán** (không nhắc tên giải thuật, không nhắc độ phức tạp, không nhắc cấu trúc dữ liệu kỹ thuật).
* **Giải pháp khắc phục**:
  * Cập nhật toàn bộ 135 tệp `De_Bai.md` trong `courses/cpp-bang-b/problems/`.
  * Đồng bộ nội dung Bối cảnh, Nhiệm vụ, Input, Output và Giải thích chuẩn mực vào file Word `c++-level-1-quyen-2.docx`.

