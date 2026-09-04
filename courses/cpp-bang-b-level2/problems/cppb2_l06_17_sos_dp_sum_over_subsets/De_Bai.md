# SOS DP Tổng Trên Tập Con Cơ Bản

## Bối cảnh
Phòng khảo sát lưu điểm số cho từng nhóm đối tượng, mỗi nhóm được mã hóa thành một tập con của $N$ đặc trưng. Với mỗi nhóm lớn, phòng cần tính tổng điểm của mọi nhóm nhỏ nằm gọn trong nó để lập báo cáo cộng dồn.

Vì số nhóm lên tới $2^N$, việc cộng lại từ đầu cho từng nhóm là không xuể, nên phòng cần một bảng cộng dồn lan dần theo từng đặc trưng để mỗi nhóm lớn đều tra được đáp án ngay.

## Nhiệm vụ
Cho một hàm $F$ xác định trên mọi tập con của tập $N$ phần tử. Với mỗi mặt nạ $mask$, hãy lập trình tính tổng $F[sub]$ trên mọi tập con $sub$ của $mask$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Sos Dp Sum Over Subsets.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
