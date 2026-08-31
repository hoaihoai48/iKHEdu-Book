# Lan Tỏa Virus Trong Mạng Lưới (Multi-Source BFS)

## Bối cảnh
Có $K$ máy tính ban đầu bị nhiễm virus. Mỗi giây, virus lan sang toàn bộ các máy kề nối trực tiếp.

## Nhiệm vụ
Tính thời gian tối thiểu để toàn bộ các máy trong mạng bị lây nhiễm (hoặc -1 nếu có máy cô lập không bị nhiễm).

## Input
- Dòng 1: $N, M, K$ ($1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5, 1 \le K \le N$).
- Dòng 2: $K$ máy tính nhiễm virus ban đầu.
- $M$ dòng tiếp theo: Các đường cáp kết nối mạng.

## Output
- Thời gian tối đa để toàn mạng nhiễm virus.

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

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
