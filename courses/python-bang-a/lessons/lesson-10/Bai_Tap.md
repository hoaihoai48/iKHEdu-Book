# Danh Sách Bài Tập Thực Hành: Bài 10: Đếm số theo quy luật và số đặc biệt

> Nguồn problems: l12 | Tổng 12 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-3
* P1 (Cơ bản): Bài 4-6
* P2 (Luyện tập): Bài 7-9
* P3 (Vận dụng): Bài 10-12
---

### Bài 1 (P0): Đếm số chia hết cho K
* **Mã bài toán:** `pya_l12_p01_dem_so_chia_het_cho_k`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Bài toán đếm số phần tử chia hết cho một số nguyên $K$ trong một khoảng số liên tiếp là nền tảng xây dựng các thuật toán tối ưu thời gian $\mathcal{O}(1)$.
* **Nhiệm vụ:** Cho 2 số nguyên dương $N$ và $K$. Hãy đếm xem trong các số từ $1$ đến $N$, có bao nhiêu số chia hết cho $K$.
* **Input:** Hai số nguyên $N$ và $K$ ($1 \le N, K \le 10^9$) cách nhau bởi khoảng trắng.
* **Output:** Một số nguyên duy nhất là số lượng các số chia hết cho $K$.
* **Sample:** ### Input
```text
20 3
```
### Output
```text
6
```
### Giải thích

Có 6 số: 3, 6, 9, 12, 15, 18.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 2 (P0): Đếm số chia hết cho 2 hoặc 3
* **Mã bài toán:** `pya_l12_p07_dem_so_chia_het_cho_2_hoac_3`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Bài toán đếm số lượng phần tử thỏa mãn ít nhất một trong hai điều kiện chia hết là bài toán mẫu mực áp dụng Nguyên lý Bao hàm – Loại trừ (Inclusion-Exclusion).
* **Nhiệm vụ:** Cho số nguyên dương $N$ ($1 \le N \le 10^{12}$). Hãy đếm xem từ 1 đến $N$ có bao nhiêu số chia hết cho 2 hoặc chia hết cho 3.
* **Input:** Một số nguyên $N$.
* **Output:** Số lượng số thỏa mãn.
* **Sample:** ### Input
```text
10
```
### Output
```text
7
```
### Giải thích

Các số là: 2, 3, 4, 6, 8, 9, 10 (có 7 số).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 3 (P0): Đếm số lẻ trong đoạn
* **Mã bài toán:** `pya_l12_p02_dem_so_le_trong_doan`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong thống kê dữ liệu liên tục, việc xác định số lượng phần tử lẻ trong một đoạn đóng vai trò kiểm tra tính phân bố đều của tập số liệu.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^9$). Hãy đếm xem có bao nhiêu số lẻ nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Input:** Hai số $A, B$ trên cùng một dòng.
* **Output:** Số lượng số lẻ.
* **Sample:** ### Input
```text
3 8
```
### Output
```text
3
```
### Giải thích

Có 3 số lẻ là: 3, 5, 7.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 4 (P1): Đếm bội của 3 nhưng không chia hết cho 5
* **Mã bài toán:** `pya_l12_p06_dem_boi_cua_3_nhung_khong_chia_het_cho_5`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong lý thuyết tập hợp, bài toán xác định các phần tử thuộc tập này nhưng không thuộc tập khác đòi hỏi kỹ thuật trừ tập hợp chính xác để tránh đếm lặp.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{12}$). Hãy đếm xem trong đoạn từ $A$ đến $B$ có bao nhiêu số chia hết cho 3 nhưng **không chia hết cho 5**.
* **Input:** Hai số $A$ và $B$ cách nhau bởi khoảng trắng.
* **Output:** Số lượng số thỏa mãn.
* **Sample:** ### Input
```text
1 30
```
### Output
```text
8
```
### Giải thích

