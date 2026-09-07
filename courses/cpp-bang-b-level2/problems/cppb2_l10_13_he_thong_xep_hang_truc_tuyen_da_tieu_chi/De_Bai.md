# Hệ thống xếp hạng trực tuyến đa tiêu chí

## Bối cảnh

Thư viện điện tử lưu điểm số của $N$ đầu sách đã được sắp xếp tăng dần theo lượt mượn để tiện tra cứu. Trong ngày, thủ thư nhận được nhiều yêu cầu thống kê, mỗi yêu cầu cho một khoảng điểm $[l, r]$ và muốn biết có bao nhiêu đầu sách có lượt mượn nằm trong khoảng đó để chuẩn bị báo cáo bổ sung ngân sách mua sách mới. Vì số yêu cầu rất lớn, thủ thư cần một chương trình trả lời mỗi truy vấn gần như ngay lập tức.

## Nhiệm vụ

Cho dãy $N$ số nguyên đã sắp xếp tăng dần và $Q$ truy vấn, mỗi truy vấn gồm hai số $l, r$. Với mỗi truy vấn, hãy lập trình đếm số phần tử của dãy nằm trong đoạn $[l, r]$, rồi in ra kết quả trên một dòng.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 10^5$), là số đầu sách và số truy vấn.
- Dòng thứ hai chứa $N$ số nguyên tăng dần $a_i$ ($1 \le a_i \le 10^9$), là lượt mượn từng đầu sách.
- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $l, r$ ($1 \le l \le r \le 10^9$), là một khoảng điểm.

## Output

- In ra $Q$ dòng, mỗi dòng là đáp án của một truy vấn.

## Sample 1

### Input

```text
5 2
1 3 5 7 9
2 6
1 9
```

### Output

```text
2
5
```

### Giải thích

- Dãy lượt mượn đã sắp xếp là $1, 3, 5, 7, 9$.
- Truy vấn $[2, 6]$: các số trong đoạn là $3$ và $5$ nên đáp án $2$.
- Truy vấn $[1, 9]$: cả năm số đều nằm trong đoạn nên đáp án $5$.

## Ràng buộc

- $1 \le N, Q \le 10^5$, dãy $a$ tăng dần, $1 \le a_i \le 10^9$, $1 \le l \le r \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
