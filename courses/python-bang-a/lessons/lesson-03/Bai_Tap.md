# Danh Sách Bài Tập Thực Hành: Bài 03

> Nguồn problems: l03 | Tổng 33 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-8
* P1 (Cơ bản): Bài 9-16
* P2 (Luyện tập): Bài 17-24
* P3 (Vận dụng): Bài 25-33
---

### Bài 1 (P0): Đổi đô la sang tiền việt
* **Mã bài toán:** `pya_l03_p31_doi_do_la_sang_tien_viet`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Bác Hùng đi công tác ở nước ngoài về và mang theo $D$ tờ đô la Mỹ, mỗi tờ trị giá $1$ đô la. Bác muốn đổi hết sang tiền Việt Nam để mua quà cho cả nhà. Biết rằng ngân hàng đổi $1$ đô la lấy $25000$ đồng. Hãy giúp bác Hùng tính xem bác sẽ nhận được bao nhiêu tiền Việt Nam.
* **Nhiệm vụ:** Hãy tính số tiền Việt Nam (đồng) đổi được từ $D$ đô la Mỹ.
* **Input:** Nhập 1 số tự nhiên $D$ ($1 \le D \le 10^6$) trên 1 dòng.
* **Output:** Số tiền Việt Nam tính bằng đồng (số nguyên).
* **Sample:** ### Input
```text
4
```
### Output
```text
100000
```
### Giải thích

- Mỗi đô la đổi được $25000$ đồng.
- $4$ đô la đổi được: $4 \times 25000 = 100000$ đồng.
* **Ràng buộc:** * **Giới hạn dữ liệu:** $1 \le D \le 10^6$
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 2 (P0): Chu vi và diện tích hình vuông
* **Mã bài toán:** `pya_l03_p01_hinh_vuong`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Bác thợ mộc Năm ở xưởng nội thất Hoàng Gia nhận được đơn hàng gia công một lô mặt bàn trà hình vuông cao cấp. Theo bản vẽ thiết kế, mỗi mặt bàn có cạnh dài $A$ mét. Trước khi cắt gỗ, bác cần tính chính xác chu vi (để dán viền bao quanh) và diện tích (để ước lượng lượng sơn phủ bề mặt) của mỗi tấm mặt bàn.
* **Nhiệm vụ:** Nhập một số nguyên dương $A$ là cạnh hình vuông. In ra chu vi và diện tích của hình vuông trên cùng một dòng cách nhau dấu cách.
* **Input:** Một dòng chứa số nguyên dương $A$ ($1 \le A \le 10^4$).
* **Output:** In ra chu vi và diện tích cách nhau một dấu cách.
* **Sample:** ### Input
```text
6
```
### Output
```text
24 36
```
### Giải thích
Chu vi $6 \times 4 = 24$, Diện tích $6 \times 6 = 36$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 3 (P0): Đổi mét sang centimet và milimet
* **Mã bài toán:** `pya_l03_p06_doi_don_vi_dai`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trên công trường xây dựng cầu vượt, kỹ sư trưởng nhận được bản vẽ ghi kích thước bằng đơn vị mét, nhưng máy cắt thép CNC lại yêu cầu nhập liệu theo xen-ti-mét. Anh cần một công cụ chuyển đổi nhanh giữa các đơn vị đo chiều dài: $1$ mét $= 100$ xen-ti-mét, $1$ ki-lô-mét $= 1000$ mét. Em hãy lập trình thực hiện phép chuyển đổi đơn vị chiều dài.
* **Nhiệm vụ:** Nhập số nguyên dương $M$ (đơn vị mét). In ra 2 số trên 1 dòng cách nhau dấu cách: độ dài tương ứng theo centimet ($\text{cm}$) và milimet ($\text{mm}$).
* **Input:** Một dòng chứa số nguyên $M$ ($1 \le M \le 1000$).
* **Output:** In ra hai số nguyên cách nhau dấu cách.
* **Sample:** ### Input
```text
3
```
### Output
```text
300 3000
```
### Giải thích
$3\text{m} = 300\text{cm} = 3000\text{mm}$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 4 (P0): Khung tranh hình vuông
* **Mã bài toán:** `pya_l03_p20_khung_tranh_hinh_vuong`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong quy trình gia công khung nhôm kính, người thợ cần chuẩn bị thanh nẹp viền bao quanh một tấm kính hình vuông có cạnh độ dài $a$.
* **Nhiệm vụ:** Cho độ dài cạnh hình vuông $a$. Hãy tính chu vi của khung hình vuông ($4 \times a$).
* **Input:** Một số tự nhiên $a$ ($1 \le a \le 10^4$).
* **Output:** In ra 2 số nguyên cách nhau một khoảng trắng: Chu vi và Diện tích.
* **Sample:** ### Input
```text
8
```
### Output
```text
32 64
```
### Giải thích

