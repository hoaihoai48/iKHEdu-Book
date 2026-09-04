# Dãy Con Tăng Dài Nhất LIS O(N log N)

## Bối cảnh
Quy mô trạm quan trắc địa chấn được nâng cấp tự động hóa trên diện rộng, số lượng mẫu dữ liệu cảm biến thu thập trong một đợt quan sát lên tới $N = 10^5$ phần tử. Với tập dữ liệu khổng lồ này, bài toán tìm dãy con tăng dài nhất đòi hỏi một thuật toán có hiệu năng vượt trội để xử lý tức thời trong vòng 1 giây.

## Nhiệm vụ
Cho dãy $A$ gồm $N$ số nguyên với $N$ lên tới $10^5$. Hãy lập trình xác định độ dài của dãy con tăng nghiêm ngặt dài nhất.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất một số nguyên là độ dài lớn nhất của dãy con tăng nghiêm ngặt.

## Sample 1
### Input
```text
6
5 2 7 4 3 8
```
### Output
```text
3
```

### Giải thích
Với dãy số $[5, 2, 7, 4, 3, 8]$:
Dãy con tăng nghiêm ngặt dài nhất có thể chọn là $[2, 4, 8]$ (hoặc $[2, 3, 8]$, $[5, 7, 8]$). Độ dài dài nhất đạt được là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
