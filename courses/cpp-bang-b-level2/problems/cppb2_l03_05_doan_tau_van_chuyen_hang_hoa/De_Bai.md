# Đoàn tàu vận chuyển hàng hóa

## Bối cảnh

Ga hàng hóa có một đoàn tàu với sức chở giới hạn mỗi chuyến. Thủ kho cần xếp các kiện hàng nặng nhẹ khác nhau lên các chuyến tàu theo đúng thứ tự nhập kho, sao cho dùng ít chuyến nhất mà chuyến nào cũng không bị quá tải.

Anh thủ kho thử tính sức chở tối thiểu cần thiết để chở hết hàng trong số chuyến cho phép.

## Nhiệm vụ

Cho trọng lượng các kiện hàng theo thứ tự và sức chở của đoàn tàu. Hãy lập trình tìm sức chở tối thiểu (hoặc số chuyến tối thiểu) để vận chuyển hết hàng hóa.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, days$ ($1 \le days \le n \le 10^5$) — số kiện hàng và số ngày vận chuyển.
- Dòng thứ hai chứa $n$ số nguyên dương $w_i$ ($1 \le w_i \le 10^9$) là khối lượng từng kiện (xếp theo đúng thứ tự lên tàu, mỗi ngày chở các kiện liên tiếp).

## Output

- In ra một dòng duy nhất là trọng tải nhỏ nhất của tàu để chở hết hàng trong đúng $days$ ngày (mỗi ngày tổng khối lượng chở không vượt quá trọng tải).

## Sample 1
### Input
```text
5 3
1 2 3 4 5
```
### Output
```text
6
```
### Giải thích

Thử trọng tải $6$: ngày $1$ chở $1 + 2 + 3 = 6$ (thêm kiện $4$ sẽ vượt), ngày $2$ chở kiện $4$, ngày $3$ chở kiện $5$ — vừa đủ $3$ ngày. Thử trọng tải $5$: ngày $1$ chở $1 + 2$ (thêm $3$ thành $6 > 5$), ngày $2$ chở $3$, ngày $3$ chở $4$, còn kiện $5$ phải sang ngày $4$ — cần tới $4$ ngày. Vậy đáp án là $6$.

## Ràng buộc

- $1 \le days \le n \le 10^5$, $1 \le w_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
