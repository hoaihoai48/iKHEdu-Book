# Đếm Số Chẵn Trong Mảng

## Bối cảnh
Cô giáo yêu cầu mỗi bạn ghi số bút chì mình có lên bảng. Cô muốn biết có bao nhiêu bạn có số bút chì chẵn (chia hết cho $2$) để chia nhóm ghép đôi.

## Nhiệm vụ
Cho dãy gồm $N$ số nguyên dương. Hãy lập trình đếm và in ra số lượng phần tử chẵn (chia hết cho $2$) trong dãy.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên dương $a_1, a_2, \dots, a_N$ ($1 \le a_i \le 10^9$), cách nhau bởi khoảng trắng.

## Output
- In ra một số nguyên duy nhất là số lượng phần tử chẵn.

## Sample 1
### Input
```text
6
1 2 3 4 5 6
```
### Output
```text
3
```

### Giải thích
Dãy có $6$ phần tử: $1, 2, 3, 4, 5, 6$.
- Phần tử chẵn: $2, 4, 6$ (chia hết cho $2$).
- Số lượng: $3$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5$, $1 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
