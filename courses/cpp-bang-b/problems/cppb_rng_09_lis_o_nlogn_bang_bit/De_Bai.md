# Dãy Con Tăng Dài Nhất LIS Bằng Fenwick Tree

## Bối cảnh
Một dự án phân tích xu thế chuỗi thời gian lớn gồm $N$ số nguyên cần tìm độ dài của dãy con tăng nghiêm ngặt dài nhất với hiệu năng tính toán tối ưu nhất có thể.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tìm độ dài dãy con tăng nghiêm ngặt dài nhất.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là độ dài của dãy con tăng dài nhất.

## Sample 1
### Input
```text
6
5 2 7 4 3 8
```
### Output
```text
3
```

### Giải thích
Với dãy số gồm 6 phần tử $[10, 20, 10, 30, 20, 50]$:
Dãy con tăng dài nhất là $[10, 20, 30, 50]$ có độ dài bằng 4.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
