# Convex hull trick DP toi uu duong thang

## Bối cảnh
Cho dữ liệu bài toán liên quan đến **Convex Hull Trick Dp Toi Uu Duong Thang**. Cần thiết kế thuật toán tối ưu để xử lý nhanh chóng trong giới hạn thời gian $1.0\text{s}$.

## Nhiệm vụ
Cho hai dãy a[i], b[i] gồm n số. Hãy lập trình tính dãy dp với dp[0] = 0 và dp[i] = min(dp[j] + b[j] * a[i]) với j < i, rồi in ra dp[n-1].

## Input
- Dòng 1: Gồm các số nguyên biểu thị tham số kích thước bài toán ($1 \le N \le 10^5$).
- Các dòng tiếp theo: Chứa các phần tử của mảng hoặc các truy vấn cần xử lý.

## Output
- In ra kết quả tối ưu của bài toán trên từng dòng tương ứng.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Convex Hull Trick Dp Toi Uu Duong Thang.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
