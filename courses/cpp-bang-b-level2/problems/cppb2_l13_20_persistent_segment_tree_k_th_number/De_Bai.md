# Số nhỏ thứ K trên đoạn (persistent)

## Bối cảnh

Sở giáo dục lưu điểm thi của N thí sinh theo số báo danh để phục vụ phúc khảo và thống kê phổ điểm theo từng cụm trường. Mỗi yêu cầu tra cứu đưa ra một đoạn số báo danh và cần biết mức điểm đứng thứ K khi xếp tăng dần trong đoạn đó nhằm xác định ngưỡng khen thưởng. Cây đoạn bền vững xây theo từng tiền tố giúp trả lời mỗi truy vấn thứ tự trong thời gian logarit mà không cần sắp xếp lại.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ cố định và $Q$ truy vấn. Hãy lập trình trả lời, với mỗi truy vấn $(l,r,k)$, giá trị nhỏ thứ $k$ trong đoạn $a_l, \dots, a_r$, rồi in ra đáp án.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng gồm $l, r, k$ ($1 \le l \le r \le N$, $1 \le k \le r-l+1$).

## Output

- Gồm $Q$ dòng, mỗi dòng là đáp án của truy vấn tương ứng.

## Sample 1

### Input

```text
5 2
5 1 4 2 3
1 5 3
2 4 2
```

### Output

```text
3
2
```

### Giải thích

- Truy vấn $(1,5,3)$: cả mảng sắp lại thành $1\ 2\ 3\ 4\ 5$, số thứ ba là $3$.
- Truy vấn $(2,4,2)$: đoạn $1\ 4\ 2$ sắp lại thành $1\ 2\ 4$, số thứ hai là $2$.
- Hai truy vấn in ra $3$ rồi $2$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
