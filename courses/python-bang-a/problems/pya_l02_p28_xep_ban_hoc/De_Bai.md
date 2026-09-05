# Xếp hàng vào bàn học

## Bối cảnh
Phòng thi Olympic Tin học cấp thành phố được bố trí toàn bộ bàn đôi — mỗi bàn ngồi đúng 2 thí sinh. Năm nay có $N$ thí sinh đăng ký dự thi. Ban tổ chức cần tính toán số lượng bàn tối thiểu phải chuẩn bị sao cho tất cả thí sinh đều có chỗ ngồi, kể cả trường hợp số thí sinh là số lẻ thì bàn cuối cùng vẫn phải kê ra dù chỉ ngồi 1 người.


## Nhiệm vụ
Có $N$ bạn thí sinh. Hỏi cần ít nhất bao nhiêu bàn đôi để tất cả các bạn đều có chỗ ngồi? (Nếu lẻ 1 bạn vẫn cần thêm 1 bàn).

## Input
Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
In ra số bàn học tối thiểu cần dùng.

## Sample 1
### Input
```text
15
```
### Output
```text
8
```
### Giải thích
15 bạn xếp được 7 bàn đôi đầy đủ, còn 1 bạn ngồi riêng 1 bàn $\implies$ Cần 8 bàn. Công thức: `(N + 1) // 2`.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
