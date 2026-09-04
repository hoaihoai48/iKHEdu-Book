# Mã Đi Tuần (Knight's Tour)

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Trong một trò chơi cờ vua cổ điển tại hoàng gia, vị vua đưa ra câu đố thử thách tài năng hiệp sĩ: Đặt một quân Mã tại ô xuất phát $(R, C)$ trên bàn cờ hình vuông $N \times N$. Hiệp sĩ phải điều khiển quân Mã di chuyển theo đúng quy tắc hình chữ L sao cho ghé thăm tất cả $N^2$ ô cờ trên bàn, mỗi ô đúng một lần duy nhất và ghi lại số thứ tự bước đi tại từng ô.

## Nhiệm vụ
Cho kích thước bàn cờ $N$ và tọa độ xuất phát $(R, C)$ (hệ tọa độ 1-based). Hãy sử dụng thuật toán Quay lui kết hợp luật heuristic Warnsdorff (luôn ưu tiên nhảy sang ô có ít nước đi tiếp theo nhất) để tìm một hành trình mã đi tuần hoàn chỉnh. In ra ma trận $N \times N$ ghi số thứ tự các bước đi từ $1$ đến $N^2$, hoặc in `-1` nếu không tìm được hành trình.

## Input
- Một dòng duy nhất chứa 3 số nguyên $N, R, C$ ($1 \le N \le 6, 1 \le R, C \le N$).

## Output
- In ra ma trận $N \times N$ ghi số thứ tự các bước đi từ $1$ đến $N^2$ (các số trên cùng hàng cách nhau bởi dấu cách), hoặc in `-1` nếu không tồn tại hành trình hợp lệ.

## Sample 1
### Input
```text
5 1 1
```
### Output
```text
1 16 11 6 25
10 5 24 15 20
17 2 19 22 7
4 9 14 21 12
3 18 23 8 13
```
### Giải thích
Quân mã xuất phát từ ô $(1, 1)$ bước 1, lần lượt nhảy qua các ô theo luật mã và ghé thăm đủ 25 ô trên bàn cờ $5 \times 5$ mà không ô nào bị trùng lặp.

## Ràng buộc
- 100% số test có $1 \le N \le 6, 1 \le R, C \le N$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
