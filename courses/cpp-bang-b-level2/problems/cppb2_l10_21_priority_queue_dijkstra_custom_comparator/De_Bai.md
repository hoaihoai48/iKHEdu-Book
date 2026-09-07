# Priority queue Dijkstra custom comparator

## Bối cảnh
Cho dữ liệu bài toán liên quan đến **Priority Queue Dijkstra Custom Comparator**. Cần thiết kế thuật toán tối ưu để xử lý nhanh chóng trong giới hạn thời gian $1.0\text{s}$.

## Nhiệm vụ
Cho đồ thị có hướng gồm n đỉnh và m cạnh có trọng số không âm. Hãy lập trình tìm đường đi ngắn nhất từ đỉnh 1 tới đỉnh n và in ra khoảng cách đó (in -1 nếu không tới được).

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Priority Queue Dijkstra Custom Comparator.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
