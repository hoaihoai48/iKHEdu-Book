# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tính tiền hóa đơn: đơn giá `a = 12` nghìn đồng nhân với số lượng `b = 5` được `60` nghìn đồng. Thầy cô cho các con hình dung mua 5 chiếc bánh, mỗi chiếc 12 nghìn.
- Quy trình gồm ba bước với hai biến `a` và `b` trong lời giải: đọc `12` vào `a` và `5` vào `b` bằng `câu trả lời`, rồi tính `a * b` tức `12 * 5 = 60` và in ra.
- Xử lý biên: ràng buộc cho `a, b` từ 1 tới 100. Thầy cô cho các con thử cặp biên `1` và `1` cho ra `1`, cặp `100` và `100` cho ra `10000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12 và 5)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = câu trả lời` với dòng 1 gõ `12` | `a = 12` | (chưa in gì) |
| 2 | `b = câu trả lời` với dòng 2 gõ `5` | `b = 5` | (chưa in gì) |
| 3 | `nói (a * b)` tức `nói (12 * 5)` | `a = 12`, `b = 5` | `60` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng: `60`. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: cộng thay vì nhân, viết `nói (a + b)` thì với mẫu `12` và `5` màn hình hiện `17` thay vì `60`. Cách sửa: tiền hóa đơn bằng đơn giá nhân số lượng, viết `a * b`.
- Bẫy 2: quên `int()`, viết `a = câu trả lời` rồi `nói (a * b)` thì máy lặp chữ, cho ra kết quả lạ thay vì `60`. Cách sửa: viết `a = câu trả lời` và `b = câu trả lời`.
- Bẫy 3: đọc hai số trên một dòng bằng `các khối hỏi và đợi cho từng biến` trong khi đề cho hai dòng riêng thì chương trình sẽ chờ thiếu số. Cách sửa: đọc hai lần `câu trả lời` cho đúng hai dòng.

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
> - nói (a * b)
