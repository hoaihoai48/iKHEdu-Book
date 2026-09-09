# Lát Gạch Bảng 3xN

## Bối cảnh
Tiếp tục bài toán thiết kế mặt sàn kiến trúc, lần này sàn nhà được mở rộng thành kích thước $3 × N$. Ban tổ chức vẫn sử dụng các viên gạch men domino có kích thước $2 × 1$ (có thể xoay ngang thành $1 × 2$). Yêu cầu đặt ra là phải lát kín hoàn toàn diện tích $3 × N$ mà không có viên gạch nào vượt ra ngoài biên hoặc đè lên nhau.

## Nhiệm vụ
Cho số nguyên dương $N$ là chiều dài của sàn nhà. Hãy lập trình đếm số cách lát kín mặt sàn $3 × N$, lấy dư cho $10^9 + 7$. (Nếu $N$ lẻ, diện tích sàn là số lẻ nên không thể phủ kín bằng các viên gạch diện tích 2, khi đó in ra `0`).

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn chiều dài của sàn.

## Output
- In ra trên một dòng duy nhất số cách lát kín sàn theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
2
```
### Output
```text
3
```

### Giải thích
Với sàn nhà kích thước $3 × 2$ ($N = 2$), tổng diện tích là $3 × 2 = 6$ ô đơn vị, cần dùng đúng 3 viên gạch domino. Có tất cả đúng 3 cách ghép hợp lệ:

1. Một viên đặt dọc ở cột 1, hai viên đặt ngang ở hàng 2 và 3.
2. Hai viên đặt ngang ở hàng 1 và 2, một viên đặt dọc ở cột 2.
3. Ba viên đặt ngang song song với nhau.
Kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
