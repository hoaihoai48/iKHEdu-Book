# Hướng Dẫn Giảng Dạy — Chuyến Tàu Vượt Đèo (`PYA-L16-P12`)

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- Học sinh giải được bài ở mức Khó trong 90 phút thi thử.
- Rèn pattern ẩn: **vòng lặp + cực trị chạy (đếm lần phá kỷ lục)**.
- Mục tiêu trong ma trận Bai_Tap.md: Rèn giữ giá trị lớn nhất hiện tại trong một lượt duyệt.
- Chuẩn đầu ra: đọc đề contest không gợi ý, tự chọn công cụ, vét điểm từng subtask.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- Dữ kiện vào: xem mục Input trong De_Bai.md. Ràng buộc: $N \le 10^5$.
- Trường hợp biên: N = 1 (đáp án 1); dãy giảm dần (đáp án 1); dãy tăng dần (đáp án N).
- Đề giấu pattern: học sinh phải tự nhận ra công cụ từ câu chuyện, không được gợi ý trước.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. Đề cho những gì, hỏi cái gì? (Gạch chân dữ kiện.)
2. Với ví dụ nhỏ, em làm tay thế nào trước khi nghĩ đến code?
3. Trường hợp N = 0 / N = 1 thì đáp án là gì?
4. Subtask 1 giới hạn nhỏ cho phép cách làm đơn giản nào?

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- Bất biến: best luôn là giá trị lớn nhất của các đèo đã đi qua.
- Cách vét điểm: subtask 1 làm cách đơn giản (lặp trực tiếp) để lấy 50% điểm trước; subtask 2 mới cần cách nhanh.
- Độ phức tạp mục tiêu xem mục 6.

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

- 1 3 5 2 4 7: kỷ lục là 1, 3, 5, 7 nên đáp án 4.
- Khuyến khích học sinh kẻ bảng tay 3 cột: bước | giá trị hiện tại | kết quả.

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian ($\mathcal{O}(...)$)

- Thời gian $\mathcal{O}(N)$ (riêng bài tổng 1..N dùng công thức nên $\mathcal{O}(1)$), bộ nhớ $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$.

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- Nhầm lớn hơn với lớn hơn hoặc bằng (dãy bằng nhau chỉ reo 1 lần); quên ngọn đầu tiên luôn được tính.
- In thừa chữ giải thích gây Wrong Answer; sai định dạng số thập phân; quên test biên.

## 8. Mã Nguồn Tham Chiếu

```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
c = 1
for x in data[1:]:
    if x > best:
        best = x
        c += 1
print(c)
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- Tăng giới hạn để buộc tối ưu hơn; đổi điều kiện (ngày lẻ, số nhỏ nhất, giảm dần).
- Ghép với bài khác trong đề thi thử thành đề 4 bài / 90 phút.
