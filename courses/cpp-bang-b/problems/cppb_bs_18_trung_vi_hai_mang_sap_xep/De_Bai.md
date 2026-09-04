# Trung Vị Của Hai Mảng Đã Sắp Xếp (Median of Two Sorted)

## Bối cảnh
Hai trạm y tế thành phố ghi nhận chỉ số nhịp tim của bệnh nhân theo hai mảng số nguyên đã sắp xếp tăng dần: trạm 1 có N người và trạm 2 có M người. Để báo cáo thống kê y tế quốc tế, ban giám đốc cần tìm giá trị trung vị (median) của tập hợp chung gồm toàn bộ N + M bệnh nhân với độ chính xác cao.

## Nhiệm vụ
Cho hai mảng đã sắp xếp A (kích thước N) và B (kích thước M). Hãy tìm giá trị trung vị của mảng hợp nhất với độ chính xác 1 chữ số thập phân.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $M$ ($1 \le N, M \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên tăng dần của mảng $A$.
- Dòng 3: Chứa $M$ số nguyên tăng dần của mảng $B$.

## Output
- In ra giá trị trung vị làm tròn đúng 1 chữ số thập phân.

## Sample 1
### Input
```text
2 2
1 3
2 4
```
### Output
```text
2.5
```
### Giải thích
Mảng hợp nhất: [1, 2, 3, 4] có 4 phần tử. Hai phần tử ở giữa là 2 và 3. Giá trị trung vị là (2 + 3) / 2 = 2.5. Kết quả in ra: 2.5.

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
