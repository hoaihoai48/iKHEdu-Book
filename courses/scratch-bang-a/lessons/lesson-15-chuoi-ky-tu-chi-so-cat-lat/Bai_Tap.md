# DANH SÁCH BÀI TẬP THỰC HÀNH: BÀI 15 — CHUỖI KÝ TỰ, CHỈ SỐ VÀ TRÍCH XUẤT

**Khóa học:** iKHEDU Scratch — Bảng A (Level 1)  
**Chuyên đề:** Chương 6: Xử Lý Chuỗi Ký Tự  
> **Tổng số bài tập thực hành:** `12 bài` chuẩn hóa 100% (Từ kho bài tập `courses/scratch-bang-a/problems/`).  

---

## 1. Ma Trận Phân Tầng Bài Tập Toàn Diện

| STT | Mã bài toán | Tên bài tập | Phân tầng | Mức nhận thức | Thao tác trọng tâm |
|:---:|---|---|:---:|:---:|---|
| 1 | `sca_l15_p01_ky_tu_dau_ky_tu_cuoi` | Ký tự đầu & ký tự cuối | **P0** | Khởi động & Quan sát | Nhập vào một chuỗi ký tự $S$ không chứa dấu cách. Hãy in ra ... |
| 2 | `sca_l15_p02_do_dai_cua_chuoi` | Độ dài của chuỗi | **P0** | Khởi động & Quan sát | Nhập một dòng văn bản $S$ từ bàn phím. Hãy đếm và in ra xem ... |
| 3 | `sca_l15_p03_cat_ba_ky_tu_dau_tien` | Cắt ba ký tự đầu tiên | **P0** | Khởi động & Quan sát | Nhập vào một chuỗi $S$ có ít nhất 3 ký tự. Hãy in ra 3 ký tự... |
| 4 | `sca_l15_p04_dao_nguoc_ten_rieng` | Đảo ngược tên riêng | **P1** | Cơ bản & Hoàn thành | Nhập một chuỗi ký tự $S$. Hãy in ra chuỗi đảo ngược của $S$. |
| 5 | `sca_l15_p05_kiem_tra_tu_doi_xung_palindrome` | Kiểm tra từ đối xứng (palindrome) | **P1** | Cơ bản & Hoàn thành | Cho một từ $S$. Kiểm tra xem $S$ có phải từ đối xứng không. ... |
| 6 | `sca_l15_p06_cat_doi_chuoi_ky_tu` | Cắt đôi chuỗi ký tự | **P1** | Cơ bản & Hoàn thành | Cho một chuỗi $S$ có độ dài chẵn. Hãy chia chuỗi $S$ thành 2... |
| 7 | `sca_l15_p07_rut_trich_ten_mien_email` | Rút trích tên miền email | **P2** | Luyện tập & Vận dụng | Cho một địa chỉ email hợp lệ. Hãy in ra phần tên miền của đị... |
| 8 | `sca_l15_p08_ky_tu_o_vi_tri_chan` | Ký tự Ở vị trí chẵn | **P2** | Luyện tập & Vận dụng | Cho một chuỗi $S$. Hãy tạo ra một chuỗi mới chỉ gồm các ký t... |
| 9 | `sca_l15_p09_hoan_doi_nua_dau_nua_sau` | Hoán đổi nửa đầu nửa sau | **P2** | Luyện tập & Vận dụng | Cho chuỗi ký tự $S$ có độ dài chẵn $2N$. Hãy hoán đổi vị trí... |
| 10 | `sca_l15_p10_xoa_ky_tu_o_vi_tri_k` | Xóa ký tự ở vị trí K | **P3** | Vận dụng cao & Sáng tạo | Cho chuỗi $S$ và chỉ số nguyên $K$ ($0 \le K < |S|$). Hãy xó... |
| 11 | `sca_l15_p11_dich_chuyen_vong_quanh_left_rotation` | Dịch chuyển vòng quanh (left rotation) | **P3** | Vận dụng cao & Sáng tạo | Cho chuỗi $S$ và số nguyên $K$ ($1 \le K \le |S| \le 10^5$).... |
| 12 | `sca_l15_p12_chuoi_con_doi_xung_dai_nhat` | Chuỗi con đối xứng dài nhất | **P3** | Vận dụng cao & Sáng tạo | Cho một chuỗi ký tự $S$. Hãy tìm độ dài của chuỗi con liên t... |

---

## 2. Chi Tiết Từng Bài Tập Thực Hành

