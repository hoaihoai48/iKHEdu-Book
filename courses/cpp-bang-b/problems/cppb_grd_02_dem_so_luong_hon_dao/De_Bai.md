# Đếm Số Lượng Hòn Đảo (Count Islands)

## Bối cảnh
Một bức ảnh viễn thám chụp một vùng biển được số hóa thành ma trận nhị phân kích thước $N  × M$. Ký tự `'0'` đại diện cho mặt nước biển, còn ký tự `'1'` đại diện cho đất liền. Một hòn đảo được định nghĩa là một tập hợp các ô đất liền `'1'` kết nối với nhau theo 4 hướng (lên, xuống, trái, phải) và được bao quanh hoàn toàn bởi nước biển.

## Nhiệm vụ
Cho bản đồ ma trận $N  × M$. Hãy lập trình đếm số lượng hòn đảo xuất hiện trên bản đồ.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa một chuỗi gồm $M$ ký tự `'0'` hoặc `'1'` biểu diễn bản đồ.

## Output
- In ra trên một dòng duy nhất số lượng hòn đảo đếm được.

## Sample 1
### Input
```text
4 5
11000
11000
00100
00011
```
### Output
```text
3
```

### Giải thích
Với bản đồ kích thước $3  × 3$ chứa các cụm đất liền biệt lập không có ô kề cạnh chung:
Các ô đất liền kết nối thành đúng 3 cụm độc lập, kết quả đếm được là 3 hòn đảo.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
