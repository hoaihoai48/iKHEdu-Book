# Đoạn Con Dài Nhất Có Tổng Không Quá S

## Bối cảnh
Tại một trạm sạc xe điện nhanh trên cao tốc, các xe xếp hàng chờ sạc với nhu cầu tiêu thụ điện năng lần lượt là A1, A2, ..., An (kWh). Nguồn pin tích năng lượng mặt trời của trạm tại thời điểm hiện tại chỉ còn lại dung lượng tối đa S. Trạm muốn phục vụ một đợt xe liên tiếp dài nhất sao cho tổng năng lượng cung cấp không vượt quá giới hạn S để không làm sập nguồn.

## Nhiệm vụ
Cho dãy gồm N số nguyên không âm và một số nguyên dương S. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có tổng không vượt quá S.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $S$ ($1 \le N \le 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: Chứa $N$ số nguyên không âm $A_1, A_2, \dots, A_N$ ($0 \le A_i \le 10^9$).

## Output
- In ra độ dài lớn nhất của đoạn con thỏa mãn.

## Sample 1
### Input
```text
5 10
1 2 3 4 5
```
### Output
```text
4
```
### Giải thích
Đoạn con [1, 2, 3, 4] có tổng 1 + 2 + 3 + 4 = 10 <= 10 và có độ dài bằng 4. Nếu xét cả 5 phần tử thì tổng là 15 > 10. Do đó độ dài lớn nhất là 4.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, S \le 10^{14}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
