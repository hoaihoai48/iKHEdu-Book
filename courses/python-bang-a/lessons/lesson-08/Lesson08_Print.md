# Bài 08: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while

## 1. Khái niệm & Tầm quan trọng của Xử lý chữ số trong lập trình

Các bài toán về **chữ số của một số nguyên** gặp rất thường xuyên trong bài tập lập trình:
* Tính tổng, tích các chữ số.
* Đếm số lượng chữ số thỏa mãn tính chất (chẵn, lẻ, nguyên tố, chia hết).
* Tìm chữ số lớn nhất, chữ số nhỏ nhất, chữ số đầu tiên bên trái.
* Tạo số đảo ngược và kiểm tra số đối xứng.
* Kiểm tra số may mắn, số Armstrong, số tự mãn.

Nhớ cho cô: mỗi số nguyên hệ thập phân đều ghép từ các lũy thừa của 10. Muốn bóc từng chữ số mà không cần chuỗi ký tự, các em dùng cặp chia nguyên `//` và chia dư `%` cho 10 cùng vòng lặp `while`.

---

## 2. Cặp toán tử "Thần thánh": `// 10` và `% 10`

### 2.1. Phép toán `N % 10` (Bóc chữ số hàng đơn vị)
Chia một số nguyên cho 10, phần dư **chính là chữ số tận cùng bên phải**:
* $2026 \% 10 = \mathbf{6}$
* $789 \% 10 = \mathbf{9}$
* $5 \% 10 = \mathbf{5}$

### 2.2. Phép toán `N // 10` (Cắt bỏ chữ số hàng đơn vị)
Chia nguyên cho 10 là **bỏ chữ số tận cùng bên phải** để thu gọn số lại:
* $2026 // 10 = \mathbf{202}$
* $789 // 10 = \mathbf{78}$
* $5 // 10 = \mathbf{0}$

---

## 3. Khung thuật toán chuẩn bóc tách chữ số

Lặp lại hai thao tác trên trong `while N > 0:`, các em duyệt từng chữ số của $N$ từ **phải sang trái**:

```python
n = int(input())

# Lưu ý: Luôn xử lý trường hợp số 0 nếu bài toán yêu cầu
if n == 0:
    # Xử lý riêng trường hợp đặc biệt n = 0
    pass
else:
    while n > 0:
        chu_so = n % 10   # 1. Bóc chữ số tận cùng
        # 2. Xử lý nghiệp vụ với chu_so ở đây
        n //= 10          # 3. Cắt bỏ chữ số tận cùng để chuẩn bị cho vòng tiếp theo
```

### Minh họa thứ tự tách chữ số:
Với $N = 375$:
1. Vòng 1: `chu_so = 375 % 10 = 5`, thu gọn `n = 375 // 10 = 37`
2. Vòng 2: `chu_so = 37 % 10 = 7`, thu gọn `n = 37 // 10 = 3`
3. Vòng 3: `chu_so = 3 % 10 = 3`, thu gọn `n = 3 // 10 = 0`
4. Điều kiện `n > 0` thành `False` $\implies$ Vòng lặp kết thúc!

---

## 4. Các dạng bài toán kinh điển trên chữ số

### 4.1. Đếm số lượng chữ số của số nguyên $N$
* **Trường hợp $N = 0$:** Số 0 có đúng 1 chữ số $\implies$ In ra 1.
* **Trường hợp $N > 0$:**
  ```python
  n = int(input())
  if n == 0:
      print(1)
  else:
      dem = 0
      while n > 0:
          dem += 1
          n //= 10
      print(dem)
  ```

### 4.2. Tính tổng và tích các chữ số
* **Tính tổng:** Khởi tạo `tong = 0`, mỗi bước cộng dồn `tong += chu_so`.
* **Tính tích các chữ số khác 0:** Khởi tạo `tich = 1`. Nếu `chu_so != 0` thì nhân dồn `tich *= chu_so`.
  ```python
  n = int(input())
  tong = 0
  tich = 1
  while n > 0:
      d = n % 10
      tong += d
      if d != 0:
          tich *= d
      n //= 10
  print(tong, tich)
  ```

### 4.3. Tìm chữ số lớn nhất và nhỏ nhất
Khởi tạo `max_d = 0` và `min_d = 9`. Duyệt qua từng chữ số và cập nhật cực trị:
```python
n = int(input())
if n == 0:
    print(0, 0)
else:
    max_d = 0
    min_d = 9
    while n > 0:
        d = n % 10
        if d > max_d: max_d = d
        if d < min_d: min_d = d
        n //= 10
    print(max_d, min_d)
```

