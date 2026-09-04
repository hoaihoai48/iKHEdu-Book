# Truy Vấn Ước Chung Lớn Nhất Đoạn (Range GCD)

## Bối cảnh
Trong một hệ thống mã hóa dữ liệu theo khối, mỗi khối dữ liệu có một mã khóa số nguyên $A_i$. Để giải mã một chuỗi các khối liên tiếp từ $L$ đến $R$, thiết bị giải mã cần tính toán ước chung lớn nhất (GCD) của tất cả các khóa trong đoạn: $\gcd(A_L, A_{L+1}, \dots, A_R)$. Hệ thống cũng hỗ trợ cập nhật lại mã khóa tại từng khối.

## Nhiệm vụ
Cho mảng $A$ và $Q$ thao tác thuộc hai dạng: `1 pos val` (gán $A[pos] = val$) và `2 L R` (tìm GCD của các phần tử trong đoạn $[L, R]$). Hãy in ra kết quả cho các thao tác loại 2.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo chứa các thao tác mô tả như trên.

## Output
- Với mỗi thao tác loại 2, in ra giá trị GCD của đoạn trên một dòng.

## Sample 1
### Input
```text
5 3
2 4 6 8 10
2 1 3
1 2 12
2 1 3
```
### Output
```text
2
2
```

### Giải thích
Với mảng $[6, 12, 18, 24]$:
- Truy vấn GCD đoạn từ 1 đến 3: $\gcd(6, 12, 18) = 6$.
- Cập nhật vị trí 1 thành 4: mảng thành $[4, 12, 18, 24]$.
- Truy vấn lại GCD đoạn từ 1 đến 3: $\gcd(4, 12, 18) = 2$.

## Ràng buộc
- $100\%$ số test có $1 \le N, Q \le 10^5, 1 \le A_i, val \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
