# Đếm số không chứa chữ số cấm

## Bối cảnh

Tổng đài taxi loại bỏ chữ số dễ gây nhầm lẫn khi đọc qua điện thoại khỏi mọi số tài xế để giảm cuốc xe bị gán nhầm trong giờ cao điểm. Mỗi đợt tuyển xét một đoạn số hiệu liên tiếp và cần đếm có bao nhiêu số hoàn toàn không chứa chữ số cấm để cấp phát cho tài xế mới. Chương trình quy hoạch động bỏ qua nhánh chứa chữ số cấm giúp đếm nhanh cả đoạn dài.

## Nhiệm vụ

Cho ba số nguyên $L, R, D$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) mà biểu diễn thập phân không chứa chữ số $D$, rồi in ra kết quả.

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

- Các số từ $1$ đến $20$ không chứa chữ số $1$ gồm $2$ đến $9$ (tám số) và $20$.
- Đếm được chín số nên chương trình in ra $9$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$; $0 \le D \le 9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
