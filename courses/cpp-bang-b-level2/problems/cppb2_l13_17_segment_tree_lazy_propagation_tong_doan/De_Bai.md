# Cộng đoạn, tổng đoạn (lazy)

## Bối cảnh

Sở nông nghiệp theo dõi năng suất của N thửa ruộng xếp liên tiếp nhau để tính toán lượng phân bón hỗ trợ sau mỗi đợt kiểm tra đồng ruộng. Mỗi đợt hỗ trợ cộng thêm cùng một lượng vào mọi thửa trong một đoạn, và cán bộ thống kê cần biết tổng năng suất của đoạn bất kỳ để lập báo cáo sản lượng quý. Cây đoạn lười cộng đoạn giúp cả hai thao tác đều chạy trong thời gian logarit trên đồng ruộng rộng lớn.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ cộng $val$ vào mọi phần tử trên $[l,r]$; loại $2$ in ra tổng trên $[l,r]$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ l\ r\ val$; loại $2$ gồm $2\ l\ r$ ($|val| \le 10^9$).

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là tổng trên đoạn yêu cầu.

## Sample 1

### Input

```text
5 3
1 2 3 4 5
1 2 4 10
2 1 5
2 2 3
```

### Output

```text
45
25
```

### Giải thích

- Cộng $10$ vào đoạn $[2,4]$ được mảng $1\ 12\ 13\ 14\ 5$.
- Tổng toàn mảng là $1+12+13+14+5 = 45$; tổng đoạn $[2,3]$ là $12+13 = 25$.
- Hai thao tác loại $2$ in ra $45$ rồi $25$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i|, |val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
