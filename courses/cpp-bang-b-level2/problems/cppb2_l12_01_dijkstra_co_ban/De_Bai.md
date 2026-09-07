# Đường Đi Ngắn Nhất Trong Thành Phố

## Bối cảnh

Thành phố có $N$ ngã tư được đánh số từ $1$ đến $N$, nối với nhau bởi $M$ con đường một chiều, mỗi con đường có thời gian di chuyển $w$ không âm. Đội giao hàng cần đi từ kho ở ngã tư số $1$ đến cửa hàng ở ngã tư số $N$ sao cho tổng thời gian di chuyển là ít nhất. Nếu có nhiều cách đi, đội giao hàng chỉ cần biết tổng thời gian nhỏ nhất có thể đạt được.

## Nhiệm vụ

Cho đồ thị có hướng gồm $N$ đỉnh và $M$ cạnh có trọng số không âm. Hãy lập trình tính tổng thời gian di chuyển nhỏ nhất từ đỉnh $1$ đến đỉnh $N$.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, M$ ($1 \le N \le 10^5$, $1 \le M \le 2 \times 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $u, v, w$ ($1 \le u, v \le N$, $0 \le w \le 10^9$), mô tả một con đường một chiều từ $u$ đến $v$ với thời gian di chuyển $w$.

## Output

- In ra một số nguyên duy nhất là tổng thời gian di chuyển nhỏ nhất từ đỉnh $1$ đến đỉnh $N$.
- Nếu không tồn tại đường đi từ $1$ đến $N$ (kể cả trường hợp $N = 1$ thì khoảng cách bằng $0$), in ra `-1`.

## Sample 1

### Input

```text
3 3
1 2 1
2 3 2
1 3 4
```

### Output

```text
3
```

### Giải thích

- Có hai cách đi từ ngã tư $1$ đến ngã tư $3$.
- Cách thứ nhất đi thẳng $1 \to 3$ với tổng thời gian $4$.
- Cách thứ hai đi vòng $1 \to 2 \to 3$ với tổng thời gian $1 + 2 = 3$.
- Vì $3$ nhỏ hơn $4$ nên đáp án là $3$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le M \le 2 \times 10^5$, $0 \le w \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
