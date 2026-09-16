# BÀI 03: LỆNH XUẤT NHẬP, BIẾN SỐ VÀ KIỂU DỮ LIỆU

**Khóa học:** Scratch — Tư duy Khối lệnh, Đồ họa & Thuật toán Thi đấu (Bảng A)  
**Mã bài học:** `SCA-L03` | **Chương 2:** Lập Trình Tính Toán Cơ Bản & Biến Số  
**Thời lượng khuyến nghị:** 2 buổi học (90 phút/buổi)  
**Ánh xạ chuẩn:** Tương đương Bài 01 của Python Bảng A (`courses/python-bang-a/lessons/lesson-01`)  

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

Sau khi hoàn thành bài học này, học sinh sẽ đạt được các chuẩn năng lực:
- **`LO-01` (Luồng dữ liệu I/O):** Hiểu rõ luồng xử lý thông tin $3$ bước của mọi bài toán tin học: **Đầu vào (`hỏi và đợi`) $\longrightarrow$ Xử lý (`đặt biến thành`) $\longrightarrow$ Đầu ra (`nói`)**.
- **`LO-02` (Biến số & Bản chất bộ nhớ):** Hiểu biến số như một "chiếc hộp dán nhãn" trong bộ nhớ RAM dùng để cất giữ một giá trị (số hoặc chữ), giá trị trong hộp có thể thay đổi trong suốt quá trình chạy.
- **`LO-03` (Bẫy tử huyệt `câu trả lời`):** Nhận thức sâu sắc rằng biến `câu trả lời` (`answer`) là biến tạm của hệ thống; mỗi khi hỏi câu mới thì câu trả lời cũ sẽ **bị xóa sạch ngay lập tức**, do đó bắt buộc phải sao lưu vào biến riêng ngay sau khi hỏi.
- **`LO-04` (Kỹ thuật ghép nối chuỗi `kết hợp`):** Thành thạo khối `kết hợp` (`join`) trong nhóm Các phép toán để in nhãn kèm kết quả, tránh bẫy dính chữ (`join [Tong la: ] (tong)`).
- **`LO-05` (Thuật toán hoán đổi 2 biến):** Vận dụng thuật toán "chiếc cốc phụ" (biến trung gian `tam`) để đổi chỗ giá trị của $2$ biến số $A$ và $B$.

---

## 2. Bản Chất Chương Trình Máy Tính & Luồng Dữ Liệu I/O

Mọi chương trình máy tính phục vụ thi đấu Tin học trẻ Bảng A đều vận hành nghiêm ngặt theo **luồng dữ liệu 3 bước khép kín**:

```text
  [ BÀN PHÍM ] ──(hỏi và đợi)──► [ CÂU TRẢ LỜI ] ──(đặt biến)──► [ BIẾN SỐ A, B ]
                                                                        │
                                                                   (Tính toán)
                                                                        ▼
  [ MÀN HÌNH ] ◄──────(nói)────── [ KẾT HỢP ] ◄────────────── [ BIẾN KẾT QUẢ ]
```

1. **Đầu vào (Input):** Chú Mèo Scratch đặt câu hỏi cho người dùng nhập từ bàn phím thông qua khối màu xanh lơ: **`hỏi () và đợi`**.
2. **Lưu trữ & Xử lý (Process):** Dữ liệu người dùng gõ vào được nạp vào biến tạm **`câu trả lời`**. Ta dùng khối màu cam đậm **`đặt [biến] thành (câu trả lời)`** để cất giữ an toàn vào chiếc hộp biến số.
3. **Đầu ra (Output):** Sau khi tính toán, chú Mèo hiển thị kết quả bằng bong bóng lời thoại thông qua khối màu tím: **`nói ()`**.

---

## 3. Lệnh Nhập Dữ Liệu: Khối `hỏi () và đợi` & Tử Huyệt `câu trả lời`

### 3.1. Cú pháp nhập dữ liệu
Trong nhóm **Cảm biến (Sensing)** màu xanh lơ:

