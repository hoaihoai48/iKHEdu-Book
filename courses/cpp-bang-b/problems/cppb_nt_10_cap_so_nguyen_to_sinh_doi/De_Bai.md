# Cặp Số Nguyên Tố Sinh Đôi (Twin Primes)

## Bối cảnh
Trong lý thuyết số giải thuật, giả thuyết về số nguyên tố sinh đôi là một bài toán nổi tiếng. Một cặp số (p, p + 2) được gọi là cặp số nguyên tố sinh đôi nếu cả p và p + 2 đều là số nguyên tố. Hãy đếm số lượng cặp nguyên tố sinh đôi không vượt quá N.

## Nhiệm vụ
Cho số nguyên dương N. Hãy đếm số lượng cặp số nguyên tố sinh đôi (p, p + 2) sao cho p + 2 <= N.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
- In ra số lượng cặp số nguyên tố sinh đôi.

## Sample 1
### Input
```text
20
```
### Output
```text
4
```
### Giải thích
Các cặp nguyên tố sinh đôi <= 20 là: (3, 5), (5, 7), (11, 13), (17, 19). Tổng cộng có 4 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
