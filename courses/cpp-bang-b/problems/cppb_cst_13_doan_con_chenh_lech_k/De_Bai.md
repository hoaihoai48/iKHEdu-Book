# Đoạn Con Có Độ Chênh Lệch Max - Min Không Quá K

## Bối cảnh
Trong một dây chuyền sản xuất vi thấu kính chính xác cao, các thấu kính đi qua cảm biến đo độ dày lần lượt ghi nhận các số đo A1, A2, ..., An. Một kiện hàng đóng gói hợp chuẩn đòi hỏi các thấu kính liên tiếp trong cùng một lô phải có độ chênh lệch giữa thấu kính dày nhất và mỏng nhất không vượt quá dung sai K. Nhà máy cần tìm lô sản phẩm liên tiếp dài nhất thỏa mãn yêu cầu dung sai này.

## Nhiệm vụ
Cho mảng gồm N số nguyên và số nguyên không âm K. Hãy tìm độ dài lớn nhất của đoạn con liên tiếp sao cho chênh lệch giữa phần tử lớn nhất và phần tử nhỏ nhất trong đoạn không vượt quá K: max(đoạn) - min(đoạn) <= K.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le N \le 10^5, 0 \le K \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra độ dài lớn nhất của đoạn con tìm được.

## Sample 1
### Input
```text
6 2
1 3 6 7 9 4
```
### Output
```text
2
```
### Giải thích
Với dung sai K = 2, các đoạn con liên tiếp có chênh lệch max - min <= 2 là [1, 3] (3 - 1 = 2) hoặc [6, 7] (7 - 6 = 1). Độ dài lớn nhất của đoạn con hợp lệ là 2.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
