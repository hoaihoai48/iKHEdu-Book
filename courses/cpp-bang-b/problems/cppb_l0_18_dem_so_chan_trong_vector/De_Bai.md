# Đếm số lượng số chẵn trong vector

## Bối cảnh
Thầy giáo thể dục ghi lại số lần nhảy dây của $N$ học sinh trong lớp thành một danh sách số nguyên. Thầy muốn thống kê xem có bao nhiêu bạn đạt số lần nhảy dây là một số chẵn. Bạn hãy lập trình giúp thầy giải quyết bài toán này.

## Nhiệm vụ
Cho một dãy gồm $N$ số nguyên. Hãy lập trình sử dụng `vector` để lưu trữ và đếm xem trong dãy có bao nhiêu số chẵn.

## Input
- Dòng thứ nhất chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng thứ hai chứa $N$ số nguyên $a_1, a_2, \dots, a_N$ ($-10^9 \le a_i \le 10^9$), cách nhau bởi một khoảng trắng.

## Output
- In ra một số nguyên duy nhất là số lượng phần tử chẵn trong dãy.

## Sample 1
### Input
```text
6
4 7 2 9 8 5
```
### Output
```text
3
```

### Giải thích
Trong dãy có 3 số chẵn là: $4, 2, 8$. Kết quả in ra: `3`.

## Sample 2
### Input
```text
4
1 3 5 7
```
### Output
```text
0
```

### Giải thích
Không có số chẵn nào trong dãy, in ra `0`.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, -10^9 \le a_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
