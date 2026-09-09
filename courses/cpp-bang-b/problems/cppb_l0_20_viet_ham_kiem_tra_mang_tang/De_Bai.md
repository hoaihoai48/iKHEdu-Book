# Viết hàm kiểm tra mảng tăng dần nghiêm ngặt

## Bối cảnh
Trước khi áp dụng thuật toán Tìm kiếm nhị phân (sẽ học ở các chương sau), một điều kiện tiên quyết bắt buộc là dãy số phải được sắp xếp theo thứ tự không giảm (tăng dần). Bạn hãy lập trình viết một hàm chuyên dụng để kiểm tra xem một dãy số đã được sắp xếp tăng dần hay chưa.

## Nhiệm vụ
Cho một dãy gồm $N$ số nguyên. Hãy viết hàm `bool isSorted(const vector<int>& a)` kiểm tra tính tăng dần của mảng:

- Nếu mảng đã sắp xếp không giảm ($a_0 \le a_1 \le \dots \le a_{n-1}$), in ra `YES`.
- Ngược lại, in ra `NO`.

## Input
- Dòng thứ nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($-10^9 \le a_i \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra một dòng duy nhất chữ `YES` hoặc `NO`.

## Sample 1
### Input
```text
5
2 4 4 7 9
```
### Output
```text
YES
```

### Giải thích
Dãy $2 \le 4 \le 4 \le 7 \le 9$ thỏa mãn thứ tự không giảm. In ra `YES`.

## Sample 2
### Input
```text
4
1 5 3 8
```
### Output
```text
NO
```

### Giải thích
Tại vị trí $5$ và $3$, ta có $5 > 3$ vi phạm tính chất tăng dần. In ra `NO`.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, -10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
