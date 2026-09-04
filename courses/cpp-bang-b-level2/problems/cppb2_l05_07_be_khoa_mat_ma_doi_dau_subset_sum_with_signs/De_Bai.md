# Bẻ khóa mật mã đổi dấu (subset sum with signs)

## Bối cảnh
Chiếc két sắt có $N$ núm vặn, mỗi núm mang một con số. Người thợ có thể xoay mỗi núm sang trái (trừ đi con số), sang phải (cộng thêm con số) hoặc giữ nguyên (bỏ qua núm đó).

Người thợ cần biết có bao nhiêu cách vặn để con số hiển thị cuối cùng đúng bằng mật mã mục tiêu.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên và một giá trị mục tiêu $T$. Hãy lập trình đếm số cách gán mỗi phần tử vào một trong ba trạng thái (bỏ qua, cộng thêm, trừ đi) sao cho tổng thu được bằng $T$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Bẻ Khóa Mật Mã Đổi Dấu (Subset Sum with Signs).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
