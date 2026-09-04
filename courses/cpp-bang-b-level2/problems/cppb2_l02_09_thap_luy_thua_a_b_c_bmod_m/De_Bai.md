# Tháp lũy thừa $a^{b^c} \bmod m$

## Bối cảnh
Trong cuộc thi xếp tháp số của lớp, mỗi đội dựng một "tháp lũy thừa" ba tầng $a^{b^c}$ rồi chỉ ghi lại phần dư của ngọn tháp khi chia cho $10^9+7$. Vì tầng trên cùng đã là một lũy thừa khổng lồ, không đội nào tính trực tiếp từ trên xuống được.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ bộ $(a, b, c)$. Hãy lập trình tính tháp lũy thừa $a^{b^c} \bmod (10^9+7)$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tháp Lũy Thừa $A^{B^C} \bmod M$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
