# Diện tích hợp các hình chữ nhật

## Bối cảnh
Trên mặt phẳng tọa độ $Oxy$, cho $N$ hình chữ nhật có các cạnh song song với các trục tọa độ. Mỗi hình chữ nhật thứ $i$ được xác định bởi tọa độ góc dưới trái $(x_1, y_1)$ và góc trên phải $(x_2, y_2)$.

## Nhiệm vụ
Hãy tính tổng diện tích của phần mặt phẳng bị phủ bởi ít nhất một trong $N$ hình chữ nhật bằng thuật toán Quét đường (Sweep-line) kết hợp Nén tọa độ.

## Input
- Dòng 1: Gồm 1 số nguyên $N$ ($1 \le N \le 2000$) — số lượng hình chữ nhật.
- $N$ dòng tiếp theo: Mỗi dòng gồm 4 số nguyên $x_1, y_1, x_2, y_2$ ($0 \le x_1 < x_2 \le 10^9, 0 \le y_1 < y_2 \le 10^9$).

## Output
- In ra một số nguyên duy nhất là tổng diện tích hợp của các hình chữ nhật.

## Sample 1
### Input
```text
2
10 10 20 20
15 15 25 25
```
### Output
```text
175
```
### Giải thích
* Hình chữ nhật 1 có diện tích $10 \times 10 = 100$.
* Hình chữ nhật 2 có diện tích $10 \times 10 = 100$.
* Phần giao nhau là hình chữ nhật $[15, 20] \times [15, 20]$ có diện tích $5 \times 5 = 25$.
* Tổng diện tích hợp phủ = $100 + 100 - 25 = 175$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 2000, 0 \le x_1 < x_2 \le 10^9, 0 \le y_1 < y_2 \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