### Bài 1 (P0): Ký tự đầu & ký tự cuối
* **Mã bài toán:** `sca_l15_p01_ky_tu_dau_ky_tu_cuoi`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Trong xử lý văn bản, việc trích xuất ký tự mở đầu và kết thúc của một từ mã giúp hệ thống nhanh chóng kiểm tra định dạng khung truyền tin.
* **Nhiệm vụ:** Nhập vào một chuỗi ký tự $S$ không chứa dấu cách. Hãy in ra ký tự đầu tiên và ký tự cuối cùng của chuỗi $S$, cách nhau bởi một dấu cách.
* **Dữ liệu vào (Input):** Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).
* **Kết quả ra (Output):** Ký tự đầu và ký tự cuối.
* **Dữ liệu mẫu (Sample):**

### Input
```text
PYTHON
```
### Output
```text
P N
```
### Giải thích

Với dữ liệu đầu vào là `PYTHON`, kết quả thu được tương ứng là `P N`.

---

### Bài 2 (P0): Độ dài của chuỗi
* **Mã bài toán:** `sca_l15_p02_do_dai_cua_chuoi`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Độ dài chuỗi ký tự là thông số cơ bản nhất để kiểm soát giới hạn bộ đệm và tính hợp lệ của dữ liệu chuỗi đầu vào.
* **Nhiệm vụ:** Nhập một dòng văn bản $S$ từ bàn phím. Hãy đếm và in ra xem chuỗi $S$ có bao nhiêu ký tự (tính cả các ký tự khoảng trắng nếu có).
* **Dữ liệu vào (Input):** Một chuỗi ký tự $S$.
* **Kết quả ra (Output):** Một số nguyên là độ dài chuỗi.
* **Dữ liệu mẫu (Sample):**

### Input
```text
Python
```
### Output
```text
6
```
### Giải thích

Với dữ liệu đầu vào là `Python`, kết quả thu được tương ứng là `6`.

---

### Bài 3 (P0): Cắt ba ký tự đầu tiên
* **Mã bài toán:** `sca_l15_p03_cat_ba_ky_tu_dau_tien`
* **Độ khó & Phân tầng:** P0 (Khởi động & Quan sát)
* **Bối cảnh:** Trong các hệ thống phân loại mã bưu chính hoặc mã vùng, ba ký tự đầu tiên thường đại diện cho mã quốc gia hoặc mã tiền tố phân luồng.
* **Nhiệm vụ:** Nhập vào một chuỗi $S$ có ít nhất 3 ký tự. Hãy in ra 3 ký tự đầu tiên của chuỗi đó.
* **Dữ liệu vào (Input):** Một chuỗi $S$ ($3 \le |S| \le 100$).
* **Kết quả ra (Output):** 3 ký tự đầu tiên.
* **Dữ liệu mẫu (Sample):**

### Input
```text
VIETNAM
```
### Output
```text
VIE
```
### Giải thích

Với dữ liệu đầu vào là `VIETNAM`, kết quả thu được tương ứng là `VIE`.

---

### Bài 4 (P1): Đảo ngược tên riêng
* **Mã bài toán:** `sca_l15_p04_dao_nguoc_ten_rieng`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Bạn Bo có một cuốn sổ để viết tên của mình và các bạn trong lớp. Một hôm, Bo nghĩ ra trò đọc ngược tên để tạo biệt danh bí mật cho vui. Cả lớp cười vang khi nghe tên mình bị đọc ngược lại thật ngộ nghĩnh. Hãy viết chương trình đọc ngược mọi cái tên.
* **Nhiệm vụ:** Nhập một chuỗi ký tự $S$. Hãy in ra chuỗi đảo ngược của $S$.
* **Dữ liệu vào (Input):** Một chuỗi ký tự $S$.
* **Kết quả ra (Output):** Chuỗi $S$ sau khi đảo ngược.
* **Dữ liệu mẫu (Sample):**

### Input
```text
DORAEMON
```
### Output
```text
NOMEAROD
```
### Giải thích

Với dữ liệu đầu vào là `DORAEMON`, kết quả thu được tương ứng là `NOMEAROD`.

---

