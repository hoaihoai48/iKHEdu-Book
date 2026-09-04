# Tìm Phần Tử Lớn Thứ Hai (Tournament Tree)

## Bối cảnh
Trong một giải đấu loại trực tiếp (Tournament), các đấu thủ thi đấu đối đầu từng cặp theo cây nhị phân. Đấu thủ về nhì chỉ có thể là người đã từng bị đấu thủ vô địch đánh bại trong hành trình tiến tới trận chung kết. Mô hình chia để trị giúp tìm phần tử lớn thứ hai với số phép so sánh tối thiểu N + log2(N) - 2.

## Nhiệm vụ
Cho mảng N số nguyên phân biệt (N là lũy thừa của 2). Hãy tìm phần tử lớn thứ hai trong mảng bằng mô hình cây thi đấu chia để trị.

## Input
- Dòng 1: Số nguyên dương $N$ ($N = 2^k, 2 \le N \le 10^5$).
- Dòng 2: $N$ số nguyên phân biệt $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra giá trị của phần tử lớn thứ hai.

## Sample 1
### Input
```text
4
3 8 2 5
```
### Output
```text
5
```
### Giải thích
Phần tử lớn nhất là 8, phần tử lớn thứ hai là 5. Kết quả in ra: 5.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
