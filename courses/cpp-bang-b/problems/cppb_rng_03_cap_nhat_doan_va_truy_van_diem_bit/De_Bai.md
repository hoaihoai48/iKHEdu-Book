# Cập Nhật Đoạn & Truy Vấn Điểm (Range Update Point Query)

## Bối cảnh
Một chương trình khuyến mãi của sàn thương mại điện tử đồng loạt cộng thêm một khoản điểm thưởng $V$ cho tất cả các khách hàng có mã số định danh nằm trong khoảng từ $L$ đến $R$. Sau đó, một khách hàng tại vị trí $pos$ muốn tra cứu số điểm thưởng tích lũy hiện tại của mình.

## Nhiệm vụ
Cho mảng $A$ và $Q$ thao tác thuộc hai dạng: `1 L R V` (cộng thêm $V$ vào tất cả các phần tử từ $L$ đến $R$) và `2 pos` (in ra giá trị hiện tại của phần tử tại vị trí $pos$). Hãy in ra kết quả của các thao tác loại 2.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.

## Output
- Với mỗi thao tác loại 2, in ra giá trị tại vị trí $pos$ trên một dòng.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
1 2 4 5
2 3
2 1
```
### Output
```text
8
1
```

### Giải thích
Với mảng ban đầu toàn số 0: $[0, 0, 0, 0, 0]$:

- Cộng thêm 5 vào đoạn từ vị trí 2 đến 4: mảng thành $[0, 5, 5, 5, 0]$.
- Truy vấn giá trị tại vị trí 3: in ra 5.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
