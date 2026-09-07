# Đếm cặp nghịch thế bằng Fenwick Tree

## Bối cảnh

Giải chạy marathon điện tử ghi lại thành tích của N vận động viên theo thứ tự về đích để xếp hạng khen thưởng cuối mùa giải. Ban trọng tài muốn đếm có bao nhiêu cặp mà người về trước lại có thành tích kém hơn người về sau nhằm phát hiện bất thường trong khâu bấm giờ chip điện tử. Cây Fenwick kết hợp nén tọa độ được dùng để đếm số cặp nghịch thế trong thời gian N log N thay vì duyệt toàn bộ từng cặp.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$. Hãy lập trình đếm số cặp nghịch thế, tức số cặp $(i,j)$ với $i < j$ mà $a_i > a_j$, rồi in ra kết quả.

## Input

- Dòng 1: số nguyên $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).

## Output

- In ra một dòng duy nhất là số cặp nghịch thế (dùng số nguyên 64-bit).

## Sample 1

### Input

```text
5
2 3 8 6 1
```

### Output

```text
5```

### Giải thích

- Mảng $2\ 3\ 8\ 6\ 1$: xét từng phần tử bên trái lớn hơn phần tử bên phải.
- Các cặp thỏa mãn là $(2,1), (3,1), (8,6), (8,1), (6,1)$, tổng $5$ cặp.
- Chương trình in ra $5$.

## Ràng buộc

- $1 \le N \le 2 \cdot 10^5$; $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
