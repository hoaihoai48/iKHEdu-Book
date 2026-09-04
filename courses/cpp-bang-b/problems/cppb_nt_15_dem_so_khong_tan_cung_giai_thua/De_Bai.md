# Đếm Số Lượng Số Không Tận Cùng Của N!

## Bối cảnh
Trong tính toán số lớn, số lượng chữ số 0 liên tiếp ở tận cùng của giai thừa N! được quyết định bởi số lần xuất hiện của thừa số 10 = 2 * 5. Do số lượng thừa số 2 luôn nhiều hơn thừa số 5, ta chỉ cần đếm số mũ của thừa số 5 trong khai triển N!.

## Nhiệm vụ
Cho số nguyên dương N. Hãy đếm số lượng chữ số 0 liên tiếp tận cùng trong biểu diễn thập phân của N!.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^9$).

## Output
- In ra số lượng chữ số 0 tận cùng của $N!$.

## Sample 1
### Input
```text
25
```
### Output
```text
6
```
### Giải thích
Số lượng thừa số 5 trong 25! là: floor(25/5) + floor(25/25) = 5 + 1 = 6. Vì vậy 25! có đúng 6 chữ số 0 tận cùng.

## Ràng buộc
- $100\%$ số test có $N \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
