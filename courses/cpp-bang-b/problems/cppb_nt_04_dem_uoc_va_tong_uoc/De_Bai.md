# Đếm Số Lượng & Tính Tổng Các Ước Số

## Bối cảnh
Trong nghiên cứu lý thuyết số giải thuật, hàm số lượng ước d(N) và hàm tổng các ước sigma(N) đóng vai trò then chốt trong việc phân loại số phong phú, số hoàn hảo và số khuyết thiếu. Hãy tính giá trị của hai hàm này cho số nguyên dương N.

## Nhiệm vụ
Cho số nguyên dương N. Hãy tính số lượng ước số nguyên dương d(N) và tổng tất cả các ước số nguyên dương của N.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).

## Output
- In ra 2 số nguyên cách nhau bởi khoảng trắng: số lượng ước và tổng các ước.

## Sample 1
### Input
```text
12
```
### Output
```text
6 28
```
### Giải thích
Các ước số của 12 là {1, 2, 3, 4, 6, 12}, tổng cộng có 6 ước. Tổng các ước là 1 + 2 + 3 + 4 + 6 + 12 = 28. Kết quả in ra: 6 28.

## Ràng buộc
- $100\%$ số test có $N \le 10^{12}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
