# Chia Kẹo Công Bằng

## Bối cảnh
Cô giáo có $M$ viên kẹo và muốn chia đều cho $N$ bạn học sinh trong lớp. Mỗi bạn được nhận số kẹo bằng nhau, số kẹo dư sẽ được cô giữ lại. Cô cần biết mỗi bạn được bao nhiêu viên và dư bao nhiêu viên.

## Nhiệm vụ
Cho hai số nguyên dương $M$ (số kẹo) và $N$ (số bạn). Hãy lập trình tính và in ra hai số: số kẹo mỗi bạn nhận được và số kẹo còn dư.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $M$ và $N$ ($1 \le N \le M \le 10^9$), cách nhau bởi khoảng trắng.

## Output
- In ra hai số nguyên trên một dòng, cách nhau bởi khoảng trắng: số kẹo mỗi bạn nhận và số kẹo còn dư.

## Sample 1
### Input
```text
17 5
```
### Output
```text
3 2
```

### Giải thích
Có $17$ viên kẹo chia cho $5$ bạn:
- Mỗi bạn nhận: $17 / 5 = 3$ viên (chia nguyên).
- Số kẹo dư: $17 \% 5 = 2$ viên.
Vậy kết quả là `3 2`.

## Ràng buộc
- $100\%$ số test có $1 \le N \le M \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
