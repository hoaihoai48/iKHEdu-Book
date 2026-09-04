# Tổng Giá Trị Nhỏ Nhất Của Mọi Đoạn Con

## Bối cảnh
Cho mảng $A$ gồm $N$ số nguyên. Một đoạn con của mảng là một chuỗi các phần tử liên tiếp $A[L..R]$ ($1 \le L \le R \le N$). Với mỗi đoạn con, ta xác định giá trị nhỏ nhất của đoạn con đó là $\min(A[L..R])$. Ban toán học cần tính tổng của tất cả các giá trị nhỏ nhất này trên mọi đoạn con có thể tạo thành từ mảng.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tính tổng giá trị nhỏ nhất của tất cả các đoạn con, lấy dư cho $10^9 + 7$.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^5$).

## Output
- In ra trên một dòng duy nhất tổng tìm được theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
4
3 1 2 4
```
### Output
```text
17
```

### Giải thích
Với mảng gồm 4 phần tử $[3, 1, 2, 4]$:
Các đoạn con có giá trị nhỏ nhất tương ứng:
- Độ dài 1: [3] -> 3, [1] -> 1, [2] -> 2, [4] -> 4 (tổng = 10).
- Độ dài 2: [3,1] -> 1, [1,2] -> 1, [2,4] -> 2 (tổng = 4).
- Độ dài 3: [3,1,2] -> 1, [1,2,4] -> 1 (tổng = 2).
- Độ dài 4: [3,1,2,4] -> 1 (tổng = 1).
Tổng cộng toàn bộ là $10 + 4 + 2 + 1 = 17$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
