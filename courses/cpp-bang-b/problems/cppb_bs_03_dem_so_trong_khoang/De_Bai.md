# Đếm Số Phần Tử Trong Đoạn [L, R]

## Bối cảnh
Một cơ quan khí tượng tổng hợp N chỉ số nhiệt độ đo được tại các trạm quan trắc (chưa sắp xếp). Các nhà nghiên cứu khí hậu gửi Q câu hỏi truy vấn độc lập, mỗi câu hỏi cần biết có bao nhiêu trạm quan trắc ghi nhận nhiệt độ nằm trong khoảng từ ngưỡng L đến ngưỡng R.

## Nhiệm vụ
Cho mảng gồm N số nguyên. Với mỗi câu hỏi gồm khoảng [L, R] (L <= R), hãy đếm số lượng phần tử của mảng có giá trị nằm trong đoạn [L, R] (L <= A[i] <= R).

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L$ và $R$ ($-10^9 \le L \le R \le 10^9$).

## Output
- In ra $Q$ dòng, mỗi dòng là số lượng phần tử thỏa mãn.

## Sample 1
### Input
```text
5 3
5 1 8 3 2
2 5
1 1
6 7
```
### Output
```text
3
1
0
```
### Giải thích
Sắp xếp mảng: [1, 2, 3, 5, 8].
- Đoạn [2, 5]: có 3 phần tử {2, 3, 5} -> in 3.
- Đoạn [1, 1]: có 1 phần tử {1} -> in 1.
- Đoạn [6, 7]: không có phần tử nào -> in 0.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
