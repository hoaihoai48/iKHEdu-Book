# Lập Lịch Công Việc Số Máy Chủ Ít Nhất

## Bối cảnh
Một trung tâm điện toán đám mây tiếp nhận $N$ tác vụ xử lý dữ liệu. Tác vụ thứ $i$ bắt đầu tại thời điểm $S_i$ và kết thúc tại thời điểm $E_i$. Một máy chủ chỉ có thể thực hiện một tác vụ tại một thời điểm. Nếu hai tác vụ có khoảng thời gian chạy bị chồng chéo nhau, chúng bắt buộc phải được giao cho hai máy chủ vật lý khác nhau.

## Nhiệm vụ
Cho danh sách thời gian bắt đầu và kết thúc của $N$ tác vụ. Hãy lập trình xác định số lượng máy chủ vật lý tối thiểu cần chuẩn bị để phục vụ toàn bộ các tác vụ.

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- $N$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $S_i$ và $E_i$ ($0 \le S_i < E_i \le 10^9$).

## Output
- In ra trên một dòng duy nhất số lượng máy chủ tối thiểu cần dùng.

## Sample 1
### Input
```text
3
0 30
5 10
15 20
```
### Output
```text
2
```

### Giải thích
Với 3 tác vụ: [0, 30], [5, 10], [15, 20]:
Tại thời điểm $t = 5$, tác vụ 1 [0, 30] đang chạy trên máy 1, nên tác vụ 2 [5, 10] bắt buộc phải mở thêm máy 2.
Tại thời điểm $t = 15$, tác vụ 2 đã xong nhưng tác vụ 1 vẫn đang chạy, nên tác vụ 3 có thể tái sử dụng máy 2.
Số máy chủ tối thiểu cần dùng là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 50000, 1 \le S_i < E_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
