# Tính giá trị phân số modulo

## Bối cảnh
Cho hai số nguyên $P, Q$ ($Q \not\equiv 0 \pmod{10^9+7}$). Hãy tính $(P \times Q^{-1}) \bmod (10^9+7)$.

## Nhiệm vụ
Cho $T$ cặp $(P, Q)$ với $Q \not\equiv 0 \pmod{10^9+7}$. Hãy lập trình tính $(P / Q) \bmod (10^9+7)$ cho mỗi cặp.

## Input
- Dòng 1: $T$ ($1 \le T \le 10^5$). $T$ dòng sau: $P, Q$ ($0 \le P \le 10^9, 1 \le Q \le 10^9$).

## Output
- In ra $(P / Q) \bmod (10^9+7)$ trên mỗi dòng.

## Sample 1
### Input
```text
2
1 2
3 7
```
### Output
```text
500000004
428571432
```

### Giải thích
* Với cặp $(P, Q) = (1, 2)$: cần tìm số $x$ sao cho $2x \equiv 1 \pmod{10^9+7}$. Thử $x = 500000004$: $2 \times 500000004 = 1000000008 = (10^9+7) + 1 \equiv 1$, vậy đáp án là `500000004`.
* Với cặp $(P, Q) = (3, 7)$: đáp án `428571432` vì $7 \times 428571432 = 3000000024 = 3 \times (10^9+7) + 3 \equiv 3 \pmod{10^9+7}$, tức $428571432$ chính là giá trị của $3/7$ trong phép chia modulo.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
