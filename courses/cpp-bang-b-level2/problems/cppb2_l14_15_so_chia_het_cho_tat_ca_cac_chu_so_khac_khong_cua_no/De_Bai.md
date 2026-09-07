# Số thứ K không chứa chữ số 4

## Bối cảnh

Khu đô thị thông minh đánh số nhà tránh dùng chữ số 4 trong mọi biển số để chiều lòng cư dân có quan niệm kiêng kỵ lâu đời. Ban quản lý cần tìm biển số thứ K trong dãy các số nguyên dương hoàn toàn không chứa chữ số 4 để gắn cho căn hộ mới bàn giao trong tuần này. Chương trình đếm số không chứa chữ số 4 kết hợp chặt nhị phân giúp tìm ra đáp án nhanh mà không cần liệt kê từng biển số.

## Nhiệm vụ

Cho số nguyên $K$. Hãy lập trình tìm số thứ $K$ (đánh số từ $1$, bắt đầu từ số $0$) trong dãy các số nguyên không âm mà biểu diễn thập phân không chứa chữ số $4$, rồi in ra kết quả.

## Input

- Dòng duy nhất: số nguyên $K$ ($1 \le K \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số cần tìm.

## Sample 1

### Input

```text
5
```

### Output

```text
5
```

### Giải thích

- Liệt kê các số không chứa chữ số $4$ từ nhỏ đến lớn: $0, 1, 2, 3, 5, \dots$ (bỏ qua $4$).
- Số thứ năm trong dãy này là $5$.
- Chương trình in ra $5$.

## Ràng buộc

- $1 \le K \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
