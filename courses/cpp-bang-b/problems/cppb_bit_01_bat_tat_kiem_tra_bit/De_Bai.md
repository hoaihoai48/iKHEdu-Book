# Bật, Tắt Và Kiểm Tra Bit Thứ K

## Bối cảnh
Trong kiến trúc hệ điều hành nhúng, thanh ghi trạng thái phần cứng của vi điều khiển được biểu diễn dưới dạng số nguyên không âm N (64-bit). Mỗi bit thứ k đại diện cho trạng thái của một cổng kết nối cảm biến ngoại vi (1 là đang bật, 0 là đang tắt). Người lập trình viên nhận Q lệnh điều khiển từ xa để thao tác trực tiếp trên các bit của thanh ghi.

## Nhiệm vụ
Cho số nguyên không âm N và Q thao tác: loại 1 (bật bit thứ k), loại 2 (tắt bit thứ k), loại 3 (kiểm tra trạng thái bit thứ k). Với thao tác loại 3, in ra 1 nếu bit đang bật, ngược lại in 0.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($0 \le N \le 10^{18}, 1 \le Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 2 số nguyên thể hiện loại thao tác và chỉ số bit $k$ ($0 \le k \le 62$).

## Output
- Với mỗi thao tác loại 3, in ra kết quả trên một dòng.

## Sample 1
### Input
```text
5 4
3 0
3 1
1 1
3 1
```
### Output
```text
1
0
1
```
### Giải thích
N = 5 có biểu diễn nhị phân là 101_2:
- Thao tác 3 0: Bit thứ 0 có giá trị 1 -> in 1.
- Thao tác 3 1: Bit thứ 1 có giá trị 0 -> in 0.
- Thao tác 1 1: Bật bit thứ 1 lên 1 -> N trở thành 111_2 = 7.
- Thao tác 3 1: Bit thứ 1 hiện tại là 1 -> in 1.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
