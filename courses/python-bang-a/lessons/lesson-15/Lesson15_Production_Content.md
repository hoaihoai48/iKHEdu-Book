# Bài 15: Chiến lược giải đề thi lập trình Python

## 1. Bản đồ 5 bước tác chiến trong phòng thi

Trong bất kỳ kỳ thi lập trình nào, từ cấp trường đến cấp quốc gia, thí sinh cần tuân thủ **quy trình 5 bước** để tối đa hóa điểm số và giảm thiểu lỗi sai:

### Bước 1: Đọc đề cẩn thận (Tối thiểu 2 lần)

- Lần 1: Đọc lướt toàn bộ để nắm bức tranh tổng quan.
- Lần 2: Đọc kỹ từng dòng, **gạch chân**: giới hạn dữ liệu ($N \le ?$), định dạng Input/Output, các trường hợp đặc biệt.

> ⚠️ **Lưu ý:** Nhiều thí sinh mất điểm oan vì đọc lướt bỏ qua chi tiết nhỏ: "in ra **trên cùng một dòng**", "cách nhau **một dấu cách**", "kết quả là **số nguyên**"...

### Bước 2: Nháp thuật toán và Dry Run trên giấy

- Xác định rõ: **Input là gì? Output cần gì? Công thức/Logic xử lý?**
- Mô phỏng tay với dữ liệu Sample trước khi chạm bàn phím.
- Nếu thuật toán chạy đúng trên Sample, mới bắt đầu viết code.

### Bước 3: Liệt kê các trường hợp biên

Trường hợp biên là những giá trị đặc biệt thường gây lỗi:

| Dạng bài | Edge Cases cần kiểm tra |
|---|---|
| Số nguyên | $N = 0$, $N = 1$, $N$ âm, $N$ rất lớn |
| Mảng/Danh sách | Mảng rỗng, mảng 1 phần tử, tất cả phần tử giống nhau |
| Chuỗi | Chuỗi rỗng `""`, chuỗi 1 ký tự, chuỗi toàn khoảng trắng |
| Chia | Chia cho 0, chia hết hoàn toàn, chia dư |

### Bước 4: Lập trình sạch sẽ, đúng cú pháp

- Đặt tên biến có ý nghĩa: `tong`, `dem`, `lon_nhat` thay vì `x`, `y`, `z`.
- Kiểm tra kỹ kiểu dữ liệu: `int(input())` hay `float(input())`?
- In đúng format: hoa/thường, có dấu cách hay không, có xuống dòng hay không.

### Bước 5: Tự kiểm thử (Self-Testing) trước khi nộp

- Chạy thử với **test mẫu** trong đề.
- Tự tạo **test biên**: giá trị nhỏ nhất, lớn nhất theo ràng buộc.
- Tự tạo **test bẫy**: giá trị = 0, giá trị âm, mảng rỗng...

---

## 2. Các tử huyệt làm mất điểm oan trong phòng thi

### 2.1. In thừa chữ dẫn dắt → Wrong Answer (WA)

Đây là lỗi **phổ biến nhất** ở thí sinh mới:

```python
# ❌ SAI: Đề chỉ yêu cầu in số 15
print("Ket qua la:", 15)  # Output: "Ket qua la: 15" → WA!

# ✅ ĐÚNG:
print(15)  # Output: "15" → Accepted!
```

> ⚠️ **Nguyên tắc vàng:** Hệ thống chấm tự động so sánh **từng ký tự** giữa output của thí sinh và đáp án chuẩn. Mọi ký tự thừa hay thiếu đều bị coi là sai.

### 2.2. Không để ý giới hạn dữ liệu → Time Limit Exceeded (TLE)

