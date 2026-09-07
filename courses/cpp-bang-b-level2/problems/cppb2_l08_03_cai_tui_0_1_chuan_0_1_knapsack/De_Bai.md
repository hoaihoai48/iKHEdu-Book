# Cái túi 0/1 chuẩn (0/1 knapsack)

## Bối cảnh

Bạn Lan chuẩn bị ba lô cho chuyến leo núi hai ngày cùng câu lạc bộ, nhưng chiếc ba lô của bạn chỉ chịu được một khối lượng giới hạn. Trước mặt bạn là nhiều món đồ dùng, mỗi món có khối lượng và mức độ hữu ích khác nhau, và mỗi món chỉ có đúng một cái nên hoặc mang theo hoặc để ở nhà. Bạn muốn chọn những món bỏ vào ba lô sao cho tổng khối lượng không vượt quá sức chịu mà tổng mức hữu ích là cao nhất.

## Nhiệm vụ

Cho sức chứa $W$ của ba lô và $N$ món đồ, mỗi món có khối lượng $w_i$ và giá trị $v_i$ (mỗi món lấy tối đa một lần). Hãy lập trình chọn các món sao cho tổng khối lượng không vượt quá $W$ và tổng giá trị lớn nhất, rồi in ra tổng giá trị đó.

## Input

- Dòng đầu tiên chứa số nguyên $N$ và số nguyên $W$ ($1 \le N \le 100$, $1 \le W \le 10^4$), là số món đồ và sức chứa của ba lô.
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $w_i, v_i$ ($1 \le w_i \le W$, $1 \le v_i \le 10^6$), là khối lượng và giá trị của một món.

## Output

- In ra một số nguyên duy nhất là tổng giá trị lớn nhất.

## Sample 1

### Input

```text
4 7
1 1
3 4
4 5
5 7
```

### Output

```text
9
```

### Giải thích

- Ba lô chịu được $7$ đơn vị khối lượng với bốn món $(1, 1)$, $(3, 4)$, $(4, 5)$, $(5, 7)$.
- Chọn món $(3, 4)$ và món $(4, 5)$: tổng khối lượng $3 + 4 = 7$ vừa khít, tổng giá trị $4 + 5 = 9$.
- Mọi cách chọn khác đều cho tổng giá trị nhỏ hơn: lấy món $(5, 7)$ thì chỉ còn chỗ cho món $(1, 1)$ được $8$; các cách còn lại đều dưới $9$.

## Ràng buộc

- $1 \le N \le 100$, $1 \le W \le 10^4$, $1 \le w_i \le W$, $1 \le v_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
