# Số Học Cực Hạn: Cặp Nguyên Tố Cùng Nhau & Phi Hàm Euler

## Bối cảnh
Trong hệ mật mã phi đối xứng hiện đại, phi hàm Euler phi(N) đếm số lượng các số nguyên dương nhỏ hơn hoặc bằng N nguyên tố cùng nhau với N. Hãy tính số lượng cặp số (x, y) với 1 <= x, y <= N sao cho gcd(x, y) = 1.

## Nhiệm vụ
Cho số nguyên dương N. Hãy đếm số lượng cặp số nguyên (x, y) thỏa mãn 1 <= x, y <= N và gcd(x, y) = 1.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
- In ra số lượng cặp nguyên tố cùng nhau.

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
Các cặp thỏa mãn với N = 3 gồm: (1, 1), (1, 2), (2, 1), (1, 3), (3, 1). Tổng cộng có 5 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
