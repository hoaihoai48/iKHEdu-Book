# Nhân hai số nguyên lớn

## Bối cảnh

Phòng kế toán tổng hợp cần tính tổng giá trị hợp đồng bằng cách nhân đơn giá với số lượng hàng hóa, trong đó cả hai số đều có thể dài tới hàng trăm chữ số vượt xa khả năng của kiểu số nguyên 64-bit thông thường. Mỗi ngày hàng nghìn phép nhân như vậy được gửi về máy chủ để lập báo cáo tài chính hợp nhất toàn tập đoàn. Chương trình nhân số lớn theo từng chữ số thập phân giúp cho ra kết quả chính xác tuyệt đối mà không bị tràn số.

## Nhiệm vụ

Cho hai số nguyên không âm $A, B$ có thể rất lớn (mỗi số tới $1000$ chữ số). Hãy lập trình tính tích $A \times B$ với độ chính xác tuyệt đối, rồi in ra kết quả.

## Input

- Dòng 1: số nguyên lớn $A$ (không có số 0 vô nghĩa ở đầu, trừ chính số $0$).
- Dòng 2: số nguyên lớn $B$ (quy ước tương tự).

## Output

- In ra một dòng duy nhất là tích $A \times B$.

## Sample 1

### Input

```text
123
456
```

### Output

```text
56088```

### Giải thích

- Đặt phép nhân $123 \times 456$ theo hàng dọc như tính tay.
- Nhân $123$ với $6$ được $738$, với $50$ được $6150$, với $400$ được $49200$.
- Cộng ba kết quả trung gian $738 + 6150 + 49200 = 56088$ nên in ra $56088$.

## Ràng buộc

- Mỗi số có tối đa $1000$ chữ số.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
