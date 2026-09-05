# Danh Sách Bài Tập Thực Hành: Bài 09: Ước số, Bội số và Số nguyên tố

> Nguồn problems: l11 | Tổng 14 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-3
* P1 (Cơ bản): Bài 4-6
* P2 (Luyện tập): Bài 7-9
* P3 (Vận dụng): Bài 10-14
---

### Bài 1 (P0): Ước chung lớn nhất & BCNN
* **Mã bài toán:** `pya_l11_p06_uoc_chung_lon_nhat_bcnn`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Thí sinh cần tìm giá trị lớn nhất hoặc nhỏ nhất trong một tập dữ liệu. Hãy viết chương trình tìm kiếm.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$. Hãy tìm Ước chung lớn nhất ($\text{GCD}$) và Bội chung nhỏ nhất ($\text{LCM}$) của 2 số này.
* **Input:** Hai số nguyên $A, B$ cách nhau bởi khoảng trắng ($1 \le A, B \le 10^9$).
* **Output:** Hai số nguyên: $\text{GCD}$ trước, $\text{LCM}$ sau, cách nhau một khoảng trắng.
* **Sample:** ### Input
```text
12 18
```
### Output
```text
6 36
```
### Giải thích

$\text{GCD}(12, 18) = 6$, $\text{LCM}(12, 18) = (12 \times 18) // 6 = 36$.

---

### Bài 2 (P0): Đếm số lượng ước số
* **Mã bài toán:** `pya_l11_p02_dem_so_luong_uoc_so`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Số lượng ước số là chỉ số quan trọng phản ánh tính chia hết của một số nguyên, đồng thời là cơ sở nhận biết số nguyên tố và số chính phương.
* **Nhiệm vụ:** Cho số tự nhiên $N$. Hãy cho biết số $N$ có tất cả bao nhiêu ước số nguyên dương.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^5$).
* **Output:** Một số nguyên duy nhất là số lượng ước số của $N$.
* **Sample:** ### Input
```text
10
```
### Output
```text
4
```
### Giải thích

Số 10 có 4 ước: 1, 2, 5, 10.

---

### Bài 3 (P0): Tính tổng các ước số
* **Mã bài toán:** `pya_l11_p03_tinh_tong_cac_uoc_so`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tính tổng tất cả các ước số của $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^5$).
* **Output:** Tổng các ước số của $N$.
* **Sample:** ### Input
```text
6
```
### Output
```text
12
```
### Giải thích

Các ước là 1, 2, 3, 6 $\implies 1 + 2 + 3 + 6 = 12$.

---

