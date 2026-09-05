# Danh Sách Bài Tập Thực Hành: Bài 14: Duyệt chuỗi và tách từ

> Nguồn problems: l14, l15 | Tổng 24 bài (sắp từ dễ đến khó theo rubric độ khó).

## Ma Trận Phân Tầng
* P0 (Khởi động): Bài 1-6
* P1 (Cơ bản): Bài 7-12
* P2 (Luyện tập): Bài 13-18
* P3 (Vận dụng): Bài 19-24
---

### Bài 1 (P0): Chuyển toàn bộ thành chữ hoa
* **Mã bài toán:** `pya_l14_p02_chuyen_toan_bo_thanh_chu_hoa`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Chuẩn hóa toàn bộ văn bản sang dạng chữ in hoa giúp việc đối sánh chuỗi trong các cơ sở dữ liệu không bị ảnh hưởng bởi quy cách gõ phím.
* **Nhiệm vụ:** Nhập một dòng văn bản $S$. Hãy chuyển tất cả các chữ cái trong $S$ thành chữ in hoa và in ra màn hình.
* **Input:** Một dòng văn bản $S$.
* **Output:** Chuỗi sau khi đã in hoa toàn bộ.
* **Sample:** ### Input
```text
ikhedu vietnam
```
### Output
```text
IKHEDU VIETNAM
```
### Giải thích

Với dữ liệu đầu vào là `ikhedu vietnam`, kết quả thu được tương ứng là `IKHEDU VIETNAM`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 2 (P0): Thay thế ký tự bí mật
* **Mã bài toán:** `pya_l14_p08_thay_the_ky_tu_bi_mat`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Để chuẩn hóa định dạng văn bản cho đường dẫn liên kết, hệ thống cần thay thế toàn bộ khoảng trống bằng ký tự gạch dưới phân tách.
* **Nhiệm vụ:** Nhập một chuỗi $S$. Hãy thay thế tất cả các ký tự khoảng trắng `" "` trong $S$ bằng dấu gạch dưới `"_"` và in ra kết quả.
* **Input:** Một chuỗi $S$.
* **Output:** Chuỗi sau khi thay thế.
* **Sample:** ### Input
```text
hoc lap trinh de vui
```
### Output
```text
hoc_lap_trinh_de_vui
```
### Giải thích

Với dữ liệu đầu vào là `hoc lap trinh de vui`, kết quả thu được tương ứng là `hoc_lap_trinh_de_vui`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 3 (P0): Xóa bỏ toàn bộ dấu cách
* **Mã bài toán:** `pya_l14_p09_xoa_bo_toan_bo_dau_cach`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Loại bỏ toàn bộ khoảng trắng thừa giúp nén kích thước chuỗi và chuẩn hóa dữ liệu khóa tìm kiếm.
* **Nhiệm vụ:** Cho một dòng văn bản $S$. Hãy xóa bỏ tất cả các ký tự khoảng trắng trong chuỗi để thu được một chuỗi viết liền hoàn toàn.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 10^5$).
* **Output:** Chuỗi viết liền không còn khoảng trắng.
* **Sample:** ### Input
```text
Lap Trinh Python Bang A
```
### Output
```text
LapTrinhPythonBangA
```
### Giải thích

Với dữ liệu đầu vào là `Lap Trinh Python Bang A`, kết quả thu được tương ứng là `LapTrinhPythonBangA`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 4 (P0): Mã ASCII của ký tự
* **Mã bài toán:** `pya_l15_p03_ma_ascii_cua_ky_tu`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Mỗi ký tự hiển thị trên máy tính đều được mã hóa bằng một số nguyên duy nhất theo chuẩn ASCII. Việc tra cứu mã này là kiến thức cốt lõi về biểu diễn dữ liệu.
* **Nhiệm vụ:** Nhập một ký tự bất kỳ từ bàn phím. Hãy in ra mã số ASCII của ký tự đó.
* **Input:** Một ký tự duy nhất $C$.
* **Output:** Một số nguyên là mã ASCII.
* **Sample:** ### Input
```text
A
```
### Output
```text
65
```
### Giải thích

