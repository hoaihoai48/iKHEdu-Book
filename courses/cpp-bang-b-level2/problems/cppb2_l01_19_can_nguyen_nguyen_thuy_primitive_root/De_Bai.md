# Căn Nguyên Nguyên Thủy (Primitive Root)

## Bối cảnh
Để tạo mật khẩu dùng một lần cho hệ thống điểm danh của trường, thầy tin học chọn một số nguyên tố $p$ rồi tìm một "số sinh" $g$: chỉ cần nhân $g$ với chính nó nhiều lần rồi lấy phần dư theo $p$, ta sẽ lần lượt tạo ra mọi số từ $1$ đến $p - 1$. Số sinh nhỏ nhất như vậy giúp thiết bị điểm danh đời cũ tính toán nhẹ nhàng nhất.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho một số nguyên tố $p$. Hãy lập trình tìm căn nguyên thủy nhỏ nhất của $p$, tức số nguyên $g \ge 2$ nhỏ nhất mà các lũy thừa của $g$ sinh ra mọi số $1, 2, \dots, p-1$ theo modulo $p$.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Can Nguyen Nguyen Thuy Primitive Root.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
