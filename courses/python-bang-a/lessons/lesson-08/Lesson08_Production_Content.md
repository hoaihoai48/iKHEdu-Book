# Bài 08: Vòng lặp while và biến cờ

---

## 1. Khởi động: Khi không biết trước phải làm bao nhiêu lần?

Ở Bài 7, chúng ta đã học vòng lặp `for` — đó là khi em **biết trước chính xác số lần cần lặp** (ví dụ: lặp đúng 10 lần, hay chạy từ 1 đến $N$).
Nhưng trong đời sống thực tế, có rất nhiều tình huống chúng ta **KHÔNG THỂ BIẾT TRƯỚC số lần lặp**:
* Chơi trò chơi điện tử: Em chơi **CHO ĐẾN KHI HẾT MẠNG THÌ DỪNG**. (Có thể chơi 2 phút, có thể chơi 1 tiếng).
* Đọc dữ liệu từ bàn phím: Người dùng nhập các số liên tục **CHO ĐẾN KHI NHẬP SỐ 0 THÌ DỪNG** (như *Bài 6 Đề thi THT Đà Lạt*).
* Đoán số bí mật: Em đoán **CHO ĐẾN KHI NÀO ĐOÁN ĐÚNG THÌ THÔI**.

Trong Python, chiếc chìa khóa vạn năng cho các bài toán "lặp có điều kiện" này chính là **Vòng lặp `while` (TRONG KHI...)**!

---

## 2. Cú pháp và bản chất của `while`

### 2.1. Cú pháp chuẩn
```python
while <Điều kiện còn ĐÚNG>:
    # Làm các công việc này lặp đi lặp lại
    # Bắt buộc phải có câu lệnh làm thay đổi điều kiện (để tránh lặp vô tận!)
```

### 2.2. Trực giác người lính gác cổng:
Mỗi khi chuẩn bị bước vào vòng lặp, người lính gác sẽ chặn lại và hỏi: *"Điều kiện có còn ĐÚNG không?"*:
* **Nếu ĐÚNG:** Mở cửa cho chạy các câu lệnh bên trong. Chạy xong lại quay lên gặp người lính gác để hỏi tiếp.
* **Nếu SAI:** Lập tức đóng cửa và kết thúc vòng lặp ngay!

```python
# Ví dụ: Đếm từ 1 đến 5 bằng while
dem = 1
while dem <= 5:
    print(dem)
    dem = dem + 1 # RẤT QUAN TRỌNG: Tăng biến đếm để có lúc dem > 5!
```

> ⚠️ **Tử huyệt bắt bẫy kinh điển: lặp vô tận (Infinite Loop)!**
> Nếu em quên viết dòng `dem = dem + 1`, thì giá trị của `dem` sẽ mãi mãi bằng $1$.
> Điều kiện `1 <= 5` sẽ mãi mãi ĐÚNG $\implies$ Chương trình sẽ chạy mãi mãi không bao giờ dừng lại, làm đơ máy tính!

---

## 3. Lệnh thoát hiểm thần kỳ: `break` và `continue`

* **`break` (Phanh gấp):** Lập tức đập vỡ vòng lặp và nhảy vọt ra ngoài, bất chấp điều kiện của vòng lặp là gì.
* **`continue` (Bỏ qua bước này):** Bỏ qua các câu lệnh còn lại của vòng lặp hiện tại và nhảy ngay sang lần lặp kế tiếp.

### Mẫu bài toán kinh điển: Nhập đến khi gặp số 0 thì dừng
```python
tong = 0

while True: # Vòng lặp chạy vô hạn
    x = int(input())
    if x == 0:
        break # Gặp số 0 thì phanh gấp thoát ra ngoài!
    tong = tong + x

print("Tong cac so da nhap la:", tong)
```

---

## 4. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Vòng lặp `while` sẽ tiếp tục chạy khi nào?
- **A.** Khi điều kiện có giá trị là `False`
- **B.** **[Đáp án đúng]** Khi điều kiện có giá trị là `True`
- **C.** Chỉ chạy đúng 1 lần
- **D.** Khi gặp lệnh `break`
> *Giải thích:* `while` có nghĩa là "trong khi điều kiện còn đúng thì còn lặp".

#### Câu 2: Điều gì xảy ra nếu điều kiện trong `while` luôn luôn đúng và không có lệnh `break`?
- **A.** Chương trình tự động dừng sau 100 lần
- **B.** **[Đáp án đúng]** Bị lặp vô tận (Infinite Loop) khiến chương trình không bao giờ kết thúc
- **C.** Máy tính báo lỗi `SyntaxError`
- **D.** Tự động in ra số 0
> *Giải thích:* Vòng lặp không có lối thoát sẽ chạy mãi mãi.

#### Câu 3: Lệnh nào sau đây dùng để lập tức thoát khỏi vòng lặp `while`?
- **A.** `stop`
- **B.** `exit()`
- **C.** **[Đáp án đúng]** `break`
- **D.** `continue`
> *Giải thích:* Từ khóa `break` dùng để bẻ gãy và thoát ngay khỏi vòng lặp.

#### Câu 4: Đoạn code sau in ra màn hình bao nhiêu số?
```python
x = 1
while x < 5:
    print(x)
    x = x + 2
```
- **A.** 5 số
- **B.** **[Đáp án đúng]** 2 số (gồm số 1 và số 3)
- **C.** 4 số
- **D.** 3 số
> *Giải thích:* Lần 1: $x = 1$ in 1, tăng $x = 3$. Lần 2: $x = 3 < 5$ in 3, tăng $x = 5$. Khi $x = 5$, điều kiện $5 < 5$ bị sai nên dừng. In 2 số.

