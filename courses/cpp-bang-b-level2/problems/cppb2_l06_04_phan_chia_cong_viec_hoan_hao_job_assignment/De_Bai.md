# Phân chia công việc hoàn hảo (job assignment)

## Bối cảnh

Quản đốc một xưởng may nhận được lô hàng gấp gồm đúng $N$ công đoạn và trong xưởng cũng có đúng $N$ công nhân đang rảnh. Mỗi người thợ có tay nghề khác nhau nên thời gian hoàn thành mỗi công đoạn của từng người đều khác nhau, và bảng thời gian này đã được ghi lại đầy đủ. Quản đốc muốn giao mỗi người đúng một công đoạn sao cho tổng thời gian cả xưởng bỏ ra là ít nhất, để kịp tiến độ giao hàng cho khách.

## Nhiệm vụ

Cho bảng chi phí $cost_{ij}$ khi giao công việc $i$ cho công nhân $j$. Hãy lập trình phân công mỗi công việc cho đúng một công nhân (mỗi công nhân nhận đúng một việc) sao cho tổng chi phí nhỏ nhất, rồi in ra tổng chi phí đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 18$), là số công việc (cũng là số công nhân).
- $N$ dòng tiếp theo, mỗi dòng chứa $N$ số nguyên $cost_{ij}$ ($0 \le cost_{ij} \le 10^6$), là chi phí khi giao công việc $i$ cho công nhân $j$.

## Output

- In ra một số nguyên duy nhất là tổng chi phí nhỏ nhất của phương án phân công.

## Sample 1

### Input

```text
3
4 2 5
3 1 6
5 4 2
```

### Output

```text
7
```

### Giải thích

- Liệt kê cả $6$ cách phân công ba công việc cho ba công nhân $0, 1, 2$.
- Giao việc $0 \to 0$, $1 \to 1$, $2 \to 2$ tốn $4 + 1 + 2 = 7$.
- Giao việc $0 \to 0$, $1 \to 2$, $2 \to 1$ tốn $4 + 6 + 4 = 14$.
- Giao việc $0 \to 1$, $1 \to 0$, $2 \to 2$ tốn $2 + 3 + 2 = 7$.
- Giao việc $0 \to 1$, $1 \to 2$, $2 \to 0$ tốn $2 + 6 + 5 = 13$.
- Giao việc $0 \to 2$, $1 \to 0$, $2 \to 1$ tốn $5 + 3 + 4 = 12$.
- Giao việc $0 \to 2$, $1 \to 1$, $2 \to 0$ tốn $5 + 1 + 5 = 11$.
- Tổng nhỏ nhất trong sáu cách là $7$.

## Ràng buộc

- $1 \le N \le 18$, $0 \le cost_{ij} \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
