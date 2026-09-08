# Tìm Giá Trị Lớn Nhất

## Bối cảnh
Trong kỳ thi học kỳ, giáo viên cần tìm ra điểm cao nhất trong lớp để trao giải thưởng. Với lớp có đông học sinh, việc rà soát bằng mắt rất dễ sai sót.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên. Hãy lập trình tìm và in ra giá trị lớn nhất trong dãy.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($|a_i| \le 10^9$), cách nhau bởi khoảng trắng.

## Output
- In ra một số nguyên duy nhất là giá trị lớn nhất trong dãy.

## Sample 1
### Input
```text
5
3 1 4 1 5
```
### Output
```text
5
```

### Giải thích
Dãy gồm $5$ phần tử: $3, 1, 4, 1, 5$.
Duyệt lần lượt:
- So sánh $3$: max hiện tại $= 3$.
- So sánh $1$: $1 < 3$, giữ nguyên.
- So sánh $4$: $4 > 3$, cập nhật max $= 4$.
- So sánh $1$: $1 < 4$, giữ nguyên.
- So sánh $5$: $5 > 4$, cập nhật max $= 5$.
Kết quả: giá trị lớn nhất là $5$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$, $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
