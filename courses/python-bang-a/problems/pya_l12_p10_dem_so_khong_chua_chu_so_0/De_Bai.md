# Đếm số không chứa chữ số 0


## Bối cảnh

Trong thiết kế hệ thống hiển thị số không hỗ trợ ký tự 0, các số chỉ tạo bởi các chữ số từ 1 đến 9 được coi là số hợp lệ cần được thống kê chính xác.

## Nhiệm vụ

Cho số nguyên dương $N$. Hãy đếm xem từ 1 đến $N$ có bao nhiêu số mà trong cách ghi thập phân của nó **không chứa bất kỳ chữ số 0 nào**.
## Input

Một số nguyên $N$ ($1 \le N \le 10^6$).
## Output

Số lượng số thỏa mãn.
## Sample 1

### Input
```text
15
```
### Output
```text
14
```
### Giải thích

Từ 1 đến 15 chỉ có duy nhất số 10 chứa chữ số 0. Vậy có $15 - 1 = 14$ số.


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
