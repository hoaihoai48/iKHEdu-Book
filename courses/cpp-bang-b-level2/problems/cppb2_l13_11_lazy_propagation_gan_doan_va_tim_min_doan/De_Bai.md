# Gán đoạn và tìm min đoạn (lazy)

## Bối cảnh

Khu nghỉ dưỡng quản lý N phòng họp xếp liên tiếp nhau với mức giá thuê theo giờ được điều chỉnh đồng loạt theo từng khu vực vào mỗi mùa du lịch. Mỗi lần ban giám đốc gán lại cùng một mức giá cho cả đoạn phòng, lễ tân cần tra cứu nhanh mức giá thấp nhất trong bất kỳ đoạn nào để báo cho đoàn khách thương lượng. Cây đoạn lười gán đoạn giúp cả hai thao tác đều chạy trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ gán mọi phần tử trên $[l,r]$ thành $val$; loại $2$ in ra giá trị nhỏ nhất trên $[l,r]$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ l\ r\ val$; loại $2$ gồm $2\ l\ r$.

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là giá trị nhỏ nhất trên đoạn yêu cầu.

## Sample 1

### Input

```text
5 3
5 4 3 2 1
2 1 5
1 2 4 10
2 1 5
```

### Output

```text
1
1```

### Giải thích

- Mảng $5\ 4\ 3\ 2\ 1$: giá trị nhỏ nhất toàn mảng là $1$ ở cuối.
- Gán đoạn $[2,4]$ thành $10$ được $5\ 10\ 10\ 10\ 1$: giá trị nhỏ nhất toàn mảng vẫn là $1$ ở vị trí $5$.
- Hai truy vấn loại $2$ in ra $1$ rồi $1$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i|, |val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
