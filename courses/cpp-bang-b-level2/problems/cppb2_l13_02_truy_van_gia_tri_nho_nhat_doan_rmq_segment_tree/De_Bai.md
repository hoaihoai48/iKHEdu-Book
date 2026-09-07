# Truy vấn giá trị nhỏ nhất đoạn (Segment Tree)

## Bối cảnh

Trạm quan trắc môi trường đặt N cảm biến dọc con sông để đo nồng độ chất gây ô nhiễm theo thời gian thực phục vụ cảnh báo lũ và sự cố tràn dầu. Mỗi giờ kỹ thuật viên hiệu chuẩn lại một cảm biến làm giá trị của nó thay đổi, đồng thời trung tâm cần biết mức thấp nhất trên từng đoạn sông để đánh giá vùng nước sạch. Hệ thống dùng cây đoạn để vừa cập nhật điểm vừa truy vấn giá trị nhỏ nhất trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ thao tác. Hãy lập trình xử lý hai loại thao tác: loại $1$ gán $a[idx] = val$; loại $2$ in ra giá trị nhỏ nhất trên đoạn $[l, r]$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo: thao tác loại $1$ gồm $1\ idx\ val$; thao tác loại $2$ gồm $2\ l\ r$ ($1 \le idx, l \le r \le N$).

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là giá trị nhỏ nhất trên đoạn yêu cầu.

## Sample 1

### Input

```text
5 3
5 3 1 4 2
2 1 5
1 3 6
2 1 5
```

### Output

```text
1
2
```

### Giải thích

- Mảng ban đầu $5\ 3\ 1\ 4\ 2$: giá trị nhỏ nhất toàn mảng là $1$ ở vị trí $3$.
- Gán $a[3] = 6$ được mảng $5\ 3\ 6\ 4\ 2$: giá trị nhỏ nhất toàn mảng còn $2$.
- Hai truy vấn loại $2$ in ra $1$ rồi $2$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i|, |val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
