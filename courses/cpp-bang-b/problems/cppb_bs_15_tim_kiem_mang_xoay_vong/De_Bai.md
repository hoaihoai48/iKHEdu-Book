# Tìm Kiếm Trên Mảng Sắp Xếp Bị Xoay Vòng (Rotated Array)

## Bối cảnh
Trong bộ nhớ vòng (ring buffer) của một hệ thống xử lý camera an ninh, danh sách N chỉ số thời gian ban đầu được sắp xếp tăng dần nhưng sau một số chu kỳ ghi đè đã bị xoay vòng tại một trục xoay k nào đó. Hệ thống nhận Q yêu cầu tra cứu mã mốc thời gian X xem nó nằm ở vị trí nào trong bộ nhớ.

## Nhiệm vụ
Cho mảng N số nguyên phân biệt bị xoay vòng tại một trục không xác định. Có Q truy vấn tìm vị trí xuất hiện (0-indexed) của số nguyên X. Nếu không tìm thấy, in ra -1.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên phân biệt bị xoay vòng.
- $Q$ dòng tiếp theo: Mỗi dòng chứa một số nguyên $X$.

## Output
- In ra $Q$ dòng, mỗi dòng là chỉ số (0-indexed) của $X$, hoặc `-1`.

## Sample 1
### Input
```text
7 3
4 5 6 7 0 1 2
0
3
5
```
### Output
```text
4
-1
1
```
### Giải thích
Mảng bị xoay vòng [4, 5, 6, 7, 0, 1, 2]:
- Số 0 ở vị trí chỉ số 4.
- Số 3 không tồn tại -> -1.
- Số 5 ở vị trí chỉ số 1.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
