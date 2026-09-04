# Phủ Sóng Trạm Phát Sóng Wifi Đô Thị

## Bối cảnh
Dọc theo một đại lộ thẳng tắp, có N căn nhà đặt tại các tọa độ X1, X2, ..., Xn. Một nhà mạng viễn thông muốn phủ sóng dịch vụ wifi cộng đồng bằng các bộ phát có bán kính phủ sóng R (nghĩa là một trạm phủ được đoạn [x - R, x + R], tức tầm phủ dài tối đa 2R). Hãy tính số lượng căn nhà tối đa có thể cùng được phủ sóng bởi một trạm phát wifi duy nhất có đường kính phủ sóng 2R.

## Nhiệm vụ
Cho danh sách tọa độ của N căn nhà đã sắp xếp tăng dần và số nguyên R. Hãy tìm số lượng căn nhà nhiều nhất nằm gọn trong một đoạn có độ dài không vượt quá 2R.

## Input
- Dòng 1: 2 số nguyên $N$ và $R$ ($1 \le N \le 10^5, 0 \le R \le 10^9$).
- Dòng 2: $N$ số nguyên đã sắp xếp tăng dần $X_1 < X_2 < \dots < X_N$ ($0 \le X_i \le 10^9$).

## Output
- In ra số lượng căn nhà tối đa được phủ sóng.

## Sample 1
### Input
```text
5 3
1 3 5 8 10
```
### Output
```text
3
```
### Giải thích
Với bán kính R = 3, đường kính phủ sóng tối đa là 2R = 6. Xét đoạn từ nhà tọa độ 1 đến nhà tọa độ 5: độ dài khoảng cách là 5 - 1 = 4 <= 6, phủ sóng được 3 căn nhà tại các tọa độ {1, 3, 5}. Tương tự, đoạn {3, 5, 8} có 8 - 3 = 5 <= 6 cũng phủ được 3 nhà. Số lượng nhà tối đa phủ được là 3.

## Ràng buộc
- $100\%$ số test có $N \le 10^5, R \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}.
