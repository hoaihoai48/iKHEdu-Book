# Hướng Dẫn Giảng Dạy: Multidimensional Prefix Balance
- Đếm tiền tố: $cntA[i], cntB[i], cntC[i]$.
- Đoạn $[L \dots R]$ cân bằng khi:
  $cntA[R] - cntA[L-1] = cntB[R] - cntB[L-1] = cntC[R] - cntC[L-1]$.
  $\iff (cntA[R] - cntB[R], cntB[R] - cntC[R]) == (cntA[L-1] - cntB[L-1], cntB[L-1] - cntC[L-1])$.
- Lưu trạng thái $(diff1, diff2)$ vào vector 2 chiều và sắp xếp để tìm vị trí xuất hiện đầu tiên.
- Độ phức tạp: $\mathcal{O}(N \log N)$.
