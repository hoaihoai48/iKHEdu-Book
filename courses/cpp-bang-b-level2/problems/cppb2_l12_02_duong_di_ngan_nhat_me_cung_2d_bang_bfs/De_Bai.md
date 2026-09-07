# Đường đi ngắn nhất trên đồ thị vô trọng số (BFS)

## Bối cảnh

Khu di tích cố đô mở tour tham quan bằng xe điện với N điểm dừng được nối với nhau bằng M đoạn đường hai chiều có độ dài bằng nhau. Du khách lên xe tại điểm S và muốn xuống tại điểm T với số đoạn đường đi qua là ít nhất để kịp giờ xem biểu diễn nghệ thuật buổi tối. Điều hành tour cần một chương trình tính số đoạn đường tối thiểu cho mọi sơ đồ tuyến, in ra trừ một khi hai điểm không thể đến được nhau.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh, $M$ cạnh, cùng hai đỉnh $S, T$. Hãy lập trình tính độ dài (số cạnh) của đường đi ngắn nhất từ $S$ đến $T$ bằng thuật toán BFS, rồi in ra kết quả ($-1$ nếu không có đường đi).

## Input

- Dòng 1: bốn số nguyên $N, M, S, T$ ($1 \le S, T \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là một cạnh hai chiều.

## Output

- In ra một dòng duy nhất là số cạnh của đường đi ngắn nhất từ $S$ đến $T$ ($-1$ nếu không tới được).

## Sample 1

### Input

```text
5 4 1 5
1 2
2 3
3 4
4 5
```

### Output

```text
4
```

### Giải thích

- Tuyến xe là một đường thẳng $1-2-3-4-5$, xuất phát $S = 1$, đích $T = 5$.
- BFS lan từ $1$: thăm $2$ ở khoảng cách $1$, $3$ ở khoảng cách $2$, $4$ ở khoảng cách $3$, $5$ ở khoảng cách $4$.
- Đích đến ở khoảng cách $4$ nên chương trình in ra $4$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
