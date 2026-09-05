# Danh Sách Bài Tập Thực Hành: Bài 04: Rẽ nhánh và điều kiện logic

> Nguồn problems: l04, l05, l06 | Tổng 37 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-9
* P1 (Cơ bản): Bài 10-18
* P2 (Luyện tập): Bài 19-27
* P3 (Vận dụng): Bài 28-37
---

### Bài 1 (P0): Số lớn nhất trong hai số
* **Mã bài toán:** `pya_l04_p04_so_lon_nhat_trong_hai_so`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Bộ vi xử lý cần thực hiện thao tác so sánh logic giữa hai thanh ghi dữ liệu $A$ và $B$ để giữ lại giá trị cực đại phục vụ tính toán tiếp theo.
* **Nhiệm vụ:** Cho hai số nguyên $A$ và $B$. Hãy tìm và in ra giá trị lớn nhất trong hai số đó.
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Một số nguyên là giá trị lớn nhất.
* **Sample:** ### Input
```text
-15
8
```
### Output
```text
8
```
### Giải thích

Hai số đầu vào là $25$ và $42$. Số lớn hơn là $42$. Kết quả in ra: `42`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 2 (P0): Trị tuyệt đối của một số
* **Mã bài toán:** `pya_l04_p09_tri_tuyet_doi_cua_mot_so`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong tính toán tọa độ và độ lệch kỹ thuật số, giá trị tuyệt đối $|x|$ thể hiện khoảng cách từ điểm đo đến mốc tham chiếu số 0.
* **Nhiệm vụ:** Cho số nguyên $x$. Hãy tính và in ra giá trị tuyệt đối $|x|$ của số đó.
* **Input:** Một số nguyên $N$ ($-10^9 \le N \le 10^9$).
* **Output:** Giá trị tuyệt đối của $N$.
* **Sample:** ### Input
```text
-25
```
### Output
```text
25
```
### Giải thích

Số đầu vào là $-15$. Giá trị tuyệt đối của $-15$ là $|-15| = 15$. Kết quả in ra: `15`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 3 (P0): Vé vào công viên
* **Mã bài toán:** `pya_l04_p02_ve_vao_cong_vien`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Tại trạm kiểm soát tự động của công viên nước, hệ thống cảm biến quang học đo chiều cao $h$ (cm) của khách hàng để phân loại vé hợp lệ.
* **Nhiệm vụ:** Nếu chiều cao $h \ge 130\text{ cm}$, in ra `VE NGUOI LON`. Nếu $h < 130\text{ cm}$, in ra `VE TRE EM`.
* **Input:** Một số nguyên $h$ ($1 \le h \le 200$).
* **Output:** `VE NGUOI LON` hoặc `VE TRE EM`.
* **Sample:** ### Input
```text
135
```
### Output
```text
VE NGUOI LON
```
### Giải thích

Chiều cao đo được là $135\text{ cm}$. Do $135 \ge 130$, khách hàng cần áp dụng mức vé người lớn. Kết quả in ra: `VE NGUOI LON`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 4 (P0): Kiểm tra số chẵn lẻ
* **Mã bài toán:** `pya_l04_p01_kiem_tra_so_chan_le`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong thuật toán phân nhánh xử lý luồng dữ liệu mạng, các gói tin mang số định danh chẵn và lẻ được chuyển tiếp qua hai kênh truyền tải khác nhau.
* **Nhiệm vụ:** Cho số tự nhiên $N$. Hãy kiểm tra nếu $N$ là số chẵn in ra `CHAN`, ngược lại in ra `LE`.
* **Input:** Một số tự nhiên $N$ ($0 \le N \le 10^9$).
* **Output:** Chuỗi `CHAN` hoặc `LE`.
* **Sample:** ### Input
```text
18
```
### Output
```text
CHAN
```
### Giải thích

Số đầu vào là $18$. Vì $18$ chia hết cho $2$ ($18 \% 2 = 0$), nên đây là số chẵn. Kết quả in ra: `CHAN`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 5 (P0): Điền phép tính lớn nhất
* **Mã bài toán:** `pya_l04_p06_dien_phep_tinh_lon_nhat`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong giờ toán vui, cô giáo viết lên bảng một số tự nhiên $A$ và biểu thức bí ẩn sau: $A \text{ ? } A = B$. Cô đố cả lớp hãy chọn một dấu trong ba dấu cộng, trừ, nhân để lấp vào chỗ dấu hỏi chấm. Thí sinh nào tìm được số $B$ to nhất sẽ được thưởng một tràng pháo tay. Hãy giúp cả lớp tìm ra số $B$ lớn nhất có thể.
* **Nhiệm vụ:** Hãy dùng một trong các phép tính $+$, $-$, $\times$ điền vào dấu $?$ để giá trị $B$ đạt được là **lớn nhất**. In ra số $B$ lớn nhất tìm được.
* **Input:** Một số tự nhiên $A$ ($0 \le A \le 100$).
* **Output:** Một số nguyên duy nhất là số $B$ lớn nhất.
* **Sample:** ### Input
```text
3
```
### Output
```text
9
```
### Giải thích

