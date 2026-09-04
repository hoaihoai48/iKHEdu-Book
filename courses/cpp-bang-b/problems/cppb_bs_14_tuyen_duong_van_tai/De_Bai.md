# Tối Ưu Hóa Tuyến Đường Vận Tải Đa Điểm

## Bối cảnh
Trên trục đường liên tỉnh dài, có N thành phố nối tiếp nhau từ 1 đến N. Tại thành phố thứ i có nhu cầu tiếp nhận Ai tấn hàng hóa. Một đội tàu vận tải gồm K đoàn tàu xuất phát từ ga đầu mối cần chia sẻ vận chuyển hàng đến các thành phố. Để không gây quá tải cho các đoàn tàu, cơ quan điều vận cần tìm mức tải trọng trần nhỏ nhất để K đoàn tàu vận chuyển trọn vẹn toàn bộ hàng hóa.

## Nhiệm vụ
Cho mảng N số nguyên và số nguyên K. Hãy tìm giá trị cận trên tải trọng nhỏ nhất cho mỗi đoàn tàu.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).

## Output
- In ra giá trị cận trên tải trọng tối ưu nhỏ nhất.

## Sample 1
### Input
```text
4 2
1 2 3 4
```
### Output
```text
6
```
### Giải thích
Chia thành 2 đoàn: [1, 2, 3] có tổng 6 và [4] có tổng 4. Mức tải trọng lớn nhất giữa hai đoàn là 6. Đây là mức tải trọng trần nhỏ nhất có thể đạt được.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
