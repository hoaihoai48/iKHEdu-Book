# Chia Tập Thành 2 Phần Có Tổng Bằng Nhau

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Cho mảng số nguyên dương $A$ gồm $N$ phần tử. Hãy kiểm tra xem có thể chia tập $A$ thành 2 tập con rời nhau sao cho tổng các phần tử của 2 tập con bằng nhau hay không. In `YES` nếu được, ngược lại in `NO`.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 20$).
- Dòng 2: $N$ số nguyên dương $A_1, \dots, A_N$ ($1 \le A_i \le 100$).

## Output
- In `YES` hoặc `NO`.

## Sample 1
### Input
```text
4
1 5 11 5
```
### Output
```text
YES
```
### Giải thích
Chia thành 2 tập: {1, 5, 5} (tổng 11) và {11} (tổng 11).

## Ràng buộc
- 100% số test có $1 \le N \le 20, A_i \le 100$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
