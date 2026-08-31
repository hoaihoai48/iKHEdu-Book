# Đảo Ngược Mảng Bằng Đệ Quy Hai Con Trỏ

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử. Hãy sử dụng hàm đệ quy 2 con trỏ `reverseRec(l, r)` để đảo ngược mảng $A$ ngay trên mảng gốc mà không dùng vòng lặp.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).

## Output
- In ra $N$ phần tử của mảng sau khi đảo ngược, cách nhau bởi dấu cách.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
5 4 3 2 1
```
### Giải thích
Mảng sau khi đảo ngược: 5 4 3 2 1.

## Ràng buộc
- 100% số test có $N \le 1000, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
