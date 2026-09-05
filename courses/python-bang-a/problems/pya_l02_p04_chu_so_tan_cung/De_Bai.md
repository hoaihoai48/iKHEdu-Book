# Lấy chữ số tận cùng

## Bối cảnh
Tại hội chợ Xuân, mỗi du khách được phát một tấm vé số may mắn mang một số nguyên dương. Theo luật chơi, giải thưởng phụ thuộc vào chữ số cuối cùng (hàng đơn vị) của tấm vé: nếu tận cùng là 0 hoặc 5 thì trúng quà, còn lại thì không. Hệ thống cần trích xuất chính xác chữ số hàng đơn vị từ số trên tấm vé để tự động phân loại trúng thưởng.


## Nhiệm vụ
Nhập số nguyên dương $N$. In ra chữ số hàng đơn vị của $N$.

## Input
Một dòng chứa số nguyên $N$ ($1 \le N \le 10^9$).

## Output
In ra chữ số tận cùng của $N$.

## Sample 1
### Input
```text
2026
```
### Output
```text
6
```
### Giải thích
$2026 \% 10 = 6$.
