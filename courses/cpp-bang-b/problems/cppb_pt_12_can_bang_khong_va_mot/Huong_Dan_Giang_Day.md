# Hướng Dẫn Giảng Dạy: Cân Bằng 0 và 1
- Quy đổi: số 0 thành $-1$, số 1 giữ nguyên $+1$.
- Bài toán trở thành: Tìm đoạn con dài nhất có tổng bằng $0$ ($P[R] == P[L-1]$).
- Dùng mảng lưu vị trí xuất hiện đầu tiên của mỗi giá trị tiền tố (chuyển offset $+N$ để chỉ số luôn dương).
- Độ phức tạp: $\mathcal{O}(N)$.