### Bài 5 (P1): Kiểm tra từ đối xứng (palindrome)
* **Mã bài toán:** `sca_l15_p05_kiem_tra_tu_doi_xung_palindrome`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Trong giờ ra chơi, bạn Na rủ cả lớp chơi trò soi gương với các con chữ. Na phát hiện một từ được gọi là từ đối xứng nếu đọc xuôi hay đọc ngược đều hoàn toàn giống nhau (ví dụ: `radar`, `level`, `madam`, `noon`). Cả lớp thi nhau tìm thêm thật nhiều từ ngộ nghĩnh như vậy. Hãy viết chương trình kiểm tra xem một từ có đối xứng hay không.
* **Nhiệm vụ:** Cho một từ $S$. Kiểm tra xem $S$ có phải từ đối xứng không. In `YES` nếu đúng, ngược lại in `NO`.
* **Dữ liệu vào (Input):** Một chuỗi $S$ viết liền ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** `YES` hoặc `NO`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
RADAR
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `RADAR`, kết quả thu được tương ứng là `YES`.

---

### Bài 6 (P1): Cắt đôi chuỗi ký tự
* **Mã bài toán:** `sca_l15_p06_cat_doi_chuoi_ky_tu`
* **Độ khó & Phân tầng:** P1 (Cơ bản & Hoàn thành)
* **Bối cảnh:** Kỹ thuật chia đôi văn bản là bước khởi đầu trong nhiều thuật toán nén dữ liệu và mã hóa hai nửa đối xứng.
* **Nhiệm vụ:** Cho một chuỗi $S$ có độ dài chẵn. Hãy chia chuỗi $S$ thành 2 nửa bằng nhau và in mỗi nửa trên một dòng.
* **Dữ liệu vào (Input):** Một chuỗi $S$ có độ dài chẵn ($2 \le |S| \le 1000$).
* **Kết quả ra (Output):** Dòng 1 in nửa đầu, dòng 2 in nửa sau.
* **Dữ liệu mẫu (Sample):**

### Input
```text
PYTHON
```
### Output
```text
PYT
HON
```
### Giải thích

Với dữ liệu đầu vào là `PYTHON`, kết quả thu được tương ứng là `PYT
HON`.

---

### Bài 7 (P2): Rút trích tên miền email
* **Mã bài toán:** `sca_l15_p07_rut_trich_ten_mien_email`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Cô giáo dạy Tin học viết lên bảng một địa chỉ thư điện tử dạng `tentaikhoan@domain.com` để cả lớp cùng xem. Cô đố cả lớp phần đứng sau ký tự `@` được gọi là tên miền (domain). Bạn nào tìm đúng tên miền sẽ được một sticker ngôi sao. Hãy giúp cả lớp viết chương trình tìm tên miền thật nhanh.
* **Nhiệm vụ:** Cho một địa chỉ email hợp lệ. Hãy in ra phần tên miền của địa chỉ đó.
* **Dữ liệu vào (Input):** Một chuỗi email chứa đúng 1 ký tự `@`.
* **Kết quả ra (Output):** Phần tên miền đứng sau `@`.
* **Dữ liệu mẫu (Sample):**

### Input
```text
hocsinh@ikhedu.vn
```
### Output
```text
ikhedu.vn
```
### Giải thích

Với dữ liệu đầu vào là `hocsinh@ikhedu.vn`, kết quả thu được tương ứng là `ikhedu.vn`.

---

### Bài 8 (P2): Ký tự Ở vị trí chẵn
* **Mã bài toán:** `sca_l15_p08_ky_tu_o_vi_tri_chan`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Trích xuất các ký tự tại các vị trí chỉ số chẵn là phương pháp lấy mẫu tín hiệu rời rạc phổ biến trong xử lý chuỗi văn bản.
* **Nhiệm vụ:** Cho một chuỗi $S$. Hãy tạo ra một chuỗi mới chỉ gồm các ký tự nằm ở **chỉ số index chẵn** ($0, 2, 4, 6 \dots$) của chuỗi $S$.
* **Dữ liệu vào (Input):** Một chuỗi ký tự $S$ ($1 \le |S| \le 1000$).
* **Kết quả ra (Output):** Chuỗi mới thu được.
* **Dữ liệu mẫu (Sample):**

### Input
```text
ABCDEF
```
### Output
```text
ACE
```
### Giải thích

Lấy các vị trí 0 ('A'), 2 ('C'), 4 ('E').

---

### Bài 9 (P2): Hoán đổi nửa đầu nửa sau
* **Mã bài toán:** `sca_l15_p09_hoan_doi_nua_dau_nua_sau`
* **Độ khó & Phân tầng:** P2 (Luyện tập & Vận dụng)
* **Bối cảnh:** Phép tráo đổi hai nửa của một chuỗi dữ liệu có độ dài chẵn thường được ứng dụng trong các giao thức hoán vị thông tin cơ bản.
* **Nhiệm vụ:** Cho chuỗi ký tự $S$ có độ dài chẵn $2N$. Hãy hoán đổi vị trí của nửa đầu chuỗi và nửa sau chuỗi với nhau.
* **Dữ liệu vào (Input):** Một chuỗi $S$ có độ dài chẵn ($2 \le |S| \le 10^5$).
* **Kết quả ra (Output):** Chuỗi sau khi hoán đổi 2 nửa.
* **Dữ liệu mẫu (Sample):**

