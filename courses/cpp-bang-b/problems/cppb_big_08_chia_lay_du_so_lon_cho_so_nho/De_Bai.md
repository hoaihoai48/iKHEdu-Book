# Chia Lấy Dư Số Lớn Cho Số Nhỏ

## Bối cảnh
Để băm (hashing) một chuỗi số lớn A có độ dài hàng trăm ngàn chữ số vào bảng băm kích thước b (b <= 10^18), kỹ sư cần tính phần dư A mod b trong thời gian O(|A|).

## Nhiệm vụ
Cho số nguyên lớn A và số nguyên nhỏ b (1 <= b <= 10^18). Hãy tính A mod b.

## Input
- Dòng 1: Chuỗi số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Số nguyên $b$ ($1 \le b \le 10^{18}$).

## Output
- In ra số dư $A \pmod b$.

## Sample 1
### Input
```text
123456789123456789
10
```
### Output
```text
9
```
### Giải thích
Chữ số tận cùng của A là 9 nên khi chia cho 10 phần dư là 9.

## Ràng buộc
- $100\%$ số test có $|A| \le 10^5, 1 \le b \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
