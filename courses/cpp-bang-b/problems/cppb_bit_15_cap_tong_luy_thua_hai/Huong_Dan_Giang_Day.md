# Hướng Dẫn Giảng Dạy: Power of Two Pairs
- Sắp xếp mảng $A$.
- Vì $A_i \le 10^9$, $A_i + A_j \le 2 \cdot 10^9 \implies$ Chỉ có 31 lũy thừa của 2 từ $2^1$ đến $2^{30}$.
- Với mỗi phần tử $A_i$, duyệt qua 31 giá trị $2^k$. Tìm số lượng phần tử bằng $2^k - A_i$ trong mảng bằng `upper_bound - lower_bound`.
- Độ phức tạp: $\mathcal{O}(31 \times N \log N)$.