### Input
```text
ABCDEF
```
### Output
```text
DEFABC
```
### Giải thích

Với dữ liệu đầu vào là `ABCDEF`, kết quả thu được tương ứng là `DEFABC`.

---

### Bài 10 (P3): Xóa ký tự ở vị trí K
* **Mã bài toán:** `sca_l15_p10_xoa_ky_tu_o_vi_tri_k`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Bạn Tí viết tên mình lên bảng rồi lỡ viết thừa một chữ cái ở giữa. Tí nhớ rằng chuỗi trong Python là bất biến (không thể dùng lệnh xóa trực tiếp `del s[k]`). Vì vậy Tí phải dùng kỹ thuật cắt lát ghép chuỗi để bỏ chữ thừa đi. Hãy giúp Tí viết chương trình xóa chữ thừa thật gọn.
* **Nhiệm vụ:** Cho chuỗi $S$ và chỉ số nguyên $K$ ($0 \le K < |S|$). Hãy xóa ký tự tại vị trí $K$ và in ra chuỗi còn lại.
* **Dữ liệu vào (Input):** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số nguyên $K$.
* **Kết quả ra (Output):** Chuỗi sau khi xóa ký tự thứ $K$.
* **Dữ liệu mẫu (Sample):**

### Input
```text
PYTHON
2
```
### Output
```text
PYHON
```
### Giải thích

Xóa ký tự tại index 2 là chữ 'T'.

---

### Bài 11 (P3): Dịch chuyển vòng quanh (left rotation)
* **Mã bài toán:** `sca_l15_p11_dich_chuyen_vong_quanh_left_rotation`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Trong trò chơi xếp chữ, bạn Bi rủ cả lớp chơi trò tàu lửa nối đuôi nhau. Phép dịch trái chuỗi $K$ vị trí là thao tác nhấc $K$ ký tự đầu tiên của chuỗi đem gắn ra phía sau cùng.
 Ví dụ: Chuỗi `ABCDE` dịch trái 2 ký tự sẽ thành `CDEAB`.
Cả lớp reo lên vì đoàn tàu chữ chạy vòng quanh thật vui. Hãy giúp bạn Bi viết chương trình chạy đoàn tàu chữ này.
* **Nhiệm vụ:** Cho chuỗi $S$ và số nguyên $K$ ($1 \le K \le |S| \le 10^5$). Hãy in ra chuỗi $S$ sau khi dịch trái $K$ vị trí.
* **Dữ liệu vào (Input):** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.
* **Kết quả ra (Output):** Chuỗi sau khi dịch.
* **Dữ liệu mẫu (Sample):**

### Input
```text
ABCDE
2
```
### Output
```text
CDEAB
```
### Giải thích

Với dữ liệu đầu vào là `ABCDE
2`, kết quả thu được tương ứng là `CDEAB`.

---

### Bài 12 (P3): Chuỗi con đối xứng dài nhất
* **Mã bài toán:** `sca_l15_p12_chuoi_con_doi_xung_dai_nhat`
* **Độ khó & Phân tầng:** P3 (Vận dụng cao & Sáng tạo)
* **Bối cảnh:** Bạn Mít có một vòng hạt với nhiều chữ cái xinh xắn xâu liền nhau. Cô giáo nói một chuỗi con là một đoạn các ký tự liên tiếp nhau của chuỗi ban đầu. Mít muốn tìm đoạn hạt đọc xuôi ngược giống nhau mà dài nhất để làm mặt dây chuyền. Hãy giúp bạn Mít tìm đoạn hạt đặc biệt đó.
* **Nhiệm vụ:** Cho một chuỗi ký tự $S$. Hãy tìm độ dài của chuỗi con liên tiếp đối xứng dài nhất nằm trong chuỗi $S$.
* **Dữ liệu vào (Input):** Một chuỗi ký tự $S$ ($1 \le |S| \le 200$).
* **Kết quả ra (Output):** Độ dài lớn nhất tìm được.
* **Dữ liệu mẫu (Sample):**

### Input
```text
ABCBADE
```
### Output
```text
5
```
### Giải thích

Chuỗi con đối xứng dài nhất là `ABCBA` có độ dài 5.

---
