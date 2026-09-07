# Quét đường thẳng nén tọa độ (sweep-line area 2d)

## Bối cảnh

Phường vẽ bản đồ các khu đất hình chữ nhật để tính tiền sử dụng đất. Cán bộ địa chính cần tính tổng diện tích bị phủ bởi ít nhất một khu đất, vì phần chồng lấn chỉ tính một lần.

Anh cán bộ kẻ các đường thẳng đứng qua mọi cạnh khu đất rồi tính diện tích từng dải một.

## Nhiệm vụ

Cho danh sách các hình chữ nhật trên mặt phẳng. Hãy lập trình tính tổng diện tích hợp bị phủ bởi ít nhất một hình chữ nhật.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($1 \le n \le 2000$) — số hình chữ nhật.
- $n$ dòng tiếp theo, mỗi dòng chứa bốn số nguyên $x_1, y_1, x_2, y_2$ ($|x_i|, |y_i| \le 10^9$, $x_1 < x_2$, $y_1 < y_2$) là góc dưới-trái và góc trên-phải của một hình.

## Output

- In ra một dòng duy nhất là tổng diện tích của phần mặt phẳng bị phủ bởi ít nhất một hình chữ nhật.

## Sample 1
### Input
```text
2
0 0 2 2
1 1 3 3
```
### Output
```text
7
```
### Giải thích

Quét từ trái sang phải theo các mốc $x = 0, 1, 2, 3$. Dải $[0, 1]$: chỉ hình thứ nhất phủ, độ cao phủ là $2$ → diện tích $1 \cdot 2 = 2$. Dải $[1, 2]$: cả hai hình cùng phủ, hợp theo trục $y$ là $[0, 3]$ cao $3$ → diện tích $3$. Dải $[2, 3]$: chỉ hình thứ hai phủ, cao $2$ → diện tích $2$. Tổng $2 + 3 + 2 = 7$.

## Ràng buộc

- $1 \le n \le 2000$, tọa độ có trị tuyệt đối không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
