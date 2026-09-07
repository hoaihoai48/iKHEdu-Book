# Số stepping hiệu hai chữ số kề ít nhất 2

## Bối cảnh

Viện thiết kế chống hàng giả in mã an ninh lên tem sản phẩm với yêu cầu hai chữ số kề nhau bất kỳ phải chênh lệch ít nhất 2 đơn vị để máy quét phân biệt rõ ràng khi tem bị mờ một phần. Mỗi đợt sản xuất xét một đoạn mã liên tiếp và cần đếm có bao nhiêu mã đạt chuẩn in ấn để đặt mực in chuyên dụng. Chương trình quy hoạch động ghi nhớ chữ số trước đó giúp đếm nhanh cả đoạn dài tới hàng nghìn tỉ.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) mà hiệu tuyệt đối của mọi cặp chữ số kề nhau đều ít nhất $2$, rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn (số có một chữ số luôn thỏa mãn).

## Sample 1

### Input

```text
1 30
```

### Output

```text
24```

### Giải thích

- Các số một chữ số từ $1$ đến $9$ đều thỏa mãn vì không có cặp kề nào.
- Các số hai chữ số tới $30$ bị loại đúng sáu số là $10, 12, 21, 23$ (hiệu $1$) và $11, 22$ (hiệu $0$).
- Còn lại $21 - 6 = 15$ số hai chữ số, tổng $9 + 15 = 24$ nên in ra $24$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
