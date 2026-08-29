# Hướng Dẫn Giảng Dạy: Chênh Lệch Nhỏ Nhất Giữa 2 Mảng
- Sắp xếp cả 2 mảng tăng dần. Dùng Hai con trỏ $i, j$:
  - Nếu $A[i] < B[j] \implies ++i$.
  - Nếu $A[i] > B[j] \implies ++j$.
  - Nếu $A[i] == B[j] \implies$ chênh lệch bằng 0.
- Độ phức tạp: $\mathcal{O}(N \log N + M \log M)$.