| Giới hạn $N$ | Độ phức tạp cho phép | Phương pháp |
|---|---|---|
| $N \le 10^3$ | $\mathcal{O}(N^2)$ | Vòng lặp lồng nhau |
| $N \le 10^5$ | $\mathcal{O}(N \log N)$ hoặc $\mathcal{O}(N)$ | Sắp xếp + duyệt |
| $N \le 10^9$ | $\mathcal{O}(\sqrt{N})$ hoặc $\mathcal{O}(\log N)$ | Công thức toán học |
| $N \le 10^{18}$ | $\mathcal{O}(1)$ | Công thức giải tích |

### 2.3. Lỗi sai số khi dùng số thực (float)

```python
# ❌ Nguy hiểm: Kiểm tra chính phương bằng float
import math
n = 10**18 + 7
if math.sqrt(n) == int(math.sqrt(n)):  # SAI do sai số!

# ✅ An toàn: Dùng phép nhân số nguyên
k = int(n ** 0.5)
if k * k == n or (k+1) * (k+1) == n:  # Kiểm tra cả k và k+1
```

### 2.4. Quên xử lý trường hợp $N = 0$ hoặc $N = 1$

```python
# Tính giai thừa: n = 0 → kết quả phải là 1
n = int(input())
gt = 1
for i in range(2, n + 1):
    gt *= i
print(gt)  # n = 0 → vòng lặp không chạy → gt = 1 ✅
```

### 2.5. Nhầm lẫn `//` và `/` khi đề yêu cầu số nguyên

```python
# Đề yêu cầu "in số nguyên"
a, b = 7, 2
print(a / b)   # 3.5 → WA nếu đề cần in 3
print(a // b)  # 3   → Đúng
```

---

## 3. Phân tích đề mẫu theo quy trình 5 bước

### 3.1. Ví dụ: Bài toán "Tổng chữ số"

**Đề bài:** Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Tính tổng các chữ số của $N$.

**Bước 1 — Đọc đề:**
- Input: Một số nguyên $N$.
- Output: Tổng các chữ số.
- Giới hạn: $N \le 10^9$ → tối đa 10 chữ số → vòng lặp `while` an toàn.

**Bước 2 — Thuật toán:**
- Lặp: Lấy chữ số cuối `N % 10`, cộng vào tổng, rồi bỏ chữ số cuối `N //= 10`.
- Dừng khi $N = 0$.

**Bước 3 — Edge Cases:**
- $N = 0$: Tổng = 0.
- $N = 1$: Tổng = 1.
- $N = 999999999$: Tổng = 81 (9 chữ số 9).

**Bước 4 — Code:**

```python
n = int(input())
tong = 0
while n > 0:
    tong += n % 10
    n //= 10
print(tong)
```

**Bước 5 — Kiểm thử:**

| Input | Expected Output | Kiểm tra |
|:---:|:---:|:---:|
| `123` | `6` | $1 + 2 + 3 = 6$ ✅ |
| `9` | `9` | ✅ |
| `1000` | `1` | $1 + 0 + 0 + 0 = 1$ ✅ |

### 3.2. Dry Run: $N = 4567$

| Vòng | `n` | `n % 10` | `tong` | `n //= 10` |
|:---:|:---:|:---:|:---:|:---:|
| Ban đầu | $4567$ | — | $0$ | — |
| 1 | $4567$ | $7$ | $7$ | $456$ |
| 2 | $456$ | $6$ | $13$ | $45$ |
| 3 | $45$ | $5$ | $18$ | $4$ |
| 4 | $4$ | $4$ | $22$ | $0$ |
| Kết thúc | $0$ | — | **In: $22$** | — |

---

## 4. Mẫu code chuẩn thi đấu theo dạng bài

### 4.1. Dạng "Kiểm tra tính chất"

```python
# Kiểm tra số nguyên tố
n = int(input())
if n < 2:
    print("NO")
else:
    nguyen_to = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            nguyen_to = False
            break
    print("YES" if nguyen_to else "NO")
```

### 4.2. Dạng "Đếm phần tử thỏa điều kiện"

```python
# Đếm số nguyên tố trong đoạn [A, B]
a, b = map(int, input().split())
dem = 0
for n in range(a, b + 1):
    if n < 2:
        continue
    ok = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            ok = False
            break
    if ok:
        dem += 1
print(dem)
```

