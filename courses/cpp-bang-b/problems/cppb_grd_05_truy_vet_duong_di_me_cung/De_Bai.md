# Truy Vết Đường Đi Mê Cung (L, R, U, D)

## Bối cảnh
Sau khi xác định được thời gian thoát hiểm ngắn nhất trong mê cung, bộ điều khiển cần xuất ra chuỗi lệnh điều hướng chi tiết bằng các ký tự viết tắt phương hướng: `'U'` (lên trên), `'D'` (xuống dưới), `'L'` (sang trái), `'R'` (sang phải) để nạp trực tiếp vào bộ nhớ vi điều khiển của robot.

## Nhiệm vụ
Cho bản đồ mê cung $N  × M$ với điểm xuất phát `S` và đích `E`. Hãy lập trình tìm đường đi ngắn nhất và in ra chuỗi các bước di chuyển tương ứng.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi $M$ ký tự.

## Output
- Dòng 1: In ra số bước đi ngắn nhất $K$ (hoặc in `NO` nếu không có đường đi).
- Dòng 2: In ra chuỗi $K$ ký tự gồm `U, D, L, R` mô tả lộ trình di chuyển.

## Sample 1
### Input
```text
5 8
########
#.A#...#
#.##.#B#
#......#
########
```
### Output
```text
YES
9
LDDRRRRRU
```

### Giải thích
Với lộ trình đi từ $(0, 0)$ sang phải rồi xuống dưới:
Chuỗi lệnh điều hướng tương ứng là: "RRD" hoặc "DRR" có độ dài 3 bước.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
