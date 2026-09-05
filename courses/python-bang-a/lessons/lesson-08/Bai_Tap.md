# Danh Sách Bài Tập Thực Hành: Bài 08: Tách chữ số

> Nguồn problems: l10 | Tổng 14 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-3
* P1 (Cơ bản): Bài 4-6
* P2 (Luyện tập): Bài 7-9
* P3 (Vận dụng): Bài 10-14
---

### Bài 1 (P0): Lấy chữ số đơn vị & chục
* **Mã bài toán:** `pya_l10_p01_lay_chu_so_don_vi_chuc`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong hệ thống xử lý số liệu đo lường, mỗi con số gồm hai chữ số đều mang thông tin độc lập ở hàng chục và hàng đơn vị. Để chuẩn hóa dữ liệu, hệ thống cần tách riêng hai giá trị này.
* **Nhiệm vụ:** Nhập một số nguyên dương $N$ có đúng 2 chữ số. Hãy in ra chữ số hàng chục và chữ số hàng đơn vị của $N$ trên cùng một dòng, cách nhau một khoảng trắng.
* **Input:** Một số nguyên $N$ ($10 \le N \le 99$).
* **Output:** Chữ số hàng chục, tiếp theo là chữ số hàng đơn vị.
* **Sample:** ### Input
```text
47
```
### Output
```text
4 7
```
### Giải thích

Với dữ liệu đầu vào là `47`, kết quả thu được tương ứng là `4 7`.

---

### Bài 2 (P0): Tổng chữ số của số 3 chữ số
* **Mã bài toán:** `pya_l10_p02_tong_chu_so_cua_so_3_chu_so`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.
* **Nhiệm vụ:** Nhập một số nguyên dương $N$ có đúng 3 chữ số. Hãy tính tổng của 3 chữ số đó.
* **Input:** Một số tự nhiên $N$ ($100 \le N \le 999$).
* **Output:** Tổng 3 chữ số.
* **Sample:** ### Input
```text
358
```
### Output
```text
16
```
### Giải thích

$3 + 5 + 8 = 16$.

---

### Bài 3 (P0): Tổng các chữ số của N
* **Mã bài toán:** `pya_l10_p03_tong_cac_chu_so_cua_n`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.
* **Nhiệm vụ:** Cho một số tự nhiên $N$ bất kỳ. Hãy tính tổng tất cả các chữ số cấu tạo nên số $N$.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^{18}$).
* **Output:** Tổng các chữ số của $N$.
* **Sample:** ### Input
```text
2024
```
### Output
```text
8
```
### Giải thích

$2 + 0 + 2 + 4 = 8$.

---

### Bài 4 (P1): Số đảo ngược
* **Mã bài toán:** `pya_l10_p08_so_dao_nguoc`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Thao tác đảo ngược thứ tự các chữ số là nền tảng quan trọng trong các bài toán kiểm tra tính đối xứng và biến đổi số học.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy in ra số đảo ngược của $N$ (bỏ qua các chữ số 0 ở đầu nếu có sau khi đảo).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Số đảo ngược.
* **Sample:** ### Input
```text
1234
```
### Output
```text
4321
```
### Giải thích

Đảo ngược các chữ số.

---

### Bài 5 (P1): Tích các chữ số khác không
* **Mã bài toán:** `pya_l10_p05_tich_cac_chu_so_khac_khong`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong một số thuật toán tạo mã băm và mã kiểm tra dữ liệu, tích của các chữ số có nghĩa (khác số 0) thường được dùng để tạo khóa đại diện cho số nguyên ban đầu.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tính tích của tất cả các chữ số **khác 0** của $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Tích các chữ số khác 0.
* **Sample:** ### Input
```text
205
```
### Output
```text
10
```
### Giải thích

Bỏ qua chữ số 0, tích là $2 \times 5 = 10$.

---

### Bài 6 (P1): Đếm số lượng chữ số
* **Mã bài toán:** `pya_l10_p04_dem_so_luong_chu_so`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong lưu trữ dữ liệu số học, việc xác định độ dài số lượng chữ số của một số nguyên giúp hệ thống cấp phát bộ nhớ và căn chỉnh bảng biểu một cách chính xác.
* **Nhiệm vụ:** Cho số nguyên không âm $N$. Hãy cho biết số $N$ có bao nhiêu chữ số.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^{18}$).
* **Output:** Số lượng chữ số.
* **Sample:** ### Input
```text
123456
```
### Output
```text
6
```
### Giải thích