$3 + 3 = 6$, $3 - 3 = 0$, $3 \times 3 = 9$. Số lớn nhất là 9.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 6 (P0): Giảm giá siêu thị
* **Mã bài toán:** `pya_l04_p07_giam_gia_sieu_thi`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Cuối tuần, mẹ dẫn Bi đi siêu thị mua đồ thật vui. Siêu thị đang có chương trình khuyến mãi: khách hàng mua đơn hàng có tổng giá trị từ $500$ nghìn đồng trở lên sẽ được giảm giá ngay $50$ nghìn đồng, còn các đơn hàng dưới $500$ nghìn đồng thì giữ nguyên giá. Bi xung phong ra quầy tính tiền giúp mẹ. Hãy tính xem phải trả bao nhiêu tiền.
* **Nhiệm vụ:** Nhập vào tổng tiền đơn hàng $N$ (nghìn đồng). Hãy in ra số tiền thực tế khách hàng phải trả sau khi đã áp dụng khuyến mãi.
* **Input:** Một số nguyên dương $N$ ($1 \le N \le 10^6$).
* **Output:** Số tiền phải trả.
* **Sample:** ### Input
```text
620
```
### Output
```text
570
```
### Giải thích

Được giảm 50 nghìn: $620 - 50 = 570$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 7 (P0): Ngày nghỉ cuối tuần
* **Mã bài toán:** `pya_l06_p03_ngay_nghi_cuoi_tuan`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Cô giáo chủ nhiệm dán thời khóa biểu tuần lên bảng và dạy cả lớp cách nhớ các ngày bằng số: `2` là Thứ Hai, `3` là Thứ Ba, cứ thế đến `7` là Thứ Bảy và `8` là Chủ Nhật. Bạn Cún thích nhất hai ngày cuối tuần vì được nghỉ học đi chơi với ông bà. Sáng nào Cún cũng nhìn vào con số trên lịch và đoán xem hôm nay thế nào. Hãy giúp Cún xem hôm đó được nghỉ hay phải đi học.
* **Nhiệm vụ:** Nhập vào một số nguyên $d$ đại diện cho một ngày. Nếu $d$ là Thứ Bảy hoặc Chủ Nhật thì in `NGHI HOC`, ngược lại in `DI HOC`.
* **Input:** Một số nguyên $d$ ($2 \le d \le 8$).
* **Output:** `NGHI HOC` hoặc `DI HOC`.
* **Sample:** ### Input
```text
7
```
### Output
```text
NGHI
```
### Giải thích
Ngày 7 là thứ Bảy nên được nghỉ học.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 8 (P0): Ai cao hơn?
* **Mã bài toán:** `pya_l04_p03_ai_cao_hon`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong hệ thống dữ liệu kiểm tra thể lực, số đo chiều cao của hai ứng viên Minh ($a\text{ cm}$) và Nam ($b\text{ cm}$) được ghi nhận.
* **Nhiệm vụ:** Biết rằng $a \ne b$, hãy xác định và in ra tên của người có chiều cao lớn hơn (`Minh` hoặc `Nam`).
* **Input:** Hai số tự nhiên $a$ và $b$ trên 2 dòng ($50 \le a, b \le 200, a \ne b$).
* **Output:** Tên bạn cao hơn.
* **Sample:** ### Input
```text
142
138
```
### Output
```text
Minh
```
### Giải thích

Chiều cao của Minh là $142\text{ cm}$ và Nam là $138\text{ cm}$. Vì $142 > 138$, bạn Minh cao hơn. Kết quả in ra: `Minh`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 9 (P0): Số chẵn có hai chữ số
* **Mã bài toán:** `pya_l06_p01_so_chan_co_hai_chu_so`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Bạn Minh đang sưu tập các số chẵn có đúng hai chữ số để trang trí bảng tin lớp học. Hãy giúp Minh liệt kê tất cả các số đó.
* **Nhiệm vụ:** Nhập vào một số tự nhiên $N$. Kiểm tra xem $N$ có phải là **số chẵn có đúng hai chữ số** hay không? Nếu đúng in `YES`, ngược lại in `NO`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
24
```
### Output
```text
YES
```
### Giải thích

24 là số chẵn và có 2 chữ số.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 10 (P1): Mario cứu công chúa
* **Mã bài toán:** `pya_l05_p06_mario_cuu_cong_chua`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong khu vườn trò chơi, bạn Mario có $K$ năng lượng còn Công chúa có $P$ năng lượng. Giữa hai người là một chiếc cầu thang có đỉnh cao $N$ bậc: Mario đứng ở chân cầu thang bên trái (cần đi lên $N$ bậc và đi xuống $N$ bậc), Công chúa đứng ở chân cầu thang bên phải (cần đi lên $N$ bậc). Mỗi bậc thang Mario đi tốn $1$ năng lượng, còn mỗi bậc thang Công chúa đi tốn $2$ năng lượng. Cả hai đều mong gặp được nhau trên cầu thang. Hãy giúp hai bạn xem với sức của mình có gặp được nhau không.
* **Nhiệm vụ:** Hỏi với mức năng lượng hiện có, Mario và Công chúa có thể gặp được nhau ở một điểm nào đó trên cầu thang hay không? Nếu gặp được in `YES`, ngược lại in `NO`.
* **Biết rằng:** Tổng số bậc cầu thang từ chân bên này sang chân bên kia là $2N$. Để gặp nhau, tổng số bậc mà Mario leo được cộng với tổng số bậc mà Công chúa leo được phải $\ge 2N$.
* **Input:** Ba số tự nhiên $K, P, N$ ($1 \le K, P, N \le 1000$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
3
3
2
```
### Output
```text
YES
```
### Giải thích

