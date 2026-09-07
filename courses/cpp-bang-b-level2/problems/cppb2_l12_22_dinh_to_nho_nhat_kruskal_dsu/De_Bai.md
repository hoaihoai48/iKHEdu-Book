# Cây khung nhỏ nhất Kruskal

## Bối cảnh

Huyện miền núi triển khai dự án thắp sáng với N thôn bản cần nối điện bằng các tuyến dây có chi phí khác nhau do phải vượt đèo và sông suối. Yêu cầu toàn mạng liên thông với tổng chi phí thấp nhất để trình hội đồng phê duyệt vốn đầu tư công, và nếu địa hình chia cắt không thể nối hết thì hồ sơ phải ghi rõ không khả thi. Tổ thiết kế dùng thuật toán Kruskal sắp xếp tuyến dây theo chi phí tăng dần kết hợp kiểm tra chu trình bằng DSU.

## Nhiệm vụ

Cho đồ thị vô hướng có trọng số gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình tính tổng trọng số cây khung nhỏ nhất bằng thuật toán Kruskal, rồi in ra kết quả (in ra $IMPOSSIBLE$ nếu đồ thị không liên thông).

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ ($1 \le w \le 10^9$).

## Output

- In ra một dòng duy nhất là tổng trọng số MST, hoặc $IMPOSSIBLE$ nếu không liên thông được.

## Sample 1

### Input

```text
4 5
1 2 1
2 3 2
3 4 3
4 1 4
1 3 5
```

### Output

```text
6
```

### Giải thích

- Xét các tuyến dây theo chi phí tăng dần: chọn $1-2$ giá $1$, rồi $2-3$ giá $2$.
- Tuyến $3-4$ giá $3$ nối thôn cuối cùng vào mạng mà không tạo chu trình, tổng thành $6$.
- Các tuyến còn lại đều tạo chu trình nên bị bỏ, chương trình in ra $6$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
