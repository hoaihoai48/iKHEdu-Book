# Phát Hiện Chu Trình Trên Đồ Thị Vô Hướng

## Bối cảnh
Một mạng lưới đường ống cấp nước đô thị cần được kiểm tra thiết kế. Nếu trong mạng lưới xuất hiện một chu trình khép kín (một vòng tròn đường ống quay về điểm xuất phát mà không đi lặp lại cạnh nào), áp lực nước có thể bị nhiễu loạn dòng chảy. Kỹ sư thủy lợi cần kiểm tra xem bản vẽ mạng lưới có chứa chu trình hay không.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình kiểm tra xem đồ thị có chứa chu trình hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- In ra `YES` nếu đồ thị chứa ít nhất một chu trình, ngược lại in ra `NO`.

## Sample 1
### Input
```text
3 3
1 2
2 3
3 1
```
### Output
```text
YES
```

### Giải thích
Với đồ thị gồm 3 đỉnh có các cạnh (1, 2), (2, 3), (3, 1):
Ba đỉnh này tạo thành một tam giác khép kín $1 - 2 - 3 - 1$, là một chu trình hoàn chỉnh. Kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
