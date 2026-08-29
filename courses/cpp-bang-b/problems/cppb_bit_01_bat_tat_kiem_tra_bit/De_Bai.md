# Bật, Tắt Và Kiểm Tra Bit Thứ K

## Bối cảnh
Cho một số nguyên không âm $N$ ($0 \le N \le 10^{18}$). Có $Q$ thao tác, mỗi thao tác thuộc một trong 3 loại:
1. `1 k`: Bật bit thứ $k$ của $N$ lên 1.
2. `2 k`: Tắt bit thứ $k$ của $N$ về 0.
3. `3 k`: Kiểm tra xem bit thứ $k$ của $N$ có đang bật hay không (in ra `1` nếu bật, `0` nếu tắt).

(Quy ước các bit được đánh số từ $0$ đến $60$, với bit 0 là bit có trọng số $2^0$).

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($0 \le N \le 10^{18}, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên `type k` ($1 \le \text{type} \le 3, 0 \le k \le 60$).

## Output
- Với mỗi thao tác loại 3, in ra kết quả trên một dòng.

## Sample 1
### Input
```text
5 4
3 0
3 1
1 1
3 1
```
### Output
```text
1
0
1
```
*(Giải thích: Ban đầu $N = 5 = 101_2$. Bit 0 bằng 1, bit 1 bằng 0. Bật bit 1 lên thì $N = 111_2 = 7$, khi đó bit 1 bằng 1).*

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}, Q \le 10^5, k \le 60$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