![Khối lệnh hỏi và đợi](../../assets/rendered_blocks/l03_block_ask_vi.png)

Khi khối lệnh này chạy:
- Chú Mèo Scratch sẽ hiện một khung nhập chữ nhật ở dưới đáy sân khấu.
- Chương trình tạm dừng (đợi) cho đến khi người dùng gõ xong dữ liệu và bấm phím **Enter** (hoặc bấm dấu tick xanh ✔).
- Nội dung người dùng vừa nhập được tự động lưu vào khối tròn màu xanh lơ mang tên: **`câu trả lời`**.

---

### 3.2. Cất giữ dữ liệu vào Biến số (Variables)
Để dữ liệu không bị thất lạc, ta tạo biến số trong nhóm **Các biến số** màu cam đậm:

![Khối đặt biến thành câu trả lời](../../assets/rendered_blocks/l03_block_set_vi.png)

*Quy trình chuẩn khi nhập 2 số $A$ và $B$:*
1. 🔵 **Hỏi [Nhập số thứ nhất A:] và đợi**
2. 🟠 **Đặt [A] thành (câu trả lời)** *(Cất ngay vào hộp A)*
3. 🔵 **Hỏi [Nhập số thứ hai B:] và đợi**
4. 🟠 **Đặt [B] thành (câu trả lời)** *(Cất ngay vào hộp B)*

> ⚠️ **TỬ HUYỆT BẬC NHẤT CỦA HỌC SINH MỚI HỌC SCRATCH:**
> Biến `câu trả lời` chỉ giữ được kết quả của **câu hỏi gần nhất**.  
> Nếu bạn hỏi câu 1, rồi hỏi tiếp câu 2 mà **quên đặt vào biến $A$**, thì khi hỏi câu 2 xong, giá trị của câu 1 sẽ **BỊ XÓA VĨNH VIỄN** và bị đè bởi giá trị của câu 2!

---

## 4. Lệnh Xuất Dữ Liệu: Khối `nói ()` & Bẫy Ghép Chuỗi `kết hợp`

Trong nhóm **Hiển thị (Looks)** màu tím:
- 🟣 **`nói (nội dung)`**: Hiện bong bóng lời thoại liên tục trên đầu nhân vật.
- 🟣 **`nói (nội dung) trong (2) giây`**: Hiện lời thoại trong đúng 2 giây rồi tự động biến mất.

### 4.1. Xuất một kết quả đơn giản
- Để in một dòng chữ chào mừng: 🟣 `nói [Xin chao cac ban! Toi la Scratch.]`
- Để in trực tiếp một con số: 🟣 `nói (2026)`
- Để in kết quả của biến: 🟣 `nói (A)`

### 4.2. In nhãn kèm kết quả: Khối `kết hợp` (`join`)
Khi cần in cả chữ và số (ví dụ: `Tổng là: 40`), trong Scratch ta không dùng dấu phẩy `,` như Python mà phải dùng khối **`kết hợp () ()`** trong nhóm Các phép toán màu xanh lá:

![Khối nói kết hợp chuỗi](../../assets/rendered_blocks/l03_block_say_join_vi.png)

> 💡 **Bẫy dính chữ (Spacing Trap):**
> Khối `kết hợp [Tong la:][(40)]` sẽ dính liền thành `Tong la:40`.  
> Muốn đẹp mắt và chuẩn chỉnh, học sinh **bắt buộc phải gõ thêm một dấu cách sau dấu hai chấm**: `[Tổng là: ]`.

---

## 5. Thuật Toán Hoán Đổi Vị Trí Hai Biến Số ($A \longleftrightarrow B$)

### 5.1. Vấn đề thực tế
Giả sử trên tay trái bạn cầm chiếc cốc đựng nước màu xanh ($A$), tay phải cầm chiếc cốc đựng nước màu đỏ ($B$). Bạn muốn đổi nước giữa hai chiếc cốc cho nhau. Bạn có thể đổ trực tiếp từ cốc $A$ sang cốc $B$ không?  
$\implies$ Không thể, vì nước sẽ bị hòa lẫn vào nhau làm mất màu ban đầu!

