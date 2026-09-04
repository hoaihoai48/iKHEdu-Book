# Bitmask Ghép Đôi Trọng Số Cực Đại

## Bối cảnh
Câu lạc bộ khiêu vũ có $2N$ thành viên đăng ký đêm hội, mỗi cặp đôi tiềm năng đều có một điểm tương hợp cho trước. Ban tổ chức cần ghép toàn bộ thành $N$ cặp sao cho tổng điểm tương hợp của cả đêm hội là lớn nhất.

Vì số cách ghép khổng lồ, chương trình máy tính ghi nhớ mặt nạ những người đã có đôi rồi thử từng bạn nhảy còn trống cho người đầu tiên chưa ghép, điền dần đáp án tốt nhất cho mọi mặt nạ.

## Nhiệm vụ
Cho $2N$ người và trọng số tương hợp của từng cặp. Hãy lập trình ghép thành $N$ cặp sao cho tổng trọng số của tất cả các cặp là lớn nhất.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Bitmask Ghep Doi Trong So Cuc Dai.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
