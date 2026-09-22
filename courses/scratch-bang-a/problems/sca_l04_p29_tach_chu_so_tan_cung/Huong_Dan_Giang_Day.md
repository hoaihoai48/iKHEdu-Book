# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là tách hai hàng thấp nhất: với `n = 857` thì hàng đơn vị `(857 mod 10) = 7`, hàng chục `làm tròn xuống của (857 / 10) % 10 = (85 mod 10) = 5`.
- Quy trình trong lời giải: đọc `n`, in `(n mod 10)` ở dòng 1 rồi in `làm tròn xuống của (n / 10) % 10` ở dòng 2.
- Xử lý biên: `n = 10` cho `0` rồi `1`; `n = 10^9 = 1000000000` cho `0` rồi `0`; `n = 99` cho `9` rồi `9`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 857)

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc một dòng, biến `n` nhận giá trị | `n = 857` |
| 2 | Tính đơn vị `(n mod 10)` và in dòng 1 | `7` |
| 3 | Tính `làm tròn xuống của (n / 10) = 85` | `85` |
| 4 | Tính `(85 mod 10)` và in dòng 2 | `5` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: In hai số trên một dòng.**

```text
nói ((n mod 10), làm tròn xuống của (n / 10) % 10)

```

Với số liệu mẫu trên, đoạn này cho `857` in ra `7 5` một dòng thay vì hai dòng `7` rồi `5`.

Cách sửa: dùng hai khối lệnh `nói ()` riêng.

**Bẫy 2: Hoán đổi thứ tự hai dòng.**

```text
nói (làm tròn xuống của (n / 10) % 10)
nói ((n mod 10))

```

Với số liệu mẫu trên, đoạn này cho `857` in ra `5` rồi `7`, ngược yêu cầu (đơn vị trước, chục sau).

Cách sửa: in `(n mod 10)` trước.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - nói (n mod 10)
> - nói (n chia nguyên 10 mod 10)