### 5.2. Giải pháp: Sử dụng chiếc cốc phụ (Biến tạm `tam`)
Để hoán đổi, ta cần mượn một chiếc cốc thứ ba rỗng mang tên **`tam`**:
1. Đổ nước từ cốc $A$ sang cốc `tam` $\implies$ Cốc $A$ rỗng, cốc `tam` giữ nước màu xanh.
2. Đổ nước từ cốc $B$ sang cốc $A$ $\implies$ Cốc $A$ nhận nước màu đỏ.
3. Đổ nước từ cốc `tam` sang cốc $B$ $\implies$ Cốc $B$ nhận nước màu xanh.

### 5.3. Cụm khối lệnh hoán đổi chuẩn trong Scratch:

![Khối lệnh hoán đổi 2 biến](../../assets/rendered_blocks/l03_block_swap_vi.png)

*Cấu trúc 3 bước vàng:*
1. 🟠 **Đặt [tam] thành (A)**
2. 🟠 **Đặt [A] thành (B)**
3. 🟠 **Đặt [B] thành (tam)**

---

## 6. Bảng Mô Phỏng Từng Bước (Dry Run Table)

Giả sử người dùng nhập $A = 10$ và $B = 99$. Bảng trace biến số khi thực hiện thuật toán hoán đổi:

| Bước thực thi | Lệnh khối Scratch | Giá trị biến $A$ | Giá trị biến $B$ | Giá trị biến `tam` | Trạng thái ghi nhận |
|:---:|---|:---:|:---:|:---:|---|
| **Khởi tạo** | Người dùng nhập | $10$ | $99$ | *(chưa có)* | Ban đầu $A=10, B=99$ |
| **Bước 1** | `đặt [tam] thành (A)` | $10$ | $99$ | **$10$** | Biến `tam` cất giữ giá trị ban đầu của $A$ |
| **Bước 2** | `đặt [A] thành (B)` | **$99$** | $99$ | $10$ | Gán giá trị của $B$ sang $A$ ($A$ đổi thành $99$) |
| **Bước 3** | `đặt [B] thành (tam)` | $99$ | **$10$** | $10$ | Lấy giá trị từ `tam` gán sang $B$ ($B$ đổi thành $10$) |
| **Kết quả** | `nói (kết hợp (A) (B))` | **$99$** | **$10$** | $10$ | Hai biến đã tráo đổi thành công! |

---

## 7. Tử Huyệt & Các Bẫy Lỗi Kinh Điển (Bug Traps)

> **Bẫy 1: Hỏi liên tiếp mà không lưu `câu trả lời`**
> - *Hiện tượng:* Học sinh kéo 2 khối `hỏi [Nhập A:] và đợi` rồi `hỏi [Nhập B:] và đợi` liền nhau, sau đó mới `đặt [A] thành (câu trả lời)` và `đặt [B] thành (câu trả lời)`.
> - *Hậu quả:* Cả hai biến $A$ và $B$ đều mang giá trị của số thứ hai! Số thứ nhất đã bị ghi đè mất tích.
> - *Khắc phục:* Quy tắc bất di bất dịch: **1 câu hỏi $\longrightarrow$ 1 lệnh cất vào biến ngay lập tức**.

> **Bẫy 2: Hoán đổi sai không dùng biến phụ**
> - *Hiện tượng:* Học sinh viết: `đặt [A] thành (B)` rồi viết tiếp `đặt [B] thành (A)`.
> - *Hậu quả:* Sau lệnh thứ nhất, $A$ đã thành $B$. Đến lệnh thứ hai, $B$ lại gán bằng $A$ (vốn đã là $B$) $\implies$ Cả hai biến cùng mang giá trị của $B$!
> - *Khắc phục:* Bắt buộc dùng biến thứ ba `tam`.

