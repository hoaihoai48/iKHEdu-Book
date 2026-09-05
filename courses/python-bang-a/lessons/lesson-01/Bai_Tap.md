# Danh Sách Bài Tập Thực Hành: Bài 01

> Nguồn problems: l01 | Tổng 25 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-6
* P1 (Cơ bản): Bài 7-12
* P2 (Luyện tập): Bài 13-18
* P3 (Vận dụng): Bài 19-25
---

### Bài 1 (P0): Lời chào robot
* **Mã bài toán:** `pya_l01_p01_loi_chao_robot`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Khi một hệ thống tự hành hoặc robot công nghiệp được khởi động trong phòng thực hành lập trình, hệ thống cần gửi thông điệp chào mừng đầu tiên ra thiết bị đầu ra tiêu chuẩn.
* **Nhiệm vụ:** Viết chương trình in ra chính xác dòng thông điệp: `Xin chao cac ban! Toi la Robot Python.`
* **Input:** Không có dữ liệu vào.
* **Output:** In ra một dòng chứa câu chào đúng mẫu.
* **Sample:** ### Input
```text

```
### Output
```text
Xin chao cac ban! Toi la Robot Python.
```
### Giải thích
In chính xác câu chào ra màn hình theo đúng quy định.

---

### Bài 2 (P0): Câu đối ngày tết
* **Mã bài toán:** `pya_l01_p02_cau_doi_tet`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong ứng dụng hiển thị bảng điện tử chào mừng năm mới, hệ thống cần in hai vế câu đối truyền thống trên hai dòng riêng biệt.
* **Nhiệm vụ:** In ra đúng hai dòng chữ, mỗi dòng là một vế câu đối:
  - Dòng 1: `Chuc mung nam moi`
  - Dòng 2: `Van su nhu y`
* **Input:** Không có dữ liệu vào.
* **Output:** In ra hai dòng theo đúng quy định.
* **Sample:** ### Input
```text

```
### Output
```text
Chuc mung nam moi
Van su nhu y
```
### Giải thích
Sử dụng hai lệnh `print()` liên tiếp để in trên hai dòng riêng biệt.

---

### Bài 3 (P0): Đọc và in số nguyên
* **Mã bài toán:** `pya_l01_p05_doc_in_so_nguyen`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Máy đếm vé tham quan cần nhận vào mã số may mắn của khách và hiển thị lại mã số đó.
* **Nhiệm vụ:** Nhập một số nguyên $N$ từ bàn phím và in số nguyên đó ra màn hình.
* **Input:** Một dòng duy nhất chứa số nguyên $N$ ($-10^9 \le N \le 10^9$).
* **Output:** In ra số nguyên $N$.
* **Sample:** ### Input
```text
2026
```
### Output
```text
2026
```
### Giải thích
Nhập vào số 2026 và in lại đúng số 2026.

---

### Bài 4 (P0): In số trên một hàng với sep
* **Mã bài toán:** `pya_l01_p03_in_so_sep`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Thầy giáo yêu cầu in 5 chữ số đầu tiên từ 1 đến 5 được nối với nhau bằng dấu gạch ngang `-`.
* **Nhiệm vụ:** Viết chương trình in ra dòng chữ: `1-2-3-4-5`.
* **Input:** Không có dữ liệu vào.
* **Output:** In ra dòng chữ `1-2-3-4-5` bằng cách tận dụng tham số `sep`.
* **Sample:** ### Input
```text

```
### Output
```text
1-2-3-4-5
```
### Giải thích
Các số từ 1 đến 5 được in cách nhau bằng dấu `-`.

---

### Bài 5 (P0): Nhân đôi giá trị
* **Mã bài toán:** `pya_l01_p25_nhan_doi_gia_tri`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Bác Tư là một nông dân giỏi nổi tiếng ở vùng Đồng Tháp Mười. Năm đầu tiên bác trồng thử nghiệm một giống cây ăn trái mới và thu hoạch được $N$ quả. Nhờ áp dụng kỹ thuật chăm sóc tiên tiến, mỗi năm tiếp theo sản lượng lại tăng gấp đôi so với năm trước. Bác muốn dự đoán sản lượng thu hoạch sau đúng một năm tới để lên kế hoạch bán hàng cho đại lý.
* **Nhiệm vụ:** Nhập số nguyên $N$ từ bàn phím. In ra giá trị gấp đôi của $N$ (tức $N \times 2$).
* **Input:** Một dòng chứa số nguyên $N$ ($0 \le N \le 10^9$).
* **Output:** In ra giá trị $N \times 2$.
* **Sample:** ### Input
```text
75
```
### Output
```text
150
```
### Giải thích
Gấp đôi của 75 là $75 \times 2 = 150$.

