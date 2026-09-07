# Đoạn con ngắn nhất có tổng $\ge s$

## Bối cảnh

Huấn luyện viên ghi lại số bước chạy của vận động viên mỗi ngày. Anh muốn tìm chuỗi ngày liên tiếp ngắn nhất mà tổng số bước đạt ít nhất mức $S$ để khen thưởng sự bứt phá.

Anh lật lại nhật ký luyện tập, mở rộng rồi thu hẹp từng cửa sổ ngày để tìm chuỗi ngắn nhất.

## Nhiệm vụ

Cho dãy số và ngưỡng $S$. Hãy lập trình tìm độ dài đoạn con liên tiếp ngắn nhất có tổng không nhỏ hơn $S$.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, S$ ($1 \le n \le 10^5$, $1 \le S \le 10^{14}$) — độ dài dãy và ngưỡng tổng.
- Dòng thứ hai chứa $n$ số nguyên dương $a_i$ ($1 \le a_i \le 10^9$).

## Output

- In ra một dòng duy nhất là độ dài của đoạn con liên tiếp ngắn nhất có tổng ít nhất $S$; in `-1` nếu không tồn tại đoạn con nào đạt ngưỡng.

## Sample 1
### Input
```text
5 11
1 2 3 4 5
```
### Output
```text
3
```
### Giải thích

Thử độ dài $2$: các tổng lớn nhất là $4 + 5 = 9 < 11$ nên không đoạn nào đạt. Thử độ dài $3$: đoạn $[3, 4, 5]$ có tổng $12 \ge 11$ — đạt yêu cầu. Vì độ dài $1$ và $2$ đều thất bại nên $3$ là ngắn nhất.

## Ràng buộc

- $1 \le n \le 10^5$, $1 \le S \le 10^{14}$, mọi $a_i$ đều dương.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
