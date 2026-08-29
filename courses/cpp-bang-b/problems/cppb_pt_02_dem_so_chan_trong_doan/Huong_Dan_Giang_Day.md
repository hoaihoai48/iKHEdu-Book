# Hướng Dẫn Giảng Dạy: Đếm Số Chẵn
- Đặt $B[i] = 1$ nếu $A[i]$ chẵn, ngược lại $B[i] = 0$.
- Tính mảng tiền tố trên mảng $B$: `p[i] = p[i - 1] + (a[i] % 2 == 0)`.
- Độ phức tạp: $\mathcal{O}(N + Q)$.
