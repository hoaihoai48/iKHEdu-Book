# Sinh Chuỗi Số Nhị Phân Bằng Queue

## Bối cảnh
Một chip tạo mã nhị phân cần xuất ra liên tục danh sách biểu diễn nhị phân của các số tự nhiên từ $1$ đến $N$ theo thứ tự tăng dần (ví dụ: với $N = 3$, danh sách là `1`, `10`, `11`). Nhờ tính chất hàng đợi, mỗi khi lấy ra một chuỗi nhị phân $S$, ta có thể dễ dàng tạo ra hai chuỗi nhị phân kế tiếp bằng cách ghép thêm ký tự `'0'` và `'1'` vào cuối.

## Nhiệm vụ
Cho số nguyên dương $N$. Hãy lập trình sinh và in ra chuỗi biểu diễn nhị phân của tất cả các số từ $1$ đến $N$, các chuỗi cách nhau bởi khoảng trắng.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^4$).

## Output
- In ra trên một dòng gồm $N$ chuỗi nhị phân tương ứng theo thứ tự tăng dần.

## Sample 1
### Input
```text
4
```
### Output
```text
1 10 11 100
```

### Giải thích
Với $N = 5$, danh sách biểu diễn nhị phân của các số từ 1 đến 5 là: 1 (số 1), 10 (số 2), 11 (số 3), 100 (số 4), 101 (số 5).

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
