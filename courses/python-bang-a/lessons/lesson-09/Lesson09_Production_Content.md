# Bài 09: Quy luật dãy số và tam giác số

---

## 1. Khởi động: Trò chơi thám tử tìm số tiếp theo

Trong các đề thi Tin học trẻ Bảng A và kỳ thi Toán Tuổi thơ, bài toán về **Dãy số có quy luật** luôn là phần thi hấp dẫn và kích thích trí tuệ nhất!
Hãy cùng tham gia thử thách thám tử số học nhé:

* **Thử thách 1:** $2, 4, 6, 8, 10, ?$ $\implies$ Số tiếp theo là $12$ (Mỗi số cộng thêm $2$).
* **Thử thách 2:** $1, 2, 4, 8, 16, ?$ $\implies$ Số tiếp theo là $32$ (Mỗi số nhân đôi $\times 2$).
* **Thử thách 3 (Bí ẩn Fibonacci):** $1, 1, 2, 3, 5, 8, 13, ?$
  Hãy quan sát thật kỹ:
  $$1 + 1 = 2$$
  $$1 + 2 = 3$$
  $$2 + 3 = 5$$
  $$3 + 5 = 8$$
  $$5 + 8 = 13$$
  $\implies$ Mỗi số đứng sau chính bằng **tổng của 2 số liền trước nó**! Số tiếp theo chắc chắn là $8 + 13 = 21$!

Làm thế nào để ra lệnh cho máy tính Python tự động tính ra số thứ $100$, thứ $1000$ của các dãy số kỳ diệu này trong chớp mắt? Hãy cùng khám phá ngay bài học hôm nay!

---

## 2. Kỹ thuật hoán đổi giá trị & cập nhật biến cuốn chiếu

### 2.1. Phép gán đồng thời (simultaneous assignment) trong Python

Trong nhiều ngôn ngữ khác, muốn tráo đổi giá trị của 2 chiếc cốc $A$ và $B$, ta phải dùng thêm một chiếc cốc trung gian `tam = A; A = B; B = tam`.
Nhưng trong Python, các nhà khoa học đã tạo ra một cú pháp kỳ diệu chỉ trong **1 dòng lệnh**:

```python
a, b = b, a  # Tráo đổi giá trị của a và b ngay lập tức!
```

### 2.2. Kỹ thuật tính dãy Fibonacci bằng kỹ thuật "cuốn chiếu"

Dãy số Fibonacci:
$$F_1 = 1, \quad F_2 = 1, \quad F_3 = 2, \quad F_4 = 3, \quad F_5 = 5, \quad F_6 = 8, \dots$$

Để tính số tiếp theo, ta chỉ cần giữ 2 số hiện tại là `a` và `b`:
* Số mới tiếp theo sẽ là `a + b`.
* Sau đó, số cũ phía sau trở thành `a`, và số mới trở thành `b`!

```python
# Tính số Fibonacci thứ N
n = int(input())

if n == 1 or n == 2:
    print(1)
else:
    a = 1
    b = 1
    for i in range(3, n + 1):
        a, b = b, a + b  # Bước nhảy thần kỳ: a nhận giá trị cũ của b, b nhận tổng mới!
    print(b)
```

### Bảng chạy khô (dry run) mô phỏng với $N = 6$:

| Bước chạy ($i$) | Giá trị `a` trước đó | Giá trị `b` trước đó | Phép tính `a, b = b, a + b` | `a` mới | `b` mới | Giải thích |
|:---:|:---:|:---:|:---:|:---:|:---:|---|
| Khởi tạo | - | - | `a = 1, b = 1` | 1 | 1 | $F_1 = 1, F_2 = 1$ |
| $i = 3$ | 1 | 1 | `b` cũ là 1, `a + b` là 2 | 1 | 2 | Tính $F_3 = 2$ |
| $i = 4$ | 1 | 2 | `b` cũ là 2, `a + b` là 3 | 2 | 3 | Tính $F_4 = 3$ |
| $i = 5$ | 2 | 3 | `b` cũ là 3, `a + b` là 5 | 3 | 5 | Tính $F_5 = 5$ |
| $i = 6$ | 3 | 5 | `b` cũ là 5, `a + b` là 8 | 5 | **8** | Tính $F_6 = 8$ (Kết quả) |

---

## 3. Nghệ thuật in tam giác số & hình ma trận bằng vòng lặp lồng nhau

### Phân tầng nội dung

