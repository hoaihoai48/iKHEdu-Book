# Trọng Tâm Của Cây (Tree Centroid)

## Bối cảnh
Một tập đoàn vận tải muốn đặt trung tâm điều hành tổng tại một trong $N$ thành phố có kết nối hình cây ($N - 1$ tuyến đường). Thành phố được chọn làm trọng tâm của cây nếu khi tạm thời gỡ bỏ thành phố này khỏi mạng lưới, kích thước của thành phần liên thông lớn nhất còn lại là nhỏ nhất có thể.

## Nhiệm vụ
Cho đồ thị cây $N$ đỉnh. Hãy lập trình tìm đỉnh trọng tâm của cây. Nếu có nhiều đỉnh trọng tâm, in ra đỉnh có số hiệu nhỏ nhất.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N - 1$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.

## Output
- In ra số hiệu của đỉnh trọng tâm tìm được.

## Sample 1
### Input
```text
5
1 2
2 3
3 4
3 5
```
### Output
```text
3
```

### Giải thích
Với cây 5 đỉnh có đỉnh 1 nối với các đỉnh 2, 3, 4, 5 (cấu trúc hình sao):
Nếu chọn đỉnh 1 làm trọng tâm, các nhánh còn lại đều chỉ có kích thước là 1. Đỉnh trọng tâm duy nhất là đỉnh 1.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
