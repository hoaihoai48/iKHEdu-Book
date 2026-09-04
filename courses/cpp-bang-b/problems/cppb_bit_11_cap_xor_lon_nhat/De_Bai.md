# Tìm Cặp Có XOR Lớn Nhất Trong Mảng

## Bối cảnh
Trong thuật toán tạo mã băm ngẫu nhiên, hệ thống cần tìm hai khóa bit số nguyên A[i] và A[j] trong danh sách N khóa để giá trị biểu thức XOR giữa chúng đạt mức độ tương phản nhị phân cao nhất (A[i] xor A[j] đạt giá trị lớn nhất).

## Nhiệm vụ
Cho mảng N số nguyên không âm. Hãy tìm giá trị lớn nhất của biểu thức A[i] ^ A[j] với 1 <= i < j <= N.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra giá trị XOR lớn nhất tìm được.

## Sample 1
### Input
```text
4
3 10 5 25
```
### Output
```text
28
```
### Giải thích
Cặp (5, 25) có 5 ^ 25 = 00101_2 ^ 11001_2 = 11100_2 = 28. Đây là giá trị XOR lớn nhất giữa 2 phần tử bất kỳ trong mảng.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
