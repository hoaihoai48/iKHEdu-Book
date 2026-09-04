# Đếm Cặp Đỉnh Không Thể Đi Tới Nhau

## Bối cảnh
Một mạng viễn thông quốc gia gồm $N$ trạm phát sóng và $M$ đường truyền hai chiều. Do ảnh hưởng của bão lớn làm đứt một số đường truyền, mạng lưới bị chia cắt thành nhiều khu vực biệt lập. Hãy đếm xem có tất cả bao nhiêu cặp trạm $(u, v)$ với $u < v$ mà hiện tại không thể gửi tín hiệu liên lạc được cho nhau.

## Nhiệm vụ
Cho đồ thị vô hướng $N$ đỉnh $M$ cạnh. Hãy lập trình đếm số lượng cặp đỉnh $(u, v)$ ($1 \le u < v \le N$) không có đường đi giữa chúng.

## Input
- Dòng 1: Chứa hai số nguyên $N$ và $M$ ($1 \le N \le 10^5, 0 \le M \le 2  × 10^5$).
- $M$ dòng tiếp theo, mỗi dòng chứa hai đỉnh $u$ và $v$.

## Output
- In ra trên một dòng duy nhất số lượng cặp đỉnh không liên thông.

## Sample 1
### Input
```text
5 2
1 2
3 4
```
### Output
```text
8
```

### Giải thích
Với 4 đỉnh và chỉ có 1 cạnh nối (1, 2):
- Cụm 1 gồm {1, 2}.
- Đỉnh 3 cô lập, đỉnh 4 cô lập.
Các cặp không đi tới nhau gồm: (1, 3), (1, 4), (2, 3), (2, 4), (3, 4). Có tổng cộng 5 cặp.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 0 \le M \le 2 \cdot 10^5$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
