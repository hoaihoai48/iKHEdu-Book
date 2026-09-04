# Đếm cặp $a_i > 2 a_j$ (significant inversions)

## Bối cảnh
Cô giáo ghi lại điểm số của cả lớp theo đúng thứ tự chỗ ngồi. Cô muốn phát hiện những chênh lệch bất thường: một bạn ngồi phía trước nhưng điểm cao gấp hơn hai lần một bạn ngồi phía sau.

Hãy giúp cô đếm có bao nhiêu cặp bạn như vậy trong lớp.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm số cặp $(i, j)$ thỏa mãn $i < j$ và $A_i > 2 \cdot A_j$, rồi in ra tổng số cặp đếm được.

## Input
- Dòng đầu tiên chứa số lượng phần tử hoặc số lượng truy vấn $N$ hoặc $T$.
- Các dòng tiếp theo chứa dữ liệu chi tiết của bài toán theo chuẩn thi đấu.

## Output
- In ra kết quả trên một dòng.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Cặp $A_i > 2 A_j$ (Significant Inversions).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
