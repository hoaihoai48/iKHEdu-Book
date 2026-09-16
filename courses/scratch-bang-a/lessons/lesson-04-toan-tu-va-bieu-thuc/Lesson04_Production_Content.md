# BÀI 04: TOÁN TỬ VÀ BIỂU THỨC SỐ HỌC

**Khóa học:** Scratch — Tư duy Khối lệnh, Đồ họa & Thuật toán Thi đấu (Bảng A)  
**Mã bài học:** `SCA-L04` | **Chương 2:** Lập Trình Tính Toán Cơ Bản & Biến Số  
**Thời lượng khuyến nghị:** 2 – 3 buổi học (90 phút/buổi)  
**Ánh xạ chuẩn:** Tương đương Bài 02 của Python Bảng A (`courses/python-bang-a/lessons/lesson-02`)  

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

Sau khi hoàn thành bài học này, học sinh sẽ đạt được các chuẩn năng lực:
- **`LO-01` (4 Toán tử số học cơ bản):** Nắm vững cách sử dụng các khối toán tử tròn màu xanh lá cây: **Cộng `+`**, **Trừ `-`**, **Nhân `*`**, **Chia `/`** trong nhóm Các phép toán.
- **`LO-02` (Kỹ thuật lồng khối thay cho dấu ngoặc đơn):** Hiểu sâu sắc cơ chế tính toán trong Scratch: Scratch **không có phím gõ dấu ngoặc đơn `()`** trong biểu thức, mà dùng cơ chế **khối lồng khối (Nested blocks)**: khối nào nằm sâu nhất ở bên trong sẽ được tính toán trước.
- **`LO-03` (Quy tắc thứ tự ưu tiên PEMDAS):** Vận dụng đúng thứ tự ưu tiên các phép tính: Nhân chia trước, Cộng trừ sau. Biết cách lồng khối cộng vào trong khối nhân để biểu diễn phép tính có dấu ngoặc: $(A + B) \times 2$.
- **`LO-04` (Công thức chu vi & diện tích hình học):** Tự tin lập trình các bài toán hình học kinh điển trong đề thi Tin học trẻ:
  - Chu vi hình chữ nhật: `(dai + rong) * 2`
  - Diện tích hình chữ nhật: `dai * rong`
  - Diện tích hình tam giác: `(day * chieu_cao) / 2`
- **`LO-05` (Bẫy tràn số và số thập phân):** Nắm được cơ chế xử lý số học tự động của Scratch khi chia ra số lẻ thập phân.

---

## 2. Bốn Phép Toán Số Học Cơ Bản Trong Scratch

Trong nhóm **Các phép toán (Operators)** màu xanh lá cây, Scratch cung cấp 4 khối toán tử hình bầu dục:

![Bốn phép toán cơ bản](../../assets/rendered_blocks/l04_operators_vi.png)

| Toán tử Scratch | Ký hiệu toán học | Ý nghĩa | Ví dụ biểu thức | Kết quả |
|:---:|:---:|---|---|:---:|
| `(A) + (B)` | $+$ | Phép cộng | `(15) + (25)` | $40$ |
| `(A) - (B)` | $-$ | Phép trừ | `(100) - (35)` | $65$ |
| `(A) * (B)` | $\times$ | Phép nhân *(dùng dấu sao `*`)* | `(8) * (7)` | $56$ |
| `(A) / (B)` | $:$ hoặc $/$ | Phép chia *(dùng dấu gạch chéo `/`)* | `(30) / (4)` | $7.5$ |

> 💡 **Khối Ô Tròn (Reporter Block):**
> Các khối toán tử hình bầu dục này không đứng độc lập mà được **nhét lọt vào các ô tròn khác**, ví dụ nhét vào khối `đặt [tong] thành ((A) + (B))` hoặc `nói ((A) * (B))`.

---

## 3. Kỹ Thuật Lồng Khối Thay Thế Cho Dấu Ngoặc Đơn `()`

Trong toán học và Python, khi muốn tính tổng trước rồi mới nhân sau, ta dùng cặp dấu ngoặc đơn:
$$\text{Chu vi} = (\text{Dài} + \text{Rộng}) \times 2$$

Trong Scratch, bàn phím không thể gõ dấu ngoặc đơn vào biểu thức. Thay vào đó, Scratch sử dụng quy tắc hình học trực quan:
> **KHỐI NÀO NẰM LỌT BÊN TRONG SẼ ĐƯỢC TÍNH TOÁN TRƯỚC!**

### Các bước lồng khối tính Chu vi hình chữ nhật:
1. Lấy khối nhân: `( ) * ( )`. Gõ số `2` vào ô bên phải.
2. Lấy khối cộng: `( ) + ( )`. Nhét biến `dai` vào ô trái, biến `rong` vào ô phải $\implies$ ta được khối con `((dai) + (rong))`.
3. Kéo cả khối cộng này thả vào ô trống bên trái của khối nhân $\implies$ ta được biểu thức lồng hoàn chỉnh:
   $$((dai) + (rong)) * (2)$$

