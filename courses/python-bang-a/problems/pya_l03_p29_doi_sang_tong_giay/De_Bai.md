# Đổi giờ - phút - giây sang tổng số giây

## Bối cảnh
Bài toán ngược lại: Cần quy đổi thời gian hiển thị `H giờ M phút S giây` về một số giây duy nhất để máy tính dễ so sánh.

## Nhiệm vụ
Nhập 3 số nguyên $H, M, S$ trên cùng 1 dòng ($0 \le H \le 1000$, $0 \le M, S < 60$). In ra tổng số giây.

## Input
Một dòng chứa 3 số nguyên $H, M, S$.

## Output
In ra một số nguyên là tổng số giây.

## Sample 1
### Input
```text
2 15 30
```
### Output
```text
8130
```
### Giải thích
$2 \times 3600 + 15 \times 60 + 30 = 7200 + 900 + 30 = 8130$.

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
