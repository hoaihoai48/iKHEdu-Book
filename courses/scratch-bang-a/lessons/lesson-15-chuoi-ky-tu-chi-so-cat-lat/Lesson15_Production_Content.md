# Bài 15: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự

## 1. Chuỗi ký tự (String) và xử lý văn bản

Bên cạnh các con số phục vụ tính toán, máy tính còn phải xử lý văn bản: tên người, địa chỉ, mật khẩu, lời thoại nhân vật... Tất cả những dữ liệu này được gọi là **Chuỗi ký tự (String)**.

- **Chuỗi ký tự** là một dãy các ký tự (chữ cái, chữ số, dấu câu, khoảng trắng) được xếp nối tiếp nhau thành một hàng ngang.

- Ví dụ: `"SCRATCH"`, `"IKH EDU"`, `"12345"`, `"Hoc Lap Trinh 2026"`.

---

## 2. Bảng tra cứu các khối lệnh xử lý chuỗi trong Scratch 3.0

Các khối lệnh xử lý chuỗi nằm trong nhóm **Các phép toán (Operators)** màu xanh lá cây:

![Bảng khối lệnh xử lý chuỗi Scratch Tiếng Việt](assets/rendered_blocks/l15_string_operations_vi.png)

| Khối lệnh trực quan Scratch 3.0 | Thao tác | Ví dụ với chuỗi `s = "TIN HOC"` | Kết quả thực tế |
|:---:|---|---|:---:|
| ![Khối ký tự của chuỗi](../../assets/rendered_blocks/str_block_letter.png) | Ký tự tại vị trí $i$ | `ký tự (1) của (s)` | `"T"` |
| ![Khối độ dài của chuỗi](../../assets/rendered_blocks/str_block_length.png) | Độ dài chuỗi | `độ dài của (s)` | `7` |
| ![Khối kết hợp chuỗi](../../assets/rendered_blocks/str_block_join.png) | Ghép 2 chuỗi | `kết hợp [TIN] [HOC]` | `"TINHOC"` |
| ![Khối chuỗi chứa](../../assets/rendered_blocks/str_block_contains.png) | Kiểm tra ký tự | `(s) chứa [H] ?` | Đúng (`True`) |

> ⚠️ **Quy tắc vàng 1-Based Indexing:** Giống như danh sách, các ký tự trong chuỗi Scratch được đánh số thứ tự bắt đầu từ **vị trí 1** đến `độ dài của chuỗi`. Trong Scratch **không có ký tự số 0**!

---

## 3. Thuật toán trích xuất chuỗi con

Để cắt ra một đoạn văn bản từ ký tự thứ $L$ đến ký tự thứ $R$ của chuỗi ban đầu, học sinh cần tự xây dựng thuật toán tích lũy chuỗi con:

![Thuật toán trích xuất chuỗi con từ L đến R](assets/rendered_blocks/l15_substring_slice_vi.png)

### Các bước thuật toán:

1. **Khởi tạo chuỗi kết quả rỗng:** `đặt [chuoi_con v] thành []` (để trống không chứa ký tự nào).

2. **Khởi tạo chỉ số bắt đầu:** `đặt [i v] thành (L)`.

3. **Số lần lặp:** Từ vị trí $L$ đến $R$ có đúng `(R - L + 1)` ký tự.

4. **Vòng lặp tích lũy ký tự:**
   - Dùng khối ghép: `đặt [chuoi_con v] thành (kết hợp (chuoi_con) (ký tự (i) của (chuoi_goc)))`.
   - Tăng chỉ số: `thay đổi [i v] một lượng (1)`.

5. Sau khi kết thúc vòng lặp, biến `chuoi_con` sẽ chứa trọn vẹn đoạn văn bản cần trích xuất.

---

## 4. Bảng mô phỏng trích xuất chuỗi từ $L = 2$ Đến $R = 4$ của chuỗi `"SCRATCH"` (Dry run)

Chuỗi gốc $S = 	ext{"SCRATCH"}$. Độ dài $= 6$. Cần cắt từ $L = 2$ đến $R = 4$.

- Số lần lặp $= 4 - 2 + 1 = 3$ lần (vị trí 2, 3, 4).

| Vòng lặp | Biến chỉ số `i` | Lệnh `ký tự (i) của (S)` | Ghép chuỗi `chuoi_con` | Giá trị mới của `chuoi_con` | Hành động tiếp theo |
|:---:|:---:|:---:|:---:|:---:|---|
| *Bắt đầu* | $i = 2$ | — | Khởi tạo rỗng `""` | `""` | Bắt đầu vòng lặp |
| **Vòng 1** | $i = 2$ | `ký tự (2)` $\to$ **`"Y"`** | `""` kết hợp `"Y"` | `"Y"` | Tăng $i = 3$ |
| **Vòng 2** | $i = 3$ | `ký tự (3)` $\to$ **`"T"`** | `"Y"` kết hợp `"T"` | `"YT"` | Tăng $i = 4$ |
| **Vòng 3** | $i = 4$ | `ký tự (4)` $\to$ **`"H"`** | `"YT"` kết hợp `"H"` | **`"YTH"`** | Tăng $i = 5$ |
| **Dừng** | $i = 5$ | — | Đã lặp đủ 3 lần | **`"YTH"`** | Vòng lặp kết thúc |

