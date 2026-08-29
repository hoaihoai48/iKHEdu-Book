# Hướng Dẫn Giảng Dạy: Single Number III
- XOR toàn bộ mảng được $S = X \oplus Y$.
- Vì $X \ne Y$, $S$ có ít nhất 1 bit 1. Tìm bit 1 nhỏ nhất: `diff_bit = S & (-S)`.
- Chia các số thành 2 nhóm: nhóm có bit đó bật và nhóm tắt.
- XOR riêng từng nhóm tìm được $X$ và $Y$.
- Độ phức tạp: $\mathcal{O}(N)$.
