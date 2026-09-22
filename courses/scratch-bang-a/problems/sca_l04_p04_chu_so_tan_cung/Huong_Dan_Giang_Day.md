# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách hàng đơn vị bằng phép dư cho `10`: với `n = 2026` thì `(2026 mod 10) = 6`.
- Quy trình trong lời giải: đọc `n` rồi in `(n mod 10)`; chỉ một phép tính duy nhất.
- Xử lý biên: `n = 1` cho `1`; `n = 10^9 = 1000000000` cho `0`; số tròn chục luôn cho chữ số tận cùng là `0`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 2026)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 2026` |
| 2 | Tính `(n mod 10)` | `(2026 mod 10) = 6` |
| 3 | In kết quả | `6` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Dùng `làm tròn xuống của (n / 10)` (xóa chữ số cuối) thay vì `% 10`.**

```text
nói (làm tròn xuống của (n / 10))

```

Với số liệu mẫu trên, đoạn này cho `2026` in ra `202` thay vì `6`.

Cách sửa: dùng `(n mod 10)`.

**Bẫy 2: In cả số `n` ra.**

```text
nói (n)

```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu in ra `2026` thay vì `6`.

Cách sửa: chỉ in `(n mod 10)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - nói (n mod 10)