Cầu thang $2N = 4$ bậc. Mario đi được $\min(3, 4) = 3$ bậc. Công chúa có 3 năng lượng đi được $3 // 2 = 1$ bậc. Tổng số bậc đi được là $3 + 1 = 4 \ge 4 \implies$ Gặp nhau!
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 11 (P1): Tiền điện bậc thang
* **Mã bài toán:** `pya_l06_p13_tien_dien_bac_thang`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Gia đình bạn Bông vừa nhận hóa đơn tiền điện tháng này. Nhà bạn đã dùng hết $N$ số điện. Giá điện được tính rất đơn giản: $100$ số điện đầu tiên có giá $2000$ đồng một số, từ số điện thứ $101$ trở đi có giá $3500$ đồng một số. Hãy giúp bạn Bông tính tổng số tiền điện cả nhà phải trả.
* **Nhiệm vụ:** Hãy tính tổng tiền điện (đồng) phải trả cho $N$ số điện theo bảng giá trên.
* **Input:** Nhập 1 số tự nhiên $N$ ($1 \le N \le 10^6$) trên 1 dòng.
* **Output:** Tổng số tiền điện phải trả (số nguyên, tính bằng đồng).
* **Sample:** ### Input
```text
120
```
### Output
```text
270000
```
### Giải thích

- $100$ số đầu: $100 \times 2000 = 200000$ đồng.
- $20$ số còn lại: $20 \times 3500 = 70000$ đồng.
- Tổng cộng: $200000 + 70000 = 270000$ đồng.
* **Ràng buộc:** * **Giới hạn dữ liệu:** $1 \le N \le 10^6$
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 12 (P1): Bác thợ mộc cắt gỗ
* **Mã bài toán:** `pya_l04_p10_bac_tho_moc_cat_go`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong xưởng gia công nội thất, một thanh gỗ có chiều dài $L$ được cưa thành các đoạn nhỏ có chiều dài đúng bằng $k$.
* **Nhiệm vụ:** Cho hai số nguyên dương $L$ và $k$. Hãy tính số đoạn gỗ cưa được và phần chiều dài gỗ vụn còn thừa.
* **Input:** Hai số tự nhiên $L$ và $K$ trên 2 dòng ($1 \le L, K \le 10^9$).
* **Output:** Hai số cách nhau dấu cách `so_doan go_thua` hoặc in chữ `KHONG DU`.
* **Sample:** ### Input
```text
17
5
```
### Output
```text
3 2
```
### Giải thích

Thanh gỗ dài $17\text{ cm}$ cưa thành các đoạn $5\text{ cm}$. Số đoạn cưa được là $17 // 5 = 3$ đoạn, phần gỗ vụn còn thừa là $17 \% 5 = 2\text{ cm}$. Kết quả in ra: `3 2`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 13 (P1): Điểm nằm trong hình chữ nhật
* **Mã bài toán:** `pya_l06_p04_diem_nam_trong_hinh_chu_nhat`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong giờ vẽ, Mít vẽ một khu vườn hình chữ nhật trên giấy ô ly. Bạn đặt góc dưới-trái của vườn tại điểm $(0, 0)$ và góc trên-phải tại điểm $(W, H)$ trong mặt phẳng tọa độ. Mít còn chấm một chú bướm đậu ở đâu đó và đố bạn xem bướm đậu trong vườn hay bay ra ngoài. Hãy giúp Mít kiểm tra chú bướm có nằm trong vườn không.
* **Nhiệm vụ:** Nhập vào $W, H$ và tọa độ của một điểm $(x, y)$. Kiểm tra xem điểm $(x, y)$ có nằm bên trong hoặc trên mép biên của hình chữ nhật hay không? Nếu có in `TRONG`, ngược lại in `NGOAI`.
* **Input:** Bốn số tự nhiên $W, H, x, y$ trên 4 dòng ($1 \le W, H \le 1000, 0 \le x, y \le 1000$).
* **Output:** `TRONG` hoặc `NGOAI`.
* **Sample:** ### Input
```text
2 3 5 5
```
### Output
```text
TRONG
```
### Giải thích
Điểm (2, 3) nằm trọn vẹn bên trong hình chữ nhật từ (0, 0) đến (5, 5).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 14 (P1): Bội chung của 3 và 5
* **Mã bài toán:** `pya_l06_p02_boi_chung_cua_3_va_5`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong trò chơi FizzBuzz phổ biến trên toàn thế giới, người chơi cần nhận biết các số chia hết cho 3, cho 5 hoặc cho cả hai. Hãy lập trình kiểm tra.
* **Nhiệm vụ:** Nhập vào số tự nhiên $N$. Nếu $N$ chia hết cho cả 3 và 5 thì in `FIZZBUZZ`. Ngược lại in `KHONG`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** `FIZZBUZZ` hoặc `KHONG`.
* **Sample:** ### Input
```text
15
```
### Output
```text
YES
```
### Giải thích
Số 15 vừa chia hết cho 3 vừa chia hết cho 5.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 15 (P1): Ba cạnh tam giác hợp lệ
* **Mã bài toán:** `pya_l06_p05_ba_canh_tam_giac_hop_le`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Thí sinh có ba que tính với các độ dài khác nhau. Bạn ấy muốn biết liệu ba que tính đó có thể ghép thành một hình tam giác hay không. Hãy giúp kiểm tra.
* **Nhiệm vụ:** Nhập vào 3 số tự nhiên $a, b, c$ trên 3 dòng. Kiểm tra xem 3 số này có thể tạo thành độ dài 3 cạnh của một tam giác hay không? Nếu có in `HOP LE`, ngược lại in `KHONG HOP LE`.
* **Input:** Ba số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^9$).
* **Output:** `HOP LE` hoặc `KHONG HOP LE`.
* **Sample:** ### Input
```text
3
4
5
```
### Output
```text
HOP LE
```
### Giải thích

