# Fenwick cập nhật đoạn, truy vấn tổng đoạn

## Bối cảnh

Quỹ học bổng thành phố phân bổ tiền hỗ trợ cho N sinh viên xếp theo mã số thứ tự để khuyến khích học tập sau đại dịch. Mỗi đợt quỹ cộng thêm một khoản vào tất cả sinh viên trong một đoạn mã số liên tiếp, và ban quản lý thường xuyên cần biết tổng số tiền của một đoạn bất kỳ để đối chiếu sổ sách kế toán. Cây Fenwick kép giúp cộng cả đoạn và hỏi tổng đoạn đều trong thời gian logarit.

## Nhiệm vụ

Cho $N$ và $Q$ thao tác, ban đầu mọi phần tử bằng $0$. Hãy lập trình xử lý: loại $1$ cộng $val$ vào mọi phần tử trên $[l,r]$; loại $2$ in ra tổng các phần tử trên $[l,r]$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ l\ r\ val$; loại $2$ gồm $2\ l\ r$ ($|val| \le 10^9$).

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là tổng trên đoạn yêu cầu.

## Sample 1

### Input

```text
5 3
1 1 3 10
1 2 5 5
2 1 5
```

### Output

```text
50```

### Giải thích

- Cộng $10$ vào $[1,3]$ rồi cộng $5$ vào $[2,5]$, mảng thành $10\ 15\ 15\ 5\ 5$.
- Tổng toàn mảng là $10 + 15 + 15 + 5 + 5 = 50$.
- Truy vấn duy nhất in ra $50$.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
