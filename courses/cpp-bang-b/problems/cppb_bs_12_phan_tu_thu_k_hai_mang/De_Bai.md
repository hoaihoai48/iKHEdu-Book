# Phần Tử Thứ K Của Hai Mảng Đã Sắp Xếp

## Bối cảnh
Hai sàn thương mại điện tử lớn nhất khu vực có danh sách giá các mặt hàng công nghệ đã được sắp xếp tăng dần: sàn A gồm N món đồ và sàn B gồm M món đồ. Người tiêu dùng muốn biết nếu gộp toàn bộ danh sách hàng hóa của hai sàn lại với nhau thành một mảng có thứ tự thì mặt hàng rẻ thứ K trên thị trường chung có giá trị là bao nhiêu.

## Nhiệm vụ
Cho hai mảng số nguyên đã sắp xếp A (kích thước N) và B (kích thước M) cùng số nguyên dương K (1 <= K <= N + M). Hãy tìm giá trị của phần tử đứng ở vị trí thứ K sau khi hợp nhất hai mảng trong thời gian O(log(min(N, M))).

## Input
- Dòng 1: Chứa 3 số nguyên $N, M, K$ ($1 \le N, M \le 10^5, 1 \le K \le N + M$).
- Dòng 2: Chứa $N$ số nguyên tăng dần của mảng $A$.
- Dòng 3: Chứa $M$ số nguyên tăng dần của mảng $B$.

## Output
- In ra giá trị phần tử thứ $K$.

## Sample 1
### Input
```text
5 4 5
2 3 6 7 9
1 4 8 10
```
### Output
```text
6
```
### Giải thích
Hợp nhất hai mảng có thứ tự: [1, 2, 3, 4, 6, 7, 8, 9, 10]. Phần tử đứng thứ K = 5 là số 6. Kết quả in ra: 6.

## Ràng buộc
- $100\%$ số test có $N, M \le 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
