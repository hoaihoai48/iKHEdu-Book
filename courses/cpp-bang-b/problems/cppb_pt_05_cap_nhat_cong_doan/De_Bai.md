# Cập Nhật Cộng Đoạn Tuyến Tính (Mảng Hiệu)

## Bối cảnh
Cho một dãy gồm $N$ số nguyên ban đầu toàn số 0. Có $Q$ thao tác, mỗi thao tác gồm 3 số $L, R, V$ yêu cầu cộng thêm $V$ vào tất cả các phần tử từ chỉ số $L$ đến $R$.

## Nhiệm vụ
Hãy in ra dãy số cuối cùng sau khi đã thực hiện xong toàn bộ $Q$ thao tác.

## Input
- Dòng 1: Gồm 2 số nguyên $N, Q$ ($1 \le N, Q \le 2 \cdot 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 3 số nguyên $L, R, V$ ($1 \le L \le R \le N, |V| \le 10^9$).

## Output
- In ra $N$ số nguyên trên một dòng biểu diễn mảng sau $Q$ thao tác, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5 3
1 3 2
2 5 3
3 4 -1
```
### Output
```text
2 5 4 2 3
```

## Ràng buộc
- $100\%$ số test có $N, Q \le 2 \cdot 10^5, |V| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
