# Số Catalan đếm dãy ngoặc đúng

## Bối cảnh

Nhà xuất bản sách thiếu nhi cần kiểm định lô khuôn in dấu ngoặc dùng cho cuốn sách toán vui sắp phát hành toàn quốc. Mỗi mẫu khuôn gồm N cặp ngoặc đơn phải xếp thành một dãy đóng mở hợp lệ thì máy in mới không báo lỗi kẹt giấy. Tổ kỹ thuật muốn biết có bao nhiêu dãy ngoặc đúng khác nhau để đặt mua đủ mực in, lấy phần dư cho 1 000 000 007 vì số lượng mẫu tăng rất nhanh theo N.

## Nhiệm vụ

Cho số nguyên $N$. Hãy lập trình tính số Catalan thứ $N$, tức số dãy ngoặc đúng gồm $N$ cặp ngoặc đơn, rồi in ra phần dư khi chia cho $1\,000\,000\,007$.

## Input

- Dòng duy nhất: số nguyên $N$ ($0 \le N \le 10^6$).

## Output

- In ra một dòng duy nhất là $C_N \bmod 1\,000\,000\,007$.

## Sample 1

### Input

```text
4
```

### Output

```text
14
```

### Giải thích

- Với $N = 4$: số dãy ngoặc đúng gồm $4$ cặp ngoặc đơn.
- Liệt kê tay một vài dãy: $(()())$, $((()))$, $()()()$ đều hợp lệ và tổng cộng có $14$ dãy.
- Chương trình in ra $14$.

## Ràng buộc

- $0 \le N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
