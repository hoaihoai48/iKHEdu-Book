# Phát hiện chu trình âm (Bellman-Ford)

## Bối cảnh

Sở giao dịch ngoại tệ theo dõi N loại tiền với M cặp quy đổi một chiều có tỉ giá được mã hoá thành chi phí có thể mang giá trị âm do ưu đãi phí chuyển đổi. Phòng phân tích cần phát hiện xem thị trường có tồn tại chu trình quy đổi mà tổng chi phí âm hay không để kịp thời cảnh báo rủi ro cho các quỹ đầu tư. Thuật toán Bellman-Ford nới lỏng toàn bộ cạnh đúng N vòng được chọn để cho kết luận chính xác.

## Nhiệm vụ

Cho đồ thị có hướng gồm $N$ đỉnh và $M$ cạnh có trọng số (có thể âm). Hãy lập trình kiểm tra tồn tại chu trình âm bằng thuật toán Bellman-Ford, rồi in ra $YES$ nếu có và $NO$ nếu không.

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ là cạnh có hướng trọng số $w$ ($|w| \le 10^9$).

## Output

- In ra một dòng duy nhất: $YES$ nếu tồn tại chu trình âm, ngược lại $NO$.

## Sample 1

### Input

```text
3 3
1 2 1
2 3 -1
3 1 -1
```

### Output

```text
YES
```

### Giải thích

- Chu trình $1 \to 2 \to 3 \to 1$ có tổng trọng số $1 + (-1) + (-1) = -1$ là số âm.
- Thuật toán Bellman-Ford sau đủ vòng nới lỏng vẫn còn cạnh cải thiện được nên kết luận có chu trình âm.
- Chương trình in ra $YES$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
