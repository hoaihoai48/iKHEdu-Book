# Chu Trình Ngắn Nhất Trên Đồ Thị (Girth)

## Bối cảnh
Trong nghiên cứu cấu trúc phân tử hóa học của các hợp chất vòng hữu cơ, các nhà hóa học cần xác định chu trình vòng có kích thước nhỏ nhất (chu vi nhỏ nhất - Girth) xuất hiện trong đồ thị liên kết nguyên tử.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh không có khuyên và không có cạnh bội. Hãy lập trình tìm độ dài của chu trình có số cạnh nhỏ nhất trong đồ thị. Nếu đồ thị không có chu trình nào, in ra `-1`.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 2000, 0 \le M \le 2000$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- In ra độ dài chu trình ngắn nhất, hoặc `-1` nếu đồ thị không có chu trình.

## Sample 1
### Input
```text
5 6
1 2
2 3
3 1
3 4
4 5
5 3
```
### Output
```text
3
```

### Giải thích
Với đồ thị gồm 4 đỉnh có các cạnh (1, 2), (2, 3), (3, 4), (4, 1) và đường chéo (1, 3):
- Chu trình tạo bởi 1-2-3-1 có độ dài 3.
- Chu trình tạo bởi 1-3-4-1 có độ dài 3.
- Chu trình ngoài 1-2-3-4-1 có độ dài 4.
Chu trình có độ dài nhỏ nhất là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 0 \le M \le 2000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
