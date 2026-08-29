# Hướng Dẫn Giảng Dạy: Search in Rotated Sorted Array
- Tại mỗi bước, ít nhất một nửa $[low \dots mid]$ hoặc $[mid \dots high]$ được sắp xếp tăng dần.
- Nếu nửa trái sắp xếp: kiểm tra xem $X \in [A[low], A[mid]]$ không để chọn nửa tiếp theo.
- Nếu nửa phải sắp xếp: kiểm tra xem $X \in [A[mid], A[high]]$ không.
- Độ phức tạp: $\mathcal{O}(Q \log N)$.