### 4.3. Dạng "Xử lý chuỗi"

```python
# Đếm từ trong câu
s = input().split()
print(len(s))
```

### 4.4. Dạng "Tối ưu bằng công thức"

```python
# Tổng 1 + 2 + ... + N
n = int(input())
print(n * (n + 1) // 2)
```

---

## 5. Concept Quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Khi đề chỉ yêu cầu "in ra kết quả", nếu in thêm `"Ket qua la:"` thì hệ thống chấm sẽ:
- **A.** Vẫn được điểm tối đa
- **B.** Được cộng điểm thưởng
- **C.** **[Đáp án đúng]** Chấm `Wrong Answer` (0 điểm)
- **D.** Được nửa điểm
- > *Giải thích:* Hệ thống so sánh từng ký tự. Mọi ký tự thừa đều bị coi là sai.

#### Câu 2: Với $N \le 10^9$, vòng lặp `for i in range(N)` sẽ:
- **A.** Chạy nhanh
- **B.** **[Đáp án đúng]** Quá chậm, gây Time Limit Exceeded (TLE)
- **C.** Gây lỗi cú pháp
- **D.** Chạy bình thường
- > *Giải thích:* $10^9$ vòng lặp mất khoảng 10-30 giây trong Python, vượt xa giới hạn 1-2 giây.

#### Câu 3: Bước đầu tiên khi nhận đề thi là:
- **A.** Viết code ngay
- **B.** **[Đáp án đúng]** Đọc đề cẩn thận ít nhất 2 lần
- **C.** Hỏi giám thị
- **D.** Chạy code mẫu
- > *Giải thích:* Đọc kỹ giúp phát hiện các chi tiết quan trọng và tránh hiểu sai yêu cầu.

#### Câu 4: "Edge Case" trong lập trình thi đấu là:
- **A.** Trường hợp dễ nhất
- **B.** **[Đáp án đúng]** Các giá trị biên hoặc đặc biệt thường gây lỗi ($N = 0$, $N = 1$, mảng rỗng...)
- **C.** Trường hợp không cần xét
- **D.** Test cuối cùng
- > *Giải thích:* Edge cases là "bẫy" do ban tổ chức cài đặt để phân loại thí sinh.

#### Câu 5: `7 / 2` và `7 // 2` trong Python lần lượt cho kết quả:
- **A.** 3 và 3
- **B.** **[Đáp án đúng]** 3.5 và 3
- **C.** 3.5 và 3.5
- **D.** 3 và 3.5
- > *Giải thích:* `/` là chia thực (luôn float), `//` là chia lấy phần nguyên.

#### Câu 6: Khi đề yêu cầu in số nguyên nhưng code in ra `3.0`, hệ thống chấm sẽ:
- **A.** Chấp nhận
- **B.** **[Đáp án đúng]** Chấm Wrong Answer vì `3.0` khác `3`
- **C.** Tự động làm tròn
- **D.** Bỏ qua phần `.0`
- > *Giải thích:* `"3.0"` và `"3"` là hai chuỗi ký tự khác nhau.

#### Câu 7: Để tính $1 + 2 + \dots + N$ với $N = 10^{18}$, cách nào khả thi?
- **A.** Vòng lặp `for`
- **B.** Vòng lặp `while`
- **C.** **[Đáp án đúng]** Công thức $N \times (N + 1) / 2$
- **D.** Không tính được
- > *Giải thích:* Với $N = 10^{18}$, vòng lặp mất hàng tỷ giây. Công thức cho kết quả tức thì $\mathcal{O}(1)$.

#### Câu 8: Dry Run (mô phỏng tay) giúp ích gì?
- **A.** Làm đẹp code
- **B.** Tăng tốc chương trình
- **C.** **[Đáp án đúng]** Phát hiện lỗi logic trước khi code, kiểm tra thuật toán đúng hay sai
- **D.** Giảm dung lượng file
- > *Giải thích:* Chạy tay trên giấy giúp phát hiện lỗi thuật toán sớm hơn nhiều so với debug code.

