# Kiểm Tra Đồ Thị Cây (Tree Verification)

## Bối cảnh
Trong cấu trúc liên kết mạng máy tính, cấu trúc dạng cây (Tree) là mô hình mạng tối ưu nhất vì nó đảm bảo tất cả $N$ máy chủ đều liên thông với nhau mà hoàn toàn không có chu trình dư thừa (số lượng kênh kết nối đúng bằng $N - 1$). Kỹ sư hệ thống cần xác thực xem một mạng lưới cho trước có thỏa mãn đầy đủ các điều kiện của một đồ thị cây hay không.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình kiểm tra xem đồ thị có phải là một cây hợp lệ hay không. Nếu đúng in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.

## Output
- In ra `YES` nếu đồ thị là cây, ngược lại in ra `NO`.

## Sample 1
### Input
```text
4 3
1 2
2 3
3 4
```
### Output
```text
YES
```

### Giải thích
Với đồ thị có $N = 4$ đỉnh và $M = 3$ cạnh: (1, 2), (1, 3), (1, 4):
Đồ thị liên thông toàn bộ và không chứa bất kỳ chu trình nào, số cạnh đúng bằng $4 - 1 = 3$. Đồ thị là một cây, kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
