# Thuật toán Dijkstra chuẩn từ một nguồn

## Bối cảnh

Sở giao thông thành phố vận hành hệ thống xe buýt nhanh với N trạm và M tuyến đường hai chiều có thời gian di chuyển khác nhau tùy mật độ phương tiện. Trung tâm điều hành đặt tại trạm S cần biết thời gian ngắn nhất đến mọi trạm còn lại để phát thanh hướng dẫn hành khách trong giờ cao điểm. Vì trọng số các tuyến đều dương nên hệ thống dùng thuật toán Dijkstra và in trừ một cho trạm không thể tới được.

## Nhiệm vụ

Cho đồ thị vô hướng có trọng số dương gồm $N$ đỉnh, $M$ cạnh và đỉnh nguồn $S$. Hãy lập trình tính khoảng cách ngắn nhất từ $S$ đến mọi đỉnh bằng thuật toán Dijkstra, rồi in ra trên một dòng ($-1$ cho đỉnh không tới được).

## Input

- Dòng 1: ba số nguyên $N, M, S$ ($1 \le S \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v, w$ là cạnh hai chiều trọng số $w$ ($1 \le w \le 10^9$).

## Output

- In ra một dòng duy nhất gồm $N$ số: khoảng cách từ $S$ đến đỉnh $1, \dots, N$ ($-1$ nếu không tới được).

## Sample 1

### Input

```text
4 4 1
1 2 1
1 3 4
2 3 2
3 4 1
```

### Output

```text
0 1 3 4```

### Giải thích

- Từ trạm $1$: đến $2$ mất $1$, đến $3$ có hai phương án $4$ trực tiếp hoặc $1+2=3$ qua $2$ nên chọn $3$.
- Từ $3$ đi tiếp đến $4$ thêm $1$ thành $4$, trạm $1$ cách chính nó $0$.
- Dãy khoảng cách là $0\ 1\ 3\ 4$ nên chương trình in ra đúng dãy này.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$, $1 \le w \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