Máy tính Scratch sẽ tự động thực hiện phép cộng `dai + rong` trước, sau đó lấy kết quả đó nhân tiếp với $2$.

---

## 4. Bảng Tra Cứu Các Biểu Thức Hình Học Kinh Điển

| Bài toán | Công thức toán học | Cách ghép khối Scratch DSL | Minh họa khối lệnh |
|---|:---:|---|---|
| **Chu vi hình vuông** | $C = 4 \times a$ | `(4) * (a)` | `(4) * (canh)` |
| **Diện tích hình vuông** | $S = a^2 = a \times a$ | `(a) * (a)` | `(canh) * (canh)` |
| **Chu vi hình chữ nhật** | $C = (a + b) \times 2$ | `((a) + (b)) * (2)` | Lồng khối `+` vào khối `*` |
| **Diện tích hình chữ nhật** | $S = a \times b$ | `(a) * (b)` | `(dai) * (rong)` |
| **Diện tích tam giác** | $S = \dfrac{a \times h}{2}$ | `((a) * (h)) / (2)` | Lồng khối `*` vào khối `/` |
| **Tổng bình phương** | $a^2 + b^2$ | `((a) * (a)) + ((b) * (b))` | Khối `+` ôm 2 khối `*` |

---

## 5. Bảng Mô Phỏng Từng Bước (Dry Run Table)

Bài toán: Nhập chiều dài $A = 12$ và chiều rộng $B = 8$. Tính chu vi và diện tích hình chữ nhật:

| Bước thực thi | Khối lệnh Scratch Tiếng Việt | Biến `dai` | Biến `rong` | Biến `chu_vi` | Biến `dien_tich` | Bong bóng lời thoại |
|:---:|---|:---:|:---:|:---:|:---:|---|
| 1 | `đặt [dai] thành (12)` | $12$ | - | - | - | - |
| 2 | `đặt [rong] thành (8)` | $12$ | $8$ | - | - | - |
| 3 | `đặt [chu_vi] thành (((dai) + (rong)) * (2))` | $12$ | $8$ | **$40$** | - | - |
| 4 | `đặt [dien_tich] thành ((dai) * (rong))` | $12$ | $8$ | $40$ | **$96$** | - |
| 5 | `nói (kết hợp [Chu vi la: ] (chu_vi)) trong (2) giây` | $12$ | $8$ | $40$ | $96$ | `Chu vi la: 40` |
| 6 | `nói (kết hợp [Dien tich la: ] (dien_tich)) trong (2) giây` | $12$ | $8$ | $40$ | $96$ | `Dien tich la: 96` |

---

## 6. Tử Huyệt & Các Bẫy Lỗi Kinh Điển (Bug Traps)

> **Bẫy 1: Ghép nhầm thứ tự ưu tiên (Lỗi quên ngoặc)**
> - *Hiện tượng:* Cần tính `(A + B) * 2`, nhưng học sinh kéo khối `+` ra trước, rồi nhét `B * 2` vào sau thành: `(A) + ((B) * (2))`.
> - *Hậu quả:* Với $A = 10, B = 5$: Đúng ra $(10 + 5) \times 2 = 30$, nhưng máy tính tính $10 + (5 \times 2) = 20$!
> - *Khắc phục:* Xác định phép tính nào cần làm trước thì nhét khối đó vào ô trong cùng.

> **Bẫy 2: Chia cho số 0 (Division by Zero)**
> - *Hiện tượng:* Người dùng nhập mẫu số $B = 0$.
> - *Hậu quả:* Trong Scratch, phép chia `(A) / (0)` sẽ trả về giá trị đặc biệt là `Infinity` (Vô cực) chứ không báo lỗi đỏ như Python, làm hỏng các phép tính so sánh sau đó.
> - *Khắc phục:* Luôn kiểm tra mẫu số khác 0 trước khi chia.

> **Bẫy 3: Nhầm lẫn dấu nhân `*` và chữ x**
> - *Khắc phục:* Trong máy tính, dấu nhân luôn luôn là ký hiệu ngôi sao `*`, dấu chia là dấu gạch chéo `/`.

---

## 7. Concept Quiz (10 Câu Trắc Nghiệm Nhận Thức)

#### Câu 1 (Phép toán nhân chia)
Trong Scratch, phép nhân và phép chia được ký hiệu bằng các ký tự nào?
- A. `x` và `:`
- B. `*` và `/`
- C. `.` và `%`
- D. `^` và `div`
> **Đáp án:** B  
> **Giải thích:** Chuẩn máy tính quy định `*` là phép nhân và `/` là phép chia.

#### Câu 2 (Quy tắc lồng khối)
Trong một khối lệnh phức tạp có nhiều phép toán lồng nhau, khối nào sẽ được tính toán trước?
- A. Khối nằm ở ngoài cùng.
- B. Khối nằm lọt sâu nhất ở bên trong.
- C. Khối nào to hơn thì tính trước.
- D. Tính từ phải sang trái.
> **Đáp án:** B  
> **Giải thích:** Khối lồng bên trong đóng vai trò như dấu ngoặc đơn `()`, luôn được ưu tiên giải quyết trước.

