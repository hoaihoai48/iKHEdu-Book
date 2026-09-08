# Kiểm Tra Năm Nhuận

## Bối cảnh
Bạn Dũng đang lập trình ứng dụng lịch và cần xác định xem một năm cho trước có phải năm nhuận hay không để hiển thị đúng số ngày trong tháng 2 (28 hoặc 29 ngày).

## Nhiệm vụ
Cho một số nguyên dương $Y$ đại diện cho năm. Hãy kiểm tra xem $Y$ có phải năm nhuận không. Năm nhuận là năm chia hết cho $4$ nhưng không chia hết cho $100$, hoặc chia hết cho $400$. In `YES` nếu là năm nhuận, `NO` nếu không.

## Input
- Một dòng duy nhất chứa số nguyên dương $Y$ ($1 \le Y \le 10^9$).

## Output
- In ra `YES` hoặc `NO`.

## Sample 1
### Input
```text
2024
```
### Output
```text
YES
```

### Giải thích
$2024$ chia hết cho $4$ ($2024 / 4 = 506$) và không chia hết cho $100$ ($2024 / 100 = 20$ dư $24$). Vậy $2024$ là năm nhuận.

## Sample 2
### Input
```text
1900
```
### Output
```text
NO
```

### Giải thích
$1900$ chia hết cho $4$ và chia hết cho $100$, nhưng không chia hết cho $400$ ($1900 / 400 = 4$ dư $300$). Vậy $1900$ không phải năm nhuận.

## Ràng buộc
- $100\%$ số test có $1 \le Y \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
