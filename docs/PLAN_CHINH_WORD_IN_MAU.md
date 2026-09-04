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
  1. `c++-level-1-quyen-1.docx` (Quyển 1: Bài 01 – Bài 12 — Bản cập nhật toàn diện Bảng & 12 Hình ảnh Light Theme)
  2. `IKHEDU_CPP_Co_Ban_Quyen_2.docx` (Quyển 2: Bài 13 – Bài 21)

---

## 3. Quy Chuẩn Thiết Kế & In Màu (Phương Án A)

### 3.1. Bảng màu chuẩn in ấn (Tiết kiệm mực, không bệt màu)
* **Chữ nội dung**: Đen xám đậm `#1E293B` (Times New Roman / Inter).
* **Tiêu đề (Headings) & Tiêu đề Bảng**:
  * Chữ đen xám `#1E293B` (loại bỏ chữ trắng trên nền xanh navy `#0F2A44` để tránh tốn mực và bệt màu).
  * **Tiêu đề mục "Bài tập thực hành"**: Đổi sang **Màu đỏ chuẩn `#FF0000` (Bold)** ở tất cả 12 Bài học để tạo điểm nhấn thị giác rõ ràng cho học sinh khi chuyển sang phần bài tập luyện tập.
  * Nền Header bảng: Xám trắng nhạt `#F1F5F9` viền `#CBD5E1`.
* **Khung ghi chú (Callout / Lưu ý)**:
  * Thống nhất 1 tone màu xanh lam nhạt `#EFF6FF`, viền `#3B82F6`, chữ `#1E3A8A`.
* **Khung Code Block**:
  * Nền `#F8FAFC`, viền `#E2E8F0`, chữ đen `#0F172A`, font `Consolas` / `JetBrains Mono`.

### 3.2. Cỡ chữ & Giãn dòng chuẩn
* **Văn bản nội dung (Body Text, First Paragraph, Compact, Normal)**:
  * Cỡ chữ chuẩn: **`12.5pt`**.
  * Giãn dòng: **`line-height = 1.15`** (khoảng cách chuẩn in sách giáo trình, thoáng đãng, dễ đọc).
  * Căn lề: Căn đều 2 bên (**`Justify`**) 100% để bản in vuông vức, thẳng đều 2 mép trang như sách xuất bản chuyên nghiệp.
* **Khung ghi chú & Callout (`Block Text`)**:
  * Cỡ chữ: **`12pt`**, giãn dòng **`1.15`**, căn đều **`Justify`**.
* **Tiêu đề (`Heading 1, 2, 3, 4`)**:
  * H1 (Chương/Bài): `18pt` (Chương - Căn giữa `Center`) / `15.5pt` (Bài học - Căn trái `Left`).
  * H2: `14pt Bold`, căn trái (`Left`).
  * H3: `13pt Bold`, căn trái (`Left`).
  * H4: `12.5pt Bold`, căn trái (`Left`).
  * *Lưu ý tuyệt đối:* **Không áp dụng căn Justify cho Heading** để tránh bị dãn khoảng cách chữ bất thường.
* **Khung Code Block (`Source Code`)**:
  * Font `Consolas` / `JetBrains Mono`, cỡ chữ `9pt`, giãn dòng `1.05`.
  * *Lưu ý tuyệt đối:* **Luôn giữ căn Trái (`Left`)**, cấm căn Justify để không làm lệch thụt đầu dòng và gãy cú pháp code.

### 3.3. Quy chuẩn toàn diện cho Bảng dữ liệu (Tables — 245 bảng)

