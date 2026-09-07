# Segment Tree Beats với phép chmin

## Bối cảnh

Công ty bảo hiểm quản lý N hợp đồng với mức phí khác nhau và định kỳ áp trần phí mới cho từng nhóm hợp đồng để tuân thủ quy định của bộ tài chính. Mỗi đợt điều chỉnh gán mỗi mức phí trong đoạn thành giá trị nhỏ hơn giữa phí cũ và trần mới, đồng thời kế toán cần tra cứu tổng phí của đoạn bất kỳ để lập báo cáo doanh thu. Cây đoạn Beats tối ưu phép chmin giúp mỗi thao tác chạy gần như logarit trên thực tế.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ thực hiện $a[i] = \min(a[i], x)$ với mọi $i$ trong $[l,r]$; loại $2$ in ra tổng trên $[l,r]$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ l\ r\ x$; loại $2$ gồm $2\ l\ r$.

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
12```

### Giải thích

- Mảng $5\ 4\ 3\ 2\ 1$: tổng toàn mảng là $15$.
- Chmin toàn mảng với $3$ được $3\ 3\ 3\ 2\ 1$: tổng còn $3+3+3+2+1 = 12$.
- Hai truy vấn loại $2$ in ra $15$ rồi $12$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i|, |x| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
