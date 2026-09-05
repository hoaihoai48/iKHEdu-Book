# Bài 05: Vòng lặp for và hàm range

## 1. Bản chất của vòng lặp trong khoa học máy tính

Trong lập trình, có những công việc cần được thực hiện lặp đi lặp lại hàng trăm, hàng nghìn, thậm chí hàng triệu lần (ví dụ: tính tổng các số từ 1 đến 1000, in danh sách thí sinh, kiểm tra từng phần tử trong một tập hợp). 

Nếu không có vòng lặp, người lập trình sẽ phải gõ tay hàng nghìn dòng lệnh giống hệt nhau — điều này hoàn toàn bất khả thi. **Vòng lặp** ra đời nhằm mục đích giải phóng con người, chỉ cần viết khối lệnh một lần và ra lệnh cho máy tính tự động lặp lại.

Khi ta đã **biết trước chính xác số lần lặp**, công cụ chuẩn mực và mạnh mẽ nhất trong Python chính là **Vòng lặp `for` kết hợp với hàm `range()`**.

---

## 2. Chiếc thước đo `range()` toàn tập

Hàm `range()` là một trong những hàm đặc biệt nhất của Python. Nó không tạo ra một danh sách chứa sẵn toàn bộ các số trong bộ nhớ RAM, mà đóng vai trò như một **bộ sinh số tự động**: Mỗi lần vòng lặp cần một con số tiếp theo, `range()` mới tính toán và cung cấp con số đó.

![Chiếc thước đo range](../../assets/l05_range_ruler.svg?v=1788575106)

### 2.1. Ba dạng sử dụng của hàm `range()`

| Dạng Cú Pháp | Số Tham Số | Ý Nghĩa Kỹ Thuật | Dãy Số Sinh Ra | Số Lần Lặp |
|---|:---:|---|---|:---:|
| `range(stop)` | 1 tham số | Bắt đầu từ số `0`, bước nhảy mặc định là `+1`, **dừng trước `stop`**. | `0, 1, 2, ..., stop - 1` | Đúng `stop` lần |
| `range(start, stop)` | 2 tham số | Bắt đầu từ `start`, bước nhảy mặc định `+1`, **dừng trước `stop`**. | `start, start + 1, ..., stop - 1` | `stop - start` lần |
| `range(start, stop, step)` | 3 tham số | Bắt đầu từ `start`, mỗi bước tăng/giảm `step`, **dừng trước `stop`**. | Các số cách đều nhau một khoảng `step` | Tính theo công thức |

> ❌ **TỬ HUYỆT BẮT BUỘC PHẢI KHẮC CỐT GHI TÂM: CẬN TRÊN `stop` LUÔN BỊ LOẠI TRỪ!**
> * Trong toán học, đoạn số thường lấy cả hai đầu mút $[1, 10]$.
> * Nhưng trong hàm `range(1, 10)`, số `10` **KHÔNG BAO GIỜ ĐƯỢC CHẠM TỚI**! Dãy số chỉ chạy đến số `9` là dừng lại.
> * Nếu muốn lặp qua các số từ $1$ đến $N$ đầy đủ, cận trên trong `range` bắt buộc phải là:
>   $$\mathbf{range(1, N + 1)}$$

### 2.2. Kỹ thuật duyệt số bước nhảy âm (Chạy lùi)

Khi tham số `step` mang giá trị âm, hàm `range()` sẽ đếm lùi từ số lớn về số bé. Cận bắt đầu `start` phải lớn hơn cận dừng `stop`:
```python
# Đếm ngược từ 5 về 1 để phóng tên lửa:
for i in range(5, 0, -1):
    print(i, end=" ")
print("PHONG!")
```
**Màn hình in ra:**
```text
5 4 3 2 1 PHONG!
```

---

## 3. Cú pháp vòng lặp `for` và Biến lặp

* **Cú pháp chuẩn mực:**
  ```python
  for bien_lap in range(start, stop, step):
      # Khoi lenh duoc lap lai (Thut le 4 dau cach)
  ```