* **VẤN ĐỀ 1: Duplicate 2 Title Table khi bảng ngắt trang (Repeat Header Rows Issue - Hình 1)**:
  * **Hiện trạng**: Ở các bảng dài bị tràn sang trang kế tiếp (như Table 36 mô phỏng Cửa sổ trượt dài 7 dòng), tiêu đề bảng (`Bước (R)`, `Nạp A_R`, `Tổng cửa sổ`...) xuất hiện 2 lần: một lần ở cuối trang trước và lặp lại ở đầu trang sau.
  * **Bản chất kỹ thuật**: Trong Word OpenXML, thẻ `<w:tblHeader/>` được thiết lập ở hàng 0 (`trPr`). Thuộc tính này có tính năng "Lặp lại hàng tiêu đề ở đầu mỗi trang mới" (*Repeat header row on every page*). 
  * **Phân tích & Đề xuất**:
    * **Nếu muốn bảng không lặp lại tiêu đề khi ngắt trang**: Tắt thuộc tính `tblHeader` (`remove(tblHeader)`), khi đó bảng ngắt trang sẽ tiếp tục các hàng dữ liệu bình thường mà không in lại dòng tiêu đề.
    * **Hoặc giữ liền khối bảng**: Bật tính năng tránh ngắt đôi bảng ngắn (`cantSplit` trên các hàng) để toàn bộ bảng nằm trọn trong 1 trang nếu trang còn đủ chỗ.

* **VẤN ĐỀ 2: Font size trong bảng không đều, mỗi hàng một cỡ chữ (Math Formula Font Size Issue - Hình 2)**:
  * **Hiện trạng**: Trong bảng mô phỏng (như Table 51), các ký tự văn bản thường (`Chỉ số`, `Mảng gốc`, `Tiền tố`) có cỡ chữ **12pt** (`w:sz val="24"`), nhưng các ký tự/số nằm trong công thức toán học Word Math (`m:oMath` như chữ $i$, $A[i]$, $P[i]$, số `0, 1, 2, 3...`) lại đang mang thuộc tính font size của công thức toán học (`w:sz val="19"` ~ **`9.5pt`** hoặc kế thừa mặc định từ Math font).
  * **Hậu quả**: Nhìn vào bảng thấy chữ to (`12pt`) nhưng số và ký hiệu toán học lại bé tí (`9.5pt`), làm các hàng trông khấp khểnh, không đồng bộ kích thước.
  * **Đề xuất xử lý triệt để**:
    * Quét toàn bộ các node công thức toán `m:oMath` bên trong tất cả các ô bảng.
    * Can thiệp trực tiếp vào thuộc tính XML `w:rPr` bên trong `m:r`: Đặt cứng `w:sz val="24"` (chuẩn **12pt**) cho toàn bộ các phần tử toán học trong bảng, đảm bảo chữ thường, chữ in hoa và số nguyên đều to đều chằn chặn **12pt** đồng nhất 100%.

* **VẤN ĐỀ 3: Bảng Sample Input / Output bị full width và lệch trái (Hình 3)**:
  * **Hiện trạng**: Bảng Sample IO (như Table 59) có chiều rộng đang bị đặt cứng full trang in ($16.5\text{ cm} = 7.920 - 9.360\text{ dxa}$) hoặc tràn sang 2 bên. Khi dữ liệu input ngắn, bảng quá rộng khiến phần text nằm sát mép trái, tạo ra khoảng trống mênh mông ở giữa và bên phải.
  * **Yêu cầu của người dùng**:
    * **Canh giữa bảng trên trang giấy** (Căn giữa Table Object `w:jc val="center"`, không phải center text bên trong ô).
    * **Không để width full trang**: Thu gọn kích thước bảng lại cho vừa vặn với nội dung (Compact Table Width: mỗi cột khoảng `2.500 – 3.200 dxa` ~ $4.5 - 5.5\text{ cm}$, tổng chiều rộng bảng chỉ khoảng $9 - 11\text{ cm}$).
    * Nội dung chữ bên trong ô Input / Output vẫn giữ **căn trái (`Left`)** để code/testcase thẳng hàng dọc, dễ đọc.

---

## 4. Phụ Lục & Phần Kèm Theo

### 4.1. Phụ lục A: Nền tảng C++
* Cả 2 Quyển đều có đầy đủ **Phụ lục A: Nền tảng C++** (toàn bộ 12 mục kiến thức nền tảng C++ dạng văn bản + bảng tra cứu cú pháp & quy trình giải bài).

### 4.2. Phụ lục B: Lời giải C++ Chuẩn Thi Đấu
* Mỗi quyển chứa trọn vẹn lời giải cho các bài tập thực hành thuộc quyển đó:
  * **Quyển 1**: Lời giải Bài 01 – Bài 12 (188 bài giải chi tiết).
  * **Quyển 2**: Lời giải Bài 13 – Bài 21 (135 bài giải chi tiết).

