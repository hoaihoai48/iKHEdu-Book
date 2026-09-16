# Hướng Dẫn Giảng Dạy: Xe Buýt Chở Học Sinh
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là làm tròn lên: với `n = 25`, `k = 10` thì `(25 + 10 - 1) // 10 = 34 // 10 = 3` xe; hai xe chở `20` bạn, xe thứ `3` chở `5` bạn còn lại.
- Quy trình trong lời giải: đọc `n` dòng 1, đọc `k` dòng 2, rồi in `(n + k - 1) // k`.
- Xử lý biên: `n = 10, k = 10` cho `1`; `n = 11, k = 10` cho `2`; `n = 10^6, k = 1` cho `1000000`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 25 và 10 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `n` nhận giá trị | `n = 25` |
| 2 | Đọc dòng 2, biến `k` nhận giá trị | `k = 10` |
| 3 | Tính `n + k - 1 = 34` | `34` |
| 4 | Chia nguyên `34 // 10` | `3` |
| 5 | In kết quả | `3` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `n // k` (bỏ bạn dư).**

```text
print(n // k)
```

Với số liệu mẫu trên, đoạn này cho `25` và `10` cho `2` thay vì `3`, còn `5` bạn không có xe.

Cách sửa: dùng `(n + k - 1) // k`.

**Bẫy 2: Đọc hai số một dòng bằng `split()`.**

```text
n, k = map(int, hỏi và đợi.split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số một dòng nên nhận thiếu `k`.

Cách sửa: đọc hai lần `hỏi và đợi` riêng.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - hỏi [Nhập k:] và đợi
> - đặt [k] thành (câu trả lời)
> - nói ((n + k - 1)
