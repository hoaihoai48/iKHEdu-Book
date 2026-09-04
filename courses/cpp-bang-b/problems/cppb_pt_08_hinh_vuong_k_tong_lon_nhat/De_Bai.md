# Tìm Hình Vuông K x K Có Tổng Lớn Nhất

## Bối cảnh
Một vệ tinh nông nghiệp chụp ảnh khu đất canh tác dưới dạng ma trận N x M, mỗi ô thể hiện sản lượng lúa dự kiến thu hoạch. Nhà đầu tư muốn thuê một mảnh đất hình vuông kích thước đúng K x K ô đất liền kề nhau sao cho tổng sản lượng thu hoạch trên mảnh đất thuê là lớn nhất có thể.

## Nhiệm vụ
Cho ma trận A kích thước N x M và số nguyên dương K (K <= min(N, M)). Hãy tìm tổng lớn nhất của một ma trận con hình vuông kích thước K x K.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, K$ ($1 \le K \le \min(N, M) \le 1000$).
- $N$ dòng tiếp theo: Mỗi dòng chứa $M$ số nguyên $A_{i, j}$ ($-10^9 \le A_{i, j} \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng lớn nhất của hình vuông $K \times K$.

## Sample 1
### Input
```text
3 3 2
1 1 1
1 2 2
1 2 3
```
### Output
```text
9
```
### Giải thích
Hình vuông kích thước 2 x 2 ở góc dưới phải gồm các ô: {2, 2, 2, 3} có tổng là 2 + 2 + 2 + 3 = 9. Đây là hình vuông kích thước 2 x 2 có tổng lớn nhất.

## Ràng buộc
- $100\%$ số test có $N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