---

### Bài 6 (P0): In không xuống dòng với end
* **Mã bài toán:** `pya_l01_p19_in_end_cung_dong`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Máy tính cần in hai từ ghép thành một khẩu hiệu trên cùng một dòng bằng hai lệnh `print()` riêng biệt.
* **Nhiệm vụ:** Viết chương trình dùng hai lệnh `print()` có tham số `end` để in ra trên một dòng: `Lap trinh rat vui!`
* **Input:** Không có dữ liệu vào.
* **Output:** In khẩu hiệu trên một dòng.
* **Sample:** ### Input
```text

```
### Output
```text
Lap trinh rat vui!
```
### Giải thích
Lệnh thứ nhất in `Lap trinh ` có `end=" "`, lệnh thứ hai in `rat vui!`.

---

### Bài 7 (P1): Hoán đổi vị trí hai biến
* **Mã bài toán:** `pya_l01_p11_hoan_doi_hai_bien`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Hai bạn An và Bình có hai thẻ số mang giá trị $A$ và $B$. Hai bạn muốn đổi thẻ cho nhau.
* **Nhiệm vụ:** Nhập hai số nguyên $A$ và $B$ trên 2 dòng. Thực hiện hoán đổi giá trị của hai biến, sau đó in ra $A$ và $B$ sau khi hoán đổi trên cùng một dòng cách nhau dấu cách.
* **Input:** Hai dòng chứa hai số nguyên $A$ và $B$ ($-10^9 \le A, B \le 10^9$).
* **Output:** Một dòng in ra giá trị mới của $A$ và $B$ cách nhau dấu cách.
* **Sample:** ### Input
```text
10
 99
```
### Output
```text
99 10
```
### Giải thích
Ban đầu $A = 10, B = 99$. Sau khi đổi chỗ, $A = 99$ và $B = 10$.

---

### Bài 8 (P1): Tổng hai số nguyên 2 dòng
* **Mã bài toán:** `pya_l01_p21_tong_hai_so_2_dong`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Bạn Minh có $A$ viên bi, bạn Nam có $B$ viên bi. Cần tính tổng số bi của cả hai bạn.
* **Nhiệm vụ:** Nhập hai số nguyên $A$ và $B$ lần lượt trên 2 dòng riêng biệt. In ra tổng $A + B$.
* **Input:** - Dòng 1: Số nguyên $A$ ($0 \le A \le 10^9$).
 - Dòng 2: Số nguyên $B$ ($0 \le B \le 10^9$).
* **Output:** In ra một số nguyên duy nhất là tổng $A + B$.
* **Sample:** ### Input
```text
15
 25
```
### Output
```text
40
```
### Giải thích
Tổng $15 + 25 = 40$.

---

### Bài 9 (P1): Hiệu hai số nguyên
* **Mã bài toán:** `pya_l01_p22_hieu_hai_so`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Bác thợ may có cuộn vải dài $A$ mét, đã cắt may hết $B$ mét. Cần tính độ dài vải còn lại.
* **Nhiệm vụ:** Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra hiệu $A - B$.
* **Input:** Hai dòng, mỗi dòng chứa một số nguyên $A, B$ ($0 \le B \le A \le 10^9$).
* **Output:** In ra số nguyên là kết quả của $A - B$.
* **Sample:** ### Input
```text
100
 35
```
### Output
```text
65
```
### Giải thích
Vải còn lại là $100 - 35 = 65$ mét.

---

