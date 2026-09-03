# Bài 03: Công thức tính toán, hình học và đổi đơn vị

---

## 1. Khởi động: Khi lập trình viên nhí giải toán hình học

Trong các kỳ thi Tin học trẻ Bảng A, có một mảng đề thi vô cùng quen thuộc và chiếm tỷ lệ điểm rất cao: **Các bài toán hình học và bài toán thực tế đời thường** (chu vi, diện tích hình chữ nhật, hình vuông, tam giác, bài toán hồ nước bao quanh đảo, bài toán đồng hồ thời gian).

Rất nhiều bạn nhỏ học rất giỏi môn Toán trên lớp, nhưng khi chuyển sang viết code Python thì lại gặp khó khăn:
* *"Tại sao công thức chu vi $(dài + rộng) \times 2$ viết vào Python lại ra kết quả sai?"*
* *"Làm sao để biết cạnh còn lại của hình chữ nhật khi chỉ biết chu vi?"*
* *"Làm sao để đổi 3750 giây thành đúng định dạng X giờ Y phút Z giây?"*

Bài học hôm nay sẽ trang bị cho các em toàn bộ kỹ năng:
1. Chuyển đổi chính xác các công thức hình học Tiểu học thành các dòng code Python an toàn.
2. Thuật toán phân rã thời gian ngược từ giây sang giờ - phút - giây.
3. Bí quyết làm tròn số thập phân (`round()` và định dạng `f-string`).

---

## 2. Các công thức hình học kinh điển trong Python

Hãy cùng ôn lại các công thức toán Tiểu học và cách viết code tương ứng:

### 2.1. Hình vuông (cạnh là $a$)
* **Chu vi:** $P = a \times 4$ $\implies$ Code: `chu_vi = a * 4`
* **Diện tích:** $S = a \times a = a^2$ $\implies$ Code: `dien_tich = a * a` hoặc `dien_tich = a ** 2`
* **Tìm cạnh khi biết chu vi:** $a = P : 4$ $\implies$ Code: `canh = P // 4` (nếu đề cho chu vi là số nguyên chia hết).

### 2.2. Hình chữ nhật (chiều dài $a$, chiều rộng $b$)
* **Chu vi:** $P = (a + b) \times 2$ $\implies$ Code: `chu_vi = (a + b) * 2`
  > ⚠️ **Tử huyệt bắt bẫy:** Tuyệt đối không được viết `a + b * 2`. Vì theo quy tắc ưu tiên, máy tính sẽ nhân `b * 2` trước rồi mới cộng `a`. Bắt buộc phải có dấu ngoặc tròn `(a + b)`!
* **Diện tích:** $S = a \times b$ $\implies$ Code: `dien_tich = a * b`
* **Nửa chu vi:** $P_{nua} = P : 2 = a + b$ $\implies$ Code: `nua_chu_vi = P // 2`
* **Tìm một cạnh khi biết chu vi $P$ và một cạnh $a$:**
  $$b = (P : 2) - a = \frac{P}{2} - a$$
  Code: `canh_con_lai = (P // 2) - a`

### 2.3. Hình tam giác (độ dài 3 cạnh là $a, b, c$)
* **Chu vi:** $P = a + b + c$ $\implies$ Code: `chu_vi = a + b + c`
* **Diện tích tam giác vuông (2 cạnh góc vuông là $a, b$):**
  $$S = \frac{a \times b}{2}$$
  Code: `dien_tich = (a * b) / 2` (nếu muốn số thực) hoặc `(a * b) // 2` (nếu tích $a \times b$ luôn chia hết cho 2).

---

## 3. Bài toán hình học lồng nhau: Diện tích phần mặt nước còn lại

Một dạng bài rất hay gặp trong đề thi Tin học trẻ (như *Bài 2: Hồ cá sấu - THT Lâm Đồng*):
* Người ta có một khu đất/hồ nước lớn hình vuông có kích thước cạnh là $A$.
* Ở chính giữa, người ta xây một hòn đảo nhỏ hình chữ nhật có kích thước $B \times C$.
* **Yêu cầu:** Tính diện tích phần mặt nước còn lại sau khi xây hòn đảo.

### Bản chất tư duy toán học:
$$\text{Diện tích mặt nước} = \text{Diện tích hồ nước lớn} - \text{Diện tích hòn đảo nhỏ}$$
$$S_{con\_lai} = S_{ho} - S_{dao} = (A \times A) - (B \times C)$$

```python
# Đoạn code giải trọn vẹn:
A = int(input())
B = int(input())
C = int(input())

dien_tich_ho = A * A
dien_tich_dao = B * C
mat_nuoc = dien_tich_ho - dien_tich_dao

print(mat_nuoc)
```
*Thời gian chạy:* $\mathcal{O}(1)$ (chỉ mất vài phép tính số học, chạy trong $0.0001$ giây!).

