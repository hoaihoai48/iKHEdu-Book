# Tìm Đoạn Con Có Trung Bình Lớn Nhất Độ Dài >= K

## Bối cảnh
Trong đánh giá hiệu quả chuỗi cung ứng, chuyên gia tài chính theo dõi chuỗi doanh thu N ngày A1, A2, ..., An. Một giai đoạn tăng trưởng bền vững bắt buộc phải kéo dài ít nhất K ngày liên tiếp. Chuyên gia muốn tìm xem giá trị doanh thu trung bình lớn nhất của một giai đoạn kéo dài tối thiểu K ngày có thể đạt tới mức nào.

## Nhiệm vụ
Cho dãy số nguyên gồm N phần tử và số nguyên K. Hãy tìm giá trị trung bình lớn nhất của một đoạn con có độ dài ít nhất K, làm tròn đến đúng 3 chữ số thập phân.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra giá trị trung bình lớn nhất tìm được với 3 chữ số sau dấu phẩy.

## Sample 1
### Input
```text
4 2
1 12 -5 -6
```
### Output
```text
6.500
```
### Giải thích
Đoạn con [1, 12] có độ dài 2 >= K = 2 có tổng 13 và trung bình là 13/2 = 6.500. Đây là giá trị trung bình lớn nhất của các đoạn con có độ dài >= 2.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, K \le N$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
