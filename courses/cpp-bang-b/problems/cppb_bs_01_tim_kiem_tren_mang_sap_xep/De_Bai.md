# Tìm Kiếm Phần Tử Trên Mảng Đã Sắp Xếp

## Bối cảnh
Cho mảng số nguyên gồm $N$ phần tử đã được sắp xếp theo thứ tự tăng dần. Có $Q$ câu hỏi, mỗi câu hỏi cho một số nguyên $X$, yêu cầu kiểm tra xem số $X$ có xuất hiện trong mảng hay không.

## Nhiệm vụ
Hãy sử dụng thuật toán Tìm kiếm nhị phân (Binary Search) để trả lời mỗi truy vấn trong thời gian $\mathcal{O}(\log N)$.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: $N$ số nguyên đã sắp xếp tăng dần $A_1, A_2, \dots, A_N$ ($|A_i| \le 10^9$).
- Dòng 3: $Q$ số nguyên $X_1, X_2, \dots, X_Q$ ($|X_i| \le 10^9$).

## Output
- In ra $Q$ dòng, mỗi dòng in `YES` nếu phần tử tương ứng tồn tại trong mảng, ngược lại in `NO`.

## Sample 1
### Input
```text
5 3
1 3 5 7 9
3 4 9
```
### Output
```text
YES
NO
YES
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5, |A_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