* **Cơ chế hoạt động:**
  1. Ở vòng lặp đầu tiên, `bien_lap` tự động nhận giá trị đầu tiên do `range` sinh ra (`start`).
  2. Toàn bộ khối lệnh bên trong thân vòng lặp được thực thi.
  3. Sau khi chạy xong lệnh cuối cùng của khối lặp, máy tính quay lên đầu, tự động gán giá trị tiếp theo cho `bien_lap`.
  4. Quá trình này lặp lại liên tục cho đến khi chạm đến giới hạn dừng `stop` thì vòng lặp kết thúc.

---

## 4. Các mẫu thuật toán tích lũy kinh điển

Trong các bài thi lập trình, vòng lặp `for` gần như luôn đi kèm với kỹ thuật **Tích lũy giá trị**.

### 4.1. Mẫu 1: Thuật toán Tính Tổng tích lũy
Bài toán: Tính tổng $S = 1 + 2 + 3 + \dots + N$.

```python
n = int(input())
# Bước 1: Khởi tạo biến tích lũy tổng ban đầu bằng 0
tong = 0

# Bước 2: Duyệt qua từng số i từ 1 đến N
for i in range(1, n + 1):
    tong += i  # Cộng dồn i vào biến tong

# Bước 3: In kết quả sau khi vòng lặp đã kết thúc hoàn toàn
print(tong)
```

### 4.2. Mẫu 2: Thuật toán Tính Tích giai thừa
Bài toán: Tính tích $P = 1 \times 2 \times 3 \times \dots \times N$ ($N!$).

```python
n = int(input())
# BẮT BUỘC: Khởi tạo biến tích bằng 1 (Nếu để bằng 0 thì mọi tích đều ra 0!)
tich = 1

for i in range(1, n + 1):
    tich *= i

print(tich)
```

### 4.3. Mẫu 3: Thuật toán Đếm số phần tử thỏa mãn điều kiện
Bài toán: Đếm xem trong đoạn từ $1$ đến $N$ có bao nhiêu số chia hết cho 3.

```python
n = int(input())
dem = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        dem += 1  # Mỗi lần phát hiện số thỏa mãn, tăng đếm lên 1

print(dem)
```

---

## 5. Bảng mô phỏng từng bước

Xét chương trình tính tổng với $N = 4$:
```python
tong = 0
for i in range(1, 5):
    tong = tong + i
print(tong)
```

### Bảng theo dõi biến thiên ô nhớ RAM qua từng vòng lặp:

| Vòng Lặp | Giá Trị Biến `i` | Biểu Thức Tính Toán | Giá Trị Cũ Của `tong` | Giá Trị Mới Của `tong` |
|:---:|:---:|:---:|:---:|:---:|
| **Khởi tạo** | *(Chưa có)* | `tong = 0` | *(Khởi đầu)* | **0** |
| **Vòng 1** | **`1`** | `tong = 0 + 1` | 0 | **1** |
| **Vòng 2** | **`2`** | `tong = 1 + 2` | 1 | **3** |
| **Vòng 3** | **`3`** | `tong = 3 + 3` | 3 | **6** |
| **Vòng 4** | **`4`** | `tong = 6 + 4` | 6 | **10** |
| **Dừng lặp** | *(Chạm cận 5)* | Thoát khỏi vòng `for` | 10 | **10** |

$$\implies \text{Kết quả in ra màn hình sau vòng lặp: } \mathbf{10}$$

---

## 6. Tử huyệt và Bẫy lỗi lập trình kinh điển

