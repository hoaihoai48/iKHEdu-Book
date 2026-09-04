# Đếm Tập Độc Lập Cực Đại

## Bối cảnh
Ban tổ chức hội thảo có sơ đồ xung đột giữa các diễn giả: hai người có cạnh nối thì không thể xếp chung một phiên. Ban tổ chức muốn liệt kê mọi danh sách diễn giả "kín lịch", tức đôi một không xung đột và không thể mời thêm bất kỳ ai mà vẫn giữ được tính chất này.

Vì số diễn giả tuy nhỏ nhưng số danh sách có thể bùng nổ, chương trình máy tính thử dần từng người theo kiểu quay lui, cắt bỏ sớm các nhánh chắc chắn trùng lặp để đếm đủ mọi danh sách kín lịch.

## Nhiệm vụ
Cho một đồ thị vô hướng gồm $N$ đỉnh (nhỏ). Hãy lập trình đếm số tập độc lập cực đại, tức các tập độc lập không thể thêm bất kỳ đỉnh nào mà vẫn giữ tính độc lập.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Tap Doc Lap Cuc Dai.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
