# Chia Tập Thành Hai Phần Bằng Nhau (Partition Equal Subset Sum)

## Bối cảnh
Một gia đình có hai người con được thừa kế $N$ thửa đất. Thửa đất thứ $i$ có giá trị thẩm định là $A_i$. Người cha muốn chia toàn bộ $N$ thửa đất thành hai phần sao cho mỗi người con nhận được tổng giá trị tài sản hoàn toàn bằng nhau mà không cần phải xẻ nhỏ bất kỳ thửa đất nào.

## Nhiệm vụ
Cho danh sách giá trị của $N$ thửa đất. Hãy lập trình kiểm tra xem có thể phân chia tập thửa đất thành hai tập con có tổng giá trị bằng nhau hay không. Nếu được in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 200$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- In ra `YES` nếu có thể chia đều thành hai phần bằng nhau, ngược lại in ra `NO`.

## Sample 1
### Input
```text
4
1 5 11 5
```
### Output
```text
YES
```

### Giải thích
Với tập hợp các số $[1, 5, 11, 5]$:
Tổng của toàn bộ dãy số là $1 + 5 + 11 + 5 = 22$. Ta có thể chia thành hai tập con $\{1, 5, 5\}$ và $\{11\}$, mỗi tập đều có tổng đúng bằng 11. Do đó kết quả in ra là YES.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 500, 1 \le A_i \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