### 4.3. Mục lục tương tác (TOC)
* Đặt ở cuối mỗi quyển sách, có số trang chính xác và hỗ trợ Hyperlink.

---

## 5. Kết Quả Xử Lý 3 Vấn Đề Bảng (Completed Items)

1. **Khắc phục Duplicate Title Table (Hình 1)**:
   * [x] Đã xóa bỏ thuộc tính lặp lại header `<w:tblHeader/>` tại toàn bộ 245 bảng. Khi bảng ngắt trang, các dòng dữ liệu tiếp theo sẽ nối tiếp tự nhiên ở trang sau mà không in lại dòng tiêu đề thêm lần nào nữa.
   * [x] Đã bổ sung thuộc tính `<w:cantSplit/>` cho từng hàng để chống xé đôi chữ ngang trang.
2. **Đồng bộ Font Size 12pt cho toàn bộ công thức Math trong Bảng (Hình 2)**:
   * [x] Đã quét và ép cứng thuộc tính `w:sz val="24"` (chuẩn **12pt**) cho toàn bộ **1.803 cụm công thức toán học (`m:oMath`)** trong tất cả các ô bảng. Chữ cái, số nguyên và ký hiệu toán học giờ đây to đều chằn chặn 12pt đồng nhất 100%.
3. **Căn giữa Bảng Sample IO & Khối Nội Dung Input/Output (Hình 3)**:
   * [x] Toàn bộ **200 bảng Sample IO** đã được căn giữa trang in (`w:jc val="center"`).
   * [x] Chiều rộng bảng đã được thu gọn vừa vặn (mỗi cột `3.400 dxa` ~ $6.0\text{ cm}$, tổng bảng ~ $12\text{ cm}$), không còn bị bè ngang full trang.
   * [x] **Tiêu đề cột (`Đầu vào (Input)` và `Đầu ra (Output)`)**: Căn giữa ô 100% (**`Center`**).
   * [x] **Căn giữa khối nội dung Input/Output bằng thụt đầu dòng (Left Indent / Tab Stop)**:
     * Tuyệt đối **không dùng `text-align: center`** cho dữ liệu testcase để tránh các số bị lệch trục, răng cưa giữa các dòng.
     * Áp dụng tính toán khoảng thụt trái (`left_indent`) động theo độ rộng thực tế của testcase trong từng cột: Khối text giữ nguyên căn trái nội bộ (`Left-aligned`) để các cột số thẳng hàng dọc chằn chặn, nhưng cả khối được đẩy vào chính giữa ô một cách cân đối, đẹp mắt và chuyên nghiệp.
     * Font giữ nguyên chuẩn `Consolas 11pt`, các dòng phân tách rõ ràng.

---

## 6. Chuyển Đổi & Kiểm Duyệt Trực Quan Trọn Bộ Hình Ảnh Sang Light Theme (In Màu / Offset 300 DPI)

