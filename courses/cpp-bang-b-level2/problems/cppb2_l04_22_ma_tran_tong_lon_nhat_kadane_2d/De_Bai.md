# Ma Trận Tổng Lớn Nhất (Kadane 2D)

## Bối cảnh

Bác nông dân có cánh đồng hình chữ nhật, mỗi ô có thể lãi hoặc lỗ tùy mùa vụ. Vụ này bác muốn khoanh một vùng hình chữ nhật có tổng lợi nhuận lớn nhất để tập trung đầu tư.

Bác ghi lại lợi nhuận từng ô rồi so sánh các vùng có thể khoanh được.

## Nhiệm vụ

Cho ma trận số nguyên. Hãy lập trình tìm tổng lớn nhất của một hình chữ nhật con bất kỳ trong ma trận.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Ma Tran Tong Lon Nhat Kadane 2d.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
