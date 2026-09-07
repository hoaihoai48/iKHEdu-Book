# Duyệt tất cả submask tính tổng phân hoạch

## Bối cảnh

Câu lạc bộ văn nghệ của trường muốn lập mọi đội hình biểu diễn có thể từ danh sách thành viên đăng ký, từ đội rỗng cho đến đội gồm tất cả mọi người. Mỗi bạn có một điểm tài năng riêng, và điểm của một đội hình bằng tổng điểm của các thành viên trong đội. Để ước tính tổng số tiết mục mà câu lạc bộ có thể dàn dựng trong cả năm, ban chủ nhiệm cần cộng dồn điểm số của tất cả các đội hình con có thể lập được, kể cả đội rỗng.

## Nhiệm vụ

Cho $N$ số nguyên là điểm tài năng của từng thành viên. Hãy lập trình tính tổng điểm của tất cả các đội hình con (mọi tập con của danh sách, kể cả tập rỗng có tổng bằng $0$), rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 20$), là số thành viên.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($0 \le a_i \le 10^6$), là điểm tài năng của từng bạn.

## Output

- In ra một số nguyên duy nhất là tổng điểm của mọi tập con.

## Sample 1

### Input

```text
3
1 2 3
```

### Output

```text
24
```

### Giải thích

- Liệt kê cả $8$ đội hình con cùng tổng điểm của từng đội.
- Đội rỗng có tổng $0$; các đội một người có tổng $1$, $2$, $3$.
- Các đội hai người $\{1, 2\}$, $\{1, 3\}$, $\{2, 3\}$ có tổng $3$, $4$, $5$.
- Đội ba người $\{1, 2, 3\}$ có tổng $6$.
- Cộng dồn tất cả: $0 + 1 + 2 + 3 + 3 + 4 + 5 + 6 = 24$.

## Ràng buộc

- $1 \le N \le 20$, $0 \le a_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
