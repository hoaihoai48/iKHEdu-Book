# Đánh Giá Biểu Thức Trung Tố (Infix Expression)

## Bối cảnh
Một máy tính bỏ túi thông minh tiếp nhận biểu thức số học viết ở dạng trung tố tự nhiên (dạng toán học thông thường có chứa các dấu ngoặc tròn `()`, số nguyên và 4 phép toán cơ bản `+`, `-`, `*`, `/`). Biểu thức tuân thủ độ ưu tiên toán học: nhân chia trước, cộng trừ sau, trong ngoặc trước, ngoài ngoặc sau.

## Nhiệm vụ
Cho một chuỗi biểu thức số học trung tố hợp lệ. Hãy lập trình tính toán và in ra giá trị số học cuối cùng của biểu thức.

## Input
- Một dòng duy nhất chứa chuỗi biểu thức gồm các chữ số, dấu ngoặc `(` `)` và các toán tử `+ - * /` ($1 \le |S| \le 10^5$).

## Output
- In ra trên một dòng duy nhất một số nguyên là kết quả của biểu thức.

## Sample 1
### Input
```text
3+2*2
```
### Output
```text
7
```

### Giải thích
Với biểu thức số học "1 + (2 * 3) - 4 / 2":
1. Tính trong ngoặc: $2 \times 3 = 6$.
2. Biểu thức trở thành: $1 + 6 - 4 / 2$.
3. Thực hiện phép chia: $4 / 2 = 2$.
4. Biểu thức thành: $1 + 6 - 2 = 5$.
Kết quả in ra là 5.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
