# Chia Để Trị Dãy Con Tổng Lớn Nhất

## Bối cảnh
Cửa hàng trực tuyến theo dõi lợi nhuận từng ngày trong tháng, có ngày lãi, có ngày lỗ. Chủ cửa hàng muốn biết đoạn ngày liên tiếp nào mang lại tổng lợi nhuận cao nhất để rút ra bài học về đợt kinh doanh thành công nhất.

Thay vì thử mọi đoạn ngày một cách thủ công, bạn nhân viên tin học chia dãy ngày thành hai nửa, tìm đoạn tốt nhất nằm gọn mỗi bên và đoạn vắt qua giữa, rồi chọn ra đáp án tốt nhất trong ba ứng viên đó.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên. Hãy lập trình tìm tổng lớn nhất trong tất cả các đoạn con liên tiếp của mảng.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Chia De Tri Day Con Tong Max.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
