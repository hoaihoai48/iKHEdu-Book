# Kiểm tra điều kiện ba cạnh tam giác

## Bối cảnh
Trong giờ thực hành môn Hình học, thầy giáo phát cho mỗi nhóm học sinh ba thanh gỗ có độ dài lần lượt là $a, b, c$. Các bạn cần kiểm tra xem ba thanh gỗ này có thể ghép lại thành một hình tam giác hay không.

## Nhiệm vụ
Cho ba số nguyên dương $a, b, c$. Hãy lập trình kiểm tra xem $a, b, c$ có thể là độ dài ba cạnh của một tam giác hợp lệ hay không:

- Nếu tạo thành tam giác, in ra `YES`.
- Nếu không tạo thành tam giác, in ra `NO`.

## Input
- Một dòng duy nhất chứa ba số nguyên dương $a, b, c$ ($1 \le a, b, c \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra một dòng duy nhất chữ `YES` hoặc `NO`.

## Sample 1
### Input
```text
3 4 5
```
### Output
```text
YES
```

### Giải thích
Ba số $3, 4, 5$ thỏa mãn bất đẳng thức tam giác:

- $3 + 4 = 7 > 5$
- $3 + 5 = 8 > 4$
- $4 + 5 = 9 > 3$
Do đó tạo thành tam giác hợp lệ. In ra `YES`.

## Sample 2
### Input
```text
1 2 5
```
### Output
```text
NO
```

### Giải thích
Ta có $1 + 2 = 3 < 5$, tổng hai cạnh không lớn hơn cạnh còn lại nên không thể tạo thành tam giác. In ra `NO`.

## Ràng buộc
- $100\%$ số test có $1 \le a, b, c \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
