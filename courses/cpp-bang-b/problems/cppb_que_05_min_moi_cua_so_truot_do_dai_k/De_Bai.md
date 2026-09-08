# Min Mọi Cửa Sổ Trượt Bằng Monotonic Deque O(N)

## Bối cảnh
Một máy đo nhiệt độ lò phản ứng hạt nhân ghi nhận chuỗi $N$ giá trị đo liên tiếp. Một cửa sổ quan sát kích thước cố định gồm $K$ phép đo trượt dần từ đầu đến cuối dãy đo. Tại mỗi vị trí của cửa sổ trượt, hệ thống cảnh báo an toàn cần xác định giá trị nhiệt độ thấp nhất bên trong cửa sổ đó với tốc độ xử lý tức thời.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình tìm giá trị nhỏ nhất trong mỗi cửa sổ trượt kích thước $K$ khi di chuyển từ trái sang phải.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N - K + 1$ số nguyên là giá trị nhỏ nhất của từng cửa sổ trượt, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
8 3
1 3 -1 -3 5 3 6 7
```
### Output
```text
-1 -3 -3 -3 3 3
```

### Giải thích
Với mảng $[1, 3, -1, -3, 5, 3, 6, 7]$ và cửa sổ $K = 3$:

- Cửa sổ 1 [1, 3, -1] -> min = -1.
- Cửa sổ 2 [3, -1, -3] -> min = -3.
- Cửa sổ 3 [-1, -3, 5] -> min = -3.
- Cửa sổ 4 [-3, 5, 3] -> min = -3.
- Cửa sổ 5 [5, 3, 6] -> min = 3.
- Cửa sổ 6 [3, 6, 7] -> min = 3.
Kết quả in ra: -1 -3 -3 -3 3 3.

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, -10^9 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
