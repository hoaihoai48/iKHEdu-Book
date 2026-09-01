# Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (cht)

## Bối cảnh
Trong lập trình thi đấu và giải quyết bài toán tối ưu, **Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT)** là bài toán trọng tâm thuộc cấp độ **P5** nhằm rèn luyện: CHT tối ưu $dp[i] = \min(dp[j] + m_j x_i + c_j)$ từ $\mathcal{O}(N^2) \to \mathcal{O}(N \log N)$.

Cho dữ liệu đầu vào thỏa mãn các ràng buộc toán học của bài toán. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Hãy lập trình giải quyết bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (cht) với độ phức tạp tối ưu nhất.

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
* Kết quả tính toán phù hợp với yêu cầu của bài toán Tối Ưu Hóa Quy Hoạch Động Bằng Convex Hull Trick (CHT).

## Ràng buộc
- $100\%$ số test có dữ liệu đầu vào nằm trong phạm vi cho phép.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
