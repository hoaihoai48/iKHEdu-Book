# Hứng Nước Mưa (Trapping Rain Water)

## Bối cảnh
Một mô hình địa hình gồm $N$ khối bê tông thẳng đứng có chiều rộng 1 đơn vị được xếp thẳng hàng kề sát nhau, khối thứ $i$ có độ cao $H_i$. Sau một cơn mưa rào lớn, nước mưa sẽ đọng lại ở các thung lũng giữa các khối bê tông cao hơn hai bên. Hãy tính toán tổng lượng nước mưa tối đa có thể đọng lại sau cơn mưa.

## Nhiệm vụ
Cho danh sách chiều cao của $N$ khối bê tông. Hãy lập trình tính tổng đơn vị thể tích nước mưa có thể đọng lại.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên không âm $H_1, H_2, \dots, H_N$ ($0 \le H_i \le 10^5$).

## Output
- In ra trên một dòng duy nhất một số nguyên là tổng thể tích nước mưa đọng lại.

## Sample 1
### Input
```text
12
0 1 0 2 1 0 1 3 2 1 2 1
```
### Output
```text
6
```

### Giải thích
Với độ cao địa hình là $[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]$:
Nước mưa sẽ bị giữ lại ở các vùng trũng giữa các cột cao:

- Tại vị trí 2: nước đọng 1 đơn vị.
- Tại vị trí 4: nước đọng 1 đơn vị.
- Tại vị trí 5: nước đọng 2 đơn vị.
- Tại vị trí 6: nước đọng 1 đơn vị.
- Tại vị trí 9: nước đọng 1 đơn vị.
Tổng lượng nước đọng lại là $1 + 1 + 2 + 1 + 1 = 6$ đơn vị.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le H_i \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
