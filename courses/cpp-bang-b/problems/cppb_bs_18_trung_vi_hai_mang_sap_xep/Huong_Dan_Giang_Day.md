# Hướng Dẫn Giảng Dạy: Median of Two Sorted Arrays
- Giả sử $N \le M$ (nếu không đổi chỗ 2 mảng).
- Chặt nhị phân vị trí vách ngăn $i \in [0, N]$ trên mảng $A$, suy ra $j = (N + M + 1)/2 - i$ trên mảng $B$.
- Điều kiện vách ngăn hợp lệ: $A[i-1] \le B[j]$ và $B[j-1] \le A[i]$.
- Độ phức tạp: $\mathcal{O}(\log(\min(N, M)))$.
