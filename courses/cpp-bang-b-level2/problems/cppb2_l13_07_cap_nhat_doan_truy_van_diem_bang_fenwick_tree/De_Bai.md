# Cập nhật đoạn, truy vấn điểm (Fenwick)

## Bối cảnh

Ban quản lý chợ đầu mối áp dụng chính sách trợ giá theo đợt cho N sạp hàng nằm liên tiếp nhau để bình ổn giá nông sản trong mùa mưa bão. Mỗi đợt hỗ trợ cộng thêm một khoản tiền vào tất cả các sạp trong một đoạn liên tiếp, và cuối ngày chủ từng sạp muốn biết tổng số tiền mình được nhận sau nhiều đợt dồn lại. Cây Fenwick hiệu đoạn giúp cộng cả đoạn trong logarit và đọc giá trị từng điểm cũng trong logarit.

## Nhiệm vụ

Cho $N$ và $Q$ thao tác. Hãy lập trình xử lý: loại $1$ cộng $val$ vào mọi phần tử trên đoạn $[l,r]$; loại $2$ in ra giá trị hiện tại của $a[idx]$. Ban đầu mọi phần tử bằng $0$.

## Input

- Dòng 1: hai số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: loại $1$ gồm $1\ l\ r\ val$; loại $2$ gồm $2\ idx$ ($|val| \le 10^9$).

## Output

- Với mỗi thao tác loại $2$, in ra một dòng là giá trị tại vị trí yêu cầu.

## Sample 1

### Input

```text
5 4
1 1 3 10
1 2 5 5
2 2
2 4
```

### Output

```text
15
5```

### Giải thích

- Cộng $10$ vào đoạn $[1,3]$ rồi cộng $5$ vào đoạn $[2,5]$.
- Vị trí $2$ nhận cả hai đợt nên bằng $10 + 5 = 15$; vị trí $4$ chỉ nhận đợt sau nên bằng $5$.
- Hai truy vấn loại $2$ in ra $15$ rồi $5$ trên hai dòng.

## Ràng buộc

- $1 \le N, Q \le 2 \cdot 10^5$; $|val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
