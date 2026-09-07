# Tiền xử lý nghịch đảo tuyến tính $\mathcal{o}(n)$

## Bối cảnh
Phòng thí nghiệm cần chuẩn bị sẵn một bảng tra cứu: với mỗi số $i$ từ $1$ đến $n$, ghi lại "số đảo" của $i$ theo modulo $10^9+7$ (số nhân với $i$ cho phần dư $1$). Bảng này được in một lần rồi dùng cho cả học kỳ, nên khâu chuẩn bị cần làm gọn trong một lượt duyệt duy nhất.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho số nguyên $n$. Hãy lập trình tính nghịch đảo modulo $10^9+7$ của từng số $i$ với $1 \le i \le n$.

## Input

- Gồm một dòng duy nhất chứa số nguyên dương $n$ ($1 \le n \le 10^6$).

## Output

- In ra một dòng duy nhất gồm nghịch đảo modulo $10^9+7$ của từng số $i$ với $1 \le i \le \min(n, 20)$, các số cách nhau bởi một dấu cách.

## Sample 1
### Input
```text
5
```
### Output
```text
1 500000004 333333336 250000002 400000003
```
### Giải thích

Kiểm tra tay từng số: $1 \cdot 1 = 1$; $2 \cdot 500000004 = 1000000008 = (10^9+7) + 1$ nên dư $1$; $3 \cdot 333333336 = 1000000008$ dư $1$; $4 \cdot 250000002 = 1000000008$ dư $1$; $5 \cdot 400000003 = 2000000015 = 2 \cdot (10^9+7) + 1$ nên dư $1$. Cả $5$ số đều đúng là nghịch đảo cần tìm.

## Ràng buộc

- $1 \le n \le 10^6$; chương trình chỉ in $\min(n, 20)$ số đầu tiên.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
