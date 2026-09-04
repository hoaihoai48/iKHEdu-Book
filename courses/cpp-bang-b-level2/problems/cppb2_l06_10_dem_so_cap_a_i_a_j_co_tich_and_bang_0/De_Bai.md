# Đếm số cặp $(a_i, a_j)$ có tích and bằng 0

## Bối cảnh
Thủ thư đánh số mỗi cuốn sách bằng một mã nhị phân. Hai cuốn sách được gọi là không chồng lấn nếu phép AND hai mã của chúng bằng $0$.

Thủ thư muốn đếm có bao nhiêu cặp sách không chồng lấn để xếp chúng lên cùng một kệ đặc biệt.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình đếm số cặp $(i, j)$ với $i < j$ sao cho $A_i \ \mathrm{AND}\  A_j = 0$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Đếm Số Cặp $(A_i, A_j)$ Có Tích AND Bằng 0.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
