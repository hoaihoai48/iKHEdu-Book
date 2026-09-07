# BFS trên đồ thị trọng số 0-1 (0-1 BFS)

## Bối cảnh

Ban quản lý phố cổ lắp hệ thống đèn dẫn đường thông minh nối N nút giao bằng M đoạn phố hai chiều, mỗi đoạn hoặc đã có đèn sáng đi qua miễn phí hoặc còn tối phải tốn một đơn vị pin để bật đèn tạm thời. Đoàn kiểm tra xuất phát từ nút S cần khảo sát chi phí pin tối thiểu tới mọi nút còn lại trong đêm tổng duyệt lễ hội. Vì mỗi đoạn phố chỉ tốn 0 hoặc 1 đơn vị pin nên đoàn dùng thuật toán 0-1 BFS với hàng đợi hai đầu.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh, $M$ cạnh trọng số $0$ hoặc $1$ và đỉnh xuất phát $S$. Hãy lập trình tính chi phí nhỏ nhất từ $S$ đến mọi đỉnh bằng thuật toán 0-1 BFS, rồi in ra trên một dòng ($-1$ cho đỉnh không tới được).

## Input

- Dòng 1: ba số nguyên $N, M, S$ ($1 \le S \le N \le 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ với $w \in \{0, 1\}$.

## Output

- In ra một dòng duy nhất gồm $N$ số là chi phí tối thiểu từ $S$ đến từng đỉnh ($-1$ nếu không tới được).

## Sample 1

### Input

```text
4 3 1
1 2 0
2 3 1
1 4 1
```

### Output

```text
0 0 1 1
```

### Giải thích

- Từ nút $1$: sang $2$ tốn $0$ nên chi phí vẫn $0$; sang $4$ tốn $1$.
- Từ $2$ sang $3$ tốn thêm $1$ thành $1$, không còn đường nào rẻ hơn.
- Dãy chi phí là $0\ 0\ 1\ 1$ nên chương trình in ra đúng dãy này.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
