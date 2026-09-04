# Tìm Vị Trí Cân Bằng Của Mảng

## Bối cảnh
Trong trò chơi bập bênh chịu lực, N quả cân được xếp thẳng hàng tại các vị trí từ 1 đến N với khối lượng lần lượt là A1, A2, ..., An. Một vị trí đặt điểm tựa i được coi là điểm cân bằng hoàn hảo nếu tổng khối lượng các quả cân bên trái bằng đúng tổng khối lượng các quả cân bên phải điểm tựa đó. Hãy tìm vị trí cân bằng đầu tiên.

## Nhiệm vụ
Cho mảng N số nguyên. Hãy tìm chỉ số i nhỏ nhất (1-indexed) sao cho tổng các phần tử bên trái i bằng tổng các phần tử bên phải i. Nếu không tồn tại, in ra -1.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra chỉ số cân bằng nhỏ nhất (1-indexed), hoặc `-1`.

## Sample 1
### Input
```text
7
-7 1 5 2 -4 3 0
```
### Output
```text
4
```
### Giải thích
Tại vị trí i = 4 (giá trị 2):
- Tổng bên trái (vị trí 1 đến 3): (-7) + 1 + 5 = -1.
- Tổng bên phải (vị trí 5 đến 7): (-4) + 3 + 0 = -1.
Hai tổng bằng nhau (-1 = -1) nên vị trí cân bằng là 4.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
