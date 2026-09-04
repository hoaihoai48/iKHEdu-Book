# So Sánh Đệ Quy Tuyến Tính & Chia Đôi Khi Tìm Min/Max

## Bối cảnh
Để minh họa sự khác biệt về độ sâu ngăn xếp cuộc gọi giữa đệ quy tuyến tính O(N) và đệ quy chia đôi (Binary Recursion) O(log N), hãy cài đặt hàm đệ quy chia đôi mảng thành 2 nửa để tìm đồng thời giá trị nhỏ nhất và lớn nhất của mảng N phần tử.

## Nhiệm vụ
Cho mảng số nguyên A gồm N phần tử. Hãy cài đặt hàm đệ quy chia đôi để tìm giá trị nhỏ nhất (min) và lớn nhất (max) trong mảng.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 2 số nguyên cách nhau bởi khoảng trắng: giá trị min và giá trị max.

## Sample 1
### Input
```text
5
3 1 9 4 2
```
### Output
```text
1 9
```
### Giải thích
Giá trị nhỏ nhất trong mảng là 1, giá trị lớn nhất là 9. Kết quả in ra: 1 9.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
