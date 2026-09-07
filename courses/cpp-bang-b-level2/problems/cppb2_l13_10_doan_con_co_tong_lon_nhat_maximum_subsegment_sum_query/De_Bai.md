# Tổng đoạn con lớn nhất có cập nhật điểm

## Bối cảnh

Trung tâm điều hành lưới điện ghi lại N mức chênh lệch công suất theo từng giờ, số dương nghĩa là dư điện và số âm nghĩa là thiếu điện cần mua ngoài. Mỗi khi số liệu một giờ được hiệu chỉnh, kỹ sư trực muốn biết ngay chuỗi giờ liên tiếp có tổng chênh lệch lớn nhất trên toàn lưới để quyết định thời điểm xả蓄 tích năng. Cây đoạn có cập nhật điểm giúp duy trì đáp án tốt nhất sau mỗi lần hiệu chỉnh trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ gán $a[idx] = val$; loại $2$ in ra tổng lớn nhất của một đoạn con liên tiếp trên toàn mảng.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ idx\ val$; loại $2$ gồm một số $2$.

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là tổng đoạn con lớn nhất hiện tại.

## Sample 1

### Input

```text
4 3
1 -2 3 4
2
1 2 5
2
```

### Output

```text
7
13```

### Giải thích

- Mảng $1\ -2\ 3\ 4$: đoạn tốt nhất là $3 + 4 = 7$ (lấy thêm $1, -2$ chỉ làm giảm tổng).
- Gán $a[2] = 5$ được $1\ 5\ 3\ 4$: cả bốn số đều dương nên tổng tốt nhất là $1+5+3+4 = 13$.
- Hai thao tác loại $2$ in ra $7$ rồi $13$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i|, |val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
