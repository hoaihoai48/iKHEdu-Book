# Tổng cấp số nhân bằng chia để trị

## Bối cảnh
Chị nhân viên ngân hàng cần tính tổng tiền gốc lẫn lãi sau nhiều kỳ gửi, khi mỗi kỳ số tiền được nhân lên theo cùng một hệ số. Số kỳ có thể rất lớn nên không thể cộng tay từng số hạng.

Chị cần tính nhanh tổng của dãy cấp số nhân này để in sao kê cho khách.

## Nhiệm vụ

Cho số nguyên $a$ và số mũ $n$. Hãy lập trình tính tổng $S(n) = 1 + a + a^2 + \dots + a^n$ (gồm $n + 1$ số hạng) theo modulo $10^9+7$.

## Input

- Gồm một dòng duy nhất chứa hai số nguyên không âm $a, n$ ($0 \le a \le 10^9$, $0 \le n \le 10^{18}$), cách nhau bởi một dấu cách.

## Output

- In ra một dòng duy nhất là giá trị $S(n) = 1 + a + \dots + a^n$ theo modulo $10^9+7$.

## Sample 1
### Input
```text
2 4
```
### Output
```text
31
```
### Giải thích

Khai triển trực tiếp: $S = 1 + 2 + 4 + 8 + 16 = 31$. Vì $31 < 10^9+7$ nên đáp án giữ nguyên là $31$.

## Ràng buộc

- $0 \le a \le 10^9$, $0 \le n \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
