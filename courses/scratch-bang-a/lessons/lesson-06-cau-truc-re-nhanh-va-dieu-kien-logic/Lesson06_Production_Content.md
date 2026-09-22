# Bài 06: Cấu trúc rẽ nhánh

## 1. Cấu trúc rẽ nhánh trong lập trình

Trong các chương trình tuần tự, các khối lệnh được thực thi lần lượt từ trên xuống dưới. Tuy nhiên, để giải quyết các bài toán thông minh trong thực tế, máy tính cần có khả năng **ra quyết định**: *Nếu điều kiện này đúng thì thực hiện hành động A, nếu sai thì chuyển sang thực hiện hành động B*.

Cấu trúc cho phép máy tính thay đổi luồng thực thi dựa trên kết quả kiểm tra điều kiện được gọi là **Cấu trúc rẽ nhánh**.

![Minh họa khối lệnh rẽ nhánh Tiếng Việt](assets/rendered_blocks/l06_branching_vi.png)

---

## 2. Hai dạng khối lệnh rẽ nhánh trong Scratch 3.0

Trong nhóm **Điều khiển (Control)** màu vàng cam, Scratch cung cấp hai khối bao quanh hình chữ C đặc trưng:

### 2.1. Cấu trúc rẽ nhánh khuyết: `nếu < > thì`

- Dùng khi chỉ cần can thiệp nếu gặp trường hợp đặc biệt; nếu không đúng điều kiện thì bỏ qua và đi tiếp.

- **Cơ chế hoạt động:**
  - Nếu điều kiện lục giác trả về `Đúng` (True): Máy tính thực thi các khối lệnh nằm kẹp bên trong miệng chữ C.
  - Nếu điều kiện trả về `Sai` (False): Toàn bộ khối bên trong chữ C bị bỏ qua, máy tính nhảy thẳng xuống chạy khối lệnh tiếp theo bên dưới.

### 2.2. Cấu trúc rẽ nhánh đủ: `nếu < > thì ... nếu không thì`

- Dùng khi bài toán có hai con đường đối lập nhau và bắt buộc phải chọn đúng một con đường:

  - Nếu điều kiện **ĐÚNG**: Thực thi nhánh trên (sau chữ `thì`).
  - Nếu điều kiện **SAI**: Thực thi nhánh dưới (sau chữ `nếu không thì`).

- **Ví dụ kinh điển:** Kiểm tra số chẵn lẻ:

  - Nếu `((n) mod (2)) = (0)` thì nói `Số chẵn`.
  - Nếu không thì nói `Số lẻ`.

---

## 3. Các phép toán so sánh và điều kiện logic

Để tạo ra điều kiện cho khối rẽ nhánh, ta sử dụng các khối hình lục giác góc nhọn màu xanh lá trong nhóm **Các phép toán (Operators)**:

| Khối lục giác Scratch | Ký hiệu toán học | Ý nghĩa logic | Ví dụ cài đặt thực tế |
|:---:|:---:|---|---|
| `< () > () >` | $>$ | So sánh lớn hơn | `< (diem) > (5) >` |
| `< () < () >` | $<$ | So sánh nhỏ hơn | `< (tuoi) < (18) >` |
| `< () = () >` | $=$ | So sánh bằng *(chú ý chỉ 1 dấu bằng)* | `< ((n) mod (2)) = (0) >` |
| `< < > và < > >` | $\text{AND}$ | **ĐỒNG THỜI**: Đúng khi cả hai điều kiện con đều đúng | `< (a > 0) và (b > 0) >` |
| `< < > hoặc < > >` | $\text{OR}$ | **HOẶC**: Đúng khi có ít nhất một điều kiện đúng | `< (thang = 1) hoặc (thang = 3) >` |
| `< không phải < > >` | $\text{NOT}$ | **PHỦ ĐỊNH**: Đảo ngược kết quả từ đúng thành sai | `< không phải < (tuoi) < (6) > >` |

---

## 4. Các mẫu thuật toán rẽ nhánh cơ bản

### 4.1. Mẫu 1: Thuật toán tìm giá trị lớn nhất của 3 số ($A, B, C$)
Ta áp dụng kỹ thuật **"Đặt vương miện giả định"**:

1. Giả sử số đầu tiên lớn nhất: `đặt [max v] thành (A)`.

2. Lấy $B$ so sánh với vương miện: nếu $B > \text{max}$ thì trao vương miện cho $B$.

3. Lấy $C$ so sánh tiếp: nếu $C > \text{max}$ thì trao vương miện cho $C$.

![Thuật toán tìm số lớn nhất của 3 số](assets/rendered_blocks/l06_max3_vi.png)

### 4.2. Mẫu 2: Cấu trúc đa nhánh lồng nhau (Tương đương `if - elif - else`)
Trong các bài toán xếp loại học sinh (Giỏi $\ge 8.0$, Khá $\ge 6.5$, Trung bình $\ge 5.0$, Yếu $< 5.0$), ta lồng các khối `nếu...nếu không thì` vào nhánh `nếu không thì` của khối trước:

![Cấu trúc đa nhánh if elif else lồng nhau](assets/rendered_blocks/l06_nested_if_elif_vi.png)

---

## 5. Bảng mô phỏng tìm số lớn nhất trong $A = 12, B = 25, C = 18$ (Dry run)

