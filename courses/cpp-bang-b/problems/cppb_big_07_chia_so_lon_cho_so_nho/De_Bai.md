# Chia Số Lớn Cho Số Nhỏ (Lấy Thương)

## Bối cảnh
Một kho quỹ dự trữ có số tiền là số nguyên lớn A muốn chia đều cho b quỹ từ thiện xã hội (b <= 10^9). Hãy tính số tiền chính xác (phần nguyên thương số) mà mỗi quỹ nhận được.

## Nhiệm vụ
Cho số nguyên lớn A và số nguyên nhỏ b (1 <= b <= 10^9). Hãy tìm phần nguyên thương số floor(A / b).

## Input
- Dòng 1: Chuỗi số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Số nguyên dương $b$ ($1 \le b \le 10^9$).

## Output
- In ra chuỗi số là thương của phép chia.

## Sample 1
### Input
```text
1000
3
```
### Output
```text
333
```
### Giải thích
1000 chia cho 3 được phần nguyên thương là 333.

## Ràng buộc
- $100\%$ số test có $|A| \le 10^5, 1 \le b \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
