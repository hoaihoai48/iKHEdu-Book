# Profile DP Lát Gạch Domino

## Bối cảnh
Bác thợ lát sàn nhận lát kín một căn phòng hình chữ nhật kích thước $N \times M$ bằng các viên gạch domino $1 \times 2$, có thể xoay dọc hoặc xoay ngang tùy ý. Trước khi mua gạch, bác muốn biết có tất cả bao nhiêu cách lát kín sàn để chuẩn bị phương án thi công.

Bác lát thử từng hàng từ trái sang phải, ghi nhớ phần gạch còn thò xuống hàng dưới bằng một dãy ghi chú hẹp, rồi điền tiếp cho khớp cho đến khi kín cả sàn.

## Nhiệm vụ
Cho một bảng hình chữ nhật kích thước $N \times M$. Hãy lập trình đếm số cách lát kín bảng bằng các viên gạch domino $1 \times 2$ (được phép xoay dọc hoặc ngang).

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Profile Dp Lat Gach Domino.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
