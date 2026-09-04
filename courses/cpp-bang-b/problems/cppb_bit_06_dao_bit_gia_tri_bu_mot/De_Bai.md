# Đảo Bit Và Giá Trị Bù 1

## Bối cảnh
Trong thiết kế mạch logic số ALU, phép bù 1 (đảo toàn bộ các bit 0 thành 1 và 1 thành 0) trên biểu diễn nhị phân hiệu dụng của số nguyên dương N được sử dụng để tính giá trị đối trong biểu diễn số bù. Hãy tìm giá trị thập phân của số thu được sau khi đảo toàn bộ bit của N.

## Nhiệm vụ
Cho số nguyên dương N. Hãy đảo toàn bộ các bit từ bit có trọng số lớn nhất đến bit 0 của N và in ra giá trị thập phân của số mới.

## Input
- Một dòng chứa số nguyên dương $N$ ($1 \le N \le 10^{18}$).

## Output
- In ra số nguyên sau khi đã đảo bit.

## Sample 1
### Input
```text
5
```
### Output
```text
2
```
### Giải thích
5 = 101_2. Đảo toàn bộ 3 bit hiệu dụng: bit 1 thành 0, bit 0 thành 1 -> ta được 010_2 = 2. Kết quả in ra: 2.

## Ràng buộc
- $100\%$ số test có $N \le 10^{18}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
