# Duyệt Toàn Bộ 2^N Tập Con Bằng Mặt Nạ Bit

## Bối cảnh
Cho một tập hợp gồm $N$ số nguyên phân biệt. Hãy liệt kê tất cả $2^N$ tập con của tập hợp này theo thứ tự từ điển của mặt nạ bit (từ $0$ đến $2^N - 1$).

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 15$).
- Dòng 2: $N$ số nguyên $A_0, A_1, \dots, A_{N-1}$ ($|A_i| \le 10^9$).

## Output
- In ra $2^N$ dòng. Mỗi dòng in ra các phần tử của tập con tương ứng, cách nhau bởi khoảng trắng (nếu là tập rỗng thì in dòng trống).

## Sample 1
### Input
```text
3
1 2 3
```
### Output
```text

1
2
1 2
3
1 3
2 3
1 2 3
```

## Ràng buộc
- $100\%$ số test có $N \le 15$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
