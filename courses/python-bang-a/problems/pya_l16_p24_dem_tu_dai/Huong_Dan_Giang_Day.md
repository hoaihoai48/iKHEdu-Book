# Hướng Dẫn Giảng Dạy — Đếm Từ Dài (`PYA-L16-P10`)

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- Học sinh giải được bài ở mức Trung bình trong 90 phút thi thử.
- Rèn pattern ẩn: **chuỗi (tách từ + rẽ nhánh theo độ dài)**.
- Mục tiêu trong ma trận Bai_Tap.md: Rèn tách từ bằng split và so sánh độ dài.
- Chuẩn đầu ra: đọc đề contest không gợi ý, tự chọn công cụ, vét điểm từng subtask.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- Dữ kiện vào: xem mục Input trong De_Bai.md. Ràng buộc: $|S| \le 10^4$.
- Trường hợp biên: K = 0 (mọi từ đều được đếm); câu có nhiều dấu cách liên tiếp.
- Đề giấu pattern: học sinh phải tự nhận ra công cụ từ câu chuyện, không được gợi ý trước.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. Đề cho những gì, hỏi cái gì? (Gạch chân dữ kiện.)
2. Với ví dụ nhỏ, em làm tay thế nào trước khi nghĩ đến code?
3. Trường hợp N = 0 / N = 1 thì đáp án là gì?
4. Subtask 1 giới hạn nhỏ cho phép cách làm đơn giản nào?

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- Bất biến: Mỗi từ trong câu được xét đúng một lần.
- Cách vét điểm: subtask 1 làm cách đơn giản (lặp trực tiếp) để lấy 50% điểm trước; subtask 2 mới cần cách nhanh.
- Độ phức tạp mục tiêu xem mục 6.

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

- Từ cung dài 4 > 3 nên đếm 1.
- Khuyến khích học sinh kẻ bảng tay 3 cột: bước | giá trị hiện tại | kết quả.

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian ($\mathcal{O}(...)$)

- Thời gian $\mathcal{O}(N)$ (riêng bài tổng 1..N dùng công thức nên $\mathcal{O}(1)$), bộ nhớ $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$.

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- Quên split mà đếm ký tự; nhầm lớn hơn với lớn hơn hoặc bằng.
- In thừa chữ giải thích gây Wrong Answer; sai định dạng số thập phân; quên test biên.

## 8. Mã Nguồn Tham Chiếu

```python
k = int(input())
s = input().split()
c = 0
for w in s:
    if len(w) > k:
        c += 1
print(c)
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- Tăng giới hạn để buộc tối ưu hơn; đổi điều kiện (ngày lẻ, số nhỏ nhất, giảm dần).
- Ghép với bài khác trong đề thi thử thành đề 4 bài / 90 phút.
