# Hình Chữ Nhật Lớn Nhất Trên Histogram

## Bối cảnh
Một biểu đồ cột (histogram) gồm $N$ cột hình chữ nhật đứng xếp kề sát nhau trên cùng một đường nằm ngang. Mỗi cột có chiều rộng cố định là 1 đơn vị, cột thứ $i$ có chiều cao là $H_i$. Ban thiết kế đồ họa cần tìm diện tích của hình chữ nhật lớn nhất có thể vẽ lọt hoàn toàn vào bên trong biểu đồ cột này.

## Nhiệm vụ
Cho danh sách chiều cao của $N$ cột. Hãy lập trình tìm diện tích lớn nhất của một hình chữ nhật nằm gọn bên trong biểu đồ cột.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên không âm $H_1, H_2, \dots, H_N$ ($0 \le H_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất diện tích lớn nhất của hình chữ nhật.

## Sample 1
### Input
```text
6
2 1 5 6 2 3
```
### Output
```text
10
```

### Giải thích
Với biểu đồ có chiều cao các cột là $[2, 1, 5, 6, 2, 3]$:
Hình chữ nhật lớn nhất được tạo thành bởi hai cột có chiều cao 5 và 6. Chiều cao của hình chữ nhật này là $\min(5, 6) = 5$, chiều rộng là 2 cột. Diện tích lớn nhất đạt được là $5 \times 2 = 10$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le H_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
