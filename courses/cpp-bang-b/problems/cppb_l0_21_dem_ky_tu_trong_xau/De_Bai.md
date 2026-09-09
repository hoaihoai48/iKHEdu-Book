# Đếm số lần xuất hiện của ký tự trong xâu

## Bối cảnh
Trong việc xử lý văn bản và công cụ tìm kiếm, thao tác đếm số lần xuất hiện của một ký tự cụ thể trong một đoạn văn bản là thao tác cơ bản nhất. Bạn hãy lập trình đọc một chuỗi ký tự và đếm xem một ký tự mục tiêu xuất hiện bao nhiêu lần trong chuỗi đó.

## Nhiệm vụ
Cho một xâu ký tự $S$ (không chứa khoảng trắng) và một ký tự $C$. Hãy lập trình đếm và in ra số lần ký tự $C$ xuất hiện trong xâu $S$.

## Input
- Dòng thứ nhất chứa xâu ký tự $S$ ($1 \le |S| \le 10^5$), chỉ gồm các chữ cái tiếng Anh.
- Dòng thứ hai chứa một ký tự $C$.

## Output
- In ra một số nguyên duy nhất là số lần xuất hiện của ký tự $C$ trong xâu $S$.

## Sample 1
### Input
```text
banana
a
```
### Output
```text
3
```

### Giải thích
Trong xâu `banana`, ký tự `a` xuất hiện $3$ lần (tại các vị trí chỉ số 1, 3, 5). In ra `3`.

## Sample 2
### Input
```text
Programming
z
```
### Output
```text
0
```

### Giải thích
Ký tự `z` không xuất hiện lần nào trong xâu, in ra `0`.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
