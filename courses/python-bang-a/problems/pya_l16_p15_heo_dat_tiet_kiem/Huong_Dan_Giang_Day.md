# Hướng Dẫn Giảng Dạy — Heo Đất Tiết Kiệm (`PYA-L16-P01`)

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- Học sinh giải được bài ở mức Dễ trong 90 phút thi thử.
- Rèn pattern ẩn: **vòng lặp + rẽ nhánh (tổng có điều kiện)**.
- Mục tiêu trong ma trận Bai_Tap.md: Rèn vòng lặp có điều kiện và phép đếm ngày chẵn.
- Chuẩn đầu ra: đọc đề contest không gợi ý, tự chọn công cụ, vét điểm từng subtask.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- Dữ kiện vào: xem mục Input trong De_Bai.md. Ràng buộc: $N \le 10^6$.
- Trường hợp biên: N = 1 (không có ngày chẵn nào); N lớn nhất.
- Đề giấu pattern: học sinh phải tự nhận ra công cụ từ câu chuyện, không được gợi ý trước.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. Đề cho những gì, hỏi cái gì? (Gạch chân dữ kiện.)
2. Với ví dụ nhỏ, em làm tay thế nào trước khi nghĩ đến code?
3. Trường hợp N = 0 / N = 1 thì đáp án là gì?
4. Subtask 1 giới hạn nhỏ cho phép cách làm đơn giản nào?

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- Bất biến: Số ngày chẵn trong N ngày đầu đúng bằng N // 2.
- Cách vét điểm: subtask 1 làm cách đơn giản (lặp trực tiếp) để lấy 50% điểm trước; subtask 2 mới cần cách nhanh.
- Độ phức tạp mục tiêu xem mục 6.

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

- N=5, A=10, B=3: số ngày chẵn là 5 // 2 = 2, thưởng 6, tổng 56.
- Khuyến khích học sinh kẻ bảng tay 3 cột: bước | giá trị hiện tại | kết quả.

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian ($\mathcal{O}(...)$)

- Thời gian $\mathcal{O}(N)$ (riêng bài tổng 1..N dùng công thức nên $\mathcal{O}(1)$), bộ nhớ $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$.

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- Dùng vòng lặp cộng từng ngày vẫn đúng nhưng công thức trực tiếp nhanh hơn; nhầm ngày chẵn với ngày lẻ.
- In thừa chữ giải thích gây Wrong Answer; sai định dạng số thập phân; quên test biên.

## 8. Mã Nguồn Tham Chiếu

```python
n, a, b = map(int, input().split())
print(n * a + (n // 2) * b)
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- Tăng giới hạn để buộc tối ưu hơn; đổi điều kiện (ngày lẻ, số nhỏ nhất, giảm dần).
- Ghép với bài khác trong đề thi thử thành đề 4 bài / 90 phút.
