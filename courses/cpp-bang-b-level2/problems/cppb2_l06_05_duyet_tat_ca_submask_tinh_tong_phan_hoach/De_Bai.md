# Duyệt tất cả submask tính tổng phân hoạch

## Bối cảnh
Câu lạc bộ muốn lập mọi đội hình con có thể từ danh sách thành viên. Mỗi đội hình đã được chấm một số điểm, và ban chủ nhiệm cần cộng dồn điểm số theo từng cách gom nhóm.

Để làm được, trước hết phải liệt kê đầy đủ mọi tập con của danh sách thành viên.

## Nhiệm vụ
Cho một mặt nạ $mask$ biểu diễn tập gồm $N$ phần tử và giá trị của từng tập con. Hãy lập trình liệt kê mọi tập con của $mask$ và tính tổng giá trị trên tất cả các tập con đó.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Duyệt Tất Cả Submask Tính Tổng Phân Hoạch.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
