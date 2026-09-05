# Tính số chuyến xe cần thiết

## Bối cảnh
Trường trung học cơ sở Ngôi Sao Sáng tổ chức chuyến dã ngoại tham quan bảo tàng cho $N$ học sinh. Nhà trường thuê xe khách loại nhỏ, mỗi xe chở tối đa $K$ em. Ban tổ chức cần tính chính xác số xe tối thiểu phải thuê sao cho tất cả học sinh đều có chỗ ngồi, kể cả khi xe cuối cùng không chở đủ $K$ em vẫn phải thuê nguyên chiếc.


## Nhiệm vụ
Nhập hai số nguyên dương $N$ và $K$ trên 1 dòng. In ra số lượng xe tối thiểu cần thuê để chở hết tất cả học sinh.

## Input
Một dòng chứa hai số nguyên dương $N, K$ ($1 \le N, K \le 10^9$).

## Output
In ra số xe tối thiểu.

## Sample 1
### Input
```text
41 10
```
### Output
```text
5
```
### Giải thích
4 xe chở được 40 em, còn 1 em vẫn cần thêm 1 xe nữa $\implies$ Cần 5 xe. Công thức làm tròn lên chuẩn: `(N + K - 1) // K`.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
