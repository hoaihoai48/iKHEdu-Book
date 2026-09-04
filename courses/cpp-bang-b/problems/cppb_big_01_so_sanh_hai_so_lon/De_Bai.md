# So Sánh Hai Số Nguyên Lớn

## Bối cảnh
Trong hệ thống xác thực chứng thực số quốc gia, hai chứng thư điện tử có chuỗi khóa băm bảo mật biểu diễn dưới dạng hai số nguyên dương khổng lồ A và B (có độ dài lên đến 100.000 chữ số). Hệ thống cần xác định nhanh mối quan hệ thứ tự giữa A và B (A > B, A < B, hay A = B).

## Nhiệm vụ
Cho 2 số nguyên dương lớn A và B. Hãy so sánh A và B, in ra '>' nếu A > B, '<' nếu A < B, '=' nếu A = B.

## Input
- Dòng 1: Chuỗi ký tự số $A$ ($1 \le |A| \le 10^5$).
- Dòng 2: Chuỗi ký tự số $B$ ($1 \le |B| \le 10^5$).

## Output
- In ra `>`, `<` hoặc `=`.

## Sample 1
### Input
```text
123456789
98765432
```
### Output
```text
>
```
### Giải thích
Số A có 9 chữ số trong khi số B chỉ có 8 chữ số. Do đó A > B. Kết quả in ra: `>`.

## Ràng buộc
- $100\%$ số test có $|A|, |B| \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