Cạnh hình vuông có độ dài $a = 6$. Chu vi của hình vuông được tính bằng $4 \times 6 = 24$. Kết quả in ra là `24`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 5 (P0): Đổi độ C sang độ F
* **Mã bài toán:** `pya_l03_p14_doi_do_c_sang_do_f`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong giờ học khoa học, cô giáo đố cả lớp một điều thú vị. Ở Việt Nam, nhiệt độ được đo bằng độ C, còn ở nước Mỹ người ta lại dùng độ F. Hôm nay trời nóng $C$ độ C, và $C$ luôn chia hết cho $5$. Hãy giúp cả lớp đổi nhiệt độ này sang độ F để kể cho người dùng ở Mỹ nghe.
* **Nhiệm vụ:** Hãy đổi nhiệt độ $C$ độ C sang độ F theo công thức $F = C \times 9 : 5 + 32$.
* **Input:** Nhập 1 số nguyên $C$ ($-50 \le C \le 50$, $C$ chia hết cho $5$) trên 1 dòng.
* **Output:** Nhiệt độ tính bằng độ F (số nguyên).
* **Sample:** ### Input
```text
30
```
### Output
```text
86
```
### Giải thích

- Đổi sang độ F: $30 \times 9 : 5 + 32 = 270 : 5 + 32 = 54 + 32 = 86$.
* **Ràng buộc:** * **Giới hạn dữ liệu:** $-50 \le C \le 50$, $C$ chia hết cho $5$
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 6 (P0): Cạnh còn lại của hình chữ nhật
* **Mã bài toán:** `pya_l03_p04_canh_con_lai_cua_hinh_chu_nhat`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Ngoài làng có một cái ao cá hình chữ nhật rất mát, một cạnh của ao bằng $a\text{ mét}$ và chu vi của ao là $P\text{ mét}$ ($P$ là số chẵn). Cuối tuần, các người dùng rủ nhau ra ao câu cá và đố nhau tìm cạnh còn lại của ao. Hãy giúp các bạn tính độ dài cạnh còn lại.
* **Nhiệm vụ:** Hãy tính và in ra độ dài của cạnh còn lại của hình chữ nhật.
* **Input:** Gồm 2 dòng: dòng 1 chứa chu vi $P$ ($P$ chẵn, $P \le 10^6$), dòng 2 chứa độ dài cạnh đã biết $a$ ($1 \le a < P // 2$).
* **Output:** Một số tự nhiên là độ dài cạnh còn lại.
* **Sample:** ### Input
```text
30
5
```
### Output
```text
10
```
### Giải thích

Nửa chu vi là: $30 : 2 = 15$. Cạnh còn lại: $15 - 5 = 10$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 7 (P0): Diện tích tam giác vuông
* **Mã bài toán:** `pya_l03_p11_dien_tich_tam_giac_vuong`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Na có một miếng bánh hình tam giác vuông rất xinh. Hai cạnh góc vuông của miếng bánh dài $a\text{ cm}$ và $h\text{ cm}$. Tích $a \times h$ luôn là số chẵn. Na muốn biết miếng bánh của mình rộng bao nhiêu để khoe với cả lớp. Hãy tính diện tích miếng bánh.
* **Nhiệm vụ:** Hãy tính diện tích của hình tam giác vuông có hai cạnh góc vuông là $a$ và $h$.
* **Input:** Nhập 2 số tự nhiên $a$ và $h$ ($1 \le a, h \le 1000$, tích $a \times h$ chia hết cho $2$) trên 2 dòng.
* **Output:** Diện tích của hình tam giác vuông (số nguyên).
* **Sample:** ### Input
```text
6
4
```
### Output
```text
12
```
### Giải thích

- Tích hai cạnh góc vuông: $6 \times 4 = 24$.
- Diện tích tam giác: $24 : 2 = 12$.
* **Ràng buộc:** * **Giới hạn dữ liệu:** $1 \le a, h \le 1000$
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 8 (P0): Chu vi tam giác ABC
* **Mã bài toán:** `pya_l03_p21_chu_vi_tam_giac_abc`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Trong giờ học hình học vui nhộn, thầy giáo vẽ một hình tam giác $ABC$ lên bảng và đố cả lớp. Thầy cho 3 số tự nhiên $a, b, c$ lần lượt là độ dài 3 cạnh của tam giác $ABC$. Các bạn thi nhau giơ tay xung phong tính chu vi. Hãy giúp cả lớp tính chu vi của tam giác $ABC$.
* **Nhiệm vụ:** Hãy lập trình tính và đưa ra chu vi của tam giác $ABC$.
* **Input:** Ba dòng lần lượt ghi 3 số tự nhiên $a, b, c$ ($1 \le a, b, c \le 10^8$).
* **Output:** In ra một số tự nhiên duy nhất là chu vi tam giác.
* **Sample:** ### Input
```text
3
4
5
```
### Output
```text
12
```
### Giải thích

Chu vi: $3 + 4 + 5 = 12$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 9 (P1): Thể tích hộp chữ nhật
* **Mã bài toán:** `pya_l03_p30_the_tich_hop_chu_nhat`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Một khối hộp vừa được tặng một hộp sữa dâu hình hộp chữ nhật. Hộp sữa có chiều dài $d\text{ cm}$, chiều rộng $r\text{ cm}$ và chiều cao $c\text{ cm}$. Một khối hộp tò mò muốn biết hộp sữa của mình chứa được bao nhiêu sữa. Hãy giúp bài toán tính thể tích của hộp sữa.
* **Nhiệm vụ:** Hãy tính thể tích của hình hộp chữ nhật có ba kích thước $d, r, c$.
* **Input:** Nhập 3 số tự nhiên $d, r, c$ ($1 \le d, r, c \le 1000$) trên 3 dòng.
* **Output:** Thể tích của hình hộp chữ nhật (số nguyên).
* **Sample:** ### Input
```text
5
3
2
```
### Output
```text
30
```
### Giải thích

- Thể tích hộp: $5 \times 3 \times 2 = 30$.
* **Ràng buộc:** * **Giới hạn dữ liệu:** $1 \le d, r, c \le 1000$
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 10 (P1): Mảnh vườn chữ nhật
* **Mã bài toán:** `pya_l03_p19_manh_vuon_chu_nhat`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Cuối làng có bác nông dân chăm chỉ với một mảnh vườn trồng rau hình chữ nhật có chiều dài $a\text{ mét}$ và chiều rộng $b\text{ mét}$. Mỗi sáng, bác ra vườn tưới rau xanh mướt, nhưng bác muốn rào quanh vườn và tính diện tích để trồng thêm rau mới. Hãy giúp bác tính chu vi và diện tích của mảnh vườn.
* **Nhiệm vụ:** Hãy tính chu vi và diện tích của mảnh vườn đó.
* **Input:** Gồm 2 dòng lần lượt chứa 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$).
* **Output:** In ra trên một dòng 2 số nguyên cách nhau một dấu cách lần lượt là: Chu vi và Diện tích của mảnh vườn.
* **Sample:** ### Input
```text
10
6
```
### Output
```text
32 60
```
### Giải thích

