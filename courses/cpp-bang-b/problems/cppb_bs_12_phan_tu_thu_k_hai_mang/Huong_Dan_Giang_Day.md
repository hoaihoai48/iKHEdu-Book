# Hướng Dẫn Giảng Dạy: K-th Element of Two Sorted Arrays
- Chặt nhị phân trên tập giá trị $X \in [-10^9, 10^9]$.
- Hàm `count_le(X)`: `upper_bound(A, X) + upper_bound(B, X)`.
- Tìm $X$ nhỏ nhất thỏa mãn `count_le(X) >= K`.
- Độ phức tạp: $\mathcal{O}(\log(\text{Range}) \times (\log N + \log M))$.
