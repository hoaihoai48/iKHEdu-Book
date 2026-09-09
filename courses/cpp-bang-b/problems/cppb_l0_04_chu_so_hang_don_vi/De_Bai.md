# Tìm chữ số hàng đơn vị

## Bối cảnh
Trong trò chơi bốc thăm may mắn tại hội chợ xuân, mỗi người tham gia nhận được một tấm vé có in một mã số nguyên dương. Hai chữ số cuối cùng của mã vé (chữ số hàng chục và chữ số hàng đơn vị) sẽ quyết định giải thưởng mà người đó nhận được.

## Nhiệm vụ
Cho một số nguyên dương $N$ có ít nhất hai chữ số. Hãy lập trình tìm và in ra chữ số hàng chục cùng chữ số hàng đơn vị của $N$, cách nhau bởi một khoảng trắng.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($10 \le N \le 10^9$).

## Output
- In ra hai chữ số cách nhau bởi một khoảng trắng lần lượt là chữ số hàng chục và chữ số hàng đơn vị của $N$.

## Sample 1
### Input
```text
357
```
### Output
```text
5 7
```

### Giải thích
Số $N = 357$:

- Chữ số hàng đơn vị là: $357 \% 10 = 7$.
- Để lấy chữ số hàng chục: chia nguyên bỏ chữ số cuối $357 / 10 = 35$, sau đó lấy phần dư $35 \% 10 = 5$.
Kết quả in ra: `5 7`.

## Sample 2
### Input
```text
80
```
### Output
```text
8 0
```

### Giải thích
Số $N = 80$ có chữ số hàng chục là $8$ và chữ số hàng đơn vị là $0$.

## Ràng buộc
- $100\%$ số test có $10 \le N \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
