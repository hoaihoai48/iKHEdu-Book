# Ordered set PBDS truy van thu hang

## Bối cảnh
Cho dữ liệu bài toán liên quan đến **Ordered Set Pbds Truy Van Thu Hang**. Cần thiết kế thuật toán tối ưu để xử lý nhanh chóng trong giới hạn thời gian $1.0\text{s}$.

## Nhiệm vụ
Cho q truy vấn trên đa tập có thứ tự: loại 1 chèn x, loại 2 xóa một lần x, loại 3 đếm số phần tử nhỏ hơn x, loại 4 tìm phần tử thứ k (0-indexed). Hãy lập trình xử lý các truy vấn và in ra đáp án cho loại 3 và 4 (in -1 nếu k không hợp lệ).

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Ordered Set Pbds Truy Van Thu Hang.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
