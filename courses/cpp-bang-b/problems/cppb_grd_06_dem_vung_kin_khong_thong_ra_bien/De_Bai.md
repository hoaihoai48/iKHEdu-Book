# Đếm Số Ô Vùng Kín Không Thông Ra Biên

## Bối cảnh
Một vùng trũng ngập nước được số hóa thành lưới $N  × M$. Các ô đất liền có giá trị `1`, ô ngập nước có giá trị `0`. Một vùng đất được gọi là "vùng kín" nếu nó là một cụm các ô `1` liên thông kề cạnh mà hoàn toàn không có bất kỳ ô nào chạm vào 4 mép biên ngoài của bản đồ (nghĩa là vùng đất bị bao bọc hoàn toàn bởi các ô nước).

## Nhiệm vụ
Cho ma trận nhị phân $N  × M$. Hãy lập trình đếm tổng số lượng ô đất liền `1` thuộc về các vùng đất kín không thông ra biên.

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1` cách nhau bởi khoảng trắng.

## Output
- In ra trên một dòng duy nhất số lượng ô đất liền thuộc các vùng kín.

## Sample 1
### Input
```text
4 4
1111
1001
1101
1111
```
### Output
```text
3
```

### Giải thích
Với ma trận có một cụm gồm 3 ô đất nằm lọt thỏm ở trung tâm và toàn bộ viền xung quanh đều là ô số 0:
Cụm này hoàn toàn không chạm biên, số ô đất kín đếm được là 3.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
