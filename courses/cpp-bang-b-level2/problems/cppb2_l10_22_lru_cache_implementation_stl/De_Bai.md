# LRU cache implementation STL

## Bối cảnh
Cho dữ liệu bài toán liên quan đến **Lru Cache Implementation Stl**. Cần thiết kế thuật toán tối ưu để xử lý nhanh chóng trong giới hạn thời gian $1.0\text{s}$.

## Nhiệm vụ
Cho dung lượng cache cap và q thao tác gồm SET k v và GET k theo nguyên tắc LRU (loại bỏ phần tử dùng lâu nhất khi đầy). Hãy lập trình mô phỏng cache và in ra kết quả của mỗi lệnh GET (hoặc -1 nếu không tồn tại).

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Lru Cache Implementation Stl.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