Chu vi: $(10 + 6) \times 2 = 32$. Diện tích: $10 \times 6 = 60$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 11 (P1): Diện tích bồn hoa chữ thập
* **Mã bài toán:** `pya_l03_p10_dien_tich_bon_hoa_chu_thap`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trong công viên xanh mát có một bồn hoa hình chữ thập (dấu cộng) rất đẹp được tạo thành bởi hai luống hoa hình chữ nhật đặt chồng lên nhau:
 * Một luống hoa nằm ngang có kích thước $a \times b$ ($a$ là chiều dài, $b$ là chiều rộng).
 * Một luống hoa nằm dọc có kích thước $b \times a$ ($b$ là chiều rộng, $a$ là chiều dài).
 * Hai luống hoa giao nhau ở chính giữa tạo thành một hình vuông kích thước $b \times b$.
Cô công nhân muốn biết diện tích thật để gieo hạt, vì phần giao nhau ở giữa không được tính hai lần. Hãy giúp cô tính diện tích bồn hoa.
* **Nhiệm vụ:** Hãy tính diện tích thực tế của toàn bộ bồn hoa chữ thập này (không được tính trùng lặp phần diện tích giao nhau ở chính giữa).
* **Input:** Nhập 2 số tự nhiên $a$ và $b$ ($1 \le b \le a \le 10^4$) trên 2 dòng.
* **Output:** Diện tích thực tế của bồn hoa.
* **Sample:** ### Input
```text
10
3
```
### Output
```text
51
```
### Giải thích

- Luống ngang: $10 \times 3 = 30$.
- Luống dọc: $3 \times 10 = 30$.
- Phần giao nhau ở giữa: $3 \times 3 = 9$.
- Diện tích bồn hoa: $30 + 30 - 9 = 51$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 12 (P1): Thuận đi gặp ánh
* **Mã bài toán:** `pya_l03_p08_thuan_di_gap_anh`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Chiều nắng đẹp, hai bạn Thuận và Ánh sống trên một con đường làng thẳng có các mốc tọa độ tính bằng kilomet. Thuận đang đứng ở vị trí $x$, còn Ánh đang đứng ở vị trí $y$ ($x < y$). Thuận nhảy lên xe đạp và phóng về phía nhà Ánh với vận tốc không đổi là $v\text{ km/h}$ để rủ bạn đi đá bóng.
* **Biết rằng:** Khoảng cách $y - x$ chia hết cho vận tốc $v$.
Ánh đứng chờ ở cổng, hồi hộp không biết bao lâu bạn tới. Hãy giúp hai bạn tính thời gian Thuận đi gặp Ánh.
* **Nhiệm vụ:** Sau bao nhiêu giờ thì Thuận sẽ gặp được Ánh?
* **Input:** Ba dòng lần lượt chứa 3 số tự nhiên $x, y, v$ ($0 \le x < y \le 10^9, 1 \le v \le 10^9$).
* **Output:** Số giờ để Thuận gặp Ánh.
* **Sample:** ### Input
```text
10
70
15
```
### Output
```text
4
```
### Giải thích