Với dữ liệu đầu vào là `A`, kết quả thu được tương ứng là `65`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 5 (P0): Đếm số từ trong câu
* **Mã bài toán:** `pya_l15_p01_dem_so_tu_trong_cau`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Đếm số lượng từ trong một đoạn văn bản là chỉ số cơ bản nhất của các phần mềm xử lý soạn thảo và phân tích ngôn ngữ tự nhiên.
* **Nhiệm vụ:** Nhập một dòng văn bản $S$ có thể chứa nhiều khoảng trắng thừa ở đầu, cuối hoặc giữa các từ. Hãy đếm xem câu văn đó có bao nhiêu từ.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng từ trong câu.
* **Sample:** ### Input
```text
 Chuc mung nam moi 
```
### Output
```text
4
```
### Giải thích

Có 4 từ: 'Chuc', 'mung', 'nam', 'moi'.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 6 (P0): Tìm từ dài nhất trong câu
* **Mã bài toán:** `pya_l15_p05_tim_tu_dai_nhat_trong_cau`
* **Độ khó:** P0 (Khởi động)
* **Bối cảnh:** Thí sinh đang tìm kiếm một giá trị đặc biệt trong tập dữ liệu. Hãy viết chương trình tìm kiếm hiệu quả.
* **Nhiệm vụ:** Cho một câu văn $S$. Hãy tìm và in ra từ có độ dài dài nhất trong câu. Nếu có nhiều từ cùng độ dài dài nhất, in ra từ đầu tiên xuất hiện.
* **Input:** Một dòng văn bản $S$.
* **Output:** Từ dài nhất tìm được.
* **Sample:** ### Input
```text
Hoc lap trinh rat thu vi
```
### Output
```text
trinh
```
### Giải thích

Từ 'trinh' có 5 chữ cái (dài nhất).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 7 (P1): Ký tự kế tiếp trong bảng chữ cái
* **Mã bài toán:** `pya_l15_p04_ky_tu_ke_tiep_trong_bang_chu_cai`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Xác định ký tự liền sau trong bảng chữ cái dựa trên phép tịnh tiến mã số ASCII là nền tảng của nhiều thuật toán sinh khóa và mã hóa cổ điển.
* **Nhiệm vụ:** Nhập vào một chữ cái in hoa từ `'A'` đến `'Y'`. Hãy in ra chữ cái đứng ngay liền sau nó trong bảng chữ cái tiếng Anh.
* **Input:** Một ký tự in hoa $C \in ['A' \dots 'Y']$.
* **Output:** Chữ cái liền sau.
* **Sample:** ### Input
```text
C
```
### Output
```text
D
```
### Giải thích

Với dữ liệu đầu vào là `C`, kết quả thu được tương ứng là `D`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 8 (P1): Từ đầu tiên & từ cuối cùng
* **Mã bài toán:** `pya_l15_p02_tu_dau_tien_tu_cuoi_cung`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Trích xuất từ mở đầu và từ kết thúc hỗ trợ xác định cấu trúc ngữ pháp và tiêu đề của một câu lệnh truy vấn.
* **Nhiệm vụ:** Cho một câu văn $S$. Hãy in ra từ đầu tiên và từ cuối cùng của câu văn đó trên 2 dòng riêng biệt.
* **Input:** Một dòng văn bản có ít nhất 1 từ.
* **Output:** Dòng 1 in từ đầu tiên, dòng 2 in từ cuối cùng.
* **Sample:** ### Input
```text
Hoc Python cuc vui
```
### Output
```text
Hoc
vui
```
### Giải thích

Với dữ liệu đầu vào là `Hoc Python cuc vui`, kết quả thu được tương ứng là `Hoc
vui`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 9 (P1): Chuẩn hóa khoảng trắng
* **Mã bài toán:** `pya_l15_p06_chuan_hoa_khoang_trang`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Na tập đánh máy để viết thiệp mời sinh nhật cho cả lớp. Khi đánh máy, một bạn học sinh lỡ tay bấm rất nhiều dấu cách thừa giữa các từ và ở hai đầu câu văn. Tấm thiệp trông rời rạc và chưa đẹp mắt chút nào. Hãy giúp Na dọn dẹp tấm thiệp cho gọn gàng.
* **Nhiệm vụ:** Cho chuỗi văn bản $S$. Hãy chuẩn hóa câu văn sao cho: không còn khoảng trắng ở đầu và cuối câu, giữa mỗi từ chỉ có duy nhất **một dấu cách**.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Câu văn chuẩn hóa.
* **Sample:** ### Input
```text
 Python rat la tuyet 
```
### Output
```text
Python rat la tuyet
```
### Giải thích

