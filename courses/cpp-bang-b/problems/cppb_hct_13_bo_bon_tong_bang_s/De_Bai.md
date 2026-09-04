# Bộ Bốn Số Có Tổng Bằng S (4-Sum)

## Bối cảnh
Trong một hệ thống mã hóa bảo mật tứ phân, máy chủ phân tích N giá trị khóa lượng tử A1, A2, ..., An. Để tạo ra khóa ký số chu kỳ tiếp theo, hệ thống cần chọn ra 4 thành phần khóa ở 4 vị trí phân biệt sao cho tổng năng lượng của 4 thành phần này đạt đúng giá trị kích hoạt S. Nếu có nhiều bộ bốn số thỏa mãn, hệ thống ghi nhận một bộ bất kỳ theo thứ tự tăng dần.

## Nhiệm vụ
Cho mảng gồm N số nguyên và số nguyên S. Hãy tìm 4 phần tử ở 4 vị trí phân biệt có tổng đúng bằng S. Nếu có nhiều bộ, in ra một bộ theo thứ tự tăng dần. Nếu không tồn tại, in ra -1.

## Input
- Dòng 1: 2 số nguyên $N$ và $S$ ($4 \le N \le 1000, -10^{18} \le S \le 10^{18}$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 4 số nguyên tăng dần hoặc `-1`.

## Sample 1
### Input
```text
6 20
2 7 5 1 8 4
```
### Output
```text
1 4 7 8
```
### Giải thích
Sắp xếp mảng tăng dần: [1, 2, 4, 5, 7, 8] và S = 20. Bộ bốn số gồm các phần tử 1, 4, 7, 8 có tổng là 1 + 4 + 7 + 8 = 20 đúng bằng S. Kết quả in ra: 1 4 7 8.

## Ràng buộc
- $100\%$ số test có $N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
