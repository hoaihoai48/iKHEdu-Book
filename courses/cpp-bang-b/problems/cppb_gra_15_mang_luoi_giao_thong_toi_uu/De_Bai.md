# Xây Dựng Thêm Đường Nối Toàn Mạng (Building Roads)

## Bối cảnh
Một vương quốc gồm $N$ thành phố nhưng hiện tại hệ thống đường sá chỉ có $M$ con đường, khiến nhiều thành phố bị cô lập không thể đi tới nhau. Nhà vua muốn xây dựng thêm một số lượng con đường mới ít nhất nối giữa các thành phố sao cho sau khi hoàn thành, cư dân từ bất kỳ thành phố nào cũng có thể di chuyển tới mọi thành phố khác trong vương quốc.

## Nhiệm vụ
Cho bản đồ vương quốc hiện tại. Hãy lập trình tìm số lượng đường mới ít nhất cần xây dựng và chỉ rõ danh sách các con đường cần làm thêm.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2 × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh biểu diễn một con đường hiện có.

## Output
- Dòng 1: In ra số nguyên $K$ là số lượng con đường ít nhất cần xây thêm.
- $K$ dòng tiếp theo, mỗi dòng in ra hai thành phố cần nối đường mới.

## Sample 1
### Input
```text
4 2
1 2
3 4
```
### Output
```text
1
1 3
```

### Giải thích
Với 4 thành phố và chỉ có 1 đường nối giữa (1, 2) và 1 đường nối giữa (3, 4):
Vương quốc đang bị chia thành 2 cụm độc lập {1, 2} và {3, 4}. Ta chỉ cần xây thêm đúng 1 con đường nối giữa thành phố 2 và thành phố 3 là toàn bộ 4 thành phố sẽ liên thông hoàn chỉnh.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
