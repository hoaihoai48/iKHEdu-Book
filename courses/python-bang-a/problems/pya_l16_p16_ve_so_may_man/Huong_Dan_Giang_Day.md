# Hướng Dẫn Giảng Dạy — Vé Số May Mắn (`PYA-L16-P02`)

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- Học sinh giải được bài ở mức Dễ trong 90 phút thi thử.
- Rèn pattern ẩn: **tách chữ số + rẽ nhánh (tổng chữ số chia hết)**.
- Mục tiêu trong ma trận Bai_Tap.md: Rèn tách chữ số và kiểm tra chia hết.
- Chuẩn đầu ra: đọc đề contest không gợi ý, tự chọn công cụ, vét điểm từng subtask.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- Dữ kiện vào: xem mục Input trong De_Bai.md. Ràng buộc: $N \le 10^{18}$.
- Trường hợp biên: N < 7; N có tổng chữ số đúng bằng 7; N = 10^18.
- Đề giấu pattern: học sinh phải tự nhận ra công cụ từ câu chuyện, không được gợi ý trước.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. Đề cho những gì, hỏi cái gì? (Gạch chân dữ kiện.)
2. Với ví dụ nhỏ, em làm tay thế nào trước khi nghĩ đến code?
3. Trường hợp N = 0 / N = 1 thì đáp án là gì?
4. Subtask 1 giới hạn nhỏ cho phép cách làm đơn giản nào?

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- Bất biến: Tổng chữ số không đổi dù duyệt từ trái hay phải.
- Cách vét điểm: subtask 1 làm cách đơn giản (lặp trực tiếp) để lấy 50% điểm trước; subtask 2 mới cần cách nhanh.
- Độ phức tạp mục tiêu xem mục 6.

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

- 1234: tổng 1+2+3+4 = 10, 10 % 7 = 3 nên in NO.
- Khuyến khích học sinh kẻ bảng tay 3 cột: bước | giá trị hiện tại | kết quả.

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian ($\mathcal{O}(...)$)

- Thời gian $\mathcal{O}(N)$ (riêng bài tổng 1..N dùng công thức nên $\mathcal{O}(1)$), bộ nhớ $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$.

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- Quên số 0 vẫn là chữ số; nhầm chia hết cho 7 với số 7 trong số.
- In thừa chữ giải thích gây Wrong Answer; sai định dạng số thập phân; quên test biên.

## 8. Mã Nguồn Tham Chiếu

```python
s = input().strip()
t = 0
for c in s:
    if "0" <= c <= "9":
        t += ord(c) - ord("0")
if t % 7 == 0:
    print("YES")
else:
    print("NO")
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- Tăng giới hạn để buộc tối ưu hơn; đổi điều kiện (ngày lẻ, số nhỏ nhất, giảm dần).
- Ghép với bài khác trong đề thi thử thành đề 4 bài / 90 phút.
