# Tính tổng các số từ 1 đến N

## Bối cảnh
Trong tuần lễ rèn luyện tính toán nhanh, các bạn học sinh lớp 6 được yêu cầu tính tổng dãy số nguyên liên tiếp $S = 1 + 2 + 3 + \dots + N$. Bạn An muốn viết một chương trình C++ sử dụng vòng lặp để vừa kiểm tra kết quả tính tay, vừa hiểu rõ cách máy tính thực hiện các phép tính tích lũy lặp đi lặp lại.

## Nhiệm vụ
Cho một số nguyên dương $N$. Hãy lập trình sử dụng vòng lặp tính và in ra tổng của tất cả các số nguyên từ $1$ đến $N$.

## Input
- Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^6$).

## Output
- In ra một số nguyên duy nhất là tổng $S = 1 + 2 + \dots + N$.

## Sample 1
### Input
```text
5
```
### Output
```text
15
```

### Giải thích
Tổng các số từ $1$ đến $5$ là:
$1 + 2 + 3 + 4 + 5 = 15$.
Chương trình in ra `15`.

## Sample 2
### Input
```text
100
```
### Output
```text
5050
```

### Giải thích
Tổng các số từ $1$ đến $100$ là $5050$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^6$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
