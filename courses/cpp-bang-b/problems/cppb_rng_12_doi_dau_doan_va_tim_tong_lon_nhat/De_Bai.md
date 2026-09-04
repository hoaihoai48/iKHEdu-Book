# Cập Nhật Phân Đoạn Nâng Cao

## Bối cảnh
Một hệ thống lưới điện thông minh hỗ trợ thao tác đổi dấu đồng loạt toàn bộ điện áp trên một phân đoạn đường dây từ $L$ đến $R$ ($A_i \to -A_i$), đồng thời hỗ trợ truy vấn tính tổng điện áp lớn nhất của một đoạn con bất kỳ.

## Nhiệm vụ
Cho mảng $A$ và các thao tác đảo dấu đoạn hoặc truy vấn tổng đoạn con lớn nhất. Hãy lập trình xử lý và in ra kết quả cho các thao tác truy vấn.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$.
- Các dòng tiếp theo chứa các thao tác cập nhật và truy vấn.

## Output
- In ra kết quả cho mỗi thao tác truy vấn trên một dòng.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
2 1 3
1 2 10
2 1 3
```
### Output
```text
6
16
```

### Giải thích
Sau thao tác đảo dấu đoạn, các giá trị âm biến thành dương giúp hình thành một đoạn con có tổng lớn nhất đạt giá trị tối ưu mới.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
