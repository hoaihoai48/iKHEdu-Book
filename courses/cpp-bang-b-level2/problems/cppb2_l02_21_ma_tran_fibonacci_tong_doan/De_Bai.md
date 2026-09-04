# Ma Trận Fibonacci Tổng Đoạn

## Bối cảnh
Vườn ươm của trường đánh số các luống cây từ $1$ trở đi, luống thứ $i$ trồng đúng $F_i$ cây con theo dãy Fibonacci. Cuối vụ, thầy phụ trách cần tổng số cây trên các luống từ $l$ đến $r$ (chỉ lấy phần dư khi chia cho $10^9+7$) để quyết toán tiền giống.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho đoạn $[l, r]$. Hãy lập trình tính tổng $F_l + F_{l+1} + \dots + F_r$ các số Fibonacci trong đoạn theo modulo $10^9+7$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Ma Tran Fibonacci Tong Doan.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
