# Số Có Đúng 3 Ước Số

## Bối cảnh
Một mã định danh số học đặc biệt có tính chất độc đáo: nó chỉ có đúng 3 ước số nguyên dương. Theo định lý toán học, một số có đúng 3 ước số khi và chỉ khi nó là bình phương của một số nguyên tố (dạng p^2 với p nguyên tố). Hãy đếm xem có bao nhiêu số như vậy không vượt quá N.

## Nhiệm vụ
Cho số nguyên dương N. Hãy đếm số lượng số nguyên dương <= N có đúng 3 ước số nguyên dương.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

## Output
- In ra một số nguyên duy nhất là số lượng số thỏa mãn.

## Sample 1
### Input
```text
50
```
### Output
```text
4
```
### Giải thích
Các số có đúng 3 ước số <= 50 là bình phương các số nguyên tố: 2^2=4, 3^2=9, 5^2=25, 7^2=49. Tổng cộng có 4 số.

## Ràng buộc
- $100\%$ số test có $N \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