> **Bẫy 3: Dùng 2 lệnh `nói ()` liên tiếp để in 2 số**
> - *Hiện tượng:* Muốn in $A$ và $B$, học sinh kéo: `nói (A)` rồi ngay dưới là `nói (B)`.
> - *Hậu quả:* Màn hình chớp qua số $A$ trong $0.01$ giây rồi chỉ hiện mỗi số $B$. Người xem không kịp nhìn thấy số $A$.
> - *Khắc phục:* Dùng khối `kết hợp (A) (kết hợp [ ] (B))` để in cả hai số cùng lúc trên 1 bong bóng, hoặc dùng `nói (A) trong (2) giây` rồi mới `nói (B) trong (2) giây`.

---

## 8. Concept Quiz (10 Câu Trắc Nghiệm Nhận Thức)

#### Câu 1 (Chức năng nhập liệu)
Trong Scratch, khối lệnh nào được dùng để nhận dữ liệu gõ vào từ bàn phím của người dùng?
- A. `nói [] và đợi`
- B. `hỏi [] và đợi`
- C. `đi tới điểm x: y:`
- D. `thay đổi x một lượng`
> **Đáp án:** B  
> **Giải thích:** Khối `hỏi [] và đợi` trong nhóm Cảm biến mở khung nhập liệu từ bàn phím.

#### Câu 2 (Vị trí lưu trữ dữ liệu vừa nhập)
Sau khi người dùng gõ số $100$ và bấm Enter, số $100$ đó ngay lập tức được cất giữ ở đâu?
- A. Trong khối `kích thước`.
- B. Trong biến `câu trả lời`.
- C. Trong khối `tọa độ x`.
- D. Bị biến mất khỏi chương trình.
> **Đáp án:** B  
> **Giải thích:** Khối `câu trả lời` tự động lưu giữ giá trị của lần nhập gần nhất.

#### Câu 3 (Bản chất biến số)
Một biến số trong lập trình Scratch có thể được hiểu tương đương với hình ảnh nào trong thực tế?
- A. Một bức tranh treo tường không bao giờ đổi.
- B. Một chiếc hộp có dán nhãn tên, bên trong chứa một giá trị có thể lấy ra hoặc thay thế.
- C. Một chiếc bút chì màu.
- D. Một phím bấm trên bàn phím.
> **Đáp án:** B  
> **Giải thích:** Biến số là ô nhớ được đặt tên dùng để lưu trữ dữ liệu có thể thay đổi.

#### Câu 4 (Tử huyệt ghi đè dữ liệu)
Đoạn lệnh sau đây sẽ cho kết quả biến $A$ bằng bao nhiêu nếu người dùng gõ lần 1 là $5$ và lần 2 là $20$?
```text
hỏi [Nhập số thứ nhất:] và đợi
hỏi [Nhập số thứ hai:] và đợi
đặt [A] thành (câu trả lời)
```
- A. $5$
- B. $20$
- C. $25$
- D. $0$
> **Đáp án:** B  
> **Giải thích:** Khi câu hỏi thứ hai được thực hiện, `câu trả lời` đã bị đổi thành $20$. Giá trị $5$ bị xóa mất vì chưa kịp cất vào biến $A$.

#### Câu 5 (Bẫy khoảng trắng trong ghép chuỗi)
Khối lệnh `kết hợp [Diem so:][10]` sẽ hiển thị trên màn hình dòng chữ nào?
- A. `Diem so: 10`
- B. `Diem so:10`
- C. `Diem so`
- D. `10`
> **Đáp án:** B  
> **Giải thích:** Khối `kết hợp` nối dính chặt 2 chuỗi ký tự lại với nhau. Nếu không có dấu cách trong ô thứ nhất, chữ sẽ bị dính liền: `Diem so:10`.

