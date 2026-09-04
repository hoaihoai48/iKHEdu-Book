# Tập Hợp Độc Lập Về Bit Lớn Nhất

## Bối cảnh
Một tập hợp N từ mã nhị phân được lưu trữ trong bộ nhớ ROM. Hai từ mã được coi là hoàn toàn độc lập nếu chúng không có bất kỳ bit 1 nào trùng nhau (tức A[i] & A[j] == 0). Hãy tìm kích thước lớn nhất của một tập con các từ mã mà giữa hai từ mã bất kỳ trong tập con đều không xung đột bit (đôi một có tích bit AND bằng 0).

## Nhiệm vụ
Cho tập hợp N số nguyên dương (N <= 22). Hãy tìm kích thước lớn nhất của một tập con mà hai phần tử bất kỳ trong tập con đều có tích bit AND bằng 0.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 22$).
- Dòng 2: $N$ số nguyên dương $A_0, A_1, \dots, A_{N-1}$ ($1 \le A_i \le 10^9$).

## Output
- In ra số lượng phần tử lớn nhất của tập con độc lập về bit.

## Sample 1
### Input
```text
4
1 2 4 3
```
### Output
```text
3
```
### Giải thích
Tập con {1, 2, 4} gồm 3 số có các bit 1 độc lập từng đôi một: (1&2=0, 1&4=0, 2&4=0). Số lượng phần tử lớn nhất là 3.

## Ràng buộc
- $100\%$ số test có $N \le 22$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
