# Phân chia tập hợp thành hai nửa có tổng bằng nhau

## Bối cảnh
Hai anh em được chia gia tài gồm nhiều món đồ có giá trị khác nhau. Cả nhà muốn việc chia chác thật công bằng: mỗi người nhận một nhóm đồ có tổng giá trị bằng nhau chính xác.

Hãy giúp cả nhà xem liệu có cách chia như vậy hay không.

## Nhiệm vụ

Cho dãy gồm $n$ số nguyên. Hãy lập trình kiểm tra xem có thể chia các phần tử thành hai nhóm có tổng bằng nhau hay không; in `YES` nếu được và `NO` nếu không.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 40$) — số phần tử.
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là `YES` nếu tồn tại cách chia thành hai nhóm có tổng bằng nhau, ngược lại in `NO`.

## Sample 1
### Input
```text
4
1 5 11 5
```
### Output
```text
YES
```
### Giải thích

Tổng cả dãy là $1 + 5 + 11 + 5 = 22$ nên mỗi nhóm phải tổng $11$. Nhóm $\{11\}$ một mình đã đủ $11$, nhóm còn lại $\{1, 5, 5\}$ cũng tổng $11$ — chia được nên đáp án là `YES`.

## Ràng buộc

- $1 \le n \le 40$, $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
