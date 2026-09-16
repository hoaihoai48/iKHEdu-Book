# Hướng Dẫn Giảng Dạy: Bác thợ mộc cắt gỗ
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là phép chia nguyên và chia dư: thanh dài `l`, mỗi đoạn dài `k`, số đoạn là `l // k`, phần thừa là `l % k`.
- Cách làm của lời giải mẫu: đọc `l` rồi đọc `k`, nếu `l < k` thì in `KHONG DU`, ngược lại in `l // k` và `l % k`. Với mẫu `l = 17`, `k = 5`: `17 // 5 = 3`, `17 % 5 = 2` nên in `3 2`.
- Xử lý biên: ràng buộc `1 <= L, K <= 10^9`. Thầy cô cho thử `l = 4`, `k = 10` (thanh ngắn hơn đoạn cần cắt) thì in `KHONG DU`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17 rồi 5)
Sample 1 với input mẫu: `17` rồi `5`.
| Bước | Việc làm | Giá trị của `l`, `k` | In ra |
|---|---|---|---|
| 1 | Đọc dòng một | `l = 17` | — |
| 2 | Đọc dòng hai | `k = 5` | — |
| 3 | Kiểm tra `17 < 5`? Sai | rẽ nhánh `else` | — |
| 4 | Tính `17 // 5 = 3`, `17 % 5 = 2` rồi in | — | `3 2` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng chia thường: bạn nhỏ viết `nói (l / k, l % k)`. Với mẫu `17` và `5` sẽ in `3.4 2` thay vì `3 2`. Cách sửa: dùng chia nguyên `//`.
- Bẫy 2 — quên nhánh gỗ ngắn: bạn nhỏ luôn in `l // k, l % k`. Với `l = 4`, `k = 10` sẽ in `0 4` thay vì `KHONG DU`. Cách sửa: giữ kiểm tra `if l < k` như lời giải mẫu.
- Bẫy 3 — in sai chữ: bạn nhỏ in `Khong du` viết thường. Với `l = 4`, `k = 10`, chương trình kiểm tra sẽ báo kết quả sai. Cách sửa: in đúng `KHONG DU` viết hoa toàn bộ.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập l:] và đợi
> - đặt [l] thành (câu trả lời)
> - hỏi [Nhập k:] và đợi
> - đặt [k] thành (câu trả lời)
> - nếu <l < k> thì:
> -   nói [YES]
> - nếu không thì:
> -   nói [NO]
