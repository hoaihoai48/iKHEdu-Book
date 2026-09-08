# Đếm Giá Trị Phân Biệt

## Bối cảnh
Tại một cổng kiểm soát vé vào hội chợ công nghệ, hệ thống quét mã vạch ghi nhận mã số thẻ của $N$ lượt khách ra vào trong ngày. Do một số khách hàng có thể quét thẻ nhiều lần khi di chuyển qua lại giữa các khu vực triển lãm, danh sách các mã vé thu thập được có hiện tượng lặp lại. Ban tổ chức cần thống kê chính xác số lượng khách tham quan thực tế (tức số lượng mã số thẻ độc nhất, phân biệt nhau) đã đến dự hội chợ.

## Nhiệm vụ
Cho danh sách $N$ mã số thẻ nguyên $A_1, A_2, \dots, A_N$. Hãy đếm và in ra số lượng giá trị phân biệt trong dãy số đó.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$) — số lượt quét mã vé.
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$) — danh sách mã vé được ghi nhận.

## Output
- In ra một số nguyên duy nhất là số lượng giá trị phân biệt xuất hiện trong dãy.

## Sample 1
### Input
```text
6
2 3 2 1 3 5
```
### Output
```text
4
```
### Giải thích
Danh sách mã vé ghi nhận là: $2, 3, 2, 1, 3, 5$.
Sau khi sắp xếp tăng dần: $1, 2, 2, 3, 3, 5$.
Các nhóm giá trị trùng nhau được gom liền kề:

- Giá trị $1$ (xuất hiện 1 lần)
- Giá trị $2$ (xuất hiện 2 lần)
- Giá trị $3$ (xuất hiện 2 lần)
- Giá trị $5$ (xuất hiện 1 lần)
Tổng cộng có $4$ giá trị phân biệt khác nhau là $\{1, 2, 3, 5\}$. Do đó in ra kết quả là `4`.

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
