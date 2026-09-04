# Lát Gạch Bảng 2xN

## Bối cảnh
Trong một triển lãm kiến trúc, ban tổ chức cần lát kín một khoảng sàn hình chữ nhật có kích thước cố định là $2  × N$ bằng các viên gạch men trang trí kích thước $1  × 2$. Mỗi viên gạch men có thể được đặt nằm ngang (kích thước $1  × 2$) hoặc dựng đứng (kích thước $2  × 1$). Toàn bộ mặt sàn phải được phủ kín hoàn toàn, không có ô nào bị bỏ trống và các viên gạch không được phép đè lên nhau.

## Nhiệm vụ
Cho số nguyên dương $N$ là chiều dài của mặt sàn. Hãy lập trình tính số cách lát gạch khác nhau để phủ kín mặt sàn $2  × N$, lấy dư cho $10^9 + 7$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn chiều dài mặt sàn.

## Output
- In ra trên một dòng duy nhất số cách lát sàn hợp lệ theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
4
```
### Output
```text
5
```

### Giải thích
Với sàn nhà kích thước $2  × 4$ ($N = 4$), có tất cả 5 cách lát kín hợp lệ:
1. Đặt 4 viên gạch dựng đứng liên tiếp.
2. Đặt 2 viên nằm ngang ở đầu, theo sau là 2 viên dựng đứng.
3. Đặt 1 viên dựng đứng, 2 viên nằm ngang ở giữa, 1 viên dựng đứng ở cuối.
4. Đặt 2 viên dựng đứng ở đầu, theo sau là 2 viên nằm ngang.
5. Đặt 2 cặp viên nằm ngang chồng lên nhau.
Kết quả in ra là 5.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
