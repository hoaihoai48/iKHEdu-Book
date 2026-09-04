# Tìm Cặp Có Tổng Gần S Nhất

## Bối cảnh
Trong kỹ thuật vi mạch điện tử, kỹ sư cần ghép nối 2 điện trở có giá trị điện trở kháng lần lượt trong danh sách N linh kiện có sẵn để mạch thu được giá trị điện trở kháng tương đương gần nhất với thông số thiết kế S. Do giá trị các linh kiện có sai số chế tạo, kỹ sư muốn tìm ra cặp linh kiện sao cho độ lệch tuyệt đối giữa tổng giá trị của cặp và thông số S là nhỏ nhất. Nếu có nhiều cặp có cùng độ lệch nhỏ nhất, ưu tiên chọn cặp có tổng giá trị nhỏ hơn.

## Nhiệm vụ
Cho mảng gồm N số nguyên và một số nguyên S. Hãy tìm một cặp số (A[i], A[j]) với i < j sao cho độ chênh lệch |(A[i] + A[j]) - S| là nhỏ nhất có thể. Nếu có nhiều cặp, in ra cặp có tổng nhỏ hơn theo thứ tự tăng dần.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $S$ ($2 \le N \le 10^5, -10^{18} \le S \le 10^{18}$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 2 số nguyên biểu diễn cặp số tìm được theo thứ tự tăng dần.

## Sample 1
### Input
```text
5 20
2 8 13 4 25
```
### Output
```text
8 13
```
### Giải thích
Sắp xếp danh sách điện trở tăng dần: [2, 4, 8, 13, 25] và S = 20. Xét các cặp có tổng gần 20: cặp (8, 13) có tổng 8 + 13 = 21 (chênh lệch |21 - 20| = 1); cặp (4, 13) có tổng 17 (chênh lệch |17 - 20| = 3). Cặp có độ chênh lệch nhỏ nhất đạt được là (8, 13) với khoảng cách chênh lệch chỉ là 1. Kết quả in ra: 8 13.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
