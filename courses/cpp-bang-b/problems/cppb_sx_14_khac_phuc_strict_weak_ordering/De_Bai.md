# Sắp Xếp Đoạn Thẳng Không Giao Lỗi

## Bối cảnh
Trong đồ họa máy tính và xử lý bản đồ số, một hệ thống cần hiển thị $N$ đoạn thẳng nằm ngang trên trục tọa độ, mỗi đoạn được xác định bởi cặp mút đầu và mút cuối $[L_i, R_i]$. Để thuật toán quét đường biên (Sweep-line) hoạt động chính xác và không bị treo do vi phạm nguyên lý so sánh nghiêm ngặt (Strict Weak Ordering), các đoạn thẳng cần được sắp xếp theo một trật tự chuẩn mực: các đoạn bắt đầu sớm hơn phải được quét trước; nếu cùng điểm bắt đầu, đoạn dài hơn (điểm kết thúc xa hơn) quét trước; và nếu hai đoạn thẳng hoàn toàn trùng khít nhau, hệ thống phải đảm bảo bảo toàn tuyệt đối thứ tự ban đầu xuất hiện trong file bản đồ (sắp xếp ổn định - Stable Sort).

## Nhiệm vụ
Cho danh sách $N$ đoạn thẳng $[L_i, R_i]$ trên trục số. Hãy sắp xếp các đoạn thẳng theo các tiêu chí sau:
1. Tọa độ đầu mút bắt đầu $L_i$ tăng dần.
2. Nếu cùng tọa độ $L_i$, tọa độ mút kết thúc $R_i$ giảm dần.
3. Nếu trùng cả $L_i$ và $R_i$, giữ nguyên thứ tự ban đầu xuất hiện trong dữ liệu vào.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 2 \cdot 10^5$) — số lượng đoạn thẳng.
- $N$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên $L_i, R_i$ ($-10^9 \le L_i \le R_i \le 10^9$) mô tả đoạn thẳng thứ $i$.

## Output
- In ra $N$ dòng, mỗi dòng gồm 2 số nguyên $L_i, R_i$ sau khi đã sắp xếp thỏa mãn toàn bộ tiêu chí trên.

## Sample 1
### Input
```text
3
2 8
1 5
2 10
```
### Output
```text
1 5
2 10
2 8
```
### Giải thích
Danh sách 3 đoạn thẳng ban đầu là: $[2, 8]$, $[1, 5]$, $[2, 10]$.
- Xét điểm đầu mút $L$: đoạn $[1, 5]$ có $L = 1$ nhỏ nhất nên đứng đầu tiên.
- Hai đoạn còn lại là $[2, 8]$ và $[2, 10]$ đều có cùng $L = 2$:
  - Xét điểm kết thúc $R$ giảm dần: đoạn $[2, 10]$ có $R = 10 > 8$ nên đoạn $[2, 10]$ phải đứng trước đoạn $[2, 8]$.

Thứ tự sau khi sắp xếp chuẩn là: `1 5`, tiếp đến `2 10`, và cuối cùng là `2 8`.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
