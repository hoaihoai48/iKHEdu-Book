# Đếm số phần tử bật BIT chung (bitwise and)

## Bối cảnh
Trường học phát cho mỗi học sinh một thẻ từ mang một mã số. Thầy giám thị muốn kiểm tra hệ thống quẹt thẻ: ở từng vị trí bit, có bao nhiêu thẻ đang bật bit đó.

Thống kê này giúp thầy phát hiện những vị trí bit bị lỗi hàng loạt.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên. Với mỗi vị trí bit $b$ ($0 \le b \le 30$), hãy lập trình đếm có bao nhiêu phần tử trong dãy bật bit $b$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Phần Tử Bật Bit Chung (Bitwise AND).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
