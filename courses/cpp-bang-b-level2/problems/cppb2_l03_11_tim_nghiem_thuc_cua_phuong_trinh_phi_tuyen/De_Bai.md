# Tìm nghiệm thực của phương trình phi tuyến

## Bối cảnh

Trong phòng thí nghiệm vật lý, các bạn học sinh đo một đại lượng biến thiên liên tục theo một biến số và thấy đồ thị của nó luôn đi lên. Thầy giáo đố cả lớp tìm xem giá trị của biến số bằng bao nhiêu thì đại lượng đo được đúng bằng một mốc cho trước.

Cả lớp ghi lại các lần đo rồi thu hẹp dần khoảng tìm kiếm quanh đáp án.

## Nhiệm vụ

Cho số thực $c \ge 0$. Xét phương trình $x^2 + \sqrt{x} = c$ với ẩn $x \ge 0$ (vế trái đơn điệu tăng nên phương trình có đúng một nghiệm). Hãy lập trình tìm nghiệm thực của phương trình với độ chính xác $10^{-6}$.

## Input

- Gồm một dòng duy nhất chứa số thực $c$ ($0 \le c \le 10^{10}$).

## Output

- In ra một dòng duy nhất là nghiệm $x$ của phương trình $x^2 + \sqrt{x} = c$, làm tròn tới $6$ chữ số thập phân.

## Sample 1
### Input
```text
6
```
### Output
```text
2.130792
```
### Giải thích

Đặt $f(x) = x^2 + \sqrt{x}$. Tính $f(2) = 4 + 1{,}414 = 5{,}414 < 6$ và $f(3) = 9 + 1{,}732 = 10{,}732 > 6$ nên nghiệm nằm giữa $2$ và $3$. Thu hẹp khoảng dần (mỗi lần thử điểm giữa: lớn hơn $6$ thì giữ nửa trái, nhỏ hơn $6$ thì giữ nửa phải) cho tới khi khoảng đủ nhỏ, được $x \approx 2{,}130792$. Kiểm tra: $2{,}130792^2 \approx 4{,}5402$, $\sqrt{2{,}130792} \approx 1{,}4597$, tổng $\approx 6{,}0$.

## Ràng buộc

- $0 \le c \le 10^{10}$.
- Thời gian: $1.0\text{s}$, Bộ nhớ: $256\text{MB}$.
