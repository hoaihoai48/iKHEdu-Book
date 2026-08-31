# Chia Tập Thành Hai Phần Bằng Nhau (Partition Equal Subset Sum)

## Bối cảnh
Cho mảng gồm $N$ số nguyên dương. Kiểm tra xem có thể chia mảng thành 2 tập hợp con rời nhau sao cho tổng các phần tử ở mỗi tập bằng nhau hay không.

## Nhiệm vụ
In ra `YES` nếu có thể chia được, ngược lại in `NO`.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 500$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- `YES` hoặc `NO`.

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

## Ràng buộc
- $100\%$ số test có $1 \le N \le 500, 1 \le A_i \le 100$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
