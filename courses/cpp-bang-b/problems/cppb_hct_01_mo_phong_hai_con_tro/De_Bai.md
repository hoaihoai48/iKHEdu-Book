# Mô Phỏng Hai Con Trỏ Đối Đầu

## Bối cảnh
Trong một hệ thống thanh toán tự động của siêu thị thông minh, máy chủ cần kết hợp giá trị của 2 phiếu giảm giá đã được sắp xếp tăng dần trong ví điện tử của khách hàng để thanh toán một hóa đơn có tổng trị giá đúng bằng S. Hệ thống cần phản hồi tức thì xem liệu có tồn tại hai phiếu giảm giá ở hai vị trí khác nhau có tổng giá trị khớp chính xác với số tiền S hay không.

## Nhiệm vụ
Cho mảng N số nguyên đã được sắp xếp tăng dần và một số nguyên S. Hãy kiểm tra xem trong mảng có tồn tại cặp chỉ số (i, j) với i < j sao cho A[i] + A[j] = S hay không. Nếu có in ra YES, ngược lại in ra NO.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên đã sắp xếp tăng dần $A_1 \le A_2 \le \dots \le A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra `YES` nếu tồn tại cặp số có tổng bằng $S$, ngược lại in ra `NO`.

## Sample 1
### Input
```text
5 20
2 5 8 12 19
```
### Output
```text
YES
```
### Giải thích
Xét mảng đã sắp xếp: [2, 5, 8, 12, 19] và S = 20. Khởi tạo hai con trỏ L trỏ vào 2 (chỉ số 1) và R trỏ vào 19 (chỉ số 5). Tổng 2 + 19 = 21 > 20 -> giảm R xuống trỏ vào 12. Tiếp tục tính tổng 2 + 12 = 14 < 20 -> tăng L trỏ vào 5. Tổng 5 + 12 = 17 < 20 -> tăng L trỏ vào 8. Khi L trỏ vào 8 và R trỏ vào 12, tổng 8 + 12 = 20 đúng bằng S. Do đó in ra YES.

## Ràng buộc
- $40\%$ số test có $N \le 1000$.
- $60\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
