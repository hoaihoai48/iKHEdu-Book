# Giám Sát Camera Giao Thông Thông Minh

## Bối cảnh
Trên tuyến đường cao tốc có $N$ vị trí gắn camera. Trạng thái camera thứ $i$ được ghi nhận bởi $A_i$ ($A_i = 1$ là hoạt động tốt, $A_i = 0$ là bị hỏng). Trung tâm muốn chọn một đoạn liên tiếp gồm $K$ camera để kiểm tra định kỳ. Hãy tìm số lượng camera bị hỏng ít nhất trong bất kỳ đoạn $K$ camera liên tiếp nào.

## Input
- Dòng 1: Chứa 2 số nguyên $N$ và $K$ ($1 \le K \le N \le 10^5$).
- Dòng 2: $N$ số nguyên $A_1, A_2, \dots, A_N$ ($A_i \in \{0, 1\}$).

## Output
- In ra số camera hỏng ít nhất trong mọi cửa sổ độ dài $K$.

## Sample 1
### Input
```text
7 3
1 0 1 1 0 0 1
```
### Output
```text
0
```
### Giải thích
Đoạn từ vị trí 3 đến 5 là $[1, 1, 1]$ (sau khi xét các cửa sổ độ dài 3, đoạn $[1, 1, 0]$ có 1 hỏng, đoạn $[1, 1, 1]$... trong ví dụ là $[1, 0, 1, 1, 0, 0, 1]$ thì đoạn con $[1, 1, 0]$ có 1 hỏng, đoạn $[1, 0, 1]$ có 1 hỏng...).

## Ràng buộc
- $100\%$ số test có $N \le 10^5, K \le N$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
