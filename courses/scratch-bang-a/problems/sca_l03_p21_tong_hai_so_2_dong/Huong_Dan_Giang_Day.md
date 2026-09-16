# Hướng Dẫn Giảng Dạy: Tổng hai số nguyên 2 dòng
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là cộng số bi của Minh và Nam: `A = 15` cộng `B = 25` được `40`. Thầy cô cho các con đếm gộp 15 viên rồi thêm 25 viên nữa.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `15` vào `a`, đọc `25` vào `b`, rồi tính `a + b` tức `15 + 25 = 40` và in ra.
- Xử lý biên: ràng buộc cho `A, B` từ 0 tới `10^9`. Thầy cô cho các con thử cặp biên `0` và `0` cho ra `0`, cặp `1000000000` và `1000000000` cho ra `2000000000` để thấy chương trình vẫn đúng.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15 và 25)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(hỏi và đợi)` với dòng 1 gõ `15` | `a = 15` | (chưa in gì) |
| 2 | `b = int(hỏi và đợi)` với dòng 2 gõ `25` | `b = 25` | (chưa in gì) |
| 3 | `nói (a + b)` tức `nói (15 + 25)` | `a = 15`, `b = 25` | `40` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `40`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: quên `int()`, viết `a = hỏi và đợi` và `b = hỏi và đợi` rồi `nói (a + b)` thì với mẫu `15` và `25` máy nối chữ thành `1525` thay vì `40`. Cách sửa: viết `a = int(hỏi và đợi)` và `b = int(hỏi và đợi)`.
- Bẫy 2: trừ thay vì cộng, viết `nói (a - b)` thì với mẫu `15` và `25` màn hình hiện `-10` thay vì `40`. Cách sửa: nhớ bài hỏi tổng nên viết dấu `+`.
- Bẫy 3: đọc hai số trên một dòng bằng `map(int, hỏi và đợi.split())` trong khi đề cho hai dòng riêng thì với mẫu nhập từng số một dòng chương trình sẽ chờ thiếu số. Cách sửa: đọc hai lần `int(hỏi và đợi)` cho đúng hai dòng.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập a:] và đợi
> - đặt [a] thành (câu trả lời)
> - hỏi [Nhập b:] và đợi
> - đặt [b] thành (câu trả lời)
> - nói (a + b)
