# Hàng Đợi Ưu Tiên K Phần Tử Lớn Nhất

## Bối cảnh
Một nền tảng phát video trực tuyến theo dõi luồng tương tác của khán giả với hàng triệu lượt đánh giá. Trong luồng dữ liệu liên tục gồm $N$ lượt đánh giá điểm số, ban biên tập cần liên tục lọc ra danh sách $K$ lượt đánh giá có điểm số cao nhất để hiển thị lên bảng tin trang chủ.

## Nhiệm vụ
Cho danh sách gồm $N$ số nguyên và số nguyên dương $K$. Hãy lập trình tìm và in ra $K$ phần tử lớn nhất trong dãy theo thứ tự giảm dần.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $K$ số nguyên lớn nhất theo thứ tự giảm dần, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
6 3
10 50 30 20 60 40
```
### Output
```text
60 50 40
```

### Giải thích
Với mảng gồm 6 phần tử $[3, 2, 1, 5, 6, 4]$ và cần lấy $K = 2$ phần tử lớn nhất:
Hai phần tử lớn nhất trong dãy là 6 và 5. In ra theo thứ tự giảm dần: 6 5.

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
