# Bài toán người du lịch (tsp bitmask DP)

## Bối cảnh
Anh nhân viên giao hàng phải ghé qua mỗi địa chỉ đúng một lần rồi quay về kho. Giá cước di chuyển giữa từng cặp địa điểm đều đã biết trước.

Anh cần một lịch trình khép kín có tổng chi phí rẻ nhất để kịp giờ giao hàng.

## Nhiệm vụ
Cho số thành phố $N$ (nhỏ) và ma trận khoảng cách giữa từng cặp thành phố. Hãy lập trình tìm chi phí nhỏ nhất của hành trình xuất phát từ thành phố $0$, thăm mỗi thành phố đúng một lần rồi quay về $0$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Bài Toán Người Du Lịch (TSP Bitmask DP).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
