# Hướng Dẫn Giảng Dạy: Bitmask Subset Enumeration
- Vòng lặp `mask` từ $0$ đến $(1 << n) - 1$.
- Kiểm tra bit `(mask >> i) & 1`.
- Độ phức tạp: $\mathcal{O}(N \times 2^N)$.