Có 6 chữ số.

---

### Bài 7 (P2): Kiểm tra số đối xứng (palindrome)
* **Mã bài toán:** `pya_l10_p09_kiem_tra_so_doi_xung_palindrome`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Na rất thích soi gương vì trong gương mọi thứ trông giống hệt ở ngoài. Một hôm, bạn Tí đố Na tìm những con số cũng "soi gương" được như vậy. Đó chính là số đối xứng: số đọc từ trái sang phải hay từ phải sang trái đều thu được số giống hệt nhau (ví dụ: $121$, $1331$, $5$, $88$). Na loay hoay mãi chưa kiểm tra hết, hãy bạn ấy.
* **Nhiệm vụ:** Nhập vào số tự nhiên $N$. Kiểm tra xem $N$ có phải số đối xứng không. Nếu có in `YES`, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^{15}$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
12321
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `12321`, kết quả thu được tương ứng là `YES`.

---

### Bài 8 (P2): Căn bậc số học
* **Mã bài toán:** `pya_l10_p13_can_bac_so_hoc_digital_root`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bạn Mít chơi trò "gộp hạt đậu": mỗi lần bạn ấy cộng dồn liên tục các chữ số của một số tự nhiên cho đến khi chỉ còn lại đúng **một chữ số duy nhất**, và bạn ấy gọi đó là căn bậc số học của số đó.
 Ví dụ: $9875 \to 9 + 8 + 7 + 5 = 29 \to 2 + 9 = 11 \to 1 + 1 = 2$. Căn bậc số học của 9875 là 2. Mít cộng mãi mà vẫn hay nhầm, hãy bạn ấy tính thật nhanh.
* **Nhiệm vụ:** Nhập vào số tự nhiên $N$. Hãy tìm căn bậc số học của $N$.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).
* **Output:** Một chữ số duy nhất (từ 1 đến 9).
* **Sample:** ### Input
```text
9875
```
### Output
```text
2
```
### Giải thích

Với dữ liệu đầu vào là `9875`, kết quả thu được tương ứng là `2`.

---

### Bài 9 (P2): Chữ số lớn nhất & nhỏ nhất
* **Mã bài toán:** `pya_l10_p07_chu_so_lon_nhat_nho_nhat`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Thí sinh cần tìm giá trị lớn nhất hoặc nhỏ nhất trong một tập dữ liệu. Hãy viết chương trình tìm kiếm.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tìm chữ số lớn nhất và chữ số nhỏ nhất xuất hiện trong số $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^{12}$).
* **Output:** Chữ số lớn nhất, theo sau là chữ số nhỏ nhất, cách nhau một khoảng trắng.
* **Sample:** ### Input
```text
9418
```
### Output
```text
9 1
```
### Giải thích

Chữ số lớn nhất là 9, nhỏ nhất là 1.

---

### Bài 10 (P3): Số may mắn chứa số 7
* **Mã bài toán:** `pya_l10_p11_so_may_man_chua_so_7`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong hệ thống lọc vé thưởng tự động, các số thẻ có chứa chữ số 7 được coi là thỏa mãn điều kiện nhận mã ưu tiên. Hệ thống cần kiểm tra nhanh tính chất này trên mỗi số thẻ.
* **Nhiệm vụ:** An coi số 7 là con số mang lại may mắn. Một số tự nhiên $N$ được gọi là "May mắn" nếu trong các chữ số của nó có ít nhất một chữ số 7. Cho số $N$, hãy kiểm tra xem $N$ có may mắn không. In `YES` nếu có, `NO` nếu không.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
372
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `372`, kết quả thu được tương ứng là `YES`.

---

