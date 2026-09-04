# Đếm số tập con có xor bằng k

## Bối cảnh
Anh kỹ sư bảo mật giữ một chùm mảnh khóa, mỗi mảnh mang một con số. Mã mở két được tạo bằng cách lấy phép XOR của tất cả các mảnh trong tập con được chọn.

Anh cần đếm xem có bao nhiêu tập con các mảnh ghép lại cho ra đúng mã mục tiêu $K$.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên và một số $K$. Hãy lập trình đếm số tập con có giá trị XOR của tất cả các phần tử trong tập con bằng $K$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Tập Con Có XOR Bằng K.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
