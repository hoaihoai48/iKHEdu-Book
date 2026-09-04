# Số Gần Nguyên Tố (Almost Prime)

## Bối cảnh
Trong lý thuyết sàng lọc số học, một số nguyên dương được gọi là 'gần nguyên tố' (2-Almost Prime) nếu nó có đúng 2 ước số nguyên tố phân biệt (ví dụ 6 = 2 * 3, 18 = 2 * 3^2). Hãy đếm xem trong khoảng từ 1 đến N có bao nhiêu số gần nguyên tố.

## Nhiệm vụ
Cho số nguyên dương N. Hãy đếm số lượng số nguyên trong đoạn [1, N] có đúng 2 ước số nguyên tố phân biệt.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 3000$).

## Output
- In ra số lượng số gần nguyên tố.

## Sample 1
### Input
```text
10
```
### Output
```text
2
```
### Giải thích
Trong đoạn [1, 10], các số có đúng 2 ước nguyên tố phân biệt là: 6 (ước 2, 3) và 10 (ước 2, 5). Tổng cộng có 2 số.

## Ràng buộc
- $100\%$ số test có $N \le 3000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
