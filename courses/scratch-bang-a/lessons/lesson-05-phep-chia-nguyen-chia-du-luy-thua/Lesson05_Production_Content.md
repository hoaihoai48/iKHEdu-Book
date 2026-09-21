# Bài 05: PHÉP CHIA NGUYÊN, CHIA DƯ VÀ LUỸ THỪA

## 1. Bản Chất Phép Chia Nguyên Và Chia Dư Trong Scratch

Khi lập trình, lập trình Bảng A, hai phép toán quan trọng bậc nhất để xử lý số học chính là **Phép chia lấy phần dư (`mod`)** và **Phép chia lấy phần nguyên (`làm tròn xuống của phép chia`)**.

![Minh họa khối lệnh chia nguyên và chia dư](assets/rendered_blocks/l05_div_mod_vi.png)

### 1.1. Phép chia lấy phần dư: Khối `() mod ()`
- Ký hiệu `mod` (viết tắt của Modulo) trả về **số dư còn lại** sau khi thực hiện phép chia giữa hai số nguyên.
- **Tính chất cốt lõi:**
  - `(17) mod (5)` $= 2$ (vì $17 = 5 \times 3 + 2$).
  - `(20) mod (4)` $= 0$ (chia hết thì số dư luôn bằng $0$).
  - Số dư của $A \pmod B$ luôn nằm trong phạm vi từ $0$ đến $B - 1$.
- **Ứng dụng thực chiến:**
  - Kiểm tra số chẵn/lẻ: `((n) mod (2)) = (0)` là số chẵn, `((n) mod (2)) = (1)` là số lẻ.
  - Kiểm tra tính chia hết: `((a) mod (b)) = (0)` nghĩa là $a$ chia hết cho $b$.

### 1.2. Phép chia lấy phần nguyên trong Scratch
Trong Scratch, không có sẵn một khối đơn lẻ mang tên chia nguyên.
Ta phối hợp hai khối lệnh màu xanh lá:

1. Thực hiện phép chia thực: `(A) / (B)`

2. Thả vào khối hàm toán học: chọn tùy chọn **`làm tròn xuống ▼ của ()`** (tương đương hàm `floor` trong toán học).

$$\text{Chia nguyên } A \text{ cho } B = \text{làm tròn xuống của } ((A) / (B))$$

- Ví dụ: `(17) / (5) = 3.4` $\implies$ `làm tròn xuống của (3.4) = 3`.

---

## 2. Bài Toán Quy Đổi Thời Gian & Đơn Vị Đo Lường Thực Tế

Một trong những dạng bài kinh điển trong lập trình là: *Cho tổng số giây $T$, hãy đổi ra Giờ, Phút, Giây.*

![Đổi thời gian bằng chia nguyên và chia dư](assets/rendered_blocks/l05_time_convert_vi.png)

### Thuật toán quy đổi thời gian 4 bước:

1. **Tính số Giờ:** Lấy tổng số giây chia nguyên cho $3600$ (vì 1 giờ = 3600 giây):
   `đặt [gio v] thành ([làm tròn xuống v] của ((tong_giay) / (3600)))`

2. **Tính số giây còn dư lại sau khi đã đổi ra giờ:**
   `đặt [giay_du v] thành ((tong_giay) mod (3600))`

3. **Tính số Phút:** Lấy số giây dư chia nguyên cho $60$ (vì 1 phút = 60 giây):
   `đặt [phut v] thành ([làm tròn xuống v] của ((giay_du) / (60)))`

4. **Tính số Giây cuối cùng:**
   `đặt [giay v] thành ((giay_du) mod (60))`

---

## 3. Phép Tính Lũy Thừa Bằng Vòng Lặp

Để tính $A^B$ ($A$ mũ $B$, tích của $B$ số $A$ nhân với nhau):

- Khởi tạo biến kết quả bằng 1: `đặt [kq v] thành (1)`.
- Lặp lại $B$ lần: nhân dồn $A$ vào kết quả:
  `lặp lại (B) lần { đặt [kq v] thành ((kq) * (A)) }`.

---

## 4. Bảng Mô Phỏng Từng Bước Đổi $T = 3725$ Giây (Dry Run Table)

