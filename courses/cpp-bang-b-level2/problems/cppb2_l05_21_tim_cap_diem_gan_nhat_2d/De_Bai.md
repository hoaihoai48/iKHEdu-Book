# Tìm Cặp Điểm Gần Nhất 2D

## Bối cảnh
Trạm điều phối taxi bay lưu tọa độ của toàn bộ xe đang hoạt động trên bản đồ thành phố. Để tránh hai xe bay quá gần nhau gây mất an toàn, hệ thống cần liên tục tìm ra cặp xe có khoảng cách gần nhất và phát cảnh báo kịp thời.

Thay vì đo khoảng cách từng đôi một, hệ thống sắp xếp các xe theo tọa độ rồi chia mặt phẳng thành từng dải hẹp, chỉ so sánh các xe thực sự có cơ hội là đáp án trong mỗi dải.

## Nhiệm vụ
Cho $N$ điểm trên mặt phẳng tọa độ hai chiều. Hãy lập trình tìm khoảng cách nhỏ nhất giữa hai điểm phân biệt trong số đó.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Tim Cap Diem Gan Nhat 2d.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
