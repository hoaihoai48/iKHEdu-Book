# Tính Số Chỉnh Hợp A(N, K) mod M

## Bối cảnh
Một giải chạy marathon có N vận động viên tranh tài. Ban tổ chức trao các giải Nhất, Nhì, ..., thứ K cho K vận động viên về đích đầu tiên theo thứ tự xếp hạng. Số cách trao giải là số chỉnh hợp A(N, K). Hãy tính giá trị này theo modulo 10^9 + 7 cho Q truy vấn.

## Nhiệm vụ
Cho Q truy vấn, mỗi truy vấn gồm 2 số N và K. Hãy tính số chỉnh hợp A(N, K) mod (10^9 + 7).

## Input
- Dòng 1: Số nguyên dương $Q$ ($1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số $N$ và $K$ ($0 \le K \le N \le 10^6$).

## Output
- In ra $Q$ dòng tương ứng là $A(N, K) \pmod{10^9 + 7}$.

## Sample 1
### Input
```text
2
5 2
4 3
```
### Output
```text
20
24
```
### Giải thích
- A(5, 2) = 5 * 4 = 20.
- A(4, 3) = 4 * 3 * 2 = 24.

## Ràng buộc
- $100\%$ số test có $Q \le 10^5, N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
