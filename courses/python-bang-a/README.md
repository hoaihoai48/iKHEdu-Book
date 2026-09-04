# iKHEDU PYTHON BẢNG A – LEVEL 1 (TIỂU HỌC)
## Nền Tảng Lập Trình Dạng Chữ & Tư Duy Thuật Toán Thi Đấu

> **Trang chủ quản lý khóa học**: Điều hướng 7 chương (modules), 16 bài học chuyên sâu (lesson packages), ngân hàng bài tập thực hành (problem packages) và hệ thống kiểm tra Concept Quiz.

## Master tổng hợp

Toàn bộ syllabus, 16 lesson, Concept Quiz và ma trận bài tập được tổng hợp tại [`MASTER_ALL_LESSONS.md`](MASTER_ALL_LESSONS.md), theo khuôn master của các khóa C++. File này được sinh tự động từ `lessons/`; 246 Problem Package chi tiết vẫn được quản lý riêng trong `problems/`. Khi nội dung lesson thay đổi, chạy `python3 build_master.py` để cập nhật lại.

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

## 2. Bản đồ 7 Chương & 16 Bài học (Syllabus)

```
PROGRAM: Python Bảng A (Level 1)
 ├── CHƯƠNG 1: TÍNH TOÁN CƠ BẢN (Bài 01 - 03)
 ├── CHƯƠNG 2: TƯ DUY RẼ NHÁNH & ĐIỀU KIỆN LOGIC (Bài 04)
 ├── CHƯƠNG 3: VÒNG LẶP (Bài 05 - 06)
 ├── CHƯƠNG 4: BÀI TOÁN SỐ HỌC (Bài 07 - 10)
 ├── CHƯƠNG 5: DANH SÁCH (LIST) (Bài 11 - 12)
 ├── CHƯƠNG 6: XỬ LÝ CHUỖI & KÝ TỰ (Bài 13 - 14)
 └── CHƯƠNG 7: LUYỆN ĐỀ THI (Bài 15 - 16)
```

### Danh mục chi tiết các bài học:

| Chương | STT | Mã Bài | Tên Bài Học | Trọng Tâm Kiến Thức | Số Quiz | Số Bài Tập |
|:---:|:---:|:---:|---|---|:---:|:---:|
| **1** | 01 | `PY-L01` | **Lệnh xuất nhập và biến số** | `print()`, `input()`, biến số, ép kiểu `int()`, `float()`, `str()` | 12 câu | 10 bài |
| | 02 | `PY-L02` | **Phép toán số học, chia nguyên và chia dư** | Các phép toán, chia nguyên `//`, chia dư `%`, lũy thừa `**` | 18 câu | 16 bài |
| | 03 | `PY-L03` | **Công thức tính toán, hình học và đổi đơn vị** | Chu vi, diện tích HCN/hình vuông, đổi thời gian, làm tròn `round()` | 18 câu | 16 bài |
| **2** | 04 | `PY-L04` | **Rẽ nhánh và điều kiện logic** | So sánh, `if-elif-else`, `and-or-not`, thụt lề, max/min, tam giác, năm nhuận | 44 câu | 36 bài |
| **3** | 05 | `PY-L05` | **Vòng lặp for và hàm range** | `range(start, stop, step)`, duyệt xuôi/ngược, tổng cấp số cộng | 15 câu | 14 bài |
| | 06 | `PY-L06` | **Vòng lặp while và biến cờ** | Vòng lặp điều kiện, biến cờ (flag), thoát vòng lặp `break` | 14 câu | 12 bài |
| **4** | 07 | `PY-L07` | **Quy luật dãy số và tam giác số** | Dãy Fibonacci, hoán đổi `a, b = b, a+b`, tam giác số | 15 câu | 14 bài |
| | 08 | `PY-L08` | **Tách chữ số với chia nguyên và chia dư** | Tách hàng đơn vị, chục, trăm; tổng chữ số, số đối xứng | 15 câu | 14 bài |
| | 09 | `PY-L09` | **Ước số, bội số và số nguyên tố** | Đếm ước, kiểm tra số nguyên tố, số chính phương, ƯCLN `math.gcd` | 15 câu | 14 bài |
| | 10 | `PY-L10` | **Đếm số theo quy luật và số đặc biệt** | Số hoàn hảo, số Armstrong, số đẹp, đếm số trong đoạn $[A, B]$ | 14 câu | 12 bài |
| **5** | 11 | `PY-L11` | **Danh sách và thao tác cơ bản** | Tạo list, thêm `append()`, xóa `remove()`, `pop()`, kiểm tra `in` | 15 câu | 14 bài |
| | 12 | `PY-L12` | **Thống kê danh sách và sắp xếp** | `min()`, `max()`, `sum()`, `len()`, `sort()`, loại bỏ trùng lặp | 15 câu | 14 bài |
| **6** | 13 | `PY-L13` | **Chỉ số và cắt lát chuỗi** | Vị trí âm/dương, cắt chuỗi `s[start:stop:step]`, đảo chuỗi `s[::-1]` | 14 câu | 12 bài |
| | 14 | `PY-L14` | **Duyệt chuỗi, biến đổi ký tự và tách từ** | `for ch in s`, `upper()/lower()`, `split()/join()`, mã Caesar (`ord`, `chr`) | 26 câu | 24 bài |
| **7** | 15 | `PY-L15` | **Chiến lược giải đề Tin học trẻ Bảng A** | Kỹ năng đọc đề, bẫy test biên, chiến lược phân bổ thời gian | 12 câu | 12 bài |
| | 16 | `PY-L16` | **Đề thi thử Tin học trẻ Bảng A** | Đề contest giấu pattern, subtask, vét điểm từng phần | — | 12 bài |

> **Đối chiếu mã bài cũ → mới** (mã problem `pya_lXX_*` giữ nguyên, chỉ đổi số Bài hiển thị): cũ 07→mới 05, 08→06, 09→07, 10→08, 11→09, 12→10, 16→11, 17→12, 13→13, 14+15→14, 18→15; cũ 04+05+06 gộp thành mới 04; mới 16 là bài đề thi thử mới.
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

Toàn bộ **246 bài tập thực hành** đều đã được trích xuất và đóng gói thành các **Problem Package độc lập** đặt tại thư mục `courses/python-bang-a/problems/`.

Mỗi Problem Package tương ứng với một thư mục định danh chuẩn: `pya_l<lesson>_p<stt>_<slug_ten_bai>/` (Ví dụ: `pya_l01_p01_loi_chao_robot/`), bao gồm:
* **`De_Bai.md`**: Statement hoàn chỉnh (Tiêu đề, Bối cảnh, Nhiệm vụ, Input, Output, Ví dụ mẫu Sample, Ràng buộc thi đấu — không ghi mã bài trong đề học sinh, mã chỉ nằm ở tên thư mục).
* **`Huong_Dan_Giang_Day.md`**: Hướng dẫn giảng dạy sư phạm chuyên sâu 9 phần chuẩn iKHEDU (Mục tiêu, Phân tích đề & Edge cases, Socratic Method, Bất biến thuật toán, Bảng Dry Run, Độ phức tạp thời gian/bộ nhớ, Bẫy lỗi kinh điển, Code Python 3 tham chiếu, Bài toán mở rộng).
* **`solution.py`**: Mã nguồn lời giải Python 3 tham chiếu tương ứng.
