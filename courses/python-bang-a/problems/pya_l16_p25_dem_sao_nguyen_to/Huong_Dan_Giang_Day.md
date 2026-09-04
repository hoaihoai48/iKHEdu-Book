# Hướng Dẫn Giảng Dạy — Đếm Sao Nguyên Tố (`PYA-L16-P11`)

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

- Học sinh giải được bài ở mức Khó trong 90 phút thi thử.
- Rèn pattern ẩn: **vòng lặp lồng nhau (sàng / kiểm tra nguyên tố đến N)**.
- Mục tiêu trong ma trận Bai_Tap.md: Rèn kiểm tra nguyên tố và vét điểm subtask nhỏ trước.
- Chuẩn đầu ra: đọc đề contest không gợi ý, tự chọn công cụ, vét điểm từng subtask.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)

- Dữ kiện vào: xem mục Input trong De_Bai.md. Ràng buộc: $N \le 10^6$.
- Trường hợp biên: N = 1 (đáp án 0); N = 2 (đáp án 1).
- Đề giấu pattern: học sinh phải tự nhận ra công cụ từ câu chuyện, không được gợi ý trước.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)

1. Đề cho những gì, hỏi cái gì? (Gạch chân dữ kiện.)
2. Với ví dụ nhỏ, em làm tay thế nào trước khi nghĩ đến code?
3. Trường hợp N = 0 / N = 1 thì đáp án là gì?
4. Subtask 1 giới hạn nhỏ cho phép cách làm đơn giản nào?

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)

- Bất biến: Sau khi xét i, mọi hợp số có ước nhỏ nhất bằng i đều đã bị gạch.
- Cách vét điểm: subtask 1 làm cách đơn giản (lặp trực tiếp) để lấy 50% điểm trước; subtask 2 mới cần cách nhanh.
- Độ phức tạp mục tiêu xem mục 6.

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)

- N = 10: gạch các bội của 2, 3 còn lại 2, 3, 5, 7 nên đáp án 4.
- Khuyến khích học sinh kẻ bảng tay 3 cột: bước | giá trị hiện tại | kết quả.

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian ($\mathcal{O}(...)$)

- Thời gian $\mathcal{O}(N)$ (riêng bài tổng 1..N dùng công thức nên $\mathcal{O}(1)$), bộ nhớ $\mathcal{O}(N)$ hoặc $\mathcal{O}(1)$.

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

- Tưởng số 1 là số nguyên tố; kiểm tra nguyên tố đến N thay vì đến căn N gây chậm.
- In thừa chữ giải thích gây Wrong Answer; sai định dạng số thập phân; quên test biên.

## 8. Mã Nguồn Tham Chiếu

```python
n = int(input())
if n < 2:
    print(0)
else:
    is_p = [True] * (n + 1)
    is_p[0] = False
    is_p[1] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            j = i * i
            while j <= n:
                is_p[j] = False
                j += i
        i += 1
    print(sum(is_p))
```

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)

- Tăng giới hạn để buộc tối ưu hơn; đổi điều kiện (ngày lẻ, số nhỏ nhất, giảm dần).
- Ghép với bài khác trong đề thi thử thành đề 4 bài / 90 phút.
