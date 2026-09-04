# Đếm Số Lượng Đoạn Con Có Tổng Không Quá S

## Bối cảnh
Tại một trạm cân hàng hóa thông minh, băng chuyền chuyển qua N gói bưu kiện liên tiếp có trọng lượng không âm A1, A2, ..., An. Xe nâng tự động nhận nhiệm vụ bốc xếp các kiện hàng liên tiếp nhau sao cho tổng tải trọng bốc một lần không vượt quá định mức S. Bộ điều khiển cần tính toán có bao nhiêu phương án chọn đoạn bưu kiện liên tiếp thỏa mãn tải trọng cho phép.

## Nhiệm vụ
Cho mảng gồm N số nguyên không âm A1, A2, ..., An và số nguyên S. Hãy đếm số lượng đoạn con liên tiếp có tổng không vượt quá S.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($1 \le N \le 10^5, 0 \le S \le 10^{14}$).
- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
4 3
1 2 1 4
```
### Output
```text
4
```
### Giải thích
Các đoạn con liên tiếp có tổng <= 3 là: [1] (tổng 1), [2] (tổng 2), [1] (ở vị trí 3, tổng 1), và [1, 2] (tổng 3). Tổng cộng có 4 đoạn con thỏa mãn.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, S \le 10^{14}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
