# Kiểm Tra Số Hoàn Hảo

## Bối cảnh
Một số nguyên dương $N$ được gọi là số hoàn hảo nếu tổng tất cả các ước số thực sự của nó (không kể chính nó) bằng $N$. Cho số $N$, hãy kiểm tra $N$ có phải số hoàn hảo.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra `YES` nếu $N$ là số hoàn hảo, ngược lại in `NO`.

## Sample 1
### Input
```text
28
```
### Output
```text
YES
```
### Giải thích
Các ước của 28 (trừ 28) là 1 + 2 + 4 + 7 + 14 = 28.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.\n- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
