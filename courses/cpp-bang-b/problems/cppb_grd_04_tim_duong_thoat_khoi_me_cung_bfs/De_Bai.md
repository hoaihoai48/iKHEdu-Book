# Tìm Đường Thoát Khỏi Mê Cung BFS

## Bối cảnh
Một robot tìm kiếm cứu nạn được thả vào một mê cung hình chữ nhật kích thước $N  × M$. Bản đồ mê cung gồm các ô đường đi trống `.` và các ô tường đá không thể vượt qua `#`. Robot xuất phát từ ô ký hiệu `S` và cần di chuyển đến ô cửa thoát hiểm ký hiệu `E`. Mỗi bước di chuyển sang một ô kề cạnh mất đúng 1 giây.

## Nhiệm vụ
Cho bản đồ mê cung. Hãy lập trình tìm thời gian ngắn nhất (số bước ít nhất) để robot đến được cửa thoát hiểm `E`. Nếu không có đường thoát, in ra `-1`.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi gồm $M$ ký tự biểu diễn mê cung.

## Output
- In ra số bước ít nhất để đến đích, hoặc `-1` nếu không có đường đi.

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
9
```

### Giải thích
Với mê cung từ 'S' tại góc $(0, 0)$ đến 'E' tại góc $(2, 2)$ qua các ô đường trống:
Lộ trình ngắn nhất gồm 4 bước di chuyển: $(0,0)  × o (0,1)  × o (1,1)  × o (1,2)  × o (2,2)$. Số bước ít nhất là 4.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
