# Đếm Số Lần Xuất Hiện Xâu Con Rời Rạc (Distinct Subsequences)

## Bối cảnh
Trong bộ lọc từ khóa độc hại của mạng xã hội, hệ thống cần kiểm tra tần suất mà một từ khóa nhạy cảm $T$ xuất hiện dưới dạng chuỗi con rời rạc bên trong một bài viết $S$. Hai cách xuất hiện được tính là khác nhau nếu tập hợp các vị trí chỉ số ký tự được chọn trong bài viết $S$ là khác nhau.

## Nhiệm vụ
Cho hai chuỗi ký tự $S$ và $T$. Hãy lập trình đếm số cách khác nhau để chọn ra chuỗi con trong $S$ bằng đúng chuỗi $T$, lấy dư cho $10^9 + 7$.

## Input
- Dòng 1: Chứa chuỗi văn bản $S$ ($1 \le |S| \le 2000$).
- Dòng 2: Chứa chuỗi mẫu $T$ ($1 \le |T| \le 500$).

## Output
- In ra số cách xuất hiện hợp lệ theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
rabbbit
rabbit
```
### Output
```text
3
```

### Giải thích
Với $S = \text{"rabbbit"}$ và $T = \text{"rabbit"}$:
Trong chuỗi $S$ có 3 ký tự 'b' liên tiếp. Để tạo thành từ "rabbit", ta có thể loại bỏ 1 trong 3 ký tự 'b' đó. Do đó có đúng 3 cách chọn khác nhau để thu được từ "rabbit". Kết quả in ra là 3.

## Ràng buộc
- $100\%$ số test có $1 \le |S| \le 2000, 1 \le |T| \le 500$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
