# Tam Giác Vuông Hay Không?


## Bối cảnh

Theo định lý Pytago, tam giác có 3 cạnh $a, b, c$ là tam giác vuông nếu bình phương một cạnh bằng tổng bình phương hai cạnh còn lại ($a^2 + b^2 = c^2$ hoặc $a^2 + c^2 = b^2$ hoặc $b^2 + c^2 = a^2$).
## Nhiệm vụ

Cho 3 số dương $a, b, c$. Nếu chúng tạo thành một tam giác vuông thì in `VUONG`, ngược lại in `KHONG VUONG`.
## Input

Ba số nguyên $a, b, c$ ($1 \le a, b, c \le 10^4$).
## Output

`VUONG` hoặc `KHONG VUONG`.
## Sample 1

### Input
```text
3
4
5
```
### Output
```text
VUONG
```
### Giải thích

$3^2 + 4^2 = 9 + 16 = 25 = 5^2$.


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