> ❌ **BẪY LỖI 1: ĐẶT LỆNH IN KẾT QUẢ VÀO BÊN TRONG THÂN VÒNG LẶP**
> * Xem đoạn code sai:
>   ```python
>   tong = 0
>   for i in range(1, n + 1):
>       tong += i
>       print(tong)  # Bị thụt lề vào trong vòng lặp!
>   ```
> * **Hậu quả:** Thay vì in ra 1 dòng kết quả duy nhất ở cuối, chương trình sẽ in ra $N$ dòng kết quả trung gian sau mỗi vòng lặp $\implies$ Bị máy chấm chấm lỗi **Wrong Answer** ngay lập tức!
> * **Quy tắc:** Lệnh in kết quả cuối cùng phải được **lùi ra ngoài ngang hàng với từ khóa `for`**.

> ❌ **BẪY LỖI 2: KHỞI TẠO BIẾN TÍCH BẰNG 0**
> * Khi tính tích hoặc giai thừa, nếu khởi tạo `tich = 0` thì $0 \times \text{bất kỳ số nào}$ cũng luôn bằng $0$. Kết quả cuối cùng sẽ luôn là $0$.
> * Luôn khởi tạo: `tong = 0` và `tich = 1`.

> ❌ **BẪY LỖI 3: QUÊN CỘNG 1 Ở CẬN TRÊN `range(1, n)`**
> * Viết `range(1, n)` sẽ chỉ chạy từ $1$ đến $n - 1$, dẫn đến thiếu mất số $n$ cuối cùng trong phép tính.

---

## 7. Mẫu code chuẩn thi đấu

```python
# Mẫu tính tổng các số chẵn trong đoạn [A, B]
a, b = map(int, input().split())
tong_chan = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        tong_chan += i

print(tong_chan)
```

---

## 8. Concept Quiz: 20 câu trắc nghiệm kiểm tra sâu khái niệm

#### Câu 1 (Bản chất hàm range 1 tham số):
Lệnh `range(5)` sẽ sinh ra lần lượt các số nào?
- **A.** `1, 2, 3, 4, 5`
- **B.** **[Đáp án đúng]** `0, 1, 2, 3, 4`
- **C.** `1, 2, 3, 4`
- **D.** `0, 1, 2, 3, 4, 5`
> *Giải thích:* `range(stop)` mặc định bắt đầu từ 0 và dừng trước `stop`, do đó dãy số là 0, 1, 2, 3, 4.

#### Câu 2 (Số lần lặp của range):
Vòng lặp `for i in range(10):` sẽ thực hiện lặp lại phần thân lệnh bao nhiêu lần?
- **A.** 9 lần
- **B.** **[Đáp án đúng]** 10 lần
- **C.** 11 lần
- **D.** Vô tận lần
> *Giải thích:* Các giá trị từ 0 đến 9 gồm đúng 10 số, do đó vòng lặp chạy đúng 10 lần.

#### Câu 3 (Cận trên bị loại trừ):
Để lặp qua các số nguyên từ 1 đến $N$ (bao gồm cả $N$), biểu thức `range` nào sau đây là chuẩn mực nhất?
- **A.** `range(1, N)`
- **B.** **[Đáp án đúng]** `range(1, N + 1)`
- **C.** `range(0, N)`
- **D.** `range(1, N + 2)`
> *Giải thích:* Vì cận trên luôn bị loại trừ nên cần truyền vào $N + 1$ để vòng lặp chạy đến số $N$.

#### Câu 4 (Dự đoán output — Đếm bước nhảy):
Đoạn code sau đây sẽ in ra dãy số nào?
```python
for i in range(2, 9, 2):
    print(i, end=" ")
```
- **A.** `2 4 6 8 10`
- **B.** **[Đáp án đúng]** `2 4 6 8`
- **C.** `2 4 6`
- **D.** `2 3 4 5 6 7 8 9`
> *Giải thích:* Bắt đầu từ 2, bước nhảy là +2, dừng trước 9. Các số sinh ra là 2, 4, 6, 8.

