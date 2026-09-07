# Tổ tiên chung gần nhất (LCA binary lifting)

## Bối cảnh

Công ty gia phả số hoá cây dòng họ gồm N thành viên với quan hệ cha con rõ ràng tạo thành một cây có gốc là cụ tổ. Mỗi ngày hệ thống nhận nhiều yêu cầu tìm cụ chung gần nhất của hai thành viên để xác định vai vế trong họ tộc phục vụ việc xếp cỗ ngày giỗ tổ. Vì số lượng truy vấn rất lớn nên hệ thống tiền xử lý nhảy nhị phân để trả lời mỗi yêu cầu gần như tức thì.

## Nhiệm vụ

Cho cây gồm $N$ đỉnh (gốc $1$) và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(u,v)$, đỉnh tổ tiên chung gần nhất của $u$ và $v$ bằng thuật toán binary lifting.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- $N-1$ dòng tiếp theo, mỗi dòng gồm $u, v$ là một cạnh của cây.
- $Q$ dòng tiếp theo, mỗi dòng gồm $u, v$ là một truy vấn.

## Output

- Gồm $Q$ dòng, mỗi dòng là đáp án của truy vấn tương ứng.

## Sample 1

### Input

```text
5 2
1 2
1 3
2 4
2 5
4 5
3 4
```

### Output

```text
2
1```

### Giải thích

- Cây có gốc $1$: $2$ và $3$ là con của $1$; $4$ và $5$ là con của $2$.
- Truy vấn $(4,5)$ gặp nhau gần nhất ở $2$; truy vấn $(3,4)$ phải lên tận gốc $1$ mới gặp nhau.
- Chương trình in ra $2$ rồi $1$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
