# Mê cung trọng số 0-1 (thuật toán 0-1 BFS)

## Bối cảnh

Nhóm cứu hộ cần đưa thiết bị y tế qua khu nhà xưởng có N phòng nối với nhau bằng M hành lang hai chiều, mỗi hành lang hoặc thông thoáng đi qua không tốn phí hoặc bị chặn một phần phải tốn một đơn vị chi phí dọn dẹp. Đội trưởng xuất phát từ phòng S muốn chọn hành trình tốn ít chi phí nhất tới mọi phòng còn lại để phân bổ ngân sách cứu trợ. Vì chi phí mỗi hành lang chỉ là 0 hoặc 1 nên đội dùng thuật toán 0-1 BFS với hàng đợi hai đầu.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh, $M$ cạnh trọng số $0$ hoặc $1$ và đỉnh xuất phát $S$. Hãy lập trình tính chi phí nhỏ nhất từ $S$ đến mọi đỉnh bằng thuật toán 0-1 BFS, rồi in ra trên một dòng ($-1$ cho đỉnh không tới được).

## Input

- Dòng 1: ba số nguyên $N, M, S$ ($1 \le S \le N \le 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ với $w \in \{0, 1\}$.

## Output

- In ra một dòng duy nhất gồm $N$ số là chi phí nhỏ nhất từ $S$ đến từng đỉnh ($-1$ nếu không tới được).

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
0 0 1 1```

### Giải thích

- Từ phòng $1$: sang $2$ tốn $0$ nên chi phí vẫn $0$; sang $4$ tốn $1$.
- Từ $2$ sang $3$ tốn thêm $1$ thành $1$, không còn đường nào rẻ hơn.
- Dãy chi phí là $0\ 0\ 1\ 1$ nên chương trình in ra đúng dãy này.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
