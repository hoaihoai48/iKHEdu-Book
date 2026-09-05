# Chữ số hàng chục

## Bối cảnh
Tại trạm kiểm soát tốc độ trên quốc lộ, camera ghi nhận biển số xe dưới dạng một số nguyên. Để phân loại phương tiện theo nhóm, hệ thống cần trích xuất chữ số ở hàng chục (vị trí thứ hai từ phải sang) của số đó. Ví dụ: số $1234$ có chữ số hàng chục là $3$, số $507$ có chữ số hàng chục là $0$. Em hãy lập trình giải quyết bài toán trích xuất này.


## Nhiệm vụ
Nhập số nguyên $N$ ($N \ge 10$). In ra chữ số hàng chục của $N$.

## Input
Một dòng chứa số nguyên $N$ ($10 \le N \le 10^9$).

## Output
In ra chữ số hàng chục.

## Sample 1
### Input
```text
378
```
### Output
```text
7
```
### Giải thích
Bỏ chữ số tận cùng: $378 // 10 = 37$. Lấy chữ số cuối của 37: $37 \% 10 = 7$.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