### Bài 10 (P1): Tích hai số nguyên
* **Mã bài toán:** `pya_l01_p23_tich_hai_so`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Tại nhà máy sản xuất bánh kẹo xuất khẩu Đại Phát, dây chuyền đóng gói hoạt động tự động theo quy trình nghiêm ngặt. Mỗi thùng carton tiêu chuẩn chứa đúng $A$ hộp sản phẩm, và bên trong mỗi hộp lại được xếp gọn gàng $B$ chiếc kẹo thơm ngon. Trước mỗi ca xuất hàng, hệ thống quản lý kho cần tính toán chính xác tổng số lượng kẹo thực tế có trong một thùng để đối soát với phiếu giao hàng.
* **Nhiệm vụ:** Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra tích $A \times B$.
* **Input:** Hai dòng, mỗi dòng chứa một số nguyên $A, B$ ($0 \le A, B \le 10^4$).
* **Output:** In ra số nguyên là tích $A \times B$.
* **Sample:** ### Input
```text
12
 8
```
### Output
```text
96
```
### Giải thích
Tổng số kẹo là $12 \times 8 = 96$ chiếc.

---

### Bài 11 (P1): Cặp số nhân đôi
* **Mã bài toán:** `pya_l01_p04_cap_so_nhan_doi`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong module xử lý tín hiệu số, mạch khuếch đại nhận một tín hiệu đầu vào có biên độ $A$ và nhân đôi biên độ đó lên gấp 2 lần.
* **Nhiệm vụ:** Nhập vào số nguyên $A$. Hãy tính và in ra giá trị của tín hiệu sau khi nhân đôi ($A \times 2$).
* **Input:** Gồm một số tự nhiên $A$ ($0 \le A \le 10^6$).
* **Output:** In ra một số nguyên là kết quả nhân đôi ($A \times 2$).
* **Sample:** ### Input
```text
15
```
### Output
```text
30
```
### Giải thích

Giá trị đầu vào là $15$. Khi nhân đôi, ta có: $15 \times 2 = 30$. Do đó, kết quả in ra màn hình là `30`.

---

### Bài 12 (P1): Tuổi của bé sau 5 năm
* **Mã bài toán:** `pya_l01_p18_tuoi_cua_be_sau_5_nam`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong hệ thống quản lý hồ sơ nhân khẩu học, độ tuổi của một đối tượng được tính toán và dự đoán theo các mốc thời gian trong tương lai.
* **Nhiệm vụ:** Cho số tuổi hiện tại $N$ ($1 \le N \le 12$). Hãy tính và in ra số tuổi của người đó sau 5 năm nữa.
* **Input:** Một dòng duy nhất chứa số tự nhiên $N$ ($1 \le N \le 12$).
* **Output:** Một số nguyên duy nhất là số tuổi của Bo sau 5 năm.
* **Sample:** ### Input
```text
8
```
### Output
```text
13
```
### Giải thích

Học sinh 8 tuổi, sau 5 năm nữa nhỏ: $8 + 5 = 13$ tuổi

---

### Bài 13 (P2): Lời chúc sinh nhật cá nhân hóa
* **Mã bài toán:** `pya_l01_p12_chuc_sinh_nhat`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bạn muốn viết một chương trình in ra thiệp chúc mừng sinh nhật theo tên và tuổi của bạn bè.
* **Nhiệm vụ:** Nhập dòng 1 là tên bạn (chuỗi ký tự), dòng 2 là số tuổi $T$ (số nguyên). In ra dòng chữ: `Chuc mung sinh nhat <Ten>, ban tron <Tuoi> tuoi!`
* **Input:** - Dòng 1: Chuỗi ký tự không dấu $Ten$.
 - Dòng 2: Số nguyên $Tuoi$ ($1 \le Tuoi \le 100$).
* **Output:** In ra câu chúc đúng mẫu.
* **Sample:** ### Input
```text
Nam
 10
```
### Output
```text
Chuc mung sinh nhat Nam, ban tron 10 tuoi!
```
### Giải thích
Ghép tên và tuổi vào đúng vị trí của câu chúc.

---

### Bài 14 (P2): Chiếc hộp hoán đổi bí mật
* **Mã bài toán:** `pya_l01_p07_chiec_hop_hoan_doi_bi_mat`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Giờ ra chơi, bạn Tèo có hai chiếc hộp xinh xắn: hộp $A$ đựng số kẹo của Tèo, hộp $B$ đựng số kẹo của Tí. Hai bạn cười khúc khích và đố nhau đổi kẹo cho nhau (số kẹo trong hộp $A$ chuyển sang hộp $B$, và số kẹo trong hộp $B$ chuyển sang hộp $A$). Cả hai loay hoay mãi chưa đổi xong. Hãy giúp hai bạn hoán đổi hai hộp kẹo này.
* **Nhiệm vụ:** Nhập vào 2 số nguyên $A$ và $B$. Hãy hoán đổi giá trị của 2 biến và in ra giá trị mới của $A$ và $B$ sau khi hoán đổi (cách nhau một dấu cách).
* **Input:** Dòng 1 chứa số $A$, dòng 2 chứa số $B$ ($0 \le A, B \le 10^9$).
* **Output:** In ra hai số $A$ và $B$ sau khi hoán đổi trên cùng một dòng.
* **Sample:** ### Input
```text
7
12
```
### Output
```text
12 7
```
### Giải thích

