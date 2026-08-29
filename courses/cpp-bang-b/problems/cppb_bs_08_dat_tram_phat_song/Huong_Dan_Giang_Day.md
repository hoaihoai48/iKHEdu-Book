# Hướng Dẫn Giảng Dạy: Aggressive Cows
- Sắp xếp tọa độ các điểm trong $\mathcal{O}(N \log N)$.
- Chặt nhị phân khoảng cách $D \in [1, X_N - X_1]$.
- Hàm `check(D)`: Tham lam đặt trạm đầu tại $X_0$, các trạm tiếp theo tại $X_i \ge \text{last} + D$. Đếm số trạm $\ge C$.
- Độ phức tạp: $\mathcal{O}(N \log(X_N - X_1))$.
