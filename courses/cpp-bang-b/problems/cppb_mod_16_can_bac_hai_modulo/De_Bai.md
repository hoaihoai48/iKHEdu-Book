# Đồng Dư Cực Hạn: Căn Bậc Hai Modulo

## Bối cảnh
Trong mã hóa đường cong elliptic (ECC), việc giải mã điểm tọa độ đòi hỏi tìm căn bậc hai theo modulo nguyên tố P = 10^9 + 7 (thỏa mãn P = 3 mod 4). Theo thuật toán số học, nếu A là thặng dư chính phương theo mod P, nghiệm căn bậc hai có thể tính trực tiếp bằng công thức A^((P + 1) / 4) mod P.

## Nhiệm vụ
Cho số nguyên A và số nguyên tố P = 10^9 + 7. Hãy tìm số nguyên X nhỏ nhất (0 <= X < P) sao cho X^2 = A mod P. Nếu không tồn tại, in ra -1.

## Input
- Một dòng duy nhất chứa số nguyên $A$ ($0 \le A < 10^9 + 7$).

## Output
- In ra nghiệm $X$ nhỏ nhất, hoặc `-1`.

## Sample 1
### Input
```text
4
```
### Output
```text
2
```
### Giải thích
2^2 = 4 = 4 mod (10^9 + 7). Nghiệm nhỏ nhất là 2.

## Ràng buộc
- $100\%$ số test có $0 \le A < 10^9 + 7$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
