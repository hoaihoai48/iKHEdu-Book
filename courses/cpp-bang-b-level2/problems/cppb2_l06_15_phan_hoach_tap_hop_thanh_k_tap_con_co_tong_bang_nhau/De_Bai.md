# Phân hoạch tập hợp thành k tập con có tổng bằng nhau

## Bối cảnh

Cô giáo chủ nhiệm cần chia lớp thành $K$ nhóm có tổng điểm năng lực bằng nhau để cuộc thi đấu kiến thức giữa các nhóm được công bằng. Mỗi bạn học sinh có một điểm năng lực riêng đã được ghi nhận từ đầu năm, và mỗi bạn chỉ thuộc đúng một nhóm. Trước khi công bố danh sách, cô muốn biết liệu có cách chia nào thỏa mãn điều kiện tổng điểm bằng nhau hay không, để còn điều chỉnh số lượng nhóm cho phù hợp với sĩ số lớp.

## Nhiệm vụ

Cho $N$ số nguyên là điểm năng lực của từng bạn và số nguyên $K$. Hãy lập trình kiểm tra xem có thể chia tất cả các bạn thành $K$ nhóm (mỗi bạn đúng một nhóm) sao cho tổng điểm của $K$ nhóm bằng nhau hay không. In ra `YES` nếu chia được và `NO` nếu không.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, K$ ($1 \le K \le N \le 18$), là số học sinh và số nhóm.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^6$), là điểm năng lực của từng bạn.

## Output

- In ra `YES` nếu chia được thành $K$ nhóm có tổng bằng nhau, ngược lại in ra `NO`.

## Sample 1

### Input

```text
4 2
1 5 11 5
```

### Output

```text
YES
```

### Giải thích

- Tổng điểm cả lớp là $1 + 5 + 11 + 5 = 22$, chia cho $K = 2$ nhóm thì mỗi nhóm phải có tổng $11$.
- Xếp bạn điểm $11$ một mình thành một nhóm, tổng đúng $11$.
- Ba bạn còn lại điểm $1, 5, 5$ thành nhóm kia, tổng $1 + 5 + 5 = 11$.
- Hai nhóm đều có tổng $11$ nên đáp án là `YES`.

## Ràng buộc

- $1 \le K \le N \le 18$, $1 \le a_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
