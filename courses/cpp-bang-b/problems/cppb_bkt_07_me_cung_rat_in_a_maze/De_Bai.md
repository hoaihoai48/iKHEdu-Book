# Mê Cung (Rat in a Maze): Tìm Mọi Đường Đi

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mê cung $N \times N$ gồm các ô `1` (đi được) và `0` (tường đá). Con chuột xuất phát từ ô $(0, 0)$ cần đi tới ô $(N-1, N-1)$. Mỗi bước chỉ được đi sang các ô kề cạnh (Down `D`, Left `L`, Right `R`, Up `U`). Hãy in ra tất cả các đường đi hợp lệ theo thứ tự từ điển (`D < L < R < U`). Nếu không có đường đi, in `-1`.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 8$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên `0` hoặc `1`.

## Output
- In ra các xâu ký tự đại diện cho các đường đi tìm được (mỗi đường trên một dòng), hoặc `-1`.

## Sample 1
### Input
```text
4
1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1
```
### Output
```text
DDRDRR
DRDDRR
```
### Giải thích
Có 2 đường đi từ (0,0) đến (3,3): DDRDRR và DRDDRR.

## Ràng buộc
- 100% số test có $2 \le N \le 8$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
