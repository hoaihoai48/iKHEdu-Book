# Tìm Vị Trí Xuất Hiện Đầu Tiên & Cuối Cùng

## Bối cảnh
Trong cơ sở dữ liệu phân tích tín hiệu âm thanh số, N mẫu tần số đã được sắp xếp tăng dần và có nhiều mẫu trùng lặp cùng tần số. Kỹ sư âm thanh gửi Q yêu cầu truy vấn giá trị tần số X, cần xác định chính xác vị trí xuất hiện đầu tiên và vị trí xuất hiện cuối cùng (1-indexed) của tần số đó trong cơ sở dữ liệu.

## Nhiệm vụ
Cho mảng N phần tử đã sắp xếp tăng dần. Với mỗi giá trị X trong Q truy vấn, hãy tìm vị trí xuất hiện đầu tiên và cuối cùng của X. Nếu X không có trong mảng, in ra `-1 -1`.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên tăng dần $A_1 \le A_2 \le \dots \le A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa một số nguyên $X$.

## Output
- In ra $Q$ dòng, mỗi dòng gồm 2 số nguyên là vị trí đầu và vị trí cuối (1-indexed), hoặc `-1 -1`.

## Sample 1
### Input
```text
7 3
1 2 2 2 3 4 5
2
3
6
```
### Output
```text
2 4
5 5
-1 -1
```
### Giải thích
- Số 2 xuất hiện từ vị trí 2 đến vị trí 4 -> in `2 4`.
- Số 3 chỉ xuất hiện tại vị trí 5 -> in `5 5`.
- Số 6 không có trong mảng -> in `-1 -1`.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
