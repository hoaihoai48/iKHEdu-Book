# Bài 18: Chiến lược giải đề Tin học trẻ Bảng A

---

## 1. Khởi động: Bước vào đấu trường Tin học trẻ Bảng A

Chúc mừng các em đã chinh phục thành công 17 bài học nền tảng của khóa học **iKHEDU Python Bảng A – Level 1**!
Giờ đây, các em không còn là những bạn nhỏ mới bỡ ngỡ làm quen với dòng code đầu tiên nữa, mà đã trở thành những **chiến binh thuật toán nhí** nắm trong tay đầy đủ các vũ khí lợi hại nhất:
* Tính toán & chia nguyên chia dư (`//`, `%`).
* Rẽ nhánh điều kiện logic (`if-elif-else`, `and-or-not`).
* Vòng lặp kiểm soát luồng (`for`, `while`, `break`).
* Kỹ thuật tách chữ số và số học chuyên sâu.
* Cắt lát và biến đổi chuỗi ký tự (`slicing`, `split`, `join`).
* Quản lý mảng danh sách và sắp xếp siêu tốc (`list`, `sort`).

Tuy nhiên, trong phòng thi thực tế, kiến thức cần đi cùng **chiến lược làm bài và kỹ năng kiểm tra trường hợp biên**.
Bài học cuối cùng này sẽ trang bị cho các em cẩm nang tác chiến thực thụ của các Quán quân Tin học trẻ toàn quốc.

---

## 2. Bản đồ tác chiến 5 bước trong phòng thi Tin học trẻ

```
BƯỚC 1: Đọc đề cẩn thận (Tối thiểu 2 lần, gạch chân Ràng buộc dữ liệu & Input/Output)
   │
BƯỚC 2: Nháp thuật toán & Dry Run tay với Sample Test trên giấy
   │
BƯỚC 3: Liệt kê các "Bẫy hiểm độc" (Edge Cases: N = 0, N = 1, số âm, số cực lớn)
   │
BƯỚC 4: Lập trình sạch sẽ, dùng đúng kiểu dữ liệu, in đúng từng chữ hoa/thường
   │
BƯỚC 5: Tự kiểm thử (Self-Testing) với test nhỏ nhất, test biên và test lớn nhất trước khi nộp!
```

### 3 tử huyệt thường làm mất điểm oan uổng nhất:
1. **In thừa chữ giải thích:** Đề bài chỉ yêu cầu in ra con số `42`, nhưng học sinh lại viết `print("Ket qua la:", 42)`. Hệ thống chấm máy tự động (DKOJ) sẽ chấm là `Wrong Answer (WA)` ngay lập tức!
2. **Quên trường hợp số 0 hoặc số 1:** Ví dụ bài kiểm tra số nguyên tố, nếu không chặn `n < 2` sẽ bị sai toàn bộ các test chứa số 0 và số 1.
3. **Quá giới hạn thời gian (TLE):** Dùng vòng lặp $N$ bước khi $N$ rất lớn. Hãy luôn so sánh số lần lặp dự kiến với giới hạn thời gian trước khi chọn thuật toán.

---

## 3. Cấu trúc một đề thi chuẩn Tin học trẻ Bảng A tiểu học

Một đề thi Tin học trẻ Bảng A thường gồm nhiều bài toán với mức độ tăng dần. Cấu trúc cụ thể phụ thuộc vào kỳ thi và ban tổ chức:
* **Bài 1 (Khởi động - 30 điểm):** Phép tính số học hoặc hình học đời sống (tính tiền điện, đổi thời gian, quy luật chu vi diện tích). Thường chỉ cần viết công thức giải tích trực tiếp $\mathcal{O}(1)$.
* **Bài 2 (Xử lý chữ số hoặc Dãy số - 30 điểm):** Tách chữ số của $N$, số đối xứng, số nguyên tố, hoặc tìm số thứ $K$ của một dãy số có quy luật.
* **Bài 3 (Xử lý chuỗi ký tự hoặc Danh sách - 25 điểm):** Đếm từ, chuẩn hóa họ tên, mật mã Caesar, sắp xếp bảng xếp hạng.
* **Bài 4 (Vận dụng cao - Phân loại huy chương - 15 điểm):** Bài toán tư duy logic, bao hàm loại trừ, hoặc thuật toán tham lam tìm phương án tối ưu.

