# Trò Chơi Sudoku 9x9

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho bảng Sudoku $9 \times 9$ với các ô trống mang giá trị `0`. Hãy điền các số từ $1$ đến $9$ vào các ô trống sao cho mỗi hàng, mỗi cột và mỗi khối vuông con $3 \times 3$ đều chứa đủ các chữ số từ $1$ đến $9$ không trùng lặp bằng thuật toán Quay Lui.

## Input
- 9 dòng, mỗi dòng chứa 9 số nguyên từ $0$ đến $9$.

## Output
- In ra bảng Sudoku hoàn chỉnh sau khi điền 9 dòng, mỗi dòng 9 số cách nhau bởi dấu cách.

## Sample 1
### Input
```text
3 0 6 5 0 8 4 0 0
5 2 0 0 0 0 0 0 0
0 8 7 0 0 0 0 3 1
0 0 3 0 1 0 0 8 0
9 0 0 8 6 3 0 0 5
0 5 0 0 9 0 6 0 0
1 3 0 0 0 0 2 5 0
0 0 0 0 0 0 0 7 4
0 0 5 2 0 6 3 0 0
```
### Output
```text
3 1 6 5 7 8 4 9 2
5 2 9 1 3 4 7 6 8
4 8 7 6 2 9 5 3 1
2 6 3 4 1 5 9 8 7
9 7 4 8 6 3 1 2 5
8 5 1 7 9 2 6 4 3
1 3 8 9 4 7 2 5 6
6 9 2 3 5 1 8 7 4
7 4 5 2 8 6 3 1 9
```
### Giải thích
Bảng Sudoku giải hoàn chỉnh duy nhất.

## Ràng buộc
- Đảm bảo bảng đầu vào có lời giải duy nhất.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
