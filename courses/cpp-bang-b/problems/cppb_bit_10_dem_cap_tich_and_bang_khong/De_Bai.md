# Đếm Cặp Có Tích Bit AND Bằng 0

## Bối cảnh
Trong phân bổ kênh truyền vô tuyến số, hai thiết bị được coi là không xung đột tần số nếu các dải tần biểu diễn dưới dạng mặt nạ bit của chúng không có chung bất kỳ kênh nào, nghĩa là tích bit AND của chúng bằng 0 (A[i] & A[j] == 0). Hãy đếm số lượng cặp thiết bị không xung đột.

## Nhiệm vụ
Cho dãy gồm N số nguyên không âm. Hãy đếm số lượng cặp chỉ số (i, j) với 1 <= i < j <= N thỏa mãn: A[i] & A[j] == 0.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i < 2^{16}$).

## Output
- In ra một số nguyên duy nhất là số lượng cặp thỏa mãn.

## Sample 1
### Input
```text
4
1 2 4 8
```
### Output
```text
6
```
### Giải thích
Các số 1 (0001_2), 2 (0010_2), 4 (0100_2), 8 (1000_2) đều có các bit 1 ở vị trí hoàn toàn khác nhau. Do đó tích bit AND giữa hai số bất kỳ đều bằng 0. Số cặp là C(4, 2) = 6 cặp.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, A_i < 2^{16}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
