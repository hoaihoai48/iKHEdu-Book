# Segment Tree Beats chmin và tổng đoạn

## Bối cảnh

Hiệp hội bán lẻ quản lý N mặt hàng với giá niêm yết khác nhau và định kỳ áp giá trần mới cho từng nhóm hàng để thực hiện chương trình bình ổn thị trường cuối năm. Mỗi đợt điều chỉnh hạ mọi mức giá trong đoạn xuống không quá trần mới, đồng thời bộ phận tài chính cần tra cứu tổng giá trị của đoạn bất kỳ để dự báo doanh thu. Cây đoạn Beats xử lý phép chmin trên đoạn trong thời gian gần logarit trên thực tế.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ thực hiện $a[i] = \min(a[i], val)$ với mọi $i$ trong $[l,r]$; loại $2$ in ra tổng trên $[l,r]$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ l\ r\ val$; loại $2$ gồm $2\ l\ r$.

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là tổng trên đoạn yêu cầu.

## Sample 1

### Input

```text
5 3
5 4 3 2 1
2 1 5
1 1 5 3
2 1 5
```

### Output

```text
15
12
```

### Giải thích

- Mảng $5\ 4\ 3\ 2\ 1$: tổng toàn mảng là $15$.
- Chmin toàn mảng với $3$ được $3\ 3\ 3\ 2\ 1$: tổng còn $3+3+3+2+1 = 12$.
- Hai thao tác loại $2$ in ra $15$ rồi $12$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 10^5$; $|a_i|, |val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
