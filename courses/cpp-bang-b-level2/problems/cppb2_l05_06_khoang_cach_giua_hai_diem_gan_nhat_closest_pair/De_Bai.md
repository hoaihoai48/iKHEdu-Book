# Khoảng cách giữa hai điểm gần nhất (closest pair)

## Bối cảnh
Trên bản đồ cứu hộ có đánh dấu vị trí của $N$ trạm quan sát. Ban chỉ huy muốn nối hai trạm gần nhau nhất bằng một đường dây liên lạc dự phòng.

Hãy giúp họ tìm ra hai trạm có khoảng cách gần nhau nhất trong tất cả các trạm.

## Nhiệm vụ
Cho $N$ điểm trên mặt phẳng tọa độ. Hãy lập trình tìm khoảng cách Euclid nhỏ nhất giữa hai điểm phân biệt trong số đó.

## Input

- Dòng đầu tiên chứa số nguyên $n$ ($2 \le n \le 10^5$) — số điểm.
- $n$ dòng tiếp theo, mỗi dòng chứa hai số nguyên $x_i, y_i$ ($|x_i|, |y_i| \le 10^9$) là tọa độ một điểm (các điểm phân biệt).

## Output

- In ra một dòng duy nhất là khoảng cách Euclid nhỏ nhất giữa hai điểm phân biệt, làm tròn tới $6$ chữ số thập phân.

## Sample 1
### Input
```text
4
0 0
3 0
1 1
2 2
```
### Output
```text
1.414214
```
### Giải thích

Tính tay các cặp gần nhau: $(1, 1)$ với $(2, 2)$ cách $\sqrt{1 + 1} = \sqrt{2} \approx 1{,}414214$; $(0, 0)$ với $(1, 1)$ cũng $\sqrt{2}$; các cặp còn lại đều xa hơn ($(0, 0)$ với $(3, 0)$ cách $3$, $(3, 0)$ với $(2, 2)$ cách $\sqrt{5} \approx 2{,}236$). Vậy khoảng cách nhỏ nhất là $1{,}414214$.

## Ràng buộc

- $2 \le n \le 10^5$, tọa độ nguyên có trị tuyệt đối không quá $10^9$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
