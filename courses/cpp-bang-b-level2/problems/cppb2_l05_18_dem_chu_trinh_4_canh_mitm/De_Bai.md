# Đếm Chu Trình 4 Cạnh bằng MITM

## Bối cảnh
Nhóm phân tích mạng xã hội muốn đo độ gắn kết của cộng đồng bằng cách đếm các nhóm bốn người khép kín thành vòng tròn bạn bè: mỗi người quen đúng hai người còn lại trong nhóm. Với đồ thị kết bạn lên tới hàng trăm nghìn mối quan hệ, việc liệt kê từng bộ bốn là bất khả thi.

Nhóm kỹ thuật bèn chia đôi danh sách người dùng, liệt kê các cặp bạn chung trong từng nửa rồi ghép kết quả lại để suy ra tổng số vòng tròn bốn người mà không bỏ sót cũng không đếm trùng.

## Nhiệm vụ
Cho một đồ thị vô hướng. Hãy lập trình đếm số chu trình đơn có độ dài đúng $4$ cạnh trong đồ thị.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Chu Trinh 4 Canh Mitm.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
