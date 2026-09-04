# Đếm Đường Đi Hamilton bằng Bitmask

## Bối cảnh
Công ty chuyển phát có $N$ điểm giao hàng và bản đồ đường đi một chiều giữa chúng. Chú tài xế muốn biết có bao nhiêu hành trình xuất phát từ một điểm, ghé mỗi điểm đúng một lần rồi kết thúc ở bất kỳ đâu, để lên kế hoạch chạy thử toàn tuyến.

Vì số hành trình tăng theo giai thừa, hệ thống ghi nhớ từng trạng thái gồm tập điểm đã ghé và điểm đang đứng bằng mặt nạ bit, rồi mở rộng dần từng bước đi kế tiếp cho đến khi đủ $N$ điểm.

## Nhiệm vụ
Cho một đồ thị gồm $N$ đỉnh (nhỏ). Hãy lập trình đếm số đường đi Hamilton, tức số đường đi qua mỗi đỉnh đúng một lần.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Duong Di Hamilton Bitmask.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
