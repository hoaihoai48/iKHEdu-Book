# Mật Khẩu Bị Ẩn

## Bối cảnh

Bé Bo đặt mật khẩu cho nhật ký điện tử của mình bằng một chuỗi gồm chữ cái và chữ số, ví dụ như `Abc123x`. Để kiểm tra độ mạnh, bé muốn biết mật khẩu của mình chứa bao nhiêu ký tự là chữ số. Em hãy giúp bé Bo đếm nhé!

## Nhiệm vụ

Cho chuỗi $S$. Hãy đếm xem có bao nhiêu ký tự trong $S$ là chữ số từ `0` đến `9`.

## Input

Một dòng chứa chuỗi $S$ ($1 \le |S| \le 10^5$, gồm chữ cái, chữ số và khoảng trắng).

## Output

In ra một số nguyên duy nhất là số lượng chữ số.

## Sample 1

### Input

```text
Abc123x
```

### Output

```text
3
```

### Giải thích

Trong chuỗi `Abc123x` có 3 ký tự là chữ số: `1`, `2` và `3`.

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le |S| \le 100$.

* Subtask 2 (50% số điểm): $100 < |S| \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
