# Số chứa đầy đủ các chữ số 0 đến 9

## Bối cảnh

Công ty bảo mật phát hành mã khóa dùng một lần với yêu cầu mỗi mã phải chứa đầy đủ cả mười chữ số từ 0 đến 9 ít nhất một lần để chống lại tấn công đoán mã bằng từ điển. Mỗi ngày hệ thống xét một đoạn mã liên tiếp và cần đếm có bao nhiêu mã đạt chuẩn an toàn để cấp phát cho các giao dịch giá trị cao. Chương trình quy hoạch động dùng mặt nạ bit ghi nhớ tập chữ số đã xuất hiện giúp đếm nhanh đoạn dài.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) mà biểu diễn thập phân chứa đầy đủ cả mười chữ số $0$ đến $9$, rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
1 2000000000
```

### Output

```text
362880```

### Giải thích

- Mọi số chứa đủ mười chữ số đều có ít nhất mười chữ số, mà $1023456789$ là số nhỏ nhất như vậy.
- Trong đoạn tới hai tỉ, chữ số đầu chỉ có thể là $1$ nên chín vị trí còn lại phải xếp đủ chín chữ số $0, 2, 3, 4, 5, 6, 7, 8, 9$ theo $9! = 362880$ cách.
- Chương trình in ra $362880$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