Ban đầu $A=7, B=12$. Sau khi đổi: $A=12, B=7$.

---

### Bài 15 (P2): Tấm danh thiếp thông minh
* **Mã bài toán:** `pya_l01_p17_tam_danh_thiep_thong_minh`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Hệ thống quản lý thông tin hội thảo cần in thẻ danh thiếp tự động cho người tham dự sau khi nhập tên.
* **Nhiệm vụ:** Nhập vào tên của một người (chuỗi ký tự). Hãy in ra thông điệp chào mừng theo mẫu: `Xin chao ban [Ten]!`
* **Input:** Một dòng duy nhất chứa chuỗi ký tự tên của người dùng.
* **Output:** In ra dòng thông điệp: `Xin chao ban <Ten>!` (giữa chữ `ban` và tên cách nhau một dấu cách, cuối câu có dấu chấm than `!`).
* **Sample:** ### Input
```text
Nam
```
### Output
```text
Xin chao ban Nam!
```
### Giải thích

Với tên nhập vào là `"Nam"`, chương trình ghép chuỗi `"Xin chao ban "` với `"Nam"` và thêm dấu chấm than `!` ở cuối, tạo thành dòng chữ `Xin chao ban Nam!`.

---

### Bài 16 (P2): Cửa hàng bánh rán
* **Mã bài toán:** `pya_l01_p06_cua_hang_banh_ran`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Hệ thống máy tính tiền tự động tại căng-tin cần tính tổng giá trị hóa đơn khi khách hàng mua nhiều sản phẩm cùng loại với đơn giá cố định.
* **Nhiệm vụ:** Nhập vào đơn giá mỗi sản phẩm $a$ (nghìn đồng) và số lượng sản phẩm $b$. Hãy tính tổng số tiền (nghìn đồng) cần thanh toán.
* **Input:** Nhập vào 2 số tự nhiên $a$ và $b$ mỗi số trên một dòng ($1 \le a \le 100, 1 \le b \le 100$).
* **Output:** In ra số tiền Doraemon cần trả.
* **Sample:** ### Input
```text
12
5
```
### Output
```text
60
```
### Giải thích

Mua 5 chiếc bánh, mỗi chiếc 12 nghìn đồng: $12 \times 5 = 60$.

---

### Bài 17 (P2): In bảng phép nhân cơ bản
* **Mã bài toán:** `pya_l01_p15_phep_nhan_bang`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Học sinh học bảng nhân muốn in một dòng phép tính dạng `A x B = C` thật đẹp mắt.
* **Nhiệm vụ:** Nhập hai số nguyên $A$ và $B$ trên 2 dòng. In ra chính xác theo định dạng: `A x B = C` (với $C = A \times B$).
* **Input:** Hai dòng, dòng 1 là $A$, dòng 2 là $B$ ($1 \le A, B \le 100$).
* **Output:** In ra dòng phép tính theo đúng mẫu, các thành phần cách nhau bởi dấu cách.
* **Sample:** ### Input
```text
7
 9
```
### Output
```text
7 x 9 = 63
```
### Giải thích
Tính $7 \times 9 = 63$ và in theo mẫu `7 x 9 = 63`.

---

### Bài 18 (P2): Tổng hai số trên cùng 1 dòng
* **Mã bài toán:** `pya_l01_p09_tong_hai_so_cung_dong`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Trong đề thi chuẩn, hai số $A$ và $B$ thường được nhập trên cùng 1 dòng ngăn cách bởi dấu cách.
* **Nhiệm vụ:** Nhập hai số nguyên $A, B$ trên cùng một dòng. In ra tổng $A + B$.
* **Input:** Một dòng duy nhất chứa hai số nguyên $A$ và $B$ cách nhau một dấu cách ($-10^9 \le A, B \le 10^9$).
* **Output:** In ra tổng $A + B$.
* **Sample:** ### Input
```text
45 55
```
### Output
```text
100
```
### Giải thích
Đọc bằng `map(int, input().split())` và in ra $45 + 55 = 100$.

