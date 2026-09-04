# Đảo Ngược Mảng Bằng Đệ Quy Hai Con Trỏ

## Bối cảnh
Một thiết bị lưu trữ dữ liệu cảm biến cần đảo chiều một mảng bộ nhớ gồm N phần tử. Kỹ sư hệ thống muốn cài đặt hàm đệ quy đảo ngược mảng theo nguyên lý hai con trỏ đối đầu (hoán đổi A[L] và A[R] rồi đệ quy vào [L + 1, R - 1]).

## Nhiệm vụ
Cho mảng số nguyên A gồm N phần tử. Hãy sử dụng hàm đệ quy 2 con trỏ reverseArray(A, L, R) để đảo ngược toàn bộ mảng tại chỗ.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra mảng sau khi đảo ngược trên một dòng.

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
Mảng ban đầu [1, 2, 3, 4, 5] sau khi đảo ngược trở thành [5, 4, 3, 2, 1].

## Ràng buộc
- $100\%$ số test có $N \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
