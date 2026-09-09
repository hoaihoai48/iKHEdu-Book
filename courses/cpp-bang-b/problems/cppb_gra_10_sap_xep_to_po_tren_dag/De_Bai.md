# Sắp Xếp Tô-pô (Topological Sort)

## Bối cảnh
Một chương trình đào tạo kỹ sư công nghệ thông tin gồm $N$ môn học được đánh số từ $1$ đến $N$. Giữa các môn học có $M$ điều kiện môn tiên quyết dạng $u × o v$ (nghĩa là sinh viên bắt buộc phải hoàn thành môn học $u$ trước khi được phép đăng ký môn học $v$). Ban đào tạo cần lập ra một lộ trình học tập hợp lệ thỏa mãn tất cả các điều kiện tiên quyết.

## Nhiệm vụ
Cho đồ thị có hướng $N$ đỉnh $M$ cạnh không có chu trình. Hãy lập trình tìm một thứ tự sắp xếp tô-pô của các môn học.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$ biểu diễn điều kiện môn $u$ học trước môn $v$.

## Output
- In ra trên một dòng gồm $N$ số nguyên là thứ tự các môn học hợp lệ, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
4 3
1 2
2 3
1 3
```
### Output
```text
1 4 2 3
```

### Giải thích
Với 3 môn học và các điều kiện: môn 1 trước môn 2 ($1 × o 2$), môn 2 trước môn 3 ($2 × o 3$):
Lộ trình học tập bắt buộc duy nhất là: 1 2 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
