# Đếm tần suất giá trị bằng safe hash map

## Bối cảnh

Thư viện trường vừa nhận về một đợt sách mới gồm $N$ cuốn thuộc nhiều thể loại khác nhau, mỗi cuốn được đóng dấu một mã thể loại. Trước khi xếp sách lên kệ, cô thủ thư muốn thống kê mỗi thể loại có bao nhiêu cuốn để phân bổ ngăn kệ cho hợp lý: thể loại nào nhiều sách thì dành ngăn to, thể loại ít thì ghép chung. Bảng thống kê liệt kê các mã thể loại theo thứ tự xuất hiện lần đầu cùng với số lượng của từng loại.

## Nhiệm vụ

Cho $N$ số nguyên là mã thể loại của từng cuốn sách theo thứ tự nhập kho. Hãy lập trình đếm số lần xuất hiện của mỗi giá trị phân biệt, rồi in ra từng giá trị cùng tần suất của nó theo thứ tự xuất hiện lần đầu trong dãy.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số cuốn sách.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($-10^9 \le a_i \le 10^9$), là mã thể loại từng cuốn.

## Output

- Mỗi dòng in ra hai số nguyên `v c`, trong đó $v$ là một giá trị phân biệt và $c$ là số lần nó xuất hiện, theo thứ tự xuất hiện lần đầu của $v$ trong dãy.

## Sample 1

### Input

```text
6
1 2 1 3 2 1
```

### Output

```text
1 3
2 2
3 1
```

### Giải thích

- Đọc dãy từ trái sang: số $1$ xuất hiện đầu tiên ở vị trí đầu, số $2$ xuất hiện đầu tiên ở vị trí thứ hai, số $3$ xuất hiện đầu tiên ở vị trí thứ tư.
- Đếm trong cả dãy: số $1$ gặp $3$ lần, số $2$ gặp $2$ lần, số $3$ gặp $1$ lần.
- In ra theo thứ tự xuất hiện lần đầu: `1 3`, `2 2`, `3 1`.

## Ràng buộc

- $1 \le N \le 10^5$, $-10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
