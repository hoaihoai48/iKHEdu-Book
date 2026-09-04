# Đếm Số Lượng Đoạn Con Có Tổng Đúng Bằng S

## Bối cảnh
Một người thợ kim hoàn cắt gọt thanh vàng nguyên khối được chia thành N đoạn nhỏ liên tiếp với trọng lượng vàng nguyên chất mỗi đoạn là các số nguyên dương A1, A2, ..., An. Khách hàng đặt mua một chuỗi các đoạn vàng liền kề nhau sao cho tổng trọng lượng của chuỗi đúng bằng S chỉ vàng. Hãy tính số lượng cách chọn đoạn liền kề đáp ứng đúng yêu cầu của khách.

## Nhiệm vụ
Cho mảng gồm N số nguyên dương A1, A2, ..., An (Ai > 0) và số nguyên dương S. Hãy đếm số lượng đoạn con liên tiếp có tổng đúng bằng S.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra số lượng đoạn con có tổng đúng bằng S.

## Sample 1
### Input
```text
5 5
1 2 3 2 1
```
### Output
```text
2
```
### Giải thích
Các đoạn con liên tiếp có tổng đúng bằng 5 là: đoạn [2, 3] (2 + 3 = 5) và đoạn [3, 2] (3 + 2 = 5). Tổng cộng có đúng 2 đoạn con thỏa mãn.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, S \le 10^{14}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
