# Hướng Dẫn Giảng Dạy: Bit Inversion Mask
- Tìm số bit của $N$: $L = 64 - \text{__builtin_clzll}(N)$.
- Mặt nạ toàn bit 1: `mask = (1LL << L) - 1`.
- Kết quả: `N ^ mask`.
- Độ phức tạp: $\mathcal{O}(1)$.
