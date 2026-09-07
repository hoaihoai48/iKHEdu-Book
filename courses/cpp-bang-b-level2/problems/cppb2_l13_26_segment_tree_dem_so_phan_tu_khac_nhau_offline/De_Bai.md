# Đếm số phần tử phân biệt offline

## Bối cảnh

Thư viện tỉnh số hoá N đầu sách xếp theo mã kệ để phục vụ bạn đọc tra cứu nhanh trong mùa thi cử. Mỗi yêu cầu mượn đưa ra một đoạn kệ và cần biết trong đoạn đó có bao nhiêu tựa sách khác nhau để thủ thư chuẩn bị đúng số phiếu mượn. Hệ thống xử lý offline sắp xếp truy vấn theo đầu phải kết hợp Fenwick đánh dấu lần xuất hiện cuối giúp trả lời mỗi truy vấn trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ cố định và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l,r)$, số giá trị phân biệt trong đoạn $a_l, \dots, a_r$, rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l, r$ ($1 \le l \le r \le N$).

## Output

- Gồm $Q$ dòng, mỗi dòng là đáp án của truy vấn tương ứng.

## Sample 1

### Input

```text
5 3
1 2 1 3 2
1 3
2 5
1 5
```

### Output

```text
2
3
3
```

### Giải thích

- Đoạn $[1,3]$ gồm $1\ 2\ 1$ có hai giá trị phân biệt là $1$ và $2$.
- Đoạn $[2,5]$ gồm $2\ 1\ 3\ 2$ có ba giá trị phân biệt là $1, 2, 3$.
- Đoạn $[1,5]$ gồm cả mảng cũng có ba giá trị phân biệt $1, 2, 3$.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
