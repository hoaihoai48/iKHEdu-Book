# Tính giá trị trung bình cộng ba số

## Bối cảnh
Kết thúc kỳ thi học kỳ, bạn Bình nhận được điểm số của ba môn thi: Toán, Văn và Ngoại ngữ. Để biết được học lực tổng kết sơ bộ, Bình cần tính điểm trung bình cộng của ba môn này và làm tròn đến đúng hai chữ số thập phân.

## Nhiệm vụ
Cho ba số nguyên $a, b, c$ lần lượt là điểm số của ba môn thi. Hãy lập trình tính và in ra điểm trung bình cộng của ba môn, lấy đúng 2 chữ số sau dấu phẩy thập phân.

## Input
- Một dòng duy nhất chứa ba số nguyên $a, b, c$ ($0 \le a, b, c \le 10$), cách nhau bởi một khoảng trắng.

## Output
- In ra một số thực là điểm trung bình cộng của ba môn thi, định dạng đúng 2 chữ số thập phân.

## Sample 1
### Input
```text
8 7 9
```
### Output
```text
8.00
```

### Giải thích
Tổng điểm ba môn: $8 + 7 + 9 = 24$.
Điểm trung bình cộng: $24 / 3 = 8.0$.
In ra đúng 2 chữ số thập phân: `8.00`.

## Sample 2
### Input
```text
7 8 8
```
### Output
```text
7.67
```

### Giải thích
Tổng điểm: $7 + 8 + 8 = 23$.
Điểm trung bình: $23 / 3 = 7.6666...$ làm tròn 2 chữ số thập phân là `7.67`.

## Ràng buộc
- $100\%$ số test có $0 \le a, b, c \le 10$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