#### Câu 3 (Tính chu vi hình chữ nhật)
Biểu thức Scratch nào sau đây tính ĐÚNG chu vi hình chữ nhật có chiều dài `dai` và chiều rộng `rong`?
- A. `(dai) + ((rong) * (2))`
- B. `((dai) + (rong)) * (2)`
- C. `(dai) * (rong)`
- D. `((dai) * (2)) + (rong)`
> **Đáp án:** B  
> **Giải thích:** Cần cộng dài với rộng trước rồi mới nhân 2.

#### Câu 4 (Giá trị biểu thức)
Khối lệnh `((10) + (5)) * ((8) - (2))` sẽ cho kết quả là bao nhiêu?
- A. $40$
- B. $90$
- C. $70$
- D. $50$
> **Đáp án:** B  
> **Giải thích:** $(10 + 5) \times (8 - 2) = 15 \times 6 = 90$.

#### Câu 5 (Tính diện tích tam giác)
Cho đáy tam giác là $10$ và chiều cao là $6$. Biểu thức `((10) * (6)) / (2)` cho kết quả là:
- A. $60$
- B. $30$
- C. $15$
- D. $20$
> **Đáp án:** B  
> **Giải thích:** $(10 \times 6) / 2 = 60 / 2 = 30$.

#### Câu 6 (Kết quả số thập phân)
Trong Scratch, phép tính `(7) / (2)` sẽ trả về kết quả là:
- A. $3$
- B. $3.5$
- C. $4$
- D. Báo lỗi không chia hết
> **Đáp án:** B  
> **Giải thích:** Toán tử `/` trong Scratch tự động tính toán ra số thập phân chính xác ($3.5$).

#### Câu 7 (Lũy thừa bậc hai)
Để tính bình phương của biến $X$ ($X^2$), trong Scratch ta dùng khối lệnh nào?
- A. `(X) + (X)`
- B. `(X) * (X)`
- C. `(X) ^ (2)`
- D. `(2) * (X)`
> **Đáp án:** B  
> **Giải thích:** Bình phương là nhân một số với chính nó: `X * X`.

#### Câu 8 (Bẫy quên ngoặc)
Nếu viết nhầm thành `(10) + ((5) * (2))` thay vì `((10) + (5)) * (2)`, kết quả sẽ bị sai lệch bao nhiêu đơn vị?
- A. Bị giảm đi 10 đơn vị (từ 30 xuống 20).
- B. Bị tăng thêm 10 đơn vị.
- C. Không thay đổi kết quả.
- D. Bị giảm đi 5 đơn vị.
> **Đáp án:** A  
> **Giải thích:** $10 + (5 \times 2) = 20$, trong khi $(10 + 5) \times 2 = 30$. Sai lệch đúng 10 đơn vị.

#### Câu 9 (Màu sắc nhóm lệnh)
Các khối toán tử `+`, `-`, `*`, `/` nằm trong nhóm lệnh nào và có màu gì?
- A. Nhóm Chuyển động (Màu xanh dương)
- B. Nhóm Các phép toán (Màu xanh lá cây)
- C. Nhóm Các biến số (Màu cam đậm)
- D. Nhóm Cảm biến (Màu xanh lơ)
> **Đáp án:** B  
> **Giải thích:** Nhóm Các phép toán (Operators) mang màu xanh lá cây đặc trưng.

#### Câu 10 (Ghép nhãn và kết quả)
Để in dòng chữ `Dien tich: 48`, khối lệnh chuẩn xác là:
- A. `nói [Dien tich: 48]`
- B. `nói (kết hợp [Dien tich: ] (dien_tich))`
- C. `nói (dien_tich)`
- D. `nói [Dien tich:]`
> **Đáp án:** B  
> **Giải thích:** Dùng `kết hợp` lồng biến `dien_tich` vào sau nhãn văn bản có chứa khoảng trắng.

---

## 8. Tóm Tắt & Hướng Dẫn Thực Hành

> **GHI NHỚ CỐT LÕI:**
> 1. Nhân chia trước, cộng trừ sau; muốn tính trước thì **lồng khối vào bên trong**.
> 2. Ký hiệu: Nhân là `*`, Chia là `/`.
> 3. Chu vi hình chữ nhật: `((dai) + (rong)) * (2)`.
> 4. Diện tích hình chữ nhật: `(dai) * (rong)`.

👉 **Tiếp theo:** Mở file [`Bai_Tap.md`](file:///Users/vu/Developer/ikhEdu_lessons/courses/scratch-bang-a/lessons/lesson-04-toan-tu-va-bieu-thuc/Bai_Tap.md) để luyện tập trọn bộ $36$ bài toán thực hành từ `sca_l04_p01` đến `sca_l04_p36`!
