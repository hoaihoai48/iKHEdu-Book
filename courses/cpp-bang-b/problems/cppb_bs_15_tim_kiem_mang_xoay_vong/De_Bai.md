# Tìm Kiếm Trên Mảng Sắp Xếp Bị Xoay Vòng (Rotated Array)

## Bối cảnh
Cho một mảng $N$ số nguyên phân biệt ban đầu đã sắp xếp tăng dần, nhưng bị xoay vòng tại một điểm bất kỳ không rõ (ví dụ: $[0, 1, 2, 4, 5, 6, 7]$ xoay vòng thành $[4, 5, 6, 7, 0, 1, 2]$). Có $Q$ câu hỏi, mỗi câu hỏi cho một số $X$, yêu cầu tìm vị trí của $X$ trong mảng (đánh số từ 1 đến $N$). Nếu không tồn tại, in ra `-1`.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên phân biệt của mảng xoay vòng $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm một số nguyên $X$ ($|X| \le 10^9$).

## Output
- In ra $Q$ dòng, mỗi dòng là vị trí của $X$ (1-based) hoặc `-1`.

## Sample 1
### Input
```text
7 2
4 5 6 7 0 1 2
0
3
```
### Output
```text
5
-1
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
