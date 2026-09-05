# Chuyến tàu vượt đèo

## Bối cảnh

Một đoàn tàu đồ chơi chạy qua $N$ ngọn đèo, ngọn thứ $i$ cao $A_i$ mét. Học sinh lái tàu reo lên mỗi khi tàu chinh phục một ngọn đèo cao hơn tất cả các ngọn đèo đã đi qua trước đó (ngọn đầu tiên luôn được reo một lần). Hãy đếm xem nhỏ reo lên tất cả bao nhiêu lần.

## Nhiệm vụ

Cho dãy $N$ số. Hãy đếm số lần phần tử lớn hơn tất cả các phần tử đứng trước nó.

## Input

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên ($|A_i| \le 10^9$).

## Output

In ra một số nguyên duy nhất là số lần reo.

## Sample 1

### Input

```text
6
1 3 5 2 4 7
```

### Output

```text
4
```

### Giải thích

Các kỷ lục mới là 1, 3, 5 rồi 7, tổng cộng 4 lần reo.

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le N \le 1000$.

* Subtask 2 (50% số điểm): $1000 < N \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
