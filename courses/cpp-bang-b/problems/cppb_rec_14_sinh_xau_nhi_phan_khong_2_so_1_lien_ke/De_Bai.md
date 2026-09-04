# Sinh Xâu Nhị Phân Không Chứa Hai Số 1 Liền Kề

## Bối cảnh
Trong kỹ thuật mã hóa kênh truyền chống can nhiễu từ trường (Run-length Limited RLL), một chuỗi bit nhị phân an toàn không được phép chứa hai bit 1 nằm kề nhau (tránh xung đột điện áp). Hãy sinh ra tất cả các xâu nhị phân độ dài N thỏa mãn điều kiện này theo thứ tự từ điển.

## Nhiệm vụ
Cho số nguyên dương N (1 <= N <= 20). Hãy sinh tất cả các xâu nhị phân độ dài N không chứa chuỗi '11' theo thứ tự từ điển.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 20$).

## Output
- In ra các xâu nhị phân thỏa mãn, mỗi xâu trên một dòng.

## Sample 1
### Input
```text
3
```
### Output
```text
000
001
010
100
101
```
### Giải thích
Các xâu nhị phân độ dài 3 không có '11' gồm: 000, 001, 010, 100, 101. Tổng cộng có 5 xâu.

## Ràng buộc
- $100\%$ số test có $N \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
