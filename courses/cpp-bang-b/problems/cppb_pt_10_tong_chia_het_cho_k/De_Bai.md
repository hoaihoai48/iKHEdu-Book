# Đoạn Con Có Tổng Chia Hết Cho K

## Bối cảnh
Một chuỗi các container hàng hóa có khối lượng A1, A2, ..., An cần được xếp lên các chuyến tàu vận tải, trong đó mỗi chuyến tàu chỉ có thể chở đúng các lô hàng có tổng khối lượng chia hết cho K tấn để đảm bảo cân bằng trọng tải đáy tàu. Hãy đếm xem có bao nhiêu đoạn con container liên tiếp có tổng khối lượng chia hết cho K.

## Nhiệm vụ
Cho mảng gồm N số nguyên và số nguyên dương K. Hãy đếm số lượng đoạn con liên tiếp có tổng chia hết cho K.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 2 \cdot 10^5, 1 \le K \le 10^9$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra một số nguyên duy nhất là số lượng đoạn con thỏa mãn.

## Sample 1
### Input
```text
5 3
1 2 3 4 5
```
### Output
```text
4
```
### Giải thích
Các đoạn con liên tiếp có tổng chia hết cho 3 là: [1, 2] (tổng 3), [3] (tổng 3), [4, 5] (tổng 9), và [1, 2, 3] (tổng 6). Tổng cộng có 4 đoạn con thỏa mãn.

## Ràng buộc
- $100\%$ số test có $N \le 2 \cdot 10^5, K \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
