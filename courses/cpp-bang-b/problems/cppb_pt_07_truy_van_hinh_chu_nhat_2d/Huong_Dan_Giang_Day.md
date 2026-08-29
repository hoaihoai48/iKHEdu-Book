# Hướng Dẫn Giảng Dạy: Prefix Sum 2D
- Bảng tiền tố 2D: `P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1] + A[i][j]`.
- Truy vấn: `P[x2][y2] - P[x1-1][y2] - P[x2][y1-1] + P[x1-1][y1-1]`.
- Độ phức tạp: Tiền xử lý $\mathcal{O}(N \times M)$, mỗi truy vấn $\mathcal{O}(1)$.
