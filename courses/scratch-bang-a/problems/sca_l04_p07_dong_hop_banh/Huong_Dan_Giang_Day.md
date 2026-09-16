# Hướng Dẫn Giảng Dạy: Đóng Hộp Bánh
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là đóng hộp 6 chiếc: với `m = 50` thì số hộp đầy `50 // 6 = 8`, bánh lẻ `50 % 6 = 2`.
- Quy trình trong lời giải: đọc `m` rồi in một dòng `nói (m // 6, m % 6)` cho ra `8 2`.
- Xử lý biên: `m = 1` cho `0 1`; `m = 6` cho `1 0`; `m = 10^6` cho `166666 4`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 50)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `m` nhận giá trị | `m = 50` |
| 2 | Tính số hộp `m // 6` | `50 // 6 = 8` |
| 3 | Tính bánh lẻ `m % 6` | `50 % 6 = 2` |
| 4 | In một dòng hai số | `8 2` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In hai số xuống hai dòng.**

```text
print(m // 6)
print(m % 6)
```

Với số liệu mẫu trên, đoạn này cho `50` in ra `8` rồi `2` xuống hai dòng thay vì `8 2` một dòng.

Cách sửa: in chung một lệnh `nói (m // 6, m % 6)`.

**Bẫy 2: Nhầm số bánh mỗi hộp thành `5`.**

```text
print(m // 5, m % 5)
```

Với số liệu mẫu trên, đoạn này cho `50` in ra `10 0` thay vì `8 2`.

Cách sửa: mỗi hộp đúng `6` chiếc.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập m:] và đợi
> - đặt [m] thành (câu trả lời)
> - nói (kết hợp m // 6 và " " và m % 6)
