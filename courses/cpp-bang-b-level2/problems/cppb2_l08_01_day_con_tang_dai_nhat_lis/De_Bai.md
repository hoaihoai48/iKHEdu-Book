# Dãy con tăng dài nhất

## Bối cảnh

Trạm quan trắc ven sông ghi lại mực nước mỗi giờ vào một dãy số dài. Nhóm kỹ sư muốn biết đợt dâng nước kéo dài nhất ẩn trong dữ liệu: chọn ra một số thời điểm theo đúng thứ tự xuất hiện sao cho mực nước tăng dần nghiêm ngặt từng bước. Đợt dâng đó không cần gồm các giờ liên tiếp nhau, chỉ cần giữ nguyên thứ tự thời gian. Độ dài của đợt dâng dài nhất chính là chỉ số mà trạm dùng để đánh giá xu hướng dâng của con sông trong ngày hôm đó.

## Nhiệm vụ

Cho số nguyên $N$ và dãy $N$ số nguyên $A_1, A_2, \dots, A_N$ ghi mực nước theo thời gian. Hãy lập trình tìm độ dài của dãy con tăng nghiêm ngặt dài nhất, tức số lượng phần tử nhiều nhất có thể chọn ra sao cho chỉ số tăng dần và giá trị tăng dần nghiêm ngặt từng bước.

## Input

- Dòng 1: số nguyên $N$ ($1 \le N \le 2 \times 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$), các số cách nhau bởi dấu cách.

## Output

- In ra một số nguyên duy nhất là độ dài của dãy con tăng nghiêm ngặt dài nhất.

## Sample 1

### Input

```text
6
10 20 10 30 20 50
```

### Output

```text
4
```

### Giải thích

Xét dãy $10, 20, 10, 30, 20, 50$ theo từng vị trí từ trái sang phải, ghi lại độ dài tốt nhất của một dãy tăng kết thúc đúng tại vị trí đó:

- Vị trí 1 (giá trị $10$): chưa có số nào đứng trước, độ dài tốt nhất là $1$.
- Vị trí 2 (giá trị $20$): có số $10$ đứng trước và $10 < 20$, nên nối dài được thành $1 + 1 = 2$.
- Vị trí 3 (giá trị $10$): không có số nào đứng trước mà nhỏ hơn $10$, độ dài tốt nhất vẫn là $1$.
- Vị trí 4 (giá trị $30$): các số đứng trước nhỏ hơn $30$ là $10, 20, 10$; dãy tốt nhất nối được là $10, 20$ rồi thêm $30$, độ dài $2 + 1 = 3$.
- Vị trí 5 (giá trị $20$): số $10$ đứng trước nhỏ hơn $20$ cho dãy $10, 20$, độ dài $1 + 1 = 2$.
- Vị trí 6 (giá trị $50$): nối tiếp sau dãy $10, 20, 30$ được $10, 20, 30, 50$, độ dài $3 + 1 = 4$.

Trong các độ dài $1, 2, 1, 3, 2, 4$, giá trị lớn nhất là $4$ nên đáp án là $4$.

## Ràng buộc

- $1 \le N \le 2 \times 10^5$; $1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
