# Hướng Dẫn Giảng Dạy: Submask Enumeration
- Dùng thuật toán: `for (long long sub = n; sub > 0; sub = (sub - 1) & n)`.
- Độ phức tạp: $\mathcal{O}(2^{\text{popcount}(N)})$.
