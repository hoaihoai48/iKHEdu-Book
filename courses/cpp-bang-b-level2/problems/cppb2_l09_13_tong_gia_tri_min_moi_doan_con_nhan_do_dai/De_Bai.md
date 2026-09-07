# Tổng giá trị min mọi đoạn con nhân độ dài

## Bối cảnh

Công ty du lịch thiết kế các tour ngắn ngày đi qua một dãy $N$ điểm tham quan liên tiếp, mỗi điểm có một mức độ hấp dẫn khác nhau. Với mỗi tour (một đoạn liên tiếp các điểm), công ty đánh giá chất lượng tour bằng điểm hấp dẫn thấp nhất trong tour nhân với số điểm mà tour ghé qua. Để chọn chiến lược quảng cáo cho cả mùa du lịch, công ty cần tính tổng điểm chất lượng của tất cả các tour có thể tổ chức.

## Nhiệm vụ

Cho $N$ số nguyên là điểm hấp dẫn của từng điểm theo thứ tự. Với mỗi đoạn liên tục, tính giá trị nhỏ nhất trong đoạn nhân với độ dài của đoạn. Hãy lập trình tính tổng các giá trị này trên mọi đoạn liên tục, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số điểm tham quan.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^6$), là điểm hấp dẫn từng nơi.

## Output

- In ra một số nguyên duy nhất là tổng trên mọi đoạn liên tục.

## Sample 1

### Input

```text
3
1 2 3
```

### Output

```text
15
```

### Giải thích

- Liệt kê cả $6$ đoạn liên tục cùng giá trị nhỏ nhất nhân độ dài của từng đoạn.
- Ba đoạn một điểm cho $1 \times 1 = 1$, $2 \times 1 = 2$, $3 \times 1 = 3$.
- Đoạn $[1, 2]$ cho $1 \times 2 = 2$; đoạn $[2, 3]$ cho $2 \times 2 = 4$.
- Đoạn $[1, 2, 3]$ cho $1 \times 3 = 3$.
- Tổng là $1 + 2 + 3 + 2 + 4 + 3 = 15$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
