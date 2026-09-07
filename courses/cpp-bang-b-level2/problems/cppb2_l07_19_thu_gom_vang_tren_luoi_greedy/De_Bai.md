# Thu gom vang tren luoi greedy

## Bối cảnh
Cho dữ liệu bài toán liên quan đến **Thu Gom Vang Tren Luoi Greedy**. Cần thiết kế thuật toán tối ưu để xử lý nhanh chóng trong giới hạn thời gian $1.0\text{s}$.

## Nhiệm vụ
Cho lưới n x m, mỗi ô chứa một lượng vàng a[i][j]. Hãy lập trình tìm đường đi từ (1,1) tới (n,m) chỉ đi xuống hoặc sang phải để thu được nhiều vàng nhất và in ra lượng vàng đó.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Thu Gom Vang Tren Luoi Greedy.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
