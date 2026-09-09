# BFS Tìm Bước Đi Ngắn Nhất Đồ Thị

## Bối cảnh
Một mạng máy tính gồm $N$ máy chủ được đánh số từ $1$ đến $N$ và $M$ kênh kết nối hai chiều không trọng số. Một gói tin xuất phát từ máy chủ nguồn $S$ muốn truyền đến máy chủ đích $D$. Mỗi lần truyền qua một kênh kết nối tốn đúng 1 bước nhảy (hop). Quản trị viên cần xác định số bước nhảy ít nhất để gói tin đến được đích.

## Nhiệm vụ
Cho đồ thị $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình tìm số bước đi ngắn nhất từ $S$ tới $D$. Nếu không thể đến được, in ra `-1`.

## Input
- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5, 1 \le S, D \le N$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $u$ và $v$ biểu diễn một kênh kết nối giữa đỉnh $u$ và $v$.

## Output
- In ra một số nguyên duy nhất là số bước đi ngắn nhất, hoặc `-1` nếu không có đường đi.

## Sample 1
### Input
```text
4 4
1 2
2 3
3 4
1 3
```
### Output
```text
2
```

### Giải thích
Với mạng gồm 4 máy chủ kết nối theo chuỗi $1 - 2 - 3 - 4$ và một kênh tắt nối trực tiếp $1 - 3$:
Để đi từ 1 tới 4, gói tin đi qua kênh tắt $1 × o 3$ tốn 1 bước, sau đó từ $3 × o 4$ tốn 1 bước nữa. Tổng số bước đi ít nhất là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
