# Đường đi ngắn nhất từ một nguồn (SPFA)

## Bối cảnh

Hãng logistics xuyên quốc gia khai thác mạng N kho hàng với M tuyến vận chuyển một chiều có cước phí khác nhau, thậm chí có tuyến được trợ giá nên cước mang giá trị âm. Trung tâm điều phối đặt tại kho S cần tính cước rẻ nhất tới mọi kho còn lại để báo giá cho khách hàng, và phải phát hiện khi tồn tại chu trình âm khiến bài toán báo giá không còn ý nghĩa. Đội ngũ kỹ thuật triển khai thuật toán hàng đợi SPFA để xử lý trọng số âm hiệu quả.

## Nhiệm vụ

Cho đồ thị có hướng gồm $N$ đỉnh, $M$ cạnh có trọng số (có thể âm) và đỉnh nguồn $S$. Hãy lập trình tính khoảng cách ngắn nhất từ $S$ đến mọi đỉnh; nếu tồn tại chu trình âm tới được từ $S$ thì in ra $-1$ duy nhất.

## Input

- Dòng 1: ba số nguyên $N, M, S$ ($1 \le S \le N \le 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ là cạnh có hướng trọng số $w$ ($|w| \le 10^9$).

## Output

- Nếu có chu trình âm tới được từ $S$: in ra $-1$. Ngược lại in ra một dòng gồm $N$ số là khoảng cách từ $S$ ($-1$ cho đỉnh không tới được).

## Sample 1

### Input

```text
4 4 1
1 2 1
2 3 2
1 3 5
3 4 1
```

### Output

```text
0 1 3 4
```

### Giải thích

- Từ kho $1$: đến $2$ cước $1$, đến $3$ qua $2$ hết $1+2=3$ rẻ hơn đi thẳng giá $5$.
- Từ $3$ đến $4$ thêm $1$ thành $4$, kho $1$ cách chính nó $0$, đồ thị không có chu trình âm.
- Dãy cước là $0\ 1\ 3\ 4$ nên chương trình in ra đúng dãy này.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
