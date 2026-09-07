# Số có các chữ số tăng ngặt

## Bối cảnh

Ngân hàng phát hành thẻ tín dụng dòng cao cấp với yêu cầu số thẻ phải có các chữ số tăng nghiêm ngặt từ trái sang phải để tạo dấu ấn sang trọng dễ nhận biết khi thanh toán. Mỗi đợt phát hành xét một đoạn số liên tiếp và cần đếm có bao nhiêu số thẻ đạt chuẩn thiết kế để đặt phôi thẻ từ nhà cung ứng. Chương trình quy hoạch động chữ số ghi nhớ chữ số trước đó giúp đếm nhanh cả đoạn dài tới hàng nghìn tỉ.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) có các chữ số tăng nghiêm ngặt từ trái sang phải, rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số thỏa mãn (số $0$ không được tính).

## Sample 1

### Input

```text
1 30
```

### Output

```text
24
```

### Giải thích

- Các số một chữ số từ $1$ đến $9$ đều thỏa mãn vì chỉ có một chữ số.
- Các số hai chữ số tới $30$ thỏa mãn là $12$ đến $19$ (tám số) và $23$ đến $29$ (bảy số), tổng $9 + 8 + 7 = 24$ nên chương trình in ra $24$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
