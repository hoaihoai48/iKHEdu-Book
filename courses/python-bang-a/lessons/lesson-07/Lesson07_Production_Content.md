# Bài 07: Vòng lặp for và hàm range

---

## 1. Khởi động: Sức mạnh siêu phàm của robot — làm đi làm lại không biết mệt!

Con người chúng ta nếu phải viết đi viết lại một câu 100 lần thì sẽ rất mỏi tay và buồn ngủ.
Nhưng với bạn Robot Python, nếu em bảo bạn ấy: *"Hãy in ra 1,000 dòng chữ!"* hay *"Hãy tính tổng từ 1 đến 1,000,000!"*, bạn ấy sẽ làm xong ngay lập tức chỉ trong **chưa đầy 1 giây** mà không hề than thở một lời!

Khả năng lặp đi lặp lại một công việc nhiều lần với tốc độ ánh sáng được gọi là **VÒNG LẶP (Loop)**.
Và công cụ đầu tiên, mạnh mẽ nhất, phổ biến nhất chính là **Vòng lặp `for` kết hợp với hàm `range()`**!

---

## 2. Giải mã hàm `range()`: Chiếc thước kẻ vạch số thần kỳ

Trước khi học lệnh `for`, các em bắt buộc phải hiểu được bí mật của hàm **`range()`**.
Hàm `range()` giống như một chiếc máy tự động in ra một dãy số theo quy luật. Có 3 cách dùng `range()`:

### Cách 1: `range(stop)` — dãy số từ 0 đến sát nút `stop`
Khi chỉ truyền 1 con số: `range(5)`
$\implies$ Máy sẽ sinh ra dãy 5 số bắt đầu từ 0: `0, 1, 2, 3, 4`
> ⚠️ **Tử huyệt bắt bẫy số 1:** Máy tính dừng lại ngay **TRƯỚC** con số `stop` (không lấy số 5)!

### Cách 2: `range(start, stop)` — dãy số từ `start` đến sát `stop`
Khi truyền 2 số: `range(1, 6)`
$\implies$ Máy sẽ sinh ra dãy số bắt đầu từ 1 đến 5: `1, 2, 3, 4, 5` (dừng trước 6).

### Cách 3: `range(start, stop, step)` — dãy số có bước nhảy `step`
Khi truyền 3 số: con số thứ ba `step` là **bước nhảy (khoảng cách giữa các số)**:
* `range(1, 10, 2)`: Bắt đầu từ 1, mỗi lần nhảy 2 bước $\implies$ `1, 3, 5, 7, 9` (Dãy số lẻ!).
* `range(10, 0, -1)`: Bắt đầu từ 10, bước nhảy âm $-1$ (Đếm ngược!) $\implies$ `10, 9, 8, ..., 1` (Dừng trước 0).

---

## 3. Cú pháp vòng lặp `for`: Điểm danh từng phần tử

```python
for <Biến_Đếm> in range(...):
    # Khối lệnh được lặp đi lặp lại (Nhớ thụt lề 4 dấu cách!)
```

### Ví dụ 1: Robot đếm số từ 1 đến 5
```python
for i in range(1, 6):
    print("So thu tu:", i)
```
**Màn hình in ra:**
```text
So thu tu: 1
So thu tu: 2
So thu tu: 3
So thu tu: 4
So thu tu: 5
```

---

## 4. Kỹ thuật "ống heo tiết kiệm": Tính tổng dồn dập

Đây là mẫu bài toán kinh điển nhất trong lập trình Tiểu học: **Tính tổng $S = 1 + 2 + 3 + \dots + N$**.

### Trực giác đời sống:
Tưởng tượng em có một chiếc **ống heo rỗng** (ban đầu `tong = 0`).
Mỗi ngày trôi qua, em bỏ thêm `i` đồng vào ống heo:
* Ngày 1: bỏ 1 đồng $\implies$ ống heo có $0 + 1 = 1$.
* Ngày 2: bỏ 2 đồng $\implies$ ống heo có $1 + 2 = 3$.
* Ngày 3: bỏ 3 đồng $\implies$ ống heo có $3 + 3 = 6$.
* Cứ thế đến ngày thứ $N$.

```python
N = int(input())

tong = 0 # Ống heo ban đầu rỗng

for i in range(1, N + 1): # Chú ý N + 1 để lấy được tới N!
    tong = tong + i

print("Tong cac so la:", tong)
```

---

## 5. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Hàm `range(5)` tạo ra dãy số gồm những số nào?
- **A.** `1, 2, 3, 4, 5`
- **B.** **[Đáp án đúng]** `0, 1, 2, 3, 4`
- **C.** `0, 1, 2, 3, 4, 5`
- **D.** `1, 2, 3, 4`
> *Giải thích:* Mặc định `range(N)` bắt đầu từ 0 và dừng trước $N$.

#### Câu 2: Để vòng lặp chạy đúng các giá trị `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`, ta viết:
- **A.** `range(1, 10)`
- **B.** **[Đáp án đúng]** `range(1, 11)`
- **C.** `range(0, 10)`
- **D.** `range(1, 10, 1)`
> *Giải thích:* Cận trên phải là $11$ thì vòng lặp mới chạy đến hết số $10$.

#### Câu 3: Đoạn code sau in ra màn hình bao nhiêu dòng?
```python
for i in range(4):
    print("Python")
```
- **A.** 3 dòng
- **B.** **[Đáp án đúng]** 4 dòng (ứng với $i = 0, 1, 2, 3$)
- **C.** 5 dòng
- **D.** Vô hạn dòng
> *Giải thích:* `range(4)` có 4 giá trị nên lệnh `print` chạy 4 lần.

