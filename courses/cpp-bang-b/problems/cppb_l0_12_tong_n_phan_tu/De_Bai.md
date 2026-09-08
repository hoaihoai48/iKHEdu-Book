# Tổng N Phần Tử

## Bối cảnh
Trong giờ kiểm tra, thầy giáo đọc lần lượt $N$ số nguyên và yêu cầu học sinh tính nhanh tổng của tất cả các số đó. Bạn muốn viết chương trình giúp tính tổng tự động.

## Nhiệm vụ
Cho số nguyên dương $N$ và dãy gồm $N$ số nguyên $a_1, a_2, \dots, a_N$. Hãy lập trình tính và in ra tổng của tất cả các phần tử trong dãy.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($|a_i| \le 10^9$), cách nhau bởi khoảng trắng.

## Output
- In ra một số nguyên duy nhất là tổng của dãy.

## Sample 1
### Input
```text
5
1 2 3 4 5
```
### Output
```text
15
```

### Giải thích
Tổng: $1 + 2 + 3 + 4 + 5 = 15$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$, $|a_i| \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
