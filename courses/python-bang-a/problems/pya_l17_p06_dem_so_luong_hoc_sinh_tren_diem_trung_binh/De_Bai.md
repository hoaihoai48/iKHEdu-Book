# Đếm số lượng học sinh trên điểm trung bình


## Bối cảnh

So sánh từng phần tử với giá trị trung bình của cả tập hợp giúp đánh giá độ phân tán và chất lượng của các chỉ số thành phần.

## Nhiệm vụ

Cho điểm thi của $N$ học sinh. Hãy đếm xem có bao nhiêu bạn học sinh có điểm số lớn hơn hoặc bằng điểm trung bình cộng của cả lớp.
## Input

 * Dòng 1: Số nguyên $N$ ($1 \le N \le 10^5$).
 * Dòng 2: $N$ số thực.
## Output

Số lượng học sinh đạt điểm $\ge$ điểm trung bình.
## Sample 1

### Input
```text
4
8 6 10 4
```
### Output
```text
2
```
### Giải thích

Điểm TB: $(8+6+10+4)/4 = 7.0$. Các bạn có điểm $\ge 7$ là 8 và 10 (có 2 bạn).


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
