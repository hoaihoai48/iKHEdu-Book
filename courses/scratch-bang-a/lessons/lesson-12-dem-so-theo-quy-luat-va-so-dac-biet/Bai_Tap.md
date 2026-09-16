# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 12 — ĐẾM SỐ THEO QUY LUẬT VÀ SỐ ĐẶC BIỆT

**Khóa học:** iKHEDU Scratch — Bảng A (Level 1)  
**Chuyên đề:** Chương 4: Số Học & Thuật Toán Tách Số  
> **Tổng số bài tập thực hành:** `12 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_l12_p01_dem_so_chia_het_cho_k` | Đếm số chia hết cho K | **P0** | Khởi động & Quan sát | Cho 2 số nguyên dương $N$ và $K$. Hãy đếm xem trong các số t... |
| 2 | `sca_l12_p02_dem_so_le_trong_doan` | Đếm số lẻ trong đoạn | **P0** | Khởi động & Quan sát | Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^9$).... |
| 3 | `sca_l12_p03_kiem_tra_so_hoan_hao` | Kiểm tra số hoàn hảo | **P0** | Khởi động & Quan sát | Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số hoàn hảo k... |
| 4 | `sca_l12_p04_so_armstrong_ba_chu_so` | Số Armstrong ba chữ số | **P1** | Cơ bản & Hoàn thành | Cho một số có đúng 3 chữ số $N$. Kiểm tra xem $N$ có phải là... |
| 5 | `sca_l12_p05_tim_tat_ca_so_hoan_hao_nho_hon_n` | Tìm tất cả số hoàn hảo nhỏ hơn N | **P1** | Cơ bản & Hoàn thành | Cho số nguyên dương $N$ ($1 \le N \le 10^4$). Hãy in ra tất ... |
| 6 | `sca_l12_p06_dem_boi_cua_3_nhung_khong_chia_het_cho_5` | Đếm bội của 3 nhưng không chia hết cho 5 | **P1** | Cơ bản & Hoàn thành | Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{12}... |
| 7 | `sca_l12_p07_dem_so_chia_het_cho_2_hoac_3` | Đếm số chia hết cho 2 hoặc 3 | **P2** | Luyện tập & Vận dụng | Cho số nguyên dương $N$ ($1 \le N \le 10^{12}$). Hãy đếm xem... |
| 8 | `sca_l12_p08_cap_so_than_thiet` | Cặp số thân thiết | **P2** | Luyện tập & Vận dụng | Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng là c... |
| 9 | `sca_l12_p09_so_phong_phu_abundant_number` | Số phong phú (abundant number) | **P2** | Luyện tập & Vận dụng | Nhập số nguyên dương $N$. Hãy in ra tất cả các số phong phú ... |
| 10 | `sca_l12_p10_dem_so_khong_chua_chu_so_0` | Đếm số không chứa chữ số 0 | **P3** | Vận dụng cao & Sáng tạo | Cho số nguyên dương $N$. Hãy đếm xem từ 1 đến $N$ có bao nhi... |
| 11 | `sca_l12_p11_dem_so_chinh_phuong_trong_doan` | Đếm số chính phương trong đoạn | **P3** | Vận dụng cao & Sáng tạo | Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{14}... |
| 12 | `sca_l12_p12_so_tu_man_narcissistic_number_k_chu_so` | Số tự mãn (Narcissistic number K chữ số) | **P3** | Vận dụng cao & Sáng tạo | Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Hãy kiểm tra x... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): Đếm số chia hết cho K
* **Mã bài toán:** `sca_l12_p01_dem_so_chia_het_cho_k`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Bài toán đếm số phần tử chia hết cho một số nguyên $K$ trong một khoảng số liên tiếp là nền tảng xây dựng các thuật toán tối ưu thời gian $\mathcal{O}(1)$.
* **Nhiệm vụ:** Cho 2 số nguyên dương $N$ và $K$. Hãy đếm xem trong các số từ $1$ đến $N$, có bao nhiêu số chia hết cho $K$.
* **Dữ liệu vào (Input):** Hai số nguyên $N$ và $K$ ($1 \le N, K \le 10^9$) cách nhau bởi khoảng trắng.
* **Kết quả ra (Output):** Một số nguyên duy nhất là số lượng các số chia hết cho $K$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
20 3
```
### Output
```text
6
```
### Giải thích

Có 6 số: 3, 6, 9, 12, 15, 18.

---

### Bài 2 (P0): Đếm số lẻ trong đoạn
* **Mã bài toán:** `sca_l12_p02_dem_so_le_trong_doan`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Trong thống kê dữ liệu liên tục, việc xác định số lượng phần tử lẻ trong một đoạn đóng vai trò kiểm tra tính phân bố đều của tập số liệu.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^9$). Hãy đếm xem có bao nhiêu số lẻ nằm trong đoạn từ $A$ đến $B$ (tính cả $A$ và $B$).
* **Dữ liệu vào (Input):** Hai số $A, B$ trên cùng một dòng.
* **Kết quả ra (Output):** Số lượng số lẻ.
* **Dữ liệu mẫu (Sample):**

### Input
```text
3 8
```
### Output
```text
3
```
### Giải thích

Có 3 số lẻ là: 3, 5, 7.

---

### Bài 3 (P0): Kiểm tra số hoàn hảo
* **Mã bài toán:** `sca_l12_p03_kiem_tra_so_hoan_hao`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Bạn Mèo chia những chiếc kẹo cho các bạn búp bê của mình. Có hôm bạn ấy ngạc nhiên vì số kẹo chia ra vừa khít, không thừa chiếc nào. Cô giáo bảo đó chính là "Số hoàn hảo": một số nguyên dương $N$ được gọi là "Số hoàn hảo" nếu tổng tất cả các ước số nguyên dương nhỏ hơn $N$ bằng chính số $N$. Mèo có nhiều gói kẹo mà kiểm tra mãi chưa hết, hãy bạn ấy.
* **Nhiệm vụ:** Nhập số nguyên dương $N$. Kiểm tra $N$ có phải số hoàn hảo không. In `YES` nếu đúng, ngược lại in `NO`.
* **Dữ liệu vào (Input):** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Kết quả ra (Output):** `YES` hoặc `NO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
6
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `6`, kết quả thu được tương ứng là `YES`.