* **Vấn đề trước đây**: Toàn bộ các hình ảnh minh họa vector mang Dark Theme (nền đen/xanh đen `#0F172A`, độ sáng trung bình $27 - 40/255$). Khi in màu hoặc in đen trắng, nền tối gây bết mực, làm ướt giấy và chìm hoàn toàn các chi tiết văn bản. Ngoài ra, việc convert bằng regex tự động trước đây để lại nhiều khối chữ mờ (chữ xanh lá nhạt/mint trên nền trắng) và các khối nền tối còn sót lại.
* **Quy trình kiểm duyệt thủ công từng ảnh (Visually Inspected & Handcrafted)**:
  * [x] **Kiểm duyệt trực quan 12/12 ảnh minh họa**: Từng file SVG đã được tinh chỉnh tay, kết xuất sang PNG độ phân giải cao 2800px (300 DPI) bằng `@resvg/resvg-js-cli`, và được xem lại cẩn thận qua công cụ hiển thị hình ảnh trước khi đóng gói:
    1. `image1.png` (`bit_operations_simulation_vi`): Bit 0 xám, bit 1 xanh dương đậm, 4 phép toán AND/OR/XOR/NOT tương phản cao, badge pill sắc nét.
    2. `image2.png` (`sieve_eratosthenes_simulation_vi`): Bảng sàng Eratosthenes sạch sẽ; số nguyên tố đóng khung xanh ngọc `#ECFDF5`/`#065F46`, hợp số gạch chéo mờ `#F8FAFC`, badge bội số `#FEE2E2`/`#991B1B` tương phản hoàn hảo.
    3. `image3.png` (`bigint_vs_modulo_vi`): So sánh 2 trường phái; thẻ Modulo xanh dương nhạt `#F0F9FF`, thẻ BigInt vàng mơ `#FFFBEB`, chữ đậm `#1E293B`, highlight rõ ràng.
    4. `image4.png` (`recursion_structure_vi`): 2 trụ cột đệ quy; Base Case xanh ngọc đậm `#065F46`, Recursive Step xanh navy `#0369A1`, khung code nền trắng `#FFFFFF` sắc nét.
    5. `image5.png` (`recursion_taxonomy_vi`): Phân loại đệ quy; nhánh tuyến tính và nhánh rẽ nhánh màu pastel sáng, chữ body `#1E293B`, callout rõ nét.
    6. `image6.png` (`fibonacci_recursion_tree_vi`): Cây gọi hàm Fibonacci; nốt gốc $F(4)$ xanh, các nốt con $F(3), F(2)$ màu cam/tím pastel viền đậm, toàn bộ chữ số to rõ, thanh chú thích thanh thoát.
    7. `image7.png` (`dnc_model_vi`): Mô hình 3 pha Chia để trị; Bài toán gốc `#EFF6FF`, bài toán con `#F0F9FF`, đáp án con `#ECFDF5`, tổng hợp `#FFFBEB`, mũi tên phân nhánh và gộp có màu sắc phân biệt rõ.
    8. `image8.png` (`dnc_decision_tree_vi`): Cây quyết định chia để trị; nốt quyết định xanh `#0369A1`, nhánh KHÔNG viền đỏ `#991B1B`, nhánh CÓ viền xanh lá `#065F46`, các khối lá nổi bật.
    9. `image9.png` (`mergesort_tree_vi`): Cây phân rã & gộp Merge Sort; dãy đầu vào `#EFF6FF`, các tầng chia mảng viền xanh/xám rõ ràng, nốt lá Base Case xanh ngọc `#ECFDF5`, các tầng gộp màu vàng cam `#FFFBEB` với hệ thống mũi tên xanh chuyển pha nhịp nhàng, nhãn tầng bên trái gọn gàng không đè chữ.
    10. `image10.png` (`search_paradigms_bridge_vi`): Cầu nối kiến trúc đệ quy $\to$ không gian trạng thái $\to$ QHĐ; thẻ Đệ quy `#EFF6FF`, D&C `#F0F9FF`, State Space `#FAF5FF` (chứa 2 pill Quay lui & Nhánh cận), thẻ QHĐ `#ECFDF5` rộng rãi, chữ sắc nét, độ tương phản chuẩn WCAG AAA.
    11. `image11.png` (`state_space_tree_vi`): Cây không gian trạng thái; nốt GỐC tròn xanh, nhánh Cắt tỉa ràng buộc đỏ `#FEF2F2`/`#991B1B`, nhánh Cắt tỉa nhánh cận cam `#FFFBEB`/`#92400E`, nhánh Đi sâu khám phá xanh `#ECFDF5`/`#065F46`, chữ to rõ dễ đọc.
    12. `image12.png` (`state_dag_overlapping_vi`): So sánh Cây tìm kiếm vét cạn (trái, khung đỏ, nốt $E$ trùng lặp màu cam) với Đồ thị trạng thái DAG (phải, khung xanh, nốt $E$ hội tụ duy nhất); mũi tên hội tụ xanh rõ nét, chữ cảnh báo và kết luận nổi bật.
  * [x] **Cập nhật trực tiếp vào file Word Quyển 1 (`courses/cpp-bang-b/c++-level-1.docx`)**: Đã thay thế đồng bộ toàn bộ **12 hình ảnh minh họa** trong file Word, đảm bảo khi in offset hoặc in màu trên giấy A4 trang sách sáng đẹp, chữ và sơ đồ rõ nét 100%. Toàn bộ 3.343 đoạn văn và 245 bảng dữ liệu được bảo toàn nguyên vẹn.
