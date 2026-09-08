# Next Greater Element Trên Mảng Vòng Tròn

## Bối cảnh
Một vòng đu quay gồm $N$ cabin được đánh số theo vòng tròn từ $1$ đến $N$, cabin thứ $N$ lại kết nối liền kề với cabin số $1$. Cabin thứ $i$ có chiều cao $A_i$. Khi đứng tại cabin $i$ và nhìn theo chiều kim đồng hồ quanh vòng tròn, hãy tìm giá trị của cabin đầu tiên có chiều cao lớn hơn cabin $i$. Nếu đi hết một vòng tròn mà không có cabin nào cao hơn, ghi nhận `-1`.

## Nhiệm vụ
Cho mảng tròn $A$ gồm $N$ phần tử. Với mỗi phần tử, hãy tìm phần tử lớn hơn đầu tiên tiếp theo trên mảng vòng tròn. Nếu không có, in ra `-1`.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N$ số nguyên tương ứng, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
3
1 2 1
```
### Output
```text
2 -1 2
```

### Giải thích
Với mảng tròn gồm 3 phần tử $[1, 2, 1]$:

- Phần tử 1 (đầu): Nhìn tiếp theo gặp số 2 lớn hơn 1 $\to$ in ra 2.
- Phần tử 2 (giữa): Nhìn tiếp theo gặp 1, rồi vòng lại đầu gặp 1, không có số nào lớn hơn 2 $\to$ in ra -1.
- Phần tử 1 (cuối): Vòng lại đầu mảng gặp 1, tiếp tục gặp 2 lớn hơn 1 $\to$ in ra 2.
Kết quả in ra: 2 -1 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
