# Căn Bậc Hai theo modulo bằng Tonelli-Shanks

## Bối cảnh
Két sắt của phòng y tế mở bằng một số $x$ mà bình phương của nó chia cho số nguyên tố $p$ còn dư đúng $n$. Quy định của trường yêu cầu luôn ghi lại chiếc chìa nhỏ hơn trong cặp chìa đối nhau; nếu không có chiếc chìa nào mở được thì ghi $-1$.

Dữ liệu đầu vào của bài toán thỏa mãn các ràng buộc đã cho. Hãy lập trình tìm kết quả chính xác theo yêu cầu.

## Nhiệm vụ
Cho cặp $(n, p)$ với $p$ nguyên tố. Hãy lập trình tìm căn bậc hai của $n$ theo modulo $p$ (in nghiệm nhỏ hơn trong cặp nghiệm đối nhau); in `-1` nếu không tồn tại.

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Can Bac Hai Modulo Tonelli Shanks.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
