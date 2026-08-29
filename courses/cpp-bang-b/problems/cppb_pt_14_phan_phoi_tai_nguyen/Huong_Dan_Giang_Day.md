# Hướng Dẫn Giảng Dạy: Mảng Hiệu Cấp 2
- Cập nhật cấp số cộng bằng Mảng hiệu bậc 2 (Second Difference Array).
- $D2[L] += S$, $D2[L+1] += D - S$, $D2[R+1] -= S + (R-L+1)D$, $D2[R+2] += S + (R-L)D$.
- Chạy 2 lần Prefix Sum liên tiếp để khôi phục mảng ban đầu.
- Độ phức tạp: $\mathcal{O}(N + Q)$.
