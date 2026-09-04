# Vé Số May Mắn

## Bối cảnh

Hội chợ trường em tổ chức trò chơi quay số trúng thưởng. Mỗi bạn nhỏ được phát một tấm vé in một số tự nhiên $N$. Ban tổ chức gọi đó là vé may mắn nếu tổng các chữ số của $N$ chia hết cho $7$. Bé Tí cầm vé số $1234$ trên tay, hồi hộp không biết mình có trúng thưởng không.

## Nhiệm vụ

Hãy kiểm tra xem tấm vé số $N$ có phải là vé may mắn không. In `YES` nếu đúng, ngược lại in `NO`.

## Input

Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).

## Output

In ra `YES` hoặc `NO`.

## Sample 1

### Input

```text
1234
```

### Output

```text
NO
```

### Giải thích

Tổng các chữ số là $1 + 2 + 3 + 4 = 10$. Vì 10 không chia hết cho 7 nên đáp án là `NO`. (Ví dụ vé số $16$ có tổng là 7 nên đáp án là `YES`.)

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le N \le 9999$ (tối đa 4 chữ số).

* Subtask 2 (50% số điểm): $10000 \le N \le 10^{18}$ (tối đa 19 chữ số).

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
