# Đếm Số Phần Tử Phân Biệt Trong Cửa Sổ K

## Bối cảnh
Một máy quét giám sát an ninh quét qua một chuỗi $N$ mã số xe lưu thông trên đường cao tốc. Máy quét sử dụng một khung quan sát (cửa sổ trượt) có kích thước cố định là $K$ xe liên tiếp. Khi cửa sổ trượt dịch chuyển từng vị trí từ đầu đến cuối hàng xe, hệ thống cần đếm xem trong mỗi cửa sổ hiện tại có bao nhiêu mã số xe phân biệt nhau.

## Nhiệm vụ
Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình in ra số lượng phần tử phân biệt trong mỗi cửa sổ kích thước $K$ khi trượt từ trái sang phải.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N - K + 1$ số nguyên là số phần tử phân biệt trong từng cửa sổ, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
7 4
1 2 1 3 4 2 3
```
### Output
```text
3 4 4 3
```

### Giải thích
Với mảng gồm 7 phần tử $[1, 2, 1, 3, 4, 2, 3]$ và kích thước cửa sổ $K = 4$:

- Cửa sổ 1 [1, 2, 1, 3]: gồm các giá trị phân biệt {1, 2, 3} $\to$ 3 phần tử.
- Cửa sổ 2 [2, 1, 3, 4]: gồm {1, 2, 3, 4} $\to$ 4 phần tử.
- Cửa sổ 3 [1, 3, 4, 2]: gồm {1, 2, 3, 4} $\to$ 4 phần tử.
- Cửa sổ 4 [3, 4, 2, 3]: gồm {2, 3, 4} $\to$ 3 phần tử.
Kết quả in ra: 3 4 4 3.

## Ràng buộc
- $100\%$ số test có $1 \le K \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
