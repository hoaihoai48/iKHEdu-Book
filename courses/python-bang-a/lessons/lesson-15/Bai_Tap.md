# Danh Sách Bài Tập Thực Hành: Bài 15: Chiến lược giải đề thi

> Nguồn problems: l18 | Tổng 12 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-3
* P1 (Cơ bản): Bài 4-6
* P2 (Luyện tập): Bài 7-9
* P3 (Vận dụng): Bài 10-12
---

### Bài 1 (P0): Chú kiến tha mồi về tổ
* **Mã bài toán:** `pya_l18_p04_chu_kien_tha_moi_ve_to`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong vườn nhà bạn Tí có một chú kiến nhỏ chăm chỉ đứng tại tọa độ $0$ trên một con đường thẳng. Hôm nay, chú ngửi thấy mùi bánh thơm ở vị trí $X$ nên muốn bò đến đó. Mỗi bước, chú kiến có thể nhảy dài tùy ý từ $1$ đến $5$ mét ($1, 2, 3, 4$ hoặc $5$). Chú kiến nhỏ xíu nên muốn đi ít bước nhất cho đỡ mệt, hãy chú tìm đường đi ngắn nhất.
* **Nhiệm vụ:** Hãy tìm số bước nhảy ít nhất để chú kiến đến được đúng vị trí $X$.
* **Input:** Một số nguyên dương $X$ ($1 \le X \le 10^9$).
* **Output:** Số bước nhảy tối thiểu.
* **Sample:** ### Input
```text
12
```
### Output
```text
3
```
### Giải thích

Nhảy $5 + 5 + 2 = 12$ mét (cần 3 bước).


### PHẦN 2: ĐỀ THI THỬ SỐ 02 (MÔ PHỎNG ĐỀ lập trình LÂM ĐỒNG / ĐÀ LẠT)
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 2 (P0): Đếm số lần xuất hiện của tên bạn thân
* **Mã bài toán:** `pya_l18_p07_dem_so_lan_xuat_hien_cua_ten_ban_than`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** An vừa viết một bài văn miêu tả kỷ niệm tuổi học trò thật dễ thương để tặng bạn thân tên là `BIN`. Học sinh tò mò muốn đếm xem tên của người bạn thân ấy xuất hiện bao nhiêu lần trong bài văn (không phân biệt chữ in hoa hay in thường: `Bin`, `BIN`, `bin` đều được tính). Bài văn dài quá nên đếm mãi mà cứ nhầm. Hãy đếm thật chính xác.
* **Nhiệm vụ:** Cho chuỗi văn bản $S$. Hãy đếm số lần từ `bin` xuất hiện như một từ độc lập.
* **Input:** Dòng văn bản $S$ ($1 \le |S| \le 10^4$).
* **Output:** Số lần xuất hiện.
* **Sample:** ### Input
```text
Hom nay Bin va bin di choi cung ban BIN
```
### Output
```text
3
```
### Giải thích

Với dữ liệu đầu vào là `Hom nay Bin va bin di choi cung ban BIN`, kết quả thu được tương ứng là `3`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 3 (P0): Chuẩn hóa mã thí sinh
* **Mã bài toán:** `pya_l18_p03_chuan_hoa_ma_thi_sinh`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trường em tổ chức hội thi vẽ tranh nên mỗi người dùng được phát một mã thí sinh gồm 2 phần: chữ cái viết tắt của tỉnh và số báo danh (ví dụ: `HN025`, `DN007`). Hôm nay, cô văn thư nhập liệu vội quá nên gõ nhầm chữ thường và để sót các khoảng trắng thừa như thế này: ` hn 25 `. Cô đang lo các thẻ dự thi bị xấu, hãy cô sửa lại các mã thí sinh cho thật ngay ngắn.
* **Nhiệm vụ:** Cho chuỗi nhập liệu gồm chữ viết tắt và số. Hãy chuẩn hóa thành chuỗi viết hoa, bỏ mọi khoảng trắng và nếu phần số có ít hơn 3 chữ số thì thêm các chữ số 0 vào trước để phần số luôn đủ 3 chữ số.
* **Input:** Một dòng văn bản gồm chữ cái và số nguyên $K$.
* **Output:** Mã thí sinh chuẩn hóa.
* **Sample:** ### Input
```text
hn 5
```
### Output
```text
HN005
```
### Giải thích

Với dữ liệu đầu vào là `hn 5`, kết quả thu được tương ứng là `HN005`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 4 (P1): Thu hoạch dâu tây đà lạt
* **Mã bài toán:** `pya_l18_p05_thu_hoach_dau_tay_da_lat`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Cuối tuần, gia đình bạn Mai lên thăm nông trại dâu tây ở Đà Lạt và thấy bác nông dân vừa thu hoạch được $K$ kg dâu chín mọng. Dâu được đóng vào 2 loại hộp xinh xắn: hộp lớn chứa được $5\text{ kg}$ và hộp nhỏ chứa được $1\text{ kg}$. Để tiết kiệm chi phí đóng gói, bác chủ nông trại muốn dùng nhiều hộp lớn nhất có thể. Hãy giúp bác chia dâu vào các hộp.
* **Nhiệm vụ:** Cho số nguyên $K$. Hãy in ra số hộp lớn và số hộp nhỏ cần dùng.
* **Input:** Một số nguyên $K$ ($1 \le K \le 10^6$).
* **Output:** Hai số nguyên: số hộp lớn trước, số hộp nhỏ sau.
* **Sample:** ### Input
```text
23
```
### Output
```text
4 3
```
### Giải thích

