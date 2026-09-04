# Kiểm Tra Số Chính Phương

## Bối cảnh
Một người thợ lát sàn gạch vuông cần kiểm tra xem diện tích sàn gồm N viên gạch nhỏ có thể xếp thành một hình vuông lớn hoàn hảo (cạnh nguyên k) hay không.

## Nhiệm vụ
Cho số nguyên dương N. Hãy kiểm tra xem N có phải là số chính phương (N = k^2 với k nguyên dương) hay không. In YES nếu đúng, ngược lại in NO.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
49
```
### Output
```text
YES
```
### Giải thích
49 = 7^2 là bình phương của số nguyên 7, do đó 49 là số chính phương -> in YES.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
