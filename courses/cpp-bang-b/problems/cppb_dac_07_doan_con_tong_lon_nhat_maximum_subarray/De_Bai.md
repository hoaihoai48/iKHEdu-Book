# Đoạn Con Tổng Lớn Nhất (Maximum Subarray D&C)

## Bối cảnh
Bài toán tìm đoạn con liên tiếp có tổng lớn nhất trong một chuỗi số tài chính (có cả số âm và số dương) được giải quyết bằng chia để trị: đoạn con tối ưu có thể nằm hoàn toàn ở nửa trái, nằm hoàn toàn ở nửa phải, hoặc bắt qua điểm chính giữa (Crossing Subarray).

## Nhiệm vụ
Cho mảng N số nguyên. Hãy tìm tổng lớn nhất của một đoạn con liên tiếp khác rỗng bằng thuật toán Chia để trị.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra tổng lớn nhất của đoạn con.

## Sample 1
### Input
```text
8
-2 -3 4 -1 -2 1 5 -3
```
### Output
```text
7
```
### Giải thích
Đoạn con [4, -1, -2, 1, 5] từ vị trí 3 đến vị trí 7 có tổng là 4 - 1 - 2 + 1 + 5 = 7. Đây là đoạn con có tổng lớn nhất.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
