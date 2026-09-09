# Đếm số chữ số và tính tổng các chữ số

## Bối cảnh
Trong khoa học mật mã và lý thuyết số, tổng chữ số và số lượng chữ số của một số nguyên lớn đóng vai trò quan trọng trong việc tính toán mã kiểm tra (checksum) để phát hiện sai sót dữ liệu truyền qua mạng.

## Nhiệm vụ
Cho một số nguyên không âm $N$. Hãy lập trình đếm số lượng chữ số và tính tổng tất cả các chữ số của $N$.

## Input
- Một dòng duy nhất chứa số nguyên không âm $N$ ($0 \le N \le 10^{18}$).

## Output
- In ra hai số nguyên cách nhau bởi một khoảng trắng: số thứ nhất là số lượng chữ số, số thứ hai là tổng các chữ số của $N$.

## Sample 1
### Input
```text
12345
```
### Output
```text
5 15
```

### Giải thích
Số $12345$ có $5$ chữ số.
Tổng các chữ số là: $1 + 2 + 3 + 4 + 5 = 15$.
Kết quả in ra: `5 15`.

## Sample 2
### Input
```text
0
```
### Output
```text
1 0
```

### Giải thích
Số $0$ có đúng $1$ chữ số và tổng các chữ số bằng $0$.

## Ràng buộc
- $100\%$ số test có $0 \le N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
