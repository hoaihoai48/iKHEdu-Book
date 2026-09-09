# Tính tiền mua vở có chương trình khuyến mãi

## Bối cảnh
Đầu năm học mới, một nhà sách tổ chức chương trình khuyến mãi đặc biệt cho học sinh: Mỗi quyển vở có giá niêm yết là $P$ đồng. Cứ mỗi khi khách hàng mua $5$ quyển vở thì sẽ được tặng thêm $1$ quyển vở hoàn toàn miễn phí. Bạn Nam cần có đúng $N$ quyển vở để phục vụ việc ghi chép các môn học. Bạn hãy tính xem Nam cần trả ít nhất bao nhiêu tiền để có đủ $N$ quyển vở.

## Nhiệm vụ
Cho hai số nguyên dương $N$ (số quyển vở Nam cần có) và $P$ (giá niêm yết một quyển vở). Hãy lập trình tính và in ra số tiền tối thiểu mà Nam phải thanh toán.

## Input
- Một dòng duy nhất chứa hai số nguyên dương $N$ và $P$ ($1 \le N \le 10^9, 1 \le P \le 10^6$), cách nhau bởi một khoảng trắng.

## Output
- In ra một số nguyên duy nhất là số tiền tối thiểu Nam cần thanh toán.

## Sample 1
### Input
```text
13 5000
```
### Output
```text
55000
```

### Giải thích
Nam cần có $13$ quyển vở:

- Cứ mỗi nhóm $6$ quyển (gồm mua $5$ tặng $1$), Nam chỉ cần trả tiền cho $5$ quyển.
- Với $13$ quyển, Nam có thể chia thành: $2$ nhóm $6$ quyển (được $12$ quyển, trong đó mua $10$ tặng $2$) và còn thiếu $1$ quyển cần mua thêm.
- Tổng số quyển Nam phải trả tiền là: $2 \times 5 + 1 = 11$ quyển.
- Số tiền thanh toán: $11 \times 5000 = 55000$ đồng.

## Sample 2
### Input
```text
5 6000
```
### Output
```text
30000
```

### Giải thích
Nam mua đúng $5$ quyển (chưa đủ 6 quyển để nhận quà tặng kèm lúc lấy), cần thanh toán $5 \times 6000 = 30000$ đồng (Nam sẽ nhận thêm 1 quyển quà tặng là 6 quyển, vẫn thỏa mãn có đủ ít nhất 5 quyển).

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^9, 1 \le P \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
