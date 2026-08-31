# Sinh Xâu Nhị Phân Không Chứa Hai Số 1 Liền Kề

**Phân loại bài toán:** `Advanced Challenge`

## Bối cảnh
Cho số nguyên dương $N$. Hãy sinh tất cả các xâu nhị phân độ dài $N$ theo thứ tự từ điển sao cho không có 2 ký tự `'1'` nào đứng cạnh nhau bằng hàm đệ quy phân nhánh trạng thái.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 20$).

## Output
- Dòng 1: Số lượng xâu thỏa mãn (bằng số Fibonacci $F_{N+2}$).
- Các dòng tiếp theo: Mỗi dòng in ra một xâu nhị phân thỏa mãn.

## Sample 1
### Input
```text
3
```
### Output
```text
5
000
001
010
100
101
```
### Giải thích
Với N = 3, có 5 xâu hợp lệ: 000, 001, 010, 100, 101.

## Ràng buộc
- 100% số test có $1 \le N \le 20$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
