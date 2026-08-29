# Hướng Dẫn Giảng Dạy: Bitwise Independent Set
- Duyệt $mask$ từ $0$ đến $(1 << n) - 1$.
- Duy trì $used\_bits = 0$, duyệt từng phần tử $i$ thuộc mask: nếu $used\_bits \ \& \ A[i] \ne 0 \implies$ không hợp lệ. Ngược lại $used\_bits \ |= A[i]$.
- Cập nhật max $\text{popcount}(mask)$.
- Độ phức tạp: $\mathcal{O}(N \times 2^N)$ với $N \le 22$.