#### Câu 5 (Duyệt ngược với bước nhảy âm):
Để in ra các số từ 10 lùi về 1, câu lệnh `range` nào đúng?
- **A.** `range(10, 1)`
- **B.** `range(10, 1, -1)`
- **C.** **[Đáp án đúng]** `range(10, 0, -1)`
- **D.** `range(1, 10, -1)`
> *Giải thích:* Bắt đầu từ 10, muốn chạm đến 1 thì cận dừng phải là 0, bước nhảy là -1.

#### Câu 6 (Khởi tạo biến tính tổng):
Khi áp dụng thuật toán tính tổng các số trong vòng lặp, giá trị khởi tạo ban đầu của biến `tong` luôn là:
- **A.** `1`
- **B.** **[Đáp án đúng]** `0`
- **C.** `None`
- **D.** `10`
> *Giải thích:* Số 0 là phần tử trung hòa của phép cộng ($x + 0 = x$).

#### Câu 7 (Khởi tạo biến tính tích):
Khi áp dụng thuật toán tính tích lũy thừa hoặc giai thừa trong vòng lặp, giá trị khởi tạo ban đầu của biến `tich` bắt buộc phải là:
- **A.** `0`
- **B.** **[Đáp án đúng]** `1`
- **C.** `-1`
- **D.** Không cần khởi tạo
> *Giải thích:* Số 1 là phần tử trung hòa của phép nhân ($x \times 1 = x$). Nếu để bằng 0 thì kết quả luôn là 0.

#### Câu 8 (Bẫy thụt lề lệnh print):
Đoạn chương trình sau sẽ in ra bao nhiêu dòng lên màn hình?
```python
for i in range(3):
    print("Python")
```
- **A.** 1 dòng
- **B.** **[Đáp án đúng]** 3 dòng
- **C.** 2 dòng
- **D.** 4 dòng
> *Giải thích:* Lệnh `print` nằm trong vòng lặp chạy 3 lần, mỗi lần in 1 dòng `Python`.

#### Câu 9 (Bẫy lặp không chạy):
Vòng lặp `for i in range(5, 2):` sẽ chạy bao nhiêu lần?
- **A.** 3 lần
- **B.** **[Đáp án đúng]** 0 lần
- **C.** Báo lỗi cú pháp
- **D.** Vô tận lần
> *Giải thích:* Mặc định bước nhảy là +1. Đi từ 5 tiến lên thì không thể nào chạm tới cận dừng 2, nên vòng lặp kết thúc ngay lập tức mà không chạy lần nào.

#### Câu 10 (Dự đoán output — Tích lũy tổng):
Sau khi thực hiện đoạn code sau, giá trị của biến `s` là:
```python
s = 0
for i in range(1, 4):
    s += i * 2
```
- **A.** `6`
- **B.** **[Đáp án đúng]** `12`
- **C.** `8`
- **D.** `14`
> *Giải thích:* Các giá trị của $i$ là 1, 2, 3. Tổng $s = (1 \times 2) + (2 \times 2) + (3 \times 2) = 2 + 4 + 6 = 12$.

#### Câu 11 (Tính số lần lặp của range(a, b)):
Biểu thức `range(4, 15)` sinh ra bao nhiêu số nguyên?
- **A.** 10 số
- **B.** **[Đáp án đúng]** 11 số
- **C.** 12 số
- **D.** 15 số
> *Giải thích:* Số phần tử $= stop - start = 15 - 4 = 11$ số.

#### Câu 12 (Đếm số thỏa điều kiện):
Đoạn code sau đếm điều gì?
```python
dem = 0
for i in range(1, 21):
    if i % 2 == 0:
        dem += 1
```
- **A.** Tính tổng các số chẵn từ 1 đến 20.
- **B.** **[Đáp án đúng]** Đếm số lượng các số chẵn từ 1 đến 20.
- **C.** In các số chẵn từ 1 đến 20.
- **D.** Đếm các số lẻ từ 1 đến 20.
> *Giải thích:* `dem += 1` mỗi khi gặp số chia hết cho 2 là kỹ thuật đếm số lượng số chẵn.

