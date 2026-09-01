# Truy vấn so khớp xâu con hashing

## Bối cảnh
Cho xâu $S$ và $Q$ truy vấn kiểm tra xem hai xâu con $S[a..b]$ và $S[c..d]$ có giống nhau hay không.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Truy Vấn So Khớp Xâu Con Hashing với độ phức tạp tối ưu nhất.

## Input
- Dòng 1: Xâu $S$ ($|S| \le 10^5$). Dòng 2: $Q$ ($1 \le Q \le 10^5$). $Q$ dòng sau: $a, b, c, d$ (1-based).

## Output
- In ra `YES` nếu hai xâu con bằng nhau, `NO` nếu khác nhau.

## Sample 1
### Input
```text
abacaba
2
1 3 5 7
1 3 2 4
```
### Output
```text
YES
NO
```

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
