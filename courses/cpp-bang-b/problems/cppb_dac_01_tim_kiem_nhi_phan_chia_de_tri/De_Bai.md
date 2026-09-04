# Tìm Kiếm Nhị Phân Bằng Đệ Quy (Cầu Nối Sang D&C)

## Bối cảnh
Thuật toán tìm kiếm nhị phân chính là mô hình chia để trị nguyên bản và tinh gọn nhất: chia không gian tìm kiếm thành hai nửa bằng nhau, trị bài toán bằng cách so sánh phần tử ở giữa và loại bỏ hoàn toàn một nửa không gian. Hãy cài đặt tìm kiếm nhị phân bằng hàm chia để trị đệ quy.

## Nhiệm vụ
Cho mảng N số nguyên đã sắp xếp tăng dần và số nguyên X. Hãy tìm vị trí (1-indexed) của X bằng đệ quy chia để trị. Nếu không tìm thấy, in ra -1.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $X$ ($1 \le N \le 10^5, -10^9 \le X \le 10^9$).
- Dòng 2: Chứa $N$ số nguyên tăng dần $A_1 \le A_2 \le \dots \le A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra vị trí của $X$ (1-indexed), hoặc `-1`.

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
Số 7 nằm ở vị trí thứ 4 trong mảng đã sắp xếp. Kết quả in ra: 4.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
