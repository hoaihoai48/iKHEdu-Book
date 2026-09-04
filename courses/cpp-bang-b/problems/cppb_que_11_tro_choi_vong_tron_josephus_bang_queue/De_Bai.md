# Trò Chơi Vòng Tròn Josephus

## Bối cảnh
Trong một trò chơi dân gian, $N$ bạn học sinh đứng thành một vòng tròn và được đánh số từ $1$ đến $N$ theo chiều kim đồng hồ. Bắt đầu đếm từ bạn số 1, cứ mỗi khi đếm đến người thứ $K$ thì người đó sẽ phải rời khỏi vòng tròn. Quá trình đếm tiếp tục với người đứng kế tiếp cho đến khi chỉ còn lại đúng một người cuối cùng trụ lại.

## Nhiệm vụ
Cho số lượng người $N$ và bước đếm $K$. Hãy lập trình xác định số thứ tự của người cuối cùng còn lại trong vòng tròn.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $N$ và $K$ ($1 \le N \le 10^5, 1 \le K \le 100$).

## Output
- In ra một số nguyên duy nhất là vị trí của người trụ lại cuối cùng.

## Sample 1
### Input
```text
7 3
```
### Output
```text
4
```

### Giải thích
Với $N = 7$ người và bước đếm $K = 3$:
Thứ tự các người bị loại lần lượt là: 3, 6, 2, 7, 5, 1. Người cuối cùng còn lại là người số 4.

## Ràng buộc
- $100\%$ số test có $1 \le N, K \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
