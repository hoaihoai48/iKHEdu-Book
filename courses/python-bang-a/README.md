# iKHEDU PYTHON BẢNG A – LEVEL 1 (TIỂU HỌC)
## Nền Tảng Lập Trình Dạng Chữ & Tư Duy Thuật Toán Thi Đấu

> **Trang chủ quản lý khóa học**: Điều hướng 6 chương (modules), 18 bài học chuyên sâu (lesson packages), ngân hàng bài tập thực hành (problem packages) và hệ thống kiểm tra Concept Quiz.

## Master tổng hợp

Toàn bộ syllabus, 18 lesson, Concept Quiz và ma trận bài tập được tổng hợp tại [`MASTER_ALL_LESSONS.md`](MASTER_ALL_LESSONS.md), theo khuôn master của các khóa C++. File này được sinh tự động từ `lessons/`; 224 Problem Package chi tiết vẫn được quản lý riêng trong `problems/`. Khi nội dung lesson thay đổi, chạy `python3 build_master.py` để cập nhật lại.

Tài liệu kiểm định dành cho giáo viên/biên tập viên: [`CURRICULUM_AUDIT.md`](CURRICULUM_AUDIT.md) và [`ALGORITHM_PATTERNS.md`](ALGORITHM_PATTERNS.md). Các nhãn quản trị nội bộ không xuất hiện trong master học sinh.

---

## 1. Thông tin tổng quan khóa học

| Trường | Giá trị |
|---|---|
| **Tên khóa học** | iKHEDU Python Bảng A – Level 1 |
| **Mã khóa học** | `python-bang-a-level1` |
| **Đối tượng** | Học sinh Tiểu học (Lớp 3, 4, 5) hoặc học sinh mới bắt đầu học ngôn ngữ dạng chữ |
| **Mục tiêu đầu ra** | Xây dựng nền tảng Python và tư duy giải bài qua tính toán, rẽ nhánh, vòng lặp, tách chữ số, chuỗi ký tự, danh sách và các bài toán định hướng Tin học trẻ Bảng A |
| **Ngôn ngữ lập trình** | Python 3 (chuẩn thi đấu hiện hành) |
| **Giọng điệu sư phạm** | Trong sáng, trực quan, gần gũi, truyền cảm hứng, dùng hình tượng hóa sinh động phù hợp tâm lý lứa tuổi Tiểu học |
| **Cấu trúc bài học** | Chu trình 8 bước: `Hook đời sống → Mô phỏng bảng chạy biến → Cú pháp chuẩn → Bẫy lỗi kinh điển → Concept Quiz → Bài tập từ cơ bản đến thử thách` |
| **Status** | `in-progress` — đang audit và chuẩn hóa |
| **Version** | `1.0.0` |

---

## 2. Bản đồ 6 Chương & 18 Bài học (Syllabus)

```
PROGRAM: Python Bảng A (Level 1)
 ├── CHƯƠNG 1: NỀN TẢNG PYTHON & TÍNH TOÁN CƠ BẢN (Bài 01 - 03)
 ├── CHƯƠNG 2: TƯ DUY RẼ NHÁNH & ĐIỀU KIỆN LOGIC (Bài 04 - 06)
 ├── CHƯƠNG 3: VÒNG LẶP & CÁC BÀI TOÁN DÃY SỐ (Bài 07 - 09)
 ├── CHƯƠNG 4: SỐ HỌC TIỂU HỌC & TÁCH CHỮ SỐ (Bài 10 - 12)
 ├── CHƯƠNG 5: THẾ GIỚI CHUỖI KÝ TỰ (STRING) (Bài 13 - 15)
 └── CHƯƠNG 6: DANH SÁCH (LIST) & LUYỆN ĐỀ THTA (Bài 16 - 18)
```

### Danh mục chi tiết các bài học:

