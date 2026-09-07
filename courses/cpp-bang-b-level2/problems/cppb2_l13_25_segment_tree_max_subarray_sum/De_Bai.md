# Tổng đoạn con lớn nhất có cập nhật điểm

## Bối cảnh

Sàn giao dịch hàng hoá phái sinh theo dõi N mức biến động giá theo từng phiên, số dương là lãi và số âm là lỗ so với giá tham chiếu đầu ngày. Mỗi khi số liệu một phiên được hiệu chỉnh do khớp lệnh muộn, chuyên viên phân tích muốn biết ngay chuỗi phiên liên tiếp có tổng biến động lớn nhất để khuyến nghị thời điểm nắm giữ. Cây đoạn hợp nhất bốn thông tin mỗi nút giúp duy trì đáp án sau mỗi lần cập nhật trong thời gian logarit.

## Nhiệm vụ

Cho mảng $a_1, \dots, a_N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ gán $a[idx] = val$; loại $2$ in ra tổng lớn nhất của một đoạn con liên tiếp nằm trong $[l,r]$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số nguyên $a_i$ ($|a_i| \le 10^9$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ idx\ val$; loại $2$ gồm $2\ l\ r$.

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là đáp án của truy vấn tương ứng.

## Sample 1

### Input

```text
4 3
1 -2 3 4
2 1 4
1 2 5
2 1 4
```

### Output

```text
7
13
```

### Giải thích

- Mảng $1\ -2\ 3\ 4$: đoạn tốt nhất là $3 + 4 = 7$.
- Gán $a[2] = 5$ được $1\ 5\ 3\ 4$ toàn số dương nên tổng tốt nhất là $1+5+3+4 = 13$.
- Hai thao tác loại $2$ in ra $7$ rồi $13$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|a_i|, |val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
