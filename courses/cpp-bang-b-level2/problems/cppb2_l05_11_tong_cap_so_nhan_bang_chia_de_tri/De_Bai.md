# Tổng cấp số nhân bằng chia để trị

## Bối cảnh
Chị nhân viên ngân hàng cần tính tổng tiền gốc lẫn lãi sau nhiều kỳ gửi, khi mỗi kỳ số tiền được nhân lên theo cùng một hệ số. Số kỳ có thể rất lớn nên không thể cộng tay từng số hạng.

Chị cần tính nhanh tổng của dãy cấp số nhân này để in sao kê cho khách.

## Nhiệm vụ
Cho số $A$, số lượng số hạng $N$ và số chia $MOD$. Hãy lập trình tính tổng $S = A^0 + A^1 + \dots + A^{N-1}$ theo modulo $MOD$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tổng Cấp Số Nhân Bằng Chia Để Trị.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
