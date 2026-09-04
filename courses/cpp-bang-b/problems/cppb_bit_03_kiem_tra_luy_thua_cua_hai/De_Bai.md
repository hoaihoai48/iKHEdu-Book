# Kiểm Tra Số Có Phải Lũy Thừa Của 2

## Bối cảnh
Trong kỹ thuật cấu hình bộ nhớ đệm máy tính, dung lượng bộ nhớ hợp chuẩn bắt buộc phải là một lũy thừa của 2 (nghĩa là có dạng 2^k với k >= 0). Hệ thống kiểm tra hợp lệ cần xác định nhanh xem số nguyên dương N có phải là một lũy thừa của 2 hay không bằng phép toán bit O(1).

## Nhiệm vụ
Cho số nguyên dương N (1 <= N <= 10^18). Kiểm tra N có phải là lũy thừa của 2 không. In YES nếu đúng, ngược lại in NO.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
16
```
### Output
```text
YES
```
### Giải thích
16 = 2^4 là một lũy thừa của 2. Phép toán bit: (16 & 15) = 0. Do đó in YES.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
