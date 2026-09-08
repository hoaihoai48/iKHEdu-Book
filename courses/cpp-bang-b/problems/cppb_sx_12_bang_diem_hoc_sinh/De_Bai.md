# Bảng Điểm Học Sinh Đa Trường

## Bối cảnh
Tại kỳ thi Olympic Khoa học Trẻ liên trường, hội đồng chấm thi tổng hợp kết quả của $N$ thí sinh tham gia hai môn thi bắt buộc là Toán và Tin học. Mỗi thí sinh có một mã định danh $ID$ duy nhất, cùng điểm số môn Toán ($Math$) và điểm số môn Tin học ($Info$). Để công bố danh sách tuyên dương và xét học bổng, hội đồng thi cần xây dựng bảng xếp hạng chung toàn cuộc thi dựa trên nhiều tiêu chí chặt chẽ.

## Nhiệm vụ
Cho danh sách $N$ học sinh cùng điểm số của hai môn thi. Hãy sắp xếp danh sách học sinh theo các quy tắc ưu tiên sau:

1. Tổng điểm hai môn ($Math + Info$) giảm dần.
2. Nếu bằng tổng điểm, thí sinh có điểm môn Tin học ($Info$) cao hơn sẽ đứng trước.
3. Nếu vẫn bằng nhau cả về điểm Tin học, thí sinh có mã số định danh $ID$ nhỏ hơn sẽ đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$) — số lượng thí sinh.
- $N$ dòng tiếp theo: Mỗi dòng gồm 3 số nguyên $ID, Math, Info$ ($1 \le ID \le 10^9, 0 \le Math, Info \le 100$) lần lượt là mã số, điểm Toán và điểm Tin học của thí sinh.

## Output
- In ra danh sách học sinh sau khi đã sắp xếp thứ tự, mỗi học sinh trên một dòng gồm 3 số nguyên $ID, Math, Info$ cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
3
101 8 9
102 9 8
103 10 10
```
### Output
```text
103 10 10
101 8 9
102 9 8
```
### Giải thích
Thống kê điểm của 3 thí sinh:

- Thí sinh $103$: Điểm Toán = $10$, Điểm Tin = $10 \implies$ Tổng điểm = $20$.
- Thí sinh $101$: Điểm Toán = $8$, Điểm Tin = $9 \implies$ Tổng điểm = $17$.
- Thí sinh $102$: Điểm Toán = $9$, Điểm Tin = $8 \implies$ Tổng điểm = $17$.

Xếp hạng theo các tiêu chí:

- Thí sinh $103$ có tổng điểm cao nhất ($20$) nên đứng vị trí số 1.
- Giữa hai thí sinh $101$ và $102$ có cùng tổng điểm là $17$: xét tiêu chí phụ điểm Tin học, thí sinh $101$ có điểm Tin $9 > 8$ của thí sinh $102$, do đó thí sinh $101$ xếp trước thí sinh $102$.

Kết quả in ra đúng thứ tự: `103 10 10`, tiếp theo là `101 8 9`, và cuối cùng là `102 9 8`.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
