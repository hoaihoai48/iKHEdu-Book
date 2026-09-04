# Nhân Ấn Độ Chống Tràn Số 64-bit

## Bối cảnh
Khi thực hiện phép nhân hai số nguyên 64-bit A và B dưới một modulo M cũng lên tới 10^18, phép nhân thông thường A * B sẽ vượt quá giới hạn 2^63 - 1 gây tràn số âm nghiêm trọng. Thuật toán nhân Ấn Độ (tương tự lũy thừa nhị phân bằng phép cộng) giúp nhân an toàn hai số 64-bit mà không bị tràn.

## Nhiệm vụ
Cho 3 số nguyên A, B, M (0 <= A, B, M <= 10^18, M > 0). Hãy tính (A * B) mod M bằng thuật toán nhân Ấn Độ chống tràn số.

## Input
- Một dòng chứa 3 số nguyên $A, B, M$ ($0 \le A, B \le 10^{18}, 1 \le M \le 10^{18}$).

## Output
- In ra giá trị $(A \times B) \pmod M$.

## Sample 1
### Input
```text
1000000000000000000 2 1000000000000000007
```
### Output
```text
999999999999999986
```
### Giải thích
A = 10^18. Tích 2 * 10^18 = 2000000000000000000. Chia lấy dư cho M = 10^18 + 7: 2000000000000000000 - (10^18 + 7) = 999999999999999986.

## Ràng buộc
- $100\%$ số test có $A, B, M \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
