# Mảng Tiền Tố XOR Đoạn Con

## Bối cảnh
Trong kỹ thuật mật mã hóa luồng, một chuỗi gồm N khóa bit số nguyên A1, A2, ..., An được lưu trữ liên tiếp. Để giải mã thông điệp truyền đi trong khoảng thời gian từ L đến R, máy chủ giải mã cần tính toán nhanh giá trị tích XOR của toàn bộ các phần tử từ vị trí L đến vị trí R cho Q yêu cầu độc lập.

## Nhiệm vụ
Cho dãy số nguyên gồm N phần tử. Có Q truy vấn, mỗi truy vấn yêu cầu tính tích XOR của các phần tử trong đoạn [L, R]: A[L] xor A[L+1] xor ... xor A[R].

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L$ và $R$ ($1 \le L \le R \le N$).

## Output
- In ra $Q$ dòng, mỗi dòng là kết quả XOR tương ứng.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
1 3
2 4
1 5
```
### Output
```text
0
5
1
```
### Giải thích
Mảng tiền tố XOR PrefXOR = [0, 1, 1^2=3, 3^3=0, 0^4=4, 4^5=1].

- Đoạn [1, 3]: PrefXOR[3] ^ PrefXOR[0] = 0 ^ 0 = 0.
- Đoạn [2, 4]: PrefXOR[4] ^ PrefXOR[1] = 4 ^ 1 = 5.
- Đoạn [1, 5]: PrefXOR[5] ^ PrefXOR[0] = 1 ^ 0 = 1.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
