# XOR Basis trong Không Gian Vectơ Tuyến Tính

## Bối cảnh
Phòng thí nghiệm tín hiệu thu được một dãy số nguyên từ các cảm biến, mỗi số được xem như một vectơ nhị phân. Kỹ sư muốn biết dãy này thực chất chứa bao nhiêu tín hiệu độc lập, tức hạng của cả họ vectơ trên trường $GF(2)$.

Anh lần lượt đưa từng số vào một bộ khung cơ sở, khử dần các bit cao nhất đã có đại diện, và chỉ giữ lại những số mang thông tin thực sự mới cho bộ cơ sở.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên. Hãy lập trình xây dựng cơ sở XOR của dãy và cho biết số vector độc lập tuyến tính tối đa (hạng của họ vector trên trường $GF(2)$).

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
* Thuật toán khởi tạo cấu trúc dữ liệu, duyệt và tính toán kết quả tối ưu của Xor Basis Vector Khong Gian Tuyen Tinh.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
