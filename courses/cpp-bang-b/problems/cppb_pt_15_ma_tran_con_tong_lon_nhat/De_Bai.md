# Tìm Ma Trận Con Có Tổng Lớn Nhất (Max Submatrix Sum)

## Bối cảnh
Một tấm kim loại công nghiệp kích thước N x M có các điểm chịu nhiệt với hệ số truyền dẫn nhiệt ghi nhận trên từng ô ma trận (có cả số âm và số dương). Các kỹ sư cần cắt ra một tấm kim loại con hình chữ nhật bất kỳ sao cho tổng hệ số dẫn nhiệt của tấm cắt ra đạt mức cực đại.

## Nhiệm vụ
Cho ma trận số nguyên A kích thước N x M. Hãy tìm một ma trận con chữ nhật có tổng các phần tử là lớn nhất.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $M$ ($1 \le N, M \le 300$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $M$ số nguyên $A_{i, j}$ ($-10^9 \le A_{i, j} \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng lớn nhất của ma trận con tìm được.

## Sample 1
### Input
```text
3 3
1 2 -1
-8 -9 -2
3 4 5
```
### Output
```text
12
```
### Giải thích
Ma trận con ở hàng 3 gồm các phần tử [3, 4, 5] có tổng 3 + 4 + 5 = 12. Đây là ma trận con có tổng lớn nhất trong bảng.

## Ràng buộc
- $100\%$ số test có $N, M \le 300$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
