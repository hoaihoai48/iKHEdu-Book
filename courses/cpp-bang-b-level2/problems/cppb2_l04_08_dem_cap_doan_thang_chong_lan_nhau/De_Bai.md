# Đếm cặp đoạn thẳng chồng lấn nhau

## Bối cảnh

Trên tuyến đường chạy, mỗi vận động viên đăng ký một đoạn đường mình sẽ chạy tiếp sức. Ban trọng tài muốn đếm có bao nhiêu cặp vận động viên có đoạn đường giao nhau để sắp xếp lịch xuất phát.

Tổ trọng tài ghi lại điểm đầu và điểm cuối của từng người rồi đếm các cặp chồng lấn.

## Nhiệm vụ

Cho danh sách các đoạn thẳng trên trục số. Hãy lập trình đếm số cặp đoạn thẳng có phần giao nhau.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 2 \cdot 10^5$) — số đoạn thẳng.
- $n$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $l, r$ ($|l|, |r| \le 10^9$, $l \le r$) là hai đầu mút của một đoạn (hai đoạn chung nhau dù chỉ một đầu mút cũng tính là chồng lấn).

## Output

- In ra một dòng duy nhất là số cặp đoạn thẳng chồng lấn nhau.

## Sample 1
### Input
```text
3
1 3
2 4
5 6
```
### Output
```text
1
```
### Giải thích

Đoạn $[1, 3]$ và $[2, 4]$ giao nhau trên $[2, 3]$ → $1$ cặp. Đoạn $[5, 6]$ nằm tách biệt, không giao đoạn nào. Vậy đáp án là $1$.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
