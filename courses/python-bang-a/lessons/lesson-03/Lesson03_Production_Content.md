# Bài 03: Công thức tính toán, hình học và đổi đơn vị

## 1. Kiến thức chuyên sâu dành cho học sinh Tiểu học

### A. Các công thức hình học nền tảng
* **Hình chữ nhật:**
  - Chu vi: $P = (a + b) 	\times 2 \implies$ Code: `(a + b) * 2` *(Bắt buộc phải có dấu ngoặc tròn)*.
  - Diện tích: $S = a 	\times b \implies$ Code: `a * b`.
  - Nửa chu vi: $P_{nua} = P // 2$.
  - Tìm một cạnh khi biết chu vi $P$ và một cạnh $a$: $b = (P // 2) - a$.
* **Hình vuông:**
  - Chu vi: $P = a 	\times 4 \implies$ Code: `a * 4`.
  - Cạnh hình vuông từ chu vi: $a = P // 4$.
  - Diện tích: $S = a 	\times a = a^2 \implies$ Code: `a * a` hoặc `a ** 2`.
* **Tam giác vuông:**
  - Diện tích khi biết 2 cạnh góc vuông $a$ và $b$: $S = \frac{a 	\times b}{2} \implies$ Code: `(a * b) // 2` (nếu tích chia hết cho 2).
* **Hình thang:**
  - Diện tích: $S = \frac{(a + b) 	\times h}{2} \implies$ Code: `((a + b) * h) // 2`.

### B. Bài toán diện tích hình học lồng ghép (Trừ phần giao / Phần còn lại)
* *Mô hình:* Có một khu đất lớn diện tích $S_1$, bên trong xây một công trình có diện tích $S_2$. Diện tích đất còn lại là:
  $$\mathbf{S_{con\_lai} = S_1 - S_2}$$
* *Bài toán bờ hồ & hòn đảo:* Hồ hình vuông cạnh $A$, đảo hình chữ nhật $B 	\times C$:
  `mat_nuoc = (A * A) - (B * C)`.

### C. Thuật toán phân rã đơn vị thời gian (Từ giây sang Giờ — Phút — Giây)
Biết rằng: $1	\text{ giờ} = 60	\text{ phút} = 3600	\text{ giây}$, $1	\text{ phút} = 60	\text{ giây}$.
Cho trước $S$ giây, quy trình phân rã gồm 3 bước:
1. **Tính số giờ:** `gio = S // 3600`
2. **Lấy số giây còn dư sau khi tính giờ:** `giay_du = S % 3600`
3. **Tính số phút và giây từ phần dư:**
   - `phut = giay_du // 60`
   - `giay = giay_du % 60`

### D. Kỹ thuật in số thập phân và làm tròn
- Làm tròn 2 chữ số thập phân: `round(x, 2)`.
- **In chuẩn định dạng thi đấu bằng f-string:** `print(f"{x:.2f}")` (Đảm bảo số `5` sẽ in ra đủ `5.00`).
- **In bù số 0 ở đầu (Ví dụ: in 5 giây thành `05`):** `print(f"{giay:02d}")`.

## 2. Bảng công thức quy đổi đơn vị đo lường cần thuộc lòng
| Tên đơn vị | Quy đổi xuôi | Lưu ý khi tính diện tích |
|---|---|---|
| Độ dài | $1	\text{ m} = 10	\text{ dm} = 100	\text{ cm} = 1000	\text{ mm}$ | $1	\text{ km} = 1000	\text{ m}$ |
| Diện tích | $1	\text{ m}^2 = 100	\text{ dm}^2 = 10,000	\text{ cm}^2$ | **Độ dài nhân 10 thì diện tích nhân 100!** |
| Khối lượng | $1	\text{ tấn} = 10	\text{ tạ} = 1000	\text{ kg}$; $1	\text{ kg} = 1000	\text{ g}$ | Luôn đổi về cùng đơn vị nhỏ nhất trước |

## 3. Bẫy lỗi phòng thi
- ❌ **Quên đổi về cùng đơn vị:** Dài $2	\text{ m}$, rộng $30	\text{ cm}$ mà tính diện tích $2 	\times 30 = 60$ là sai! Phải đổi $2	\text{ m} = 200	\text{ cm}$, diện tích là $200 	\times 30 = 6000	\text{ cm}^2$.
- ❌ **Thiếu ngoặc phép tính nửa chu vi:** Viết `P // 2 - a` thì đúng, nhưng viết `P - a // 2` là sai hoàn toàn!

## 4. Concept quiz: 18 câu trắc nghiệm bắt bẫy củng cố khái niệm

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

#### Câu 13 (diện tích tam giác vuông):
Một miếng bánh hình tam giác vuông có hai cạnh góc vuông dài $6\text{ cm}$ và $4\text{ cm}$. Diện tích miếng bánh đó là:
- **A.** $10\text{ cm}^2$
- **B.** $20\text{ cm}^2$
- **C.** **[Đáp án đúng]** $12\text{ cm}^2$
- **D.** $24\text{ cm}^2$
> *Giải thích:* Diện tích tam giác vuông bằng tích hai cạnh góc vuông chia cho 2: $(6 \times 4) : 2 = 24 : 2 = 12\text{ cm}^2$.

#### Câu 14 (thể tích hộp chữ nhật):
Một hộp sữa có chiều dài $3\text{ cm}$, chiều rộng $2\text{ cm}$ và chiều cao $4\text{ cm}$. Thể tích của hộp sữa đó là:
- **A.** $9\text{ cm}^3$
- **B.** $14\text{ cm}^3$
- **C.** **[Đáp án đúng]** $24\text{ cm}^3$
- **D.** $29\text{ cm}^3$
> *Giải thích:* Thể tích hộp chữ nhật bằng dài nhân rộng nhân cao: $3 \times 2 \times 4 = 24\text{ cm}^3$.

#### Câu 15 (đổi đơn vị thời gian xuôi):
Bạn Bi chạy bộ trong $2$ giờ $15$ phút. Hỏi bạn Bi đã chạy tổng cộng bao nhiêu giây?
- **A.** $215$ giây
- **B.** $2250$ giây
- **C.** **[Đáp án đúng]** $8100$ giây
- **D.** $135$ giây
> *Giải thích:* $2$ giờ $= 2 \times 3600 = 7200$ giây. $15$ phút $= 15 \times 60 = 900$ giây. Tổng cộng: $7200 + 900 = 8100$ giây.

#### Câu 16 (dự đoán output — phân rã giờ phút giây):
Đoạn code sau in ra kết quả gì?
```python
s = 7325
gio = s // 3600
du = s % 3600
phut = du // 60
giay = du % 60
print(gio, phut, giay)
```
- **A.** `1 62 5`
- **B.** `7 3 25`
- **C.** **[Đáp án đúng]** `2 2 5`
- **D.** `2 3 5`
> *Giải thích:* $7325 : 3600 = 2$ dư $125$. Từ $125$ giây dư: $125 : 60 = 2$ phút dư $5$ giây. Vậy in ra `2 2 5` (2 giờ 2 phút 5 giây).

#### Câu 17 (làm tròn với `round()`):
Kết quả của lệnh `round(5.678, 2)` là:
- **A.** `5.67`
- **B.** **[Đáp án đúng]** `5.68`
- **C.** `5.6`
- **D.** `6`
> *Giải thích:* Chữ số thứ ba sau dấu phẩy là 8 ($\ge 5$) nên làm tròn lên: `5.678` thành `5.68`.

#### Câu 18 (làm tròn với `f-string`):
Cho `x = 7.456`. Lệnh nào in ra `7.5` (làm tròn đến 1 chữ số thập phân)?
- **A.** `print(round(x))`
- **B.** `print(f"{x:.2f}")`
- **C.** **[Đáp án đúng]** `print(f"{x:.1f}")`
- **D.** `print(x // 10)`
> *Giải thích:* Cú pháp `:.1f` trong `f-string` nghĩa là làm tròn và hiển thị đúng 1 chữ số sau dấu phẩy, nên `7.456` thành `7.5`.
