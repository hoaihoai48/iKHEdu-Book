# Đếm tam giác có độ dài cạnh hợp lệ

## Bối cảnh

Câu lạc bộ thủ công có một bó que với đủ loại độ dài. Các bạn muốn đếm xem có bao nhiêu cách chọn ra ba que để ghép thành một hình tam giác đúng nghĩa.

Cả nhóm sắp xếp các que từ ngắn đến dài rồi thử từng cặp, đếm xem que thứ ba dài bao nhiêu thì ghép được.

## Nhiệm vụ

Cho độ dài các que. Hãy lập trình đếm số bộ ba có thể ghép thành một tam giác không suy biến.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($3 \le n \le 5000$) — số đoạn thẳng.
- Dòng thứ hai chứa $n$ số nguyên dương $a_i$ ($1 \le a_i \le 10^9$) là độ dài các đoạn.

## Output

- In ra một dòng duy nhất là số bộ ba chỉ số $(i, j, k)$ với $i < j < k$ sao cho ba đoạn thẳng tạo thành một tam giác không suy biến (tổng hai cạnh ngắn hơn luôn lớn hơn cạnh dài nhất).

## Sample 1
### Input
```text
5
3 4 5 6 7
```
### Output
```text
9
```
### Giải thích

Sắp xếp: $3, 4, 5, 6, 7$. Cố định cạnh dài nhất là $7$: các cặp cạnh ngắn thỏa $tổng > 7$ là $(3, 6), (4, 6), (5, 6), (3, 5), (4, 5)$ — $5$ bộ. Cố định $6$: các cặp $(3, 5), (4, 5), (3, 4)$ — $3$ bộ. Cố định $5$: cặp $(3, 4)$ ($3 + 4 = 7 > 5$) — $1$ bộ. Tổng $5 + 3 + 1 = 9$.

## Ràng buộc

- $3 \le n \le 5000$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
