# Cặp số nguyên tố sinh đôi trong đoạn

## Bối cảnh
Trong lý thuyết số học, một cặp số nguyên tố sinh đôi (Twin Primes) là cặp số nguyên tố $(p, p+2)$ có khoảng cách đúng bằng 2. Bài toán đặt ra yêu cầu đếm số lượng cặp số nguyên tố sinh đôi nằm hoàn toàn trong đoạn $[L, R]$. Do $R$ có thể lên tới $10^{12}$ và độ dài đoạn $R - L \le 10^6$, ta cần kết hợp Sàng nguyên tố phân đoạn (Segmented Sieve) để đánh dấu các số nguyên tố trong khoảng truy vấn.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Cặp Số Nguyên Tố Sinh Đôi Trong Đoạn với độ phức tạp tối ưu nhất.

## Input
- Dòng đầu tiên chứa số nguyên dương $T$ ($1 \le T \le 10$) — số lượng bộ dữ liệu.
- $T$ dòng tiếp theo, mỗi dòng chứa hai số nguyên dương $L, R$ ($1 \le L \le R \le 10^{12}, R - L \le 10^6$).

## Output
- In ra $T$ dòng, mỗi dòng là số lượng cặp số nguyên tố $(p, p+2)$ thỏa mãn $L \le p < p+2 \le R$.

## Sample 1
### Input
```text
2
1 20
10 30
```
### Output
```text
4
2
```
### Giải thích
* Đoạn [1, 20] có 4 cặp sinh đôi: (3, 5), (5, 7), (11, 13), (17, 19).
* Đoạn [10, 30] có 2 cặp sinh đôi: (11, 13), (17, 19).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
