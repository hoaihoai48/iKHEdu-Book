# Heo Đất Tiết Kiệm

## Bối cảnh

Bé Na có một chú heo đất màu hồng rất xinh. Mỗi ngày, bé bỏ vào heo $A$ đồng tiền ăn sáng để dành. Đặc biệt, cứ vào các ngày chẵn (ngày thứ 2, 4, 6, ...) bé còn được mẹ thưởng thêm $B$ đồng vì chăm ngoan. Sau $N$ ngày, bé Na hồi hộp muốn biết trong heo có tất cả bao nhiêu tiền.

## Nhiệm vụ

Hãy tính tổng số tiền trong heo đất sau $N$ ngày.

## Input

Một dòng gồm ba số nguyên $N$, $A$, $B$ ($1 \le N \le 10^6$, $1 \le A, B \le 10^4$).

## Output

In ra một số nguyên duy nhất là tổng số tiền.

## Sample 1

### Input

```text
5 10 3
```

### Output

```text
56
```

### Giải thích

5 ngày, mỗi ngày 10 đồng được 50 đồng. Các ngày chẵn là ngày 2 và ngày 4, được thưởng thêm $2 \times 3 = 6$ đồng. Tổng cộng $50 + 6 = 56$ đồng.

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le N \le 1000$. Vòng lặp từng ngày vẫn chạy kịp.

* Subtask 2 (50% số điểm): $1000 < N \le 10^6$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
