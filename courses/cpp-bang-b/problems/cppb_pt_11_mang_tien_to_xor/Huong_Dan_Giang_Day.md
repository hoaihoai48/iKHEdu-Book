# Hướng Dẫn Giảng Dạy: Prefix XOR
- Vì $x \oplus x = 0$, ta có: $\text{XOR}(L, R) = P[R] \oplus P[L-1]$ với $P[i] = P[i-1] \oplus A[i]$.
- Độ phức tạp: $\mathcal{O}(N + Q)$.
