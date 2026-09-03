# Bài 10: Tách chữ số với chia nguyên và chia dư

---

## 1. Khởi động: Chiếc kéo cắt số và cỗ máy thu hoạch chữ số

Trong các bài toán số học của Tin học trẻ Bảng A, việc làm việc với từng chữ số của một số tự nhiên là một dạng bài thường gặp, ví dụ:
* Tính tổng các chữ số của số $N$ (Ví dụ: $2024 \to 2 + 0 + 2 + 4 = 8$).
* Đếm xem số $N$ có bao nhiêu chữ số lẻ, bao nhiêu chữ số chẵn.
* Kiểm tra số đối xứng (Palindrome): đọc xuôi hay đọc ngược đều giống nhau (ví dụ: $121$, $1331$).
* Tìm chữ số lớn nhất, chữ số nhỏ nhất của số $N$.

Một số bạn nhỏ thường nghĩ ngay đến việc: "Em coi số đó là chuỗi chữ (String) để cắt từng chữ cái!".
Tuy nhiên, trong tư duy lập trình thuật toán số học chuyên sâu, các cao thủ tin học luôn dùng **2 phép toán ma thuật**: **Chia lấy dư (`% 10`)** và **Chia lấy nguyên (`// 10`)**!
Kỹ thuật này giúp chương trình bám sát cấu trúc của số và thường tránh được việc chuyển đổi dữ liệu không cần thiết.

---

## 2. Bí thuật 2 nhịp: Bóc vỏ và gọt đuôi

Hãy tưởng tượng số nguyên dương $N = 358$ như một củ hành tây có nhiều lớp:

```
      [ 3 5 8 ]
         |
         +----> Lấy chữ số hàng đơn vị (chữ số cuối cùng):
         |      358 % 10  =  8  (Nhịp 1: BÓC ĐUÔI)
         |
         +----> Vứt bỏ chữ số cuối cùng đi:
                358 // 10 =  35 (Nhịp 2: GỌT BỎ ĐUÔI)
```

### Quy luật vàng 2 nhịp vĩnh cửu:
1. **`chu_so = n % 10`**: Luôn luôn tóm được chữ số hàng đơn vị (đuôi của số).
2. **`n = n // 10`**: Gọt bỏ chữ số đuôi, số $N$ ngắn lại 1 chữ số!

Lặp đi lặp lại 2 nhịp này cho đến khi củ hành tây bị gọt hết sạch ($N = 0$) thì dừng lại!

---

## 3. Thuật toán kinh điển: Vòng lặp `while n > 0`

### 3.1. Tính tổng các chữ số của $N$
```python
n = int(input())
tong = 0

# Trường hợp đặc biệt nếu n = 0 thì tổng bằng 0
if n == 0:
    tong = 0
else:
    # Nếu n âm, ta đổi sang dương
    if n < 0:
        n = -n

    while n > 0:
        cs = n % 10      # Nhịp 1: Bóc chữ số cuối cùng ra
        tong = tong + cs # Cộng dồn vào biến tổng
        n = n // 10      # Nhịp 2: Gọt bỏ chữ số đó đi

print("Tong chu so la:", tong)
```

### Bảng dry run mô phỏng cặn kẽ với $N = 257$:

| Vòng lặp | Giá trị `n` đầu vòng | `cs = n % 10` | `tong` mới (`tong + cs`) | `n = n // 10` | Điều kiện `n > 0` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Ban đầu | 257 | - | 0 | - | $257 > 0$ (Đúng) |
| Lần 1 | 257 | **7** | $0 + 7 = 7$ | 25 | $25 > 0$ (Đúng) |
| Lần 2 | 25 | **5** | $7 + 5 = 12$ | 2 | $2 > 0$ (Đúng) |
| Lần 3 | 2 | **2** | $12 + 2 = \mathbf{14}$ | 0 | $0 > 0$ (**SAI! DỪNG**) |

Kết quả in ra: `14`. Tuyệt đối chính xác!

