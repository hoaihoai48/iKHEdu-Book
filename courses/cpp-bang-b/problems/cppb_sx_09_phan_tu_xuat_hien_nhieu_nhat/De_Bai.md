# Tìm Phần Tử Xuất Hiện Nhiều Nhất

## Bối cảnh
Trong một đợt khảo sát ý kiến bình chọn sản phẩm được yêu thích nhất của một trang thương mại điện tử, ban tổ chức thu thập được $N$ phiếu bầu có mã định danh sản phẩm lần lượt là $A_1, A_2, \dots, A_N$. Ban tổ chức cần công bố sản phẩm chiến thắng — tức sản phẩm nhận được số lượng phiếu bầu nhiều nhất. Trong trường hợp có nhiều sản phẩm cùng đạt được số phiếu bầu cao nhất, ban tổ chức sẽ ưu tiên trao giải cho sản phẩm có mã số định danh nhỏ nhất.

## Nhiệm vụ
Cho danh sách $N$ số nguyên đại diện cho các mã phiếu bầu. Hãy tìm phần tử có tần suất xuất hiện nhiều nhất trong dãy. Nếu có nhiều phần tử có cùng tần suất cực đại, hãy in ra phần tử có giá trị nhỏ nhất cùng với số lần xuất hiện của nó.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$) — số lượng phiếu bầu.
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$) — danh sách mã phiếu bầu.

## Output
- In ra hai số nguyên cách nhau bởi khoảng trắng: số đầu tiên là giá trị của phần tử xuất hiện nhiều nhất, số thứ hai là số lần xuất hiện của phần tử đó.

## Sample 1
### Input
```text
7
3 5 2 3 5 3 2
```
### Output
```text
3 3
```
### Giải thích
Danh sách các phiếu bầu là: $3, 5, 2, 3, 5, 3, 2$.
Thống kê tần suất xuất hiện của từng giá trị:

- Mã số $2$: xuất hiện 2 lần.
- Mã số $3$: xuất hiện 3 lần.
- Mã số $5$: xuất hiện 2 lần.

Mã số xuất hiện nhiều nhất là $3$ với số lần xuất hiện là $3$. Do đó kết quả in ra là `3 3`.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, \vert A_i \vert \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
