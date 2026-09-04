# Chia Tập Thành 2 Phần Có Tổng Bằng Nhau

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Trong ngày hội thể thao iKH-Games, ban tổ chức tiếp nhận $N$ thùng dụng cụ thể thao có khối lượng lần lượt là $A_1, A_2, \dots, A_N$. Để vận chuyển lên hai chiếc xe tải cùng một chuyến đi, tổng khối lượng hàng hóa trên mỗi xe bắt buộc phải bằng nhau tuyệt đối nhằm đảm bảo cân bằng tải trọng và an toàn giao thông đường đèo dốc.

## Nhiệm vụ
Cho mảng số nguyên dương $A$ gồm $N$ phần tử. Hãy xác định xem có thể chia toàn bộ $N$ phần tử thành hai tập con rời nhau sao cho tổng giá trị của hai tập con bằng nhau hay không. Nếu có thể chia được in `YES`, ngược lại in `NO`.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 20$).
- Dòng 2: $N$ số nguyên dương $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- In ra `YES` nếu có thể chia đều thành 2 phần bằng nhau, ngược lại in `NO`.

## Sample 1
### Input
```text
4
1 5 11 5
```
### Output
```text
YES
```
### Giải thích
Tổng khối lượng của tất cả các thùng là $1 + 5 + 11 + 5 = 22$. Nửa tổng là 11. Ta có thể chia thành 2 phần: tập thứ nhất gồm $\{1, 5, 5\}$ có tổng bằng 11 và tập thứ hai gồm $\{11\}$ có tổng bằng 11. Do đó đáp án là `YES`.

## Ràng buộc
- 100% số test có $1 \le N \le 20, 1 \le A_i \le 100$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
