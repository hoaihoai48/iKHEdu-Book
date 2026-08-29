# Hướng Dẫn Giảng Dạy: Maximum Submatrix Sum (Kadane 2D)
- Cố định 2 hàng $r1$ và $r2$.
- Dùng mảng tiền tố cột: $colSum[c] = P[r2][c] - P[r1-1][c]$.
- Áp dụng thuật toán Kadane 1D trên mảng $colSum$ để tìm đoạn con lớn nhất trong $\mathcal{O}(M)$.
- Tổng độ phức tạp: $\mathcal{O}(N^2 \times M)$ chạy dưới $0.2\text{s}$ với $N, M \le 400$.
