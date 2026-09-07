# Tìm phần tử kế tiếp nhỏ nhất lớn hơn x

## Bối cảnh

Kho hàng của siêu thị lưu các mức giá niêm yết khác nhau của cùng một mặt hàng qua các đợt khuyến mãi, mỗi mức giá chỉ ghi nhận một lần. Nhân viên muốn tìm mức giá nhỏ nhất trong kho mà vẫn lớn hơn một ngưỡng cho trước. Hệ thống cần trả lời nhanh nhiều lượt hỏi như vậy trong ngày để quầy thu ngân không bị ùn tắc vào giờ cao điểm.

## Nhiệm vụ

Cho $N$ số nguyên phân biệt là các mức giá trong kho và $Q$ truy vấn, mỗi truy vấn cho một ngưỡng $x$. Với mỗi truy vấn, hãy lập trình tìm mức giá nhỏ nhất trong kho mà lớn hơn $x$, rồi in ra giá đó. Nếu không có thì in ra $-1$.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, Q$ ($1 \le N, Q \le 10^5$), là số mức giá và số truy vấn.
- Dòng thứ hai chứa $N$ số nguyên phân biệt $a_i$ ($1 \le a_i \le 10^9$), là các mức giá.
- $Q$ dòng tiếp theo, mỗi dòng chứa một số nguyên $x$ ($0 \le x \le 10^9$), là ngưỡng của một truy vấn.

## Output

- In ra $Q$ dòng, mỗi dòng là đáp án của một truy vấn ($-1$ nếu không tồn tại).

## Sample 1

### Input

```text
5 3
1 5 3 7 2
4
7
0
```

### Output

```text
5
-1
1
```

### Giải thích

- Kho có các mức giá $1, 5, 3, 7, 2$.
- Ngưỡng $4$: các mức giá lớn hơn $4$ là $5$ và $7$, nhỏ nhất trong đó là $5$.
- Ngưỡng $7$: không có mức giá nào lớn hơn $7$ nên đáp án $-1$.
- Ngưỡng $0$: mọi mức giá đều lớn hơn $0$, nhỏ nhất là $1$.

## Ràng buộc

- $1 \le N, Q \le 10^5$, các $a_i$ phân biệt, $1 \le a_i \le 10^9$, $0 \le x \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
