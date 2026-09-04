# Lũy Thừa Nhị Phân Cơ Bản

## Bối cảnh
Trong giải thuật mã hóa RSA và chữ ký số ElGamal, phép tính lũy thừa bậc cao A^B mod M là thao tác cốt lõi được gọi hàng triệu lần mỗi giây. Thuật toán Lũy thừa nhị phân (Binary Exponentiation) cho phép tính kết quả này chỉ trong O(log B) phép nhân thay vì O(B).

## Nhiệm vụ
Cho 3 số nguyên A, B, M. Hãy tính A^B mod M bằng thuật toán Lũy thừa nhị phân.

## Input
- Một dòng duy nhất chứa 3 số nguyên $A, B, M$ ($0 \le A, B \le 10^{18}, 1 \le M \le 10^9$).

## Output
- In ra giá trị của $A^B \pmod M$.

## Sample 1
### Input
```text
2 10 1000
```
### Output
```text
24
```
### Giải thích
2^10 = 1024. Khi chia lấy dư cho 1000 ta được: 1024 mod 1000 = 24. Kết quả in ra: 24.

## Ràng buộc
- $100\%$ số test có $A, B \le 10^{18}, 1 \le M \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
