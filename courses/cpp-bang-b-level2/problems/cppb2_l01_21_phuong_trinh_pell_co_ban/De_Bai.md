# Phương Trình Pell Cơ Bản

## Bối cảnh
Câu lạc bộ cờ của trường tổ chức trò chơi tìm cặp số nguyên $(x, y)$ thỏa mãn đẳng thức $x^2 - d\cdot y^2 = 1$ với số $d$ cho trước. Đội nào tìm được cặp nghiệm dương nhỏ nhất sẽ thắng, vì đó là "chìa khóa" mở ra mọi nghiệm còn lại của đẳng thức này.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho số nguyên dương $d$. Hãy lập trình tìm nghiệm nguyên dương nhỏ nhất $(x, y)$ của phương trình $x^2 - d\cdot y^2 = 1$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Phuong Trinh Pell Co Ban.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
