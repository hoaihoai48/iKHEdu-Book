# BÀI 05: PHÉP CHIA NGUYÊN, CHIA DƯ VÀ LUỸ THỪA

**Khóa học:** Scratch — Tư duy Khối lệnh, Đồ họa & Thuật toán Thi đấu (Bảng A)  
**Mã bài học:** `SCA-L05` | **Chương 2:** Lập Trình Tính Toán Cơ Bản & Biến Số  
**Thời lượng khuyến nghị:** 2 – 3 buổi học (90 phút/buổi)  
**Ánh xạ chuẩn:** Tương đương Bài 03 của Python Bảng A (`courses/python-bang-a/lessons/lesson-03`)  

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

Sau khi hoàn thành bài học này, học sinh sẽ đạt được các chuẩn năng lực:
- **`LO-01` (Phép chia lấy phần dư `mod`):** Nắm vững khối toán tử `((A) mod (B))` màu xanh lá cây; hiểu rõ bản chất số dư trong phép chia số nguyên (kết quả luôn trong đoạn $[0, B - 1]$).
- **`LO-02` (Phép chia lấy phần nguyên `floor`):** Hiểu rằng Scratch không có khối `//` riêng; để chia nguyên ta dùng kết hợp hàm toán học: `([làm tròn xuống v] của ((A) / (B)))`.
- **`LO-03` (Bất biến phép chia số học):** Nắm vững công thức bất biến: $A = (\text{thương nguyên} \times B) + \text{số dư}$.
- **`LO-04` (Nhận diện chẵn lẻ & Tính chia hết):**
  - $N$ là số chẵn khi `((N) mod (2)) = 0`.
  - $N$ là số lẻ khi `((N) mod (2)) = 1`.
  - $A$ chia hết cho $B$ khi `((A) mod (B)) = 0`.
- **`LO-05` (Ứng dụng thực tế kinh điển):** Giải quyết thành thạo các bài toán chia kẹo, xếp hàng, đổi giây sang phút-giây, giờ sang ngày-giờ và chu kỳ bánh xe/kim đồng hồ.
- **`LO-06` (Khái niệm Luỹ thừa):** Hiểu cách tính luỹ thừa cơ bản $A^2 = A \times A$, $A^3 = A \times A \times A$ hoặc thông qua vòng lặp nhân dồn.

---

## 2. Bản Chất Phép Chia Nguyên Và Chia Dư Trong Scratch

Khác với Python có sẵn toán tử `//` (chia nguyên) và `%` (chia dư), trong Scratch 3.0:

![Minh họa khối lệnh chia nguyên và chia dư](../../assets/rendered_blocks/l05_div_mod_vi.png)

### 2.1. Phép chia lấy phần dư: Khối `mod`
- Trong nhóm **Các phép toán (Operators)**, Scratch có khối tròn: `((A) mod (B))`.
- Ví dụ:
  - `(17) mod (5)` trả về **`2`** (vì $17 = 5 \times 3 + 2$).
  - `(20) mod (4)` trả về **`0`** (vì $20$ chia hết cho $4$).
  - `(7) mod (2)` trả về **`1`** (số lẻ chia cho 2 luôn dư 1).
  - `(5) mod (10)` trả về **`5`** (số bị chia nhỏ hơn số chia).

### 2.2. Phép chia lấy phần nguyên: Khối `làm tròn xuống của ((A) / (B))`
- Scratch cung cấp khối toán học nâng cao: `([làm tròn xuống v] của ())`.
- Để tính phần nguyên của $A : B$, ta đặt khối chia `(A) / (B)` vào bên trong:
  $$\text{thuong\_nguyen} = \text{[làm tròn xuống]} \text{ của } ((A) / (B))$$
- Ví dụ:
  - $17 / 5 = 3.4 \implies$ làm tròn xuống được **`3`**.
  - $29 / 10 = 2.9 \implies$ làm tròn xuống được **`2`**.

---

## 3. Bảng Tra Cứu Các Biểu Thức Tính Toán Thời Gian & Đơn Vị

| Tình huống thực tế | Dữ liệu đầu vào | Giá trị phần nguyên | Giá trị phần dư | Khối lệnh Scratch tương ứng |
|---|:---:|:---:|:---:|---|
| **Đổi giây $\to$ phút và giây** | $T$ giây | `phut = floor(T / 60)` | `giay = T mod 60` | `([làm tròn xuống] (T / 60))`<br>`(T mod 60)` |
| **Đổi phút $\to$ giờ và phút** | $M$ phút | `gio = floor(M / 60)` | `phut = M mod 60` | `([làm tròn xuống] (M / 60))`<br>`(M mod 60)` |
| **Đổi giờ $\to$ ngày và giờ** | $H$ giờ | `ngay = floor(H / 24)` | `gio = H mod 24` | `([làm tròn xuống] (H / 24))`<br>`(H mod 24)` |
| **Chia đều bánh kẹo** | $N$ kẹo, $K$ bạn | Số kẹo mỗi bạn | Số kẹo còn thừa | `floor(N / K)` kẹo mỗi bạn<br>`N mod K` kẹo thừa |
| **Xếp học sinh lên xe buýt** | $N$ bạn, xe chở $S$ | Số chuyến xe chở đầy | Số bạn chuyến cuối | `floor(N / S)` chuyến đầy<br>`N mod S` bạn lẻ |