Khoảng cách giữa 2 bạn: $70 - 10 = 60\text{ km}$.
Thời gian gặp nhau: $60 : 15 = 4$ giờ.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 13 (P1): Hồ cá sấu và đảo nhỏ
* **Mã bài toán:** `pya_l03_p23_ho_ca_sau_va_dao_nho`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Ở một trang trại vui vẻ có một hồ nước hình vuông cạnh $A$ nuôi những chú cá sấu con hiền lành. Ở chính giữa hồ, người ta xây một hòn đảo nhỏ hình chữ nhật có kích thước $B \times C$ để cá sấu bò lên phơi nắng (hòn đảo nằm trọn trong hồ nước và không chạm vào bờ hồ). Các người dùng thắc mắc mặt nước còn lại rộng bao nhiêu để cá bơi lội. Hãy giúp các bạn tính diện tích mặt nước còn lại.
* **Nhiệm vụ:** Hãy tính diện tích phần mặt nước còn lại sau khi đã xây hòn đảo nhỏ.
* **Input:** Ba số tự nhiên $A, B, C$ trên 3 dòng ($1 \le B, C < A \le 10^4$).
* **Output:** Một số nguyên duy nhất là diện tích mặt nước còn lại.
* **Sample:** ### Input
```text
10
3
4
```
### Output
```text
88
```
### Giải thích

Diện tích hồ: $10 \times 10 = 100$. Diện tích đảo: $3 \times 4 = 12$.
Mặt nước còn lại: $100 - 12 = 88$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 14 (P1): Chu vi hình tam giác
* **Mã bài toán:** `pya_l03_p03_chu_vi_tam_giac`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Đội thi đấu robotics của trường cần thiết kế một tấm chắn bảo vệ hình tam giác cho robot chiến đấu. Ba cạnh của tấm chắn có độ dài lần lượt là $a$, $b$ và $c$ xen-ti-mét. Để mua đủ thanh nhôm gia cố viền ngoài, đội trưởng cần tính chính xác chu vi của tấm chắn tam giác này.
* **Nhiệm vụ:** Nhập 3 số nguyên dương $A, B, C$ trên cùng một dòng. In ra chu vi của bồn hoa đó.
* **Input:** Một dòng chứa 3 số nguyên dương $A, B, C$ ($1 \le A, B, C \le 10^4$).
* **Output:** In ra chu vi hình tam giác.
* **Sample:** ### Input
```text
5 7 8
```
### Output
```text
20
```
### Giải thích
Chu vi $= 5 + 7 + 8 = 20$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 15 (P1): Đổi phút sang giờ và phút
* **Mã bài toán:** `pya_l03_p09_phut_sang_gio_phut`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Tại trung tâm huấn luyện thể thao quốc gia, huấn luyện viên ghi lại thời gian thi đấu của vận động viên bằng tổng số phút (ví dụ: $135$ phút). Để báo cáo lên ban huấn luyện, anh cần quy đổi sang dạng "$X$ giờ $Y$ phút" cho trực quan. Em hãy viết chương trình chuyển đổi từ tổng số phút sang dạng giờ-phút.
* **Nhiệm vụ:** Nhập số nguyên dương $M$ ($1 \le M \le 10^6$). In ra định dạng `X gio Y phut`.
* **Input:** Một dòng chứa số nguyên $M$.
* **Output:** In ra định dạng `X gio Y phut`.
* **Sample:** ### Input
```text
135
```
### Output
```text
2 gio 15 phut
```
### Giải thích
$135 // 60 = 2$ giờ và $135 \% 60 = 15$ phút.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 16 (P1): Tính vận tốc làm tròn
* **Mã bài toán:** `pya_l03_p33_tinh_van_toc_lam_tron`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Cuối tuần, bạn Mít đạp xe đi thăm bà ngoại. Quãng đường từ nhà Mít đến nhà bà dài $D\text{ km}$, và bạn Mít đạp xe hết $T$ giờ. Mẹ dặn bạn Mít phải ghi lại vận tốc trung bình của chuyến đi, làm tròn đến đúng $2$ chữ số sau dấu chấm thập phân. Hãy giúp bạn Mít tính vận tốc của chuyến đi.
* **Nhiệm vụ:** Hãy tính vận tốc trung bình $V = D : T$ (km/h) và in ra kết quả làm tròn đến $2$ chữ số thập phân.
* **Input:** Nhập 2 số trên 2 dòng: quãng đường $D$ ($1 \le D \le 10^4$) và thời gian $T$ ($1 \le T \le 10^4$). Cả hai đều là số nguyên.
* **Output:** Vận tốc trung bình làm tròn đến $2$ chữ số thập phân.
* **Sample:** ### Input
```text
100
6
```
### Output
```text
16.67
```
### Giải thích

