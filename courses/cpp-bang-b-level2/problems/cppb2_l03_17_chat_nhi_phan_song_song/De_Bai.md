# Chặt nhị phân song song

## Bối cảnh
Cho một hệ thống gồm $N$ trạm thiên văn và $Q$ thiên thạch di chuyển. Mỗi thiên thạch cần thu thập ít nhất $P_i$ đơn vị năng lượng từ các trạm thiên văn trong phạm vi kiểm soát của nó sau một số mốc thời gian $M$. Sau mỗi mốc thời gian $t$, một trạm thiên văn sẽ phát ra một lượng sóng năng lượng.

## Nhiệm vụ
Với mỗi thiên thạch, hãy tìm mốc thời gian $t$ nhỏ nhất ($1 \le t \le N$) để thiên thạch đó tích lũy đủ số năng lượng $P_i$. Nếu không thể tích lũy đủ sau tất cả $N$ mốc thời gian, hãy in ra `-1`.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$) — số mốc thời gian và số lượng thiên thạch.
- Dòng 2: $N$ số nguyên biểu thị năng lượng phát ra tại các trạm theo thứ tự thời gian.
- Dòng 3: $Q$ số nguyên $P_1, P_2, \dots, P_Q$ ($1 \le P_i \le 10^9$) — lượng năng lượng yêu cầu của từng thiên thạch.

## Output
- In ra $Q$ dòng, mỗi dòng chứa mốc thời gian nhỏ nhất tương ứng cho từng thiên thạch.

## Sample 1
### Input
```text
5 3
10 20 30 40 50
15 55 200
```
### Output
```text
2
3
-1
```
### Giải thích
* Thiên thạch 1 cần $15$ năng lượng: tại mốc $t=1$ có $10$, tại mốc $t=2$ tích lũy tổng $30 \ge 15$, do đó đáp án là $2$.
* Thiên thạch 2 cần $55$ năng lượng: tại $t=3$ tích lũy tổng $60 \ge 55$, đáp án là $3$.
* Thiên thạch 3 cần $200$ năng lượng: sau cả $5$ mốc chỉ tích lũy được $150 < 200$, in ra `-1`.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le P_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
