# Tìm Phần Tử Nhỏ Nhất Lớn Hơn X

## Bối cảnh
Tại một sàn đấu giá kim cương trực tuyến, danh sách mức giá đề xuất của N món đồ đã được sắp xếp tăng dần. Một nhà sưu tầm đặt ra mức giá trần X và muốn hệ thống đề xuất món đồ tiếp theo có giá thấp nhất nhưng phải nghiêm ngặt cao hơn mức giá X để xem xét đấu giá tiếp.

## Nhiệm vụ
Cho mảng N số nguyên đã sắp xếp tăng dần. Với mỗi truy vấn X, hãy tìm phần tử nhỏ nhất trong mảng có giá trị nghiêm ngặt lớn hơn X. Nếu không có, in ra -1.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên tăng dần $A_1 \le A_2 \le \dots \le A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa một số nguyên $X$.

## Output
- In ra $Q$ dòng, mỗi dòng là giá trị phần tử tìm được hoặc `-1`.

## Sample 1
### Input
```text
5 3
2 3 5 6 8
4
2
8
```
### Output
```text
5
3
-1
```
### Giải thích
- Với X = 4: phần tử nhỏ nhất > 4 là 5.
- Với X = 2: phần tử nhỏ nhất > 2 là 3.
- Với X = 8: không có phần tử nào > 8 -> in -1.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
