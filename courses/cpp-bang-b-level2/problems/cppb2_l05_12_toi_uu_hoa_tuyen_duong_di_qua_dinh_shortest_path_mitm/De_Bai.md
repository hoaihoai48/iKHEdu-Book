# Tối ưu hóa tuyến đường đi qua đỉnh (shortest path mitm)

## Bối cảnh
Nhóm phượt thủ lên lịch trình xuyên tỉnh: bản đồ có các thị trấn và những cung đường nối chúng với độ dài đã biết. Đoàn xuất phát từ thị trấn $S$ và phải tới thị trấn $T$.

Cả nhóm muốn tìm cung đường ngắn nhất để chia xăng xe công bằng.

## Nhiệm vụ

Cho một đồ thị vô hướng không trọng số gồm $n$ đỉnh và $m$ cạnh, cùng điểm xuất phát $s$ và điểm đích $t$. Hãy lập trình tìm số cạnh ít nhất trên đường đi từ $s$ tới $t$; in `-1` nếu hai đỉnh không liên thông.

## Input

- Dòng đầu tiên chứa bốn số nguyên $n, m, s, t$ ($1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$, $1 \le s, t \le n$) — số đỉnh, số cạnh, điểm xuất phát và điểm đích.
- $m$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u, v$ mô tả một cạnh vô hướng.

## Output

- In ra một dòng duy nhất là số cạnh ít nhất trên đường đi từ $s$ tới $t$; in `-1` nếu không tồn tại đường đi.

## Sample 1
### Input
```text
4 3 1 4
1 2
2 3
3 4
```
### Output
```text
3
```
### Giải thích

Đồ thị là đường thẳng $1 - 2 - 3 - 4$. Xuất phát từ $1$: bước $1$ tới đỉnh $2$, bước $2$ tới đỉnh $3$, bước $3$ tới đỉnh $4$ — tới đích sau $3$ cạnh, và không có đường tắt nào ngắn hơn. Đáp án là $3$.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$, $0 \le m \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