- Vận tốc: $100 : 6 = 16.666\ldots$.
- Làm tròn đến $2$ chữ số thập phân được $16.67$ km/h.
* **Ràng buộc:** * **Giới hạn dữ liệu:** $1 \le D, T \le 10^4$
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 17 (P2): Lát gạch sân trường
* **Mã bài toán:** `pya_l03_p25_lat_gach_san_truong`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Sân trường của trường học sinh iKHEDU có hình chữ nhật dài $D\text{ mét}$ và rộng $R\text{ mét}$, nơi các bạn chơi nhảy dây mỗi giờ ra chơi. Hè này, nhà trường muốn lát gạch men cho toàn bộ sân trường bằng các viên gạch hình vuông có cạnh là $K\text{ mét}$ ($D$ và $R$ đều chia hết cho $K$). Bác lao công đã chở gạch đến đầy sân. Hãy giúp bác đếm số viên gạch cần dùng.
* **Nhiệm vụ:** Tính số lượng viên gạch men cần dùng để lát kín mặt sân.
* **Input:** Ba dòng lần lượt chứa 3 số tự nhiên $D, R, K$ ($1 \le K \le R \le D \le 1000$).
* **Output:** Một số nguyên duy nhất là số viên gạch.
* **Sample:** ### Input
```text
20
10
2
```
### Output
```text
50
```
### Giải thích

Diện tích sân: $20 \times 10 = 200$. Diện tích 1 viên gạch: $2 \times 2 = 4$.
Số gạch cần: $200 : 4 = 50$ viên.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 18 (P2): Rào quanh vườn hoa có cửa
* **Mã bài toán:** `pya_l03_p27_rao_quanh_vuon_hoa_co_cua`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bác thợ làm vườn có một vườn hoa rực rỡ hình chữ nhật với chiều dài $a\text{ mét}$, chiều rộng $b\text{ mét}$, thơm ngát mùi hoa hồng. Bác muốn dựng một hàng rào thép gai xung quanh vườn hoa, nhưng chừa lại một lối đi ở một góc vườn làm cổng ra vào rộng đúng $c\text{ mét}$ (không rào cửa).
* **Biết giá thành làm rào:** Mỗi mét hàng rào tốn $15$ nghìn đồng.
Bác đã chuẩn bị tiền nhưng chưa biết có đủ không. Hãy giúp bác tính tổng số tiền mua rào.
* **Nhiệm vụ:** Tính tổng số tiền (nghìn đồng) bác thợ cần dùng để mua đủ rào thép.
* **Input:** Ba dòng lần lượt là $a, b, c$ ($1 \le a, b \le 10^4, 1 \le c < (a + b) * 2$).
* **Output:** Một số nguyên là số tiền (nghìn đồng).
* **Sample:** ### Input
```text
12
8
2
```
### Output
```text
570
```
### Giải thích

