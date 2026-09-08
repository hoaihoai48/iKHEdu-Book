# Đảo Ngược Mảng

## Bối cảnh
Thầy giáo xếp $N$ bạn học sinh đứng thành một hàng ngang. Bây giờ thầy muốn đảo ngược thứ tự: bạn đứng cuối hàng chuyển lên đầu, bạn đứng đầu chuyển xuống cuối.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên. Hãy lập trình in ra dãy sau khi đảo ngược thứ tự.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($|a_i| \le 10^9$), cách nhau bởi khoảng trắng.

## Output
- In ra $N$ số nguyên trên một dòng, cách nhau bởi khoảng trắng, là dãy sau khi đảo ngược.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
5 4 3 2 1
```

### Giải thích
Dãy ban đầu: $1, 2, 3, 4, 5$.
Đảo ngược: phần tử cuối ($5$) lên đầu, phần tử đầu ($1$) xuống cuối.
Kết quả: $5, 4, 3, 2, 1$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$, $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
