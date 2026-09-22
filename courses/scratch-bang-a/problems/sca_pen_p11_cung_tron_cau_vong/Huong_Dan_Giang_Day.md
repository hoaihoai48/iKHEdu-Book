# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Nắm vững kỹ thuật lập trình đồ họa tương tác với phần mở rộng Bút vẽ (Pen).
- Hiểu và áp dụng thành thạo: Vẽ cung tròn đổi màu 7 sắc cầu vồng.
- Rèn luyện tư duy tính toán góc quay hình học và bất biến vẽ hình khép kín.

- **Bản chất hình học:** Sử dụng vòng lặp kết hợp di chuyển  và đổi hướng .
- Với các hình cung tròn: Mỗi bước đi một đoạn nhỏ và xoay ^\circ$.
- Cần nhấc bút  khi di chuyển vị trí xuất phát để không làm lem nét vẽ thừa.

1. *Muốn vẽ hình mà không để lại vệt mực thừa trên đường đi ta làm thế nào?* -> Nhấc bút trước khi đi tới tọa độ mới.

2. *Làm sao để nét vẽ nổi bật và rõ ràng?* -> Đặt kích thước nét vẽ từ 2 đến 3.

- Luôn có khối chuẩn bị môi trường: Xóa tất cả, đặt hướng 90 độ, đặt tọa độ xuất phát.
- Bất biến: Sau khi vẽ xong một cánh hoa/hình con, nhân vật quay về vị trí tâm và xoay một góc để sẵn sàng vẽ hình tiếp theo.

- *Độ phức tạp:* Thời gian: Vẽ tức thì trong vòng dưới 1 giây. Bộ nhớ: Không tốn biến nhớ phụ.

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
| Bước | Khối lệnh Scratch Tiếng Việt | Ý nghĩa hành động |
|:---:|---|---|
| 1 |  | Khởi động kịch bản |
| 2 |  | Làm sạch sân khấu |
| 3 |  | Đặt độ đậm nét vẽ |
| 4 |  | Bắt đầu vẽ nét |

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1:** Quên đặt bút khiến nhân vật di chuyển nhưng sân khấu trắng tinh.
- **Bẫy 2:** Không xóa sân khấu cũ khiến hình vẽ mới bị đè lên hình cũ.

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0
![Khối lệnh Cung tròn cầu vồng](solution_blocks_vi.png)

- Khối Bút vẽ: , , , .
- Khối Điều khiển: .
