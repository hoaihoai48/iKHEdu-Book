# Tính Ước Nguyên Tố Lớn Nhất

## Bối cảnh
Xưởng tái chế của khu phố nhận về một lô kiện hàng, mỗi kiện dán một con số. Máy phân loại sẽ tách mỗi con số thành các thừa số nguyên tố, và kiện nào có thừa số nguyên tố lớn nhất thì được đưa vào dây chuyền xử lý đặc biệt. Người quản đốc cần biết con số lớn nhất mà máy sẽ gặp trong cả lô hàng hôm nay.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho $n$ số nguyên. Hãy lập trình tìm ước nguyên tố lớn nhất của mỗi số, rồi in ra giá trị lớn nhất trong số đó.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Tinh Uoc Nguyen To Lon Nhat.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
