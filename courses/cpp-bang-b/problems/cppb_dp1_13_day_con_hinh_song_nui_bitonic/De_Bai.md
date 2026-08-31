# Dãy Con Hình Sóng Núi (Longest Bitonic Subsequence)

## Bối cảnh
Một dãy con được gọi là có dạng hình sóng núi (Bitonic) nếu ban đầu tăng dần nghiêm ngặt rồi sau đó giảm dần nghiêm ngặt.

## Nhiệm vụ
Tìm độ dài lớn nhất của một dãy con hình sóng núi từ mảng ban đầu.

## Input
- Dòng 1: Số nguyên $N$ ($1 \le N \le 2000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- Độ dài lớn nhất của dãy con hình sóng núi.

## Sample 1
### Input
```text
8
1 11 2 10 4 5 2 1
```
### Output
```text
6
```

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
