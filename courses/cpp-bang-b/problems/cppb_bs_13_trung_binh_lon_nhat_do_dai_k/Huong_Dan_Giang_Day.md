# Hướng Dẫn Giảng Dạy: Maximum Average Subarray >= K
- Chặt nhị phân giá trị trung bình $X \in [0, \max A]$.
- Chuyển mảng thành $B_i = A_i - X$. Tồn tại đoạn $\ge K$ có trung bình $\ge X \iff$ tồn tại đoạn $\ge K$ trên mảng $B$ có tổng $\ge 0$.
- Xây dựng mảng tiền tố trên $B$: $P_i = P_{i-1} + B_i$. Đoạn $[j+1, i]$ độ dài $\ge K \iff i - j \ge K$.
- Duy trì $\min_{0 \le j \le i-K} P_j$. Nếu $P_i - \min P_j \ge 0 \implies$ thỏa mãn.
- Độ phức tạp: $\mathcal{O}(80 \times N)$.
