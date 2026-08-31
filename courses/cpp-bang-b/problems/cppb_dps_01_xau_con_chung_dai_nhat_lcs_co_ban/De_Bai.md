# Xâu Con Chung Dài Nhất Cơ Bản (LCS)

## Bối cảnh
Cho hai chuỗi ký tự $S$ và $T$. Một xâu con chung là một chuỗi xuất hiện trong cả hai chuỗi theo đúng thứ tự tương đối nhưng không nhất thiết phải liền kề.

## Nhiệm vụ
Tìm độ dài của xâu con chung dài nhất giữa $S$ và $T$.

## Input
- Dòng 1: Chuỗi ký tự $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chuỗi ký tự $T$ ($1 \le |T| \le 2000$).

## Output
- Độ dài LCS.

## Sample 1
### Input
```text
AGGTAB
GXTXAYB
```
### Output
```text
4
```

## Ràng buộc
- $100\%$ số test có $1 \le |S|, |T| \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
