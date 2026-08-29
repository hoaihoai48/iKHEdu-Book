# Hướng Dẫn Giảng Dạy: AND Pairs Frequency
- Vì $A_i < 4096$, đếm tần suất các số vào mảng `cnt[4096]`.
- Duyệt qua tất cả các cặp giá trị $(u, v)$ từ $0 \dots 4095$:
  - Nếu $u \ \& \ v == 0$: cộng thêm $cnt[u] \times cnt[v]$ (hoặc $cnt[u](cnt[u]-1)/2$ nếu $u=v=0$).
- Độ phức tạp: $\mathcal{O}(N + 4096^2) \approx 10^5 + 1.6 \cdot 10^7$ phép tính.
