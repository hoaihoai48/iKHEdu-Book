# Hướng Dẫn Giảng Dạy: Difference Array 2D
- Cập nhật 4 điểm trong $\mathcal{O}(1)$:
  `d[x1][y1] += v`, `d[x1][y2+1] -= v`, `d[x2+1][y1] -= v`, `d[x2+1][y2+1] += v`.
- Khôi phục ma trận bằng Prefix Sum 2D.
- Độ phức tạp: $\mathcal{O}(Q + N \times M)$.
