# Đường Kính Của Cây (Tree Diameter)

## Bối cảnh
Một mạng cáp viễn thông kết nối $N$ máy trạm tạo thành một cấu trúc cây liên thông không chu trình gồm đúng $N - 1$ đường cáp hai chiều. Khoảng cách giữa hai máy trạm là số lượng đường cáp trên hành trình nối giữa chúng. Đường kính của cây là khoảng cách lớn nhất giữa hai máy trạm bất kỳ trong toàn bộ mạng lưới.

## Nhiệm vụ
Cho cấu trúc cây gồm $N$ đỉnh. Hãy lập trình tìm đường kính (khoảng cách lớn nhất giữa hai đỉnh) của cây.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N - 1$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$ biểu diễn một cạnh của cây.

## Output
- In ra trên một dòng duy nhất đường kính của cây.

## Sample 1
### Input
```text
5
1 2
1 3
3 4
3 5
```
### Output
```text
3
```

### Giải thích
Với cây gồm 5 đỉnh có các cạnh (1, 2), (1, 3), (2, 4), (4, 5):
Hành trình dài nhất nối giữa đỉnh 3 và đỉnh 5 qua các cạnh: $3 - 1 - 2 - 4 - 5$, gồm đúng 4 cạnh. Đường kính của cây là 4.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
