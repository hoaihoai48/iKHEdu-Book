# Đánh Giá Biểu Thức Hậu Tố (Reverse Polish Notation)

## Bối cảnh
Trong thiết kế vi xử lý và máy tính cầm tay, biểu thức toán học thường được chuyển đổi sang dạng ký pháp nghịch đảo Ba Lan (hậu tố - Postfix) để máy tính dễ dàng tính toán mà không cần quan tâm đến độ ưu tiên của dấu ngoặc. Trong biểu thức hậu tố, toán tử luôn đứng sau hai toán hạng của nó (ví dụ: `2 3 +` tương đương `2 + 3 = 5`).

## Nhiệm vụ
Cho một biểu thức hậu tố gồm các số nguyên và 4 phép toán cơ bản `+`, `-`, `*`, `/` (chia lấy phần nguyên). Hãy lập trình tính và in ra giá trị cuối cùng của biểu thức.

## Input
- Một dòng duy nhất chứa các toán hạng và toán tử cách nhau bởi khoảng trắng ($1 \le \text{số lượng token} \le 10^4$).

## Output
- In ra một số nguyên duy nhất là giá trị của biểu thức.

## Sample 1
### Input
```text
5
2 1 + 3 *
```
### Output
```text
9
```

### Giải thích
Với biểu thức hậu tố "2 1 + 3 *":
1. Gặp toán tử '+': Thực hiện $2 + 1 = 3$.
2. Biểu thức trở thành "3 3 *".
3. Gặp toán tử '*': Thực hiện $3 \times 3 = 9$.
Giá trị cuối cùng thu được là 9.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
