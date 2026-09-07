# Sắp đặt chuỗi ký tự không trùng lặp kề nhau

## Bối cảnh

Cô giáo mầm non chuẩn bị một bộ thẻ chữ cái để xếp thành hàng trang trí lớp học nhân ngày hội đọc sách. Trong túi có nhiều chữ cái khác nhau với số lượng mỗi loại đã đếm sẵn, và cô muốn xếp toàn bộ thẻ thành một hàng dài sao cho không có hai thẻ giống nhau nào đứng cạnh nhau, vì như vậy hàng chữ trông sẽ đều và đẹp mắt hơn. Trước khi bắt tay vào xếp, cô cần biết liệu với số thẻ hiện có thì cách xếp như vậy có tồn tại hay không.

## Nhiệm vụ

Cho một chuỗi $s$ gồm các chữ cái thường. Hãy lập trình sắp xếp lại các ký tự của $s$ thành một chuỗi mới sao cho không có hai ký tự giống nhau nào đứng kề nhau. In ra chuỗi tìm được, hoặc in ra $-1$ nếu không thể.

## Input

- Dòng đầu tiên chứa chuỗi $s$ ($1 \le |s| \le 10^5$) gồm các chữ cái thường `a` đến `z`.

## Output

- In ra một chuỗi là hoán vị của $s$ mà không có hai ký tự kề nhau trùng nhau, hoặc $-1$ nếu không tồn tại.

## Sample 1

### Input

```text
aab
```

### Output

```text
aba
```

### Giải thích

- Chuỗi ban đầu có hai chữ `a` và một chữ `b`.
- Đặt chữ `a` đầu tiên, còn lại một `a` và một `b`.
- Đặt chữ `b` tiếp theo vì vừa dùng `a` xong, còn lại một `a`.
- Đặt chữ `a` cuối cùng, được chuỗi `aba` mà không có hai ký tự kề nhau nào trùng nhau.

## Ràng buộc

- $1 \le |s| \le 10^5$, $s$ chỉ gồm chữ cái thường.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
