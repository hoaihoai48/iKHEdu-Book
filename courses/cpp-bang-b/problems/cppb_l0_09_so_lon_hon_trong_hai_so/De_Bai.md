# Tìm số lớn hơn trong hai số

## Bối cảnh
Trong cuộc thi đo chiều cao tại phòng y tế học đường, bác sĩ cần so sánh chiều cao của hai bạn An và Bình để ghi nhận bạn nào có chiều cao nhỉnh hơn. Nếu hai bạn cao bằng nhau thì bác sĩ ghi nhận kết quả là bằng nhau.

## Nhiệm vụ
Cho hai số nguyên $a$ và $b$. Hãy lập trình so sánh hai số:

- Nếu $a > b$, in ra giá trị của $a$.
- Nếu $b > a$, in ra giá trị của $b$.
- Nếu $a = b$, in ra chuỗi `BANG NHAU`.

## Input
- Một dòng duy nhất chứa hai số nguyên $a$ và $b$ ($-10^9 \le a, b \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra một dòng duy nhất theo yêu cầu của đề bài.

## Sample 1
### Input
```text
7 12
```
### Output
```text
12
```

### Giải thích
Vì $12 > 7$ nên chương trình in ra số lớn hơn là `12`.

## Sample 2
### Input
```text
9 9
```
### Output
```text
BANG NHAU
```

### Giải thích
Vì hai số bằng nhau nên chương trình in ra `BANG NHAU`.

## Ràng buộc
- $100\%$ số test có $-10^9 \le a, b \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
