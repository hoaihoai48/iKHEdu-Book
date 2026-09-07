# Multiset interval management

## Bối cảnh
Cho dữ liệu bài toán liên quan đến **Multiset Interval Management**. Cần thiết kế thuật toán tối ưu để xử lý nhanh chóng trong giới hạn thời gian $1.0\text{s}$.

## Nhiệm vụ
Cho q truy vấn trên các đoạn số nguyên: loại 1 thêm đoạn [l, r] và hợp nhất các đoạn giao nhau, loại 2 hỏi đoạn [l, r] có bị phủ kín hay không. Hãy lập trình xử lý lần lượt các truy vấn và in ra YES/NO cho mỗi truy vấn loại 2.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Multiset Interval Management.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
