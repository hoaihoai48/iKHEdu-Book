# Truy vấn tổng đoạn Fenwick Tree

## Bối cảnh

Kho hàng của siêu thị mini có $n$ kệ đựng gạo, mỗi kệ chứa một số bao nhất định. Cuối ngày, thủ kho thường xuyên nhập thêm bao gạo lên một kệ nào đó, đồng thời quản lý hay hỏi tổng số bao gạo trên một dãy kệ liên tiếp để đối chiếu sổ sách. Vì số kệ rất nhiều và thao tác diễn ra liên tục, thủ kho cần một chương trình trả lời nhanh từng yêu cầu. Em hãy giúp chú thủ kho ghi nhận hàng hóa chính xác mà không phải cộng tay từng kệ mỗi lần kiểm kê.

## Nhiệm vụ

Cho mảng $A$ gồm $n$ số nguyên và $q$ thao tác. Hãy lập trình xử lý từng thao tác theo thứ tự: với thao tác loại $1$, cộng thêm một lượng vào một vị trí; với thao tác loại $2$, tính tổng các phần tử trên một đoạn liên tiếp.

## Input

- Dòng 1: hai số nguyên $n, q$ ($1 \le n, q \le 2 \times 10^5$).
- Dòng 2: $n$ số nguyên $A_1, A_2, \dots, A_n$ ($|A_i| \le 10^9$).
- $q$ dòng tiếp theo, mỗi dòng mô tả một thao tác:
  - `1 idx val`: cộng thêm $val$ ($|val| \le 10^9$) vào $A[idx]$ ($1 \le idx \le n$).
  - `2 l r`: yêu cầu tính tổng $A[l] + A[l+1] + \dots + A[r]$ ($1 \le l \le r \le n$).

## Output

- Với mỗi thao tác loại $2$, in ra tổng của đoạn được hỏi trên một dòng.

## Sample 1

### Input

```text
5 3
1 2 3 4 5
2 1 5
1 3 2
2 1 5
```

### Output

```text
15
17
```

### Giải thích

Mảng ban đầu là $[1, 2, 3, 4, 5]$. Thao tác đầu hỏi tổng từ vị trí $1$ đến $5$: $1 + 2 + 3 + 4 + 5 = 15$ nên in ra $15$. Thao tác tiếp cộng thêm $2$ vào vị trí $3$, mảng thành $[1, 2, 5, 4, 5]$. Thao tác cuối hỏi lại tổng từ vị trí $1$ đến $5$: $1 + 2 + 5 + 4 + 5 = 17$ nên in ra $17$.

## Ràng buộc

- $1 \le n, q \le 2 \times 10^5$, $|A_i| \le 10^9$, $|val| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
