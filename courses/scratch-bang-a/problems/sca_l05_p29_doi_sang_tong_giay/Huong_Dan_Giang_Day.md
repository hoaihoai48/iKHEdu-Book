# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất đổi về giây: 1 giờ bằng 3600 giây và 1 phút bằng 60 giây, nên tổng là `h * 3600 + m * 60 + s`.
- Quy trình trong lời giải: đọc một dòng rồi tách thành `h, m, s`, sau đó in `h * 3600 + m * 60 + s`; với mẫu `2 15 30` thì `2 * 3600 = 7200`, `15 * 60 = 900`, tổng `7200 + 900 + 30 = 8130`.
- Xử lý biên: `H` tới 1000, `M` và `S` dưới 60, tổng lớn nhất là 3635940.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2 15 30)
Với số mẫu một dòng `2 15 30`, chương trình phải in ra `8130`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `h, m, s` | `h = 2`, `m = 15`, `s = 30` | đủ ba số |
| 2 | Tính `h * 3600` | `2 * 3600 = 7200` | 7200 giây |
| 3 | Tính `7200 + 15 * 60 + 30` | `7200 + 900 + 30 = 8130` | khớp kết quả mẫu `8130` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — nhầm hệ số phút: viết `h * 3600 + m * 100 + s` thì với mẫu ra `8730` thay vì `8130`; cách sửa là phút nhân 60.
- Bẫy 2 — nhầm hệ số giờ: viết `h * 60 + m * 60 + s` thì với mẫu ra `1050` thay vì `8130`; cách sửa là giờ nhân 3600.
- Bẫy 3 — đọc ba dòng riêng: dùng ba lần `câu trả lời` thì với mẫu một dòng sẽ bị treo chờ; cách sửa là tách một dòng bằng `split()`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập h:] và đợi
> - đặt [h] thành (câu trả lời)
> - hỏi [Nhập m:] và đợi
> - đặt [m] thành (câu trả lời)
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - nói (h * 3600 + m * 60 + s)
