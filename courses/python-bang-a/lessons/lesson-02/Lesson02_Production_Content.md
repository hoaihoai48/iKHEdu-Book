# Bài 02: Toán tử số học và biểu thức toán học

## 1. Bản chất của tính toán số học trong khoa học máy tính

Mọi chương trình máy tính, từ chiếc máy tính bỏ túi đơn giản cho đến những hệ thống điều khiển tàu vũ trụ, đều khởi nguồn từ việc thực hiện các **phép tính số học**. Máy tính có thể thực hiện hàng tỷ phép tính mỗi giây với độ chính xác tuyệt đối, nhưng để máy tính cho ra kết quả đúng như mong muốn, người lập trình cần hiểu rõ:
* Bản chất của các phép toán cơ bản: cộng, trừ, nhân, chia.
* Sự khác biệt sống còn của **phép chia thực `/`** trong bộ nhớ máy tính.
* Cơ chế phân rã và tính toán một **biểu thức toán học** theo **tháp thứ tự ưu tiên**.
* Vai trò của **cặp dấu ngoặc tròn `()`** khi chuyển đổi các phân số đại số phức tạp sang dòng lệnh máy tính.

---

## 2. Bốn toán tử số học cơ bản

Python cung cấp 4 toán tử tính toán cơ bản thao tác trên số nguyên (`int`) và số thực (`float`):

| Ký hiệu | Tên phép toán | Cú pháp | Ví dụ cụ thể | Kết quả trả về | Kiểu dữ liệu kết quả |
|:---:|---|---|:---:|:---:|:---:|
| **`+`** | Phép cộng | `a + b` | `15 + 7` | `22` | `int` (hoặc `float`) |
| **`-`** | Phép trừ | `a - b` | `20 - 6` | `14` | `int` (hoặc `float`) |
| **`*`** | Phép nhân | `a * b` | `6 * 7` | `42` | `int` (hoặc `float`) |
| **`/`** | Phép chia thực | `a / b` | `7 / 2` | `3.5` | **Luôn luôn là `float`** |

> ⚠️ **TỬ HUYỆT BẮT BUỘC PHẢI NHỚ: PHÉP CHIA THỰC `/` LUÔN TRẢ VỀ SỐ THỰC (`float`)**
> * Trong Python, kết quả của phép chia `/` **luôn luôn mang kiểu số thực (`float`)**, kể cả khi phép chia hoàn toàn chia hết không có dư!
> * Ví dụ: `8 / 2` cho kết quả hiển thị là `4.0` (có dấu chấm thập phân, không phải số nguyên `4`).
> * Nếu đề thi yêu cầu in ra một số nguyên, học sinh dùng `a / b` sẽ in ra `4.0` và bị máy chấm tự động đánh lỗi kết quả sai (**Wrong Answer**). Khi cần kết quả là số nguyên trong phép chia hết, ta phải dùng phép chia nguyên `a // b`.

---

## 3. Biểu thức toán học & Tháp thứ tự ưu tiên

### 3.1. Khái niệm biểu thức toán học
Một **biểu thức toán học** là sự kết hợp có quy tắc giữa:
* **Toán hạng:** Hằng số (`5`, `10`), biến số (`a`, `b`) hoặc kết quả của các hàm số.
* **Toán tử:** Các dấu phép tính `+`, `-`, `*`, `/`.

Biểu thức sau khi được CPU xử lý sẽ luôn tính ra một **giá trị duy nhất** để gán vào một biến hoặc in trực tiếp ra màn hình.

### 3.2. Tháp thứ tự ưu tiên tính toán

Khi trong một dòng lệnh xuất hiện nhiều phép tính đan xen, máy tính không tính bừa bãi từ trái sang phải mà tuân thủ nghiêm ngặt **tháp thứ tự ưu tiên từ trên xuống dưới**:

![Tháp thứ tự ưu tiên toán tử](../../assets/l02_operator_precedence.svg?v=1788575106)

1. **Cấp 1 (Ưu tiên tuyệt đối):** Cặp ngoặc tròn `( )`. Mọi biểu thức nằm bên trong ngoặc luôn được máy tính giải quyết trước tiên.
2. **Cấp 2:** Phép Nhân `*` và Phép Chia `/`. Hai phép này có cùng bậc ưu tiên, được tính lần lượt từ **trái qua phải**.
3. **Cấp 3 (Ưu tiên thấp nhất):** Phép Cộng `+` và Phép Trừ `-`. Tính lần lượt từ **trái qua phải**.

