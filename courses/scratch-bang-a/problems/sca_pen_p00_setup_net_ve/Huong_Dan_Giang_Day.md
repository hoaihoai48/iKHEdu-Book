# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Củng cố phản xạ khởi tạo giấy bút: `xóa tất cả` $\to$ `nhấc bút` $\to$ `đi tới điểm x: 0 y: 0` $\to$ `đặt hướng bằng (90)` $\to$ `đặt bút`.
- Làm chủ kỹ thuật vẽ "tiến rồi lùi về gốc" (`di chuyển (50) bước` $\to$ `di chuyển (-50) bước`).
- Hiểu góc xoay vuông góc $90^\circ$ giữa 4 hướng không gian.

- **Vấn đề cốt lõi:** Làm thế nào để vẽ 4 nhánh tỏa ra từ một điểm trung tâm mà nét mực không bị chồng chéo méo mó?
- **Cách tiếp cận tối ưu:** Mỗi chu kỳ gồm 3 bước: Đi tới trước $50$ bước $\to$ Lùi lại $-50$ bước $\to$ Xoay phải $90^\circ$. Lặp lại đúng $4$ lần.
- **Edge cases:**
  - Nếu học sinh chỉ đi tới $50$ rồi xoay $90$ và đi tiếp, nhân vật sẽ vẽ thành hình vuông nhỏ chứ không phải dấu cộng.
  - Quên thiết lập tọa độ ban đầu khiến dấu cộng bị lệch khỏi tâm sân khấu.

1. *"Trước khi cầm bút vẽ trên trang giấy trắng, ta cần chuẩn bị gì?"* $\to$ Xóa sạch trang giấy cũ (`xóa tất cả`), chọn màu mực và chỉnh độ đậm nét vẽ (`đặt kích thước bút vẽ bằng (3)`).

2. *"Sau khi chú Mèo vẽ xong 1 nhánh dài 50 bước, chú Mèo đang ở đâu?"* $\to$ Đang ở đầu mút của nhánh cây.

3. *"Làm thế nào để chú Mèo quay về điểm xuất phát để vẽ nhánh thứ 2?"* $\to$ Cho chú Mèo đi lùi $-50$ bước (`di chuyển (-50) bước`).

- **Bất biến sau mỗi nhánh:** Sau mỗi lần lặp, nhân vật luôn trở về đúng tọa độ ban đầu $(0, 0)$ và hướng xoay tăng thêm $90^\circ$.
- **Độ phức tạp:** Thực thi 4 lần lặp, thời gian chạy tức thời $\mathcal{O}(1)$.

- *Độ phức tạp:* Thời gian: $\mathcal{O}(1)$ — hoàn thành trong $0.05$ giây trên sân khấu Scratch. Không gian: Sử dụng $1$ Sprite mặc định, không tốn bộ nhớ RAM.

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
| Vòng lặp | Lệnh thực thi | Vị trí nhân vật | Nét mực tạo ra | Hướng sau lệnh |
|:---:|---|:---:|---|:---:|
| **Khởi tạo** | `đi tới điểm x: 0 y: 0`, `đặt hướng bằng (90)`, `đặt bút` | $(0, 0)$ | Chấm đỏ tại tâm | $90^\circ$ (Phải) |
| **Lần 1** | `di chuyển (50) bước`, `di chuyển (-50) bước`, `xoay phải ↻ (90) độ` | $(0, 0)$ | Đoạn thẳng sang phải $(0, 0) \to (50, 0)$ | $180^\circ$ (Xuống) |
| **Lần 2** | `di chuyển (50) bước`, `di chuyển (-50) bước`, `xoay phải ↻ (90) độ` | $(0, 0)$ | Đoạn thẳng cắm xuống $(0, 0) \to (0, -50)$ | $-90^\circ$ (Trái) |
| **Lần 3** | `di chuyển (50) bước`, `di chuyển (-50) bước`, `xoay phải ↻ (90) độ` | $(0, 0)$ | Đoạn thẳng sang trái $(0, 0) \to (-50, 0)$ | $0^\circ$ (Lên) |
| **Lần 4** | `di chuyển (50) bước`, `di chuyển (-50) bước`, `xoay phải ↻ (90) độ` | $(0, 0)$ | Đoạn thẳng hướng lên $(0, 0) \to (0, 50)$ | $90^\circ$ (Phải) |

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1:** Nhập `di chuyển (50) bước` rồi lại `di chuyển (50) bước` $\to$ Nhân vật đi tiếp $100$ bước. Phải giải thích cho học sinh: Số âm mang ý nghĩa đi lùi (`di chuyển (-50) bước`).
- **Bẫy 2:** Quên khối `đặt bút` $\to$ Chú Mèo nhảy múa nhưng không để lại nét mực nào trên màn hình.

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0
![Khối lệnh Scratch 3.0 giải bài sca_pen_p00_setup_net_ve](solution_blocks_vi.png)

- **Mở rộng 1:** Thay vì vẽ dấu cộng 4 cánh, em hãy đổi góc xoay thành $60^\circ$ và lặp lại $6$ lần để tạo thành bông hoa tuyết 6 cánh.
- **Mở rộng 2:** Đổi góc xoay thành $45^\circ$ và lặp lại $8$ lần để tạo thành ngôi sao 8 cánh.
