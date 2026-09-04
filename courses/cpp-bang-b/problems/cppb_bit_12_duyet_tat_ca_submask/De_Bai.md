# Duyệt Tất Cả Các Tập Con Của Một Mặt Nạ Bit

## Bối cảnh
Trong kỹ thuật tối ưu hóa thuật toán quy hoạch động trên tập con SOS DP (Sum Over Subsets), với một mặt nạ bit N cho trước, việc duyệt qua toàn bộ các mặt nạ con (submask) có bit là tập con của N đòi hỏi thuật toán chuyển giao submask hiệu quả.

## Nhiệm vụ
Cho số nguyên dương N. Hãy liệt kê tất cả các số nguyên dương s là tập con bit của N (nghĩa là (s & N) == s với s > 0) theo thứ tự giảm dần.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
- In ra các số nguyên thỏa mãn cách nhau bởi khoảng trắng theo thứ tự giảm dần.

## Sample 1
### Input
```text
5
```
### Output
```text
5 4 1
```
### Giải thích
5 có biểu diễn nhị phân là 101_2. Các tập con bit dương của 101_2 gồm có: 101_2 (5), 100_2 (4) và 001_2 (1). Thứ tự giảm dần là: 5 4 1.

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
