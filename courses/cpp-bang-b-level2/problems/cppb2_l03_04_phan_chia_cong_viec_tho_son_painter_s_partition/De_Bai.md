# Phân chia công việc thợ sơn (painter's partition)

## Bối cảnh

Đội thợ sơn nhận sơn một dãy đoạn tường liền kề, mỗi đoạn tốn một khoảng thời gian khác nhau. Anh đội trưởng cần chia dãy tường thành các phần liên tiếp để giao cho các thợ, sao cho người làm lâu nhất cũng xong sớm nhất có thể.

Mọi người cùng bàn cách chia sao cho công việc cân đối, không ai phải chờ ai quá lâu.

## Nhiệm vụ

Cho thời gian sơn từng đoạn tường và số thợ. Hãy lập trình tìm thời gian hoàn thành nhỏ nhất có thể của người làm lâu nhất khi chia công việc liên tiếp cho các thợ.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, k$ ($1 \le k \le n \le 10^5$) — số đoạn tường và số thợ sơn.
- Dòng thứ hai chứa $n$ số nguyên dương $a_i$ ($1 \le a_i \le 10^9$) là thời gian sơn từng đoạn (mỗi thợ sơn một số đoạn liên tiếp, mỗi đoạn đúng một thợ).

## Output

- In ra một dòng duy nhất là tổng thời gian lớn nhất của một thợ trong phương án chia việc tốt nhất (tổng thời gian hoàn thành cả công trình khi các thợ làm song song).

## Sample 1
### Input
```text
4 2
10 20 30 40
```
### Output
```text
60
```
### Giải thích

Thử đáp án $60$: thợ thứ nhất sơn $10 + 20 + 30 = 60$ (thêm đoạn $40$ nữa sẽ vượt), thợ thứ hai sơn nốt đoạn $40$ — vừa đủ $2$ thợ. Thử $59$: thợ thứ nhất chỉ sơn được $10 + 20 = 30$ (thêm $30$ nữa thành $60 > 59$), thợ thứ hai sơn $30$ rồi không gánh nổi đoạn $40$ ($30 + 40 > 59$) nên cần tới thợ thứ ba — không đủ người. Vậy đáp án là $60$.

## Ràng buộc

- $1 \le k \le n \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
