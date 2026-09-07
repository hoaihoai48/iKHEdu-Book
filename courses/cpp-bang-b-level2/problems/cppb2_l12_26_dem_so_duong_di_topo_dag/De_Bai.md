# Đếm số đường đi trên DAG theo topo

## Bối cảnh

Khu công nghiệp công nghệ cao thiết kế dây chuyền gồm N công đoạn với M đường chuyển linh kiện một chiều tạo thành đồ thị không chu trình để tránh tắc nghẽn vòng lặp. Phòng kế hoạch cần biết có bao nhiêu tuyến đường khác nhau đưa linh kiện từ công đoạn khởi đầu S đến công đoạn hoàn thiện T nhằm dự phòng khi một số băng tải phải bảo trì. Chương trình duyệt các công đoạn theo thứ tự topo và cộng dồn số cách đi tới từng điểm.

## Nhiệm vụ

Cho đồ thị có hướng không chu trình gồm $N$ đỉnh, $M$ cạnh cùng hai đỉnh $S, T$. Hãy lập trình đếm số đường đi có hướng từ $S$ đến $T$ theo thứ tự topo, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng 1: bốn số nguyên $N, M, S, T$ ($1 \le S, T \le N \le 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là cạnh có hướng $u \to v$ (đồ thị đảm bảo không chu trình).

## Output

- In ra một dòng duy nhất là số đường đi từ $S$ đến $T$ theo modulo $1\,000\,000\,007$.

## Sample 1

### Input

```text
4 4 1 4
1 2
1 3
2 4
3 4
```

### Output

```text
2
```

### Giải thích

- Từ công đoạn $1$ linh kiện có thể sang $2$ hoặc sang $3$.
- Cả hai nhánh $1 \to 2 \to 4$ và $1 \to 3 \to 4$ đều về đích $4$.
- Có $2$ tuyến đường nên chương trình in ra $2$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
