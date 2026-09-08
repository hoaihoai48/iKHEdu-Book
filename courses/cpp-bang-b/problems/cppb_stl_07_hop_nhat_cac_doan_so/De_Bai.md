# Hợp Nhất Các Đoạn Số (Merge Intervals)

## Bối cảnh
Một máy chủ lập lịch tiếp nhận $N$ khoảng thời gian đặt lịch phòng họp, khoảng thời gian thứ $i$ bắt đầu từ thời điểm $L_i$ và kết thúc tại $R_i$. Một số khoảng thời gian bị chồng lấn (giao nhau) hoặc tiếp xúc liền kề. Ban quản trị tòa nhà cần hợp nhất tất cả các khoảng thời gian bị giao nhau lại thành các khối thời gian liền mạch độc lập.

## Nhiệm vụ
Cho danh sách $N$ khoảng thời gian $[L_i, R_i]$. Hãy lập trình hợp nhất các khoảng giao nhau và in ra danh sách các khoảng thời gian sau khi đã hợp nhất theo thứ tự thời điểm bắt đầu tăng dần.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $L_i$ và $R_i$ ($0 \le L_i \le R_i \le 10^9$).

## Output
- Dòng 1: In ra số lượng khoảng thời gian $M$ sau khi hợp nhất.
- $M$ dòng tiếp theo, mỗi dòng in ra hai số nguyên là điểm đầu và điểm cuối của một khoảng.

## Sample 1
### Input
```text
4
1 3
2 6
8 10
15 18
```
### Output
```text
3
1 6
8 10
15 18
```

### Giải thích
Với các khoảng thời gian $[1, 3], [2, 6], [8, 10], [15, 18]$:

- Khoảng $[1, 3]$ và $[2, 6]$ giao nhau vì $2 \le 3$, hợp nhất thành khoảng $[1, 6]$.
- Các khoảng $[8, 10]$ và $[15, 18]$ độc lập không giao nhau.
Kết quả thu được 3 khoảng: $[1, 6], [8, 10], [15, 18]$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le L_i \le R_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
