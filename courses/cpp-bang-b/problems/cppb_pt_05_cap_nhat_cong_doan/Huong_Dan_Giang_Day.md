# Hướng Dẫn Giảng Dạy: Mảng Hiệu 1D
- Mảng hiệu $D$ kích thước $N + 2$.
- Thao tác $L, R, V$: `D[L] += V`, `D[R + 1] -= V`.
- Khôi phục: `A[i] = A[i - 1] + D[i]`.
- Độ phức tạp: $\mathcal{O}(N + Q)$.
