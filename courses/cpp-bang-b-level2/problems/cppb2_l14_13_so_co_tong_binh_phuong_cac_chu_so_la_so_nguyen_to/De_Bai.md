# Đếm số có đúng K bit 1

## Bối cảnh

Nhà sản xuất chip nhớ kiểm tra dải địa chỉ ô nhớ liên tiếp với yêu cầu mỗi địa chỉ đạt chuẩn phải có đúng K bit 1 trong biểu diễn nhị phân để mạch giải mã hoạt động ổn định ở tần số cao. Mỗi lô chip xét một đoạn địa chỉ và cần đếm có bao nhiêu địa chỉ đạt chuẩn trước khi đóng gói xuất xưởng. Chương trình tổ hợp theo từng bit giúp đếm nhanh đoạn dài mà không cần quét từng ô nhớ.

## Nhiệm vụ

Cho ba số nguyên $L, R, K$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) có đúng $K$ bit $1$ trong biểu diễn nhị phân, rồi in ra kết quả.

## Input

- Dòng duy nhất: ba số nguyên $L, R, K$ ($0 \le L \le R \le 10^{18}$, $0 \le K \le 60$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
1 10 2
```

### Output

```text
5
```

### Giải thích

- Các số từ $1$ đến $10$ viết nhị phân: $3 = 11$, $5 = 101$, $6 = 110$, $9 = 1001$, $10 = 1010$ có đúng hai bit $1$.
- Các số còn lại có một hoặc ba bit $1$ nên bị loại.
- Đếm được $5$ số nên chương trình in ra $5$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$; $0 \le K \le 60$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
