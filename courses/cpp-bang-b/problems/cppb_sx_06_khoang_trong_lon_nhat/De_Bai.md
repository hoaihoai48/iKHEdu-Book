# Khoảng Trống Lớn Nhất Trên Trục Tọa Độ

## Bối cảnh
Trong một trò chơi thám hiểm vũ trụ ảo, một con tàu không gian phải di chuyển dọc theo một hành lang hẹp trên trục tọa độ 1 chiều. Trên hành lang này xuất hiện $N$ chướng ngại vật thiên thạch tại các tọa độ $A_1, A_2, \dots, A_N$. Để con tàu có thể kích hoạt động cơ siêu tốc một cách an toàn, nó cần tìm ra khoảng không gian trống lớn nhất giữa hai chướng ngại vật liên tiếp nhau dọc theo hành trình.

## Nhiệm vụ
Cho danh sách tọa độ của $N$ chướng ngại vật. Hãy tìm và in ra khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp sau khi sắp xếp vị trí của chúng theo thứ tự tăng dần trên trục tọa độ.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 10^5$) — số lượng chướng ngại vật.
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^{18} \le A_i \le 10^{18}$) — tọa độ các chướng ngại vật.

## Output
- In ra một số nguyên duy nhất là khoảng cách lớn nhất giữa hai chướng ngại vật liên tiếp.

## Sample 1
### Input
```text
5
10 3 25 8 12
```
### Output
```text
13
```
### Giải thích
Tọa độ các chướng ngại vật ban đầu là: $10, 3, 25, 8, 12$.
Sau khi sắp xếp tăng dần theo chiều dọc hành lang:
$3, 8, 10, 12, 25$.
Khoảng cách giữa các chướng ngại vật liên tiếp lần lượt là:

- $8 - 3 = 5$
- $10 - 8 = 2$
- $12 - 10 = 2$
- $25 - 12 = 13$

Khoảng trống lớn nhất giữa hai chướng ngại vật liên tiếp là $13$ (giữa vị trí $12$ và $25$).

## Ràng buộc
- $40\%$ số test có $N \le 1000, \vert A_i \vert \le 10^9$.
- $60\%$ số test có $N \le 10^5, \vert A_i \vert \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