### 4.4. Tạo số đảo ngược
* **Ý nghĩa:** Cho số $N = 1234$, số đảo ngược thu được là $4321$.
* **Bản chất toán học:** Mỗi khi có một chữ số mới $d$, số đảo ngược hiện tại phải được dịch sang trái một hàng (nhân với 10), rồi cộng thêm $d$ vào hàng đơn vị:
  $$\mathbf{dao = dao \times 10 + d}$$
```python
n = int(input())
dao = 0
while n > 0:
    d = n % 10
    dao = dao * 10 + d
    n //= 10
print(dao)
```

### 4.5. Kiểm tra số đối xứng (Số Palindrome)
Một số nguyên là **số đối xứng** nếu đọc xuôi hay ngược đều giống nhau (ví dụ: $121, 1331, 2002, 7$).
* **Thuật toán:**
  1. Giữ lại giá trị ban đầu vào biến tạm: `goc = n`.
  2. Tạo số đảo ngược `dao` của $n$.
  3. So sánh `if dao == goc:` $\implies$ Số đối xứng!

```python
n = int(input())
goc = n
dao = 0

while n > 0:
    dao = dao * 10 + (n % 10)
    n //= 10

if dao == goc:
    print("YES")
else:
    print("NO")
```

---

## 5. Bảng mô phỏng biến thiên ô nhớ

### Thuật toán: Tạo số đảo ngược của $N = 375$
```python
n = 375
dao = 0
```

### Bảng theo dõi trạng thái bộ nhớ RAM qua từng vòng lặp:

| Vòng Lặp | `n` Ban Đầu | Tách `chu_so = n % 10` | Cập Nhật `dao = dao * 10 + chu_so` | Cắt Bỏ `n //= 10` | Trạng thái điều kiện `n > 0` |
|:---:|:---:|:---:|---|:---:|:---:|
| **Khởi tạo** | $375$ | Chưa có | `dao = 0` | $375$ | $375 > 0$ (Đúng) |
| **Vòng 1** | $375$ | **`5`** | `dao = 0 * 10 + 5 = 5` | **`37`** | $37 > 0$ (Đúng) |
| **Vòng 2** | $37$ | **`7`** | `dao = 5 * 10 + 7 = 57` | **`3`** | $3 > 0$ (Đúng) |
| **Vòng 3** | $3$ | **`3`** | `dao = 57 * 10 + 3 = 573` | **`0`** | $0 > 0$ (**Sai**) |
| **Dừng lặp** | $0$ | *(Thoát lặp vì n = 0)* | Giữ nguyên: **`573`** | Giữ nguyên: `0` | Kết thúc vòng lặp |

$$\implies \text{Kết quả: Số đảo ngược của } 375 \text{ là } \mathbf{573}$$

---

## 6. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: QUÊN LƯU LẠI GIÁ TRỊ GỐC CỦA BIẾN $N$**
> * Chạy xong `while n > 0:`, biến `n` đã về `0`, nên `if dao == n:` là so `dao` với `0` $\implies$ Sai hẳn!
> * **Điều bắt buộc phải nhớ:** Giữ giá trị ban đầu bằng `goc = n` trước khi vào vòng lặp.

> **BẪY LỖI 2: QUÊN XỬ LÝ TRƯỜNG HỢP BIÊN $N = 0$**
> * Với $N = 0$, `while n > 0:` không chạy bước nào nên bài "Đếm số chữ số" in ra `0` là sai (số 0 có đúng 1 chữ số).
> * **Khắc phục:** Thêm `if n == 0: print(1)`.

> **BẪY LỖI 3: DÙNG KIỂU CHUỖI KHI BÀI YÊU CẦU THUẬT TOÁN SỐ**
> * Dù viết `s = str(n)` cũng được, các em vẫn nên làm chủ cặp `//` và `%` vì đó là tư duy thuật toán cốt lõi, code chạy nhanh và dễ chuyển sang ngôn ngữ khác (C++, Java).

---

## 7. Mẫu code thường gặp

### Mẫu 1: Tìm chữ số đầu tiên bên trái (hàng cao nhất) của số $N$
```python
n = int(input())
while n >= 10:
    n //= 10
print(n)
```

### Mẫu 2: Đếm số lượng chữ số chẵn và lẻ
```python
n = int(input())
chan = 0
le = 0

if n == 0:
    chan = 1
else:
    while n > 0:
        d = n % 10
        if d % 2 == 0:
            chan += 1
        else:
            le += 1
        n //= 10

print(chan, le)
```

### Mẫu 3: Đếm các số đối xứng trong đoạn $[A, B]$
```python
a, b = map(int, input().split())
dem = 0

for x in range(a, b + 1):
    goc = x
    dao = 0
    t = x
    while t > 0:
        dao = dao * 10 + (t % 10)
        t //= 10
    if dao == goc:
        dem += 1

print(dem)
```

---
