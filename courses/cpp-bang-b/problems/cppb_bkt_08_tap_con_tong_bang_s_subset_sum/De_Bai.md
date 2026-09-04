# Tập Con Có Tổng Bằng S (Subset Sum)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Một kho quỹ ngân hàng đang lưu trữ $N$ thỏi vàng nguyên chất với trọng lượng lần lượt là $A_1, A_2, \dots, A_N$. Khách hàng VIP nộp phiếu yêu cầu rút đúng một khối lượng vàng có tổng trọng lượng bằng $S$. Thủ kho cần lập danh sách tất cả các phương án chọn các thỏi vàng trong kho để giao dịch đúng số lượng yêu cầu mà không phải cắt xẻ bất kỳ thỏi vàng nào.

## Nhiệm vụ
Cho mảng số nguyên dương $A$ gồm $N$ phần tử và số nguyên dương $S$. Hãy sử dụng thuật toán Quay lui kết hợp cắt tỉa khả thi (dừng nhánh khi tổng tích lũy vượt quá $S$) để tìm và in ra tất cả các tập con có tổng bằng đúng $S$ theo thứ tự từ điển. Nếu không có phương án nào thỏa mãn, in ra `-1`.

## Input
- Dòng 1: Hai số nguyên dương $N, S$ ($1 \le N \le 20, 1 \le S \le 1000$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- In ra các tập con thỏa mãn (mỗi tập con trên một dòng, các phần tử cách nhau bởi dấu cách), hoặc in `-1` nếu không tìm thấy tập con nào.

## Sample 1
### Input
```text
4 6
1 2 3 5
```
### Output
```text
1 2 3
1 5
```
### Giải thích
Với kho vàng gồm các thỏi $[1, 2, 3, 5]$ và mục tiêu $S = 6$, có 2 phương án chọn:
- Phương án 1: Chọn các thỏi $\{1, 2, 3\}$ vì $1 + 2 + 3 = 6$.
- Phương án 2: Chọn các thỏi $\{1, 5\}$ vì $1 + 5 = 6$.

## Ràng buộc
- 100% số test có $1 \le N \le 20, 1 \le S \le 1000$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