---

### Bài 19 (P3): Đổi thước kẻ milimet
* **Mã bài toán:** `pya_l01_p20_doi_thuoc_ke_milimet`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong thiết kế cơ khí chính xác, kích thước của chi tiết gia công gồm phần kích thước chẵn $a\text{ cm}$ và phần sai số dư $b\text{ mm}$.
* **Nhiệm vụ:** Cho biết $1\text{ cm} = 10\text{ mm}$. Hãy quy đổi toàn bộ độ dài gồm $a\text{ cm}$ và $b\text{ mm}$ sang đơn vị milimet ($\text{mm}$).
* **Input:** * Dòng 1: Chứa số tự nhiên $a$ ($1 \le a \le 1000$).
 * Dòng 2: Chứa số tự nhiên $b$ ($1 \le b \le 1000$).
* **Output:** Một số tự nhiên duy nhất là độ dài của thước tính theo đơn vị milimet ($\text{mm}$).
* **Sample:** ### Input
```text
2
5
```
### Output
```text
25
```
### Giải thích

$2\text{ cm} = 20\text{ mm}$. Tổng cộng là: $20 + 5 = 25\text{ mm}$.

---

### Bài 20 (P3): Ghép ngày tháng năm định dạng chuẩn
* **Mã bài toán:** `pya_l01_p14_ghep_ngay_thang_nam`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Hệ thống cần nhận 3 số nguyên là Ngày, Tháng, Năm và in ra dạng chuẩn hiển thị trên lịch.
* **Nhiệm vụ:** Nhập 3 số nguyên $D, M, Y$ trên cùng một dòng. In ra theo định dạng: `D/M/Y`.
* **Input:** Một dòng chứa 3 số nguyên $D, M, Y$ cách nhau dấu cách ($1 \le D \le 31$, $1 \le M \le 12$, $1900 \le Y \le 2100$).
* **Output:** In ra dạng `D/M/Y`.
* **Sample:** ### Input
```text
4 9 2026
```
### Output
```text
4/9/2026
```
### Giải thích
Tận dụng lệnh `print(d, m, y, sep="/")`.

---

### Bài 21 (P3): Đoàn tàu toa xe ghép số
* **Mã bài toán:** `pya_l01_p08_doan_tau_toa_xe_ghep_so`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Sáng sớm ở ga xe lửa, có 2 toa xe chở 2 con số $a$ và $b$ vừa chạy vào sân ga. Bác trưởng ga vui tính muốn nhìn thấy cả hai kết quả:
 1. Nếu ghép 2 toa tàu lại thành một dãy số (Ghép chữ).
 2. Nếu cộng giá trị của 2 toa tàu lại với nhau (Cộng số học).
Bác loay hoay mãi với cuốn sổ ghi chép. Hãy giúp bác trưởng ga làm cả hai việc này.
* **Nhiệm vụ:** Nhập vào 2 số tự nhiên $a$ và $b$. Dòng 1 in ra kết quả khi ghép chuỗi chữ. Dòng 2 in ra kết quả khi cộng số.
* **Input:** Nhập 2 số tự nhiên $a, b$ ($1 \le a, b \le 100$) trên 2 dòng.
* **Output:** * Dòng 1: Chuỗi ghép dính $a$ và $b$.
 * Dòng 2: Tổng giá trị số học $a + b$.
* **Sample:** ### Input
```text
25
30
```
### Output
```text
2530
55
```
### Giải thích

Dòng 1 ghép chữ: `"25" + "30" = "2530"`.
Dòng 2 cộng số: $25 + 30 = 55$.

---

### Bài 22 (P3): Chênh lệch tuổi của hai anh em
* **Mã bài toán:** `pya_l01_p16_chenh_lech_tuoi`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Anh hơn em một số tuổi. Biết tuổi của anh là $A$ và tuổi của em là $E$. Cần tính số tuổi anh hơn em và in câu thông báo.
* **Nhiệm vụ:** Nhập hai số nguyên $A$ và $E$ trên cùng 1 dòng ($1 \le E \le A \le 100$). In ra một dòng có nội dung: `Anh hon em <so_tuoi> tuoi.`
* **Input:** Một dòng chứa hai số nguyên $A$ và $E$ cách nhau dấu cách.
* **Output:** In ra câu kết luận đúng mẫu.
* **Sample:** ### Input
```text
12 7
```
### Output
```text
Anh hon em 5 tuoi.
```
### Giải thích
Hiệu số tuổi $12 - 7 = 5$. In ra `Anh hon em 5 tuoi.`.

