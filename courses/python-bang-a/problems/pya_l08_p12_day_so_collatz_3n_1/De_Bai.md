# Dãy Số Collatz (3n + 1)


## Bối cảnh

Giả thuyết Collatz là một bài toán toán học kỳ bí: Bắt đầu từ số tự nhiên $N > 0$:
  * Nếu $N$ là số chẵn: chia đôi $N = N // 2$.
  * Nếu $N$ là số lẻ: nhân ba cộng một $N = 3 \times N + 1$.
  * Lặp lại quy trình trên cho đến khi số $N$ biến thành số $1$ thì dừng lại!
## Nhiệm vụ

Nhập vào số tự nhiên $N$. Hãy in ra số bước biến đổi để $N$ trở thành 1.
## Input

Một số tự nhiên $N$ ($1 \le N \le 10^5$).
## Output

Số bước biến đổi.
## Sample 1

### Input
```text
6
```
### Output
```text
8
```
### Giải thích

Dãy biến đổi: $6 \to 3 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1$ (qua 8 bước biến đổi).

## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
