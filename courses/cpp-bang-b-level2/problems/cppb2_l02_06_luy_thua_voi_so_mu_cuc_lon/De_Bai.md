# Lũy thừa với số mũ cực lớn

## Bối cảnh
Máy chủ của thư viện mã hóa mỗi lượt mượn sách bằng một lũy thừa $a^b$, trong đó số mũ $b$ dài tới hàng nghìn chữ số nên không thể nhập vào máy tính thông thường. Thủ thư chỉ cần biết phần dư của kết quả khi chia cho $10^9+7$ để in lên phiếu mượn.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho cơ số $a$ và số mũ $b$ rất lớn được cho dưới dạng chuỗi thập phân. Hãy lập trình tính $a^b \bmod (10^9+7)$.

## Input

- Gồm một dòng duy nhất chứa cơ số $a$ ($0 \le a \le 10^9$) và số mũ $b$ rất lớn được cho dưới dạng chuỗi thập phân (độ dài không quá $10^5$ ký tự, không có số $0$ vô nghĩa ở đầu trừ chính số $0$), cách nhau bởi một dấu cách.

## Output

- In ra một dòng duy nhất là giá trị $a^b \bmod (10^9+7)$.

## Sample 1
### Input
```text
2 1000000007
```
### Output
```text
2
```
### Giải thích

Số mũ $1000000007$ quá lớn nên ta duyệt từng chữ số của nó từ trái sang phải, mỗi bước nhân phần dư đang có với $10$ rồi cộng chữ số mới và chỉ giữ phần dư khi chia cho $10^9+6$. Sau khi duyệt cả $10$ chữ số, phần dư thu được là $1$. Vì vậy đáp án là $2^1 = 2$.

## Ràng buộc

- $0 \le a \le 10^9$; chuỗi $b$ có độ dài không quá $10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
