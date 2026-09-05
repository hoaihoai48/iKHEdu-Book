# Bất biến chia kẹo và phục hồi số bị chia

## Bối cảnh
Nam đem một số kẹo bí mật chia cho $B$ bạn thì mỗi bạn được $Q$ chiếc kẹo và Nam còn thừa lại $R$ chiếc kẹo.

## Nhiệm vụ
Nhập 3 số nguyên $B, Q, R$ trên cùng 1 dòng ($B > R \ge 0$, $Q \ge 0$). Hãy tìm lại tổng số kẹo ban đầu mà Nam có.

## Input
Một dòng chứa 3 số nguyên $B, Q, R$ ($1 \le B, Q \le 10^6$, $0 \le R < B$).

## Output
In ra số kẹo ban đầu.

## Sample 1
### Input
```text
6 8 3
```
### Output
```text
51
```
### Giải thích
Áp dụng định lý bất biến phép chia: $A = B \times Q + R = 6 \times 8 + 3 = 51$.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
