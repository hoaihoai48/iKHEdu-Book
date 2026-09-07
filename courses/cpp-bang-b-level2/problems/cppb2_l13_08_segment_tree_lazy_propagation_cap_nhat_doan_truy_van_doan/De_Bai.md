# Tổng đoạn con lớn nhất trên đoạn truy vấn

## Bối cảnh

Công ty chứng khoán phân tích N phiên giao dịch liên tiếp với mức lãi lỗ của cổ phiếu chủ lực để tư vấn khung thời gian nắm giữ tối ưu cho khách hàng. Mỗi yêu cầu tư vấn đưa ra một khoảng thời gian và cần biết tổng lợi nhuận lớn nhất của một chuỗi phiên liên tiếp nằm trong khoảng đó. Cây đoạn lưu tổng, tiền tố, hậu tố và đáp án tốt nhất mỗi nút giúp trả lời từng truy vấn trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ cố định và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l,r)$, tổng lớn nhất của một đoạn con liên tiếp nằm trong $[l,r]$, rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l, r$ ($1 \le l \le r \le N$).

## Output

- Gồm $Q$ dòng, mỗi dòng là tổng đoạn con lớn nhất trong đoạn tương ứng.

## Sample 1

### Input

```text
5 2
-1 2 3 -2 5
1 5
1 4
```

### Output

```text
8
5
```

### Giải thích

- Toàn mảng $-1\ 2\ 3\ -2\ 5$: đoạn con tốt nhất là $2 + 3 + (-2) + 5 = 8$.
- Trên $[1,4]$ gồm $-1\ 2\ 3\ -2$: đoạn tốt nhất là $2 + 3 = 5$ (thêm $-2$ chỉ làm giảm tổng).
- Hai truy vấn in ra $8$ rồi $5$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
