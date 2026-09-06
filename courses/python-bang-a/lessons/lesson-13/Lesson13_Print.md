# Bài 13: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự

## 1. Bản chất khoa học máy tính: Chuỗi ký tự trong bộ nhớ RAM

Chuỗi ký tự (`str`) là một **dãy các ký tự xếp liền nhau theo thứ tự** trong bộ nhớ. Mỗi ký tự có một vị trí cố định gọi là **chỉ số (index)**. Python dùng hai chiều chỉ số rất thuận tiện:
* **Chỉ số dương:** Bắt đầu từ $0$ ở ký tự đầu bên trái, tăng dần đến $\text{len}(s) - 1$ ở ký tự cuối.
* **Chỉ số âm:** Bắt đầu từ $-1$ ở ký tự cuối bên phải, giảm dần về $-\text{len}(s)$ ở ký tự đầu.

![Hệ thống chỉ số dương và âm của chuỗi ký tự](../../assets/l13_string_indexing.svg?v=1788575106)

### Bảng tra cứu chỉ số chuỗi với ví dụ `s = "PYTHON"`:

| Chiều duyệt | Ký tự 1 | Ký tự 2 | Ký tự 3 | Ký tự 4 | Ký tự 5 | Ký tự 6 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| **Ký tự thực tế** | `'P'` | `'Y'` | `'T'` | `'H'` | `'O'` | `'N'` |
| **Chỉ số dương (Từ trái sang phải)** | `0` | `1` | `2` | `3` | `4` | `5` |
| **Chỉ số âm (Từ phải sang trái)** | `-6` | `-5` | `-4` | `-3` | `-2` | `-1` |

### Các cú pháp truy cập cơ bản:

```python
s = "PYTHON"

print(s[0])     # In ra: 'P'  (Ký tự đầu tiên)
print(s[5])     # In ra: 'N'  (Ký tự cuối cùng: index = len(s) - 1)
print(s[-1])    # In ra: 'N'  (Ký tự cuối cùng dùng chỉ số âm)
print(s[-2])    # In ra: 'O'  (Ký tự áp chót)
print(len(s))   # In ra: 6    (Độ dài chuỗi - tổng số lượng ký tự)
```

> **Điều bắt buộc phải nhớ: Lỗi vượt quá chỉ số (`IndexError`)**
> * Nếu chuỗi có độ dài $N = \text{len}(s)$, chỉ số dương hợp lệ chỉ nằm trong đoạn $[0, N - 1]$.
> * Truy cập vào `s[N]` hoặc `s[len(s)]` sẽ khiến chương trình dừng đột ngột với lỗi: `IndexError: string index out of range`.
> * Với chuỗi rỗng `s = ""`, độ dài bằng 0, mọi thao tác truy cập `s[0]` đều gây lỗi ngay.

---

## 2. Kỹ thuật cắt lát chuỗi — Trích xuất chuỗi con

Cắt lát giúp lấy ra một đoạn ký tự liên tiếp hoặc cách quãng từ chuỗi ban đầu để tạo chuỗi con mới.

### Cú pháp tổng quát:
$$\mathbf{s[\text{start} : \text{stop} : \text{step}]}$$

* `start`: Vị trí bắt đầu lấy (mặc định là $0$ nếu để trống).
* `stop`: Vị trí kết thúc (nhưng **luôn bị loại trừ**, chỉ lấy đến $\text{stop} - 1$).
* `step`: Bước nhảy (mặc định là $1$). Bước nhảy âm nghĩa là đi lùi.

### Bảng các mẫu cắt lát kinh điển khi làm bài:

| Cú pháp cắt lát | Quy tắc trích xuất | Ví dụ với `s = "ABCDEFGH"` | Chuỗi con kết quả |
|---|---|---|:---:|
| `s[2:5]` | Lấy từ vị trí $2$ đến vị trí $4$ | `s[2:5]` | `"CDE"` |
| `s[:4]` | Bỏ trống `start`: Lấy từ đầu đến vị trí $3$ | `s[:4]` | `"ABCD"` |
| `s[3:]` | Bỏ trống `stop`: Lấy từ vị trí $3$ đến hết chuỗi | `s[3:]` | `"DEFGH"` |
| `s[::2]` | Lấy từ đầu đến cuối với bước nhảy $2$ | `s[::2]` | `"ACEG"` |
| `s[1::2]` | Lấy từ vị trí $1$ với bước nhảy $2$ (vị trí lẻ) | `s[1::2]` | `"BDFH"` |
| `s[::-1]` | **Bí thuật đảo ngược chuỗi**: Bước nhảy $-1$ | `s[::-1]` | `"HGFEDCBA"` |

```python
s = "iKHEDU2026"

print(s[0:6])   # "iKHEDU" (Lấy 6 ký tự đầu tiên)
print(s[:6])    # "iKHEDU" (Cách viết gọn tương đương)
print(s[6:])    # "2026"   (Lấy từ vị trí thứ 6 đến hết)
print(s[::-1])  # "6202UDEHKi" (Đảo ngược toàn bộ chuỗi)
```

> 💡 **Quy tắc khoảng bán mở $[start, stop)$:**
> Quy tắc cận trên `stop` bị loại trừ dùng chung cho `range(start, stop)` và `s[start:stop]`. Số ký tự lấy ra khi `step = 1` luôn bằng: $\text{stop} - \text{start}$.

---

## 3. Đặc tính bất biến của chuỗi ký tự

