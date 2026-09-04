# Tổng cấp số nhân $s_n = \sum_{i=0}^n a^i \bmod m$

## Bối cảnh
Một người gửi tiết kiệm theo kiểu lạ: tháng đầu gửi $1$ đồng, các tháng sau số tiền gửi gấp $a$ lần tháng trước, kéo dài tới tháng thứ $n$. Ngân hàng cần biết tổng số tiền đã gửi theo modulo $10^9+7$ để in sao kê, mà $n$ có thể rất lớn nên không thể cộng từng tháng một.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $T$ cặp $(a, n)$. Hãy lập trình tính $S = 1 + a + a^2 + \dots + a^n$ theo modulo $10^9+7$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Cấp Số Nhân $S_N = \sum_{i=0}^N A^i \bmod M$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
