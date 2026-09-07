# Kỹ thuật small-to-large merging trên STL map

## Bối cảnh

Phòng kế toán của công ty quản lý các khoản thu theo từng mã dự án, mỗi khoản thu ghi một dòng gồm mã dự án và số tiền. Cuối tháng, phòng cần lập báo cáo gộp các khoản thu cùng mã lại với nhau: với mỗi mã dự án, báo cáo cho biết có bao nhiêu khoản thu và tổng số tiền là bao nhiêu. Các mã dự án được liệt kê theo thứ tự từ điển để giám đốc dễ đối chiếu với hợp đồng đã ký từ đầu năm.

## Nhiệm vụ

Cho $N$ cặp gồm mã dự án $key$ (chuỗi không dấu cách) và số tiền $val$. Hãy lập trình gộp các cặp có cùng mã: với mỗi mã phân biệt, đếm số khoản thu và tính tổng số tiền, rồi in ra theo thứ tự từ điển của mã.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số khoản thu.
- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi $key$ ($1 \le |key| \le 20$, không dấu cách) và một số nguyên $val$ ($1 \le val \le 10^6$), là mã dự án và số tiền.

## Output

- Mỗi dòng in ra theo dạng `key: Count=c, Sum=s`, trong đó $c$ là số khoản thu và $s$ là tổng số tiền của mã đó, theo thứ tự từ điển của $key$.

## Sample 1

### Input

```text
5
a 1
b 2
a 3
b 4
a 4
```

### Output

```text
a: Count=3, Sum=8
b: Count=2, Sum=6
```

### Giải thích

- Gom các khoản thu theo mã dự án: mã `a` có ba khoản $1, 3, 4$; mã `b` có hai khoản $2, 4$.
- Mã `a` cho tổng $1 + 3 + 4 = 8$ với $3$ khoản thu; mã `b` cho tổng $2 + 4 = 6$ với $2$ khoản thu.
- Sắp xếp hai mã theo thứ tự từ điển `a` trước `b` rồi in ra hai dòng báo cáo.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le |key| \le 20$, $1 \le val \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
