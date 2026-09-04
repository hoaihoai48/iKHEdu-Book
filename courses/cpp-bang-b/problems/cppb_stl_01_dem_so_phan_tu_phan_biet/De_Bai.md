# Đếm Số Phần Tử Phân Biệt

## Bối cảnh
Tại một hội nghị thượng đỉnh về chuyển đổi số, ban lễ tân quét mã QR định danh của $N$ lượt đại biểu tham dự. Do một số đại biểu di chuyển nhiều lần qua cổng kiểm soát, danh sách các mã định danh thu thập được bị trùng lặp. Ban tổ chức cần thống kê chính xác số lượng đại biểu thực tế (tức số lượng mã định danh độc nhất, phân biệt) đã có mặt.

## Nhiệm vụ
Cho danh sách gồm $N$ số nguyên đại diện cho mã định danh. Hãy lập trình đếm và in ra số lượng giá trị phân biệt xuất hiện trong dãy số.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 2  × 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$) cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất một số nguyên là số lượng phần tử phân biệt trong dãy.

## Sample 1
### Input
```text
5
2 3 2 2 3
```
### Output
```text
2
```

### Giải thích
Với dãy gồm 5 số nguyên $[2, 3, 2, 1, 3]$:
Các giá trị phân biệt xuất hiện trong dãy là $\{1, 2, 3\}$. Có tất cả 3 giá trị phân biệt, kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
