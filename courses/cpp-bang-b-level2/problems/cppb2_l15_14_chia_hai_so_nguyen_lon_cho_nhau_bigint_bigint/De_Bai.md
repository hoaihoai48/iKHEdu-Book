# Chia hai số nguyên lớn

## Bối cảnh

Công ty logistics quốc tế cần chia đều lô hàng có tổng giá trị khổng lồ cho các đối tác theo tỉ lệ góp vốn, trong đó cả tổng giá trị và số phần chia đều là những số nguyên vượt xa kiểu dữ liệu thông thường. Mỗi hợp đồng yêu cầu biết thương nguyên và số dư của phép chia để lập biên bản phân chia tài sản có chữ ký các bên. Chương trình chia số lớn theo từng chữ số thập phân cho ra thương và dư chính xác tuyệt đối.

## Nhiệm vụ

Cho hai số nguyên dương $A, B$ rất lớn. Hãy lập trình tính thương nguyên $Q$ và số dư $R$ của phép chia $A$ cho $B$, rồi in ra trên hai dòng.

## Input

- Dòng 1: số nguyên lớn $A$.
- Dòng 2: số nguyên lớn $B$ ($B > 0$).

## Output

- Dòng 1: thương nguyên $Q$.
- Dòng 2: số dư $R$.

## Sample 1

### Input

```text
12345
123
```

### Output

```text
100
45```

### Giải thích

- Lấy $12345 \div 123$: $123 \times 100 = 12300$ vừa khít không vượt quá.
- Số dư còn lại là $12345 - 12300 = 45$.
- In ra $100$ rồi $45$ trên hai dòng.

## Ràng buộc

- Mỗi số có tối đa $1000$ chữ số.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
