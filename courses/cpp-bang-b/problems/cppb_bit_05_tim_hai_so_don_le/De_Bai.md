# Tìm Hai Số Xuất Hiện 1 Lần Duy Nhất

## Bối cảnh
Trong một sự kiện bắt cặp khiêu vũ gồm 2N + 2 người tham gia mang các số định danh nguyên, sau khi các cặp đôi ghép thành công thì còn lại đúng 2 người chưa tìm được bạn nhảy. Hãy tìm ra số định danh của 2 người đó theo thứ tự tăng dần.

## Nhiệm vụ
Cho mảng gồm 2N + 2 số nguyên, trong đó mọi phần tử xuất hiện 2 lần trừ đúng 2 phần tử X và Y xuất hiện 1 lần duy nhất. Hãy tìm và in ra X, Y theo thứ tự tăng dần.

## Input
- Dòng 1: Số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $2N + 2$ số nguyên $A_1, A_2, \dots, A_{2N+2}$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra 2 số nguyên $X, Y$ ($X < Y$) cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
2
1 2 3 2 1 4
```
### Output
```text
3 4
```
### Giải thích
Các số 1 và 2 đều xuất hiện 2 lần. Hai số chỉ xuất hiện 1 lần duy nhất là 3 và 4. Kết quả in theo thứ tự tăng dần: 3 4.

## Ràng buộc
- $100\%$ số test có $N \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
