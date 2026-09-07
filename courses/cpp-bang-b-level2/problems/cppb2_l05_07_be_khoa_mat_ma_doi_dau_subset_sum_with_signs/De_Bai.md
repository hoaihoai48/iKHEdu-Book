# Bẻ khóa mật mã đổi dấu (subset sum with signs)

## Bối cảnh
Chiếc két sắt có $N$ núm vặn, mỗi núm mang một con số. Người thợ có thể xoay mỗi núm sang trái (trừ đi con số), sang phải (cộng thêm con số) hoặc giữ nguyên (bỏ qua núm đó).

Người thợ cần biết có bao nhiêu cách vặn để con số hiển thị cuối cùng đúng bằng mật mã mục tiêu.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên và một giá trị mục tiêu $T$. Hãy lập trình đếm số cách gán mỗi phần tử vào một trong ba trạng thái (bỏ qua, cộng thêm, trừ đi) sao cho tổng thu được bằng $T$.

## Input

- Dòng đầu tiên chứa số nguyên $n$ và số nguyên $T$ ($1 \le n \le 24$, $|T| \le 10^{14}$) — số phần tử và tổng mục tiêu.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là số cách gán mỗi phần tử vào một trong ba trạng thái (bỏ qua, cộng thêm, trừ đi) sao cho tổng thu được đúng bằng $T$ (cách gán bỏ qua tất cả cũng được tính nếu tổng bằng $T$).

## Sample 1
### Input
```text
3 0
1 2 3
```
### Output
```text
3
```
### Giải thích

Với dãy $[1, 2, 3]$ và $T = 0$, xét dấu của số $3$: nếu bỏ qua $3$ thì $\pm 1 \pm 2 = 0$ chỉ xảy ra khi bỏ qua cả hai — $1$ cách (bỏ hết). Nếu lấy $+3$ thì cần $\pm 1 \pm 2 = -3$, chỉ có $-1 - 2$ thỏa — $1$ cách. Nếu lấy $-3$ thì cần $\pm 1 \pm 2 = 3$, chỉ có $+1 + 2$ thỏa — $1$ cách. Tổng cộng $3$ cách.

## Ràng buộc

- $1 \le n \le 24$, $|T| \le 10^{14}$, $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