Với dữ liệu đầu vào là `Python rat la tuyet`, kết quả thu được tương ứng là `Python rat la tuyet`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 10 (P1): In từng chữ cái xuống dòng
* **Mã bài toán:** `pya_l14_p01_in_tung_chu_cai_xuong_dong`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Duyệt tuần tự qua từng ký tự của văn bản là thao tác nền tảng để phân tích cú pháp và kiểm định luồng dữ liệu ký tự.
* **Nhiệm vụ:** Nhập vào một từ $S$. Hãy in ra từng chữ cái của từ đó, mỗi chữ cái nằm trên một dòng riêng biệt.
* **Input:** Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).
* **Output:** Mỗi ký tự trên một dòng.
* **Sample:** ### Input
```text
CAT
```
### Output
```text
C
A
T
```
### Giải thích

Với dữ liệu đầu vào là `CAT`, kết quả thu được tương ứng là `C
A
T`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 11 (P1): Viết hoa chữ cái đầu mỗi từ (title case)
* **Mã bài toán:** `pya_l15_p07_viet_hoa_chu_cai_dau_moi_tu_title_case`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Quy tắc viết hoa chữ cái đầu mỗi từ là chuẩn mực định dạng bắt buộc khi lưu trữ danh tính người dùng trong hệ thống cơ sở dữ liệu.
* **Nhiệm vụ:** Nhập họ và tên của một bạn học sinh viết chưa đúng quy tắc (ví dụ: `nguyen van an`). Hãy chuẩn hóa họ tên bằng cách viết hoa chữ cái đầu tiên của mỗi từ và viết thường các chữ cái còn lại.
* **Input:** Một chuỗi họ tên.
* **Output:** Họ tên sau khi chuẩn hóa.
* **Sample:** ### Input
```text
nguyen van an
```
### Output
```text
Nguyen Van An
```
### Giải thích

Với dữ liệu đầu vào là `nguyen van an`, kết quả thu được tương ứng là `Nguyen Van An`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 12 (P1): Đảo ngược từng từ trong câu
* **Mã bài toán:** `pya_l15_p08_dao_nguoc_tung_tu_trong_cau`
* **Độ khó:** P1 (Cơ bản)
* **Bối cảnh:** Đảo ngược các ký tự nội bộ của từng từ trong khi vẫn bảo toàn thứ tự các từ trong câu là bài toán rèn luyện kỹ năng kết hợp tách từ và cắt lát chuỗi.
* **Nhiệm vụ:** Cho một câu văn. Hãy đảo ngược thứ tự các chữ cái trong từng từ một, nhưng giữ nguyên vị trí của các từ trong câu.
* **Input:** Một dòng văn bản.
* **Output:** Câu văn mới với từng từ bị đảo ngược.
* **Sample:** ### Input
```text
Toi yeu Viet Nam
```
### Output
```text
ioT uey teiV maN
```
### Giải thích

'Toi' -> 'ioT', 'yeu' -> 'uey'...
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 13 (P2): Mật mã thay thế hoán vị (anagram)
* **Mã bài toán:** `pya_l15_p12_mat_ma_thay_the_hoan_vi_anagram`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Trong giờ thủ công, hai bạn cùng xáo trộn các thẻ chữ cái để xếp thành từ mới. Hai từ được gọi là "Anagram" (hoán vị ký tự của nhau) nếu chúng có thể tạo thành từ nhau bằng cách xáo trộn lại thứ tự các chữ cái (ví dụ: `silent` và `listen`, `heart` và `earth`). Cả lớp thi xem ai xếp được cặp từ trùng khớp nhau. Hãy giúp các bạn kiểm tra xem hai từ có phải Anagram không.
* **Nhiệm vụ:** Cho 2 từ $S_1$ và $S_2$. Kiểm tra xem chúng có phải là Anagram của nhau không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Hai dòng, mỗi dòng chứa một từ viết thường ($1 \le |S_1|, |S_2| \le 10^5$).
* **Output:** `YES` hoặc `NO`.
* **Sample:** ### Input
```text
listen
silent
```
### Output
```text
YES
```
### Giải thích

