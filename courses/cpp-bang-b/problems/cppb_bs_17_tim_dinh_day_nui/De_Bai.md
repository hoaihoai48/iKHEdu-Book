# Tìm Đỉnh Của Dãy Núi (Peak in Mountain Array)

## Bối cảnh
Một thiết bị bay không người lái (drone) bay qua một đỉnh núi cao và ghi nhận liên tục N độ cao địa hình. Dãy độ cao tạo thành dạng dãy núi: ban đầu tăng nghiêm ngặt lên đỉnh cao nhất, sau đó giảm nghiêm ngặt xuống chân núi. Hãy tìm vị trí đỉnh núi (vị trí có độ cao lớn nhất) trong thời gian O(log N).

## Nhiệm vụ
Cho mảng dãy núi A gồm N phần tử (tăng dần rồi giảm dần). Hãy tìm chỉ số (0-indexed) của phần tử đỉnh núi.

## Input
- Dòng 1: Số nguyên dương $N$ ($3 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_0, A_1, \dots, A_{N-1}$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra chỉ số (0-indexed) của đỉnh núi.

## Sample 1
### Input
```text
4
0 2 1 0
```
### Output
```text
1
```
### Giải thích
Đỉnh núi có độ cao lớn nhất là 2, nằm ở chỉ số 1 (0-indexed). Kết quả in ra: 1.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
