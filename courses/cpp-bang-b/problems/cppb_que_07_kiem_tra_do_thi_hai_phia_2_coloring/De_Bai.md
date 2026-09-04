# Kiểm Tra Đồ Thị Hai Phía (Bipartite Graph)

## Bối cảnh
Trong một hội thảo giao lưu quốc tế, có $N$ đại biểu và $M$ mối quan hệ quen biết lẫn nhau. Ban tổ chức muốn chia toàn bộ $N$ đại biểu vào đúng 2 phòng thảo luận khác nhau sao cho không có hai người nào quen nhau lại ngồi chung trong cùng một phòng (tương đương bài toán tô màu đồ thị bằng 2 màu sao cho hai đỉnh kề nhau luôn có màu khác nhau).

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình kiểm tra xem đồ thị có phải là đồ thị hai phía hay không. Nếu có in ra `YES`, ngược lại in ra `NO`.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.

## Output
- In ra `YES` nếu đồ thị là hai phía, ngược lại in ra `NO`.

## Sample 1
### Input
```text
4 4
1 2
2 3
3 4
4 1
```
### Output
```text
YES
```

### Giải thích
Với đồ thị là hình vuông gồm 4 đỉnh có các cạnh: 1-2, 2-3, 3-4, 4-1:
Ta có thể chia thành hai tập đỉnh độc lập: tập 1 gồm {1, 3} và tập 2 gồm {2, 4}. Không có hai đỉnh nào cùng tập có cạnh nối. Đồ thị là hai phía, kết quả in ra YES.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
