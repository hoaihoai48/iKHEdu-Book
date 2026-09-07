# Tối ưu hóa chi phí mua cổ phiếu theo thời gian

## Bối cảnh

Thủ kho của cửa hàng linh kiện quản lý các lô hàng cùng một mã sản phẩm nhập về ở nhiều thời điểm khác nhau, mỗi lô được dán nhãn một mã số. Trong ngày, thủ kho thực hiện nhiều thao tác: nhập thêm một lô có mã $x$, xuất đi một lô có mã $x$ (nếu còn), hoặc kiểm kê xem hiện còn bao nhiêu lô mang mã $x$ trong kho. Vì số thao tác lên tới hàng chục nghìn lượt, thủ kho cần một chương trình ghi nhận và trả lời kiểm kê tức thì.

## Nhiệm vụ

Cho $Q$ thao tác, mỗi thao tác gồm loại $type$ và mã $x$: loại $1$ là nhập một lô mã $x$, loại $2$ là xuất một lô mã $x$ (nếu kho còn), loại $3$ là hỏi hiện có bao nhiêu lô mã $x$. Hãy lập trình in ra đáp án của mỗi thao tác loại $3$ trên một dòng.

## Input

- Dòng đầu tiên chứa số nguyên $Q$ ($1 \le Q \le 10^5$), là số thao tác.
- $Q$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $type, x$ ($1 \le type \le 3$, $1 \le x \le 10^9$), mô tả một thao tác.

## Output

- Mỗi dòng in ra đáp án của một thao tác loại $3$.

## Sample 1

### Input

```text
6
1 5
1 3
1 5
3 5
2 5
3 5
```

### Output

```text
2
1
```

### Giải thích

- Nhập lô mã $5$, nhập lô mã $3$, nhập thêm lô mã $5$ thì kho có hai lô mã $5$.
- Hỏi mã $5$ được đáp án $2$; xuất đi một lô mã $5$ thì kho còn một lô mã $5$.
- Hỏi lại mã $5$ được đáp án $1$.

## Ràng buộc

- $1 \le Q \le 10^5$, $1 \le type \le 3$, $1 \le x \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