#### Câu 9: Biến `ok = True` trong code kiểm tra nguyên tố đóng vai trò gì?
- **A.** Đếm số ước
- **B.** **[Đáp án đúng]** Cờ đánh dấu trạng thái: `True` = vẫn có thể là nguyên tố, `False` = chắc chắn không phải
- **C.** Lưu kết quả chia
- **D.** Đếm vòng lặp
- > *Giải thích:* Biến cờ là kỹ thuật phổ biến để theo dõi trạng thái.

#### Câu 10: Lệnh `break` trong vòng lặp kiểm tra nguyên tố có tác dụng gì?
- **A.** Thoát chương trình
- **B.** **[Đáp án đúng]** Thoát vòng lặp ngay lập tức khi đã tìm thấy ước, tránh kiểm tra thừa
- **C.** In kết quả
- **D.** Chuyển sang vòng lặp tiếp
- > *Giải thích:* `break` giúp tối ưu hiệu suất — không cần kiểm tra thêm khi đã biết không phải nguyên tố.

#### Câu 11: Kiểm tra nguyên tố chỉ cần duyệt đến $\sqrt{N}$ vì:
- **A.** Python chạy nhanh hơn
- **B.** **[Đáp án đúng]** Nếu $N$ có ước $d > \sqrt{N}$ thì chắc chắn tồn tại ước $N/d < \sqrt{N}$ đã được kiểm tra
- **C.** Ước số luôn nhỏ hơn $\sqrt{N}$
- **D.** Quy ước toán học
- > *Giải thích:* Các ước luôn đi theo cặp $(d, N/d)$, một bên $\le \sqrt{N}$, bên kia $\ge \sqrt{N}$.

#### Câu 12: Đoạn code sau có lỗi gì?
```python
n = int(input())
if n == 1:
    print("YES")
for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        print("NO")
        break
else:
    print("YES")
```
- **A.** Lỗi cú pháp
- **B.** **[Đáp án đúng]** Số 1 bị in "YES" rồi lại in "YES" lần nữa (thiếu `else` cho trường hợp $n = 1$)
- **C.** Không có lỗi
- **D.** Vòng lặp sai
- > *Giải thích:* $n = 1$ in "YES" ở dòng `if`, sau đó `range(2, 2)` rỗng nên `else` của `for` cũng in "YES". Số 1 **không phải** nguyên tố.

#### Câu 13: `continue` trong vòng lặp `for` có tác dụng:
- **A.** Thoát vòng lặp
- **B.** **[Đáp án đúng]** Bỏ qua phần còn lại của lần lặp hiện tại, nhảy đến lần lặp kế tiếp
- **C.** Dừng chương trình
- **D.** Lặp lại lần lặp hiện tại
- > *Giải thích:* `continue` khác `break`: `break` thoát hẳn vòng lặp, `continue` chỉ bỏ qua 1 lần.

#### Câu 14: Khi code chạy đúng với Sample nhưng vẫn bị WA, nguyên nhân thường gặp nhất là:
- **A.** Máy chấm bị lỗi
- **B.** **[Đáp án đúng]** Code chưa xử lý đúng Edge Case (trường hợp biên)
- **C.** Ngôn ngữ Python bị cấm
- **D.** Sample sai
- > *Giải thích:* Sample thường là test đơn giản. Test ẩn của ban tổ chức mới có edge cases phức tạp.

#### Câu 15: Thứ tự ưu tiên giải bài trong phòng thi nên là:
- **A.** Giải bài khó trước để gây ấn tượng
- **B.** **[Đáp án đúng]** Giải bài dễ trước lấy điểm chắc, bài khó giải sau
- **C.** Giải ngẫu nhiên
- **D.** Giải bài cuối trước
- > *Giải thích:* Chiến lược "dễ trước khó sau" đảm bảo tối đa hóa tổng điểm trong thời gian có hạn.
