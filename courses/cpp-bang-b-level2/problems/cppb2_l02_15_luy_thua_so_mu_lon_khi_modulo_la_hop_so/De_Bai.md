# Lũy thừa số mũ lớn khi modulo là hợp số

## Bối cảnh
Trạm quan trắc ghi chỉ số bụi mịn dưới dạng lũy thừa $a^b$, trong đó số mũ $b$ dài hàng nghìn chữ số và máy chỉ hiển thị phần dư khi chia cho $m$ (một hợp số). Kỹ thuật viên cần tính phần dư này mỗi giờ mà không thể nhập nổi số mũ khổng lồ vào máy tính bỏ túi.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho cơ số $a$, số mũ $b$ rất lớn (dạng chuỗi thập phân) và modulo $m$ là hợp số. Hãy lập trình tính $a^b \bmod m$.

## Input

- Gồm một dòng duy nhất chứa cơ số $a$ ($0 \le a \le 10^{18}$), số mũ $b$ rất lớn dưới dạng chuỗi thập phân (độ dài không quá $10^5$ ký tự) và modulo $m$ ($1 \le m \le 10^9$), cách nhau bởi dấu cách.

## Output

- In ra một dòng duy nhất là giá trị $a^b \bmod m$.

## Sample 1
### Input
```text
2 10 1000
```
### Output
```text
24
```
### Giải thích

Số mũ $10$ vừa đủ nhỏ để tính trực tiếp: $2^{10} = 1024$. Lấy $1024 = 1 \cdot 1000 + 24$ nên phần dư khi chia cho $1000$ là $24$.

## Ràng buộc

- $0 \le a \le 10^{18}$; chuỗi $b$ dài không quá $10^5$; $1 \le m \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
