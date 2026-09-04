# Giá Trị Trung Bình Lớn Nhất Của Đoạn K

## Bối cảnh
Trong phân tích kỹ thuật chứng khoán, chỉ báo đường trung bình động MA(K) được dùng để xác định xu hướng giá cổ phiếu. Nhà phân tích cần khảo sát lịch sử giá đóng cửa trong N phiên giao dịch liên tiếp để tìm ra khoảng thời gian K phiên liên tiếp có giá trị trung bình đạt mức cao nhất.

## Nhiệm vụ
Cho dãy gồm N số nguyên và số nguyên K (K <= N). Hãy tìm giá trị trung bình lớn nhất của một đoạn con gồm K phần tử liên tiếp, làm tròn đến đúng 3 chữ số thập phân.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra giá trị trung bình lớn nhất tìm được với đúng 3 chữ số sau dấu phẩy.

## Sample 1
### Input
```text
4 4
1 12 -5 -6
```
### Output
```text
0.500
```
### Giải thích
Với N = 4 và K = 4, chỉ có duy nhất 1 đoạn con gồm 4 phần tử: [1, 12, -5, -6]. Tổng của đoạn là 1 + 12 - 5 - 6 = 2. Giá trị trung bình là 2 / 4 = 0.500. Kết quả in ra: 0.500.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
