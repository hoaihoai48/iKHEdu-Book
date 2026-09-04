# Tìm Max Đoạn & Đếm Số Lần Xuất Hiện

## Bối cảnh
Một hệ thống đánh giá hiệu năng máy chủ theo dõi điểm tải đỉnh của $N$ máy tính. Ban giám sát muốn biết trong một khoảng thời gian từ mốc $L$ đến $R$, giá trị tải lớn nhất (Max) đạt được là bao nhiêu và có bao nhiêu máy tính đạt đúng mức tải đỉnh này.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn, mỗi truy vấn gồm hai chỉ số $L, R$. Hãy tìm giá trị lớn nhất và số lần xuất hiện của giá trị lớn nhất đó trong đoạn $[L, R]$.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $L$ và $R$ ($1 \le L \le R \le N$).

## Output
- Với mỗi truy vấn, in ra trên một dòng hai số nguyên: giá trị lớn nhất và số lần xuất hiện của nó, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5 3
2 5 3 5 1
2 1 5
1 3 5
2 1 5
```
### Output
```text
5 2
5 3
```

### Giải thích
Với mảng $[3, 5, 2, 5, 5, 1]$ và truy vấn đoạn từ vị trí 1 đến 5:
Giá trị lớn nhất trong đoạn là 5, và số 5 xuất hiện đúng 3 lần tại các vị trí 2, 4, 5. Kết quả in ra: 5 3.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
