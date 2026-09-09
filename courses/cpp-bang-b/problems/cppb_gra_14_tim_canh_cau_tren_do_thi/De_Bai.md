# Đếm Số Cạnh Cầu Trên Đồ Thị (Bridges)

## Bối cảnh
Một hệ thống giao thông đường thủy gồm $N$ cảng biển và $M$ tuyến hải trình. Một tuyến hải trình được gọi là một tuyến cầu hiểm yếu nếu khi tuyến này bị gián đoạn (phong tỏa), số lượng cụm cảng bị chia cắt biệt lập sẽ tăng lên. Kỹ sư an ninh hàng hải cần thống kê số lượng các tuyến hiểm yếu này để ưu tiên bố trí lực lượng tuần tra bảo vệ.

## Nhiệm vụ
Cho đồ thị vô hướng liên thông $N$ đỉnh $M$ cạnh. Hãy lập trình đếm số lượng cạnh cầu trong đồ thị.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.

## Output
- In ra trên một dòng duy nhất số lượng cạnh cầu tìm được.

## Sample 1
### Input
```text
5 5
1 2
2 3
3 1
3 4
4 5
```
### Output
```text
2
```

### Giải thích
Với đồ thị gồm 4 đỉnh có các cạnh (1, 2), (2, 3), (3, 4):
Nếu bỏ bất kỳ cạnh nào trong số 3 cạnh trên, đồ thị đều bị chia đôi thành 2 phần rời nhau. Do đó cả 3 cạnh đều là cạnh cầu, kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 0 \le M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
