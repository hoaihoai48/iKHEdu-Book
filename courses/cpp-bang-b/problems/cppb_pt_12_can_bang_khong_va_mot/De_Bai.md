# Đoạn Con Cân Bằng Số Lượng 0 và 1

## Bối cảnh
Một hệ thống phân phối tải nhị phân gồm chuỗi N tác vụ chỉ mang nhãn 0 hoặc 1. Để máy chủ xử lý đạt trạng thái cân bằng tài nguyên hoàn hảo, bộ điều phối cần chọn ra một chuỗi tác vụ liên tiếp dài nhất có số lượng tác vụ nhãn 0 bằng đúng số lượng tác vụ nhãn 1.

## Nhiệm vụ
Cho mảng nhị phân gồm N phần tử chỉ chứa các số 0 và 1. Hãy tìm độ dài lớn nhất của một đoạn con liên tiếp có số lượng số 0 bằng số lượng số 1.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

## Output
- In ra độ dài lớn nhất tìm được, hoặc `0` nếu không có đoạn con nào thỏa mãn.

## Sample 1
### Input
```text
6
0 1 0 0 1 1
```
### Output
```text
6
```
### Giải thích
Toàn bộ mảng gồm 6 phần tử có 3 số 0 và 3 số 1 (số lượng số 0 bằng số lượng số 1). Do đó đoạn con cân bằng dài nhất có độ dài bằng 6.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
