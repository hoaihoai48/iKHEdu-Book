# Dijkstra nhiều tầng với K vé miễn phí

## Bối cảnh

Liên minh hàng không triển khai gói ưu đãi cho phép hành khách bay qua tối đa K chặng bất kỳ mà không phải trả thêm phí trên mạng N sân bay với M đường bay hai chiều có giá vé khác nhau. Một gia đình muốn bay từ sân bay 1 đến sân bay N với tổng chi phí thấp nhất bằng cách tận dụng tối đa K lượt miễn phí của gói ưu đãi. Tổng đài đặt vé cần tính chi phí tối ưu bằng mô hình đồ thị nhiều tầng kết hợp thuật toán Dijkstra.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh, $M$ cạnh có trọng số không âm và số nguyên $K$. Hãy lập trình tính chi phí nhỏ nhất từ đỉnh $1$ đến đỉnh $N$ khi được miễn phí tối đa $K$ cạnh trên hành trình, rồi in ra kết quả ($-1$ nếu không tới được).

## Input

- Dòng 1: ba số nguyên $N, M, K$ ($1 \le N \le 10^4$, $0 \le K \le 10$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ là đường bay hai chiều giá $w$ ($0 \le w \le 10^9$).

## Output

- In ra một dòng duy nhất là chi phí tối ưu ($-1$ nếu không tới được).

## Sample 1

### Input

```text
3 3 1
1 2 5
2 3 5
1 3 12
```

### Output

```text
0
```

### Giải thích

- Hành trình $1 \to 2 \to 3$ tốn $10$, hành trình bay thẳng $1 \to 3$ tốn $12$.
- Dùng lượt miễn phí cho chặng bay thẳng $12$ thì chi phí còn $0$, tốt hơn miễn phí một chặng $5$ ở hành trình hai chặng (còn $5$).
- Đáp án tối ưu là $0$ nên chương trình in ra $0$.

## Ràng buộc

- $1 \le N \le 10^4$, $0 \le K \le 10$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
