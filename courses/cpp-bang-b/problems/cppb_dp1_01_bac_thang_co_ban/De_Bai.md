# Bậc Thang Cơ Bản

## Bối cảnh
Trong một tòa tháp công nghệ hiện đại, bạn robot phục vụ cần di chuyển lên đỉnh cầu thang gồm $N$ bậc để chuyển tài liệu. Do thiết kế cơ học của chân bước, ở mỗi nhịp di chuyển, robot chỉ có thể bước lên đúng $1$ bậc hoặc bước sải dài qua $2$ bậc liên tiếp. Để lập trình điều hướng linh hoạt cho robot, kỹ sư phần mềm cần tính toán xem có tất cả bao nhiêu trình tự bước đi khác nhau để đưa robot từ chân cầu thang lên tới đúng đỉnh bậc thứ $N$.

## Nhiệm vụ
Cho số nguyên dương $N$ là số bậc của cầu thang. Hãy lập trình tính số cách bước hợp lệ để robot lên đến đỉnh bậc thứ $N$. Vì kết quả có thể rất lớn, hãy in ra phần dư của kết quả khi chia cho $10^9 + 7$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$) biểu diễn số bậc của cầu thang.

## Output
- In ra trên một dòng duy nhất một số nguyên là số cách bước hợp lệ theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
3
```
### Output
```text
3
```

### Giải thích
Với cầu thang có $N = 3$ bậc, robot có tất cả 3 trình tự bước đi hợp lệ để lên đến đỉnh:
1. Bước từng bậc một: $1 + 1 + 1 = 3$.
2. Bước 1 bậc rồi bước 2 bậc: $1 + 2 = 3$.
3. Bước 2 bậc rồi bước 1 bậc: $2 + 1 = 3$.
Kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
