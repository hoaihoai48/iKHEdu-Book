# Lũy thừa ma trận kích thước $k \times k$

## Bối cảnh
Mạng lưới giao thông giữa $k$ bến xe được ghi trong một bảng $k \times k$: ô $(i, j)$ cho biết có bao nhiêu chuyến xe đi thẳng từ bến $i$ đến bến $j$ trong một chặng. Để biết sau đúng $n$ chặng thì giữa các bến có bao nhiêu hành trình, người ta nhân bảng này với chính nó $n$ lần rồi lấy phần dư theo $10^9+7$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho ma trận vuông $A$ kích thước $k \times k$ và số mũ $n$. Hãy lập trình tính $A^n$ theo modulo $10^9+7$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Ma Trận Kích Thước $K \times K$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
