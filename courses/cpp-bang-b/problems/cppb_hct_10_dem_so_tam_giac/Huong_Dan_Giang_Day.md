# Hướng Dẫn Giảng Dạy: Đếm Tam Giác
- Sắp xếp tăng dần. Cố định cạnh lớn nhất $k$ từ $N-1$ về $2$.
- Dùng Two Pointers $L = 0, R = k - 1$. Khi $A[L] + A[R] > A[k] \implies$ có $R - L$ cặp, sau đó $--R$. Ngược lại $++L$.
- Độ phức tạp: $\mathcal{O}(N^2)$.