| Bước | Khối lệnh thực thi | Biến `max` | Biểu thức kiểm tra | Kết quả điều kiện | Hành động máy tính |
|:---:|---|:---:|---|:---:|---|
| **1** | `đặt [max v] thành (A)` | **12** | — | — | Giả định `max = 12` |
| **2** | `nếu < (B) > (max) > thì` | 12 | $25 > 12$ | **ĐÚNG** (True) | Bước vào nhánh: `đặt [max] thành 25` |
| **3** | Cập nhật `max` | **25** | — | — | Vương miện thuộc về $B$ |
| **4** | `nếu < (C) > (max) > thì` | 25 | $18 > 25$ | **SAI** (False) | Bỏ qua nhánh |
| **5** | `nói (max)` | **25** | — | — | Chú Mèo nói: `25` |

---

## 6. Các bẫy lỗi thường gặp (Bug Traps)

> **Bẫy 1: Xếp các khối `nếu...thì` độc lập thay vì dùng `nếu...nếu không thì`**
> - *Hiện tượng:* Đặt 2 khối `nếu` tách rời nhau:
>   - `nếu < (diem) >= (5) > thì nói [Đỗ]`
>   - `nếu < (diem) < (5) > thì nói [Trượt]`
> - *Nguy cơ:* Nếu viết nhầm dấu so sánh, chú Mèo có thể nói cả hai câu cùng lúc làm hỏng logic!
> - *Khắc phục:* Luôn dùng cấu trúc đủ `nếu ... thì ... nếu không thì`.

> **Bẫy 2: Nhầm lẫn giữa liên từ `và` (AND) với `hoặc` (OR)**
> - *Ví dụ:* Điều kiện để 3 cạnh $a, b, c$ tạo thành tam giác hợp lệ:
>   $$\text{ĐÚNG: } < < (a + b > c) \text{ và } (b + c > a) > \text{ và } (c + a > b) >$$
> - Nếu nhầm thành `hoặc`, bộ ba cạnh $1, 2, 100$ cũng bị công nhận là tam giác!

> **Bẫy 3: Viết điều kiện kẹp đôi kiểu toán học `3 < x < 10`**
> - Scratch **không cho phép** đặt 3 đối tượng vào một khối so sánh.
> - Bắt buộc phải tách thành hai biểu thức con ghép lại: `< < (x) > (3) > và < (x) < (10) > >`.

---

## 7. Bộ câu hỏi trắc nghiệm củng cố (Concept Quizzes)

1. **Khi điều kiện lục giác trong khối `nếu < > thì` trả về kết quả SAI, máy tính sẽ:**
   - A. Dừng chương trình
   - B. Bỏ qua các lệnh bên trong và chạy tiếp các khối phía dưới *(Đáp án đúng)*
   - C. Báo lỗi đỏ
   - D. Lặp lại từ đầu

2. **Muốn kiểm tra số nguyên $N$ có chia hết cho cả 3 và 5 không, ta dùng khối:**
   - A. `< ((N mod 3) = 0) hoặc ((N mod 5) = 0) >`
   - B. `< ((N mod 3) = 0) và ((N mod 5) = 0) >` *(Đáp án đúng)*
   - C. `< không phải < (N mod 15) = 0 > >`
   - D. `< (N mod 3) = (N mod 5) >`

3. **Biểu thức `< không phải < (A) > (B) > >` tương đương với:**
   - A. $A < B$
   - B. $A = B$
   - C. $A \le B$ ($A$ nhỏ hơn hoặc bằng $B$) *(Đáp án đúng)*
   - D. $A \ne B$

4. **Cho $A = 8, B = 3$. Giá trị của biểu thức `< (A > 5) và (B > 5) >` là:**
   - A. Đúng (True)
   - B. Sai (False) *(Đáp án đúng: vì B > 5 bị Sai)*
   - C. 8
   - D. 3

5. **Để tìm số lớn hơn giữa 2 số $A$ và $B$, khối nào viết chuẩn nhất?**
   - A. `nếu < A > B > thì đặt max thành A, nếu không thì đặt max thành B` *(Đáp án đúng)*
   - B. `lặp lại A lần đặt max thành B`
   - C. `đặt max thành A + B`
   - D. `nói A và B`

6. **Trong Scratch, khối so sánh bằng sử dụng bao nhiêu dấu bằng?**
   - A. 1 dấu `=` *(Đáp án đúng)*
   - B. 2 dấu `==`
   - C. Dấu `:=`
   - D. Dấu `equals`

7. **Cho biến `tuoi = 15`. Đoạn lệnh `nếu < tuoi >= 18 > thì nói [Người lớn] nếu không thì nói [Trẻ em]` sẽ nói:**
   - A. Người lớn
   - B. Trẻ em *(Đáp án đúng)*
   - C. Cả hai câu
   - D. Không nói gì

8. **Muốn kiểm tra điểm thi có nằm trong khoảng hợp lệ từ 0 đến 10 hay không, ta ghép điều kiện:**
   - A. `< (diem >= 0) và (diem <= 10) >` *(Đáp án đúng)*
   - B. `< (diem >= 0) hoặc (diem <= 10) >`
   - C. `< 0 <= diem <= 10 >`
   - D. `< không phải (diem = 0) >`

9. **Khi cả hai nhánh của `nếu ... nếu không thì` đều có lệnh giống nhau ở cuối, ta nên:**
   - A. Để nguyên trong từng nhánh
   - B. Kéo lệnh đó ra ngoài đặt ở ngay phía dưới khối rẽ nhánh *(Đáp án đúng: tối ưu mã)*
   - C. Xóa bỏ lệnh đó
   - D. Nhân đôi số lần thực hiện

10. **Biểu thức `< (thang = 1) hoặc < (thang = 2) hoặc (thang = 3) > >` dùng để kiểm tra:**
    - A. Tháng 1
    - B. Tháng thuộc Quý 1 trong năm *(Đáp án đúng)*
    - C. Cả năm
    - D. Lỗi cú pháp
