# Duy trì tổng của k phần tử lớn nhất động

## Bối cảnh

Phòng kinh doanh theo dõi doanh thu của từng cửa hàng trong chuỗi theo thời gian thực, mỗi khi có cửa hàng mới khai trương thì con số của nó được thêm vào danh sách. Sau mỗi lần thêm, giám đốc muốn biết ngay tổng doanh thu của $K$ cửa hàng tốt nhất tính đến lúc đó: nếu chưa đủ $K$ cửa hàng thì cộng tất cả những gì đang có. Con số cập nhật liên tục này giúp ban lãnh đạo quyết định có nên mở thêm chi nhánh mới hay không.

## Nhiệm vụ

Cho số nguyên $K$ và $N$ số nguyên đến lần lượt theo thời gian. Sau mỗi số vừa đến, lấy ra tối đa $K$ số lớn nhất trong các số đã thấy và tính tổng của chúng. Hãy lập trình in ra tổng này sau mỗi lần thêm một số.

## Input

- Dòng đầu tiên chứa hai số nguyên $N, K$ ($1 \le K \le N \le 10^5$), là số cửa hàng và quy mô tốp đầu.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là doanh thu từng cửa hàng theo thứ tự.

## Output

- In ra $N$ dòng, dòng thứ $i$ là tổng của tối đa $K$ số lớn nhất trong $i$ số đầu tiên.

## Sample 1

### Input

```text
5 3
1 5 3 7 2
```

### Output

```text
1
6
9
15
15
```

### Giải thích

- Sau số đầu ($1$): chỉ có một số nên tổng là $1$.
- Sau hai số ($1, 5$): cả hai đều thuộc tốp nên tổng là $1 + 5 = 6$.
- Sau ba số ($1, 5, 3$): tốp $3$ gồm $5, 3, 1$, tổng là $9$.
- Sau bốn số ($1, 5, 3, 7$): tốp $3$ gồm $7, 5, 3$, tổng là $15$.
- Sau năm số ($1, 5, 3, 7, 2$): tốp $3$ vẫn gồm $7, 5, 3$, tổng là $15$.

## Ràng buộc

- $1 \le K \le N \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
