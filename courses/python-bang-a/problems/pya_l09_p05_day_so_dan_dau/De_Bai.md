# Dãy số đan dấu


## Bối cảnh

Thí sinh tạo ra dãy số với quy luật đặc biệt: số đầu tiên cho trước, các số tiếp theo tuân theo một công thức biến đổi nhất định. Hãy in $N$ số đầu tiên.

## Nhiệm vụ

Cho số nguyên dương $N$. Hãy tính tổng của dãy số đan dấu:
 $$S = 1 - 2 + 3 - 4 + 5 - 6 + \dots + (-1)^{N+1} N$$
## Input

Một số nguyên $N$ ($1 \le N \le 10^6$).
## Output

Giá trị của tổng $S$.
## Sample 1

### Input
```text
5
```
### Output
```text
3
```
### Giải thích

$1 - 2 + 3 - 4 + 5 = 3$.
## Sample 2

### Input
```text
6
```
### Output
```text
-3
```
### Giải thích

$1 - 2 + 3 - 4 + 5 - 6 = -3$.
