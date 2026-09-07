# Đường đi ngắn nhất mọi cặp đỉnh (Floyd-Warshall)

## Bối cảnh

Tổng công ty chuyển phát nhanh khai thác mạng N bưu cục với M tuyến đường hai chiều có thời gian di chuyển khác nhau giữa các tỉnh thành. Để in bảng tra cứu thời gian vận chuyển cho toàn bộ cặp bưu cục phục vụ khách hàng tại quầy, trung tâm dữ liệu chạy thuật toán Floyd-Warshall xét mọi đỉnh trung gian và thay vô cực bằng trừ một cho các cặp không thể đi tới nhau.

## Nhiệm vụ

Cho đồ thị vô hướng có trọng số không âm gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình tính khoảng cách ngắn nhất giữa mọi cặp đỉnh bằng thuật toán Floyd-Warshall, rồi in ra ma trận $N \times N$ ($-1$ cho cặp không tới được).

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 500$, $0 \le M \le 10^4$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ là cạnh hai chiều ($1 \le w \le 10^9$).

## Output

- In ra $N$ dòng, dòng $i$ gồm $N$ số là khoảng cách từ $i$ đến mọi đỉnh ($-1$ nếu không tới được).

## Sample 1

### Input

```text
3 2
1 2 4
2 3 1
```

### Output

```text
0 4 5
4 0 1
5 1 0
```

### Giải thích

- Tuyến $1-2$ mất $4$, tuyến $2-3$ mất $1$, từ $1$ đến $3$ phải qua $2$ hết $4+1=5$.
- Ma trận khoảng cách đối xứng với đường chéo chính bằng $0$.
- Chương trình in ra ba dòng $0\ 4\ 5$, $4\ 0\ 1$ và $5\ 1\ 0$.

## Ràng buộc

- $1 \le N \le 500$, $0 \le M \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
