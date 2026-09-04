# Bitmask DP Phân Nhóm K Tập

## Bối cảnh
Huấn luyện viên có $N$ vận động viên và cần chia thành đúng $K$ đội, mỗi cách xếp đội đều tốn một chi phí cho trước tùy vào thành phần đội hình. Mục tiêu là tìm cách chia sao cho tổng chi phí của cả $K$ đội là nhỏ nhất.

Vì số cách chia tăng rất nhanh, ban huấn luyện đánh số mỗi nhóm vận động viên bằng một mặt nạ bit rồi điền dần bảng phương án tốt nhất cho từng mặt nạ với từng số đội đã xếp.

## Nhiệm vụ
Cho tập gồm $N$ phần tử, một số nguyên $K$ và cách tính chi phí của mỗi nhóm. Hãy lập trình chia tập đã cho thành đúng $K$ nhóm sao cho tổng chi phí là nhỏ nhất.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Bitmask Dp Phan Nhom K Tap.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
