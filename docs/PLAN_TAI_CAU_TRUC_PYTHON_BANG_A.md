# Kế hoạch tái cấu trúc và biên soạn sách giáo trình: iKHEDU Python Bảng A
**Khóa học: Nền tảng lập trình Python & tư duy thuật toán thi đấu Bảng A**  
*Mã khóa học: `python-bang-a-level1` | File quản trị: `docs/PLAN_TAI_CAU_TRUC_PYTHON_BANG_A.md`*

---

## 1. Phân tích yêu cầu & định hướng nội dung bài học giáo trình

### 1.1. Bản chất "Nội dung bài học" vs "Bài giảng / Slide note"
- **Hiện trạng cũ**: Nội dung mang phong cách tóm tắt slide bài giảng (gạch vài đầu dòng, đưa vài cú pháp ngắn rồi chuyển ngay sang quiz / bài tập). Học sinh đọc vào không hiểu được bản chất kỹ thuật, không tự học và tự suy luận được.
- **Quy chuẩn mới**: Toàn bộ nội dung bài học trong `LessonXX_Production_Content.md` phải là **văn phong sách giáo trình học thuật chuẩn mực, trực diện, khoa học**, tuyệt đối không văn thơ hoa mỹ, không viết hoa chữ cái đầu vô tội vạ, tập trung vào bản chất máy tính:
  1. **Khái niệm & bản chất khoa học máy tính**: Định nghĩa trực diện, chính xác, nêu rõ tại sao cần công cụ này trong lập trình.
  2. **Cú pháp, quy tắc & bảng phân loại**: Chia tách chi tiết từng thành phần của câu lệnh, toán tử, biểu thức.
  3. **Hình ảnh minh họa trực quan (SVG diagram)**: Nhúng trực tiếp sơ đồ kiến trúc, luồng I/O, mô hình ô nhớ RAM, sơ đồ rẽ nhánh và vòng lặp.
  4. **Bảng mô phỏng từng bước & biến thiên ô nhớ**: Bảng 4 cột (`Dòng lệnh` | `Thao tác máy tính thực hiện` | `Giá trị biến trong RAM` | `Màn hình xuất hiện gì`) theo dõi sự thay đổi của từng byte dữ liệu.
  5. **Tử huyệt & bẫy lỗi kinh điển**: Cảnh báo `> ⚠️ **Lưu ý:**` hoặc `> ❌ **Bẫy lỗi:**`, nêu rõ đoạn code sai $\to$ lý do sai $\to$ cách viết chuẩn an toàn.
  6. **Mẫu code chuẩn thi đấu**: Code Python 3 trực tiếp, trong sáng, an toàn.
  7. **Hệ thống concept quiz chuyên sâu**: 15–26 câu hỏi trắc nghiệm kiểm tra nhận diện, bắt bẫy, dự đoán output và bản chất ô nhớ kèm lời giải thích cặn kẽ.
  8. **Hệ thống bài tập thực hành phân tầng (P0 $\to$ P3/P4)**: Đủ bối cảnh, nhiệm vụ, input/output, sample trace tay và gợi ý thuật toán.

---

## 2. Chuẩn hóa cấu trúc 6 chương & 16 bài học (Chuẩn kỹ thuật)

Cấu trúc toàn bộ khóa học được tổ chức thành **6 chương logic** và **16 bài học chuyên sâu**, đồng bộ hoàn hảo với hệ thống 299 bài tập thực hành (`problem packages`):

* **Chương 1: Tính toán cơ bản**
  * **Bài 01**: Lệnh xuất nhập, biến số và kiểu dữ liệu
  * **Bài 02**: Toán tử số học và biểu thức toán học *(Tách riêng 4 phép tính cơ bản `+`, `-`, `*`, `/`, dấu ngoặc và tháp ưu tiên)*
  * **Bài 03**: Phép chia nguyên, chia dư và lũy thừa *(Tách riêng `//`, `%`, `**`, bất biến phép chia và 4 ứng dụng Modulo)*
