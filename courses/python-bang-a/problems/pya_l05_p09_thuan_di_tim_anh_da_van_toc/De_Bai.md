# Thuận Đi Tìm Ánh Đa Vận Tốc


*(Lấy cảm hứng từ Bài 5 Đề thi THT Huyện Từ Sơn)*

## Bối cảnh

Thuận đứng ở vị trí $x$, Ánh đứng ở vị trí $y$. Thuận đi về phía Ánh với vận tốc $v\text{ km/h}$.
## Nhiệm vụ

Hãy phân tích các tình huống:
  * Nếu $x == y$: in `DA GAP NHAU` (vì đang đứng cùng một chỗ).
  * Nếu $x \ne y$ nhưng $v == 0$: in `KHONG THE GAP` (vì Thuận đứng yên).
  * Nếu $x \ne y$ và $v > 0$:
    * Nếu khoảng cách $|y - x|$ chia hết cho $v$: in ra số giờ để gặp nhau.
    * Nếu không chia hết: in `GAP NHAU LE GIO`.
## Input

Ba số nguyên $x, y, v$ ($-10^9 \le x, y \le 10^9, 0 \le v \le 10^9$).
## Output

Thông báo tương ứng hoặc số giờ nguyên.


## Ràng buộc


* **Giới hạn thời gian:** $1.0\text{s}$
* **Giới hạn bộ nhớ:** $256\text{MB}$
