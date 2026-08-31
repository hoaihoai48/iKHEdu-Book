# Tìm Kiếm Nhị Phân Bằng Đệ Quy (Cầu Nối Sang D&C)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên $A$ gồm $N$ phần tử đã được sắp xếp tăng dần và số nguyên $X$. Hãy sử dụng hàm đệ quy Chia Để Trị `binarySearchDac(l, r, x)` để tìm vị trí xuất hiện đầu tiên của $X$ trong mảng (chỉ số 1-based). Nếu không tìm thấy, in ra `-1`.

## Input
- Dòng 1: Hai số nguyên $N, X$ ($1 \le N \le 10^5, |X| \le 10^9$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ đã sắp xếp tăng dần ($|A_i| \le 10^9$).

## Output
- In ra vị trí 1-based của $X$ trong mảng, hoặc `-1` nếu không tồn tại.

## Sample 1
### Input
```text
5 7
1 3 5 7 9
```
### Output
```text
4
```
### Giải thích
Số 7 xuất hiện tại vị trí thứ 4 trong mảng.

## Ràng buộc
- 100% số test có $N \le 10^5, |A_i| \le 10^9$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
