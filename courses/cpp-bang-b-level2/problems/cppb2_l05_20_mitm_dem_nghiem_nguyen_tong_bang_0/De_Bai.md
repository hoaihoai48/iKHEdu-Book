# MITM Đếm Nghiệm Nguyên Tổng Bằng 0

## Bối cảnh
Thủ quỹ của câu lạc bộ có danh sách các khoản thu chi trong năm, gồm cả số dương lẫn số âm. Cuối năm, bạn ấy muốn biết có bao nhiêu nhóm khoản mục khác nhau mà tổng cộngbù nhau về đúng $0$, để đối chiếu sổ sách cho khớp.

Vì số khoản mục quá nhiều để thử mọi tập con, thủ quỹ chia danh sách thành hai nửa, liệt kê tổng của mọi tập con trong từng nửa rồi ghép các tổng đối nhau lại để ra đáp án.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên. Hãy lập trình đếm số tập con có tổng các phần tử bằng $0$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Mitm Dem Nghiem Nguyen Tong Bang 0.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
