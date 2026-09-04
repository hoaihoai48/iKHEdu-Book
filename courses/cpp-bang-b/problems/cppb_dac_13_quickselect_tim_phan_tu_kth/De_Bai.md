# Thuật Toán QuickSelect Tìm K-th Element

## Bối cảnh
Khi cần tìm phần tử nhỏ thứ K trong một danh sách N số mà không muốn tốn thời gian sắp xếp toàn bộ mảng O(N log N), thuật toán QuickSelect của Hoare sử dụng cơ chế chia để trị phân hoạch ngẫu nhiên Pivot để tìm ra phần tử thứ K trong thời gian trung bình tuyến tính O(N).

## Nhiệm vụ
Cho mảng N số nguyên và số nguyên K (1 <= K <= N). Hãy tìm giá trị của phần tử nhỏ thứ K bằng thuật toán QuickSelect.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra giá trị của phần tử nhỏ thứ $K$.

## Sample 1
### Input
```text
6 3
3 2 1 5 6 4
```
### Output
```text
3
```
### Giải thích
Mảng có thứ tự: [1, 2, 3, 4, 5, 6]. Phần tử nhỏ thứ K = 3 là số 3. Kết quả in ra: 3.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
