# Nén Tọa Độ Mảng Số Lớn

## Bối cảnh
Trong xử lý đồ họa máy tính, các điểm ảnh có tọa độ rất lớn lên tới $10^9$, nhưng tổng số lượng điểm ảnh thực tế xuất hiện trong khung hình chỉ tối đa là $N = 10^5$. Để tiết kiệm bộ nhớ khi đánh chỉ số mảng mà vẫn bảo toàn tuyệt đối thứ tự tương đối về độ lớn giữa các điểm ảnh, kỹ sư đồ họa áp dụng kỹ thuật nén tọa độ: thay thế mỗi giá trị bằng thứ hạng của nó từ $1$ đến $K$ (với $K$ là số giá trị phân biệt).

## Nhiệm vụ
Cho mảng gồm $N$ số nguyên. Hãy lập trình thay thế mỗi phần tử trong mảng bằng thứ hạng nén của nó (bắt đầu từ 1 cho giá trị nhỏ nhất).

## Input
- Dòng 1: Chứa số nguyên dương $N$ ($1 \le N \le 10^5$).
- Dòng 2: Chứa $N$ số nguyên $A_1, A_2, \dots, A_N$ ($-10^9 \le A_i \le 10^9$).

## Output
- In ra trên một dòng gồm $N$ số nguyên là các giá trị sau khi đã nén tọa độ, cách nhau bởi khoảng trắng.

## Sample 1
### Input
```text
5
100 20000 50 20000 100
```
### Output
```text
1 2 0 2 1
```

### Giải thích
Với mảng số ban đầu là $[100, 5, 100, 20, 5]$:
Các giá trị phân biệt sau khi sắp xếp tăng dần là: $5 < 20 < 100$.

- Giá trị 5 nhỏ nhất nhận thứ hạng 1.
- Giá trị 20 nhận thứ hạng 2.
- Giá trị 100 nhận thứ hạng 3.
Mảng sau khi nén tọa độ tương ứng là: $[3, 1, 3, 2, 1]$.

## Ràng buộc
- $100\%$ số test có $1 \le N \le 10^5, 1 \le A_i \le 10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