#### Câu 5: Lệnh `continue` trong vòng lặp có tác dụng gì?
- **A.** Thoát hoàn toàn khỏi chương trình
- **B.** Thoát khỏi vòng lặp
- **C.** **[Đáp án đúng]** Bỏ qua phần còn lại của lần lặp hiện tại và chuyển sang lần lặp tiếp theo
- **D.** Quay lại từ đầu chương trình
> *Giải thích:* `continue` bỏ qua các câu lệnh phía dưới nó trong thân vòng lặp hiện tại.

#### Câu 6: Đoạn code sau in ra giá trị cuối cùng của `k` là bao nhiêu?
```python
k = 10
while k > 0:
    k = k - 3
print(k)
```
- **A.** `1`
- **B.** `0`
- **C.** **[Đáp án đúng]** `-2`
- **D.** `3`
> *Giải thích:* Các giá trị của $k$: $10 \to 7 \to 4 \to 1 \to -2$. Khi $k = -2 \ngtr 0$ thì vòng lặp dừng, in ra $-2$.

#### Câu 7: Vòng lặp sau chạy bao nhiêu lần?
```python
while False:
    print("Python")
```
- **A.** 1 lần
- **B.** Vô tận lần
- **C.** **[Đáp án đúng]** 0 lần (Không chạy lần nào)
- **D.** Báo lỗi cú pháp
> *Giải thích:* Điều kiện là `False` ngay từ đầu nên người lính gác không cho vào vòng lặp lần nào.

#### Câu 8: Đoạn code nào sau đây nhập số từ bàn phím cho đến khi người dùng nhập số 0 thì dừng?
- **A.** `for i in range(0): input()`
- **B.** **[Đáp án đúng]** `while True: x = int(input()); if x == 0: break`
- **C.** `while x == 0: x = int(input())`
- **D.** `while x != 0: break`
> *Giải thích:* Mẫu `while True:` kết hợp với `if x == 0: break` là kỹ thuật nhập dữ liệu chuẩn mực.

#### Câu 9: Muốn gấp đôi số tiền $1000$ đồng cho đến khi số tiền vượt quá $10000$ đồng, ta dùng điều kiện `while` nào?
- **A.** `while tien > 10000:`
- **B.** **[Đáp án đúng]** `while tien <= 10000:`
- **C.** `while tien == 10000:`
- **D.** `while tien >= 1000:`
> *Giải thích:* Trong khi số tiền còn $\le 10000$ thì ta vẫn tiếp tục nhân đôi.

#### Câu 10: Đoạn code sau in ra gì?
```python
i = 0
while i < 3:
    i = i + 1
    if i == 2:
        continue
    print(i, end=" ")
```
- **A.** `1 2 3`
- **B.** `1 2`
- **C.** **[Đáp án đúng]** `1 3`
- **D.** `2 3`
> *Giải thích:* Khi $i = 2$, lệnh `continue` bỏ qua lệnh `print`, nên số 2 không được in.

#### Câu 11: Cho đoạn code sau:
```python
n = 123
dem = 0
while n > 0:
    n = n // 10
    dem = dem + 1
print(dem)
```
Kết quả in ra là gì?
- **A.** `0`
- **B.** `1`
- **C.** `2`
- **D.** **[Đáp án đúng]** `3`
> *Giải thích:* Đây là thuật toán đếm số lượng chữ số! $123 \to 12 \to 1 \to 0$. Lặp đúng 3 lần, đếm được 3 chữ số.

#### Câu 12: So sánh giữa `for` và `while`:
- **A.** `for` mạnh hơn `while`, làm được mọi bài toán mà `while` không làm được
- **B.** `while` không bao giờ dùng được cho dãy số
- **C.** **[Đáp án đúng]** Mọi bài toán dùng `for` đều có thể viết lại được bằng `while`
- **D.** Cả hai lệnh này bắt buộc phải dùng cùng nhau
> *Giải thích:* `while` là vòng lặp tổng quát, có thể mô phỏng lại mọi vòng lặp `for`.

#### Câu 13: Đoạn code sau có bị lặp vô tận không?
```python
x = 5
while x > 0:
    print(x)
    x = x + 1
```
- **A.** Không, nó dừng khi $x = 100$
- **B.** **[Đáp án đúng]** Có, vì $x$ ban đầu bằng 5 và càng ngày càng tăng, nên luôn luôn $> 0$
- **C.** Python tự động dừng sau 1 giây
- **D.** Báo lỗi `MemoryError`
> *Giải thích:* $x$ tăng dần $5, 6, 7, \dots$ nên điều kiện $x > 0$ mãi mãi đúng.

#### Câu 14: Biến cờ (flag) trong lập trình là gì?
- **A.** Một biến để vẽ lá cờ
- **B.** **[Đáp án đúng]** Một biến kiểu `bool` (`True`/`False`) dùng để đánh dấu một sự kiện đã xảy ra hay chưa
- **C.** Một lệnh dừng chương trình
- **D.** Tên một thư viện trong Python
> *Giải thích:* Biến Flag (ví dụ: `tim_thay = False`) dùng như một cột mốc đánh dấu trong vòng lặp.