---

## 4. Nghệ thuật phân rã thời gian: Từ giây sang giờ - phút - giây

Ở Bài 2, chúng ta đã biết đổi xuôi từ Giờ/Phút sang Giây ($1\text{h} = 3600\text{s}, 1\text{m} = 60\text{s}$).
Bây giờ, nếu đề bài cho một số giây khổng lồ, ví dụ **$3755$ giây**, làm sao phân rã thành mấy giờ, mấy phút, mấy giây?

### Sơ đồ tư duy 3 bước:
1. **Bước 1 (Tính số giờ):**
   * Trong $3755$ giây có bao nhiêu giờ trọn vẹn?
   * Vì $1$ giờ có $3600$ giây, ta lấy: `gio = 3755 // 3600` $\implies 3755 // 3600 = \mathbf{1}$ giờ.
2. **Bước 2 (Tìm số giây còn dư lại sau khi đã tính giờ):**
   * Số giây còn thừa chưa đủ 1 giờ: `giay_du = 3755 % 3600` $\implies 3755 \% 3600 = \mathbf{155}$ giây.
3. **Bước 3 (Tính số phút và số giây cuối cùng từ phần dư):**
   * Từ $155$ giây dư đó, ta tính xem được bao nhiêu phút:
     `phut = giay_du // 60` $\implies 155 // 60 = \mathbf{2}$ phút.
   * Số giây cuối cùng còn thừa lại là:
     `giay = giay_du % 60` $\implies 155 \% 60 = \mathbf{35}$ giây.

$$\implies \mathbf{3755 \text{ giây}} = \mathbf{1 \text{ giờ } 2 \text{ phút } 35 \text{ giây}}!$$

```python
tong_giay = int(input())

gio = tong_giay // 3600
giay_du = tong_giay % 3600

phut = giay_du // 60
giay = giay_du % 60

print(gio, phut, giay)
```

---

## 5. Làm tròn số thập phân: `round()` và `f-string`

Khi tính chu vi hình tròn hoặc vận tốc, kết quả có thể ra số thập phân dài vô tận như `3.3333333333333335`.
Đề thi thường yêu cầu: *"In ra kết quả làm tròn đến 2 chữ số thập phân"*.

### Cách 1: Dùng hàm `round(so, k)`
Hàm `round(x, 2)` sẽ làm tròn số `x` đến đúng 2 chữ số thập phân theo quy tắc toán học (từ 5 trở lên thì làm tròn lên).
```python
diem = 8.66666
print(round(diem, 2))  # In ra: 8.67
```

### Cách 2: Dùng định dạng chuỗi chuyên nghiệp (`f-string`)
Đây là cách các lập trình viên Python hiện đại yêu thích nhất vì vừa đẹp mắt vừa chính xác:
```python
diem = 8.66666
print(f"{diem:.2f}")   # In ra chính xác: 8.67
```

---

## 6. Concept quiz: 12 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1 (công thức chu vi hình chữ nhật):
Cho chiều dài `a` và chiều rộng `b`. Biểu thức Python nào tính đúng chu vi hình chữ nhật?
- **A.** `P = a + b * 2`
- **B.** **[Đáp án đúng]** `P = (a + b) * 2`
- **C.** `P = a * b * 2`
- **D.** `P = (a * b) // 2`
> *Giải thích:* Chu vi bằng tổng chiều dài và chiều rộng rồi nhân đôi. Cần có dấu ngoặc `(a + b)` để thực hiện phép cộng trước phép nhân.

#### Câu 2 (tìm cạnh hình chữ nhật):
Một hình chữ nhật có chu vi là `P` và chiều rộng là `w`. Chiều dài của hình chữ nhật đó được tính bằng công thức:
- **A.** `P - w`
- **B.** `P // 2 + w`
- **C.** **[Đáp án đúng]** `P // 2 - w`
- **D.** `(P - w) // 2`
> *Giải thích:* Nửa chu vi là $P // 2$. Chiều dài bằng nửa chu vi trừ đi chiều rộng: `P // 2 - w`.

#### Câu 3 (đổi đơn vị thời gian):
Một giờ có bao nhiêu giây?
- **A.** 60 giây
- **B.** 360 giây
- **C.** **[Đáp án đúng]** 3600 giây
- **D.** 6000 giây
> *Giải thích:* $1\text{ giờ} = 60\text{ phút} = 60 \times 60 = 3600\text{ giây}$.

