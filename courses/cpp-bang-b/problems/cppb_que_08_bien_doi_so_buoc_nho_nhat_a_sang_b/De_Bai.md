# Biến Đổi Số Bước Nhỏ Nhất Từ A Sang B

## Bối cảnh
Một trò chơi giải đố toán học bắt đầu với số nguyên dương $A$. Tại mỗi bước, người chơi có thể thực hiện một trong hai thao tác: nhân đôi số hiện tại ($x \to 2x$) hoặc trừ số hiện tại đi 1 đơn vị ($x \to x - 1$). Hãy tìm số thao tác ít nhất để biến đổi số $A$ ban đầu thành đúng số mục tiêu $B$.

## Nhiệm vụ
Cho hai số nguyên dương $A$ và $B$. Hãy lập trình tìm số bước biến đổi ít nhất từ $A$ thành $B$.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^4$).

## Output
- In ra trên một dòng duy nhất một số nguyên là số bước ít nhất.

## Sample 1
### Input
```text
4 6
```
### Output
```text
2
```

### Giải thích
Để biến đổi từ $A = 4$ sang $B = 6$:

- Bước 1: Trừ 1 đơn vị: $4 - 1 = 3$.
- Bước 2: Nhân đôi: $3 \times 2 = 6$.
Chỉ cần đúng 2 bước biến đổi, kết quả in ra là 2.

## Ràng buộc
- $100\%$ số test có $1 \le A, B \le 10^4$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