---

## 4. Concept quiz: 12 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Khi đề bài yêu cầu "in ra kết quả trên một dòng", nếu in thêm dòng chữ `"Ket qua la:"` thì hệ thống chấm thi tự động sẽ đánh giá thế nào?
- **A.** Vẫn được điểm tối đa vì code chạy đúng logic
- **B.** Được cộng điểm vì giải thích rõ ràng
- **C.** **[Đáp án đúng]** Bị chấm `Wrong Answer (WA)` (0 điểm) vì output không khớp chính xác với định dạng của đề bài
- **D.** Được nửa số điểm
- > *Giải thích:* Hệ thống chấm tự động so sánh từng ký tự trong file output của thí sinh với đáp án chuẩn. Mọi ký tự thừa hay thiếu đều bị coi là sai.

#### Câu 2: Khi đánh giá số vòng lặp trong chương trình Python, cách suy nghĩ nào phù hợp nhất?
- **A.** Chỉ nhìn vào số biến trong chương trình
- **B.** **[Đáp án đúng]** Ước lượng số lần lặp theo giới hạn dữ liệu và kiểm tra bằng test phù hợp
- **C.** Luôn chọn vòng lặp dài nhất
- **D.** Bỏ qua giới hạn thời gian
- > *Giải thích:* Tốc độ phụ thuộc vào môi trường, thao tác và dữ liệu. Điều cần làm là phân tích độ phức tạp, giới hạn đề bài và kiểm tra thực tế khi cần.

#### Câu 3: Nếu dữ liệu đầu vào cho $N \le 10^9$, thuật toán có độ phức tạp thời gian nào sau đây sẽ chắc chắn bị lỗi `Time Limit Exceeded` (tle)?
- **A.** $\mathcal{O}(1)$ (Công thức toán)
- **B.** **[Đáp án đúng]** $\mathcal{O}(N)$ (Vòng lặp chạy từ 1 đến $N$)
- **C.** $\mathcal{O}(\sqrt{N})$ (Vòng lặp chạy đến $\sqrt{N} \approx 31622$)
- **D.** $\mathcal{O}(\log N)$
- > *Giải thích:* Khi $N$ rất lớn, một vòng lặp tuyến tính có thể vượt giới hạn thời gian. Cần xem giới hạn cụ thể và tìm công thức hoặc cách giảm số bước nếu phù hợp.

#### Câu 4: Khi giải bài toán liên quan đến số tự nhiên $N$, các "test biên" (edge cases) bắt buộc phải tự kiểm tra tay trước tiên là:
- **A.** $N = 100$
- **B.** **[Đáp án đúng]** $N = 0$, $N = 1$, và giá trị $N$ nhỏ nhất / lớn nhất trong phạm vi đề bài cho
- **C.** $N = 50$
- **D.** $N$ là số ngẫu nhiên
- > *Giải thích:* Các bài toán tin học thường gài bẫy tại các điểm biên như 0, 1 hoặc giới hạn cực đại.

#### Câu 5: Dòng lệnh nào sau đây giúp đọc trọn vẹn cả một dòng văn bản chứa cả khoảng trắng trong Python?
- **A.** `input().split()`
- **B.** **[Đáp án đúng]** `s = input()`
- **C.** `s = int(input())`
- **D.** `s = input().strip().split()`
- > *Giải thích:* Hàm `input()` đọc nguyên vẹn cả dòng cho đến khi gặp phím Enter.

#### Câu 6: Trong Python, số nguyên có bị giới hạn kích thước tối đa là 32-bit hay 64-bit như trong pascal hay C++ không?
- **A.** Có, tối đa là $2 \times 10^9$
- **B.** Có, tối đa là $9 \times 10^{18}$
- **C.** **[Đáp án đúng]** Không, Python hỗ trợ số nguyên lớn (Arbitrary-precision integers) có thể chứa hàng nghìn chữ số mà không bao giờ bị tràn số
- **D.** Tối đa 100 chữ số
- > *Giải thích:* Đây là lợi thế cực lớn của Python so với các ngôn ngữ khác trong kỳ thi Tin học trẻ Tiểu học: Không bao giờ lo bị tràn số!

