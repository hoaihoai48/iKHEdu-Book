# Phần Tử Xuất Hiện Nhiều Nhất (Mode)

## Bối cảnh
Một hệ thống kiểm phiếu biểu quyết tiếp nhận $N$ lá phiếu được đánh mã số nguyên. Ban kiểm phiếu cần xác định giá trị mã số nào xuất hiện với tần suất nhiều nhất trong hòm phiếu (giá trị mốt - Mode). Nếu có nhiều mã số cùng đạt số phiếu cao nhất bằng nhau, hệ thống quy định sẽ ưu tiên chọn mã số có giá trị số học nhỏ nhất.

## Nhiệm vụ
Cho danh sách $N$ lá phiếu nguyên. Hãy lập trình tìm mã số xuất hiện nhiều lần nhất. Nếu có nhiều mã số cùng xuất hiện nhiều nhất, in ra mã số có giá trị nhỏ nhất trong số đó.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất giá trị mã số xuất hiện nhiều nhất theo quy ước trên.

## Sample 1
### Input
```text
6
1 3 2 1 4 1
```
### Output
```text
1 3
```

### Giải thích
Với dãy số $[1, 2, 2, 3, 1]$:
Cả hai số 1 và 2 đều xuất hiện đúng 2 lần (nhiều nhất). Theo quy định ưu tiên giá trị số học nhỏ hơn, ta chọn số 1. Kết quả in ra là 1.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
