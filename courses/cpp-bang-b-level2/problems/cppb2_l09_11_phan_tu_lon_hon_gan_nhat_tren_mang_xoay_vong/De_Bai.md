# Phần tử lớn hơn gần nhất trên mảng xoay vòng

## Bối cảnh

Các gian hàng hội chợ được xếp thành một vòng tròn khép kín quanh sân vận động, mỗi gian có một chiều cao biển hiệu khác nhau. Ban tổ chức muốn với mỗi gian hàng, tìm ra gian hàng gần nhất khi đi theo chiều kim đồng hồ (được đi vòng qua điểm xuất phát) mà có biển hiệu cao hơn gian đang xét, để đặt nhờ bảng chỉ đường sang gian nổi bật bên cạnh. Gian nào mà đi hết vòng tròn cũng không gặp biển hiệu nào cao hơn thì đành tự treo bảng chỉ đường riêng.

## Nhiệm vụ

Cho $N$ số nguyên xếp thành vòng tròn (sau phần tử cuối là phần tử đầu). Với mỗi vị trí $i$, tìm phần tử lớn hơn $a_i$ gần nhất khi duyệt theo chiều kim đồng hồ (cho phép đi vòng). Hãy lập trình in ra $N$ giá trị tìm được theo thứ tự, vị trí nào không có thì in ra $-1$.

## Input

- Dòng đầu tiên chứa số nguyên $N$ ($1 \le N \le 10^5$), là số gian hàng.
- Dòng thứ hai chứa $N$ số nguyên $a_i$ ($1 \le a_i \le 10^9$), là chiều cao biển hiệu.

## Output

- In ra $N$ số nguyên trên một dòng là đáp án của từng vị trí ($-1$ nếu không tồn tại).

## Sample 1

### Input

```text
3
1 2 1
```

### Output

```text
2 -1 2
```

### Giải thích

- Gian cao $1$ đầu tiên nhìn sang phải gặp ngay gian cao $2$ nên đáp án là $2$.
- Gian cao $2$ đi hết vòng tròn chỉ gặp các gian cao $1$ và chính nó nên không có gian nào cao hơn, đáp án $-1$.
- Gian cao $1$ cuối cùng đi tiếp một bước vòng về gian đầu cao $1$ (không cao hơn), bước nữa gặp gian cao $2$ nên đáp án là $2$.

## Ràng buộc

- $1 \le N \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