$3+4>5$, $3+5>4$, $4+5>3$ đều đúng.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 16 (P1): Kiểm tra năm nhuận
* **Mã bài toán:** `pya_l06_p06_kiem_tra_nam_nhuan`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Lịch treo tường năm nay có 365 hay 366 ngày? Để biết được, em cần xác định năm đó có phải năm nhuận hay không. Hãy viết chương trình kiểm tra.
* **Nhiệm vụ:** Nhập vào một năm dương lịch $Y$. Hãy in ra `NAM NHUAN` nếu năm đó là năm nhuận, ngược lại in `NAM THUONG`.
* **Quy tắc:** Năm nhuận là năm chia hết cho 400, HOẶC chia hết cho 4 nhưng không chia hết cho 100.
* **Input:** Một số tự nhiên $Y$ ($1 \le Y \le 10^5$).
* **Output:** `NAM NHUAN` hoặc `NAM THUONG`.
* **Sample:** ### Input
```text
2024
```
### Output
```text
NAM NHUAN
```
### Giải thích

Với dữ liệu đầu vào là `2024`, kết quả thu được tương ứng là `NAM NHUAN`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 17 (P1): Rút thẻ may mắn
* **Mã bài toán:** `pya_l06_p09_rut_the_may_man`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Ngày hội chợ xuân, sân trường rộn ràng tiếng cười nói. Mỗi người dùng được bốc một chiếc thẻ có ghi một số tự nhiên $N$. Cô tổng phụ trách reo lên rằng chiếc thẻ được coi là "Thẻ Trúng Thưởng" nếu số $N$ chia hết cho 7, **HOẶC** số $N$ có chữ số tận cùng là 7. Bạn Tèo run run mở chiếc thẻ trên tay, hồi hộp không biết mình có trúng thưởng không. Hãy giúp Tèo xem chiếc thẻ có trúng thưởng không.
* **Nhiệm vụ:** Nhập vào số $N$ trên thẻ. In ra `TRUNG THUONG` nếu trúng thưởng, ngược lại in `CHUC MAY MAN LAN SAU`.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 10^9$).
* **Output:** Thông báo tương ứng.
* **Sample:** ### Input
```text
14
```
### Output
```text
TRUNG THUONG
```
### Giải thích
Số 14 chia hết cho 7 nên chiếc thẻ trúng thưởng.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 18 (P1): Số lớn nhất trong ba số
* **Mã bài toán:** `pya_l05_p03_so_lon_nhat_trong_ba_so`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Ba bạn học sinh thi chạy 100 mét. Mỗi bạn chạy được một thành tích khác nhau. Hãy tìm bạn có thành tích tốt nhất (số lớn nhất).
* **Nhiệm vụ:** Nhập vào 3 số nguyên $a, b, c$ mỗi số trên một dòng. Hãy tìm và in ra số có giá trị lớn nhất trong 3 số đó.
* **Input:** Ba số nguyên $a, b, c$ ($-10^9 \le a, b, c \le 10^9$).
* **Output:** Một số nguyên duy nhất là số lớn nhất.
* **Sample:** ### Input
```text
15
28
9
```
### Output
```text
28
```
### Giải thích

Với dữ liệu đầu vào là `15
28
9`, kết quả thu được tương ứng là `28`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 19 (P2): Dấu của số nguyên
* **Mã bài toán:** `pya_l05_p02_dau_cua_so_nguyen`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Trong bài kiểm tra toán, thầy giáo yêu cầu phân loại các số nguyên thành ba nhóm: số dương, số âm và số không. Hãy viết chương trình phân loại tự động.
* **Nhiệm vụ:** Nhập vào số nguyên $N$. Hãy in ra:
 * `DUONG` nếu $N > 0$.
 * `AM` nếu $N < 0$.
 * `KHONG` nếu $N == 0$.
* **Input:** Một số nguyên $N$ ($-10^9 \le N \le 10^9$).
* **Output:** Chuỗi kết quả.
* **Sample:** ### Input
```text
-15
```
### Output
```text
AM
```
### Giải thích
Số -15 nhỏ hơn 0 nên in ra AM.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 20 (P2): Thuận đi tìm ánh đa vận tốc
* **Mã bài toán:** `pya_l05_p09_thuan_di_tim_anh_da_van_toc`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Một buổi chiều đẹp trời, bạn Thuận đứng ở vị trí $x$ còn bạn Ánh đứng ở vị trí $y$ trong sân trường rộng. Thuận rất nhớ bạn nên đi bộ về phía Ánh với vận tốc $v\text{ km/h}$. Cả hai hồi hộp không biết bao giờ thì gặp được nhau. Hãy giúp hai bạn xem khi nào thì gặp nhau.
* **Nhiệm vụ:** Hãy phân tích các tình huống:
 * Nếu $x == y$: in `DA GAP NHAU` (vì đang đứng cùng một chỗ).
 * Nếu $x \ne y$ nhưng $v == 0$: in `KHONG THE GAP` (vì Thuận đứng yên).
 * Nếu $x \ne y$ và $v > 0$:
 * Nếu khoảng cách $|y - x|$ chia hết cho $v$: in ra số giờ để gặp nhau.
 * Nếu không chia hết: in `GAP NHAU LE GIO`.
