# Bài 15: Chiến lược giải đề Tin học trẻ Bảng A

## 1. Bản đồ 5 bước tác chiến trong phòng thi
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

## 2. Các tử huyệt làm mất điểm oan
- In thừa chữ dẫn dắt: Đề chỉ yêu cầu in `15`, viết `print("Ket qua la:", 15)` sẽ bị chấm `Wrong Answer (WA)` ngay lập tức.
- Không để ý giới hạn $N$: Nếu $N \le 10^5$ thì vòng lặp `for` an toàn. Nếu $N \ge 10^9$ bắt buộc phải dùng công thức giải tích $\mathcal{O}(1)$.

## 3. Concept quiz: 12 câu trắc nghiệm bắt bẫy củng cố khái niệm

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