### 3.2. Bí kíp lật ngược một con số (tạo số đảo ngược)
Làm sao để biến số $123$ thành $321$?
Mỗi khi bóc được một chữ số mới `cs`, ta đẩy số đảo cũ sang bên trái một hàng (nhân 10) rồi nhét chữ số mới vào đuôi:
$$\text{dao} = \text{dao} \times 10 + \text{cs}$$

```python
n = int(input())
goc = n
dao = 0

while n > 0:
    cs = n % 10
    dao = dao * 10 + cs
    n = n // 10

print("So dao nguoc la:", dao)
if dao == goc:
    print("Day la so doi xung (Palindrome)!")
```

---

## 4. Concept quiz: 15 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Phép tính `456 % 10` cho kết quả là gì?
- **A.** 4
- **B.** 5
- **C.** **[Đáp án đúng]** 6
- **D.** 45
- > *Giải thích:* Phép chia dư `% 10` luôn trả về chữ số tận cùng (hàng đơn vị).

#### Câu 2: Phép tính `456 // 10` cho kết quả là gì?
- **A.** 6
- **B.** 4.56
- **C.** **[Đáp án đúng]** 45
- **D.** 45.6
- > *Giải thích:* Phép chia nguyên `// 10` cắt bỏ chữ số tận cùng bên phải.

#### Câu 3: Điều kiện dừng của vòng lặp tách chữ số của một số nguyên dương $N$ là gì?
- **A.** Khi `n == 1`
- **B.** **[Đáp án đúng]** Khi `n == 0` (hoặc vòng lặp `while n > 0` kết thúc)
- **C.** Khi `n % 10 == 0`
- **D.** Sau đúng 10 lần lặp
- > *Giải thích:* Khi $N$ bị chia nguyên liên tiếp cho 10 đến khi không còn chữ số nào ($N = 0$) thì dừng.

#### Câu 4: Số $N = 7$ khi thực hiện `7 // 10` sẽ nhận giá trị bằng bao nhiêu?
- **A.** 7
- **B.** **[Đáp án đúng]** 0
- **C.** 1
- **D.** 0.7
- > *Giải thích:* $7$ chia $10$ được thương nguyên là $0$, dư $7$.

#### Câu 5: Số nào sau đây là số đối xứng (palindrome)?
- **A.** 1234
- **B.** 1220
- **C.** **[Đáp án đúng]** 1221
- **D.** 1231
- > *Giải thích:* Số $1221$ đọc từ trái qua phải hay từ phải qua trái đều là $1221$.

#### Câu 6: Đoạn code sau thực hiện điều gì?
```python
dem = 0
while n > 0:
    dem += 1
    n //= 10
```
- **A.** Tính tổng các chữ số của $N$
- **B.** **[Đáp án đúng]** Đếm số lượng chữ số của $N$ (với $N > 0$)
- **C.** Đếm số chữ số chẵn của $N$
- **D.** Tìm chữ số lớn nhất của $N$
- > *Giải thích:* Cứ mỗi lần gọt bỏ 1 chữ số (`n //= 10`), biến `dem` tăng thêm 1.

#### Câu 7: Nếu nhập $N = 0$, đoạn code `while n > 0: dem += 1; n //= 10` sẽ cho kết quả `dem` bằng bao nhiêu?
- **A.** 1
- **B.** **[Đáp án đúng]** 0 (Bẫy số 0!)
- **C.** Báo lỗi
- **D.** Vô tận
- > *Giải thích:* Đây là bẫy kinh điển: Số 0 có 1 chữ số, nhưng điều kiện `0 > 0` bị sai ngay lập tức nên vòng lặp không chạy. Ta phải xử lý riêng nếu $N = 0$ thì `dem = 1`.

