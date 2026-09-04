# Lũy thừa ma trận 2x2 (dãy fibonacci lớn)

## Bối cảnh
Trang trại thỏ của bác nông dân phát triển theo quy luật quen thuộc: mỗi tháng, số cặp thỏ mới bằng tổng số cặp thỏ của hai tháng trước đó. Sau rất nhiều tháng, đàn thỏ lên tới con số khổng lồ nên bác chỉ cần biết phần dư của con số đó khi chia cho $10^9+7$ để đối chiếu với sức chứa của chuồng.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ truy vấn, mỗi truy vấn gồm một số nguyên không âm $n$. Hãy lập trình tính số Fibonacci thứ $n$ (với $F_0 = 0, F_1 = 1$) theo modulo $10^9+7$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Ma Trận 2x2 (Dãy Fibonacci Lớn).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
