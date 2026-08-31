# Đổi Tiền Xu Ít Nhất (B&B Coin Change)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho $N$ mệnh giá tiền xu $C_1, C_2, \dots, C_N$ (số lượng mỗi loại không giới hạn) và số tiền cần đổi $S$. Hãy tìm số lượng đồng xu ít nhất để đổi đúng số tiền $S$ bằng thuật toán Nhánh Cận (Branch and Bound). Nếu không đổi được, in `-1`.

## Input
- Dòng 1: Hai số nguyên $N, S$ ($1 \le N \le 15, 1 \le S \le 100$).
- Dòng 2: $N$ số nguyên dương $C_1, \dots, C_N$ ($1 \le C_i \le 100$).

## Output
- In ra số đồng xu ít nhất, hoặc `-1`.

## Sample 1
### Input
```text
3 11
1 2 5
```
### Output
```text
3
```
### Giải thích
11 = 5 + 5 + 1 (dùng đúng 3 đồng xu).

## Ràng buộc
- 100% số test có $N \le 15, S \le 100$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
