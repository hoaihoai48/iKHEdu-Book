# Hướng Dẫn Giảng Dạy: Tổng Chia Hết Cho K
- Tính tiền tố $P_i$, lấy dư $M_i = (P_i \% K + K) \% K$.
- Đếm số lần xuất hiện của mỗi số dư $0 \dots K-1$ vào mảng `cnt`.
- Với mỗi số dư $r$, số cặp tạo thành tổng chia hết cho $K$ là $\frac{cnt[r] \times (cnt[r] - 1)}{2}$.
- Độ phức tạp: $\mathcal{O}(N + K)$.