| Bước thực hiện | Khối lệnh Scratch | Phép tính toán học | Giá trị biến lưu trong RAM |
|:---:|---|---|:---:|
| 1 | `đặt [gio v] thành ([floor] của (3725 / 3600))` | $3725 / 3600 = 1.034 \to \mathbf{1}$ | `gio = 1` |
| 2 | `đặt [giay_du v] thành (3725 mod 3600)` | $3725 - 3600 \times 1 = \mathbf{125}$ | `giay_du = 125` |
| 3 | `đặt [phut v] thành ([floor] của (125 / 60))` | $125 / 60 = 2.083 \to \mathbf{2}$ | `phut = 2` |
| 4 | `đặt [giay v] thành (125 mod 60)` | $125 - 60 \times 2 = \mathbf{5}$ | `giay = 5` |

$\implies$ Kết quả: $3725$ giây = **$1$ giờ $2$ phút $5$ giây**.

---

## 5. Tử Huyệt & Các Bẫy Lỗi Kinh Điển (Bug Traps)

> **Bẫy 1: Dùng nhầm khối `làm tròn của ()` thay vì `làm tròn xuống của ()`**
> - *Khối `làm tròn` (Round):* Sẽ làm tròn lên số nguyên gần nhất nếu phần thập phân $\ge 0.5$.
> - *Ví dụ:* $7 / 4 = 1.75$. Nếu dùng `làm tròn`, kết quả ra $2$ (SAI, vì chia nguyên $7$ cho $4$ chỉ được thương là $1$!).
> - *Khắc phục:* Bắt buộc chọn chính xác **`làm tròn xuống ▼`** trong danh sách thả xuống.

> **Bẫy 2: Chia dư cho số 0**
> - *Hiện tượng:* `(x) mod (0)`.
> - *Hậu quả:* Scratch sẽ trả về giá trị `NaN` (Not a Number), làm tê liệt toàn bộ chương trình!

---

## 6. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Khối lệnh `(23) mod (5)` trả về kết quả là bao nhiêu?**
   - A. 4
   - B. 3 *(Đáp án đúng: vì 23 = 5 * 4 + 3)*
   - C. 2
   - D. 5

2. **Muốn kiểm tra một số nguyên $N$ có phải là số chẵn hay không, điều kiện nào sau đây là ĐÚNG?**
   - A. `< ((N) mod (2)) = (0) >` *(Đáp án đúng)*
   - B. `< ((N) mod (2)) = (1) >`
   - C. `< ((N) / (2)) = (0) >`
   - D. `< (N) > (2) >`

3. **Để thực hiện phép chia lấy phần nguyên của $A$ cho $B$ trong Scratch, ta dùng khối nào?**
   - A. `làm tròn của ((A) / (B))`
   - B. `làm tròn xuống của ((A) / (B))` *(Đáp án đúng)*
   - C. `căn bậc hai của ((A) / (B))`
   - D. `(A) mod (B)`

4. **Giá trị của biểu thức `[làm tròn xuống v] của ((19) / (4))` là:**
   - A. 4.75
   - B. 5
   - C. 4 *(Đáp án đúng: 19 chia 4 được 4 dư 3)*
   - D. 3

5. **Nếu $A$ chia hết cho $B$, thì biểu thức `(A) mod (B)` luôn luôn bằng:**
   - A. 1
   - B. B
   - C. 0 *(Đáp án đúng)*
   - D. A

6. **Một năm nhuận có 366 ngày. Một tuần có 7 ngày. Phép tính nào cho biết số ngày lẻ còn dư ra của năm nhuận?**
   - A. `(366) / (7)`
   - B. `(366) mod (7)` *(Đáp án đúng: 366 mod 7 = 2 ngày dư)*
   - C. `(366) - (7)`
   - D. `(366) * (7)`

7. **Biểu thức `(10) mod (10)` trả về:**
   - A. 0 *(Đáp án đúng)*
   - B. 1
   - C. 10
   - D. 100

8. **Để lấy chữ số tận cùng của một số tự nhiên $N$ (ví dụ số 358 lấy ra số 8), ta dùng biểu thức:**
   - A. `(N) / (10)`
   - B. `(N) mod (10)` *(Đáp án đúng)*
   - C. `(N) - (10)`
   - D. `làm tròn xuống của (N)`

9. **Kết quả của `(4) mod (7)` là:**
   - A. 0
   - B. 3
   - C. 4 *(Đáp án đúng: Số bị chia nhỏ hơn số chia thì số dư chính là số bị chia)*
   - D. 7

10. **Khởi tạo biến `kq = 1`, lặp lại 3 lần nhân với 2, kết quả cuối cùng là:**
    - A. 6
    - B. 8 *(Đáp án đúng: 2 mũ 3 = 8)*
    - C. 9
    - D. 16
