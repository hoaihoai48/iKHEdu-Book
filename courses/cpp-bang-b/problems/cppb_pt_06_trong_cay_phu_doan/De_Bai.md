# Trồng Cây Phủ Đoạn Tối Ưu

## Bối cảnh
Để phủ xanh đô thị, ban quản lý công viên có N hố trồng cây được đánh số từ 1 đến N dọc tuyến phố. Có Q tình nguyện viên tham gia, mỗi người nhận phụ trách tưới nước bổ sung cho các hố cây trong đoạn từ L đến R. Sau chiến dịch, ban tổ chức cần kiểm tra xem mỗi hố cây đã được bao nhiêu lượt tình nguyện viên tưới nước.

## Nhiệm vụ
Cho N vị trí và Q đoạn [L, R]. Hãy đếm số lượt phủ của mỗi vị trí từ 1 đến N sau Q lần thao tác.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $L$ và $R$ ($1 \le L \le R \le N$).

## Output
- In ra $N$ số nguyên cách nhau bởi khoảng trắng là số lượt phủ tại mỗi vị trí từ $1$ đến $N$.

## Sample 1
### Input
```text
5 3
1 3
2 4
2 5
```
### Output
```text
1 3 3 2 1
```
### Giải thích
Mỗi đoạn [L, R] tương ứng với thao tác cộng 1 vào đoạn [L, R]. Mảng hiệu ghi nhận số lượt tưới tại từng vị trí lần lượt là: vị trí 1 được 1 lượt, vị trí 2 được 3 lượt, vị trí 3 được 3 lượt, vị trí 4 được 2 lượt, vị trí 5 được 1 lượt. Kết quả in ra: 1 3 3 2 1.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
