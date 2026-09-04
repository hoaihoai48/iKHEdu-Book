# Tính Tổng Dãy Số & Giai Thừa Bằng Đệ Quy

## Bối cảnh
Hai công thức toán học cơ bản nhất phản ánh tính chất đệ quy tự nhiên: tổng dãy số nguyên liên tiếp S(N) = S(N - 1) + N và giai thừa N! = (N - 1)! * N. Hãy cài đặt hai hàm đệ quy này để tính toán giá trị đồng thời.

## Nhiệm vụ
Cho số nguyên dương N (1 <= N <= 20). Hãy tính tổng S = 1 + 2 + ... + N và giai thừa N! bằng hàm đệ quy.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 20$).

## Output
- In ra 2 số nguyên cách nhau bởi khoảng trắng: tổng $S$ và giai thừa $N!$.

## Sample 1
### Input
```text
5
```
### Output
```text
15 120
```
### Giải thích
S(5) = 1 + 2 + 3 + 4 + 5 = 15; 5! = 1 * 2 * 3 * 4 * 5 = 120. Kết quả in ra: 15 120.

## Ràng buộc
- $100\%$ số test có $N \le 20$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