* **Input:** Ba số nguyên $x, y, v$ ($-10^9 \le x, y \le 10^9, 0 \le v \le 10^9$).
* **Output:** Thông báo tương ứng hoặc số giờ nguyên.
* **Sample:** ### Input
```text
15
```
### Output
```text
XE DAP
```
### Giải thích
Vận tốc 15 km/h nằm trong khoảng từ 10 đến 30 km/h nên Thuận đi xe đạp.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 21 (P2): Cửa hàng bánh bột lọc khuyến mãi
* **Mã bài toán:** `pya_l05_p11_cua_hang_banh_bot_loc_khuyen_mai`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Cuối tuần, cô chủ nhỏ mở một cửa hàng bánh bột lọc thơm ngon trước cổng trường. Cô treo bảng ưu đãi số lượng thật hấp dẫn: mua dưới 10 cái giá $5$ nghìn đồng một cái, mua từ 10 đến 49 cái giá $4$ nghìn đồng một cái, còn mua từ 50 cái trở lên giá chỉ còn $3$ nghìn đồng một cái. Các người dùng xếp hàng dài chờ mua bánh mang về liên hoan. Hãy giúp cô chủ nhỏ tính tiền cho khách.
* **Nhiệm vụ:** Nhập vào số lượng bánh $N$ mà khách muốn mua. Tính tổng số tiền khách phải trả.
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 1000$).
* **Output:** Tổng số tiền (nghìn đồng).
* **Sample:** ### Input
```text
25
```
### Output
```text
100000
```
### Giải thích
Mua 25 chiếc (từ 20 chiếc trở lên) được giá 4000 đ/chiếc: 25 x 4000 = 100000 đ.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 22 (P2): Cạnh thứ tư hình chữ nhật
* **Mã bài toán:** `pya_l04_p11_canh_thu_tu_hinh_chu_nhat`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Sau giờ thủ công, bạn Nam nhặt được 3 thanh gỗ có độ dài là $A, B, C$ ở góc lớp học. Cô giáo mỉm cười cho biết chắc chắn 3 thanh này là 3 cạnh của một hình chữ nhật, mà một hình chữ nhật luôn có 4 cạnh tạo thành 2 cặp cạnh đối bằng nhau (2 chiều dài bằng nhau và 2 chiều rộng bằng nhau). Nam muốn tìm thêm đúng một thanh gỗ nữa để ghép vừa khít thành khung hình. Hãy giúp bạn Nam tìm độ dài thanh gỗ còn thiếu.
* **Nhiệm vụ:** Hãy tìm độ dài thanh gỗ thứ 4 còn thiếu để ghép vừa khít thành hình chữ nhật.
* **Input:** Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le A, B, C \le 1000$).
* **Output:** Độ dài cạnh thứ 4.
* **Sample:** ### Input
```text
3
5
3
```
### Output
```text
5
```
### Giải thích

