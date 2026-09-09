# Bước Nhảy Quân Mã Ngắn Nhất (Knight Moves)

## Bối cảnh
Trên bàn cờ vua tiêu chuẩn kích thước $N × N$, quân Mã di chuyển theo quy tắc hình chữ L đặc thù: tại mỗi bước, quân Mã di chuyển 2 ô theo một trục và 1 ô theo trục vuông góc (tối đa 8 hướng nhảy). Cho vị trí ban đầu của quân Mã tại ô $(x_1, y_1)$ và ô mục tiêu $(x_2, y_2)$. Hãy tính số bước nhảy ít nhất để quân Mã di chuyển đến được ô mục tiêu.

## Nhiệm vụ
Cho kích thước bàn cờ $N$ và hai tọa độ điểm xuất phát, điểm đích. Hãy lập trình tìm số bước nhảy ít nhất của quân Mã.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 1000$).
- Dòng 2: Chứa 4 số nguyên $x_1, y_1, x_2, y_2$ ($1 \le x_1, y_1, x_2, y_2 \le N$).

## Output
- In ra số bước nhảy ít nhất cần dùng.

## Sample 1
### Input
```text
8 8 0 0 7 7
```
### Output
```text
6
```

### Giải thích
Để đi từ ô $(1, 1)$ tới ô $(4, 5)$ trên bàn cờ vua:
Quân mã thực hiện lần lượt các bước nhảy: $(1, 1) × o (2, 3) × o (4, 4) × o (2, 5) × o (4, 5)$ hoặc lộ trình tối ưu tương tự với đúng 3 bước nhảy. Kết quả là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