Phần bắt buộc của bài gồm dãy số, Fibonacci, biến cuốn chiếu và vòng lặp lồng nhau đơn giản. Tribonacci, Pascal, bài tìm chữ số thứ $K$ và các bài cần tối ưu là phần **Thử thách**, dùng để mở rộng sau khi học sinh đã chắc phần cốt lõi.

Khi viết đề thi Tin học trẻ, dạng bài **Vẽ tam giác số / tháp số** xuất hiện với tần suất cực kỳ cao.
Bí quyết để giải quyết dạng bài này là tư duy **2 vòng lặp lồng nhau (Nested Loops)**:
* Vòng lặp ngoài (`for i in ...`): Điều khiển **TỪNG DÒNG** (từ trên xuống dưới).
* Vòng lặp trong (`for j in ...`): Điều khiển **TỪNG CỘT** trên dòng đó (từ trái qua phải).

### 3.1. Tam giác số vuông góc trái

Muốn in ra tháp số có $N = 4$ dòng như sau:
```
1
1 2
1 2 3
1 2 3 4
```

**Quy luật:** Dòng thứ $i$ sẽ in các số từ $1$ đến $i$.
```python
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()  # In xong 1 dòng thì xuống dòng mới!
```

### 3.2. Tam giác số lặp lại số dòng

```
1
2 2
3 3 3
4 4 4 4
```

**Quy luật:** Dòng thứ $i$ có đúng $i$ số, và tất cả các số đều bằng $i$.
```python
n = int(input())
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
```

---

## 4. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Dãy số $1, 1, 2, 3, 5, 8, 13, \dots$ mang tên nhà toán học nổi tiếng nào?
- **A.** Newton
- **B.** **[Đáp án đúng]** Fibonacci
- **C.** Pythagoras
- **D.** Archimedes
- > *Giải thích:* Đây là dãy số Fibonacci huyền thoại xuất hiện nhiều trong tự nhiên và đề thi tin học trẻ.

#### Câu 2: Trong Python, câu lệnh `x, y = 10, 20` có ý nghĩa gì?
- **A.** `x` và `y` đều nhận giá trị 10
- **B.** Máy tính báo lỗi cú pháp
- **C.** **[Đáp án đúng]** `x` nhận giá trị 10 và `y` nhận giá trị 20
- **D.** `x` nhận giá trị 20 và `y` nhận giá trị 10
- > *Giải thích:* Phép gán đồng thời gán lần lượt biến theo thứ tự các giá trị ở vế phải.

#### Câu 3: Cho đoạn code sau:
```python
a = 5
b = 9
a, b = b, a
print(a, b)
```
Kết quả in ra là gì?
- **A.** `5 9`
- **B.** `5 5`
- **C.** **[Đáp án đúng]** `9 5`
- **D.** `9 9`
- > *Giải thích:* Câu lệnh `a, b = b, a` hoán đổi trực tiếp giá trị của 2 biến mà không cần biến phụ.

#### Câu 4: Cho `a = 2, b = 3`. Sau khi thực hiện lệnh `a, b = b, a + b`, giá trị mới của `a` và `b` là:
- **A.** `a = 2, b = 5`
- **B.** **[Đáp án đúng]** `a = 3, b = 5`
- **C.** `a = 5, b = 5`
- **D.** `a = 3, b = 6`
- > *Giải thích:* Giá trị ban đầu của $b$ là 3 (gán cho $a$). Giá trị ban đầu của $a+b$ là $2+3=5$ (gán cho $b$).

#### Câu 5: Số hạng thứ 7 của dãy Fibonacci (bắt đầu bằng $1, 1, 2, \dots$) là:
- **A.** 8
- **B.** 11
- **C.** **[Đáp án đúng]** 13
- **D.** 21
- > *Giải thích:* Các số hạng lần lượt là: $F_1=1, F_2=1, F_3=2, F_4=3, F_5=5, F_6=8, F_7=13$.

#### Câu 6: Dãy số $3, 7, 11, 15, 19, \dots$ có công sai (khoảng cách giữa 2 số liền nhau) là bao nhiêu?
- **A.** 3
- **B.** **[Đáp án đúng]** 4
- **C.** 5
- **D.** 7
- > *Giải thích:* $7 - 3 = 4$, $11 - 7 = 4$. Đây là cấp số cộng có khoảng cách bằng 4.

