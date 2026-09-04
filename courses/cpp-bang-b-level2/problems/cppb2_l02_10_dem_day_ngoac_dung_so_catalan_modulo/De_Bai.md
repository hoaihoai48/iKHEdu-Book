# Đếm dãy ngoặc đúng (số Catalan modulo)

## Bối cảnh
Cô giáo mỹ thuật yêu cầu cả lớp vẽ các dãy ngoặc tròn mở và đóng sao cho mỗi ngoặc đóng đều khớp đúng với một ngoặc mở trước đó. Với $n$ cặp ngoặc, số dãy vẽ đúng có thể rất lớn nên lớp trưởng chỉ ghi lại phần dư khi chia cho $10^9+7$ để báo cáo.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ truy vấn, mỗi truy vấn gồm một số nguyên không âm $n$. Hãy lập trình đếm số dãy ngoặc đúng gồm $n$ cặp ngoặc (số Catalan thứ $n$) theo modulo $10^9+7$.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả của bài toán thỏa mãn các điều kiện đề bài trên một hoặc nhiều dòng.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```
### Giải thích
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Dãy Ngoặc Đúng (Số Catalan Modulo).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