Đây là điểm khác nhau quan trọng nhất giữa chuỗi (`str`) và danh sách (`list`):

* **Chuỗi trong Python là bất biến:** Khi chuỗi đã có trong bộ nhớ, ta **không thể sửa hay gán đè trực tiếp** từng ký tự của nó.

```python
s = "HELLO"

# Cố gắng sửa chữ 'H' thành chữ 'J':
# s[0] = "J"
# Báo lỗi nghiêm trọng: TypeError: 'str' object does not support item assignment
```

### Cách xử lý chuẩn xác khi muốn thay đổi ký tự trong chuỗi:
Ta phải **tạo một chuỗi hoàn toàn mới** bằng phép ghép (`+`) hoặc cắt lát:

```python
s = "HELLO"

# ĐÚNG: Ghép ký tự mới với phần đuôi còn lại của chuỗi
s = "J" + s[1:]
print(s)  # In ra: "JELLO"
```

---

## 4. Các phương thức duyệt chuỗi bằng vòng lặp

Duyệt chuỗi là đi thăm từng ký tự để kiểm tra, đếm hoặc tính toán.

### 4.1. Duyệt trực tiếp từng ký tự bằng `for ... in`
Dùng khi chỉ cần quan tâm giá trị từng ký tự, không cần biết vị trí:

```python
s = input()
for ch in s:
    print(ch)
```

### 4.2. Duyệt qua chỉ số bằng `for i in range(len(s))`
Dùng khi cần dựa vào vị trí, ví dụ: xét ký tự cạnh nhau, hoặc chỉ xét vị trí chẵn/lẻ:

```python
s = input()
for i in range(len(s)):
    # s[i] là ký tự tại vị trí thứ i
    if i % 2 == 0:
        print(f"Ký tự tại vị trí chẵn {i}: {s[i]}")
```

### 4.3. Duyệt cặp ký tự liền kề
Mẫu kiểm tra hai ký tự giống nhau đứng cạnh nhau:

```python
s = input()
dem_trung = 0
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        dem_trung += 1
print(dem_trung)
```

---

## 5. Bảng mô phỏng biến thiên ô nhớ

### Thuật toán: Kiểm tra chuỗi có đối xứng hay không bằng hai con trỏ

```python
s = "RADAR"
la_doi_xung = True
n = len(s)

for i in range(n // 2):
    if s[i] != s[n - 1 - i]:
        la_doi_xung = False
        break

if la_doi_xung:
    print("YES")
else:
    print("NO")
```

| Bước | Vòng lặp `i` | So sánh `s[i]` và `s[n - 1 - i]` | Kết quả so sánh | Biến `la_doi_xung` | Trạng thái thực thi |
|:---:|:---:|:---:|:---:|:---:|---|
| Khởi tạo | — | — | — | `True` | $n = 5$, vòng lặp chạy $i \in [0, 1]$ |
| 1 | $i = 0$ | `s[0]` ('R') so với `s[4]` ('R') | `'R' == 'R'` | `True` | Thỏa mãn, tiếp tục vòng lặp |
| 2 | $i = 1$ | `s[1]` ('A') so với `s[3]` ('A') | `'A' == 'A'` | `True` | Thỏa mãn, tiếp tục vòng lặp |
| Kết thúc | — | — | — | `True` | Hết vòng lặp, in ra `YES` |

---

## 6. Lỗi hay gặp và bẫy lỗi kinh điển

> **Lỗi hay gặp 1: Tìm kiếm bằng `find()` trả về `-1`**
> * `s.find(sub)` tìm vị trí đầu tiên của `sub` trong `s`. Nếu không thấy, hàm trả về `-1` (chương trình vẫn chạy tiếp).
> * Nếu viết `if s.find("a"):` sẽ sai! Vì số `-1` được coi là `True` trong biểu thức điều kiện.
> * **Cách viết an toàn:** `if s.find("a") != -1:` hoặc: `if "a" in s:`.

> **Lỗi hay gặp 2: Nhầm lẫn giữa phép nối chuỗi và cộng số**
> * Khi đọc bằng `input()`, nhập số `12` thì ta vẫn nhận được chuỗi `"12"`.
> * `"12" + "34"` cho ra `"1234"` (ghép chuỗi).
> * **Cách viết an toàn:** Đổi sang số nguyên bằng `int()` trước khi tính toán.

> **Lỗi hay gặp 3: Phân biệt chữ hoa và chữ thường trong phép so sánh**
> * Trong Python, `'A' == 'a'` luôn cho `False`.
> * Khi bài yêu cầu không phân biệt hoa thường, em chuẩn hóa về một dạng: `if s1.lower() == s2.lower():`.

---

## 7. Mẫu code thường gặp

### 7.1. Mẫu kiểm tra chuỗi đối xứng
```python
s = input()
if s == s[::-1]:
    print("YES")
else:
    print("NO")
```

### 7.2. Mẫu xóa bỏ ký tự tại vị trí chỉ định $K$
```python
s = input()
k = int(input())
# Trích xuất đoạn trước k và đoạn sau k rồi ghép lại
ket_qua = s[:k] + s[k + 1:]
print(ket_qua)
```

### 7.3. Mẫu đếm số lần xuất hiện của một ký tự bằng vòng lặp
```python
s = input()
ky_tu_can_tim = input()
dem = 0

for ch in s:
    if ch == ky_tu_can_tim:
        dem += 1

print(dem)
```
