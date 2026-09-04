# Centroid Decomposition Cơ Bản

## Bối cảnh
Công ty giao hàng nhanh quản lý một mạng lưới kho bãi nối với nhau thành một cây phân phối, mỗi kho là một đỉnh và mỗi tuyến đường là một cạnh. Mỗi ngày, tổng đài nhận hàng loạt truy vấn kiểu "kho nào gần đơn hàng nhất" hay "có bao nhiêu kho trong phạm vi phục vụ", đòi hỏi trả lời thật nhanh trên cây có tới hàng trăm nghìn đỉnh.

Để không phải duyệt cả cây cho mỗi truy vấn, đội kỹ thuật chia nhỏ mạng lưới theo từng cụm cân bằng quanh các kho trung tâm, rồi xử lý truy vấn bằng cách leo dần qua các tầng cụm lồng nhau.

## Nhiệm vụ
Cho dữ liệu mô tả một cây gồm $N$ đỉnh và các yêu cầu truy vấn trên cây. Hãy lập trình xử lý và in ra đáp án cho từng truy vấn.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Centroid Decomposition Co Ban.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
