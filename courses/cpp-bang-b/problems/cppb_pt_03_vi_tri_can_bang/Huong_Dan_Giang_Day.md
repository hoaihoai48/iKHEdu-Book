# Hướng Dẫn Giảng Dạy: Vị Trí Cân Bằng
- Tính tổng mảng `total`.
- Duyệt $i$ từ $1 \to N$: duy trì `left_sum = p[i - 1]`, `right_sum = total - p[i]`.
- Nếu `left_sum == right_sum` thì in $i$ và kết thúc.
- Độ phức tạp: $\mathcal{O}(N)$.
