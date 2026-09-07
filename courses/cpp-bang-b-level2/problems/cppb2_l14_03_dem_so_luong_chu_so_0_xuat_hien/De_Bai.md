# Đếm số không chứa chữ số D

## Bối cảnh

Sở giao thông đô thị phát hành biển số xe theo dải số liên tiếp cho đợt đăng ký mới, nhưng một số khách hàng kiêng chữ số D vì quan niệm không may mắn khi lưu thông trên đường. Phòng đăng ký cần đếm trong đoạn số từ L đến R có bao nhiêu biển số hoàn toàn không chứa chữ số D để sắp xếp lịch bấm biển riêng. Vì dải số rất dài nên chương trình dùng quy hoạch động chữ số thay vì kiểm tra từng biển.

## Nhiệm vụ

Cho ba số nguyên $L, R, D$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) mà biểu diễn thập phân của $x$ không chứa chữ số $D$, rồi in ra kết quả.

## Input

- Dòng duy nhất: ba số nguyên $L, R, D$ ($0 \le L \le R \le 10^{18}$, $0 \le D \le 9$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
1 20 1
```

### Output

```text
9
```

### Giải thích

- Các số từ $1$ đến $20$ không chứa chữ số $1$ gồm $2$ đến $9$ (tám số) và $20$, tổng chín số nên chương trình in ra $9$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$; $0 \le D \le 9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
