# Truy vấn GCD trên đoạn (static)

## Bối cảnh

Nhà máy chế biến gỗ cần cắt các thanh gỗ nguyên liệu có độ dài khác nhau thành từng khúc bằng nhau mà không để thừa phế liệu trong ca sản xuất mới. Với mỗi đơn hàng yêu cầu một đoạn các thanh liên tiếp, tổ trưởng cần biết độ dài lớn nhất có thể của mỗi khúc cắt chính là ước chung lớn nhất của đoạn đó. Hệ thống dùng bảng thưa Sparse Table để trả lời mỗi truy vấn GCD trong thời gian hằng số sau khi tiền xử lý logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l,r)$, ước chung lớn nhất của các phần tử $a_l, \dots, a_r$, rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên dương $a_i$ ($1 \le a_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l, r$ ($1 \le l \le r \le N$).

## Output

- Gồm $Q$ dòng, mỗi dòng là GCD của đoạn tương ứng.

## Sample 1

### Input

```text
5 3
4 6 10 15 30
1 3
2 4
1 5
```

### Output

```text
2
1
1```

### Giải thích

- Đoạn $[1,3]$ gồm $4, 6, 10$: ước chung lớn nhất là $2$.
- Đoạn $[2,4]$ gồm $6, 10, 15$: ước chung lớn nhất là $1$.
- Đoạn $[1,5]$ gồm cả năm số: ước chung lớn nhất cũng là $1$.
- Chương trình in ra $2$ rồi $1$ rồi $1$ trên ba dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
