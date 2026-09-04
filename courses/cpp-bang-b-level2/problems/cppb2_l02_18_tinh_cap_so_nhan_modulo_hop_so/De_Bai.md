# Tính Cấp Số Nhân theo modulo Hợp Số

## Bối cảnh
Cửa hàng xếp ly giấy thành chồng cao dần: tầng thứ $i$ có đúng $a^i$ chiếc ly, xếp tới tầng thứ $n$. Vì tổng số ly quá lớn, chủ cửa hàng chỉ ghi lại phần dư khi chia cho $m$ để ước lượng số thùng cần dùng.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho ba số $a, n, m$. Hãy lập trình tính $S = 1 + a + a^2 + \dots + a^n$ theo modulo $m$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Tinh Cap So Nhan Modulo Hop So.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
