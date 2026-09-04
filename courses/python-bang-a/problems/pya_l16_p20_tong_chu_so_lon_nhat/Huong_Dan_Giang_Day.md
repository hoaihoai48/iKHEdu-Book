# Hướng Dẫn Giảng Dạy — Tổng Chữ Số Lớn Nhất (`PYA-L16-P06`)

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- Học sinh giải được bài ở mức Trung bình trong 90 phút thi thử.
- Rèn pattern ẩn: **tách chữ số lồng trong vòng lặp + chọn cực trị**.
- Mục tiêu trong ma trận Bai_Tap.md: Rèn hàm con tính tổng chữ số và chọn cực trị có điều kiện phụ.
- Chuẩn đầu ra: đọc đề contest không gợi ý, tự chọn công cụ, vét điểm từng subtask.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- Dữ kiện vào: xem mục Input trong De_Bai.md. Ràng buộc: $N \le 10^5$.
- Trường hợp biên: N = 1; mọi số có tổng chữ số bằng nhau; số 0.
- Đề giấu pattern: học sinh phải tự nhận ra công cụ từ câu chuyện, không được gợi ý trước.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. Đề cho những gì, hỏi cái gì? (Gạch chân dữ kiện.)
2. Với ví dụ nhỏ, em làm tay thế nào trước khi nghĩ đến code?
3. Trường hợp N = 0 / N = 1 thì đáp án là gì?
4. Subtask 1 giới hạn nhỏ cho phép cách làm đơn giản nào?

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- Bất biến: Sau mỗi bước, best luôn là đáp án đúng của các số đã xét.
- Cách vét điểm: subtask 1 làm cách đơn giản (lặp trực tiếp) để lấy 50% điểm trước; subtask 2 mới cần cách nhanh.
- Độ phức tạp mục tiêu xem mục 6.

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

- 99 có tổng 18 lớn nhất nên thắng.
- Khuyến khích học sinh kẻ bảng tay 3 cột: bước | giá trị hiện tại | kết quả.

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian ($\mathcal{O}(...)$)

- Thời gian $\mathcal{O}(N)$ (riêng bài tổng 1..N dùng công thức nên $\mathcal{O}(1)$), bộ nhớ $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$.

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- Quên điều kiện phụ số nhỏ hơn khi hòa; tính tổng chữ số sai với số 0.
- In thừa chữ giải thích gây Wrong Answer; sai định dạng số thập phân; quên test biên.

## 8. Mã Nguồn Tham Chiếu

```python
n = int(input())
data = []
while len(data) < n:
    data += list(map(int, input().split()))
data = data[:n]
best = data[0]
bs = sum(map(int, str(best)))
for x in data[1:]:
    s = sum(map(int, str(x)))
    if s > bs or (s == bs and x < best):
        best = x
        bs = s
print(best)
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- Tăng giới hạn để buộc tối ưu hơn; đổi điều kiện (ngày lẻ, số nhỏ nhất, giảm dần).
- Ghép với bài khác trong đề thi thử thành đề 4 bài / 90 phút.