#### Câu 4 (dự đoán output — phân rã thời gian):
Đoạn code sau in ra kết quả gì?
```python
s = 125
phut = s // 60
giay = s % 60
print(phut, giay)
```
- **A.** `2 5`
- **B.** **[Đáp án đúng]** `2 5`
- **C.** `1 65`
- **D.** `12 5`
> *Giải thích:* $125 : 60 = 2$ dư $5$. Vậy in ra `2 5` (2 phút 5 giây).

#### Câu 5 (hình học lồng nhau):
Một bức tường hình vuông cạnh $a = 10\text{m}$. Người ta khoét một cửa sổ hình vuông cạnh $b = 2\text{m}$. Diện tích phần tường còn lại là:
- **A.** 16
- **B.** 80
- **C.** **[Đáp án đúng]** 96
- **D.** 100
> *Giải thích:* $S_{tuong} = 10 \times 10 = 100$. $S_{cua} = 2 \times 2 = 4$. Diện tích còn lại: $100 - 4 = 96\text{ m}^2$.

#### Câu 6 (bắt bẫy đơn vị đo lường):
Cạnh hình vuông $a = 2\text{ m}$. Diện tích hình vuông đó tính theo đơn vị $\text{cm}^2$ là:
- **A.** $4\text{ cm}^2$
- **B.** $400\text{ cm}^2$
- **C.** **[Đáp án đúng]** $40000\text{ cm}^2$
- **D.** $20000\text{ cm}^2$
> *Giải thích:* $2\text{ m} = 200\text{ cm}$. Diện tích là $200 \times 200 = 40000\text{ cm}^2$. Rất nhiều học sinh nhầm chỉ nhân thêm 100!

#### Câu 7 (làm tròn số thập phân):
Kết quả của lệnh `round(4.5678, 2)` là:
- **A.** `4.56`
- **B.** **[Đáp án đúng]** `4.57`
- **C.** `4.6`
- **D.** `5`
> *Giải thích:* Chữ số thứ ba sau dấu phẩy là 7 ($\ge 5$), do đó làm tròn lên thành `4.57`.

#### Câu 8 (tính vận tốc — thời gian gặp nhau):
Hai người đứng cách nhau khoảng cách $D$ (km). Người thứ nhất đi về phía người thứ hai với vận tốc $V$ (km/h). Thời gian (giờ) để hai người gặp nhau là:
- **A.** `D * V`
- **B.** `V / D`
- **C.** **[Đáp án đúng]** `D / V`
- **D.** `D - V`
> *Giải thích:* Thời gian = Quãng đường : Vận tốc $\implies D / V$.

#### Câu 9 (bắt bẫy phép chia diện tích tam giác):
Cho tam giác có đáy $a = 5$ và chiều cao $h = 3$. Lệnh `dien_tich = a * h / 2` sẽ cho kết quả thuộc kiểu dữ liệu nào?
- **A.** `int`
- **B.** **[Đáp án đúng]** `float` (kết quả `7.5`)
- **C.** `str`
- **D.** Báo lỗi
> *Giải thích:* Vì có dấu chia thực `/`, kết quả luôn là kiểu `float`, giá trị là `7.5`.

#### Câu 10 (chu vi hình vuông từ diện tích):
Một hình vuông có diện tích là $S = 64$. Chu vi hình vuông đó là bao nhiêu?
- **A.** 16
- **B.** **[Đáp án đúng]** 32
- **C.** 64
- **D.** 256
> *Giải thích:* Cạnh hình vuông là $\sqrt{64} = 8$. Chu vi là $8 \times 4 = 32$.

#### Câu 11 (ghép gạch lát sân):
Một sân hình chữ nhật kích thước $6\text{m} \times 4\text{m}$. Người ta dùng các viên gạch hình vuông cạnh $1\text{m}$ để lát kín sân. Cần bao nhiêu viên gạch?
- **A.** 10 viên
- **B.** 20 viên
- **C.** **[Đáp án đúng]** 24 viên
- **D.** 48 viên
> *Giải thích:* Diện tích sân: $6 \times 4 = 24\text{ m}^2$. Mỗi viên gạch diện tích $1 \times 1 = 1\text{ m}^2$. Số viên gạch là $24 : 1 = 24$ viên.

#### Câu 12 (format chuỗi thời gian đẹp):
Lệnh nào sau đây in ra số phút và số giây luôn có 2 chữ số (ví dụ: phút 5 in ra `05`, giây 9 in ra `09`)?
- **A.** `print(f"{phut}:{giay}")`
- **B.** **[Đáp án đúng]** `print(f"{phut:02d}:{giay:02d}")`
- **C.** `print(round(phut, 2), round(giay, 2))`
- **D.** `print("0" + phut + "0" + giay)`
> *Giải thích:* Cú pháp `:02d` trong `f-string` của Python tự động bù thêm số 0 ở đằng trước nếu số đó có ít hơn 2 chữ số.
