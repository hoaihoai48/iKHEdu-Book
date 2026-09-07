# Chuồng bò xa nhau nhất (aggressive cows)

## Bối cảnh

Một trang trại bò sữa có dãy chuồng đặt dọc theo con đường, mỗi chuồng ở một vị trí khác nhau. Bác nông dân muốn chọn ra một số chuồng để nhốt những chú bò hay húc nhau, sao cho hai chuồng được chọn gần nhau nhất cũng càng xa nhau càng tốt.

Bác đi dọc dãy chuồng, ghi lại vị trí từng chuồng và tính xem nên chọn chuồng nào cho hợp lý.

## Nhiệm vụ

Cho vị trí các chuồng và số bò cần nhốt. Hãy lập trình tìm khoảng cách nhỏ nhất lớn nhất có thể giữa hai chuồng được chọn.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, c$ ($2 \le c \le n \le 10^5$) — số vị trí chuồng và số con bò.
- Dòng thứ hai chứa $n$ số nguyên phân biệt $x_i$ ($0 \le x_i \le 10^9$) là tọa độ các vị trí.

## Output

- In ra một dòng duy nhất là khoảng cách nhỏ nhất lớn nhất có thể đạt được giữa hai con bò kề nhau sau khi xếp cả $c$ con vào các vị trí.

## Sample 1
### Input
```text
5 3
1 2 8 4 9
```
### Output
```text
3
```
### Giải thích

Sắp xếp các vị trí: $1, 2, 4, 8, 9$. Thử khoảng cách $3$: đặt bò tại $1$, con tiếp theo đặt tại $4$ (vị trí đầu tiên cách ít nhất $3$), con thứ ba đặt tại $8$ — đủ chỗ cho $3$ con. Thử khoảng cách $4$: đặt tại $1$, tiếp theo là $8$, sau đó không còn vị trí nào cách $8$ ít nhất $4$ — chỉ xếp được $2$ con. Vậy đáp án là $3$.

## Ràng buộc

- $2 \le c \le n \le 10^5$, $0 \le x_i \le 10^9$, các $x_i$ phân biệt.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
