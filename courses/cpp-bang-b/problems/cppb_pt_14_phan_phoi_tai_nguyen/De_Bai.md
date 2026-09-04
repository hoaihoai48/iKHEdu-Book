# Phân Phối Tài Nguyên Không Gian Tuyến Tính

## Bối cảnh
Một tuyến đường ống cấp nước đô thị dài N mét ban đầu lưu lượng nước bổ sung bằng 0. Trải qua Q lượt cấp nước bổ trợ dạng cấp số cộng: lượt thứ k cấp nước vào đoạn từ L đến R với lưu lượng tại mét L là V và mỗi mét tiếp theo tăng thêm D đơn vị lưu lượng (dạng cấp số cộng). Hãy xác định lượng nước phân phối cuối cùng tại mỗi mét đường ống.

## Nhiệm vụ
Cho dãy số N phần tử ban đầu toàn số 0. Thực hiện Q thao tác cộng vào đoạn [L, R] một dãy cấp số cộng với số hạng đầu V và công sai D. Hãy in ra mảng kết quả cuối cùng.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $Q$ ($1 \le N, Q \le 10^5$).
- $Q$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $L, R, V, D$ ($1 \le L \le R \le N, -10^9 \le V, D \le 10^9$).

## Output
- In ra $N$ số nguyên trên một dòng biểu diễn mảng sau khi hoàn thành $Q$ thao tác.

## Sample 1
### Input
```text
5 1
2 4 1 2
```
### Output
```text
0 1 3 5 0
```
### Giải thích
Thao tác trên đoạn [2, 4] với V = 1, D = 2: vị trí 2 nhận 1; vị trí 3 nhận 1 + 2 = 3; vị trí 4 nhận 1 + 2*2 = 5. Kết quả in ra: 0 1 3 5 0.

## Ràng buộc
- $100\%$ số test có $N, Q \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
