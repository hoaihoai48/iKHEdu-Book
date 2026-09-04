# Tìm Phần Tử Xuất Hiện 1 Lần Duy Nhất

## Bối cảnh
Trong một trò chơi ghép thẻ bài đôi gồm 2N + 1 lá bài mang các con số nguyên, toàn bộ các lá bài đều có cặp trùng khớp ngoại trừ đúng một lá bài duy nhất không có đối tác ghép cặp. Hãy tìm giá trị của lá bài cô độc đó trong thời gian O(N) và bộ nhớ O(1).

## Nhiệm vụ
Cho mảng gồm 2N + 1 số nguyên, trong đó mọi phần tử đều xuất hiện đúng 2 lần trừ 1 phần tử xuất hiện đúng 1 lần. Hãy tìm phần tử duy nhất đó.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $2N + 1$ số nguyên $A_1, A_2, \dots, A_{2N+1}$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra giá trị phần tử xuất hiện một lần duy nhất.

## Sample 1
### Input
```text
2
4 1 2 1 2
```
### Output
```text
4
```
### Giải thích
Các số 1 và 2 đều xuất hiện 2 lần. Số 4 chỉ xuất hiện 1 lần duy nhất. Phép XOR toàn bộ mảng triệt tiêu các cặp giống nhau và giữ lại đúng số 4. Kết quả in ra: 4.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