Với dữ liệu đầu vào là `listen
silent`, kết quả thu được tương ứng là `YES`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 14 (P2): Từ xuất hiện nhiều nhất trong đoạn
* **Mã bài toán:** `pya_l15_p11_tu_xuat_hien_nhieu_nhat_trong_doan`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Tìm từ xuất hiện với tần suất cao nhất trong một văn bản là bài toán quan trọng trong trích xuất từ khóa và khai phá dữ liệu văn bản.
* **Nhiệm vụ:** Cho một đoạn văn bản chỉ gồm các từ cách nhau bởi khoảng trắng. Hãy tìm xem từ nào xuất hiện nhiều lần nhất trong đoạn văn đó và xuất hiện bao nhiêu lần. Dữ liệu đảm bảo chỉ có 1 từ xuất hiện nhiều nhất.
* **Input:** Một đoạn văn bản $S$ gồm các chữ cái viết thường.
* **Output:** Từ xuất hiện nhiều nhất và số lần xuất hiện, cách nhau một khoảng trắng.
* **Sample:** ### Input
```text
cam quyt mit dua cam xoai cam dua
```
### Output
```text
cam 3
```
### Giải thích

Với dữ liệu đầu vào là `cam quyt mit dua cam xoai cam dua`, kết quả thu được tương ứng là `cam 3`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 15 (P2): Đếm số lượng nguyên âm
* **Mã bài toán:** `pya_l14_p10_dem_so_luong_nguyen_am`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Trong giờ tiếng Anh, cô giáo dạy cả lớp bài hát về các chữ cái vui nhộn. Cô nói trong tiếng Anh, 5 chữ cái: `A, E, I, O, U` (cả hoa lẫn thường) được gọi là nguyên âm (vowels). Bạn nào đếm đúng số nguyên âm trong một từ sẽ được hát trước cả lớp. Hãy giúp cả lớp đếm số nguyên âm thật nhanh.
* **Nhiệm vụ:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu ký tự nguyên âm trong chuỗi $S$.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng nguyên âm.
* **Sample:** ### Input
```text
EDUCATION
```
### Output
```text
5
```
### Giải thích

Các nguyên âm: E, U, A, I, O (có 5 nguyên âm).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 16 (P2): Đếm ký tự 'A' (cả hoa lẫn thường)
* **Mã bài toán:** `pya_l14_p03_dem_ky_tu_a_ca_hoa_lan_thuong`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Thống kê tần suất xuất hiện của một chữ cái cụ thể (không phân biệt hoa thường) là thao tác căn bản trong phân tích văn bản ngôn ngữ.
* **Nhiệm vụ:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu chữ cái `'A'` hoặc `'a'` xuất hiện trong chuỗi $S$.
* **Input:** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng chữ cái 'A' hoặc 'a'.
* **Sample:** ### Input
```text
An va Ba hoc bai
```
### Output
```text
4
```
### Giải thích

Gồm chữ 'A' (1 lần) và 'a' (3 lần trong 'va', 'Ba', 'bai').
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 17 (P2): Tính tổng các chữ số trong chuỗi
* **Mã bài toán:** `pya_l14_p06_tinh_tong_cac_chu_so_trong_chuoi`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Trong bài kiểm tra, người dùng cần tính nhanh tổng một dãy số. Hãy viết chương trình hỗ trợ tính toán.
* **Nhiệm vụ:** Cho một chuỗi văn bản $S$. Hãy tính tổng giá trị của tất cả các chữ số xuất hiện trong chuỗi đó.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 10^5$).
* **Output:** Một số nguyên duy nhất là tổng các chữ số.
* **Sample:** ### Input
```text
A1B2C3D4
```
### Output
```text
10
```
### Giải thích

