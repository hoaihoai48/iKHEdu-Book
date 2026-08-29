# Hướng Dẫn Giảng Dạy: Find Peak in Mountain Array
- So sánh $A[mid]$ và $A[mid + 1]$.
- Nếu $A[mid] < A[mid + 1] \implies$ đỉnh nằm bên phải $\implies low = mid + 1$.
- Ngược lại $\implies$ đỉnh nằm ở $mid$ hoặc bên trái $\implies high = mid$.
- Độ phức tạp: $\mathcal{O}(\log N)$.
