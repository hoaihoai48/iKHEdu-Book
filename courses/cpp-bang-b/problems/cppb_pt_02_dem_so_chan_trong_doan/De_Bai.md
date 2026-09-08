# Đếm Số Lượng Số Chẵn Trong Đoạn

## Bối cảnh
Một máy quét an ninh tại sân bay kiểm tra mã barcode của N kiện hành lý liên tiếp. Để phân luồng vào băng chuyền đặc biệt, hệ thống cần đếm nhanh số lượng kiện hành lý mang mã số chẵn trong từng phân đoạn bưu kiện liên tiếp [L, R] qua Q đợt kiểm tra đột xuất.

## Nhiệm vụ
Cho dãy gồm N số nguyên. Hãy trả lời Q truy vấn [L, R], mỗi truy vấn yêu cầu đếm xem có bao nhiêu số chẵn trong đoạn từ vị trí L đến R.

## Input
- Dòng 1: Chứa 2 số nguyên dương $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 2 số nguyên $L$ và $R$ ($1 \le L \le R \le N$).

## Output
- In ra $Q$ dòng, mỗi dòng là số lượng số chẵn trong đoạn tương ứng.

## Sample 1
### Input
```text
6 3
2 3 4 6 7 8
1 4
2 5
1 6
```
### Output
```text
3
2
4
```
### Giải thích
Mảng nhị phân đánh dấu số chẵn: [1, 0, 1, 1, 0, 1]. Mảng tiền tố đếm số chẵn: [0, 1, 1, 2, 3, 3, 4].

- Đoạn [1, 4]: gồm {2, 3, 4, 6} có 3 số chẵn.
- Đoạn [2, 5]: gồm {3, 4, 6, 7} có 2 số chẵn.
- Đoạn [1, 6]: có 4 số chẵn.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
