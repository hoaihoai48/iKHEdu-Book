# Kiểm tra tính chẵn lẻ của số nguyên

## Bối cảnh
Trong các bài toán số học, tính chẵn lẻ (parity) là một tính chất căn bản. Một số nguyên chia hết cho 2 được gọi là số chẵn, ngược lại được gọi là số lẻ. Bạn hãy lập trình kiểm tra tính chẵn lẻ của một số nguyên được nhập từ bàn phím.

## Nhiệm vụ
Cho một số nguyên $N$. Hãy lập trình kiểm tra:

- Nếu $N$ là số chẵn, in ra `CHAN`.
- Nếu $N$ là số lẻ, in ra `LE`.

## Input
- Một dòng duy nhất chứa số nguyên $N$ ($-10^{18} \le N \le 10^{18}$).

## Output
- In ra một dòng duy nhất chữ `CHAN` hoặc `LE`.

## Sample 1
### Input
```text
8
```
### Output
```text
CHAN
```

### Giải thích
Số $8$ chia hết cho $2$ (phần dư bằng $0$) nên là số chẵn. In ra `CHAN`.

## Sample 2
### Input
```text
-7
```
### Output
```text
LE
```

### Giải thích
Số $-7$ không chia hết cho $2$ nên là số lẻ. In ra `LE`.

## Ràng buộc
- $100\%$ số test có $-10^{18} \le N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