---

### Bài 23 (P3): Bốn phép tính đồng thời
* **Mã bài toán:** `pya_l01_p13_bon_phep_tinh`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Máy tính cầm tay cần hiển thị bảng kết quả 3 phép tính cơ bản giữa hai số nguyên.
* **Nhiệm vụ:** Nhập hai số nguyên $A$ và $B$ trên cùng 1 dòng. In ra 3 dòng:
* **Input:** Một dòng chứa hai số nguyên $A$ và $B$ cách nhau dấu cách ($-10^4 \le A, B \le 10^4$).
* **Output:** 3 dòng lần lượt chứa tổng, hiệu và tích.
* **Sample:** ### Input
```text
8 5
```
### Output
```text
13
3
40
```
### Giải thích
$8 + 5 = 13$, $8 - 5 = 3$, $8 \times 5 = 40$.

---

### Bài 24 (P3): Cỗ máy thời gian 3 thế hệ
* **Mã bài toán:** `pya_l01_p10_co_may_thoi_gian_3_the_he`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong bài toán phân tích nhân khẩu học, tuổi của ba thành viên trong một gia đình thuộc ba thế hệ liên tiếp được ghi nhận.
* **Nhiệm vụ:** Cho số tuổi của người con là $a$, người bố hơn con $b$ tuổi, và người ông hơn bố $c$ tuổi. Hãy tính tuổi của bố, tuổi của ông và tổng tuổi của cả ba người.
* **Input:** Ba dòng lần lượt chứa 3 số nguyên $a, b, c$ ($1 \le a \le 20, 20 \le b \le 40, 20 \le c \le 40$).
* **Output:** Gồm 3 dòng tương ứng với 3 yêu cầu của bài toán.
* **Sample:** ### Input
```text
10
30
25
```
### Output
```text
40
65
115
```
### Giải thích

- Tuổi Nam: $10$.
- Tuổi Bố: $10 + 30 = 40$.
- Tuổi Ông: $40 + 25 = 65$.
- Tổng cả 3 người: $10 + 40 + 65 = 115$.

---

### Bài 25 (P3): Vé tham quan chùa hương
* **Mã bài toán:** `pya_l01_p24_ve_tham_quan_chua_huong`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Cuối tuần này, một đoàn khách nhỏ chuẩn bị đi tham quan Chùa Hương Tích. Để lên chùa, đoàn phải đi thuyền rồi đi cáp treo ngắm cảnh núi rừng:
 * Vé thuyền: người lớn $a$ nghìn đồng/người, trẻ em $b$ nghìn đồng/người.
 * Vé cáp treo: người lớn $x$ nghìn đồng/người, trẻ em $y$ nghìn đồng/người.
 * Đoàn khách có tổng cộng $n$ người, trong đó có $m$ trẻ em.
Cô hướng dẫn viên cần tính tiền để mua vé cho cả đoàn. Hãy giúp cô tính tổng số tiền cần chuẩn bị.
* **Nhiệm vụ:** Hãy tính tổng số tiền (đơn vị nghìn đồng) cần chuẩn bị để mua toàn bộ vé thuyền và vé cáp treo cho cả đoàn khách.
* **Input:** Gồm 6 dòng lần lượt chứa các số tự nhiên: $a, b, x, y, n, m$ ($0 < a, b, x, y < 100$; $0 \le m \le n < 100$).
* **Output:** In ra một số nguyên duy nhất là tổng số tiền cần chuẩn bị.
* **Sample:** ### Input
```text
20
10
50
30
10
4
```
### Output
```text
580
```
### Giải thích

- Số trẻ em: $4$, số người lớn: $10 - 4 = 6$ người.
- Tiền thuyền: $6 \times 20 + 4 \times 10 = 120 + 40 = 160$.
- Tiền cáp treo: $6 \times 50 + 4 \times 30 = 300 + 120 = 420$.
- Tổng tiền: $160 + 420 = 580$ nghìn đồng.

---
