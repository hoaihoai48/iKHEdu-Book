# Đếm Số Lượng Bit 1 (Popcount)

## Bối cảnh
Một giao thức mã hóa dữ liệu mạng kiểm tra tính toàn vẹn của gói tin bằng cách đếm trọng số Hamming — tức số lượng bit 1 xuất hiện trong mã khóa nhị phân 64-bit của số nguyên N. Hãy đếm chính xác số lượng bit 1 trong biểu diễn nhị phân của N.

## Nhiệm vụ
Cho số nguyên không âm N (0 <= N <= 10^18). Hãy đếm và in ra số lượng bit có giá trị bằng 1 trong biểu diễn nhị phân của N.

## Input
- Một dòng duy nhất chứa số nguyên không âm $N$ ($0 \le N \le 10^{18}$).

## Output
- In ra một số nguyên duy nhất là số lượng bit 1 của $N$.

## Sample 1
### Input
```text
13
```
### Output
```text
3
```
### Giải thích
13 biểu diễn nhị phân là 1101_2, có tổng cộng 3 bit 1 (tại các vị trí bit 0, 2, 3). Kết quả in ra: 3.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
