# Ngày trong tuần

## Bối cảnh
Quy ước Chủ Nhật là ngày 0, Thứ Hai là ngày 1, ..., Thứ Bảy là ngày 6. Hôm nay là ngày $D$.

## Nhiệm vụ
Nhập ngày hiện tại $D$ ($0 \le D \le 6$) và số ngày trôi qua $N$ ($0 \le N \le 10^9$). In ra thứ tương ứng sau $N$ ngày.

## Input
Một dòng chứa hai số nguyên $D$ và $N$.

## Output
In ra mã số ngày trong tuần (từ 0 đến 6).

## Sample 1
### Input
```text
1 10
```
### Output
```text
4
```
### Giải thích
Thứ Hai là ngày 1. Sau 10 ngày nữa: $(1 + 10) \% 7 = 11 \% 7 = 4$ (tức Thứ Năm).

## Ràng buộc
* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
