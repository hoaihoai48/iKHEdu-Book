# Chia kẹo công bằng và tính kẹo dư

## Bối cảnh
Trong môn Toán tư duy, các bạn nhỏ được làm quen với khái niệm "Tổng các chữ số". Cô giáo đố bạn Nam tính thật nhanh tổng các chữ số của một số nguyên dương có đúng 3 chữ số mà không cần dùng đến vòng lặp.

## Nhiệm vụ
Cho một số nguyên dương $N$ có đúng ba chữ số ($100 \le N \le 999$). Hãy lập trình tính và in ra tổng của ba chữ số tạo nên số $N$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($100 \le N \le 999$).

## Output
- In ra một số nguyên duy nhất là tổng các chữ số của $N$.

## Sample 1
### Input
```text
357
```
### Output
```text
15
```

### Giải thích
Số $N = 357$ có 3 chữ số:

- Chữ số hàng trăm: $357 / 100 = 3$.
- Chữ số hàng chục: $(357 / 10) \% 10 = 5$.
- Chữ số hàng đơn vị: $357 \% 10 = 7$.
Tổng ba chữ số là: $3 + 5 + 7 = 15$.

## Sample 2
### Input
```text
505
```
### Output
```text
10
```

### Giải thích
Tổng các chữ số: $5 + 0 + 5 = 10$.

## Ràng buộc
- $100\%$ số test có $100 \le N \le 999$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
