# Bài toán người du lịch (tsp)

## Bối cảnh
Cho ma trận khoảng cách giữa $N$ thành phố ($N \le 18$). Tìm chi phí nhỏ nhất xuất phát từ thành phố 0, thăm tất cả các thành phố đúng 1 lần rồi quay về 0.

## Nhiệm vụ
Cho số nguyên $N$ và ma trận khoảng cách $C$ kích thước $N \times N$ giữa các thành phố. Hãy lập trình tìm chi phí nhỏ nhất của hành trình xuất phát từ thành phố $0$, thăm mỗi thành phố đúng một lần rồi quay về $0$, rồi in ra chi phí đó.

## Input
- Dòng 1: $N$. $N$ dòng tiếp theo: Ma trận khoảng cách $C_{i, j}$.

## Output
- In ra chi phí nhỏ nhất.

## Sample 1
### Input
```text
4
0 10 15 20
10 0 35 25
15 35 0 30
20 25 30 0
```
### Output
```text
80
```

### Giải thích
Xuất phát từ thành phố $0$, liệt kê mọi hành trình thăm mỗi thành phố đúng một lần rồi quay về $0$ cùng tổng chi phí:
- $0 \to 1 \to 2 \to 3 \to 0$: $10 + 35 + 30 + 20 = 95$.
- $0 \to 1 \to 3 \to 2 \to 0$: $10 + 25 + 30 + 15 = 80$.
- $0 \to 2 \to 1 \to 3 \to 0$: $15 + 35 + 25 + 20 = 95$.
- $0 \to 2 \to 3 \to 1 \to 0$: $15 + 30 + 25 + 10 = 80$.
- $0 \to 3 \to 1 \to 2 \to 0$: $20 + 25 + 35 + 15 = 95$.
- $0 \to 3 \to 2 \to 1 \to 0$: $20 + 30 + 35 + 10 = 95$.

Chi phí nhỏ nhất trong các hành trình trên là $80$. Vậy đáp án là $80$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
