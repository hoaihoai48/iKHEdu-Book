# Lũy Thừa Ma Trận Đếm Đường Đi

## Bối cảnh
Bản đồ du lịch của huyện có $n$ điểm tham quan nối với nhau bằng $m$ con đường hai chiều. Hội thi "phượt thủ" thách mỗi đội lên lịch trình đúng $k$ chặng đường đi từ điểm $u$ đến điểm $v$ (được quay lại điểm cũ), và ban tổ chức cần đếm xem có tất cả bao nhiêu lịch trình như vậy.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho đồ thị vô hướng gồm $n$ đỉnh, $m$ cạnh cùng hai đỉnh $u, v$ và độ dài $k$. Hãy lập trình đếm số đường đi (được phép lặp đỉnh, lặp cạnh) có độ dài đúng $k$ từ $u$ đến $v$ theo modulo $10^9+7$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Luy Thua Ma Tran Dem Duong Di.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