* **Chương 2: Cấu trúc rẽ nhánh & Cấu trúc vòng lặp** *(Gộp rẽ nhánh và vòng lặp vào một chương thuật toán điều khiển cốt lõi)*
  * **Bài 04**: Cấu trúc rẽ nhánh và điều kiện logic
  * **Bài 05**: Vòng lặp for và hàm range
  * **Bài 06**: Vòng lặp while, biến cờ và điều khiển vòng lặp
* **Chương 3: Bài toán số học & Tách chữ số**
  * **Bài 07**: Quy luật dãy số và tam giác số
  * **Bài 08**: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while
  * **Bài 09**: Ước số, bội số và số nguyên tố
  * **Bài 10**: Đếm số theo quy luật và số đặc biệt
* **Chương 4: Danh sách & Thống kê**
  * **Bài 11**: Danh sách và thao tác cơ bản
  * **Bài 12**: Thống kê danh sách và sắp xếp
* **Chương 5: Xử lý chuỗi ký tự** *(Chương riêng biệt cho chuyên đề chuỗi ký tự)*
  * **Bài 13**: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự
  * **Bài 14**: Duyệt chuỗi, biến đổi ký tự và tách từ
* **Chương 6: Luyện thi** *(Chương luyện thi và tổng ôn đề thi)*
  * **Bài 15**: Chiến lược giải đề thi lập trình Python
  * **Bài 16**: Tổng ôn kiến thức và đề thi thử

