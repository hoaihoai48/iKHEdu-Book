# Tối ưu hóa tuyến đường đi qua đỉnh (shortest path with mitm)

## Bối cảnh
Bản đồ thành phố gồm các ngã tư và những con đường nối chúng. Anh tài xế xe ôm công nghệ nhận một cuốc xe từ điểm đón $S$ tới điểm trả $T$.

Anh cần tìm hành trình ngắn nhất từ $S$ tới $T$ để tiết kiệm xăng và thời gian cho khách.

## Nhiệm vụ
Cho bản đồ gồm các địa điểm và những con đường nối chúng với độ dài đã biết, cùng điểm xuất phát $S$ và điểm đích $T$. Hãy lập trình tìm độ dài hành trình ngắn nhất từ $S$ tới $T$.

## Input

- Dòng đầu tiên chứa bốn số nguyên $n, m, s, t$ ($1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$, $1 \le s, t \le n$) — số địa điểm, số con đường, điểm xuất phát và điểm đích.
- $m$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $u, v, w$ ($1 \le u, v \le n$, $0 \le w \le 10^9$) mô tả một con đường hai chiều dài $w$.

## Output

- In ra một dòng duy nhất là độ dài hành trình ngắn nhất từ $s$ tới $t$; in `-1` nếu hai điểm không liên thông.

## Sample 1
### Input
```text
4 4 1 4
1 2 2
2 4 3
1 3 1
3 4 5
```
### Output
```text
5
```
### Giải thích

Liệt kê các hành trình từ $1$ tới $4$: đi $1 \to 2 \to 4$ dài $2 + 3 = 5$; đi $1 \to 3 \to 4$ dài $1 + 5 = 6$. Không còn đường nào khác nên hành trình ngắn nhất dài $5$.

## Ràng buộc

- $1 \le n \le 10^5$, $0 \le m \le 2 \cdot 10^5$, $0 \le w \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
