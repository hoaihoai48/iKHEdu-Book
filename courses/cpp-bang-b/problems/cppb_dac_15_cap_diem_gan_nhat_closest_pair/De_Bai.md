# Cặp Điểm Gần Nhất (Closest Pair of Points)

## Bối cảnh
Trong hệ thống radar hàng không, việc phát hiện hai máy bay có nguy cơ va chạm đòi hỏi tìm khoảng cách Euclidean nhỏ nhất giữa N điểm trên mặt phẳng 2D. Thuật toán chia để trị của Shamos và Hoey chia mặt phẳng thành hai nửa bởi đường thẳng x = Mid, tìm khoảng cách d nhỏ nhất ở hai nửa rồi quét dải băng biên hẹp 2d trong O(N log N).

## Nhiệm vụ
Cho N điểm trên mặt phẳng tọa độ 2D. Hãy tìm khoảng cách Euclidean nhỏ nhất giữa hai điểm bất kỳ, làm tròn đúng 4 chữ số thập phân.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $X_i, Y_i$ ($-10^9 \le X_i, Y_i \le 10^9$).

## Output
- In ra khoảng cách nhỏ nhất với 4 chữ số sau dấu phẩy.

## Sample 1
### Input
```text
3
0 0
1 1
2 2
```
### Output
```text
1.4142
```
### Giải thích
Khoảng cách giữa (0, 0) và (1, 1) là sqrt((1-0)^2 + (1-0)^2) = sqrt(2) = 1.4142. Kết quả in ra: 1.4142.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
