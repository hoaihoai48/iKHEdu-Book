# Đếm Nghịch Thế 3 Chiều bằng CDQ

## Bối cảnh
Phòng đào tạo lưu hồ sơ mỗi học viên dưới dạng một bộ ba chỉ số: thứ tự nộp bài cùng hai loại điểm thành phần. Thầy hiệu phó muốn đếm có bao nhiêu cặp học viên mà người nộp trước lại xếp sau ở cả hai loại điểm, để phát hiện những trường hợp tiến bộ vượt bậc.

Với hàng trăm nghìn bộ ba, việc so sánh từng cặp là quá chậm, nên phòng kỹ thuật chia hồ sơ thành từng đợt theo thứ tự nộp bài rồi lần lượt gộp và đếm chéo giữa các đợt.

## Nhiệm vụ
Cho tập gồm $N$ bộ ba số nguyên. Hãy lập trình đếm số cặp nghịch thế ba chiều, tức các cặp $(i, j)$ với $i < j$ thỏa mãn điều kiện thứ tự trên cả ba chiều.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Dem Nghich The 3 Chieu Cdq.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
