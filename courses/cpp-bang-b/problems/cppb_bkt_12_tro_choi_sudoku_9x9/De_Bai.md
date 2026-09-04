# Trò Chơi Sudoku 9x9

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Tại vòng chung kết cuộc thi Trí tuệ Logic học sinh giỏi, các thí sinh nhận được một bảng Sudoku kích thước tiêu chuẩn $9 \times 9$ trong đó một số ô đã có sẵn số từ $1$ đến $9$, còn các ô trống được ký hiệu bằng số `0`. Để tự động hóa khâu chấm thi và kiểm tra đáp án, ban giám khảo cần một chương trình tự động giải quyết bàn cờ Sudoku này dựa trên các quy tắc chuẩn quốc tế.

## Nhiệm vụ
Cho bảng Sudoku $9 \times 9$ với các ô trống mang giá trị `0`. Hãy sử dụng thuật toán Quay lui để điền các chữ số từ $1$ đến $9$ vào các ô trống sao cho: mỗi hàng, mỗi cột và mỗi khối vuông con $3 \times 3$ đều chứa đủ 9 chữ số từ $1$ đến $9$ không lặp lại. Đảm bảo dữ liệu đầu vào luôn có nghiệm duy nhất.

## Input
- Gồm 9 dòng, mỗi dòng chứa 9 số nguyên từ $0$ đến $9$ cách nhau bởi dấu cách biểu diễn bảng Sudoku ban đầu.

## Output
- In ra bảng Sudoku hoàn chỉnh sau khi điền gồm 9 dòng, mỗi dòng 9 số cách nhau bởi dấu cách.

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
Tất cả các số 0 được thay thế bằng các chữ số từ 1 đến 9 thỏa mãn trọn vẹn quy tắc: hàng ngang, cột dọc và các phân vùng $3 \times 3$ đều không có số nào bị lặp lại.

## Ràng buộc
- Dữ liệu đầu vào luôn hợp lệ và đảm bảo có đúng 1 lời giải duy nhất.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