$1 + 2 + 3 + 4 = 10$.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 18 (P2): Tách riêng chữ số ra khỏi văn bản
* **Mã bài toán:** `pya_l14_p05_tach_rieng_chu_so_ra_khoi_van_ban`
* **Độ khó:** P2 (Luyện tập)
* **Bối cảnh:** Bạn An nhận được một bức thư mật mã, trong đó có các chữ số bị giấu lẫn vào giữa các chữ cái. An phải thật tinh mắt mới thấy những con số trốn kỹ trong dòng chữ. Cả nhóm bạn quyết tâm nhặt hết các chữ số ra để đọc mật thư. Hãy giúp bạn An nhặt hết các chữ số bí mật này.
* **Nhiệm vụ:** Cho chuỗi $S$. Hãy nhặt ra toàn bộ các ký tự là chữ số ('0' - '9') và ghép chúng lại theo thứ tự ban đầu để in ra màn hình. Nếu không có chữ số nào, in ra `KHONG CO`.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Chuỗi các chữ số ghép lại, hoặc `KHONG CO`.
* **Sample:** ### Input
```text
Toi sinh nam 2014 vao thang 08
```
### Output
```text
201408
```
### Giải thích

Với dữ liệu đầu vào là `Toi sinh nam 2014 vao thang 08`, kết quả thu được tương ứng là `201408`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 19 (P3): Nén chuỗi ký tự (Run-Length encoding)
* **Mã bài toán:** `pya_l14_p11_nen_chuoi_ky_tu_runlength_encoding`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Nam gấp thật nhiều ngôi sao giấy cùng màu rồi xếp chúng thành hàng dài trên bàn. Cô giáo dạy thuật toán nén chuỗi đơn giản thay thế một dãy các ký tự giống nhau liên tiếp bằng ký tự đó kèm theo số lần lặp lại.
 Ví dụ: `AAABBC` nén thành `A3B2C1`.
Nam muốn ghi lại hàng ngôi sao thật gọn vào sổ. Hãy giúp bạn Nam viết chương trình nén chuỗi thật gọn.
* **Nhiệm vụ:** Cho một chuỗi $S$ chỉ gồm các chữ cái in hoa. Hãy in ra dạng nén của chuỗi $S$.
* **Input:** Một chuỗi $S$ ($1 \le |S| \le 1000$).
* **Output:** Chuỗi sau khi nén.
* **Sample:** ### Input
```text
AAABBCCCC
```
### Output
```text
A3B2C4
```
### Giải thích

Với dữ liệu đầu vào là `AAABBCCCC`, kết quả thu được tương ứng là `A3B2C4`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 20 (P3): Đếm chữ cái in hoa & in thường
* **Mã bài toán:** `pya_l14_p04_dem_chu_cai_in_hoa_in_thuong`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Đo lường tỉ lệ giữa chữ cái in hoa và in thường giúp hệ thống tự động đánh giá độ phức tạp và độ an toàn của mật khẩu.
* **Nhiệm vụ:** Cho một chuỗi $S$. Hãy đếm xem có bao nhiêu chữ cái in hoa và bao nhiêu chữ cái in thường trong chuỗi đó.
* **Input:** Chuỗi ký tự $S$.
* **Output:** Hai số nguyên cách nhau một khoảng trắng: số lượng chữ in hoa trước, số lượng chữ in thường sau.
* **Sample:** ### Input
```text
Lap Trinh Python
```
### Output
```text
3 11
```
### Giải thích

Chữ in hoa: 'L', 'T', 'P' (3 chữ).
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 21 (P3): Mật mã Caesar dịch chuyển K
* **Mã bài toán:** `pya_l15_p09_mat_ma_caesar_dich_chuyen_k`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Bạn Bin và cả nhóm chơi trò điệp viên gửi thư bí mật cho nhau trong sân trường. Hoàng đế Caesar mã hóa bức thư gồm các chữ cái in hoa (`'A'` đến `'Z'`) bằng cách dịch chuyển mỗi chữ cái sang phải $K$ bước theo vòng tròn 26 chữ cái ($A \to B \dots Z \to A$). Cả nhóm háo hức muốn tự mã hóa thư của riêng mình. Hãy giúp bạn Bin viết chương trình mã hóa thư.
* **Nhiệm vụ:** Cho chuỗi $S$ chỉ gồm các chữ cái in hoa và số nguyên $K$ ($1 \le K \le 25$). Hãy in ra bản mật mã sau khi mã hóa.
* **Input:** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.
* **Output:** Chuỗi sau khi mã hóa.
* **Sample:** ### Input
```text
ABCXYZ
3
```
### Output
```text
DEFABC
```
### Giải thích