Chu vi cả vườn: $(12 + 8) \times 2 = 40\text{ m}$.
Độ dài rào cần mua: $40 - 2 = 38\text{ m}$.
Số tiền: $38 \times 15 = 570$ nghìn đồng.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 19 (P2): Chu vi và diện tích hình chữ nhật
* **Mã bài toán:** `pya_l03_p02_hinh_chu_nhat`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Sân bóng rổ đa năng của trường trung học cơ sở Lê Quý Đôn vừa được tân trang lại. Theo bản đo đạc, sân có chiều dài $A$ mét và chiều rộng $B$ mét. Ban quản lý cơ sở vật chất cần tính chu vi sân để mua đủ lưới rào bảo vệ, đồng thời tính diện tích sân để đặt mua sơn kẻ vạch sân thi đấu theo tiêu chuẩn.
* **Nhiệm vụ:** Nhập hai số nguyên dương $A$ và $B$ trên cùng 1 dòng. In ra chu vi và diện tích của sân bóng rổ trên cùng một dòng cách nhau dấu cách.
* **Input:** Một dòng chứa hai số nguyên dương $A, B$ ($1 \le B \le A \le 10^4$).
* **Output:** In ra chu vi và diện tích.
* **Sample:** ### Input
```text
10 6
```
### Output
```text
32 60
```
### Giải thích
Chu vi $2 \times (10 + 6) = 32$, Diện tích $10 \times 6 = 60$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 20 (P2): Đổi tạ và yến sang kilogram
* **Mã bài toán:** `pya_l03_p07_doi_khoi_luong`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Tại cảng xuất khẩu nông sản Cát Lái, mỗi container hàng ghi trọng lượng bằng đơn vị gam. Tuy nhiên, phiếu hải quan yêu cầu khai báo bằng ki-lô-gam và tấn. Nhân viên kho vận cần một chương trình chuyển đổi nhanh giữa các đơn vị khối lượng: $1$ ki-lô-gam $= 1000$ gam, $1$ tấn $= 1000$ ki-lô-gam. Em hãy giúp họ tự động hóa việc quy đổi.
* **Nhiệm vụ:** Nhập hai số nguyên $T$ và $Y$ trên cùng 1 dòng. In ra tổng khối lượng thóc tính bằng kilogram ($\text{kg}$).
* **Input:** Một dòng chứa hai số nguyên $T, Y$ ($0 \le T, Y \le 1000$).
* **Output:** In ra tổng khối lượng theo $\text{kg}$.
* **Sample:** ### Input
```text
5 3
```
### Output
```text
530
```
### Giải thích
$5\text{ tạ} = 500\text{kg}$, $3\text{ yến} = 30\text{kg}$. Tổng $= 500 + 30 = 530\text{kg}$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 21 (P2): Hàng rào quanh mảnh đất
* **Mã bài toán:** `pya_l03_p32_hang_rao_manh_dat`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bác Năm có mảnh vườn hình chữ nhật dài $A$ mét, rộng $B$ mét. Bác muốn làm hàng rào lưới thép xung quanh, chừa lại một cổng ra vào rộng $C$ mét.
* **Nhiệm vụ:** Nhập 3 số nguyên $A, B, C$ trên cùng 1 dòng ($C < 2 \times (A + B)$). In ra tổng chiều dài hàng rào lưới thép cần mua.
* **Input:** Một dòng chứa 3 số nguyên $A, B, C$ ($1 \le A, B \le 10^4$, $1 \le C \le 100$).
* **Output:** In ra chiều dài hàng rào.
* **Sample:** ### Input
```text
20 15 3
```
### Output
```text
67
```
### Giải thích
Chu vi mảnh vườn $= 2 \times (20 + 15) = 70\text{m}$. Trừ cổng $3\text{m} \implies 70 - 3 = 67\text{m}$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 22 (P2): Bài toán chạy bộ hai người ngược chiều
* **Mã bài toán:** `pya_l03_p18_chay_bo_gap_nhau`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Hai bạn An và Bình ở hai đầu một con đường thẳng dài $S$ mét. Cùng lúc, hai bạn chạy lại phía nhau: An chạy với vận tốc $V_1$ mét/giây, Bình chạy với vận tốc $V_2$ mét/giây.
* **Nhiệm vụ:** Nhập 3 số nguyên $S, V_1, V_2$ trên cùng 1 dòng. In ra thời gian (tính bằng giây) kể từ lúc bắt đầu chạy cho đến khi hai bạn gặp nhau, làm tròn 1 chữ số thập phân.
* **Input:** Một dòng chứa 3 số nguyên dương $S, V_1, V_2$ ($1 \le S \le 10^5$, $1 \le V_1, V_2 \le 100$).
* **Output:** In ra thời gian gặp nhau dạng `f"{t:.1f}"`.
* **Sample:** ### Input
```text
150 2 3
```
### Output
```text
30.0
```
### Giải thích
Vận tốc tiếp cận $= 2 + 3 = 5\text{m/s}$. Thời gian gặp nhau $= 150 / 5 = 30.0$ giây.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 23 (P2): Diện tích tam giác vuông
* **Mã bài toán:** `pya_l03_p22_dien_tich_tam_giac_vuong`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Kiến trúc sư Hà đang thiết kế một khu vườn trang trí trước sảnh tòa nhà văn phòng. Khu vườn có dạng hình tam giác vuông với hai cạnh góc vuông lần lượt dài $a$ mét và $b$ mét. Để ước tính lượng cỏ nhân tạo cần trải và chi phí thi công, cô cần tính chính xác diện tích khu vườn tam giác vuông này.
* **Nhiệm vụ:** Nhập hai số nguyên dương $A, B$ trên cùng 1 dòng. In ra diện tích lá cờ dưới dạng số thực lấy đúng 1 chữ số thập phân.
* **Input:** Một dòng chứa hai số nguyên $A, B$ ($1 \le A, B \le 10^4$).
* **Output:** In ra diện tích định dạng `f"{S:.1f}"`.
* **Sample:** ### Input
```text
5 7
```
### Output
```text
17.5
```
### Giải thích
Diện tích $= (5 \times 7) / 2 = 17.5$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 24 (P2): Đổi giờ - phút - giây sang tổng số giây
* **Mã bài toán:** `pya_l03_p29_doi_sang_tong_giay`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bài toán ngược lại: Cần quy đổi thời gian hiển thị `H giờ M phút S giây` về một số giây duy nhất để máy tính dễ so sánh.
* **Nhiệm vụ:** Nhập 3 số nguyên $H, M, S$ trên cùng 1 dòng ($0 \le H \le 1000$, $0 \le M, S < 60$). In ra tổng số giây.
* **Input:** Một dòng chứa 3 số nguyên $H, M, S$.
* **Output:** In ra một số nguyên là tổng số giây.
* **Sample:** ### Input
```text
2 15 30
```
### Output
```text
8130
```
### Giải thích
$2 \times 3600 + 15 \times 60 + 30 = 7200 + 900 + 30 = 8130$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 25 (P3): Tính tiền mua sơn quét tường
* **Mã bài toán:** `pya_l03_p17_son_tuong_phong`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Một bức tường hình chữ nhật có chiều dài $A$ mét và chiều cao $H$ mét. Trên tường có một cửa sổ hình chữ nhật kích thước $X \times Y$ mét không cần quét sơn. Biết mỗi mét vuông tường tốn $G$ đồng tiền sơn.
* **Nhiệm vụ:** Nhập 5 số nguyên $A, H, X, Y, G$ trên cùng 1 dòng. In ra tổng số tiền sơn cần chuẩn bị.
* **Input:** Một dòng chứa 5 số nguyên dương ($X < A, Y < H$, $1 \le A, H \le 100$, $1 \le G \le 10^5$).
* **Output:** In ra tổng số tiền sơn.
* **Sample:** ### Input
```text
6 3 2 1 50000
```
### Output
```text
800000
```
### Giải thích
Diện tích tường $= 6 \times 3 = 18\text{m}^2$. Diện tích cửa sổ $= 2 \times 1 = 2\text{m}^2$. Diện tích cần sơn $= 18 - 2 = 16\text{m}^2$. Tổng tiền $= 16 \times 50000 = 800000$ đồng.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 26 (P3): Diện tích hình thang
* **Mã bài toán:** `pya_l03_p05_dien_tich_hinh_thang`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Thửa ruộng nhà ông Ba ở Cần Thơ có hình dạng hình thang cân, với đáy lớn dài $a$ mét, đáy nhỏ dài $b$ mét và chiều cao $h$ mét. Cuối vụ mùa, hợp tác xã cần tính diện tích thửa ruộng để quy đổi sản lượng lúa thu hoạch trên mỗi mét vuông và lập báo cáo năng suất nông nghiệp.
* **Nhiệm vụ:** Nhập 3 số nguyên dương $A, B, H$ trên cùng một dòng. In ra diện tích thửa ruộng dưới dạng số thực lấy đúng 1 chữ số thập phân.
* **Input:** Một dòng chứa 3 số nguyên $A, B, H$ ($1 \le B \le A \le 10^4$, $1 \le H \le 10^4$).
* **Output:** In ra diện tích định dạng `f"{S:.1f}"`.
* **Sample:** ### Input
```text
12 8 5
```
### Output
```text
50.0
```
### Giải thích
Diện tích $= ((12 + 8) \times 5) / 2 = 50.0$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 27 (P3): Tính vận tốc trung bình
* **Mã bài toán:** `pya_l03_p26_van_toc_trung_binh`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Xe buýt tuyến 01 khởi hành từ bến xe Miền Đông đi bến xe Miền Tây, quãng đường dài $S$ ki-lô-mét và xe chạy hết $T$ giờ (kể cả thời gian dừng đón trả khách). Công ty vận tải cần tính vận tốc trung bình thực tế của chuyến xe để đánh giá hiệu suất và điều chỉnh lịch trình cho phù hợp.
* **Nhiệm vụ:** Nhập hai số nguyên $S$ và $T$ ($1 \le T \le 100$, $1 \le S \le 10^5$). In ra vận tốc trung bình của ô tô làm tròn 2 chữ số thập phân.
* **Input:** Một dòng chứa $S$ và $T$.
* **Output:** In ra vận tốc dạng `f"{v:.2f}"` (đơn vị $\text{km/h}$).
* **Sample:** ### Input
```text
100 3
```
### Output
```text
33.33
```
### Giải thích
$100 / 3 \approx 33.3333... \implies 33.33$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 28 (P3): Đổi giây sang giờ phút giây
* **Mã bài toán:** `pya_l03_p24_doi_giay_sang_gio_phut_giay`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong hệ thống theo dõi quỹ đạo trạm không gian, đồng hồ đo ghi nhận thời gian hoàn thành một vòng quỹ đạo là tổng cộng $S$ giây. Hệ thống cần hiển thị giá trị này dưới dạng tường minh: gồm bao nhiêu giờ ($H$), bao nhiêu phút ($M$) và bao nhiêu giây ($S$).
* **Nhiệm vụ:** Nhập vào tổng số giây $S$. Hãy phân rã thành $H$ giờ, $M$ phút, $S$ giây.
* **Input:** Một số nguyên $S$ ($0 \le S \le 10^8$).
* **Output:** In ra ba số nguyên $H, M, S$ cách nhau một khoảng trắng.
* **Sample:** ### Input
```text
3665
```
### Output
```text
1 1 5
```
### Giải thích

