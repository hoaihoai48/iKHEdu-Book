# Đếm số có tổng chữ số nguyên tố

## Bối cảnh

Đài thiên văn tỉnh phát động cuộc thi tìm ngôi sao may mắn trong đó mã số đăng ký được coi là đẹp khi tổng các chữ số của nó là một số nguyên tố để gắn với chủ đề các con số bí ẩn của vũ trụ bao la. Mỗi đợt thi xét một đoạn mã liên tiếp và cần đếm có bao nhiêu mã đẹp để chuẩn bị giấy chứng nhận cho thí sinh dự thi. Chương trình quy hoạch động ghi nhớ tổng chữ số rồi kiểm tra tính nguyên tố giúp đếm nhanh cả đoạn dài.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) có tổng các chữ số là số nguyên tố, rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
1 13
```

### Output

```text
6
```

### Giải thích

- Các số từ $1$ đến $13$ có tổng chữ số là nguyên tố gồm $2, 3, 5, 7$ (tổng một chữ số) và $11, 12$ (tổng $2$ và $3$).
- Đếm được sáu số nên chương trình in ra $6$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
