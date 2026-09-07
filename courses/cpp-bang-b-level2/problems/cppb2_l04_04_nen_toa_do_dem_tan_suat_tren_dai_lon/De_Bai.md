# Nén tọa độ & đếm tần suất trên dải lớn

## Bối cảnh

Trạm thu phí ghi lại biển số xe đi qua trong ngày, có những biển số rất lớn và thưa thớt. Nhân viên thống kê muốn gom các biển số về thứ hạng liên tiếp để đếm tần suất mỗi loại xe cho gọn.

Anh nhân viên liệt kê tất cả biển số xuất hiện rồi đánh số lại từ đầu để dễ đếm.

## Nhiệm vụ

Cho dãy gồm $n$ tọa độ nguyên (giá trị có thể rất lớn). Hãy lập trình đếm số lần xuất hiện của từng giá trị phân biệt, rồi in ra theo thứ tự tăng dần của giá trị.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 2 \cdot 10^5$).
- Dòng thứ hai chứa $n$ số nguyên $a_i$ ($|a_i| \le 10^{18}$).

## Output

- In ra mỗi giá trị phân biệt trên một dòng theo thứ tự tăng dần, theo định dạng `giá trị: tần suất`.

## Sample 1
### Input
```text
6
5 2 5 3 2 5
```
### Output
```text
2: 2
3: 1
5: 3
```
### Giải thích

Dãy có ba giá trị phân biệt. Đếm tay: số $2$ xuất hiện $2$ lần, số $3$ xuất hiện $1$ lần, số $5$ xuất hiện $3$ lần. Sắp xếp tăng dần các giá trị rồi in kèm tần suất, được đúng ba dòng kết quả.

## Ràng buộc

- $1 \le n \le 2 \cdot 10^5$, $|a_i| \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