### 3.3. Kỹ thuật chuyển đổi biểu thức toán học sang mã Python

Trong sách giáo khoa toán học, biểu thức thường được viết dưới dạng phân số có gạch ngang nằm ở giữa. Khi lập trình, tất cả các thành phần phải được viết thẳng hàng trên một dòng ngang. 

Nếu không sử dụng cặp ngoặc tròn `()` để bao bọc, máy tính sẽ hiểu sai ý định của người lập trình:

| Biểu thức toán học | Cách viết SAI ❌ | Vì sao sai? | Cách viết ĐÚNG chuẩn mực ✅ |
|:---:|:---:|---|:---:|
| $\frac{a + b}{c}$ | `a + b / c` | Máy tính sẽ chia `b / c` trước, rồi mới lấy `a` cộng vào. | `(a + b) / c` |
| $\frac{a + b}{c + d}$ | `(a + b) / c + d` | Máy tính lấy tổng `(a + b)` chia cho `c` xong rồi mới cộng `d`. | `(a + b) / (c + d)` |
| $\frac{a \times b}{c \times d}$ | `a * b / c * d` | Máy tính nhân `a * b`, chia `c`, rồi lại nhân kết quả đó với `d`. | `(a * b) / (c * d)` |
| $2a + 3b$ | `2a + 3b` | Lỗi cú pháp! Python không hiểu phép nhân ngầm. | `2 * a + 3 * b` |

---

## 4. Bảng mô phỏng từng bước tính biểu thức phức tạp

Xét đoạn chương trình tính biểu thức:
```python
a = 8
b = 2
c = 5
ans = (a + 4) / (b + 1) + c * 3 - 6 / 2
```

### Bảng phân rã từng bước thực thi của CPU theo tháp ưu tiên:

| Bước | Phép tính được ưu tiên | Biểu thức sau khi tính | Giải thích lý do |
|:---:|:---:|:---:|---|
| **Gốc** | `(8 + 4) / (2 + 1) + 5 * 3 - 6 / 2` | | Nạp biểu thức ban đầu vào bộ xử lý CPU |
| **1** | Ngoặc 1: `(8 + 4)` | `12 / (2 + 1) + 5 * 3 - 6 / 2` | Ngoặc tròn thứ nhất có độ ưu tiên cao nhất $\implies 12$ |
| **2** | Ngoặc 2: `(2 + 1)` | `12 / 3 + 5 * 3 - 6 / 2` | Ngoặc tròn thứ hai được tính tiếp theo $\implies 3$ |
| **3** | Chia: `12 / 3` | `4.0 + 5 * 3 - 6 / 2` | Phép chia thực hiện từ trái sang phải $\implies 4.0$ |
| **4** | Nhân: `5 * 3` | `4.0 + 15 - 6 / 2` | Phép nhân tiếp theo $\implies 15$ |
| **5** | Chia: `6 / 2` | `4.0 + 15 - 3.0` | Phép chia cuối cùng $\implies 3.0$ |
| **6** | Cộng: `4.0 + 15` | `19.0 - 3.0` | Phép cộng từ trái sang phải $\implies 19.0$ |
| **7** | Trừ: `19.0 - 3.0` | `16.0` | Phép trừ cuối cùng $\implies 16.0$ |
| **Kết thúc** | Gán kết quả | `ans = 16.0` | Lưu giá trị `16.0` vào biến `ans` trong RAM |

---

## 5. Tử huyệt và bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: LỖI CHIA CHO SỐ KHÔNG (`ZeroDivisionError`)**
> * Trong toán học và lập trình, phép chia cho số 0 là không xác định.
> * Nếu mẫu số bằng 0 (ví dụ `x / 0` hoặc `(a + b) / (c - d)` khi `c == d`), chương trình sẽ bị dừng khẩn cấp với thông báo lỗi: `ZeroDivisionError: division by zero`.
> * **Cách phòng tránh:** Luôn kiểm tra điều kiện mẫu số phải khác 0 trước khi thực hiện phép chia.

> ❌ **BẪY LỖI 2: QUÊN DẤU NHÂN `*` TRONG ĐẠI SỐ**
> * Trong toán học, ta hay viết $2x$ hoặc $3(a + b)$.
> * Trong Python, nếu viết `2x` hay `3(a + b)`, máy tính sẽ báo lỗi cú pháp: `SyntaxError: invalid syntax`.
> * **Quy tắc:** Mọi phép nhân bắt buộc phải có dấu sao `*`: `2 * x` hoặc `3 * (a + b)`.