---

### Bài 4 (P1): Số Armstrong ba chữ số
* **Mã bài toán:** `sca_l12_p04_so_armstrong_ba_chu_so`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Bạn Tôm tìm thấy một chiếc hộp phép thuật có khóa bằng số. Trên hộp ghi rằng chỉ những số Armstrong mới mở được khóa. Số Armstrong có 3 chữ số là số tự nhiên có dạng $\overline{abc}$ thỏa mãn $a^3 + b^3 + c^3 = \overline{abc}$. Tôm thử mãi chưa mở được hộp, hãy bạn ấy kiểm tra.
* **Nhiệm vụ:** Cho một số có đúng 3 chữ số $N$. Kiểm tra xem $N$ có phải là số Armstrong không. In `YES` hoặc `NO`.
* **Dữ liệu vào (Input):** Một số nguyên $N$ ($100 \le N \le 999$).
* **Kết quả ra (Output):** `YES` hoặc `NO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
153
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `153`, kết quả thu được tương ứng là `YES`.

---

### Bài 5 (P1): Tìm tất cả số hoàn hảo nhỏ hơn N
* **Mã bài toán:** `sca_l12_p05_tim_tat_ca_so_hoan_hao_nho_hon_n`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho số nguyên dương $N$ ($1 \le N \le 10^4$). Hãy in ra tất cả các số hoàn hảo nhỏ hơn hoặc bằng $N$ theo thứ tự tăng dần.
* **Dữ liệu vào (Input):** Một số nguyên $N$.
* **Kết quả ra (Output):** Các số hoàn hảo, cách nhau bởi khoảng trắng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
30
```
### Output
```text
6 28
```
### Giải thích

