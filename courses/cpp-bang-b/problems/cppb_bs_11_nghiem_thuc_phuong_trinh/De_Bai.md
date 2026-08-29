# Tìm Nghiệm Thực Của Phương Trình Đơn Điệu

## Bối cảnh
Cho phương trình số thực:
$$f(x) = x^3 + 2x^2 + 10x - C = 0$$
với $C$ là một hằng số thực dương ($1 \le C \le 10^9$).

## Nhiệm vụ
Hãy tìm nghiệm thực $x > 0$ của phương trình với độ chính xác sai số tuyệt đối không quá $10^{-6}$.

## Input
- Dòng 1: Số thực $C$ ($1 \le C \le 10^9$).

## Output
- In ra nghiệm thực $x$ lấy đúng 6 chữ số sau dấu phẩy thập phân.

## Sample 1
### Input
```text
13
```
### Output
```text
1.000000
```
*(Giải thích: Tại $x = 1$, $1^3 + 2(1^2) + 10(1) - 13 = 0$).*

## Ràng buộc
- $100\%$ số test có $1 \le C \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