> ❌ **BẪY LỖI 3: DÙNG DẤU PHẨY `,` THAY CHO DẤU CHẤM THẬP PHÂN `.`**
> * Trong tiếng Việt, ta quen viết $3,5$. Nhưng trong Python, số thực bắt buộc dùng dấu chấm: `3.5`.
> * Nếu viết `x = 3,5`, Python sẽ hiểu biến `x` là một bộ hai phần tử `(3, 5)`, dẫn đến kết quả sai hoàn toàn!

---

## 6. Mẫu code chuẩn thi đấu

### 6.1. Tính giá trị biểu thức phân số đại số
```python
a, b, c = map(int, input().split())
# Tính biểu thức: (a + b) / c
ket_qua = (a + b) / c
print(ket_qua)
```

### 6.2. Tính giá trị đa thức bậc hai
```python
# Tính giá trị y = a*x^2 + b*x + c
a, b, c, x = map(int, input().split())
y = a * (x * x) + b * x + c
print(y)
```

---

## 7. Concept Quiz: 18 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Phép chia `10 / 2` trong Python trả về kết quả nào?
- **A.** `5` (kiểu `int`)
- **B.** **[Đáp án đúng]** `5.0` (kiểu `float`)
- **C.** `5.00`
- **D.** Báo lỗi
- > *Giải thích:* Phép chia `/` trong Python luôn luôn trả về kiểu số thực `float`.

#### Câu 2: Biểu thức `2 + 3 * 4` có kết quả là bao nhiêu?
- **A.** 20
- **B.** **[Đáp án đúng]** 14
- **C.** 24
- **D.** 10
- > *Giải thích:* Phép nhân có độ ưu tiên cao hơn phép cộng, nên máy tính tính `3 * 4 = 12` trước, sau đó `2 + 12 = 14`.

#### Câu 3: Muốn biểu diễn phân số đại số $\frac{a + b}{c + d}$ trong Python, cách viết nào sau đây là chuẩn mực nhất?
- **A.** `a + b / c + d`
- **B.** `(a + b) / c + d`
- **C.** `a + b / (c + d)`
- **D.** **[Đáp án đúng]** `(a + b) / (c + d)`
- > *Giải thích:* Cần đặt cả tử số và mẫu số trong cặp ngoặc tròn để máy tính tính toán tổng trước khi chia.

#### Câu 4: Khi thực hiện lệnh `print(10 / 0)`, hiện tượng gì sẽ xảy ra?
- **A.** In ra `0`
- **B.** In ra giá trị vô cùng (`inf`)
- **C.** **[Đáp án đúng]** Báo lỗi `ZeroDivisionError: division by zero`
- **D.** Chương trình tự động bỏ qua
- > *Giải thích:* Trong toán học và máy tính, phép chia cho 0 là không hợp lệ và gây lỗi ngắt chương trình.

#### Câu 5: Trong Python, ký hiệu nào được dùng cho phép nhân?
- **A.** `x`
- **B.** `.`
- **C.** `:`
- **D.** **[Đáp án đúng]** `*`
- > *Giải thích:* Dấu sao `*` là toán tử nhân chuẩn mực trong hầu hết các ngôn ngữ lập trình.

#### Câu 6: Biểu thức `(10 - 2) * (3 + 1)` cho kết quả bằng:
- **A.** 16
- **B.** 22
- **C.** **[Đáp án đúng]** 32
- **D.** 28
- > *Giải thích:* Các biểu thức trong ngoặc được tính trước: `8 * 4 = 32`.

#### Câu 7: Khi viết `x = 2(a + b)` trong Python, máy tính sẽ phản hồi như thế nào?
- **A.** Tự động hiểu là nhân 2 với tổng
- **B.** **[Đáp án đúng]** Báo lỗi cú pháp `SyntaxError: invalid syntax`
- **C.** In ra kết quả bình thường
- **D.** Gán giá trị 2 vào biến
- > *Giải thích:* Python không hỗ trợ phép nhân ngầm, bắt buộc phải viết `2 * (a + b)`.

