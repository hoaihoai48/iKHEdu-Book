# Tổng thời gian chờ nhỏ nhất (sjf)

## Bối cảnh

Phòng khám đa khoa của phường mỗi sáng tiếp nhận một hàng dài bệnh nhân đến khám, mỗi người cần một khoảng thời gian khám khác nhau đã được y tá ước tính từ trước. Chỉ có một bác sĩ trực nên mọi người phải xếp hàng chờ đến lượt mình. Ban quản lý phòng khám muốn sắp xếp thứ tự khám sao cho tổng thời gian chờ của tất cả bệnh nhân là nhỏ nhất, để không ai phải ngồi đợi quá lâu mà bác sĩ vẫn khám hết được mọi người trong buổi sáng.

## Nhiệm vụ

Cho $N$ số nguyên là thời gian khám của từng bệnh nhân. Hãy lập trình sắp xếp thứ tự khám sao cho tổng thời gian chờ của tất cả mọi người là nhỏ nhất (thời gian chờ của một người bằng tổng thời gian khám của những người khám trước họ), rồi in ra tổng nhỏ nhất đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số bệnh nhân.
- Dòng thứ hai chứa $N$ số nguyên $t_i$ ($1 \le t_i \le 10^6$), là thời gian khám của từng người.

## Output

- In ra một số nguyên duy nhất là tổng thời gian chờ nhỏ nhất.

## Sample 1

### Input

```text
4
3 1 2 5
```

### Output

```text
10
```

### Giải thích

- Sắp xếp bốn người theo thời gian khám tăng dần: $1, 2, 3, 5$.
- Người đầu tiên không phải chờ ai nên thời gian chờ là $0$.
- Người thứ hai chờ $1$; người thứ ba chờ $1 + 2 = 3$; người thứ tư chờ $1 + 2 + 3 = 6$.
- Tổng thời gian chờ là $0 + 1 + 3 + 6 = 10$, và không có thứ tự nào cho tổng nhỏ hơn.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le t_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
