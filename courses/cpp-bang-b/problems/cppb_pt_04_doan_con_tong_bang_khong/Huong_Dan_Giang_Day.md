# Hướng Dẫn Giảng Dạy: Tổng Bằng 0
- Tính mảng tiền tố $P_0 = 0, P_1, \dots, P_N$.
- Đoạn $[L \dots R]$ có tổng bằng $0 \iff P_R = P_{L-1}$.
- Sắp xếp mảng tiền tố $P$ gồm $N+1$ phần tử, nếu có 2 phần tử kề nhau bằng nhau $\implies$ YES.
- Độ phức tạp: $\mathcal{O}(N \log N)$ không cần dùng hash map.
