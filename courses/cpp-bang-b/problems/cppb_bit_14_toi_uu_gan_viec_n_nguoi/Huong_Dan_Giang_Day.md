# Hướng Dẫn Giảng Dạy: Bitmask DP / Permutation Min Cost
- $DP[mask]$ là chi phí tối thiểu để giao công việc cho tập nhân viên biểu diễn bởi $mask$.
- Số công việc đã giao = $\text{popcount}(mask)$.
- Chuyển trạng thái: Duyệt thêm nhân viên $j$ chưa được giao việc.
- Độ phức tạp: $\mathcal{O}(N \times 2^N)$ với $N = 16$ mất $16 \times 65536 \approx 10^6$ thao tác.
