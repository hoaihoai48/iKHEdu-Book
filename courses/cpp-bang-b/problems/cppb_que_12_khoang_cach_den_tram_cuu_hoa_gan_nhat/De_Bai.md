# Khoảng Cách Đến Trạm Cứu Hỏa Gần Nhất (Multi-Source BFS)

## Bối cảnh
Một bản đồ đô thị gồm $N$ khu dân cư và $M$ tuyến đường hai chiều. Trong thành phố có $K$ trạm cứu hỏa được đặt tại một số khu dân cư nhất định. Để đảm bảo an toàn phòng cháy chữa cháy, ban điều hành cứu hộ cần xác định khoảng cách ngắn nhất (số cạnh) từ mỗi khu dân cư tới trạm cứu hỏa gần nhất.

## Nhiệm vụ
Cho bản đồ thành phố và danh sách vị trí các trạm cứu hỏa. Hãy lập trình tính khoảng cách ngắn nhất từ từng khu dân cư đến trạm cứu hỏa gần nhất.

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, K$ ($1 \le K \le N \le 10^5, 0 \le M \le 2  × 10^5$).
- Dòng 2: Chứa $K$ số nguyên là vị trí đặt các trạm cứu hỏa.
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh biểu diễn một tuyến đường.

## Output
- In ra trên một dòng gồm $N$ số nguyên là khoảng cách từ mỗi đỉnh đến trạm cứu hỏa gần nhất, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
4 3 2
1 4
1 2
2 3
3 4
```
### Output
```text
0 1 1 0
```

### Giải thích
Với 4 khu dân cư nối liên tiếp 1 - 2 - 3 - 4 và trạm cứu hỏa đặt tại khu 2:

- Khu 1: cách trạm cứu hỏa 1 bước.
- Khu 2: có sẵn trạm cứu hỏa $\to$ khoảng cách 0.
- Khu 3: cách trạm cứu hỏa 1 bước.
- Khu 4: cách trạm cứu hỏa 2 bước.
Kết quả in ra: 1 0 1 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
