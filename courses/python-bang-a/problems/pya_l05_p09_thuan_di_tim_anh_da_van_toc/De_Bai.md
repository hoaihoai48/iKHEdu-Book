# Thuận Đi Tìm Ánh Đa Vận Tốc


*(Lấy cảm hứng từ Bài 5 Đề thi THT Huyện Từ Sơn)*

## Bối cảnh

Một buổi chiều đẹp trời, bạn Thuận đứng ở vị trí $x$ còn bạn Ánh đứng ở vị trí $y$ trong sân trường rộng. Thuận rất nhớ bạn nên đi bộ về phía Ánh với vận tốc $v\text{ km/h}$. Cả hai hồi hộp không biết bao giờ thì gặp được nhau. Em hãy giúp hai bạn xem khi nào thì gặp nhau nhé!
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