Với dữ liệu đầu vào là `1 30`, kết quả thu được tương ứng là `8`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 5 (P1): Số Armstrong ba chữ số
* **Mã bài toán:** `pya_l12_p04_so_armstrong_ba_chu_so`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Bạn Tôm tìm thấy một chiếc hộp phép thuật có khóa bằng số. Trên hộp ghi rằng chỉ những số Armstrong mới mở được khóa. Số Armstrong có 3 chữ số là số tự nhiên có dạng $\overline{abc}$ thỏa mãn $a^3 + b^3 + c^3 = \overline{abc}$. Tôm thử mãi chưa mở được hộp, hãy bạn ấy kiểm tra.
* **Nhiệm vụ:** Cho một số có đúng 3 chữ số $N$. Kiểm tra xem $N$ có phải là số Armstrong không. In `YES` hoặc `NO`.
* **Input:** Một số nguyên $N$ ($100 \le N \le 999$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
153
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `153`, kết quả thu được tương ứng là `YES`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 6 (P1): Số tự mãn (Narcissistic number K chữ số)
* **Mã bài toán:** `pya_l12_p12_so_tu_man_narcissistic_number_k_chu_so`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Bạn Kiến rất tự hào vì mỗi bạn kiến trong đàn đều góp sức làm nên tổ lớn. Bạn ấy nghe cô kể về những con số cũng "tự hào" như vậy. Một số tự nhiên $N$ có $K$ chữ số được gọi là "Số tự mãn" nếu tổng lũy thừa bậc $K$ của các chữ số của nó đúng bằng chính số $N$.
 Ví dụ:
 * $N = 153$ có 3 chữ số: $1^3 + 5^3 + 3^3 = 153$ $\implies$ Thỏa mãn.
 * $N = 1634$ có 4 chữ số: $1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$ $\implies$ Thỏa mãn. Kiến đố em tìm thêm những con số đặc biệt này, hãy bạn ấy.
* **Nhiệm vụ:** Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Hãy kiểm tra xem $N$ có phải là số tự mãn không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số nguyên $N$.
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
1634
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `1634`, kết quả thu được tương ứng là `YES`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 7 (P2): Đếm số không chứa chữ số 0
* **Mã bài toán:** `pya_l12_p10_dem_so_khong_chua_chu_so_0`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Trong thiết kế hệ thống hiển thị số không hỗ trợ ký tự 0, các số chỉ tạo bởi các chữ số từ 1 đến 9 được coi là số hợp lệ cần được thống kê chính xác.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy đếm xem từ 1 đến $N$ có bao nhiêu số mà trong cách ghi thập phân của nó **không chứa bất kỳ chữ số 0 nào**.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** Số lượng số thỏa mãn.
* **Sample:** ### Input
```text
15
```
### Output
```text
14
```
### Giải thích

Từ 1 đến 15 chỉ có duy nhất số 10 chứa chữ số 0. Vậy có $15 - 1 = 14$ số.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 8 (P2): Kiểm tra số hoàn hảo
* **Mã bài toán:** `pya_l12_p03_kiem_tra_so_hoan_hao`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bạn Mèo chia những chiếc kẹo cho các bạn búp bê của mình. Có hôm bạn ấy ngạc nhiên vì số kẹo chia ra vừa khít, không thừa chiếc nào. Cô giáo bảo đó chính là "Số hoàn hảo": một số nguyên dương $N$ được gọi là "Số hoàn hảo" nếu tổng tất cả các ước số nguyên dương nhỏ hơn $N$ bằng chính số $N$. Mèo có nhiều gói kẹo mà kiểm tra mãi chưa hết, hãy bạn ấy.
* **Nhiệm vụ:** Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số hoàn hảo không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
6
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `6`, kết quả thu được tương ứng là `YES`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 9 (P2): Đếm số chính phương trong đoạn
* **Mã bài toán:** `pya_l12_p11_dem_so_chinh_phuong_trong_doan`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Xác định số lượng số chính phương trong một phạm vi lớn là bài toán tối ưu quan trọng, yêu cầu chuyển đổi từ duyệt từng phần tử sang phương pháp tính giải tích bằng căn bậc hai.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{14}$). Hãy đếm xem có bao nhiêu số chính phương nằm trong đoạn từ $A$ đến $B$.
* **Input:** Hai số nguyên $A, B$ trên cùng một dòng.
* **Output:** Số lượng số chính phương trong đoạn $[A, B]$.
* **Sample:** ### Input
```text
5 25
```
### Output
```text
3
```
### Giải thích

Có 3 số chính phương là 9, 16, 25.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 10 (P3): Tìm tất cả số hoàn hảo nhỏ hơn N
* **Mã bài toán:** `pya_l12_p05_tim_tat_ca_so_hoan_hao_nho_hon_n`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho số nguyên dương $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các số hoàn hảo nhỏ hơn hoặc bằng $N$ theo thứ tự tăng dần.
* **Input:** Một số nguyên $N$.
* **Output:** Các số hoàn hảo, cách nhau bởi khoảng trắng.
* **Sample:** ### Input
```text
30
```
### Output
```text
6 28
```
### Giải thích

Với dữ liệu đầu vào là `30`, kết quả thu được tương ứng là `6 28`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 11 (P3): Số phong phú
* **Mã bài toán:** `pya_l12_p09_so_phong_phu_abundant_number`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Ổi có một giỏ đầy những quả ngọt để chia cho bạn bè. Có những con số cũng "rộng rãi" giống như giỏ quả của Ổi vậy. Một số tự nhiên được gọi là "Số phong phú" nếu tổng các ước số nhỏ hơn nó lớn hơn chính nó (ví dụ: số 12 có tổng các ước nhỏ hơn nó là $1+2+3+4+6=16 > 12$). Ổi muốn tìm thật nhiều con số rộng rãi như thế, hãy bạn ấy.
* **Nhiệm vụ:** Nhập số nguyên dương $N$. Hãy in ra tất cả các số phong phú nhỏ hơn hoặc bằng $N$.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^4$).
* **Output:** Dãy các số phong phú tăng dần trên một dòng.
* **Sample:** ### Input
```text
20
```
### Output
```text
12 18 20
```
### Giải thích

Với dữ liệu đầu vào là `20`, kết quả thu được tương ứng là `12 18 20`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 12 (P3): Cặp số thân thiết
* **Mã bài toán:** `pya_l12_p08_cap_so_than_thiet`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Hai bạn thân Nấm và Mít chơi trò chia kẹo công bằng cho nhau. Cô giáo kể rằng trong thế giới các con số cũng có những đôi bạn như vậy. Hai số $A$ và $B$ ($A \ne B$) được gọi là "Cặp số thân thiết" nếu tổng các ước số nhỏ hơn $A$ bằng $B$, và tổng các ước số nhỏ hơn $B$ bằng $A$. Hai bạn tìm mãi chưa ra các cặp số thân nhau, hãy hai bạn kiểm tra.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng là cặp số thân thiết, ngược lại in `NO`.
* **Input:** Hai số $A, B$ ($1 \le A, B \le 10^5$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
220 284
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `220 284`, kết quả thu được tương ứng là `YES`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---
