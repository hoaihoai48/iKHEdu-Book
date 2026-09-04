# Lũy thừa với số mũ cực lớn

## Bối cảnh
Máy chủ của thư viện mã hóa mỗi lượt mượn sách bằng một lũy thừa $a^b$, trong đó số mũ $b$ dài tới hàng nghìn chữ số nên không thể nhập vào máy tính thông thường. Thủ thư chỉ cần biết phần dư của kết quả khi chia cho $10^9+7$ để in lên phiếu mượn.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho cơ số $a$ và số mũ $b$ rất lớn được cho dưới dạng chuỗi thập phân. Hãy lập trình tính $a^b \bmod (10^9+7)$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Lũy Thừa Với Số Mũ Cực Lớn.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
