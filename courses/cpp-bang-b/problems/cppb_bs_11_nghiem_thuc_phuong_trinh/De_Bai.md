# Tìm Nghiệm Thực Của Phương Trình Đơn Điệu

## Bối cảnh
Trong mô phỏng khí động lực học của tên lửa đẩy, hàm tiêu hao nhiên liệu theo thời gian tuân theo phương trình bậc ba đơn điệu tăng ngặt: f(x) = x^3 + 2x^2 + 10x - C = 0 (với x >= 0 và C là hằng số tiêu hao năng lượng). Các kỹ sư cần xác định thời điểm thực x với độ chính xác cao (sai số tuyệt đối không quá 10^-6).

## Nhiệm vụ
Cho số thực C dương (1 <= C <= 10^9). Hãy tìm nghiệm thực dương x của phương trình x^3 + 2x^2 + 10x - C = 0 với độ chính xác 6 chữ số thập phân.

## Input
- Một dòng chứa số thực $C$ ($1 \le C \le 10^9$).

## Output
- In ra nghiệm thực $x$ lấy đúng 6 chữ số sau dấu phẩy.

## Sample 1
### Input
```text
20.0
```
### Output
```text
1.233519
```
### Giải thích
Thay x = 1.233519 vào f(x): 1.233519^3 + 2*1.233519^2 + 10*1.233519 - 20 = 0.000000. Nghiệm chính xác đến 6 chữ số thập phân là 1.233519.

## Ràng buộc
- $100\%$ số test có $1 \le C \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
