# Đường Đi Trên Lưới Có Vật Cản

## Bối cảnh
Vẫn trên lưới ô vuông $N × M$ của kho hàng, robot tự hành cần đi từ ô $(1, 1)$ đến ô $(N, M)$. Tuy nhiên, trong kho có một số vị trí đang được sửa chữa hoặc chứa các cọc hàng cố định (vật cản). Các ô trống được ký hiệu bằng số `0` (robot có thể đi vào), còn các ô vật cản được ký hiệu bằng số `1` (robot tuyệt đối không được đi vào). Robot vẫn chỉ được phép di chuyển sang phải hoặc xuống dưới.

## Nhiệm vụ
Cho bản đồ kho hàng kích thước $N × M$. Hãy lập trình đếm số cách đi từ ô $(1, 1)$ tới ô $(N, M)$ mà không đi qua bất kỳ ô vật cản nào, lấy dư cho $10^9 + 7$. (Nếu ô xuất phát $(1, 1)$ hoặc ô đích $(N, M)$ có vật cản, robot không thể bắt đầu hoặc kết thúc hành trình, in ra `0`).

## Input
- Dòng 1: Chứa hai số nguyên dương $N$ và $M$ ($1 \le N, M \le 1000$).
- $N$ dòng tiếp theo, mỗi dòng chứa $M$ số nguyên `0` hoặc `1` cách nhau bởi khoảng trắng biểu diễn bản đồ kho.

## Output
- In ra trên một dòng duy nhất số đường đi hợp lệ theo modulo $10^9 + 7$.

## Sample 1
### Input
```text
3 3
...
.#.
...
```
### Output
```text
2
```

### Giải thích
Với lưới $3 × 3$ và có vật cản tại ô $(2, 2)$:
Các đường đi ban đầu đi qua ô tâm $(2, 2)$ đều bị phong tỏa. Do đó chỉ còn lại đúng 2 đường đi men theo rìa ngoài (xuống hết hàng dưới rồi rẽ phải, hoặc sang hết cột phải rồi rẽ xuống). Kết quả in ra là 2.

## Ràng buộc
- $100\%$ số test có $1 \le N, M \le 1000$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