| Chương | STT | Mã Bài | Tên Bài Học | Trọng Tâm Kiến Thức | Số Quiz | Số Bài Tập |
|:---:|:---:|:---:|---|---|:---:|:---:|
| **1** | 01 | `PY-L01` | **Lệnh xuất nhập và biến số** | `print()`, `input()`, biến số, ép kiểu `int()`, `float()`, `str()` | 12 câu | 10 bài |
| | 02 | `PY-L02` | **Phép toán số học, chia nguyên và chia dư** | Các phép toán, chia nguyên `//`, chia dư `%`, lũy thừa `**` | 15 câu | 12 bài |
| | 03 | `PY-L03` | **Công thức tính toán, hình học và đổi đơn vị** | Chu vi, diện tích HCN/hình vuông, đổi thời gian, làm tròn `round()` | 12 câu | 10 bài |
| **2** | 04 | `PY-L04` | **Rẽ nhánh có điều kiện với if-else** | So sánh (`==`, `!=`, `<`, `>`), thụt lề Indentation, max/min 2 số | 15 câu | 12 bài |
| | 05 | `PY-L05` | **Rẽ nhánh nhiều hướng với elif** | Phân loại bậc thang, xếp loại, max/min 3-4 số, bài toán vận tốc | 14 câu | 12 bài |
| | 06 | `PY-L06` | **Điều kiện ghép với and-or-not** | Kết hợp điều kiện logic, tam giác hợp lệ, năm nhuận, đếm ngày | 15 câu | 12 bài |
| **3** | 07 | `PY-L07` | **Vòng lặp for và hàm range** | `range(start, stop, step)`, duyệt xuôi/ngược, tổng cấp số cộng | 15 câu | 14 bài |
| | 08 | `PY-L08` | **Vòng lặp while và biến cờ** | Vòng lặp điều kiện, biến cờ (flag), thoát vòng lặp `break` | 14 câu | 12 bài |
| | 09 | `PY-L09` | **Quy luật dãy số và tam giác số** | Dãy Fibonacci, hoán đổi `a, b = b, a+b`, tam giác số | 15 câu | 14 bài |
| **4** | 10 | `PY-L10` | **Tách chữ số với chia nguyên và chia dư** | Tách hàng đơn vị, chục, trăm; tổng chữ số, số đối xứng | 15 câu | 14 bài |
| | 11 | `PY-L11` | **Ước số, bội số và số nguyên tố** | Đếm ước, kiểm tra số nguyên tố, số chính phương, ƯCLN `math.gcd` | 15 câu | 14 bài |
| | 12 | `PY-L12` | **Đếm số theo quy luật và số đặc biệt** | Số hoàn hảo, số Armstrong, số đẹp, đếm số trong đoạn $[A, B]$ | 14 câu | 12 bài |
| **5** | 13 | `PY-L13` | **Chỉ số và cắt lát chuỗi** | Vị trí âm/dương, cắt chuỗi `s[start:stop:step]`, đảo chuỗi `s[::-1]` | 14 câu | 12 bài |
| | 14 | `PY-L14` | **Duyệt chuỗi và biến đổi ký tự** | `for ch in s`, `upper()`, `lower()`, `isdigit()`, đếm chữ cái | 14 câu | 12 bài |
| | 15 | `PY-L15` | **Tách từ và mã hóa thay thế** | `split()`, `join()`, đếm từ, mã hóa dịch chuyển Caesar (`ord`, `chr`) | 12 câu | 12 bài |
| **6** | 16 | `PY-L16` | **Danh sách và thao tác cơ bản** | Tạo list, thêm `append()`, xóa `remove()`, `pop()`, kiểm tra `in` | 15 câu | 14 bài |
| | 17 | `PY-L17` | **Thống kê danh sách và sắp xếp** | `min()`, `max()`, `sum()`, `len()`, `sort()`, loại bỏ trùng lặp | 15 câu | 14 bài |
| | 18 | `PY-L18` | **Chiến lược giải đề Tin học trẻ Bảng A** | Kỹ năng đọc đề, bẫy test biên, 3 bộ đề thi thử THTA toàn diện | 12 câu | 12 bài |

---

## 3. Quy chuẩn tài liệu trong mỗi Lesson Package

Mỗi bài học được lưu trữ tại `lessons/lesson-xx/` gồm 2 file bắt buộc:
1. **`LessonXX_Production_Content.md`**:
   - Khái niệm, trực giác đời sống và hình tượng hóa sư phạm.
   - Bảng Dry Run phân tích từng dòng lệnh và sự biến thiên của bộ nhớ.
   - Các bẫy lỗi kinh điển của học sinh Tiểu học và cách phòng tránh.
   - **Hệ thống Concept Quiz** ($\ge 12$ câu hỏi đa dạng giải thích chi tiết đáp án).
2. **`Bai_Tap.md`**:
   - Hệ thống bài tập đi từ cơ bản, luyện tập, vận dụng đến thử thách.
   - Mỗi bài đều có: Đề bài, Giới hạn dữ liệu, Input/Output mẫu, Giải thích cặn kẽ và Gợi ý thuật toán.

---

## 4. Hệ thống Problem Library Độc Lập (`courses/python-bang-a/problems/`)

Toàn bộ **224 bài tập thực hành** đều đã được trích xuất và đóng gói thành các **Problem Package độc lập** đặt tại thư mục `courses/python-bang-a/problems/`.

Mỗi Problem Package tương ứng với một thư mục định danh chuẩn: `pya_l<lesson>_p<stt>_<slug_ten_bai>/` (Ví dụ: `pya_l01_p01_loi_chao_robot/`), bao gồm:
* **`De_Bai.md`**: Statement hoàn chỉnh (Tiêu đề, Mã bài `PYA-Lxx-Pxx`, Bối cảnh, Yêu cầu, Input, Output, Ví dụ mẫu Sample, Ràng buộc thi đấu).
* **`Huong_Dan_Giang_Day.md`**: Hướng dẫn giảng dạy sư phạm chuyên sâu 9 phần chuẩn iKHEDU (Mục tiêu, Phân tích đề & Edge cases, Socratic Method, Bất biến thuật toán, Bảng Dry Run, Độ phức tạp thời gian/bộ nhớ, Bẫy lỗi kinh điển, Code Python 3 tham chiếu, Bài toán mở rộng).
* **`solution.py`**: Mã nguồn lời giải Python 3 tham chiếu tương ứng.
