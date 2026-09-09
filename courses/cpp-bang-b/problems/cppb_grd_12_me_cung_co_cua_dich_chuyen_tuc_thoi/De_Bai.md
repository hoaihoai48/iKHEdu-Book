# Cổng Dịch Chuyển Tức Thời (Teleport Maze)

## Bối cảnh
Trong một trò chơi thực tế ảo trong mê cung lưới $N × M$, ngoài các ô đường đi thông thường, mê cung còn bố trí một số cặp cổng dịch chuyển tức thời không gian. Khi bước vào một cổng dịch chuyển, người chơi sẽ ngay lập tức được dịch chuyển sang cổng tương ứng ở vị trí khác mà không tốn thời gian (0 giây). Hãy tìm thời gian ngắn nhất để đi từ điểm xuất phát `S` tới đích `E`.

## Nhiệm vụ
Cho bản đồ mê cung và danh sách các cặp cổng dịch chuyển. Hãy lập trình tìm số bước ít nhất để đến đích.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N, M \le 1000$).
- Các dòng tiếp theo mô tả bản đồ mê cung và các cặp cổng dịch chuyển.

## Output
- In ra số bước ít nhất từ S tới E, hoặc `-1` nếu không có đường đi.

## Sample 1
### Input
```text
3 3
..A
.##
A..
```
### Output
```text
2
```

### Giải thích
Nhờ sử dụng cổng dịch chuyển tức thời, người chơi rút ngắn được quãng đường vòng qua tường đá, thời gian đến đích giảm xuống còn 3 bước.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
