# Tìm số 1 thứ K trong dãy nhị phân

## Bối cảnh

Rạp chiếu phim thông minh quản lý N ghế ngồi bằng dãy bit, ghế trống ghi số 1 và ghế đã bán ghi số 0 để lễ tân tra cứu tức thì. Mỗi khi có khách mua hoặc trả vé, bit tương ứng được cập nhật ngay, và yêu cầu phổ biến là tìm vị trí ghế trống thứ K tính từ đầu rạp cho nhóm khách đi cùng nhau. Cây đoạn lưu tổng số ghế trống mỗi nút giúp vừa cập nhật điểm vừa nhảy tìm vị trí trong thời gian logarit.

## Nhiệm vụ

Cho dãy nhị phân độ dài $N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ gán bit tại $idx$ thành $val$ ($0$ hoặc $1$); loại $2$ in ra vị trí nhỏ nhất mà tổng số số $1$ từ đầu đến đó bằng $k$ (in ra $-1$ nếu không đủ).

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- Dòng 2: $N$ số $0/1$.
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ idx\ val$; loại $2$ gồm $2\ k$ ($1 \le k \le N$).

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là vị trí cần tìm hoặc $-1$.

## Sample 1

### Input

```text
5 3
1 0 1 1 0
2 2
1 2 1
2 3
```

### Output

```text
3
3
```

### Giải thích

- Dãy $1\ 0\ 1\ 1\ 0$: các số $1$ ở vị trí $1, 3, 4$ nên số $1$ thứ hai ở vị trí $3$.
- Cập nhật vị trí $2$ thành $1$ được dãy $1\ 1\ 1\ 1\ 0$: số $1$ thứ ba vẫn ở vị trí $3$.
- Hai truy vấn loại $2$ in ra $3$ rồi $3$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
