# Cái túi kích thước nhỏ (knapsack $n \le 40$)

## Bối cảnh
Bác thủ kho cần xếp hàng lên một chuyến xe tải có sức chở giới hạn. Mỗi kiện hàng có khối lượng và giá trị khác nhau, mà số kiện thì khá nhiều (vài chục kiện) nên không thể thử hết mọi cách bằng tay.

Bác muốn chọn ra những kiện mang đi sao cho tổng giá trị cao nhất mà xe vẫn chở nổi.

## Nhiệm vụ
Cho $N$ món đồ ($N \le 40$), mỗi món có khối lượng và giá trị, cùng sức chứa của chiếc túi. Hãy lập trình chọn ra một tập con các món đồ có tổng giá trị lớn nhất mà tổng khối lượng không vượt quá sức chứa.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Cái Túi Kích Thước Nhỏ (Knapsack $N \le 40$).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
