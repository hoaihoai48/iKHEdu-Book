# Kiểm tra đồ thị hai phía (tô màu)

## Bối cảnh

Ban tổ chức giải cờ vua đồng đội cần xếp N kỳ thủ vào hai đội sao cho mọi cặp kỳ thủ từng hoà nhau ở vòng loại đều nằm khác đội để trận chung kết thêm kịch tính. Danh sách M cặp từng gặp nhau được ghi lại đầy đủ, và ban tổ chức muốn biết liệu cách chia hai đội như mong muốn có tồn tại hay không. Chương trình cần trả lời YES khi xếp được và NO khi có mâu thuẫn không thể hoá giải.

## Nhiệm vụ

Cho đồ thị vô hướng gồm $N$ đỉnh và $M$ cạnh. Hãy lập trình kiểm tra đồ thị có phải là đồ thị hai phía bằng thuật toán tô màu hai màu, rồi in ra $YES$ nếu đúng và $NO$ nếu sai.

## Input

- Dòng 1: hai số nguyên $N, M$ ($1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$).
- $M$ dòng tiếp theo, mỗi dòng gồm $u, v$ là một cạnh hai chiều.

## Output

- In ra một dòng duy nhất: $YES$ nếu đồ thị hai phía, ngược lại $NO$.

## Sample 1

### Input

```text
3 2
1 2
2 3
```

### Output

```text
YES```

### Giải thích

- Đồ thị là đường $1-2-3$: tô đỉnh $1$ màu đỏ thì đỉnh $2$ phải màu xanh, đỉnh $3$ lại màu đỏ.
- Không có cạnh nào nối hai đỉnh cùng màu nên phép tô màu thành công.
- Chương trình in ra $YES$.

## Ràng buộc

- $1 \le N \le 10^5$, $0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
