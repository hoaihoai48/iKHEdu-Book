# Tối ưu phân đoạn trọng số ma trận 2d

## Bối cảnh

Cô thủ thư muốn chia kho sách hình chữ nhật thành các khu vực để mỗi khu vực có tổng trọng lượng sách không vượt quá sức chịu của kệ. Cô cần biết sức chịu tối thiểu của kệ để có thể chia kho thành số khu vực đúng quy định.

Cô cân thử từng chồng sách rồi tính toán phương án chia kho hợp lý.

## Nhiệm vụ

Cho một mảng đã sắp xếp tăng dần rồi bị xoay vòng tại một vị trí chưa biết, cùng một số nguyên $target$. Hãy lập trình tìm chỉ số (đánh số từ $0$) của $target$ trong mảng; in `-1` nếu $target$ không xuất hiện.

## Input

- Dòng đầu tiên chứa hai số nguyên $n, target$ ($1 \le n \le 10^6$) — độ dài mảng và giá trị cần tìm.
- Dòng thứ hai chứa $n$ số nguyên phân biệt tạo thành một mảng xoay của dãy tăng dần.

## Output

- In ra một dòng duy nhất là chỉ số (đánh số từ $0$) của $target$ trong mảng; in `-1` nếu không tìm thấy.

## Sample 1
### Input
```text
5 3
4 5 1 2 3
```
### Output
```text
4
```
### Giải thích

Mảng $[4, 5, 1, 2, 3]$, cần tìm $3$. Xét giữa đoạn $[0, 4]$ là vị trí $2$ (giá trị $1$): nửa trái $[4, 5, 1]$ không tăng dần nên nửa phải $[1, 2, 3]$ tăng dần; $3$ nằm trong khoảng $[1, 3]$ nên tìm tiếp trong $[3, 4]$. Giữa đoạn $[3, 4]$ là vị trí $3$ (giá trị $2 < 3$) nên sang phải, gặp $a[4] = 3$ — đúng giá trị cần tìm, đáp án là $4$.

## Ràng buộc

- $1 \le n \le 10^6$, các phần tử phân biệt.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
