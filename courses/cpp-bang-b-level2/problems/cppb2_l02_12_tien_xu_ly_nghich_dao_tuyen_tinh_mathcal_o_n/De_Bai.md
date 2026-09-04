# Tiền xử lý nghịch đảo tuyến tính $\mathcal{o}(n)$

## Bối cảnh
Phòng thí nghiệm cần chuẩn bị sẵn một bảng tra cứu: với mỗi số $i$ từ $1$ đến $n$, ghi lại "số đảo" của $i$ theo modulo $10^9+7$ (số nhân với $i$ cho phần dư $1$). Bảng này được in một lần rồi dùng cho cả học kỳ, nên khâu chuẩn bị cần làm gọn trong một lượt duyệt duy nhất.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho số nguyên $n$. Hãy lập trình tính nghịch đảo modulo $10^9+7$ của từng số $i$ với $1 \le i \le n$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tiền Xử Lý Nghịch Đảo Tuyến Tính $\mathcal{O}(N)$.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