3665 giây = 1 giờ (3600s) + 1 phút (60s) + 5 giây.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 29 (P3): Khoảng thời gian giữa hai thời điểm trong ngày
* **Mã bài toán:** `pya_l03_p12_khoang_cach_thoi_gian`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Minh bắt đầu học bài lúc $H_1$ giờ $M_1$ phút và kết thúc lúc $H_2$ giờ $M_2$ phút (trong cùng một ngày).
* **Nhiệm vụ:** Nhập 4 số nguyên $H_1, M_1, H_2, M_2$ trên 1 dòng. In ra khoảng thời gian học tính theo đơn vị phút.
* **Input:** Một dòng chứa 4 số nguyên ($0 \le H_1 \le H_2 \le 23$, $0 \le M_1, M_2 < 60$, thời điểm 2 không sớm hơn thời điểm 1).
* **Output:** In ra số phút chênh lệch.
* **Sample:** ### Input
```text
8 30 10 15
```
### Output
```text
105
```
### Giải thích
Từ 8h30 đến 10h15 là 1 giờ 45 phút $= 60 + 45 = 105$ phút.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 30 (P3): Lát nền phòng học
* **Mã bài toán:** `pya_l03_p15_lat_gach_nen_nha`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Phòng học hình chữ nhật có chiều dài $L$ mét và chiều rộng $W$ mét. Người ta dùng các viên gạch hoa hình vuông cạnh $D$ centimet để lát nền.
* **Nhiệm vụ:** Nhập 3 số nguyên dương $L, W, D$ trên cùng 1 dòng ($L, W$ tính bằng mét, $D$ tính bằng centimet). Giả sử phòng học vừa khít các viên gạch, hãy in ra tổng số viên gạch cần dùng.
* **Input:** Một dòng chứa 3 số nguyên $L, W, D$ ($1 \le L, W \le 100$, $10 \le D \le 100$).
* **Output:** In ra số viên gạch cần dùng.
* **Sample:** ### Input
```text
6 4 50
```
### Output
```text
96
```
### Giải thích
Đổi $L = 600\text{cm}, W = 400\text{cm}$. Diện tích sàn $= 600 \times 400 = 240000\text{cm}^2$. Diện tích 1 viên gạch $= 50 \times 50 = 2500\text{cm}^2$. Số gạch $= 240000 // 2500 = 96$ viên.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 31 (P3): Đổi tổng số giây sang giờ, phút, giây
* **Mã bài toán:** `pya_l03_p28_doi_giay_sang_gio_phut_giay`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Đồng hồ bấm giờ trong cuộc thi chạy marathon ghi nhận tổng thời gian là $T$ giây.
* **Nhiệm vụ:** Nhập số nguyên dương $T$ ($1 \le T \le 10^9$). In ra theo định dạng `H:M:S`.
* **Input:** Một dòng chứa số nguyên $T$.
* **Output:** In ra chuỗi `H:M:S` (với $H$ là giờ, $M$ là phút, $S$ là giây).
* **Sample:** ### Input
```text
3665
```
### Output
```text
1:1:5
```
### Giải thích
1 giờ 1 phút 5 giây.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 32 (P3): Điểm trung bình môn học
* **Mã bài toán:** `pya_l03_p13_diem_trung_binh`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Cuối học kỳ, hệ thống quản lý điểm số của trường tự động tính điểm trung bình từ các bài kiểm tra. Một học sinh có điểm ba môn chính lần lượt là $a$, $b$ và $c$. Điểm trung bình được tính bằng công thức $\text{TB} = \frac{a + b + c}{3}$. Em hãy lập trình tính điểm trung bình và in kết quả với số thập phân chính xác.
* **Nhiệm vụ:** Nhập 3 số thực là điểm của 3 môn trên cùng 1 dòng. In ra điểm trung bình cộng làm tròn đúng 2 chữ số thập phân.
* **Input:** Một dòng chứa 3 số thực ($0 \le d_1, d_2, d_3 \le 10$).
* **Output:** In ra điểm trung bình dạng `f"{dtb:.2f}"`.
* **Sample:** ### Input
```text
8.5 9.0 7.5
```
### Output
```text
8.33
```
### Giải thích
$(8.5 + 9.0 + 7.5) / 3 = 25.0 / 3 \approx 8.3333... \implies 8.33$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 33 (P3): Diện tích lối đi quanh hồ nước
* **Mã bài toán:** `pya_l03_p16_loi_di_quanh_ho`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Trong công viên có một hồ nước hình chữ nhật kích thước dài $A$ mét, rộng $B$ mét. Xung quanh hồ, người ta làm một lối đi dạo có bề rộng đồng đều là $D$ mét.
* **Nhiệm vụ:** Nhập 3 số nguyên $A, B, D$ trên cùng 1 dòng. Hãy tính diện tích của lối đi dạo đó.
* **Input:** Một dòng chứa 3 số nguyên $A, B, D$ ($1 \le A, B \le 10^4$, $1 \le D \le 100$).
* **Output:** In ra diện tích lối đi.
* **Sample:** ### Input
```text
10 8 2
```
### Output
```text
88
```
### Giải thích
Kích thước cả hồ và lối đi là $(10 + 2 \times 2) = 14\text{m}$ và $(8 + 2 \times 2) = 12\text{m}$. Diện tích toàn phần $= 14 \times 12 = 168\text{m}^2$. Diện tích hồ $= 10 \times 8 = 80\text{m}^2$. Diện tích lối đi $= 168 - 80 = 88\text{m}^2$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---
