# Số Hạng Dãy Cấp Số Cộng


## Nhiệm vụ

Cho một dãy số cách đều có số đầu tiên là $u_1$ và khoảng cách giữa 2 số liền kề là $d$. Cho số nguyên dương $N$. Hãy tìm số hạng thứ $N$ của dãy số.
## Input

Ba số nguyên $u_1, d, N$ ($1 \le u_1, d, N \le 10^6$).
## Output

Một số nguyên là số hạng thứ $N$.
## Sample 1

### Input
```text
3 4 5
```
### Output
```text
19
```
### Giải thích

Dãy số là: 3, 7, 11, 15, 19. Số thứ 5 là 19.
* **Công thức toán học:** $u_N = u_1 + (N - 1) \times d$.


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
