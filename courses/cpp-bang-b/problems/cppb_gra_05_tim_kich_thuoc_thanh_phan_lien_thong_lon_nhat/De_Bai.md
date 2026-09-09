# Kích Thước Thành Phần Liên Thông Lớn Nhất

## Bối cảnh
Vẫn tại quần đảo gồm $N$ hòn đảo và $M$ cây cầu, ban quy hoạch kinh tế muốn tìm cụm đảo liên thông phát triển sầm uất nhất (chứa số lượng hòn đảo nhiều nhất) để đầu tư xây dựng trung tâm logistics tập trung.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình tìm số lượng đỉnh thuộc về thành phần liên thông có kích thước lớn nhất.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.

## Output
- In ra trên một dòng duy nhất kích thước của thành phần liên thông lớn nhất.

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
3
```

### Giải thích
Với 5 đỉnh và các cạnh (1, 2), (2, 3), (4, 5):

- Cụm 1 gồm {1, 2, 3} có 3 hòn đảo.
- Cụm 2 gồm {4, 5} có 2 hòn đảo.
Kích thước của thành phần liên thông lớn nhất là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
