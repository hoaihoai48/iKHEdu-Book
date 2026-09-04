# Chia Hai Số Nguyên Lớn (A / B)

## Bối cảnh
Phép chia hai số nguyên lớn A / B là phép toán phức tạp nhất trong thư viện BigInt chuẩn, đòi hỏi kỹ thuật tìm kiếm nhị phân chữ số thương kết hợp nhân số lớn để tìm phần nguyên thương số.

## Nhiệm vụ
Cho 2 số nguyên dương lớn A và B. Hãy tìm phần nguyên thương số floor(A / B).

## Input
- Dòng 1: Chuỗi số $A$ ($1 \le |A| \le 1000$).
- Dòng 2: Chuỗi số $B$ ($1 \le |B| \le 1000$).

## Output
- In ra phần nguyên thương số $\lfloor A / B \rfloor$.

## Sample 1
### Input
```text
100
3
```
### Output
```text
33
```
### Giải thích
100 / 3 = 33 (dư 1). Phần nguyên thương là 33.

## Ràng buộc
- $100\%$ số test có $|A|, |B| \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
