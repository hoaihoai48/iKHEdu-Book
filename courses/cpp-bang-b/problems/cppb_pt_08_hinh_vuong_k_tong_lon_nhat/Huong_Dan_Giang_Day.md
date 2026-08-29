# Hướng Dẫn Giảng Dạy: Hình Vuông KxK
- Xây dựng Prefix Sum 2D.
- Duyệt mọi ô $(i, j)$ từ $K$ đến $N, M$ làm góc phải dưới:
  `Sum = p[i][j] - p[i-K][j] - p[i][j-K] + p[i-K][j-K]`.
- Cập nhật max.
- Độ phức tạp: $\mathcal{O}(N \times M)$.
