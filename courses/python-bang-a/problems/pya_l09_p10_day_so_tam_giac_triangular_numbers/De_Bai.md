# Dãy Số Tam Giác (Triangular Numbers)


## Bối cảnh

Người Hy Lạp cổ đại thường xếp các viên sỏi thành hình tam giác đều:
  * Tầng 1: 1 viên
  * Tầng 2: 1 + 2 = 3 viên
  * Tầng 3: 1 + 2 + 3 = 6 viên
  * Tầng 4: 1 + 2 + 3 + 4 = 10 viên
## Nhiệm vụ

Cho số tự nhiên $K$. Hãy kiểm tra xem $K$ có phải là một "Số tam giác" hay không (nghĩa là có tồn tại số nguyên dương $N$ sao cho $\frac{N(N+1)}{2} = K$)? Nếu có, in ra `YES` và số $N$, ngược lại in `NO`.
## Input

Một số nguyên $K$ ($1 \le K \le 10^9$).
## Output

`YES <N>` hoặc `NO`.
## Sample 1

### Input
```text
10
```
### Output
```text
YES 4
```
## Sample 2

### Input
```text
8
```
### Output
```text
NO
```


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
