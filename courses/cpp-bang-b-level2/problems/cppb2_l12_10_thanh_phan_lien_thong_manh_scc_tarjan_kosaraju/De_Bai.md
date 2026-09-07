# Thành phần liên thông mạnh (Tarjan/Kosaraju)

## Bối cảnh

Mạng xã hội nội bộ của tập đoàn có N tài khoản và M lượt theo dõi một chiều giữa các thành viên trong quý vừa qua. Ban truyền thông muốn nhóm các tài khoản thành từng cụm sao cho trong mỗi cụm ai cũng có thể tới được ai qua các lượt theo dõi để triển khai chiến dịch lan tỏa thông tin. Chương trình cần đếm số cụm liên thông mạnh trong toàn mạng lưới phục vụ báo cáo tổng kết chiến dịch.

## Nhiệm vụ

Cho đồ thị có hướng gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình đếm số thành phần liên thông mạnh bằng thuật toán Tarjan hoặc Kosaraju, rồi in ra kết quả.

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là cạnh có hướng $u \to v$.

## Output

- In ra một dòng duy nhất là số thành phần liên thông mạnh.

## Sample 1

### Input

```text
4 4
1 2
2 1
2 3
3 4
```

### Output

```text
3```

### Giải thích

- Hai tài khoản $1$ và $2$ theo dõi lẫn nhau nên tạo thành một cụm, còn $3$ và $4$ chỉ có cạnh một chiều đi tới.
- Các cụm là $\{1,2\}$, $\{3\}$, $\{4\}$, tổng $3$ cụm.
- Chương trình in ra $3$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
