# Cập Nhật Cộng Đoạn Tuyến Tính (Mảng Hiệu)

## Bối cảnh
Một tuyến đê biển dài được chia thành N phân đoạn ban đầu có độ cao gia cố bằng 0. Trải qua Q đợt bồi đắp phù sa, mỗi đợt người ta gia cố thêm một lượng đất đá X trên đoạn từ cọc L đến cọc R. Kỹ sư thủy lợi cần biết độ cao cuối cùng của toàn bộ N phân đoạn đê sau khi hoàn thành tất cả Q đợt gia cố.

## Nhiệm vụ
Cho mảng N số nguyên ban đầu toàn số 0. Thực hiện Q thao tác cộng giá trị X vào đoạn [L, R]. Hãy in ra mảng kết quả cuối cùng sau Q thao tác bằng kỹ thuật Mảng hiệu.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng chứa 3 số nguyên $L, R, X$ ($1 \le L \le R \le N, -10^9 \le X \le 10^9$).

## Output
- In ra $N$ số nguyên trên một dòng biểu diễn mảng sau khi hoàn thành toàn bộ $Q$ thao tác.

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
### Giải thích
Sử dụng mảng hiệu D kích thước N + 2:
- Cộng 2 vào [1, 3]: D[1] += 2, D[4] -= 2.
- Cộng 3 vào [2, 5]: D[2] += 3, D[6] -= 3.
- Cộng -1 vào [3, 4]: D[3] -= 1, D[5] += 1.
Tính tổng tiền tố của D để thu được mảng kết quả: 2 5 4 2 3.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
