# Tối Ưu Cửa Sổ Trượt Tuyến Tính Khi N = 2.10⁵

## Bối cảnh
Một máy chủ phân tích dữ liệu lớn thu thập N giá trị dung lượng truy cập mỗi giây từ cổng Internet quốc tế. Để phát hiện các mẫu tấn công từ chối dịch vụ (DDoS) tiềm ẩn, thuật toán an ninh mạng cần đếm số lượng đoạn thời gian liên tiếp nhau mà tổng lưu lượng đúng bằng ngưỡng cảnh báo S, với dữ liệu cực lớn lên tới N = 200.000 phần tử đòi hỏi xử lý thời gian thực nghiêm ngặt O(N).

## Nhiệm vụ
Cho mảng gồm N số nguyên dương và số nguyên S. Hãy tìm số lượng đoạn con liên tiếp có tổng đúng bằng S trong thời gian O(N).

## Input
- Dòng 1: 2 số nguyên $N$ và $S$ ($1 \le N \le 2 \cdot 10^5, 1 \le S \le 10^{14}$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
5 7
2 3 2 5 2
```
### Output
```text
2
```
### Giải thích
Các đoạn con liên tiếp có tổng đúng bằng 7 là: [2, 3, 2] (2 + 3 + 2 = 7) và [5, 2] (5 + 2 = 7). Tổng cộng có đúng 2 đoạn con thỏa mãn.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, S \le 10^{14}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
