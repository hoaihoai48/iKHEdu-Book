# Xếp Hàng Điểm Danh

## Bối cảnh
Trong buổi học thể dục đầu năm, thầy giáo muốn xếp hàng $N$ bạn học sinh theo thứ tự chiều cao từ thấp đến cao để chuẩn bị cho bài tập đồng diễn.

## Nhiệm vụ
Cho danh sách chiều cao của $N$ bạn học sinh. Hãy in ra danh sách chiều cao sau khi đã xếp hàng theo thứ tự tăng dần.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: Chứa $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^6$).

## Output
- In ra trên một dòng gồm $N$ số nguyên biểu diễn chiều cao sau khi sắp xếp tăng dần, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5
1550 1420 1680 1500 1600
```
### Output
```text
1420 1500 1550 1600 1680
```

### Giải thích
Chiều cao ban đầu của 5 bạn học sinh lần lượt là: $1550, 1420, 1680, 1500, 1600$ (đơn vị: mm).
Sau khi sắp xếp theo thứ tự chiều cao tăng dần từ thấp đến cao, thứ tự đứng vào hàng chuẩn xác sẽ là:
$1420 \le 1500 \le 1550 \le 1600 \le 1680$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 1000, 1 \le A_i \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
