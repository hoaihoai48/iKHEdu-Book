# Phân chia công việc hoàn hảo (job assignment)

## Bối cảnh
Quản đốc có $N$ công nhân và $N$ công việc. Mỗi người làm mỗi việc tốn một chi phí (thời gian) khác nhau, và mỗi người chỉ làm đúng một việc.

Quản đốc cần phân công sao cho tổng chi phí của cả xưởng là thấp nhất.

## Nhiệm vụ
Cho ma trận chi phí kích thước $N \times N$, trong đó ô $(i, j)$ là chi phí khi giao việc $j$ cho người $i$. Hãy lập trình phân công mỗi người đúng một việc sao cho tổng chi phí là nhỏ nhất.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Phân Chia Công Việc Hoàn Hảo (Job Assignment).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
