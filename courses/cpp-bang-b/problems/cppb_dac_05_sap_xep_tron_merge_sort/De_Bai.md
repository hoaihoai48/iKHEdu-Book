# Thuật Toán Sắp Xếp Trộn (Merge Sort)

## Bối cảnh
Thuật toán sắp xếp trộn Merge Sort do John von Neumann phát minh năm 1945 là biểu tượng kinh điển của phương pháp chia để trị, đảm bảo độ phức tạp thời gian O(N log N) trong mọi trường hợp (kể cả trường hợp xấu nhất) và là thuật toán sắp xếp ổn định (Stable Sort).

## Nhiệm vụ
Cho mảng N số nguyên. Hãy tự cài đặt hoàn chỉnh thuật toán Merge Sort chia để trị để sắp xếp mảng theo thứ tự tăng dần.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra dãy số sau khi sắp xếp tăng dần.

## Sample 1
### Input
```text
5
4 2 1 5 3
```
### Output
```text
1 2 3 4 5
```
### Giải thích
Mảng sau khi sắp xếp tăng dần bằng Merge Sort là: 1 2 3 4 5.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
