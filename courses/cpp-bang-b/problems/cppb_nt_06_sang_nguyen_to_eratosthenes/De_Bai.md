# Sàng Nguyên Tố Eratosthenes

## Bối cảnh
Để phục vụ các bài toán mã hóa khóa công khai RSA quy mô nhỏ, máy chủ cần khởi tạo sẵn bảng tra cứu tất cả các số nguyên tố từ 2 đến N bằng thuật toán Sàng Eratosthenes kinh điển.

## Nhiệm vụ
Cho số nguyên dương N. Hãy in ra tất cả các số nguyên tố không vượt quá N theo thứ tự tăng dần.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($2 \le N \le 10^6$).

## Output
- In ra các số nguyên tố trên một dòng cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
15
```
### Output
```text
2 3 5 7 11 13
```
### Giải thích
Các số nguyên tố không vượt quá 15 là: 2, 3, 5, 7, 11, 13.

## Ràng buộc
- $100\%$ số test có $N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
