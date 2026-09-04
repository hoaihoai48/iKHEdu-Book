# Mê Cung (Rat in a Maze): Tìm Mọi Đường Đi

**Phân loại bài toán:** `Core Foundation`

## Bối cảnh
Một robot thám hiểm thông minh được thả vào một mê cung hình vuông kích thước $N \times N$. Trong mê cung, các ô có giá trị `1` là đường đi thông thoáng an toàn, còn các ô có giá trị `0` là những khối đá cản trở không thể đi qua. Robot bắt đầu hành trình từ ô xuất phát ở góc trên cùng bên trái $(0, 0)$ và cần tìm đường đến điểm cứu hộ ở góc dưới cùng bên phải $(N-1, N-1)$. Để lập kế hoạch cứu nạn dự phòng, robot cần vẽ lại tất cả các tuyến đường khả thi.

## Nhiệm vụ
Cho bản đồ mê cung $N \times N$. Giả sử mỗi bước robot chỉ di chuyển sang các ô kề cạnh chưa từng ghé qua theo các hướng: Xuống dưới (`D`), Sang trái (`L`), Sang phải (`R`), Lên trên (`U`). Hãy áp dụng thuật toán Quay lui để tìm và in ra tất cả các chuỗi di chuyển hợp lệ theo thứ tự từ điển (`D < L < R < U`). Nếu ô xuất phát bị chặn hoặc không có đường đi nào, in ra `-1`.

## Input
- Dòng 1: Số nguyên dương $N$ ($2 \le N \le 8$).
- $N$ dòng tiếp theo: Mỗi dòng gồm $N$ số nguyên `0` hoặc `1` cách nhau bởi dấu cách.

## Output
- In ra các xâu ký tự đại diện cho các đường đi tìm được (mỗi đường trên một dòng theo thứ tự từ điển), hoặc in `-1` nếu không tồn tại đường đi.

## Sample 1
### Input
```text
4
1 0 0 0
1 1 0 1
0 1 0 0
1 1 1 1
```
### Output
```text
DDRDRR
DRDDRR
```
### Giải thích
Robot xuất phát tại $(0,0)$ và đích đến là $(3,3)$. Có 2 tuyến đường hợp lệ không qua ô 0:
- Tuyến 1: Đi xuống $\to$ xuống $\to$ phải $\to$ xuống $\to$ phải $\to$ phải (`DDRDRR`).
- Tuyến 2: Đi xuống $\to$ phải $\to$ xuống $\to$ xuống $\to$ phải $\to$ phải (`DRDDRR`).

## Ràng buộc
- 100% số test có $2 \le N \le 8$.
- Thời gian: 1.0s, Bộ nhớ: 256MB.