Với dữ liệu đầu vào là `30`, kết quả thu được tương ứng là `6 28`.

---

### Bài 6 (P1): Đếm bội của 3 nhưng không chia hết cho 5
* **Mã bài toán:** `sca_l12_p06_dem_boi_cua_3_nhung_khong_chia_het_cho_5`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Trong lý thuyết tập hợp, bài toán xác định các phần tử thuộc tập này nhưng không thuộc tập khác đòi hỏi kỹ thuật trừ tập hợp chính xác để tránh đếm lặp.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{12}$). Hãy đếm xem trong đoạn từ $A$ đến $B$ có bao nhiêu số chia hết cho 3 nhưng **không chia hết cho 5**.
* **Dữ liệu vào (Input):** Hai số $A$ và $B$ cách nhau bởi khoảng trắng.
* **Kết quả ra (Output):** Số lượng số thỏa mãn.
* **Dữ liệu mẫu (Sample):**

### Input
```text
1 30
```
### Output
```text
8
```
### Giải thích

Với dữ liệu đầu vào là `1 30`, kết quả thu được tương ứng là `8`.

---

### Bài 7 (P2): Đếm số chia hết cho 2 hoặc 3
* **Mã bài toán:** `sca_l12_p07_dem_so_chia_het_cho_2_hoac_3`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Bài toán đếm số lượng phần tử thỏa mãn ít nhất một trong hai điều kiện chia hết là bài toán mẫu mực áp dụng Nguyên lý Bao hàm – Loại trừ (Inclusion-Exclusion).
* **Nhiệm vụ:** Cho số nguyên dương $N$ ($1 \le N \le 10^{12}$). Hãy đếm xem từ 1 đến $N$ có bao nhiêu số chia hết cho 2 hoặc chia hết cho 3.
* **Dữ liệu vào (Input):** Một số nguyên $N$.
* **Kết quả ra (Output):** Số lượng số thỏa mãn.
* **Dữ liệu mẫu (Sample):**

### Input
```text
10
```
### Output
```text
7
```
### Giải thích

Các số là: 2, 3, 4, 6, 8, 9, 10 (có 7 số).

---

