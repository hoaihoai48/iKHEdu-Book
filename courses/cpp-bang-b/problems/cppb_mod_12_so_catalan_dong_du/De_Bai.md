# Số Catalan Đồng Dư

## Bối cảnh
Số Catalan C_N là con số huyền thoại trong toán học tổ hợp, xuất hiện trong bài toán đếm số dãy ngoặc đúng gồm N cặp ngoặc, số cây nhị phân có N đỉnh, và số cách chia đa giác lồi thành các tam giác. Hãy tính số Catalan thứ N theo modulo 10^9 + 7.

## Nhiệm vụ
Cho số nguyên N. Hãy tính số Catalan C_N = C(2N, N) / (N + 1) theo modulo 10^9 + 7.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
- In ra số Catalan $C_N \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
3
```
### Output
```text
5
```
### Giải thích
C_3 = C(6, 3) / (3 + 1) = 20 / 4 = 5. Kết quả in ra: 5.

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
