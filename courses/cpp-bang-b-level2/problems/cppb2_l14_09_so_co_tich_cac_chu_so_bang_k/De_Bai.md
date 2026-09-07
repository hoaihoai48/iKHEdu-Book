# Số có tích các chữ số bằng K

## Bối cảnh

Xưởng sản xuất khóa số cơ khí kiểm định các mã khóa mới với yêu cầu tích các chữ số của mã phải đúng bằng hằng số K thì ổ khóa mới xoay trơn tru theo thiết kế rãnh bi. Mỗi lô kiểm định xét một đoạn mã liên tiếp và cần đếm có bao nhiêu mã đạt chuẩn để dán tem xuất xưởng. Chương trình quy hoạch động ghi nhớ tích hiện tại giúp đếm nhanh cả đoạn dài mà không cần thử từng chiếc khóa.

## Nhiệm vụ

Cho ba số nguyên $L, R, K$. Hãy lập trình đếm các số $x$ ($L \le x \le R$, $x > 0$) có tích các chữ số đúng bằng $K$, rồi in ra kết quả.

## Input

- Dòng duy nhất: ba số nguyên $L, R, K$ ($1 \le L \le R \le 10^{18}$, $0 \le K \le 10^9$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
1 30 6
```

### Output

```text
3```

### Giải thích

- Số $6$ có tích chữ số là $6$; số $16$ có tích $1 \times 6 = 6$; số $23$ có tích $2 \times 3 = 6$.
- Mọi số còn lại tới $30$ đều có tích khác $6$ (ví dụ $26$ cho tích $12$).
- Đếm được $3$ số nên chương trình in ra $3$.

## Ràng buộc

- $1 \le L \le R \le 10^{18}$; $0 \le K \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
