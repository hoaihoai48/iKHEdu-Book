# Tìm chu trình hamilton chi phí nhỏ nhất

## Bối cảnh
Đoàn kiểm tra phải thăm mỗi chi nhánh đúng một lần rồi quay về trụ sở. Chi phí di chuyển giữa từng cặp chi nhánh đều đã biết.

Đoàn cần một hành trình khép kín rẻ nhất để tiết kiệm ngân sách công tác.

## Nhiệm vụ
Cho ma trận chi phí di chuyển giữa $N$ thành phố (nhỏ). Hãy lập trình tìm chu trình Hamilton có tổng chi phí nhỏ nhất, tức hành trình thăm mỗi thành phố đúng một lần rồi quay về điểm xuất phát.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tìm Chu Trình Hamilton Chi Phí Nhỏ Nhất.

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
