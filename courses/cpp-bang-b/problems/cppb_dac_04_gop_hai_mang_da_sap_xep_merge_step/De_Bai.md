# Gộp Hai Mảng Đã Sắp Xếp (Merge Step)

## Bối cảnh
Thao tác gộp (Merge) hai mảng đã có thứ tự thành một mảng có thứ tự duy nhất là bước kết hợp (Combine) nền tảng của thuật toán kinh điển Merge Sort. Kỹ thuật hai con trỏ cho phép gộp hai mảng kích thước N và M trong đúng O(N + M).

## Nhiệm vụ
Cho 2 mảng tăng dần A (kích thước N) và B (kích thước M). Hãy gộp hai mảng thành một dãy tăng dần duy nhất.

## Input
- Dòng 1: 2 số nguyên dương $N$ và $M$ ($1 \le N, M \le 10^5$).
- Dòng 2: $N$ số nguyên tăng dần của mảng $A$.
- Dòng 3: $M$ số nguyên tăng dần của mảng $B$.

## Output
- In ra $N + M$ số nguyên theo thứ tự tăng dần sau khi gộp.

## Sample 1
### Input
```text
3 3
1 4 7
2 5 6
```
### Output
```text
1 2 4 5 6 7
```
### Giải thích
Gộp hai mảng [1, 4, 7] và [2, 5, 6] ta được mảng tăng dần hoàn chỉnh: 1 2 4 5 6 7.

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
