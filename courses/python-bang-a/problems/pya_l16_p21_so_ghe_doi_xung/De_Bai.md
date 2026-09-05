# Số ghế đối xứng

## Bối cảnh

Rạp xiếc trong thành phố có một hàng ghế đặc biệt: những ghế mang số đối xứng (đọc từ trái sang phải hay từ phải sang trái đều giống nhau, như 121 hay 44) được gọi là ghế vàng và ngồi xem rất rõ. Mi mua được vé ghế số $N$ và muốn biết ghế của mình có phải ghế vàng không.

## Nhiệm vụ

Hãy kiểm tra số $N$ có phải số đối xứng không. In `YES` nếu đúng, ngược lại in `NO`.

## Input

Một số tự nhiên $N$ ($1 \le N \le 10^{18}$).

## Output

In ra `YES` hoặc `NO`.

## Sample 1

### Input

```text
121
```

### Output

```text
YES
```

### Giải thích

Số 121 đọc xuôi là 121, đọc ngược cũng là 121 nên đây là ghế vàng.

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le N \le 9999$.

* Subtask 2 (50% số điểm): $10000 \le N \le 10^{18}$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
