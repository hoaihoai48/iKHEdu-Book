# Tổng chữ số lớn nhất

## Bối cảnh

Trong giờ ra chơi, các bạn thi nhau khoe số báo danh của mình. Bạn nào có tổng các chữ số lớn nhất sẽ được làm lớp trưởng ngày mai. Có $N$ bạn tham gia, mỗi bạn có một số báo danh. Nếu hai bạn có tổng chữ số bằng nhau thì bạn có số báo danh nhỏ hơn sẽ thắng.

## Nhiệm vụ

Hãy tìm số báo danh của bạn thắng cuộc.

## Input

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số tự nhiên ($0 \le A_i \le 10^{18}$).

## Output

In ra số báo danh thắng cuộc.

## Sample 1

### Input

```text
5
12 99 45 100 38
```

### Output

```text
99
```

### Giải thích

Tổng chữ số của 12 là 3, của 99 là 18, của 45 là 9, của 100 là 1, của 38 là 11. Tổng lớn nhất là 18 của số 99.

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le N \le 1000$, $A_i \le 9999$.

* Subtask 2 (50% số điểm): $1000 < N \le 10^5$, $A_i \le 10^{18}$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