$\implies$ Nhân vật thông báo kết quả trích xuất: `"YTH"`.

---

## 5. Các bẫy lỗi thường gặp (Bug Traps)

> **Bẫy 1: Bẫy ký tự số 0 trong chuỗi (Zero-Index Trap)**
> - *Hiện tượng:* Học sinh gọi `ký tự (0) của (chuỗi)`.
> - *Hậu quả:* Trong Scratch không có vị trí 0! Khối này sẽ trả về chuỗi rỗng (`""`).
> - *Khắc phục:* Luôn nhớ ký tự đầu tiên là `ký tự (1)`.

> **Bẫy 2: Dấu cách (khoảng trắng) cũng là một ký tự hợp lệ**
> - *Hiện tượng:* Học sinh đếm chuỗi `"IKH EDU"` chỉ có 6 chữ cái nên đoán độ dài là 6.
> - *Hậu quả:* Kết quả thực tế là **7**! Dấu cách ở giữa cũng chiếm đúng một vị trí chỉ số như mọi chữ cái bình thường.
> - *Khắc phục:* Luôn tính cả dấu cách khi đếm độ dài và cắt chuỗi.

> **Bẫy 3: Quên làm rỗng biến `chuoi_con` trước khi bắt đầu ghép**
> - *Hiện tượng:* Không dùng lệnh `đặt [chuoi_con v] thành []` ở đầu kịch bản.
> - *Hậu quả:* Nếu kịch bản chạy lần thứ hai, chuỗi con mới sẽ bị ghép nối đuôi vào chuỗi con của lần chạy trước!
> - *Khắc phục:* Luôn dọn sạch chuỗi tích lũy trước vòng lặp.

---

## 6. Bộ câu hỏi trắc nghiệm củng cố (Concept Quizzes)

1. **Với chuỗi văn bản `"ROBOT"`, khối `độ dài của (chuỗi)` trả về kết quả là:**
   - A. 4
   - B. 5 *(Đáp án đúng: có 5 ký tự)*
   - C. 6
   - D. 0

2. **Ký tự đầu tiên của một chuỗi trong Scratch được lấy bằng khối lệnh nào?**
   - A. `ký tự (0) của (chuỗi)`
   - B. `ký tự (1) của (chuỗi)` *(Đáp án đúng)*
   - C. `ký tự (-1) của (chuỗi)`
   - D. `phần tử (1) của (chuỗi)`

3. **Để lấy ký tự cuối cùng của chuỗi văn bản bất kỳ `S`, ta dùng khối:**
   - A. `ký tự (cuối) của (S)`
   - B. `ký tự (độ dài của (S)) của (S)` *(Đáp án đúng)*
   - C. `ký tự (độ dài của (S) - 1) của (S)`
   - D. `ký tự (-1) của (S)`

4. **Khối lệnh `kết hợp (Lap) (Trinh)` sẽ trả về kết quả là:**
   - A. `"Lap Trinh"`
   - B. `"LapTrinh"` *(Đáp án đúng: dính liền nhau không có khoảng trắng)*
   - C. `"Lap, Trinh"`
   - D. Báo lỗi

5. **Chuỗi `"TIN HOC 2026"` có độ dài bằng bao nhiêu?**
   - A. 10
   - B. 11
   - C. 12 *(Đáp án đúng: 3 chữ TIN + 1 cách + 3 chữ HOC + 1 cách + 4 số 2026 = 12)*
   - D. 9

6. **Điều kiện nào kiểm tra xem chuỗi `Email` có chứa ký tự `@` hay không?**
   - A. `< [Email v] chứa [@] ?>` *(Đáp án đúng)*
   - B. `< [@] trong [Email v] ?>`
   - C. `< [Email v] = [@] >`
   - D. `< ký tự (@) của [Email v] >`

7. **Muốn trích xuất các ký tự từ vị trí $L$ đến vị trí $R$ trong chuỗi, vòng lặp cần chạy bao nhiêu lần?**
   - A. `R - L` lần
   - B. `R - L + 1` lần *(Đáp án đúng: tính cả hai đầu mút)*
   - C. `R` lần
   - D. `L` lần

8. **Nếu ta gọi `ký tự (100) của [Scratch]`, khối lệnh sẽ trả về:**
   - A. Báo lỗi treo máy
   - B. Chuỗi rỗng `""` *(Đáp án đúng)*
   - C. Chữ `"h"`
   - D. Số 0

9. **Để ghép 3 chuỗi văn bản $A, B, C$ lại với nhau trong Scratch, ta cần:**
   - A. Lồng 2 khối `kết hợp () ()` vào nhau *(Đáp án đúng)*
   - B. Dùng khối `kết hợp (A) (B) (C)`
   - C. Dùng toán tử cộng `A + B + C`
   - D. Dùng danh sách

10. **Biểu thức `kết hợp (kết hợp [Xin] [ ]) [chao]` sẽ tạo ra chuỗi:**
    - A. `"Xin chao"` *(Đáp án đúng: có một dấu cách ở giữa)*
    - B. `"Xinchao"`
    - C. `"Xin  chao"`
    - D. `"chao Xin"`
