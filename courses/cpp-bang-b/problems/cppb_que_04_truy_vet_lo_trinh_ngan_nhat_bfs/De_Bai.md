# Truy Vết Lộ Trình Ngắn Nhất Bằng BFS

## Bối cảnh
Sau khi tính toán được số bước nhảy tối thiểu để truyền gói tin giữa hai máy chủ, trung tâm điều hành cần in ra chính xác danh sách thứ tự các máy chủ mà gói tin đã đi qua để cấu hình bảng định tuyến mạng.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh và hai đỉnh $S, D$. Hãy lập trình tìm và in ra một đường đi ngắn nhất từ $S$ tới $D$. Nếu không có đường đi, in ra `-1`.

## Input
- Dòng 1: Chứa 4 số nguyên $N, M, S, D$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u, v$.

## Output
- Dòng 1: In ra số lượng đỉnh trên đường đi $K$.
- Dòng 2: In ra $K$ số nguyên là thứ tự các đỉnh trên hành trình từ $S$ tới $D$.

## Sample 1
### Input
```text
5 5
1 2
2 3
3 5
1 4
4 5
```
### Output
```text
3
1 4 5
```

### Giải thích
Với đồ thị có đường đi ngắn nhất từ 1 tới 4 là $1  × o 3  × o 4$:
Dòng 1 in ra 3 (số đỉnh trên đường đi).
Dòng 2 in ra 1 3 4.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
