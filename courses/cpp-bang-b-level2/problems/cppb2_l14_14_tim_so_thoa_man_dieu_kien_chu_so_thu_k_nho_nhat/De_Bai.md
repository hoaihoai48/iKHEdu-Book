# Đếm số không chứa chuỗi 49

## Bối cảnh

Hãng hàng không mới khai trương tránh dùng chuỗi 49 trong mã số ghế vì cách đọc dễ gây nhầm lẫn của nhiều hành khách trên các đường bay quốc tế tấp nập. Mỗi đợt mở bán xét một đoạn mã ghế liên tiếp và cần đếm có bao nhiêu mã hoàn toàn không chứa chuỗi 49 kề nhau để in thẻ lên máy bay kịp tiến độ. Chương trình quy hoạch động ghi nhớ chữ số trước đó giúp đếm nhanh cả đoạn dài hàng tỉ mã ghế.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) mà biểu diễn thập phân không chứa chuỗi con $49$ (chữ số $4$ đứng ngay trước chữ số $9$), rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn.

## Sample 1

### Input

```text
40 55
```

### Output

```text
15
```

### Giải thích

- Trong đoạn từ $40$ đến $55$ có $16$ số, chỉ duy nhất số $49$ chứa chuỗi $49$ kề nhau.
- Còn lại $16 - 1 = 15$ số đạt chuẩn.
- Chương trình in ra $15$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
