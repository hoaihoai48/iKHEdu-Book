# Hướng Dẫn Giảng Dạy: Đếm Cặp Trùng Lặp
- Sắp xếp tăng dần. Dùng Two Pointers đếm số lượng phần tử bằng $A[L]$ ($c_1$) và $A[R]$ ($c_2$):
  - Nếu $A[L] == A[R] \implies$ cộng $c_1(c_1-1)/2$.
  - Nếu $A[L] \neq A[R] \implies$ cộng $c_1 \times c_2$.
- Độ phức tạp: $\mathcal{O}(N \log N)$.
