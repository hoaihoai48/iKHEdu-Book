# Mã Đi Tuần (Knight's Tour)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho bàn cờ $N \times N$. Quân mã xuất phát từ ô $(R, C)$ (1-based). Hãy tìm một hành trình di chuyển quân mã đi qua tất cả $N^2$ ô đúng 1 lần bằng thuật toán Quay Lui kết hợp quy tắc sắp xếp thứ tự nhánh Warnsdorff. In ra ma trận $N \times N$ ghi số thứ tự các bước đi từ $1$ đến $N^2$, hoặc `-1` nếu không có.

## Input
- Một dòng duy nhất chứa 3 số nguyên $N, R, C$ ($1 \le N \le 6, 1 \le R, C \le N$).

## Output
- In ra ma trận $N \times N$ các bước đi, hoặc `-1`.

## Sample 1
### Input
```text
5 1 1
```
### Output
```text
1 16 11 6 25
10 5 24 15 20
17 2 19 22 7
4 9 14 21 12
3 18 23 8 13
```
### Giải thích
Một hành trình mã đi tuần hoàn chỉnh trên bàn cờ 5x5.

## Ràng buộc
- 100% số test có $N \le 6, 1 \le R, C \le N$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
