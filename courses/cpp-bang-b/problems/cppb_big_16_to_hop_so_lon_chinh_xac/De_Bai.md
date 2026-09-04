# Số Lớn Cực Hạn: Tổ Hợp C(N, K) Chính Xác

## Bối cảnh
Khi cần tính số cách chia tổ hợp C(N, K) chính xác tuyệt đối mà không áp dụng modulo, việc giản ước thừa số chung giữa tử số và mẫu số kết hợp nhân BigInt cho phép tính chính xác đến chữ số cuối cùng.

## Nhiệm vụ
Cho 2 số nguyên N và K. Hãy tính giá trị chính xác tuyệt đối của C(N, K) = N! / (K! * (N - K)!).

## Input
- Một dòng chứa 2 số nguyên $N$ và $K$ ($0 \le K \le N \le 200$).

## Output
- In ra giá trị chính xác tuyệt đối của $C(N, K)$.

## Sample 1
### Input
```text
5 2
```
### Output
```text
10
```
### Giải thích
C(5, 2) = 10.

## Ràng buộc
- $100\%$ số test có $N \le 200$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