#### Câu 7: Khi gặp một bài toán khó chưa nghĩ ra cách làm tối ưu $\mathcal{O}(1)$ hay $\mathcal{O}(N)$, chiến thuật khôn ngoan nhất trong phòng thi là gì?
- **A.** Bỏ bài đó để đi về sớm
- **B.** Ngồi nghĩ đến hết giờ
- **C.** **[Đáp án đúng]** Viết lời giải đơn giản trước, kiểm tra đúng đắn rồi cải thiện nếu giới hạn dữ liệu yêu cầu
- **D.** Viết ngẫu nhiên một câu lệnh print
- > *Giải thích:* Chiến thuật "vét điểm từng test": 50% điểm của một bài khó quý giá hơn là bỏ trắng 0 điểm.

#### Câu 8: Khi nộp bài lên hệ thống thi đấu, nếu nhận được thông báo lỗi `Memory Limit Exceeded` (mle), nguyên nhân là gì?
- **A.** Chạy quá thời gian quy định
- **B.** In ra sai đáp án
- **C.** **[Đáp án đúng]** Chương trình tiêu thụ quá nhiều bộ nhớ RAM (vượt mức 256MB quy định)
- **D.** Lỗi cú pháp
- > *Giải thích:* MLE xảy ra khi tạo mảng quá lớn hoặc để đệ quy quá sâu.

#### Câu 9: Để in ra số thực $X$ với đúng 2 chữ số sau dấu phẩy (làm tròn chuẩn), câu lệnh nào chuẩn xác nhất?
- **A.** `print(round(X, 2))`
- **B.** **[Đáp án đúng]** `print(f"{X:.2f}")`
- **C.** `print(int(X))`
- **D.** `print(X)`
- > *Giải thích:* `round(5.0, 2)` có thể chỉ in `5.0`. Dùng f-string định dạng `{X:.2f}` đảm bảo luôn in đủ 2 chữ số phần thập phân như `5.00`.

#### Câu 10: Tên file nộp bài trong các kỳ thi thường có định dạng như thế nào?
- **A.** Tên bất kỳ do thí sinh chọn
- **B.** **[Đáp án đúng]** Bắt buộc phải trùng khớp với mã bài toán theo quy định của ban tổ chức (ví dụ: `BAI1.PY`)
- **C.** Luôn luôn là `main.py`
- **D.** Tên của thí sinh
- > *Giải thích:* Đặt sai tên file hoặc sai phần mở rộng sẽ khiến máy chấm không tìm thấy bài và bị 0 điểm.

#### Câu 11: Trước khi nộp bài 5 phút, thí sinh nên làm việc gì nhất?
- **A.** Viết lại toàn bộ code của bài khó nhất
- **B.** **[Đáp án đúng]** Rà soát lại tất cả các dòng `print` thừa dùng để debug, kiểm tra tên file và bấm nộp thử lại toàn bộ các bài
- **C.** Tắt máy tính đi ra ngoài
- **D.** Sửa đổi các biến số
- > *Giải thích:* Rất nhiều thí sinh bị mất điểm vì quên xóa các dòng `print("debug: ...")` dẫn đến bị máy chấm bắt lỗi output thừa.

#### Câu 12: Phẩm chất quan trọng nhất của một tuyển thủ Tin học trẻ xuất sắc là gì?
- **A.** Gõ bàn phím thật nhanh
- **B.** **[Đáp án đúng]** Tính kiên trì, tư duy cẩn trọng, đọc kỹ đề bài và không bao giờ bỏ cuộc
- **C.** Thuộc lòng code mẫu
- **D.** Chỉ làm các bài dễ
- > *Giải thích:* Sự kiên trì và tư duy logic sắc bén là chìa khóa mở cánh cửa đến với mọi thành công trong công nghệ và cuộc sống.
