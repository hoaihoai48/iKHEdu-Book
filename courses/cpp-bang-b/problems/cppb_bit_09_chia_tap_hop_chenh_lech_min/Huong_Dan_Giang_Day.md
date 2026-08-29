# Hướng Dẫn Giảng Dạy: Apple Division
- Tính tổng mảng `total_sum`.
- Duyệt $mask$ từ $0$ đến $(1 << n) - 1$.
- Giỏ 1 có tổng $S_1$, giỏ 2 có tổng $S_2 = \text{total} - S_1$.
- Hiệu: $|S_1 - S_2| = |2 S_1 - \text{total}|$.
- Cập nhật min.
- Độ phức tạp: $\mathcal{O}(N \times 2^N)$.
