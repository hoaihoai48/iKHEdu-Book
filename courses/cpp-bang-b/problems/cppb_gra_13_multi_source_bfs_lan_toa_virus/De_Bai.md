# Lan Tỏa Virus Trong Mạng Lưới (Multi-Source BFS)

## Bối cảnh
Trong một cuộc tấn công không gian mạng giả định, có $N$ máy tính được kết nối bởi $M$ kênh mạng hai chiều. Ban đầu tại thời điểm $t = 0$, có $K$ máy tính bị nhiễm mã độc virus. Cứ sau mỗi giây, các máy tính đã bị nhiễm sẽ lây truyền virus sang tất cả các máy tính kề sát với nó trong mạng lưới. Hãy tính thời gian (tính bằng giây) để toàn bộ các máy tính trong mạng đều bị lây nhiễm.

## Nhiệm vụ
Cho đồ thị mạng và danh sách $K$ máy tính bị nhiễm ban đầu. Hãy lập trình tính thời gian để toàn bộ máy tính trong thành phần liên thông bị nhiễm.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, K$ ($1 \le K \le N \le 10^5, 0 \le M \le 2 × 10^5$).
- Dòng 2: Chứa $K$ số nguyên là chỉ số các máy tính nhiễm bệnh ban đầu.
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- In ra thời gian tối đa để lây lan hết mạng lưới.

## Sample 1
### Input
```text
4 3 1
1
1 2
2 3
3 4
```
### Output
```text
3
```

### Giải thích
Với 5 máy tính nối thành đường thẳng 1 - 2 - 3 - 4 - 5 và máy 3 bị nhiễm ban đầu:

- Giây 1: máy 3 lây sang máy 2 và 4.
- Giây 2: máy 2 lây sang 1, máy 4 lây sang 5.
Sau đúng 2 giây toàn bộ mạng lưới đều bị lây nhiễm, kết quả là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