#### Câu 13 (Biến lặp sau khi vòng lặp kết thúc):
Trong Python, sau khi vòng lặp `for i in range(1, 5): pass` kết thúc, giá trị của biến `i` bằng bao nhiêu?
- **A.** `5`
- **B.** **[Đáp án đúng]** `4`
- **C.** `0`
- **D.** Biến `i` bị xóa hoàn toàn khỏi bộ nhớ
> *Giải thích:* Giá trị cuối cùng được gán cho `i` trong vòng lặp là 4, sau khi thoát lặp biến `i` vẫn lưu giá trị 4 này.

#### Câu 14 (Duyệt bước nhảy lẻ):
Dãy số lẻ từ 1 đến 9 có thể được tạo ra bằng lệnh:
- **A.** `range(1, 10)`
- **B.** **[Đáp án đúng]** `range(1, 10, 2)`
- **C.** `range(1, 9, 2)`
- **D.** `range(0, 10, 2)`
> *Giải thích:* `range(1, 10, 2)` sinh ra các số 1, 3, 5, 7, 9.

#### Câu 15 (Tổng cấp số cộng):
Tổng $1 + 2 + 3 + \dots + 10$ bằng bao nhiêu?
- **A.** 50
- **B.** **[Đáp án đúng]** 55
- **C.** 45
- **D.** 60
> *Giải thích:* Công thức Gauss: $\frac{10 \times 11}{2} = 55$.

#### Câu 16 (Dự đoán output — In nối trên một hàng):
Đoạn code sau sẽ in ra gì?
```python
for i in range(3):
    print(i, end="")
```
- **A.** `123`
- **B.** **[Đáp án đúng]** `012`
- **C.** `0 1 2`
- **D.** Ba dòng: `0`, `1`, `2`
> *Giải thích:* Tham số `end=""` không xuống dòng và không cách, in liền dính các số 0, 1, 2.

#### Câu 17 (Vòng lặp lồng nhau cơ bản):
Đoạn code sau sẽ in ra bao nhiêu dấu sao `*`?
```python
for i in range(2):
    for j in range(3):
        print("*", end="")
```
- **A.** 5 dấu sao
- **B.** **[Đáp án đúng]** 6 dấu sao
- **C.** 2 dấu sao
- **D.** 3 dấu sao
> *Giải thích:* Vòng lặp ngoài chạy 2 lần, mỗi lần vòng lặp trong chạy 3 lần $\implies 2 \times 3 = 6$ lần in.

#### Câu 18 (Toán tử gán tăng tong += i):
Lệnh `tong += i` tương đương với:
- **A.** `tong = i`
- **B.** **[Đáp án đúng]** `tong = tong + i`
- **C.** `i = tong + i`
- **D.** `tong == tong + i`
> *Giải thích:* `+=` là cú pháp viết tắt của phép cộng dồn giá trị.

#### Câu 19 (Tính giai thừa 4!):
Kết quả của đoạn chương trình sau là:
```python
p = 1
for i in range(1, 5):
    p *= i
print(p)
```
- **A.** 10
- **B.** 20
- **C.** **[Đáp án đúng]** 24
- **D.** 120
> *Giải thích:* $p = 1 \times 2 \times 3 \times 4 = 24$.

#### Câu 20 (Quy tắc tối ưu trong thi đấu):
Khi cần tính tổng $S = 1 + 2 + \dots + N$ với $N = 10^9$, cách nào sau đây chạy nhanh nhất và không bị quá thời gian (TLE)?
- **A.** Dùng vòng lặp `for i in range(1, N + 1):`
- **B.** **[Đáp án đúng]** Áp dụng công thức toán học $\mathcal{O}(1)$: `S = N * (N + 1) // 2`
- **C.** Dùng vòng lặp `while`
- **D.** Đệ quy
> *Giải thích:* Vòng lặp $10^9$ bước sẽ chạy mất vài giây và bị TLE. Công thức toán $\mathcal{O}(1)$ tính ngay lập tức trong $0.0001\text{s}$.