#### Câu 7: Công thức tổng quát của số hạng thứ $n$ trong dãy cấp số cộng có số đầu $u_1$ và khoảng cách $d$ là:
- **A.** $u_n = u_1 + n \times d$
- **B.** **[Đáp án đúng]** $u_n = u_1 + (n - 1) \times d$
- **C.** $u_n = u_1 \times d$
- **D.** $u_n = (u_1 + d) \times n$
- > *Giải thích:* Để đi từ số thứ 1 đến số thứ $n$, ta cần nhảy thêm $(n-1)$ bước nhảy độ dài $d$.

#### Câu 8: Đoạn code sau in ra bao nhiêu dấu hoa thị `*`?
```python
for i in range(3):
    for j in range(2):
        print("*", end="")
```
- **A.** 3
- **B.** 5
- **C.** **[Đáp án đúng]** 6
- **D.** 2
- > *Giải thích:* Vòng lặp ngoài lặp 3 lần, mỗi lần vòng lặp trong chạy 2 lần. Tổng cộng: $3 \times 2 = 6$ lần.

#### Câu 9: Lệnh `print()` rỗng (không có tham số) ở cuối vòng lặp ngoài có tác dụng gì khi in ma trận?
- **A.** Xóa màn hình
- **B.** In ra khoảng trắng
- **C.** **[Đáp án đúng]** Xuống dòng mới
- **D.** Dừng chương trình
- > *Giải thích:* `print()` mặc định kết thúc bằng ký tự xuống dòng `\n`, giúp bắt đầu dòng mới cho hàng kế tiếp.

#### Câu 10: Đoạn code sau in ra hình gì?
```python
for i in range(1, 4):
    print("*" * i)
```
- **A.** Hình vuông $3 \times 3$
- **B.** **[Đáp án đúng]** Tam giác sao tăng dần
- **C.** 3 dòng giống hệt nhau
- **D.** Một hàng ngang duy nhất
- > *Giải thích:* Python hỗ trợ nhân chuỗi: `"*" * 1` là `*`, `"*" * 2` là `**`, `"*" * 3` là `***`.

#### Câu 11: Cho dãy số đan dấu: $1, -2, 3, -4, 5, -6, \dots$. Số thứ 10 của dãy là:
- **A.** 10
- **B.** **[Đáp án đúng]** -10
- **C.** -9
- **D.** 11
- > *Giải thích:* Các vị trí chẵn mang dấu trừ ($-$), số thứ 10 là vị trí chẵn nên là $-10$.

#### Câu 12: Tổng của dãy số đan dấu $S = 1 - 2 + 3 - 4 + \dots + 99 - 100$ bằng bao nhiêu?
- **A.** 0
- **B.** 50
- **C.** **[Đáp án đúng]** -50
- **D.** -100
- > *Giải thích:* Nhóm từng cặp: $(1-2) + (3-4) + \dots + (99-100) = (-1) \times 50 = -50$.

#### Câu 13: Khi giải bài toán tìm số thứ $N$ của dãy số trong phòng thi, nếu $N \le 10^5$ ta có thể dùng vòng lặp, nhưng nếu $N = 10^9$ ta nên ưu tiên điều gì?
- **A.** Chạy vòng lặp thật nhanh
- **B.** **[Đáp án đúng]** Tìm công thức toán học tính trực tiếp $\mathcal{O}(1)$
- **C.** Dùng máy tính mạnh hơn
- **D.** Bỏ qua bài toán
- > *Giải thích:* $10^9$ phép tính vòng lặp sẽ bị quá thời gian (TLE > 1s). Cần dùng công thức giải tích trực tiếp $\mathcal{O}(1)$.

#### Câu 14: Đoạn code sau in ra giá trị gì?
```python
s = 0
for i in range(1, 5):
    s = s + i * (i + 1)
print(s)
```
- **A.** 20
- **B.** 30
- **C.** **[Đáp án đúng]** 40
- **D.** 50
- > *Giải thích:* $1 \times 2 + 2 \times 3 + 3 \times 4 + 4 \times 5 = 2 + 6 + 12 + 20 = 40$.

#### Câu 15: Tam giác pascal hàng thứ 3 (coi hàng đầu là hàng 0: `1`, hàng 1: `1 1`, hàng 2: `1 2 1`) sẽ là:
- **A.** `1 2 2 1`
- **B.** **[Đáp án đúng]** `1 3 3 1`
- **C.** `1 4 4 1`
- **D.** `1 3 4 1`
- > *Giải thích:* Mỗi số bên trong bằng tổng 2 số liền kề ngay trên nó: $1$, $1+2=3$, $2+1=3$, $1$.
