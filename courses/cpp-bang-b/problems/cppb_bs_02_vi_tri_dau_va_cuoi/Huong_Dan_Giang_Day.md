# Hướng Dẫn Giảng Dạy: lower_bound và upper_bound
- Dùng `lower_bound` tìm vị trí đầu tiên $\ge X$.
- Dùng `upper_bound` tìm vị trí đầu tiên $> X$.
- Kiểm tra xem $X$ có xuất hiện không: `low != a.end() && *low == X`.
- Vị trí đầu: `low - a.begin() + 1`. Vị trí cuối: `(upper - a.begin())`.
- Độ phức tạp: $\mathcal{O}(Q \log N)$.
