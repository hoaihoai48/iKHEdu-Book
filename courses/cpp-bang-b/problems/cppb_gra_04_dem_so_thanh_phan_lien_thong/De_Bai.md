# Đếm Số Thành Phần Liên Thông

## Bối cảnh
Một quần đảo gồm $N$ hòn đảo và $M$ cây cầu hai chiều nối giữa một số cặp đảo. Hai hòn đảo thuộc cùng một cụm đảo liên thông nếu cư dân có thể đi lại giữa chúng qua các cây cầu (trực tiếp hoặc gián tiếp). Ban quản lý du lịch cần xác định xem toàn bộ quần đảo đang bị chia cắt thành bao nhiêu cụm đảo biệt lập.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình đếm số lượng thành phần liên thông của đồ thị.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.

## Output
- In ra trên một dòng duy nhất một số nguyên là số lượng thành phần liên thông.

## Sample 1
### Input
```text
5 3
1 2
2 3
4 5
```
### Output
```text
2
```

### Giải thích
Với 5 đỉnh và các cạnh (1, 2), (3, 4):

- Cụm 1 gồm các đỉnh {1, 2}.
- Cụm 2 gồm các đỉnh {3, 4}.
- Cụm 3 gồm đỉnh cô lập {5}.
Có tất cả 3 thành phần liên thông độc lập, kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
