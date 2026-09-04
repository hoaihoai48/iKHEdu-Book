# Tìm Phần Tử Đa Số (Majority Element) D&C

## Bối cảnh
Trong các giao thức đồng thuận phân tán Byzantine, một phần tử được gọi là phần tử đa số nếu nó chiếm hơn một nửa tổng số phiếu bầu (tần suất > N / 2). Kỹ thuật chia để trị chia mảng làm 2 nửa: nếu tồn tại phần tử đa số trên toàn mảng thì phần tử đó bắt buộc phải là phần tử đa số của ít nhất một trong hai nửa.

## Nhiệm vụ
Cho mảng N số nguyên. Hãy tìm phần tử đa số (xuất hiện > N / 2 lần). Nếu không tồn tại, in ra -1.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra giá trị phần tử đa số, hoặc `-1`.

## Sample 1
### Input
```text
7
2 2 1 1 1 2 2
```
### Output
```text
2
```
### Giải thích
Số 2 xuất hiện 4 lần trên tổng số 7 phần tử (4 > 7/2 = 3.5). Do đó phần tử đa số là 2.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
