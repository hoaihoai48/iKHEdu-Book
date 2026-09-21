# Chia kẹo Trung Thu

## Bối cảnh
Nhân dịp Tết Trung Thu, cô giáo chủ nhiệm mang đến lớp một gói kẹo gồm $N$ chiếc kẹo để chia đều cho $K$ bạn học sinh trong lớp. Mỗi bạn học sinh đều nhận được số lượng kẹo bằng nhau. Số kẹo còn dư lại (nếu có) sẽ được cho vào hòm quà chung của lớp.

## Nhiệm vụ
Cho hai số nguyên dương $N$ và $K$ lần lượt là số lượng kẹo và số bạn học sinh. Hãy lập trình tính và in ra số kẹo mỗi bạn nhận được và số kẹo còn dư vào hòm quà chung.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $N$ và $K$ ($1 \le N, K \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra hai số nguyên cách nhau bởi một khoảng trắng: số thứ nhất là số kẹo mỗi bạn nhận được, số thứ hai là số kẹo còn dư.

## Sample 1
### Input
```text
23 5
```
### Output
```text
4 3
```

### Giải thích
Có $23$ cái kẹo chia cho $5$ bạn:

- Mỗi bạn nhận được: $23 / 5 = 4$ cái kẹo.
- Số kẹo đã chia: $4 \times 5 = 20$ cái.
- Số kẹo còn dư: $23 \% 5 = 3$ cái.
Kết quả in ra: `4 3`.

## Sample 2
### Input
```text
30 6
```
### Output
```text
5 0
```

### Giải thích
$30$ chia hết cho $6$, mỗi bạn nhận đúng $5$ cái và không dư cái nào.

## Ràng buộc
- $100\%$ số test có $1 \le N, K \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
