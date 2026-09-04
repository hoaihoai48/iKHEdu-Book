# Đếm Kẹo Chẵn Lẻ

## Bối cảnh

Liên hoan cuối năm, cô giáo mua $N$ gói kẹo, mỗi gói có $A_i$ viên kẹo. Cô muốn chia các gói kẹo thành hai mâm: mâm gói chẵn (số kẹo là số chẵn) và mâm gói lẻ (số kẹo là số lẻ). Em hãy giúp cô đếm xem mỗi mâm có bao nhiêu gói nhé!

## Nhiệm vụ

Cho $N$ số nguyên. Hãy đếm số lượng số chẵn và số lượng số lẻ, in trên một dòng.

## Input

Dòng 1: số nguyên $N$ ($1 \le N \le 10^5$). Dòng 2: $N$ số nguyên ($0 \le A_i \le 10^9$).

## Output

In ra hai số trên một dòng: số lượng số chẵn trước, số lượng số lẻ sau.

## Sample 1

### Input

```text
6
1 2 3 4 5 6
```

### Output

```text
3 3
```

### Giải thích

Các số chẵn là 2, 4, 6 (3 gói). Các số lẻ là 1, 3, 5 (3 gói).

## Ràng buộc

Subtask 1 (50% số điểm): $1 \le N \le 1000$.

* Subtask 2 (50% số điểm): $1000 < N \le 10^5$.

* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