Với dữ liệu đầu vào là `23`, kết quả thu được tương ứng là `4 3`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 5 (P1): Cặp số bạn bè
* **Mã bài toán:** `pya_l18_p02_cap_so_ban_be`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Bi và Bo là đôi bạn thân hay chơi trò các con số cùng nhau. Hai bạn đặt ra luật riêng: hai số tự nhiên được gọi là "Cặp số bạn bè" nếu tổng các chữ số của chúng bằng nhau. Ví dụ: $25$ ($2+5=7$) và $34$ ($3+4=7$) là một cặp số bạn bè vì cả hai cùng có tổng bằng 7. Hai bạn đố nhau mãi không phân thắng bại, hãy hai bạn kiểm tra các cặp số.
* **Nhiệm vụ:** Cho hai số nguyên dương $A$ và $B$. Hãy kiểm tra xem $A$ và $B$ có phải là cặp số bạn bè không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Hai số nguyên $A, B$ ($1 \le A, B \le 10^{18}$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
123 51
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `123 51`, kết quả thu được tương ứng là `YES`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 6 (P1): Bảng điểm thi khảo sát năng khiếu
* **Mã bài toán:** `pya_l18_p11_bang_diem_thi_khao_sat_nang_khieu`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trường em vừa tổ chức kỳ thi khảo sát năng khiếu thật sôi nổi với $N$ người dùng cùng tham gia. Mỗi bạn có một điểm số nguyên từ 0 đến 100 được cô giáo ghi cẩn thận lên bảng vàng. Ban giám khảo quyết định chọn ra $K$ bạn có điểm cao nhất để vào đội tuyển chính thức đi thi cấp thành phố. Cả sân trường đang hồi hộp chờ kết quả, hãy ban giám khảo chọn ra các bạn xuất sắc nhất.
* **Nhiệm vụ:** Cho danh sách điểm của $N$ bạn và số $K$. Hãy in ra điểm số của $K$ bạn được chọn theo thứ tự giảm dần từ cao xuống thấp.
* **Input:** * Dòng 1: Hai số $N$ và $K$ ($1 \le K \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên là điểm của các thí sinh.
* **Output:** $K$ điểm số cao nhất cách nhau bởi khoảng trắng.
* **Sample:** ### Input
```text
6 3
70 95 85 60 90 85
```
### Output
```text
95 90 85
```
### Giải thích

Với dữ liệu đầu vào là `6 3
70 95 85 60 90 85`, kết quả thu được tương ứng là `95 90 85`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 7 (P2): Đồng hồ cát kỳ diệu
* **Mã bài toán:** `pya_l18_p09_dong_ho_cat_ky_dieu`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bạn Tèo được tặng một chiếc đồng hồ cát kỳ diệu có thể đo được các khoảng thời gian thật hay. Tối nay, bạn cùng bố quan sát bầu trời đầy sao, bắt đầu từ $0$ giờ $0$ phút $0$ giây. Sau đúng $S$ giây ngắm sao, buổi quan sát kết thúc và hai bố con muốn ghi lại giờ giấc thật đẹp. Hãy giúp hai bố con đổi số giây thành giờ phút giây.
* **Nhiệm vụ:** Hãy đổi $S$ giây thành định dạng chuẩn: `HH:MM:SS` (Giờ:Phút:Giây), mỗi thành phần luôn có 2 chữ số (ví dụ: `05:08:09`).
* **Input:** Một số nguyên $S$ ($0 \le S < 86400$).
* **Output:** Chuỗi giờ phút giây định dạng `HH:MM:SS`.
* **Sample:** ### Input
```text
3665
```
### Output
```text
01:01:05
```
### Giải thích

Với dữ liệu đầu vào là `3665`, kết quả thu được tương ứng là `01:01:05`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 8 (P2): Mua bút tặng bạn
* **Mã bài toán:** `pya_l18_p01_mua_but_tang_ban`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Đầu năm học mới, bạn Lan rủ mẹ đi mua bút để tặng các bạn trong lớp. Cửa hàng văn phòng phẩm có chương trình khuyến mãi thật hay: mỗi chiếc bút có giá $P$ đồng. Nếu mua từ 5 chiếc bút trở lên, mỗi chiếc bút sẽ được giảm giá $10\%$. Nếu mua từ 10 chiếc bút trở lên, mỗi chiếc bút sẽ được giảm giá $20\%$. Mẹ nhờ Lan tính nhanh số tiền phải trả, hãy bạn Lan tính.
* **Nhiệm vụ:** Cho số lượng bút cần mua $N$ và đơn giá $P$. Hãy tính tổng số tiền bạn Lan phải trả (kết quả là số nguyên).
* **Input:** Hai số nguyên dương $N$ và $P$ ($1 \le N \le 1000, 1000 \le P \le 100000$).
* **Output:** Tổng số tiền phải thanh toán.
* **Sample:** ### Input
```text
6 10000
```
### Output
```text
54000
```
### Giải thích

Mua 6 chiếc ($\ge 5$), giá mỗi chiếc là $9000$ đ. Tổng tiền: $6 \times 9000 = 54000$ đ.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 9 (P2): Số đặc biệt chia hết cho tổng chữ số
* **Mã bài toán:** `pya_l18_p06_so_dac_biet_chia_het_cho_tong_chu_so_harshad`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bạn Tí rất thích sưu tầm các con số kỳ lạ trong cuốn sổ tay toán học của mình. Hôm nay, bạn phát hiện một loại số đặc biệt: một số tự nhiên $N$ được gọi là số Harshad nếu nó chia hết cho chính tổng các chữ số của nó. Ví dụ: số 18 có tổng các chữ số là $1 + 8 = 9$. Vì 18 chia hết cho 9 nên 18 là số Harshad. Bạn Tí đố cả lớp tìm thêm các số như vậy, hãy cả lớp kiểm tra.
* **Nhiệm vụ:** Cho số $N$. In `YES` nếu $N$ là số Harshad, ngược lại in `NO`.
* **Input:** Số nguyên $N$ ($1 \le N \le 10^9$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
18
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `18`, kết quả thu được tương ứng là `YES`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 10 (P3): Dãy con liên tiếp tăng dài nhất
* **Mã bài toán:** `pya_l18_p12_day_con_lien_tiep_tang_dai_nhat`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Các người dùng lớp 4A đang chơi trò xếp thẻ số thành một hàng dài gồm $N$ số nguyên. Các bạn phát hiện một trò rất vui gọi là "dãy con liên tiếp tăng": đó là một đoạn các phần tử đứng cạnh nhau mà phần tử đứng sau luôn lớn hơn phần tử đứng ngay trước nó ($A_i < A_{i+1} < A_{i+2} \dots$). Ai tìm được đoạn dài nhất sẽ thắng, hãy các bạn tìm xem đoạn dài nhất có bao nhiêu thẻ số.
* **Nhiệm vụ:** Hãy tìm độ dài của dãy con liên tiếp tăng dài nhất trong dãy số đã cho.
* **Input:** * Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).
* **Output:** Một số nguyên duy nhất là độ dài lớn nhất tìm được.
* **Sample:** ### Input
```text
6
1 3 5 2 4 7
```
### Output
```text
3
```
### Giải thích

Dãy con tăng dài nhất có độ dài 3 (đoạn `1 3 5` hoặc `2 4 7`).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 11 (P3): Dãy số bội chung của 3 và 5 đẹp mắt
* **Mã bài toán:** `pya_l18_p08_day_so_boi_chung_cua_3_va_5_dep_mat`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Na có một hộp bi màu rất đẹp và bạn đánh số lên từng viên bi theo quy tắc riêng: chỉ chọn các số chia hết cho 3 HOẶC chia hết cho 5 rồi xếp tăng dần thành một dãy: $3, 5, 6, 9, 10, 12, 15, 18, 20 \dots$. Bạn Na muốn biết viên bi thứ mấy mang số nào mà đếm hoài không xuể. Hãy giúp bạn Na tìm nhanh.
* **Nhiệm vụ:** Cho số nguyên dương $K$ ($1 \le K \le 10^5$). Hãy tìm số hạng thứ $K$ của dãy số này.
* **Input:** Một số nguyên $K$.
* **Output:** Giá trị số hạng thứ $K$.
* **Sample:** ### Input
```text
7
```
### Output
```text
15
```
### Giải thích

Số thứ 7 là 15.


### PHẦN 3: ĐỀ THI THỬ SỐ 03 (MÔ PHỎNG VÒNG CHUNG KẾT TOÀN QUỐC BẢNG A)
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 12 (P3): Số nguyên tố đối xứng
* **Mã bài toán:** `pya_l18_p10_so_nguyen_to_doi_xung`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Mi có một chiếc gương thần mà mỗi lần soi một con số, số đó hiện ra giống hệt khi đọc xuôi hay đọc ngược. Học sinh gọi những số đặc biệt này là số đối xứng, và một số tự nhiên được gọi là "Nguyên tố đối xứng" nếu nó vừa là số nguyên tố, vừa là số đối xứng (ví dụ: $11, 101, 131, 151, 181, 191, \dots$). Mi muốn tìm các số kỳ diệu này, hãy nhỏ.
* **Nhiệm vụ:** Cho số nguyên dương $N$. Hãy tìm số nguyên tố đối xứng nhỏ nhất nhưng **lớn hơn hoặc bằng** $N$.
* **Input:** Một số nguyên $N$ ($1 \le N \le 10^5$).
* **Output:** Số nguyên tố đối xứng tìm được.
* **Sample:** ### Input
```text
100
```
### Output
```text
101
```
### Giải thích

Với dữ liệu đầu vào là `100`, kết quả thu được tương ứng là `101`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---