Đã có 2 cạnh bằng 3, vậy cạnh còn lại phải là 5.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 23 (P2): Chia kẹo công bằng
* **Mã bài toán:** `pya_l04_p05_chia_keo_cong_bang`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Hôm liên hoan lớp, cô giáo mang đến một túi có $a$ chiếc kẹo thơm ngon để chia cho $b$ bạn học sinh. Cô muốn chia thật công bằng sao cho tất cả các bạn đều nhận được số kẹo bằng nhau và không còn thừa cái nào, để không bạn nào phải buồn. Cả lớp nín thở chờ xem túi kẹo có chia vừa khít hay không. Hãy giúp cô kiểm tra xem số kẹo có chia đều được không.
* **Nhiệm vụ:** Kiểm tra xem số kẹo có chia đều được hay không? Nếu chia đều được thì in `YES`, ngược lại in `NO`.
* **Input:** Hai số nguyên dương $a, b$ ($1 \le a, b \le 10^6$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
20
4
```
### Output
```text
YES
```
### Giải thích

20 chia hết cho 4, mỗi bạn 5 cái kẹo.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 24 (P2): Thứ mấy trong tuần?
* **Mã bài toán:** `pya_l05_p10_thu_may_trong_tuan`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Đầu năm mới, Bin treo một tờ lịch thật đẹp trong phòng học. Mẹ đố Bin rằng ngày mùng 1 tháng Giêng năm nay là ngày **Thứ Hai**. Bin rất thích lật từng tờ lịch và đếm xem các ngày tiếp theo rơi vào thứ mấy. Hãy giúp Bin trả lời ngày thứ $K$ là thứ mấy.
* **Nhiệm vụ:** Cho biết ngày thứ $K$ trong năm đó là thứ mấy?
 * Biết rằng: ngày 1 là Thứ Hai, ngày 2 là Thứ Ba, ..., ngày 7 là Chủ Nhật, ngày 8 lại quay về Thứ Hai.
* **Input:** Một số tự nhiên $K$ ($1 \le K \le 365$).
* **Output:** In ra một trong các chuỗi: `THU HAI`, `THU BA`, `THU TU`, `THU NAM`, `THU SAU`, `THU BAY`, `CHU NHAT`.
* **Sample:** ### Input
```text
2
```
### Output
```text
THU 2
```
### Giải thích
Ngày thứ 2 trong tuần là Thứ Hai.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 25 (P2): Phân loại tam giác
* **Mã bài toán:** `pya_l05_p08_phan_loai_tam_giac`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Trong giờ thủ công, Na cắt được một miếng bìa hình tam giác có 3 cạnh dài $a, b, c$ và cô giáo bảo đó là một tam giác hợp lệ. Cả lớp tò mò không biết miếng bìa của Na thuộc loại tam giác nào. Na muốn khoe với mẹ mà chưa gọi đúng tên hình. Hãy giúp bạn Na gọi đúng tên loại tam giác.
* **Nhiệm vụ:** Hãy phân loại tam giác đó:
 * Nếu 3 cạnh bằng nhau ($a == b == c$): in `TAM GIAC DEU`.
 * Nếu có 2 cạnh bằng nhau ($a == b$ hoặc $b == c$ hoặc $c == a$): in `TAM GIAC CAN`.
 * Các trường hợp còn lại: in `TAM GIAC THUONG`.
* **Input:** Ba số tự nhiên $a, b, c$ trên 3 dòng ($1 \le a, b, c \le 1000$).
* **Output:** Tên phân loại tam giác.
* **Sample:** ### Input
```text
3 3 3
```
### Output
```text
DEU
```
### Giải thích
Ba cạnh có độ dài bằng nhau nên tam giác là tam giác đều.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 26 (P2): Tính cước taxi bậc thang
* **Mã bài toán:** `pya_l05_p07_tinh_cuoc_taxi_bac_thang`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Hôm nay cả lớp đi dã ngoại bằng chiếc taxi "Rùa Con" rất dễ thương. Bác tài xế dán bảng giá lên cửa xe: giá mở cửa cho $1\text{ km}$ đầu tiên là $10$ nghìn đồng, từ kilomet thứ 2 đến kilomet thứ 10 giá $8$ nghìn đồng mỗi km, còn từ kilomet thứ 11 trở đi giá $6$ nghìn đồng mỗi km. Mi ngồi ghế đầu, tay cầm đồng hồ đo quãng đường và muốn tính tiền giúp cả lớp. Hãy tính tổng tiền cước.
* **Nhiệm vụ:** Nhập vào số kilomet $N$ mà khách đã đi (số nguyên $N \ge 1$). Tính tổng số tiền cước (nghìn đồng).
* **Input:** Một số tự nhiên $N$ ($1 \le N \le 100$).
* **Output:** Tổng tiền cước taxi.
* **Sample:** ### Input
```text
1
```
### Output
```text
10
```
### Giải thích

Đúng 1 km đầu: 10 nghìn.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 27 (P2): Xếp loại học lực
* **Mã bài toán:** `pya_l05_p04_xep_loai_hoc_luc`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Cuối học kỳ, cô giáo cần xếp loại học lực cho từng học sinh dựa vào điểm trung bình. Hãy giúp cô giáo viết chương trình xếp loại tự động.
* **Nhiệm vụ:** Nhập vào điểm trung bình môn Tin học của một người dùng (số thực $0.0 \le diem \le 10.0$).
 * Điểm $\ge 9.0$: in `XUAT SAC`.
 * Điểm $\ge 8.0$ và $< 9.0$: in `GIOI`.
 * Điểm $\ge 6.5$ và $< 8.0$: in `KHA`.
 * Điểm $< 6.5$: in `CAN CO GANG`.
* **Input:** Một số thực $diem$.
* **Output:** Xếp loại tương ứng.
* **Sample:** ### Input
```text
8.5
```
### Output
```text
GIOI
```
### Giải thích
Điểm 8.5 thuộc thang điểm giỏi (từ 8.0 trở lên).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 28 (P3): Số ngày trong tháng
* **Mã bài toán:** `pya_l06_p07_so_ngay_trong_thang`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Lan muốn biết tháng sinh nhật của mình có bao nhiêu ngày. Mỗi tháng trong năm có số ngày khác nhau, đặc biệt tháng 2 còn phụ thuộc vào năm nhuận. Hãy giúp Lan.
* **Nhiệm vụ:** Nhập vào tháng $M$ ($1 \le M \le 12$) và năm $Y$ ($1 \le Y \le 10^5$). Hãy in ra số lượng ngày của tháng đó trong năm $Y$.
* **Biết rằng:**
 * Tháng 1, 3, 5, 7, 8, 10, 12 có đúng 31 ngày.
 * Tháng 4, 6, 9, 11 có đúng 30 ngày.
 * Tháng 2: có 29 ngày nếu $Y$ là năm nhuận, có 28 ngày nếu $Y$ là năm thường.
* **Input:** Hai dòng lần lượt là $M$ và $Y$.
* **Output:** Một số nguyên duy nhất là số ngày của tháng.
* **Sample:** ### Input
```text
2
2024
```
### Output
```text
29
```
### Giải thích

Với dữ liệu đầu vào là `2
2024`, kết quả thu được tương ứng là `29`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 29 (P3): Cặp đôi cùng dấu hay trái dấu
* **Mã bài toán:** `pya_l06_p11_cap_doi_cung_dau_hay_trai_dau`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Hai số nguyên được gọi là "cùng dấu" nếu cả hai đều dương hoặc cả hai đều âm. Ngược lại chúng "trái dấu". Hãy kiểm tra cặp số.
* **Nhiệm vụ:** Nhập vào hai số nguyên $a$ và $b$ (có thể âm, dương hoặc bằng 0).
 * In `CO SO KHONG` nếu có ít nhất một số bằng 0 ($a == 0$ hoặc $b == 0$).
 * In `CUNG DAU` nếu cả hai số cùng mang dấu dương hoặc cùng mang dấu âm ($a \times b > 0$).
 * In `TRAI DAU` nếu một số dương và một số âm ($a \times b < 0$).
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Thông báo theo quy định.
* **Sample:** ### Input
```text
5 10
```
### Output
```text
CUNG DAU
```
### Giải thích
Cả hai số 5 và 10 đều là số dương nên cùng dấu.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 30 (P3): Cặp số bằng nhau hay khác?
* **Mã bài toán:** `pya_l04_p08_cap_so_bang_nhau_hay_khac`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong trò chơi ghép đôi, hai lá bài được lật lên. Nếu hai lá bài có cùng giá trị thì người chơi được cộng điểm. Hãy kiểm tra xem hai số có bằng nhau không.
* **Nhiệm vụ:** Nhập vào 2 số nguyên $a$ và $b$. Hãy so sánh và in ra màn hình một trong ba thông báo:
 * `a LON HON b` (nếu $a > b$)
 * `a NHO HON b` (nếu $a < b$)
 * `HAI SO BANG NHAU` (nếu $a == b$)
* **Input:** Hai số nguyên $a, b$ ($-10^9 \le a, b \le 10^9$).
* **Output:** Một dòng thông báo theo đúng mẫu.
* **Sample:** ### Input
```text
15 28
```
### Output
```text
a NHO HON b
```
### Giải thích
Số 15 nhỏ hơn số 28 nên in ra a NHO HON b.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 31 (P3): Trò chơi oẳn tù tì
* **Mã bài toán:** `pya_l04_p12_tro_choi_oan_tu_ti`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Giờ ra chơi, hai bạn Tí và Tèo rủ nhau chơi trò Oẳn Tù Tì thật sôi nổi. Hai bạn quy ước các lựa chọn bằng số: `1` là Búa (Đấm), `2` là Kéo, `3` là Bao (Lá). Luật chơi là: Búa (1) thắng Kéo (2); Kéo (2) thắng Bao (3); Bao (3) thắng Búa (1), còn nếu ra cùng số thì hòa nhau. Cả hai cùng hô to và ra tay mà chưa biết ai thắng. Hãy giúp hai bạn xem ai là người thắng cuộc.
* **Nhiệm vụ:** Nhập vào lựa chọn của Tí và Tèo. Hãy in ra kết quả: `TI THANG`, `TEO THANG` hoặc `HOA`.
* **Input:** Hai số tự nhiên lần lượt là lựa chọn của Tí và Tèo ($1, 2, 3$).
* **Output:** `TI THANG`, `TEO THANG` hoặc `HOA`.
* **Sample:** ### Input
```text
1
2
```
### Output
```text
TI THANG
```
### Giải thích

Tí ra Búa (1), Tèo ra Kéo (2) $\to$ Tí thắng.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 32 (P3): Đèn giao thông ngã tư
* **Mã bài toán:** `pya_l05_p01_den_giao_thong_nga_tu`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Tại ngã tư gần trường, đèn giao thông điều khiển lưu lượng xe. Mỗi màu đèn có ý nghĩa khác nhau: đỏ thì dừng, vàng thì chuẩn bị, xanh thì đi. Hãy lập trình mô phỏng hệ thống đèn giao thông.
* **Nhiệm vụ:** Nhập vào một chữ cái in hoa đại diện cho màu đèn: `D` (Đỏ), `V` (Vàng), `X` (Xanh).
 * Nếu là `D`: in ra `DUNG LAI`.
 * Nếu là `V`: in ra `DI CHAM`.
 * Nếu là `X`: in ra `DUOC DI`.
* **Input:** Một ký tự `D`, `V` hoặc `X`.
* **Output:** Thông báo tương ứng.
* **Sample:** ### Input
```text
do
```
### Output
```text
DUNG LAI
```
### Giải thích
Màu đèn là "do" nên in ra thông báo DUNG LAI.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 33 (P3): Giao nhau của hai đoạn thẳng
* **Mã bài toán:** `pya_l06_p12_giao_nhau_cua_hai_doan_thang`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong giờ chơi xếp hình, hai bạn An và Bình mỗi bạn có một đoạn dây thun màu căng trên cây thước dài. Trên trục số thực, đoạn dây thứ nhất nối từ điểm $L_1$ đến $R_1$ ($L_1 \le R_1$), đoạn dây thứ hai nối từ điểm $L_2$ đến $R_2$ ($L_2 \le R_2$). Hai bạn thắc mắc không biết hai đoạn dây có chồng lên nhau ở chỗ nào không. Hãy giúp hai bạn kiểm tra xem hai đoạn dây có điểm chung không.
* **Nhiệm vụ:** Hãy kiểm tra xem hai đoạn thẳng này có điểm chung (giao nhau) hay không?
 * Nếu có giao nhau: in ra `GIAO NHAU` và độ dài của đoạn giao nhau đó.
 * Nếu không giao nhau: in `KHONG GIAO NHAU`.
* **Input:** Bốn số nguyên $L_1, R_1, L_2, R_2$ trên 4 dòng ($-10^9 \le L_1 \le R_1 \le 10^9, -10^9 \le L_2 \le R_2 \le 10^9$).
* **Output:** `GIAO NHAU [do_dai]` hoặc `KHONG GIAO NHAU`.
* **Sample:** ### Input
```text
1
6
4
9
```
### Output
```text
GIAO NHAU 2
```
### Giải thích

Đoạn giao nhau từ 4 đến 6, độ dài: $6 - 4 = 2$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 34 (P3): Vé gửi xe bến bãi
* **Mã bài toán:** `pya_l05_p05_ve_gui_xe_ben_bai`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Sáng chủ nhật, cả nhà Bo đến khu vui chơi gửi xe ở bãi giữ xe thông minh. Bác bảo vệ vui tính chỉ bảng giá vé theo loại phương tiện: loại `1` (Xe đạp) giá $2$ nghìn đồng, loại `2` (Xe máy) giá $5$ nghìn đồng, loại `3` (Xe ô tô) giá $30$ nghìn đồng, còn các loại khác thì máy báo `LOI PHUONG TIEN`. Bo xung phong đọc mã loại xe giúp bác. Hãy tính đúng giá vé.
* **Nhiệm vụ:** Nhập vào mã loại xe và in ra giá vé tương ứng; nếu mã không thuộc `1`, `2`, `3` thì in `LOI PHUONG TIEN`.
* **Input:** Một số nguyên mã loại xe.
* **Output:** Số tiền gửi xe hoặc chữ `LOI PHUONG TIEN`.
* **Sample:** ### Input
```text
xe may
```
### Output
```text
5000
```
### Giải thích
Phương tiện gửi là xe máy có mức phí 5000 đồng.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 35 (P3): Bốn mùa trong năm
* **Mã bài toán:** `pya_l05_p12_bon_mua_trong_nam`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong giờ khoa học, cô giáo treo bức tranh bốn mùa thật đẹp lên bảng. Cô giảng rằng một năm có 12 tháng được chia thành 4 mùa: **Mùa Xuân** gồm tháng 1, 2, 3; **Mùa Hạ (Hè)** gồm tháng 4, 5, 6; **Mùa Thu** gồm tháng 7, 8, 9; còn **Mùa Đông** gồm tháng 10, 11, 12. Su thích nhất mùa hè vì được đi biển cùng gia đình. Hãy xác định một tháng bất kỳ thuộc mùa nào.
* **Nhiệm vụ:** Nhập vào một số nguyên $M$.
 * Nếu $1 \le M \le 12$, hãy in ra tên mùa tương ứng (`XUAN`, `HA`, `THU`, `DONG`).
 * Nếu $M$ không nằm từ 1 đến 12, in ra `THANG KHONG HOP LE`.
* **Input:** Một số nguyên $M$ ($-100 \le M \le 100$).
* **Output:** Tên mùa hoặc thông báo lỗi.
* **Sample:** ### Input
```text
4
```
### Output
```text
HA
```
### Giải thích
Tháng 4 thuộc mùa hạ (mùa hè).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 36 (P3): Tam giác vuông hay không?
* **Mã bài toán:** `pya_l06_p08_tam_giac_vuong_hay_khong`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong giờ toán hình, cô giáo kể về định lý Pytago nổi tiếng: tam giác có 3 cạnh $a, b, c$ là tam giác vuông nếu bình phương một cạnh bằng tổng bình phương hai cạnh còn lại ($a^2 + b^2 = c^2$ hoặc $a^2 + c^2 = b^2$ hoặc $b^2 + c^2 = a^2$). Bạn Tôm rất thích xếp que tính thành hình tam giác và đoán xem hình nào có góc vuông. Tôm loay hoay mãi chưa chắc chắn. Hãy giúp Tôm kiểm tra xem ba que tính có tạo thành tam giác vuông không.
* **Nhiệm vụ:** Cho 3 số dương $a, b, c$. Nếu chúng tạo thành một tam giác vuông thì in `VUONG`, ngược lại in `KHONG VUONG`.
* **Input:** Ba số nguyên $a, b, c$ ($1 \le a, b, c \le 10^4$).
* **Output:** `VUONG` hoặc `KHONG VUONG`.
* **Sample:** ### Input
```text
3
4
5
```
### Output
```text
VUONG
```
### Giải thích

$3^2 + 4^2 = 9 + 16 = 25 = 5^2$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 37 (P3): Ngày kế tiếp trong năm
* **Mã bài toán:** `pya_l06_p10_ngay_ke_tiep_trong_nam`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Bông có một cuốn lịch để bàn rất xinh và ngày nào cũng tự tay xé một tờ. Hôm nay tờ lịch ghi một ngày hợp lệ gồm 3 số: ngày $D$, tháng $M$, năm $Y$. Bông tò mò muốn biết lật sang tờ tiếp theo sẽ là ngày tháng năm nào. Mẹ dặn rằng phải nhớ cả tháng dài tháng ngắn và năm nhuận nữa. Hãy giúp Bông tìm ra ngày kế tiếp ngay sau đó.
* **Nhiệm vụ:** Hãy tính và in ra ngày, tháng, năm của **ngày kế tiếp ngay sau đó**.
* **Input:** Ba số tự nhiên $D, M, Y$ trên 3 dòng.
* **Output:** Ba số nguyên cách nhau một dấu cách `D_tiep M_tiep Y_tiep`.
* **Sample:** ### Input
```text
31
12
2024
```
### Output
```text
1 1 2025
```
### Giải thích

Ngày cuối năm chuyển sang ngày đầu năm mới!
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---