#### Câu 6 (Thuật toán hoán đổi biến)
Để tráo đổi giá trị của 2 biến $A$ và $B$, ta bắt buộc phải sử dụng thêm điều gì?
- A. Phải vẽ thêm một nhân vật mới.
- B. Phải sử dụng thêm một biến tạm trung gian (ví dụ `tam`).
- C. Phải dùng khối lệnh bút vẽ màu đỏ.
- D. Phải xóa toàn bộ sân khấu.
> **Đáp án:** B  
> **Giải thích:** Cần một biến trung gian để lưu giữ giá trị của biến thứ nhất trước khi bị biến thứ hai ghi đè.

#### Câu 7 (Đổi chỗ hai biến)
Cho $A = 15, B = 40$. Sau khi thực hiện 3 lệnh sau, giá trị của $A$ và $B$ lần lượt là:
```text
đặt [tam] thành (A)
đặt [A] thành (B)
đặt [B] thành (tam)
```
- A. $A = 15, B = 40$
- B. $A = 40, B = 40$
- C. $A = 40, B = 15$
- D. $A = 15, B = 15$
> **Đáp án:** C  
> **Giải thích:** Thuật toán hoán đổi đã tráo đổi vị trí của $A$ và $B$.

#### Câu 8 (Hiển thị nhiều thông điệp)
Nếu muốn chú Mèo đọc lần lượt câu chào 1, rồi đến câu chào 2 cho người xem kịp đọc, ta nên dùng khối lệnh nào?
- A. Dùng 2 khối `nói []` liên tiếp không có thời gian.
- B. Dùng 2 khối `nói [] trong (2) giây` liên tiếp.
- C. Dùng khối `ẩn`.
- D. Dùng khối `dừng lại tất cả`.
> **Đáp án:** B  
> **Giải thích:** Lệnh `nói trong (2) giây` tạm dừng đủ lâu để người dùng đọc kịp trước khi chuyển sang câu tiếp theo.

#### Câu 9 (Nhận biết khối lệnh)
Khối lệnh nào dưới đây thuộc nhóm Các biến số (màu cam đậm)?
- A. `đặt [x] thành (0)`
- B. `di chuyển (10) bước`
- C. `chọn màu vẽ`
- D. `hỏi và đợi`
> **Đáp án:** A  
> **Giải thích:** Khối `đặt biến thành` là lệnh thao tác biến số cơ bản của Scratch.

#### Câu 10 (Ứng dụng thực tế)
Trong các bài thi Tin học trẻ Bảng A, khi đề bài cho: *"Nhập vào hai số nguyên A và B trên 2 dòng..."*, bước lập trình đầu tiên của em là gì?
- A. Bật công cụ bút vẽ và tô màu sân khấu.
- B. Tạo 2 biến số mang tên $A$ và $B$, sau đó viết 2 cặp lệnh `hỏi và đợi` kèm `đặt biến thành câu trả lời`.
- C. Đổi trang phục cho chú Mèo.
- D. Bấm phím cách liên tục.
> **Đáp án:** B  
> **Giải thích:** Tạo biến và nạp dữ liệu đầu vào là bước khởi đầu tiên quyết của mọi bài toán thuật toán.

---

## 9. Tóm Tắt & Hướng Dẫn Thực Hành

> **GHI NHỚ CỐT LÕI:**
> 1. Nhập liệu chuẩn: 🔵 **hỏi [] và đợi** $\longrightarrow$ 🟠 **đặt [biến] thành (câu trả lời)**.
> 2. Xuất dữ liệu kèm nhãn: 🟣 **nói (kết hợp [Nhãn: ] (biến))**.
> 3. Hoán đổi $2$ biến: Mượn biến phụ `tam`: `tam = A` $\to$ `A = B` $\to$ `B = tam`.

👉 **Tiếp theo:** Mở file [`Bai_Tap.md`](file:///Users/vu/Developer/ikhEdu_lessons/courses/scratch-bang-a/lessons/lesson-03-lenh-xuat-nhap-bien-so-kieu-du-lieu/Bai_Tap.md) để thực hành $8$ bài tập lập trình tính toán và nhập xuất dữ liệu từ `sca_l03_p01` đến `sca_l03_p08` (tương ứng trực tiếp với kho bài `pya_l01_*` của Python Bảng A)!
