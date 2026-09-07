# Tổng bình phương chữ số trên đoạn

## Bối cảnh

Viện kiểm định chất lượng mã vạch dùng chỉ số đặc trưng bằng tổng bình phương các chữ số của mọi mã trong lô hàng để phát hiện sai lệch khi quét hàng loạt tại cửa khẩu. Mỗi lô ứng với một đoạn mã liên tiếp và hệ thống cần tính tổng đặc trưng này để so với tem kiểm định đã dán trên thùng hàng. Chương trình quy hoạch động cộng dồn bình phương chữ số giúp tính tổng cả lô dài hàng nghìn tỉ trong tích tắc.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình tính tổng bình phương các chữ số của tất cả các số $x$ ($L \le x \le R$), rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là tổng cần tính (dùng số nguyên 64-bit).

## Sample 1

### Input

```text
1 10
```

### Output

```text
286
```

### Giải thích

- Bình phương chữ số từ $1$ đến $9$ cộng lại là $1+4+9+16+25+36+49+64+81 = 285$.
- Số $10$ đóng góp $1^2 + 0^2 = 1$.
- Tổng chung $285 + 1 = 286$ nên chương trình in ra $286$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
