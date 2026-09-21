# Đóa hoa 8 cánh sắc màu diệu kỳ

## Bối cảnh

Trong khu vườn mùa xuân của xứ sở Scratch, muôn hoa đua nhau khoe sắc thắm. Để chào đón ngày hội hoa xuân, chú Mèo Scratch muốn lập trình tạo ra một đóa hoa 8 cánh tuyệt đẹp: mỗi chiếc cánh hoa được uốn lượn cong cong mềm mại từ hai cung tròn đối xứng, và mỗi cánh hoa lại mang một màu sắc biến đổi rực rỡ như cầu vồng.

## Nhiệm vụ

Em hãy lập trình điều khiển chú Mèo Scratch hoàn thành bức tranh đóa hoa 8 cánh với các yêu cầu kỹ thuật sau:

1. Đặt nét bút vẽ có độ dày bằng $3$.

2. Tạo thủ tục con vẽ một chiếc cánh hoa đơn lẻ gồm hai cung tròn $90^\circ$ (mỗi bước vi phân dài $1.2$ bước) khép kín đối xứng nhau tại 2 đỉnh.

3. Sử dụng vòng lặp xoay quanh gốc tâm $(0, 0)$ đúng $8$ lần:
   - Vẽ một chiếc cánh hoa.
   - Thay đổi màu bút vẽ một lượng thích hợp (ví dụ $15$ hoặc $20$) để cánh tiếp theo có màu mới.
   - Xoay phải quanh tâm đúng góc: $\text{Góc xoay} = \dfrac{360^\circ}{8} = 45^\circ$.

4. Khi hoàn thành, đóa hoa 8 cánh xòe đều cân xứng quanh tâm, tạo thành một họa tiết hoa văn rực rỡ và hài hòa.

## Kịch bản tương tác (Input Scenario)

- Khởi động khi người dùng nhấn vào biểu tượng **Cờ Xanh**.
- Không yêu cầu nhập dữ liệu từ bàn phím.

## Kết quả mong đợi (Expected Behavior / Output)

- Xuất hiện một đóa hoa gồm đúng $8$ cánh hoa cong mềm mại tỏa đều ra 8 hướng từ tâm $(0, 0)$.
- Các cánh hoa đều nhau chằn chặn, xếp đan khít không bị lệch tâm.
- Màu sắc của các cánh hoa chuyển đổi dần từ đỏ sang cam, vàng, lục, lam, tím.

## Sample 1

### Kịch bản chạy
```text
Sự kiện: Bấm Cờ Xanh
Hành động:
- Xóa màn hình, đưa Mèo về (0, 0), hướng 0 độ (hướng lên)
- Đặt nét bút bằng 3
- Lặp lại 8 lần:
  + Vẽ 1 cánh hoa (2 cung 90 độ)
  + Đổi màu bút vẽ một lượng 15
  + Xoay phải 45 độ
- Ẩn nhân vật
```

### Kết quả trên sân khấu
Một đóa hoa 8 cánh nở rộ cân đối giữa màn hình.

### Giải thích
Mỗi cánh hoa uốn lượn từ tâm $(0, 0)$ rồi lại khép kín quay về đúng tâm $(0, 0)$. Nhờ tính chất bảo toàn vị trí này, lệnh xoay phải $45^\circ$ sẽ đưa nhân vật vào hướng chuẩn bị vẽ cánh tiếp theo mà không làm xê dịch tâm hoa.

## Ràng buộc

- Tọa độ tâm hoa: $x = 0, y = 0$.
- Số cánh hoa: Đúng $8$ cánh.
- Góc xoay tâm: Đúng $45^\circ$ ($360 / 8$).