### Bài 11 (P3): Đếm chữ số chẵn và lẻ
* **Mã bài toán:** `pya_l10_p06_dem_chu_so_chan_va_le`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Phân tích cấu trúc chẵn lẻ của các chữ số là bước kiểm định tính cân bằng số học trong các hệ thống mã hóa và kiểm thử dữ liệu đầu vào.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy đếm xem trong số $N$ có bao nhiêu chữ số chẵn (0, 2, 4, 6, 8) và bao nhiêu chữ số lẻ (1, 3, 5, 7, 9).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{12}$).
* **Output:** In hai số nguyên cách nhau một khoảng trắng: số lượng chữ số chẵn trước, số lượng chữ số lẻ sau.
* **Sample:** ### Input
```text
2035
```
### Output
```text
2 2
```
### Giải thích

Chữ số chẵn: 2, 0 (2 số). Chữ số lẻ: 3, 5 (2 số).

---

### Bài 12 (P3): Số tăng giảm đẹp
* **Mã bài toán:** `pya_l10_p14_so_tang_giam_dep`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Cún thích xếp những bậc thang bằng các chữ số. Có hôm bạn ấy xếp được cầu thang đi lên thật đẹp, có hôm lại xếp được cầu thang đi xuống thật gọn. Cô giáo gọi đó là:
 * **Số Tăng Dần:** Nếu mỗi chữ số đứng sau luôn lớn hơn chữ số đứng trước nó (ví dụ: $1379, 258$).
 * **Số Giảm Dần:** Nếu mỗi chữ số đứng sau luôn nhỏ hơn chữ số đứng trước nó (ví dụ: $9641, 852$). Cún nhờ em nhìn giúp xem mỗi con số là cầu thang lên, cầu thang xuống hay không phải cầu thang.
* **Nhiệm vụ:** Cho số $N$. In ra `TANG` nếu $N$ là số tăng dần, in `GIAM` nếu $N$ là số giảm dần, và in `KHONG` nếu không thỏa mãn cả 2 tính chất trên.
* **Input:** Một số nguyên $N$ ($10 \le N \le 10^{12}$).
* **Output:** `TANG`, `GIAM` hoặc `KHONG`.
* **Sample:** ### Input
```text
1379
```
### Output
```text
TANG
```
### Giải thích

Với dữ liệu đầu vào là `1379`, kết quả thu được tương ứng là `TANG`.

---

### Bài 13 (P3): Số toàn chẵn hoặc toàn lẻ
* **Mã bài toán:** `pya_l10_p10_so_toan_chan_hoac_toan_le`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Lớp của Bi chia thành hai đội chơi xếp số rất vui. Đội Chẵn chỉ thích những số "Toàn chẵn", tức là số mà mọi chữ số của nó đều là số chẵn. Đội Lẻ lại mê những số "Toàn lẻ", tức là số mà mọi chữ số của nó đều là số lẻ. Trọng tài Tí nhờ em giúp phân xử mỗi con số, hãy bạn ấy.
* **Nhiệm vụ:** Nhập số nguyên dương $N$. In ra `TOAN CHAN` nếu $N$ là số toàn chẵn, in `TOAN LE` nếu $N$ toàn lẻ, ngược lại in `BINH THUONG`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^{15}$).
* **Output:** `TOAN CHAN`, `TOAN LE` hoặc `BINH THUONG`.
* **Sample:** ### Input
```text
2468
```
### Output
```text
TOAN CHAN
```
### Giải thích

Với dữ liệu đầu vào là `2468`, kết quả thu được tương ứng là `TOAN CHAN`.

---

### Bài 14 (P3): Đếm số lượng số đối xứng trong đoạn
* **Mã bài toán:** `pya_l10_p12_dem_so_luong_so_doi_xung_trong_doan`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Các số đối xứng (palindrome) sở hữu tính cân bằng cấu trúc đặc biệt và xuất hiện thường xuyên trong bài toán sinh mã định danh và nén số liệu.
* **Nhiệm vụ:** Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^5$). Hãy đếm xem có bao nhiêu số đối xứng nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số nguyên $A, B$ trên cùng một dòng.
* **Output:** Số lượng số đối xứng trong đoạn $[A, B]$.
* **Sample:** ### Input
```text
1 20
```
### Output
```text
10
```
### Giải thích

Các số đối xứng là: 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 (tổng cộng 10 số).

---
