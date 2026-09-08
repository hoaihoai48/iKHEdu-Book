# Tìm Phần Tử Nhỏ Nhất Lớn Hơn Hoặc Bằng X

## Bối cảnh
Một sàn giao dịch hàng hóa trực tuyến duy trì một kho các lệnh bán với mức giá niêm yết $A_1, A_2, \dots, A_N$. Khi một nhà đầu tư gửi lệnh mua với mức trần giá tối đa là $X$, hệ thống giao dịch tự động cần nhanh chóng tìm ra lệnh bán có mức giá nhỏ nhất thỏa mãn điều kiện lớn hơn hoặc bằng $X$ để khớp lệnh.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn, mỗi truy vấn gồm một số nguyên $X$. Hãy lập trình tìm phần tử nhỏ nhất trong mảng lớn hơn hoặc bằng $X$. Nếu không có phần tử nào thỏa mãn, in ra `-1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên $X$ ($-10^9 \le X \le 10^9$).

## Output
- Với mỗi truy vấn, in ra giá trị nhỏ nhất lớn hơn hoặc bằng $X$, hoặc `-1` nếu không có.

## Sample 1
### Input
```text
5 3
10 20 30 40 50
25
50
60
```
### Output
```text
30
50
-1
```

### Giải thích
Với mảng $[1, 4, 6, 8, 10]$ và các truy vấn $X$:

- Truy vấn $X = 5$: Phần tử nhỏ nhất trong mảng $\ge 5$ là 6.
- Truy vấn $X = 11$: Không có phần tử nào trong mảng $\ge 11$, in ra -1.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, X \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