> 💡 **Lưu ý về nội dung hình học & đổi đơn vị:** Kiến thức về công thức hình học (chu vi, diện tích), quy đổi đơn vị (chiều dài, thời gian) và định dạng f-string đã được quy hoạch độc lập vào file tra cứu [reference/KIEN_THUC_TRONG_TAM_CAN_NHO.md](file:///Users/vu/Developer/ikhEdu_lessons/courses/python-bang-a/reference/KIEN_THUC_TRONG_TAM_CAN_NHO.md), không chiếm một bài học lý thuyết riêng lẻ trong khung chương trình chính.

---

## 3. Chi tiết nội dung các chương học

### 🔹 Chương 1: Tính toán cơ bản

#### Bài 01: Lệnh xuất nhập, biến số và kiểu dữ liệu
- **1. Luồng xử lý dữ liệu của máy tính**: Đầu vào (bàn phím) $\to$ Bộ nhớ RAM & CPU (tính toán) $\to$ Đầu ra (màn hình).
- **2. Lệnh in ra màn hình `print()`**: In chuỗi, in số, in biểu thức, in nhiều đối số với dấu phẩy `,`, tham số `sep` và `end`.
- **3. Biến số và bộ nhớ RAM**: Tên định danh vùng nhớ, phép gán `=`, quy tắc đặt tên biến, hoán đổi biến `a, b = b, a`.
- **4. Các kiểu dữ liệu cơ bản**: `int`, `float`, `str`, kiểu dữ liệu logic `bool`, kiểu `list`, hàm kiểm tra kiểu `type()`.
- **5. Lệnh nhập `input()` và đổi kiểu dữ liệu**: `input()` trả về chuỗi `str`, đổi kiểu số nguyên `int()`, số thực `float()`, tách dòng `split()` và `map()`.
- **6. Bảng mô phỏng biến thiên ô nhớ**: Chạy vết từng dòng lệnh trong RAM.
- **7. Tử huyệt và bẫy lỗi kinh điển**: Quên đổi kiểu số, nhầm dấu gán `=` với so sánh `==`.

#### Bài 02: Toán tử số học và biểu thức toán học
- **1. Bản chất tính toán số học**: Cộng `+`, trừ `-`, nhân `*`, chia thực `/`.
- **2. Tử huyệt phép chia thực `/`**: Luôn luôn sinh số thực `float` (kể cả khi chia hết, ví dụ `8 / 2 = 4.0`).
- **3. Biểu thức toán học & tháp thứ tự ưu tiên**:
  - Cặp ngoặc tròn `()` (ưu tiên tuyệt đối).
  - Nhân `*` và chia thực `/` (kết hợp từ trái sang phải).
  - Cộng `+` và trừ `-` (kết hợp từ trái sang phải).
- **4. Chuyển đổi biểu thức toán học sang Python**: Kỹ thuật bọc ngoặc bảo vệ tử số và mẫu số phân số đại số $\frac{a + b}{c + d} \implies `(a + b) / (c + d)`$.
- **5. Bảng mô phỏng từng bước** tính biểu thức phức tạp.
- **6. Bẫy lỗi kinh điển**: Chia cho số 0 (`ZeroDivisionError`), quên dấu nhân `*`, nhầm dấu phẩy `,` thành chấm `.`.

#### Bài 03: Phép chia nguyên, chia dư và lũy thừa
- **1. Phép chia lấy phần nguyên `//`**: Định nghĩa toán học làm tròn xuống thương số, ý nghĩa chia đồ vật, tính số toa xe.
- **2. Phép chia lấy phần dư `%`**: Định nghĩa phần dư, bất biến phép chia $A = (A // B) \times B + (A \% B)$.
- **3. Bốn ứng dụng cốt lõi của Modulo trong thi đấu**:
  - Kiểm tra chẵn lẻ (`N % 2 == 0`).
  - Kiểm tra tính chia hết (`A % B == 0`).
  - Lấy chữ số tận cùng (`N % 10`) và cắt bỏ chữ số tận cùng (`N // 10`).
  - Bài toán chu kỳ thời gian và tuần hoàn (đồng hồ 24 giờ, thứ trong tuần).
- **4. Phép nâng lên lũy thừa `**`**: Bản chất $A^B$, cảnh báo tử huyệt phòng thi không dùng dấu `^` (phép bitwise XOR).
- **5. Bảng mô phỏng biến thiên ô nhớ** bóc tách chữ số bằng `//` và `%`.

---

### 🔹 Chương 2: Cấu trúc rẽ nhánh & Cấu trúc vòng lặp

#### Bài 04: Cấu trúc rẽ nhánh và điều kiện logic
- **1. Bản chất khoa học máy tính**: Dòng chảy tuần tự vs dòng chảy rẽ nhánh theo điều kiện.
- **2. Phép toán so sánh & kiểu dữ liệu logic**: `==`, `!=`, `>`, `<`, `>=`, `<=`. Bẫy nhầm giữa `=` và `==`.
- **3. Quy tắc thụt lề**: Khối lệnh, chuẩn 4 dấu cách, bẫy lỗi thụt lề.
- **4. 3 cấu trúc rẽ nhánh trong Python**: `if` đơn, `if - else`, `if - elif - else` đa nhánh.
- **5. Toán tử logic `and`, `or`, `not`**: Bảng chân trị, thứ tự ưu tiên logic (`not` $\to$ `and` $\to$ `or`).
- **6. Các bài toán thuật toán kinh điển**: Tìm max/min 3 số, kiểm tra tam giác hợp lệ, bài toán năm nhuận.

#### Bài 05: Vòng lặp for và hàm range
- **1. Bản chất khoa học máy tính**: Lặp xác định (biết trước số lần lặp).
- **2. Hàm `range()` toàn tập**: `range(stop)`, `range(start, stop)`, `range(start, stop, step)` với quy tắc cận trên luôn bị loại trừ.
- **3. Biến đếm vòng lặp**: Cơ chế gán tự động sau mỗi bước lặp.
- **4. Các mẫu thuật toán tích lũy**: Tính tổng dãy số, tính tích giai thừa, đếm số phần tử thỏa điều kiện, tìm max/min trong dãy.

#### Bài 06: Vòng lặp while, biến cờ và điều khiển vòng lặp
- **1. Bản chất khoa học máy tính**: Lặp không xác định (lặp khi điều kiện còn đúng).
- **2. Cấu trúc 3 thành phần**: Khởi tạo biến điều khiển $\to$ điều kiện duy trì $\to$ cập nhật biến điều khiển trong thân vòng lặp.
- **3. Ngăn ngừa vòng lặp vô tận**: Nguyên nhân và cách khắc phục lỗi tràn thời gian (TLE).
- **4. Hai lệnh điều khiển luồng**: `break` (thoát lặp) và `continue` (bỏ qua bước hiện tại).
- **5. Kỹ thuật biến cờ và lính canh**: Đánh dấu trạng thái tìm thấy và đọc dữ liệu đến khi gặp dấu hiệu kết thúc.

---

### 🔹 Chương 3: Bài toán số học & Tách chữ số
- **Bài 07**: Quy luật dãy số và tam giác số (dãy cách đều, Fibonacci cuốn chiếu, vòng lặp lồng nhau in tam giác số).
- **Bài 08**: Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while (lấy chữ số cuối `% 10`, bỏ chữ số cuối `// 10`, tính tổng chữ số, kiểm tra số đối xứng).
- **Bài 09**: Ước số, bội số và số nguyên tố (đếm ước, kiểm tra số nguyên tố, số chính phương, tìm ước chung lớn nhất Euclid).
- **Bài 10**: Đếm số theo quy luật và số đặc biệt (số hoàn hảo, số Armstrong, đếm số trong đoạn $[A, B]$).

---

### 🔹 Chương 4: Danh sách & Thống kê
- **Bài 11**: Danh sách và thao tác cơ bản (khởi tạo danh sách, chỉ số âm/dương, thêm phần tử `append()`, xóa `pop()`/`remove()`, kiểm tra `in`).
- **Bài 12**: Thống kê danh sách và sắp xếp (`min()`, `max()`, `sum()`, `len()`, phương thức `sort()`, đảo ngược, kỹ thuật loại bỏ phần tử trùng lặp bằng duyệt danh sách).

---

### 🔹 Chương 5: Xử lý chuỗi ký tự
- **Bài 13**: Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự (tính chất bất biến, chỉ số hai chiều, cắt lát `s[start:stop:step]`, đảo chuỗi `s[::-1]`, duyệt từng ký tự).
- **Bài 14**: Duyệt chuỗi, biến đổi ký tự và tách từ (kiểm tra `isdigit()`, `isalpha()`, biến đổi `upper()`, `lower()`, bản chất mã ASCII với `ord()` và `chr()`, hằng số chênh lệch 32, kỹ thuật tách từ `split()` và ghép từ `join()`).

---

### 🔹 Chương 6: Luyện thi
- **Bài 15**: Chiến lược giải đề thi lập trình Python (kỹ thuật đọc đề, phân bổ thời gian, nhận diện bẫy test biên, kỹ thuật vét điểm từng phần theo subtask).
- **Bài 16**: Tổng ôn kiến thức và đề thi thử (hệ thống đề thi tổng hợp phong cách contest thực chiến, tổng ôn toàn bộ kỹ năng).

---

## 4. Bảng phân phối bài học, Quiz và hệ thống 299 bài tập thực hành

| Chương | Bài | Mã bài | Tên bài học chuẩn kỹ thuật | Concept Quiz | Bài tập thực hành |
|:---:|:---:|:---:|---|:---:|:---:|
| **1** | 01 | `PY-L01` | Lệnh xuất nhập, biến số và kiểu dữ liệu | 15 câu | 25 bài (`pya_l01_p01` $\to$ `p16`...) |
| | 02 | `PY-L02` | Toán tử số học và biểu thức toán học | 18 câu | 36 bài (`pya_l02_p01` $\to$ `p20`...) |
| | 03 | `PY-L03` | Phép chia nguyên, chia dư và lũy thừa | 18 câu | 34 bài (`pya_l03_p01` $\to$ `p18`...) |
| **2** | 04 | `PY-L04` | Cấu trúc rẽ nhánh và điều kiện logic | 24 câu | 36 bài (`PYA-L04-P01` $\to$ `L06-P12`) |
| | 05 | `PY-L05` | Vòng lặp for và hàm range | 20 câu | 14 bài (`PYA-L07-P01` $\to$ `L07-P14`) |
| | 06 | `PY-L06` | Vòng lặp while, biến cờ và điều khiển vòng lặp | 20 câu | 12 bài (`PYA-L08-P01` $\to$ `L08-P12`) |
| **3** | 07 | `PY-L07` | Quy luật dãy số và tam giác số | 15 câu | 14 bài (`PYA-L09-P01` $\to$ `L09-P14`) |
| | 08 | `PY-L08` | Kỹ thuật tách chữ số và xử lý số nguyên qua vòng lặp while | 16 câu | 14 bài (`PYA-L10-P01` $\to$ `L10-P14`) |
| | 09 | `PY-L09` | Ước số, bội số và số nguyên tố | 16 câu | 14 bài (`PYA-L11-P01` $\to$ `L11-P14`) |
| | 10 | `PY-L10` | Đếm số theo quy luật và số đặc biệt | 15 câu | 12 bài (`PYA-L12-P01` $\to$ `L12-P12`) |
| **4** | 11 | `PY-L11` | Danh sách và thao tác cơ bản | 15 câu | 14 bài (`PYA-L16-P01` $\to$ `L16-P14`) |
| | 12 | `PY-L12` | Thống kê danh sách và sắp xếp | 15 câu | 14 bài (`PYA-L17-P01` $\to$ `L17-P14`) |
| **5** | 13 | `PY-L13` | Chuỗi ký tự — Chỉ số, cắt lát và duyệt ký tự | 15 câu | 12 bài (`PYA-L13-P01` $\to$ `L13-P12`) |
| | 14 | `PY-L14` | Duyệt chuỗi, biến đổi ký tự và tách từ | 26 câu | 24 bài (`PYA-L14-P01` $\to$ `L15-P12`) |
| **6** | 15 | `PY-L15` | Chiến lược giải đề thi lập trình Python | 15 câu | 12 bài (`PYA-L18-P01` $\to$ `L18-P12`) |
| | 16 | `PY-L16` | Tổng ôn kiến thức và đề thi thử | 15 câu | 12 bài (`PYA-L16-P15` $\to$ `L16-P26`) |
| **Tổng** | **16 bài** | | | **278 câu** | **299 bài tập** |

---

## 5. Quy chuẩn đồng bộ Problem Packages theo `cp-solve`

1. **`De_Bai.md`**:
   - Bối cảnh thực tế gắn với bài toán, không văn thơ sáo rỗng.
   - Nhiệm vụ kỹ thuật rõ ràng, trực diện.
   - Input / output định dạng chuẩn xác, đầy đủ mô tả thứ tự và kiểu dữ liệu.
   - Bảng sample và phần `### Giải thích` mô phỏng từng bước trên số liệu mẫu. **Tuyệt đối cấm spoil thuật toán hay cấu trúc kỹ thuật nâng cao**.
   - Ràng buộc: $1.0\text{s}, 256\text{MB}$.
2. **`Huong_Dan_Giang_Day.md`**: Bắt buộc đủ **9 phần sư phạm chuyên sâu**:
   - (1) Mục tiêu học tập & chuẩn đầu ra
   - (2) Phân tích đề bài & bản chất toán học
   - (3) Câu hỏi gợi mở dẫn dắt
   - (4) Chiến lược tối ưu & bất biến thuật toán
   - (5) Mô phỏng từng bước trên sample
   - (6) Phân tích độ phức tạp thời gian & không gian
   - (7) Các bẫy lỗi lập trình kinh điển
   - (8) Mã nguồn tham chiếu Python 3 chuẩn
   - (9) Bài toán mở rộng & chuyển giao
3. **`solution.py`**:
   - **Tuyệt đối không dùng**: `import sys`, `sys.stdin`, `def solve():`, `def main():`, `if __name__ == "__main__":`.
   - **Cú pháp Python 3 chuẩn học sinh**: Đọc trực tiếp bằng `input()`, đổi kiểu dữ liệu `int(input())` và in trực tiếp bằng `print()`.
4. **Testcase**: Chưa tạo testcase theo quy chuẩn khóa Python Bảng A.
