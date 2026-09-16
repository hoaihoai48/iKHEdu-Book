# HƯỚNG DẪN GIẢNG DẠY: HÌNH TRÒN ĐỒNG TÂM
**Mã bài toán:**  | **Phân tầng:** P1/P2 (Bút Vẽ Pen)  
**Chuyên đề:** Đồ Họa Bút Vẽ Scratch 3.0

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
- Nắm vững kỹ thuật lập trình đồ họa tương tác với phần mở rộng Bút vẽ (Pen).
- Hiểu và áp dụng thành thạo: Vẽ nhiều đường tròn lồng nhau cùng tâm.
- Rèn luyện tư duy tính toán góc quay hình học và bất biến vẽ hình khép kín.

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
- **Bản chất hình học:** Sử dụng vòng lặp kết hợp di chuyển  và đổi hướng .
- Với các hình cung tròn: Mỗi bước đi một đoạn nhỏ và xoay ^\circ$.
- Cần nhấc bút  khi di chuyển vị trí xuất phát để không làm lem nét vẽ thừa.

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. *Muốn vẽ hình mà không để lại vệt mực thừa trên đường đi ta làm thế nào?* -> Nhấc bút trước khi đi tới tọa độ mới.
2. *Làm sao để nét vẽ nổi bật và rõ ràng?* -> Đặt kích thước nét vẽ từ 2 đến 3.

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
- Luôn có khối chuẩn bị môi trường: Xóa tất cả, đặt hướng 90 độ, đặt tọa độ xuất phát.
- Bất biến: Sau khi vẽ xong một cánh hoa/hình con, nhân vật quay về vị trí tâm và xoay một góc để sẵn sàng vẽ hình tiếp theo.

## 5. Bảng Mô Phỏng Từng Bước (Dry Run Table)
| Bước | Khối lệnh Scratch Tiếng Việt | Ý nghĩa hành động |
|:---:|---|---|
| 1 |  | Khởi động kịch bản |
| 2 |  | Làm sạch sân khấu |
| 3 |  | Đặt độ đậm nét vẽ |
| 4 |  | Bắt đầu vẽ nét |

## 6. Phân Tích Độ Phức Tạp
- Thời gian: Vẽ tức thì trong vòng dưới 1 giây.
- Bộ nhớ: Không tốn biến nhớ phụ.

## 7. Các Bẫy Lỗi Thường Gặp (Bug Traps)
- **Bẫy 1:** Quên đặt bút khiến nhân vật di chuyển nhưng sân khấu trắng tinh.
- **Bẫy 2:** Không xóa sân khấu cũ khiến hình vẽ mới bị đè lên hình cũ.

## 8. Khối Lệnh Tham Chiếu (Scratch Tiếng Việt)
- Khối Bút vẽ: , , , .
- Khối Điều khiển: .


## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - xóa tất cả, đặt kích thước bút vẽ bằng (3)
> - đặt [R] thành (30)
> - lặp lại (3) lần:
> -   nhấc bút, đi tới điểm x: (0) y: (R), đặt hướng (90), đặt bút
> -   lặp lại (360) lần: di chuyển ((2 * 3.14 * R) / 360) bước, xoay phải ↻ (1) độ
> -   thay đổi [R] một lượng (30)