### Bài 4 (P1): Hai số nguyên tố cùng nhau
* **Mã bài toán:** `pya_l11_p10_hai_so_nguyen_to_cung_nhau`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** An và Bình mỗi bạn có một rổ bi. Hai bạn muốn biết hai rổ bi của mình có "hợp nhau" không. Cô giáo bảo hai số $A$ và $B$ được gọi là nguyên tố cùng nhau nếu Ước chung lớn nhất của chúng bằng 1 ($\text{GCD}(A, B) = 1$). Hai bạn đếm mãi chưa xong, hãy hai bạn kiểm tra.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng nguyên tố cùng nhau, ngược lại in `NO`.
* **Input:** Hai số $A, B$ ($1 \le A, B \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
8 9
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `8 9`, kết quả thu được tương ứng là `YES`.

---

### Bài 5 (P1): Liệt kê tất cả ước số
* **Mã bài toán:** `pya_l11_p01_liet_ke_tat_ca_uoc_so`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Xác định toàn bộ các ước số nguyên dương của một số nguyên là phép phân tích cơ bản trong số học, giúp giải quyết các bài toán chia đều tài nguyên và phân nhóm phần tử.
* **Nhiệm vụ:** Nhập một số tự nhiên $N$. Hãy in ra tất cả các ước số nguyên dương của $N$ theo thứ tự tăng dần trên một dòng, cách nhau bởi khoảng trắng.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** Dãy các ước số của $N$.
* **Sample:** ### Input
```text
12
```
### Output
```text
1 2 3 4 6 12
```
### Giải thích

Với dữ liệu đầu vào là `12`, kết quả thu được tương ứng là `1 2 3 4 6 12`.

---

### Bài 6 (P1): Đếm ước chẵn của N
* **Mã bài toán:** `pya_l11_p07_dem_uoc_chan_cua_n`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong phân tích chia nhóm chẵn lẻ, việc xác định các ước số chẵn giúp tối ưu hóa việc phân chia tài nguyên thành các phần có kích thước chia hết cho 2.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu ước số của $N$ là số chẵn.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng ước chẵn của $N$.
* **Sample:** ### Input
```text
12
```
### Output
```text
4
```
### Giải thích

Các ước của 12 là: 1, 2, 3, 4, 6, 12. Trong đó các ước chẵn là: 2, 4, 6, 12 (có 4 số).

---

### Bài 7 (P2): Tìm ước số lớn thứ hai
* **Mã bài toán:** `pya_l11_p08_tim_uoc_so_lon_thu_hai`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho số nguyên dương $N$ ($N \ge 2$). Ước số lớn nhất của $N$ luôn là chính nó ($N$). Hãy tìm ước số lớn thứ hai của $N$ (tức là ước số lớn nhất nhưng nhỏ hơn $N$).
* **Input:** Một số tự nhiên $N$ ($2 \le N \le 10^9$).
* **Output:** Ước số lớn thứ hai của $N$.
* **Sample:** ### Input
```text
24
```
### Output
```text
12
```
### Giải thích

Ước lớn nhất là 24, lớn thứ hai là 12.

---

### Bài 8 (P2): Kiểm tra số chính phương
* **Mã bài toán:** `pya_l11_p05_kiem_tra_so_chinh_phuong`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Giờ xếp hình, Bo xếp các viên gạch thành một ô vuông thật ngay ngắn. Cô giáo cười và bảo những số gạch xếp được thành hình vuông như vậy gọi là số chính phương: số bằng bình phương của một số tự nhiên (ví dụ: $0, 1, 4, 9, 16, 25, \dots$). Bo có một đống gạch mà chưa biết có xếp vuông được không, hãy bạn ấy kiểm tra.
* **Nhiệm vụ:** Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số chính phương không. Nếu đúng in `YES`, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
25
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `25`, kết quả thu được tương ứng là `YES`.

---

### Bài 9 (P2): Phân tích ra thừa số nguyên tố
* **Mã bài toán:** `pya_l11_p13_phan_tich_ra_thua_so_nguyen_to`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Định lý cơ bản của số học khẳng định mọi số tự nhiên lớn hơn 1 đều phân tích được duy nhất thành tích các thừa số nguyên tố. Phép phân tích này đóng vai trò cốt lõi trong mật mã học.
* **Nhiệm vụ:** Mọi số tự nhiên $N \ge 2$ đều có thể phân tích thành tích của các thừa số nguyên tố. Cho số tự nhiên $N$. Hãy in ra dạng phân tích của $N$.
* **Input:** Một số tự nhiên $N$ ($2 \le N \le 10^6$).
* **Output:** Dãy các thừa số nguyên tố tăng dần theo định dạng `p1 * p2 * ...`.
* **Sample:** ### Input
```text
60
```
### Output
```text
2 * 2 * 3 * 5
```
### Giải thích

Với dữ liệu đầu vào là `60`, kết quả thu được tương ứng là `2 * 2 * 3 * 5`.

---

### Bài 10 (P3): Kiểm tra số nguyên tố
* **Mã bài toán:** `pya_l11_p04_kiem_tra_so_nguyen_to`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong giờ lập trình, thầy giáo đưa ra một bài toán kiểm tra tính chất của số. Hãy viết chương trình kiểm tra tự động.
* **Nhiệm vụ:** Nhập vào số nguyên $N$. Hãy kiểm tra xem $N$ có phải là số nguyên tố hay không. Nếu có in `YES`, nếu không in `NO`.
* **Input:** Một số nguyên $N$ ($0 \le N \le 10^7$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
7
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `7`, kết quả thu được tương ứng là `YES`.

---

### Bài 11 (P3): Đếm số nguyên tố trong đoạn
* **Mã bài toán:** `pya_l11_p09_dem_so_nguyen_to_trong_doan`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Đếm số lượng số nguyên tố trong một khoảng giá trị cho trước là dạng toán kinh điển đánh giá hiệu quả của các thuật toán sàng lọc và kiểm tra số nguyên tố.
* **Nhiệm vụ:** Cho hai số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^4$). Hãy đếm xem có bao nhiêu số nguyên tố nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số $A, B$ trên cùng một dòng.
* **Output:** Số lượng số nguyên tố trong đoạn $[A, B]$.
* **Sample:** ### Input
```text
10 20
```
### Output
```text
4
```
### Giải thích

Có 4 số nguyên tố: 11, 13, 17, 19.

---

### Bài 12 (P3): Tìm số có đúng 3 ước số
* **Mã bài toán:** `pya_l11_p14_tim_so_co_dung_3_uoc_so`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Xoài mở một câu lạc bộ sưu tầm những viên đá rất kén chọn. Bạn ấy chỉ giữ lại những viên đá mang số $X$ đặc biệt: một số tự nhiên $X$ có đúng 3 ước số nguyên dương khi và chỉ khi $X$ là bình phương của một số nguyên tố ($X = P^2$, ví dụ: $4 = 2^2, 9 = 3^2, 25 = 5^2, 49 = 7^2$). Xoài có cả một hộp đá mà đếm mãi chưa xong, hãy bạn ấy đếm.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy đếm xem có bao nhiêu số nhỏ hơn hoặc bằng $N$ mà có **đúng 3 ước số**.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Số lượng các số có đúng 3 ước số $\le N$.
* **Sample:** ### Input
```text
30
```
### Output
```text
3
```
### Giải thích

Có 3 số là: 4 ($2^2$), 9 ($3^2$), 25 ($5^2$).

---

### Bài 13 (P3): Số siêu nguyên tố
* **Mã bài toán:** `pya_l11_p12_so_sieu_nguyen_to_super_prime`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bi có một chiếc tàu lượn bằng các chữ số rất lạ. Mỗi lần tàu chạy qua, chữ số ở cuối toa lại rơi xuống một cái. Bạn ấy reo lên khi phát hiện có những con số gọi là "Siêu nguyên tố": bản thân nó là số nguyên tố, và khi ta lần lượt xóa bớt chữ số tận cùng bên phải thì các số thu được vẫn luôn là số nguyên tố!
 * Ví dụ: Số $239$ là số nguyên tố.
 * Cắt đuôi 9 còn $23$ (vẫn là số nguyên tố).
 * Cắt đuôi 3 còn $2$ (vẫn là số nguyên tố).
 $\implies 239$ là một Siêu nguyên tố! Bi đố em tìm thêm thật nhiều số đặc biệt như vậy, hãy bạn ấy.
* **Nhiệm vụ:** Cho số tự nhiên $N$. Hãy kiểm tra xem $N$ có phải là Siêu nguyên tố hay không. In `YES` hoặc `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^7$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
239
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `239`, kết quả thu được tương ứng là `YES`.

---

### Bài 14 (P3): Cặp số nguyên tố sinh đôi
* **Mã bài toán:** `pya_l11_p11_cap_so_nguyen_to_sinh_doi`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Hai chị em Song sinh nhà bạn Tí lúc nào cũng ngồi cạnh nhau thật thân thiết. Nghe chuyện đó, cô giáo đố cả lớp tìm những cặp số nguyên tố cũng "sinh đôi" như vậy. Hai số nguyên tố được gọi là "Sinh đôi" nếu chúng hơn kém nhau đúng 2 đơn vị (ví dụ: $(3, 5), (5, 7), (11, 13), (17, 19)$). Cả lớp tìm mãi chưa đủ, hãy các bạn liệt kê.
* **Nhiệm vụ:** Cho số tự nhiên $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các cặp số nguyên tố sinh đôi $(P, P+2)$ sao cho $P+2 \le N$.
* **Input:** Một số nguyên $N$.
* **Output:** Mỗi dòng in một cặp số nguyên tố sinh đôi cách nhau bởi khoảng trắng, theo thứ tự tăng dần.
* **Sample:** ### Input
```text
15
```
### Output
```text
3 5
5 7
11 13
```
### Giải thích

Với dữ liệu đầu vào là `15`, kết quả thu được tương ứng là `3 5
5 7
11 13`.

---