'A'->'D', 'B'->'E', 'X'->'A', 'Y'->'B', 'Z'->'C'.
* **Công thức toán học:** `chr((ord(ch) - ord('A') + k) % 26 + ord('A'))`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 22 (P3): Giải mã mật thư Caesar
* **Mã bài toán:** `pya_l15_p10_giai_ma_mat_thu_caesar`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Mật mã Caesar là một trong những phương pháp mã hóa thay thế lâu đời nhất, hoạt động bằng cách dịch chuyển từng chữ cái trong bảng mã theo một bước nhảy cố định.
* **Nhiệm vụ:** Cho một bản mật mã $S$ (chỉ gồm các chữ cái in hoa) đã bị mã hóa Caesar với bước nhảy $K$. Hãy giải mã để tìm lại thông điệp ban đầu.
* **Input:** Dòng 1 chứa bản mật mã $S$. Dòng 2 chứa số nguyên $K$ ($1 \le K \le 25$).
* **Output:** Thông điệp ban đầu trước khi mã hóa.
* **Sample:** ### Input
```text
DEFABC
3
```
### Output
```text
ABCXYZ
```
### Giải thích

Với dữ liệu đầu vào là `DEFABC
3`, kết quả thu được tương ứng là `ABCXYZ`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 23 (P3): Đổi chữ hoa thành thường & ngược lại
* **Mã bài toán:** `pya_l14_p07_doi_chu_hoa_thanh_thuong_nguoc_lai`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Đảo ngược trạng thái viết hoa và viết thường trên toàn bộ văn bản là thao tác chuyển đổi định dạng thường gặp trong các trình biên tập mã nguồn.
* **Nhiệm vụ:** Cho chuỗi ký tự $S$. Hãy biến đổi chuỗi bằng quy tắc: chữ hoa đổi thành chữ thường, chữ thường đổi thành chữ hoa, các ký tự khác (số, dấu câu, khoảng trắng) giữ nguyên.
* **Input:** Một chuỗi văn bản $S$.
* **Output:** Chuỗi sau khi biến đổi.
* **Sample:** ### Input
```text
Hello World 123
```
### Output
```text
hELLO wORLD 123
```
### Giải thích

Với dữ liệu đầu vào là `Hello World 123`, kết quả thu được tương ứng là `hELLO wORLD 123`.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---

### Bài 24 (P3): Trích xuất số lớn nhất trong văn bản
* **Mã bài toán:** `pya_l14_p12_trich_xuat_so_lon_nhat_trong_van_ban`
* **Độ khó:** P3 (Vận dụng)
* **Bối cảnh:** Lớp trưởng ghi một bài báo cáo, trong đó có các con số nằm rải rác giữa các câu chữ. Một con số có thể có nhiều chữ số liên tiếp nhau. Cả lớp muốn biết con số nào to nhất để khen bạn được điểm cao. Hãy giúp lớp trưởng tìm ra con số lớn nhất trong bài báo cáo.
* **Nhiệm vụ:** Cho chuỗi văn bản $S$. Hãy tìm và in ra giá trị của **con số nguyên lớn nhất** xuất hiện trong chuỗi đó. Dữ liệu đảm bảo có ít nhất 1 chữ số.
* **Input:** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số nguyên lớn nhất tìm được.
* **Sample:** ### Input
```text
Lop 5A co 38 hoc sinh va 105 quyen sach
```
### Output
```text
105
```
### Giải thích

Các con số xuất hiện là: 5, 38, 105. Số lớn nhất là 105.
* **Ràng buộc:** * **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$

---