---

## 4. Mô Phỏng Chạy Tay Từng Bước (Dry Run Table)

**Bài toán:** Bạn An có $T = 145$ giây. Hãy đổi sang số phút và số giây lẻ.

| Bước | Khối lệnh Scratch Tiếng Việt | Biến `T` | Biến `phut` | Biến `giay` | Lời thoại Mèo hiển thị |
|:---:|---|:---:|:---:|:---:|---|
| 1 | `đặt [T v] thành (145)` | $145$ | - | - | - |
| 2 | `đặt [phut v] thành ([làm tròn xuống] của ((T) / (60)))` | $145$ | **`2`** | - | *(145 / 60 = 2.416 $\to$ lấy 2)* |
| 3 | `đặt [giay v] thành ((T) mod (60))` | $145$ | $2$ | **`25`** | *(145 - 2*60 = 25)* |
| 4 | `nói (kết hợp (phut) (kết hợp [ phut ] (kết hợp (giay) [ giay])))` | $145$ | $2$ | $25$ | **`2 phut 25 giay`** |

---

## 5. Bẫy Lỗi Kinh Điển Khi Lập Trình (Bug Traps)

> **Bẫy 1: Dùng nhầm khối `làm tròn` (Round) thay vì `làm tròn xuống` (Floor)**
> - *Hiện tượng:* Chọn khối `làm tròn của ((A) / (B))` mặc định.
> - *Hậu quả:* Nếu $A = 18, B = 5 \implies 18 / 5 = 3.6$. Khối `làm tròn` sẽ làm tròn lên thành `4`! Thực tế 18 cái kẹo chia cho 5 bạn thì mỗi bạn chỉ được trọn vẹn `3` cái kẹo.
> - *Cách sửa:* Bắt buộc chọn đúng menu tam giác: **`làm tròn xuống` (floor)**.

> **Bẫy 2: Quên kiểm tra chia cho 0**
> - *Hiện tượng:* Nhập mẫu số $B = 0$ vào khối `mod`.
> - *Hậu quả:* Trong Scratch, `(A) mod (0)` sẽ trả về giá trị `NaN` (Not a Number - Không phải số), khiến nhân vật nói linh tinh hoặc đứng im.
> - *Cách sửa:* Đảm bảo số chia luôn lớn hơn 0.

> **Bẫy 3: Ghép chuỗi dính liền số và chữ**
> - *Hiện tượng:* Dùng khối `kết hợp (phut) [phut]` mà không có dấu cách.
> - *Hậu quả:* Màn hình hiện `2phut` thay vì `2 phut`.

---

## 6. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Khối `(19) mod (4)` trả về giá trị nào?**
   - A. `4`
   - B. `3` *(Đáp án đúng: vì 19 = 4 * 4 + 3)*
   - C. `2`
   - D. `1`

2. **Muốn kiểm tra số $X$ có phải là số chẵn hay không, ta so sánh:**
   - A. `((X) mod (2)) = 0` *(Đáp án đúng)*
   - B. `((X) mod (2)) = 1`
   - C. `((X) / (2)) = 0`
   - D. `([làm tròn] (X)) = 2`

3. **Để tính số xe 4 chỗ ít nhất chở hết $N$ người (kể cả người lẻ), công thức chuẩn là:**
   - A. `[làm tròn xuống] (N / 4)`
   - B. `[làm tròn lên] (N / 4)` *(Đáp án đúng: khối ceiling hoặc cộng thêm 3 trước khi chia)*
   - C. `N mod 4`
   - D. `(N + 4) / 4`

4. **Biểu thức `(25) mod (5)` có giá trị là:**
   - A. `5`
   - B. `1`
   - C. `0` *(Đáp án đúng: phép chia hết số dư bằng 0)*
   - D. `25`

5. **Khi tính `(8) mod (12)` kết quả là bao nhiêu?**
   - A. `0`
   - B. `8` *(Đáp án đúng: vì 8 chia 12 được 0 dư 8)*
   - C. `4`
   - D. `12`

6. **Trong Scratch, khối nào tương đương với phép chia `//` của Python?**
   - A. `[làm tròn] của ((A) / (B))`
   - B. `[làm tròn xuống] của ((A) / (B))` *(Đáp án đúng)*
   - C. `((A) mod (B))`
   - D. `((A) / (B))`

7. **Số $A$ chia hết cho $5$ khi:**
   - A. `(A mod 5) = 1`
   - B. `(A mod 5) = 0` *(Đáp án đúng)*
   - C. `(A / 5) = 0`
   - D. `(A * 5) = 0`

8. **Biểu thức tính $A^2$ trong Scratch là:**
   - A. `(A) ^ (2)`
   - B. `(A) ** (2)`
   - C. `(A) * (A)` *(Đáp án đúng)*
   - D. `(A) + (A)`

9. **Nếu một sự kiện lặp lại sau mỗi 7 ngày, để tìm thứ trong tuần ta dùng toán tử:**
   - A. `+`
   - B. `/`
   - C. `mod 7` *(Đáp án đúng)*
   - D. `* 7`

10. **Khi chia $N = 37$ học sinh thành các tổ 5 bạn, số bạn bị dư ra là:**
    - A. `7`
    - B. `2` *(Đáp án đúng: 37 mod 5 = 2)*
    - C. `5`
    - D. `3`