#### Câu 4: Kết quả của đoạn code sau là gì?
```python
s = 0
for i in range(1, 4):
    s = s + i
print(s)
```
- **A.** `3`
- **B.** **[Đáp án đúng]** `6`
- **C.** `10`
- **D.** `0`
> *Giải thích:* $s = 0 + 1 + 2 + 3 = 6$.

#### Câu 5: Cú pháp nào sau đây in ra các số chẵn từ 2 đến 10?
- **A.** `range(2, 10)`
- **B.** **[Đáp án đúng]** `range(2, 11, 2)`
- **C.** `range(2, 10, 2)`
- **D.** `range(0, 10, 2)`
> *Giải thích:* Bắt đầu từ 2, bước nhảy 2, dừng trước 11 sẽ gồm: `2, 4, 6, 8, 10`.

#### Câu 6: Để đếm ngược từ 5 về 1, ta viết:
- **A.** `range(5, 1, -1)`
- **B.** **[Đáp án đúng]** `range(5, 0, -1)`
- **C.** `range(5, -1, 0)`
- **D.** `range(1, 5, -1)`
> *Giải thích:* Bắt đầu từ 5, dừng trước 0 với bước nhảy âm $-1$ sẽ ra: `5, 4, 3, 2, 1`.

#### Câu 7: Bẫy thụt lề: Đoạn code sau in ra gì?
```python
tong = 0
for i in range(1, 4):
    tong = tong + i
    print(tong)
```
- **A.** Chỉ in một số 6
- **B.** **[Đáp án đúng]** In 3 dòng lần lượt là: `1`, `3`, `6`
- **C.** In `0, 1, 3, 6`
- **D.** Báo lỗi
> *Giải thích:* Vì lệnh `print(tong)` bị thụt lề nằm BÊN TRONG vòng lặp `for`, nên sau mỗi bước lặp nó đều in ra giá trị hiện tại của `tong`.

#### Câu 8: Đoạn code sau in ra gì?
```python
for i in range(5, 5):
    print("Hello")
```
- **A.** In 1 chữ Hello
- **B.** In 5 chữ Hello
- **C.** **[Đáp án đúng]** Không in ra gì cả
- **D.** Báo lỗi
> *Giải thích:* `start = 5` và `stop = 5`, khoảng rỗng nên vòng lặp không chạy lần nào.

#### Câu 9: Trong vòng lặp `for i in range(1, 10):`, sau mỗi lần lặp, biến `i` tự động:
- **A.** Giữ nguyên giá trị
- **B.** **[Đáp án đúng]** Tự động tăng lên 1 đơn vị
- **C.** Tự động giảm đi 1 đơn vị
- **D.** Bị xóa khỏi bộ nhớ
> *Giải thích:* Bước nhảy mặc định của `range` là $+1$.

#### Câu 10: Vòng lặp `for` thường được dùng trong trường hợp nào?
- **A.** Khi không biết trước số lần lặp
- **B.** **[Đáp án đúng]** Khi đã biết trước số lần lặp cụ thể
- **C.** Khi muốn chương trình chạy mãi mãi không dừng
- **D.** Khi muốn chia lấy dư
> *Giải thích:* Vòng lặp `for` là vòng lặp với số lần biết trước (xác định bởi số phần tử của dãy).

#### Câu 11: Đoạn code tính giai thừa $3! = 1 \times 2 \times 3$ nào sau đây đúng?
- **A.** `tich = 0; for i in range(1, 4): tich = tich * i`
- **B.** **[Đáp án đúng]** `tich = 1; for i in range(1, 4): tich = tich * i`
- **C.** `tich = 1; for i in range(1, 3): tich = tich * i`
- **D.** `tich = 3 * 2 * 1`
> *Giải thích:* Tính tích bắt buộc biến khởi tạo phải là $1$. Nếu gán `tich = 0` thì $0$ nhân với số nào cũng bằng $0$!

#### Câu 12: Đoạn code sau in ra gì?
```python
dem = 0
for i in range(1, 11):
    if i % 2 != 0:
        dem = dem + 1
print(dem)
```
- **A.** `10`
- **B.** **[Đáp án đúng]** `5`
- **C.** `25`
- **D.** `4`
> *Giải thích:* Từ 1 đến 10 có đúng 5 số lẻ ($1, 3, 5, 7, 9$). Mỗi lần gặp số lẻ thì `dem` tăng 1, vậy kết quả là 5.

#### Câu 13: Giá trị của `i` sau khi kết thúc vòng lặp `for i in range(3): pass` là:
- **A.** `0`
- **B.** `1`
- **C.** **[Đáp án đúng]** `2`
- **D.** `3`
> *Giải thích:* Giá trị cuối cùng được gán cho `i` trong `range(3)` là số 2.

#### Câu 14: Biểu thức `range(10, 2, -2)` sinh ra những số nào?
- **A.** `10, 8, 6, 4, 2`
- **B.** **[Đáp án đúng]** `10, 8, 6, 4`
- **C.** `8, 6, 4, 2`
- **D.** `10, 9, 8`
> *Giải thích:* Dừng trước 2 nên chỉ lấy: $10, 8, 6, 4$.

#### Câu 15: Công thức tính nhanh tổng $1 + 2 + \dots + N$ trong toán học mà không cần dùng vòng lặp là:
- **A.** $N \times (N + 1)$
- **B.** **[Đáp án đúng]** $N \times (N + 1) // 2$
- **C.** $(N + 1) // 2$
- **D.** $N \times N // 2$
> *Giải thích:* Công thức tính tổng cấp số cộng Gauss: $S = \frac{N(N+1)}{2}$. Khi $N = 10^9$, dùng công thức này tính trong 0.00001s thay vì lặp $10^9$ lần!
