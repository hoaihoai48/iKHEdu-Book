# Sắp Xếp Lưu Vị Trí Ban Đầu

## Bối cảnh
Trong một cuộc thi marathon tiếp sức, ban tổ chức gắn chip định vị ghi nhận tốc độ chạy trung bình của $N$ vận động viên. Mỗi vận động viên xuất phát từ một vị trí tương ứng với số thứ tự đăng ký ban đầu từ $1$ đến $N$, với tốc độ đạt được lần lượt là $A_1, A_2, \dots, A_N$. Để phục vụ công tác xếp hạng phân loại và trao huy chương sau chặng đua, ban trọng tài cần sắp xếp lại các vận động viên theo thứ tự tốc độ tăng dần, đồng thời phải truy vết chính xác số thứ tự xuất phát ban đầu của từng người. Nếu có hai vận động viên đạt cùng một mức tốc độ, người nào xuất phát trước (có số thứ tự ban đầu nhỏ hơn) sẽ được xếp đứng trước.

## Nhiệm vụ
Cho một dãy gồm $N$ số nguyên $A_1, A_2, \dots, A_N$. Hãy sắp xếp các phần tử theo thứ tự giá trị tăng dần, đồng thời in ra giá trị và vị trí ban đầu (chỉ số 1-indexed) của mỗi phần tử trong mảng gốc. Nếu hai phần tử có cùng giá trị, phần tử xuất hiện trước trong mảng gốc sẽ đứng trước.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$) — số lượng phần tử.
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$) — giá trị của các phần tử.

## Output
- In ra $N$ dòng, mỗi dòng gồm 2 số nguyên cách nhau bởi khoảng trắng: số đầu tiên là giá trị phần tử sau khi sắp xếp, số thứ hai là chỉ số ban đầu của nó trong mảng gốc.

## Sample 1
### Input
```text
5
40 10 20 10 30
```
### Output
```text
10 2
10 4
20 3
30 5
40 1
```
### Giải thích
Dãy ban đầu cùng vị trí gốc (1-indexed) là:

- Vị trí 1: $40$
- Vị trí 2: $10$
- Vị trí 3: $20$
- Vị trí 4: $10$
- Vị trí 5: $30$

Sau khi sắp xếp theo giá trị tăng dần:

- Giá trị $10$: có ở vị trí 2 và vị trí 4. Vì $2 < 4$ nên in `10 2` trước, sau đó in `10 4`.
- Giá trị $20$: ở vị trí 3 $\implies$ in `20 3`.
- Giá trị $30$: ở vị trí 5 $\implies$ in `30 5`.
- Giá trị $40$: ở vị trí 1 $\implies$ in `40 1`.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, \vert A_i \vert \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
