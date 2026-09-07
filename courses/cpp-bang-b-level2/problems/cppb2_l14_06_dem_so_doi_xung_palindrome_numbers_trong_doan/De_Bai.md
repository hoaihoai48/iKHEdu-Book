# Đếm số đối xứng trong đoạn

## Bối cảnh

Nhà sách thiếu nhi in mã số đối xứng lên bìa bộ truyện tranh sưu tầm để độc giả nhỏ tuổi dễ ghi nhớ và thích thú khi đọc ngược vẫn giống hệt. Mỗi đợt in xét một đoạn mã liên tiếp và cần đếm có bao nhiêu mã đối xứng để đặt giấy bìa cứng chống thấm nước. Chương trình sinh nửa đầu rồi phản chiếu giúp đếm nhanh cả đoạn dài mà không cần kiểm tra từng mã số.

## Nhiệm vụ

Cho hai số nguyên $L, R$. Hãy lập trình đếm các số $x$ ($L \le x \le R$) đọc xuôi ngược giống nhau (palindrome), rồi in ra kết quả.

## Input

- Dòng duy nhất: hai số nguyên $L, R$ ($0 \le L \le R \le 10^{18}$).

## Output

- In ra một dòng duy nhất là số lượng số đối xứng trong đoạn.

## Sample 1

### Input

```text
1 20
```

### Output

```text
10
```

### Giải thích

- Các số một chữ số từ $1$ đến $9$ đều đối xứng, tổng chín số.
- Trong các số hai chữ số tới $20$ chỉ có $11$ đọc ngược vẫn là $11$.
- Tổng $9 + 1 = 10$ nên chương trình in ra $10$.

## Ràng buộc

- $0 \le L \le R \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
