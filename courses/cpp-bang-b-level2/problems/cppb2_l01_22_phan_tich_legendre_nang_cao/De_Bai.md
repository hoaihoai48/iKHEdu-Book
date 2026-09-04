# Phân Tích Legendre Nâng Cao

## Bối cảnh
Thủ kho của cửa hàng đồ chơi xếp các hộp quà thành dãy dài đánh số từ $1$ đến $N$ rồi lại xếp thêm một dãy nữa đến $M$. Cô muốn biết trong tích tất cả các số của cả hai dãy có tất cả bao nhiêu thừa số nguyên tố $P$ — tức số mũ của $P$ trong $N!$ cộng với số mũ của $P$ trong $M!$ — mà không cần nhân trực tiếp các số khổng lồ này.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho ba số nguyên $N, M, P$ với $P$ là số nguyên tố. Hãy lập trình tính tổng số mũ của $P$ trong phân tích của $N!$ và $M!$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Phan Tich Legendre Nang Cao.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
