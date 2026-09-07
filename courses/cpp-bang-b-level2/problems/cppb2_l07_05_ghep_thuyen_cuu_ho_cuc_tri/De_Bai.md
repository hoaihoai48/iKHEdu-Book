# Ghép thuyền cứu hộ cực trị

## Bối cảnh

Mùa mưa lũ, đội cứu hộ của xã cần đưa mọi người dân ra khỏi vùng ngập bằng những chiếc thuyền nhỏ. Mỗi thuyền chở được tối đa hai người và tổng cân nặng trên thuyền không được vượt quá giới hạn an toàn, nếu không thuyền sẽ lật giữa dòng nước xiết. Trưởng đội muốn ghép người dân lên các thuyền sao cho số thuyền cần dùng là ít nhất, để toàn bộ bà con được đưa đến nơi an toàn trong thời gian ngắn nhất trước khi nước dâng cao thêm.

## Nhiệm vụ

Cho $N$ số nguyên là cân nặng của từng người và giới hạn $limit$ của mỗi thuyền (mỗi thuyền chở tối đa hai người). Hãy lập trình ghép người lên thuyền sao cho số thuyền dùng ít nhất, rồi in ra số thuyền đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ và số nguyên $limit$ ($1 \le N \le 10^5$, $1 \le limit \le 10^9$), là số người và giới hạn mỗi thuyền.
- Dòng thứ hai chứa $N$ số nguyên $w_i$ ($1 \le w_i \le limit$), là cân nặng của từng người.

## Output

- In ra một số nguyên duy nhất là số thuyền ít nhất cần dùng.

## Sample 1

### Input

```text
4 5
1 2 3 4
```

### Output

```text
2
```

### Giải thích

- Sắp xếp cân nặng tăng dần: $1, 2, 3, 4$.
- Ghép người nhẹ nhất ($1$) với người nặng nhất ($4$): tổng $1 + 4 = 5$ vừa đúng giới hạn nên họ đi chung một thuyền.
- Hai người còn lại ($2$ và $3$) có tổng $2 + 3 = 5$ cũng vừa đúng giới hạn nên đi chung thuyền thứ hai.
- Tất cả bốn người chỉ cần $2$ thuyền và không thể ít hơn vì mỗi thuyền chở tối đa hai người.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le limit \le 10^9$, $1 \le w_i \le limit$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