#### Câu 8: Biểu thức `12 / 4 / 3` được máy tính tính toán như thế nào?
- **A.** Tính `4 / 3` trước rồi lấy `12` chia cho kết quả đó
- **B.** **[Đáp án đúng]** Tính từ trái sang phải: `(12 / 4) / 3 = 3.0 / 3 = 1.0`
- **C.** Báo lỗi vì có 2 dấu chia liên tiếp
- **D.** Kết quả là 9.0
- > *Giải thích:* Các phép chia có cùng bậc ưu tiên và được thực hiện kết hợp từ trái sang phải.

#### Câu 9: Trong biểu thức `10 - 4 + 2`, thứ tự tính toán đúng là:
- **A.** Tính `4 + 2 = 6` trước rồi lấy `10 - 6 = 4`
- **B.** **[Đáp án đúng]** Tính từ trái sang phải: `10 - 4 = 6`, sau đó `6 + 2 = 8`
- **C.** Tính tùy ý vì cộng và trừ như nhau
- **D.** Kết quả là 4
- > *Giải thích:* Phép cộng và trừ có cùng độ ưu tiên, được tính lần lượt từ trái sang phải.

#### Câu 10: Kết quả của biểu thức `7 / 2` trong Python là:
- **A.** `3`
- **B.** **[Đáp án đúng]** `3.5`
- **C.** Báo lỗi vì 7 không chia hết cho 2
- **D.** `3` (phần nguyên)
- > *Giải thích:* Phép chia `/` trong Python **luôn luôn trả về số thực (`float`)**, kể cả khi chia hết: `4 / 2` cũng cho ra `2.0` chứ không phải `2`.

#### Câu 11: Giá trị của biểu thức `10 - 3 * 2` là:
- **A.** 14
- **B.** **[Đáp án đúng]** 4
- **C.** 7
- **D.** 24
- > *Giải thích:* Toán tử `*` có độ ưu tiên cao hơn `-`, nên `3 * 2 = 6` được tính trước, sau đó mới trừ từ 10: `10 - 6 = 4`.

#### Câu 12: Biểu thức `20 / (5 - 5)` sẽ dẫn đến lỗi gì?
- **A.** `ValueError`
- **B.** `TypeError`
- **C.** **[Đáp án đúng]** `ZeroDivisionError`
- **D.** Không có lỗi
- > *Giải thích:* `5 - 5 = 0`, phép chia biến thành `20 / 0` gây chia cho 0.

#### Câu 13: Để đổi dấu một số $x$ từ dương sang âm, ta viết:
- **A.** `-x`
- **B.** `0 - x`
- **C.** `x * (-1)`
- **D.** **[Đáp án đúng]** Cả A, B, C đều đúng
- > *Giải thích:* Cả 3 cách đều cho ra số đối dấu của $x$.

#### Câu 14: Biểu thức nào sau đây cho kết quả là số thực?
- **A.** `5 + 3`
- **B.** `10 - 2`
- **C.** `4 * 2`
- **D.** **[Đáp án đúng]** `8 / 4`
- > *Giải thích:* Chỉ có phép chia `/` luôn luôn trả về kiểu `float`.

#### Câu 15: Kết quả của `(6 + 2) / 2` là:
- **A.** 7
- **B.** **[Đáp án đúng]** 4.0
- **C.** 4
- **D.** 7.0
- > *Giải thích:* `(6 + 2) = 8`, `8 / 2 = 4.0`.

#### Câu 16: Biểu thức `6 + 2 / 2` là:
- **A.** 4.0
- **B.** **[Đáp án đúng]** 7.0
- **C.** 7
- **D.** 4
- > *Giải thích:* Không có ngoặc nên `2 / 2 = 1.0` tính trước, `6 + 1.0 = 7.0`.

#### Câu 17: Cặp ngoặc nào được dùng để gom nhóm ưu tiên trong biểu thức toán học của Python?
- **A.** Cặp ngoặc vuông `[ ]`
- **B.** Cặp ngoặc nhọn `{ }`
- **C.** **[Đáp án đúng]** Cặp ngoặc tròn `( )`
- **D.** Cặp ngoặc nhọn `< >`
- > *Giải thích:* Python chỉ sử dụng ngoặc tròn `()` cho biểu thức toán học.

#### Câu 18: Kết quả của `(100 - 50) * (20 - 10) / 10` là:
- **A.** 50
- **B.** **[Đáp án đúng]** 50.0
- **C.** 500
- **D.** 500.0
- > *Giải thích:* $50 \times 10 / 10 = 500 / 10 = 50.0$.
