# Bài 05: Vòng lặp for và hàm range

## 1. Bản chất của vòng lặp trong khoa học máy tính

Trong lập trình, có những công việc phải làm đi làm lại hàng trăm, hàng nghìn lần (ví dụ: tính tổng các số từ 1 đến 1000, in danh sách tên, kiểm tra từng phần tử).

Nếu không có vòng lặp, các em phải gõ tay hàng nghìn dòng lệnh giống hệt nhau — không thể làm được! **Vòng lặp** giúp các em chỉ viết khối lệnh một lần rồi nhờ máy tính tự lặp lại.

Khi đã **biết trước chính xác số lần lặp**, công cụ chuẩn nhất trong Python là **vòng lặp `for` kết hợp với hàm `range()`**.

---

## 2. Chiếc thước đo `range()` toàn tập

Hàm `range()` rất đặc biệt: nó không tạo sẵn cả dãy số trong bộ nhớ, mà giống như một **máy nhả số tự động** — mỗi lần lặp cần một số mới, `range()` mới tính và đưa ra.

![Chiếc thước đo range](../../assets/l05_range_ruler.svg?v=1788575106)

### 2.1. Ba dạng sử dụng của hàm `range()`

| Dạng Cú Pháp | Số Tham Số | Ý Nghĩa Kỹ Thuật | Dãy Số Sinh Ra | Số Lần Lặp |
|---|:---:|---|---|:---:|
| `range(stop)` | 1 tham số | Bắt đầu từ số `0`, bước nhảy mặc định là `+1`, **dừng trước `stop`**. | `0, 1, 2, ..., stop - 1` | Đúng `stop` lần |
| `range(start, stop)` | 2 tham số | Bắt đầu từ `start`, bước nhảy mặc định `+1`, **dừng trước `stop`**. | `start, start + 1, ..., stop - 1` | `stop - start` lần |
| `range(start, stop, step)` | 3 tham số | Bắt đầu từ `start`, mỗi bước tăng/giảm `step`, **dừng trước `stop`**. | Các số cách đều nhau một khoảng `step` | Tính theo công thức |

> **ĐIỀU BẮT BUỘC PHẢI NHỚ: CẬN TRÊN `stop` LUÔN BỊ LOẠI TRỪ!**
> * Trong toán học, đoạn số thường lấy cả hai đầu mút $[1, 10]$.
> * Nhưng trong hàm `range(1, 10)`, số `10` **KHÔNG BAO GIỜ ĐƯỢC CHẠM TỚI**! Dãy số chỉ chạy đến số `9` là dừng lại.
> * Nếu muốn lặp qua các số từ $1$ đến $N$ đầy đủ, cận trên trong `range` bắt buộc phải là:
>  $$\mathbf{range(1, N + 1)}$$

### 2.2. Kỹ thuật duyệt số bước nhảy âm (Chạy lùi)

Khi `step` là số âm, `range()` sẽ đếm lùi từ số lớn về số bé. Số bắt đầu `start` phải lớn hơn số dừng `stop`:
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
 1. Ở vòng đầu tiên, `bien_lap` nhận giá trị đầu tiên do `range` sinh ra (`start`).
 2. Toàn bộ khối lệnh bên trong được thực thi.
 3. Chạy xong lệnh cuối, máy quay lên đầu và gán giá trị tiếp theo cho `bien_lap`.
 4. Lặp liên tục cho đến khi chạm giới hạn `stop` thì dừng.

---

## 4. Các mẫu thuật toán tích lũy kinh điển

Khi làm bài tập, vòng lặp `for` gần như luôn đi cùng kỹ thuật **tích lũy giá trị**.

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

## 6. Lỗi hay gặp và cách tránh

> **BẪY LỖI 1: ĐẶT LỆNH IN KẾT QUẢ VÀO BÊN TRONG THÂN VÒNG LẶP**
> * Xem đoạn code sai:
>  ```python
>   tong = 0
>   for i in range(1, n + 1):
>       tong += i
>       print(tong)  # Bị thụt lề vào trong vòng lặp!
>   ```
> * **Hậu quả:** Thay vì in ra 1 dòng kết quả duy nhất ở cuối, chương trình sẽ in ra $N$ dòng kết quả trung gian sau mỗi vòng lặp $\implies$ Bị chương trình kiểm tra chấm lỗi **kết quả sai** ngay lập tức!
> * **Quy tắc:** Lệnh in kết quả cuối cùng phải được **lùi ra ngoài ngang hàng với từ khóa `for`**.

> **BẪY LỖI 2: KHỞI TẠO BIẾN TÍCH BẰNG 0**
> * Khi tính tích hoặc giai thừa, nếu khởi tạo `tich = 0` thì $0 \times \text{bất kỳ số nào}$ cũng luôn bằng $0$. Kết quả cuối cùng sẽ luôn là $0$.
> * Luôn khởi tạo: `tong = 0` và `tich = 1`.

> **BẪY LỖI 3: QUÊN CỘNG 1 Ở CẬN TRÊN `range(1, n)`**
> * Viết `range(1, n)` sẽ chỉ chạy từ $1$ đến $n - 1$, dẫn đến thiếu mất số $n$ cuối cùng trong phép tính.

---

## 7. Mẫu code thường gặp

```python
# Mẫu tính tổng các số chẵn trong đoạn [A, B]
a, b = map(int, input().split())
tong_chan = 0

for i in range(a, b + 1):
    if i % 2 == 0:
        tong_chan += i

print(tong_chan)
```
