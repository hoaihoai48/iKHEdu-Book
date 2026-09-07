# Chia số nguyên lớn cho số nhỏ

## Bối cảnh

Chi cục thuế tính thuế thu nhập cho doanh nghiệp có doanh thu khổng lồ vượt xa kiểu số nguyên 64-bit bằng cách chia tổng doanh thu cho số lượng cổ đông để xác định cổ tức bình quân mỗi người. Mỗi hồ sơ quyết toán gửi một số bị chia rất lớn và một số chia vừa phải, chương trình cần trả về thương nguyên chính xác tuyệt đối để in lên biên lai thuế. Thuật toán chia theo từng chữ số thập phân cho ra thương trong thời gian tuyến tính theo số chữ số.

## Nhiệm vụ

Cho số nguyên lớn $A$ (tới $1000$ chữ số) và số nguyên $B$. Hãy lập trình tính thương nguyên của $A$ chia cho $B$, rồi in ra kết quả.

## Input

- Dòng 1: số nguyên lớn $A$ ($A \ge 0$).
- Dòng 2: số nguyên $B$ ($1 \le B \le 10^9$).

## Output

- In ra một dòng duy nhất là thương nguyên $\lfloor A/B \rfloor$.

## Sample 1

### Input

```text
12345
123
```

### Output

```text
100
```

### Giải thích

- Lấy $12345 \div 123$: $123 \times 100 = 12300$ vừa khít không vượt quá, còn $123 \times 101 = 12423$ đã lớn hơn.
- Thương nguyên là $100$ với số dư $45$ nhưng đề chỉ yêu cầu in thương.
- Chương trình in ra $100$.

## Ràng buộc

- $A$ có tối đa $1000$ chữ số; $1 \le B \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
