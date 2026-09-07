# Chặt nhị phân song song (parallel binary search)

## Bối cảnh

Trạm khí tượng có nhiều cảm biến gửi số liệu về theo từng đợt. Kỹ sư trực cần trả lời cùng lúc nhiều câu hỏi dạng: với ngưỡng cho trước, đợt đo thứ mấy thì số liệu tích lũy mới vượt ngưỡng.

Thay vì trả lời từng câu hỏi một, anh kỹ sư xử lý tất cả các câu hỏi song song theo từng đợt số liệu.

## Nhiệm vụ

Cho dãy $a_1, \dots, a_n$ ghi kết quả từng đợt đo và $q$ câu hỏi, mỗi câu hỏi gồm $(l, r, target)$. Hãy lập trình trả lời với mỗi câu hỏi: vị trí $j$ nhỏ nhất trong $[l, r]$ sao cho $a_l + \dots + a_j \ge target$; in `-1` nếu tổng cả đoạn vẫn chưa đạt ngưỡng.

## Input

- Dòng đầu tiên chứa ba số nguyên $n, m, q$ ($1 \le n, q \le 2000$, $m$ là tham số dự phòng, chương trình bỏ qua) — số đợt đo và số câu hỏi.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $q$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $l, r, target$ ($1 \le l \le r \le n$).

## Output

- Với mỗi câu hỏi, in ra một dòng là vị trí $j$ thỏa mãn; in `-1` nếu không tồn tại.

## Sample 1
### Input
```text
5 0 2
1 2 3 4 5
1 5 7
2 4 10
```
### Output
```text
4
-1
```
### Giải thích

* Câu hỏi $(1, 5, 7)$: cộng dồn từ vị trí $1$: $1$, rồi $1 + 2 = 3$, rồi $+3 = 6$, rồi $+4 = 10 \ge 7$ — dừng tại vị trí $4$.
* Câu hỏi $(2, 4, 10)$: cộng dồn $2$, rồi $2 + 3 = 5$, rồi $+4 = 9 < 10$ — hết đoạn mà chưa đạt ngưỡng nên đáp án là `-1`.

## Ràng buộc

- $1 \le n, q \le 2000$, $1 \le l \le r \le n$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
