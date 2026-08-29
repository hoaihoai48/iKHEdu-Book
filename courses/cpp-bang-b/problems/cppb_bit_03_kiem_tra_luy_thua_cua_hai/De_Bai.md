# Kiểm Tra Số Có Phải Lũy Thừa Của 2

## Bối cảnh
Cho một số nguyên dương $N$ ($1 \le N \le 10^{18}$). Hãy kiểm tra xem $N$ có phải là một lũy thừa của 2 hay không (tức tồn tại số nguyên không âm $k$ sao cho $N = 2^k$).

## Input
- Dòng 1: Số nguyên $T$ ($1 \le T \le 10^5$) là số lượng testcase.
- $T$ dòng tiếp theo: Mỗi dòng gồm một số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra $T$ dòng, mỗi dòng in `YES` nếu là lũy thừa của 2, ngược lại in `NO`.

## Sample 1
### Input
```text
3
16
18
1
```
### Output
```text
YES
NO
YES
```
*(Giải thích: $16 = 2^4$ (YES), $18$ không phải (NO), $1 = 2^0$ (YES)).*

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
