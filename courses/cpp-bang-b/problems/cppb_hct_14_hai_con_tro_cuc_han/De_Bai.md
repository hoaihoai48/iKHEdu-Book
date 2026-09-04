# Cặp Số Tối Ưu Với Chênh Lệch Cực Hạn

## Bối cảnh
Tại một trạm quan trắc địa chấn liên vùng, hai trạm cảm biến đặt ở hai thung lũng ghi nhận N xung địa chấn dãy A và M xung địa chấn dãy B (với biên độ có thể lên tới 10^18). Để đồng bộ pha tín hiệu giữa hai trạm, các nhà địa chấn học cần tìm một xung địa chấn Ai từ trạm A và một xung địa chấn Bj từ trạm B sao cho độ lệch biên độ tuyệt đối giữa chúng |Ai - Bj| là nhỏ nhất có thể.

## Nhiệm vụ
Cho 2 dãy số nguyên A gồm N phần tử và B gồm M phần tử. Hãy tìm một phần tử A[i] và một phần tử B[j] sao cho độ chênh lệch |A[i] - B[j]| là nhỏ nhất có thể.

## Input
- Dòng 1: 2 số nguyên $N$ và $M$ ($1 \le N, M \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$).
- Dòng 3: $M$ số nguyên $B_1, B_2, \dots, B_M$ ($-10^{18} \le B_j \le 10^{18}$).

## Output
- In ra một số nguyên duy nhất là giá trị chênh lệch nhỏ nhất $|A_i - B_j|$.

## Sample 1
### Input
```text
3 3
1 5 10
2 8 14
```
### Output
```text
1
```
### Giải thích
Dãy A = [1, 5, 10] và dãy B = [2, 8, 14]. So sánh các cặp phần tử: chọn A[0] = 1 và B[0] = 2 cho độ chênh lệch |1 - 2| = 1. Đây là mức chênh lệch nhỏ nhất có thể đạt được giữa hai dãy.

## Ràng buộc
- $100\%$ số test có $N, M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
