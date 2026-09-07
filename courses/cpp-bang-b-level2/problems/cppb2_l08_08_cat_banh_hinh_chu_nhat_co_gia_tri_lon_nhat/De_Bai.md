# Cắt bánh hình chữ nhật có giá trị lớn nhất

## Bối cảnh

Tiệm bánh của gia đình vừa nướng xong một khay bánh lớn hình chữ nhật kích thước $W \times H$ để bán trong dịp lễ. Cửa hàng có bảng giá cho nhiều cỡ miếng bánh nhỏ khác nhau, mỗi cỡ được mua với một giá tiền cố định và có thể xoay dọc hay ngang tùy ý. Người bán được cắt khay bánh lớn thành các miếng nhỏ (bằng các nhát cắt thẳng suốt tấm bánh) rồi bán từng miếng theo bảng giá. Tiệm muốn chọn cách cắt sao cho tổng số tiền thu được là cao nhất.

## Nhiệm vụ

Cho kích thước khay bánh $W \times H$ và $N$ loại miếng bánh, mỗi loại có kích thước $w \times h$ với giá bán $val$ (được xoay $90$ độ, mỗi loại dùng bao nhiêu miếng tùy ý). Hãy lập trình tính tổng số tiền lớn nhất có thể thu được từ khay bánh, rồi in ra tổng đó.

## Input

- Dòng đầu tiên chứa ba số nguyên $W, H, N$ ($1 \le W, H \le 200$, $0 \le N \le 100$), là kích thước khay và số loại miếng bánh.
- $N$ dòng tiếp theo, mỗi dòng chứa ba số nguyên $w, h, val$ ($1 \le w, h \le 200$, $1 \le val \le 10^6$), là kích thước và giá bán của một loại miếng.

## Output

- In ra một số nguyên duy nhất là tổng số tiền lớn nhất.

## Sample 1

### Input

```text
4 2 1
2 2 6
```

### Output

```text
12
```

### Giải thích

- Khay bánh $4 \times 2$ chỉ có một loại miếng $2 \times 2$ giá $6$.
- Cắt một nhát dọc giữa khay được hai miếng $2 \times 2$, mỗi miếng bán $6$.
- Tổng thu được $6 + 6 = 12$, và không có cách cắt nào cho nhiều hơn vì cả khay chỉ đủ chỗ cho hai miếng.

## Ràng buộc

- $1 \le W, H \le 200$, $0 \le N \le 100$, $1 \le w, h \le 200$, $1 \le val \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
