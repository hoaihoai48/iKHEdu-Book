# Đổi Tiền Số Xu Ít Nhất

## Bối cảnh
Tại một trạm đổi tiền tự động thông minh của trung tâm thương mại, hệ thống hỗ trợ $N$ loại đồng xu với các mệnh giá khác nhau. Khách hàng có nhu cầu đổi một số tiền mặt đúng bằng $S$ đồng để sử dụng máy bán nước tự động. Nhằm tối ưu hóa số lượng tiền kim loại lưu thông và giúp ví của khách hàng không bị quá nặng, hệ thống máy luôn tìm cách chi trả bằng số lượng đồng xu ít nhất có thể. Biết rằng kho tiền xu của trạm luôn dồi dào, mỗi mệnh giá có số lượng xu không giới hạn.

## Nhiệm vụ
Cho danh sách $N$ mệnh giá đồng xu và số tiền cần đổi $S$. Hãy lập trình xác định số lượng đồng xu ít nhất để đổi được đúng số tiền $S$. Nếu không có cách nào đổi được đúng số tiền đó, in ra `-1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $S$ ($1 \le N \le 100, 1 \le S \le 10^5$) lần lượt là số loại đồng xu và số tiền mục tiêu cần đổi.
- Dòng 2: Chứa $N$ số nguyên dương $c_1, c_2, \dots, c_N$ ($1 \le c_i \le 10^4$) biểu diễn các mệnh giá đồng xu, các số cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất một số nguyên là số lượng đồng xu ít nhất cần dùng. Nếu không đổi được, in ra `-1`.

## Sample 1
### Input
```text
3 11
1 5 6
```
### Output
```text
2
```

### Giải thích
Để đổi được số tiền $S = 11$ từ các mệnh giá xu $\{1, 5, 6\}$:
- Cách 1: Dùng 1 đồng 6 và 5 đồng 1 ($6 + 1  × 5 = 11$), tổng cộng tốn 6 đồng xu.
- Cách 2: Dùng 2 đồng 5 và 1 đồng 1 ($5  × 2 + 1 = 11$), tổng cộng tốn 3 đồng xu.
- Phương án tối ưu nhất: Dùng 1 đồng 5 và 1 đồng 6 ($5 + 6 = 11$), chỉ cần đúng 2 đồng xu. Kết quả là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 100, 1 \le S \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