#### Câu 8: Muốn kiểm tra chữ số cuối cùng của $N$ có phải là số lẻ hay không, ta viết điều kiện nào?
- **A.** `n % 2 == 0`
- **B.** **[Đáp án đúng]** `(n % 10) % 2 != 0` (hoặc `n % 2 != 0`)
- **C.** `n // 10 % 2 != 0`
- **D.** `n % 10 == 1`
- > *Giải thích:* Một số nguyên lẻ thì chữ số tận cùng của nó cũng là số lẻ.

#### Câu 9: Cho $N = 305$. Tổng các chữ số của $N$ là:
- **A.** 35
- **B.** **[Đáp án đúng]** 8
- **C.** 15
- **D.** 3
- > *Giải thích:* $3 + 0 + 5 = 8$.

#### Câu 10: Đoạn code sau in ra màn hình giá trị gì?
```python
n = 8492
max_cs = 0
while n > 0:
    cs = n % 10
    if cs > max_cs:
        max_cs = cs
    n //= 10
print(max_cs)
```
- **A.** 8
- **B.** 4
- **C.** **[Đáp án đúng]** 9
- **D.** 2
- > *Giải thích:* Thuật toán tìm chữ số lớn nhất trong các chữ số 8, 4, 9, 2 $\implies$ Chữ số 9 lớn nhất.

#### Câu 11: Cho số nguyên dương $N = 12345$. Chữ số hàng chục của $N$ là kết quả của biểu thức nào?
- **A.** `(n % 100) // 10`
- **B.** `(n // 10) % 10`
- **C.** **[Đáp án đúng]** Cả A và B đều đúng
- **D.** `n % 10`
- > *Giải thích:* Cách A: $12345 \% 100 = 45 \implies 45 // 10 = 4$. Cách B: $12345 // 10 = 1234 \implies 1234 \% 10 = 4$. Cả 2 đều cho ra chữ số hàng chục 4.

#### Câu 12: Biểu thức `dao = dao * 10 + cs` với `dao = 35` và `cs = 7` sẽ cho giá trị `dao` mới là:
- **A.** 42
- **B.** 350
- **C.** **[Đáp án đúng]** 357
- **D.** 735
- > *Giải thích:* $35 \times 10 + 7 = 350 + 7 = 357$.

#### Câu 13: Một số tự nhiên được gọi là "toàn chẵn" khi nào?
- **A.** Khi số đó chia hết cho 2
- **B.** **[Đáp án đúng]** Khi TẤT CẢ các chữ số cấu tạo nên số đó đều là chữ số chẵn
- **C.** Khi chữ số đầu tiên là chẵn
- **D.** Khi tổng các chữ số là số chẵn
- > *Giải thích:* Định nghĩa số toàn chẵn (ví dụ: $2468$, $402$) là mọi chữ số của nó đều thuộc tập $\{0, 2, 4, 6, 8\}$.

#### Câu 14: Để kiểm tra số $N$ có toàn chữ số chẵn không, nếu gặp một chữ số `cs % 2 != 0`, ta nên làm gì?
- **A.** Tiếp tục kiểm tra
- **B.** **[Đáp án đúng]** Kết luận ngay là KHÔNG và dùng `break` để thoát vòng lặp
- **C.** Báo lỗi
- **D.** Trừ biến đếm
- > *Giải thích:* Chỉ cần phát hiện 1 chữ số lẻ duy nhất thì số đó lập tức vi phạm điều kiện "toàn chẵn".

#### Câu 15: Tại sao trong các bài toán tách chữ số, ta cần lưu `goc = n` trước khi chạy vòng lặp `while n > 0`?
- **A.** Để làm đẹp code
- **B.** **[Đáp án đúng]** Vì sau khi vòng lặp kết thúc, biến `n` đã bị gọt về $0$
- **C.** Vì Python bắt buộc phải có 2 biến
- **D.** Để tăng tốc độ chương trình
- > *Giải thích:* Vòng lặp thực hiện `n = n // 10` liên tục, khi kết thúc thì $n = 0$. Cần biến `goc` để lưu lại giá trị ban đầu so sánh với số đảo.
