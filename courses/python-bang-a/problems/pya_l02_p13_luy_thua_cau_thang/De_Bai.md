# Lũy thừa cầu thang

## Bối cảnh

Bạn Thỏ Nâu rất thích xếp các khối gỗ thành một chiếc cầu thang toán học. Tầng đầu tiên cần $a$ khối gỗ, mỗi tầng tiếp theo lại gấp $a$ lần số khối của tầng trước đó. Thỏ Nâu đếm được chiếc cầu thang của mình có tất cả $n$ tầng. Hãy giúp bạn Thỏ tính xem tầng cao nhất có bao nhiêu khối gỗ.

## Nhiệm vụ

Cho hai số nguyên $a$ và $n$, em hãy tính giá trị lũy thừa $a^n$.

## Input

Gồm 2 dòng, mỗi dòng một số nguyên: dòng đầu là cơ số $a$, dòng sau là số mũ $n$ ($1 \le a \le 10$, $0 \le n \le 10$).

## Output

In ra một số nguyên duy nhất là giá trị của $a^n$.

## Sample 1

### Input
```text
3
4
```
### Output
```text
81
```
### Giải thích

$3^4 = 3 \times 3 \times 3 \times 3 = 81$. Tầng cao nhất của cầu thang có 81 khối gỗ.

## Ràng buộc

* **Giới hạn dữ liệu:** $1 \le a \le 10$, $0 \le n \le 10$.
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
