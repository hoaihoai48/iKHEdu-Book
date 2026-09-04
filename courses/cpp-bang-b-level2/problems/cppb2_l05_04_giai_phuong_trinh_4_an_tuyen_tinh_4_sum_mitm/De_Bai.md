# Giải phương trình $4$ ẩn tuyến tính (4-sum mitm)

## Bối cảnh
Trong ngày hội thể thao, ban tổ chức có bốn bảng danh sách điểm số của bốn đội. Mỗi bảng ghi điểm của các vận động viên đội mình.

Ban tổ chức muốn biết có bao nhiêu cách chọn mỗi bảng đúng một con số sao cho tổng bốn số được chọn bằng $0$, để trao giải đồng đội cân bằng.

## Nhiệm vụ
Cho bốn dãy số $A, B, C, D$. Hãy lập trình đếm số bộ bốn $(a, b, c, d)$ với $a \in A, b \in B, c \in C, d \in D$ sao cho $a + b + c + d = 0$.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Giải Phương Trình $4$ Ẩn Tuyến Tính (4-Sum MITM).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