### Bài 8 (P2): Cặp số thân thiết
* **Mã bài toán:** `sca_l12_p08_cap_so_than_thiet`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Hai bạn thân Nấm và Mít chơi trò chia kẹo công bằng cho nhau. Cô giáo kể rằng trong thế giới các con số cũng có những đôi bạn như vậy. Hai số $A$ và $B$ ($A \ne B$) được gọi là "Cặp số thân thiết" nếu tổng các ước số nhỏ hơn $A$ bằng $B$, và tổng các ước số nhỏ hơn $B$ bằng $A$. Hai bạn tìm mãi chưa ra các cặp số thân nhau, hãy hai bạn kiểm tra.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$. In ra `YES` nếu chúng là cặp số thân thiết, ngược lại in `NO`.
* **Dữ liệu vào (Input):** Hai số $A, B$ ($1 \le A, B \le 10^5$).
* **Kết quả ra (Output):** `YES` hoặc `NO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
220 284
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `220 284`, kết quả thu được tương ứng là `YES`.

---

### Bài 9 (P2): Số phong phú (abundant number)
* **Mã bài toán:** `sca_l12_p09_so_phong_phu_abundant_number`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Bạn Ổi có một giỏ đầy những quả ngọt để chia cho bạn bè. Có những con số cũng "rộng rãi" giống như giỏ quả của Ổi vậy. Một số tự nhiên được gọi là "Số phong phú" nếu tổng các ước số nhỏ hơn nó lớn hơn chính nó (ví dụ: số 12 có tổng các ước nhỏ hơn nó là $1+2+3+4+6=16 > 12$). Ổi muốn tìm thật nhiều con số rộng rãi như thế, hãy bạn ấy.
* **Nhiệm vụ:** Nhập số nguyên dương $N$. Hãy in ra tất cả các số phong phú nhỏ hơn hoặc bằng $N$.
* **Dữ liệu vào (Input):** Số nguyên $N$ ($1 \le N \le 10^4$).
* **Kết quả ra (Output):** Dãy các số phong phú tăng dần trên một dòng.
* **Dữ liệu mẫu (Sample):**

### Input
```text
20
```
### Output
```text
12 18 20
```
### Giải thích

Với dữ liệu đầu vào là `20`, kết quả thu được tương ứng là `12 18 20`.

---

### Bài 10 (P3): Đếm số không chứa chữ số 0
* **Mã bài toán:** `sca_l12_p10_dem_so_khong_chua_chu_so_0`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Trong thiết kế hệ thống hiển thị số không hỗ trợ ký tự 0, các số chỉ tạo bởi các chữ số từ 1 đến 9 được coi là số hợp lệ cần được thống kê chính xác.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy đếm xem từ 1 đến $N$ có bao nhiêu số mà trong cách ghi thập phân của nó **không chứa bất kỳ chữ số 0 nào**.
* **Dữ liệu vào (Input):** Một số nguyên $N$ ($1 \le N \le 10^6$).
* **Kết quả ra (Output):** Số lượng số thỏa mãn.
* **Dữ liệu mẫu (Sample):**

### Input
```text
15
```
### Output
```text
14
```
### Giải thích

Từ 1 đến 15 chỉ có duy nhất số 10 chứa chữ số 0. Vậy có $15 - 1 = 14$ số.

---

### Bài 11 (P3): Đếm số chính phương trong đoạn
* **Mã bài toán:** `sca_l12_p11_dem_so_chinh_phuong_trong_doan`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Xác định số lượng số chính phương trong một phạm vi lớn là bài toán tối ưu quan trọng, yêu cầu chuyển đổi từ duyệt từng phần tử sang phương pháp tính giải tích bằng căn bậc hai.
* **Nhiệm vụ:** Cho 2 số nguyên dương $A$ và $B$ ($1 \le A \le B \le 10^{14}$). Hãy đếm xem có bao nhiêu số chính phương nằm trong đoạn từ $A$ đến $B$.
* **Dữ liệu vào (Input):** Hai số nguyên $A, B$ trên cùng một dòng.
* **Kết quả ra (Output):** Số lượng số chính phương trong đoạn $[A, B]$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
5 25
```
### Output
```text
3
```
### Giải thích

Có 3 số chính phương là 9, 16, 25.

---

### Bài 12 (P3): Số tự mãn (Narcissistic number K chữ số)
* **Mã bài toán:** `sca_l12_p12_so_tu_man_narcissistic_number_k_chu_so`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Bạn Kiến rất tự hào vì mỗi bạn kiến trong đàn đều góp sức làm nên tổ lớn. Bạn ấy nghe cô kể về những con số cũng "tự hào" như vậy. Một số tự nhiên $N$ có $K$ chữ số được gọi là "Số tự mãn" (Narcissistic number) nếu tổng lũy thừa bậc $K$ của các chữ số của nó đúng bằng chính số $N$.
 Ví dụ:
 * $N = 153$ có 3 chữ số: $1^3 + 5^3 + 3^3 = 153$ $\implies$ Thỏa mãn.
 * $N = 1634$ có 4 chữ số: $1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634$ $\implies$ Thỏa mãn. Kiến đố em tìm thêm những con số đặc biệt này, hãy bạn ấy.
* **Nhiệm vụ:** Cho số nguyên dương $N$ ($1 \le N \le 10^9$). Hãy kiểm tra xem $N$ có phải là số tự mãn không. In `YES` nếu đúng, ngược lại in `NO`.
* **Dữ liệu vào (Input):** Một số nguyên $N$.
* **Kết quả ra (Output):** `YES` hoặc `NO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
1634
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `1634`, kết quả thu được tương ứng là `YES`.

---
