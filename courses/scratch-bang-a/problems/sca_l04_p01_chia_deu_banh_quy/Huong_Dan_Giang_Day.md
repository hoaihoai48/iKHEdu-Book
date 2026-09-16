# Hướng Dẫn Giảng Dạy: Chia Đều Bánh Quy
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất là phép chia nguyên một lần: với `a = 17` chiếc bánh và `b = 5` chiếc đĩa, số bánh mỗi đĩa là `a // b = 17 // 5 = 3`, số dư là `a % b = 17 % 5 = 2`.
- Quy trình trong lời giải: đọc `a` từ dòng 1, đọc `b` từ dòng 2, rồi in một dòng duy nhất `nói (a // b, a % b)` cho ra `3 2`.
- Xử lý biên: khi `a = 1, b = 1000` thì mỗi đĩa được `0` và dư `1`; khi `a = 1000, b = 1` thì mỗi đĩa `1000` dư `0`; khi `a` chia hết cho `b` (ví dụ `10` và `5`) phần dư bằng `0`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 17 và 5 (hai dòng))

| Bước | Diễn giải | Giá trị |
|------|-----------|---------|
| 1 | Đọc dòng 1, biến `a` nhận giá trị | `a = 17` |
| 2 | Đọc dòng 2, biến `b` nhận giá trị | `b = 5` |
| 3 | Tính `a // b` | `17 // 5 = 3` |
| 4 | Tính `a % b` | `17 % 5 = 2` |
| 5 | In kết quả một dòng | `3 2` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp

**Bẫy 1: Chỉ in thương, quên in số dư.**

```text
print(a // b)
```

Với số liệu mẫu trên, đoạn này cho `17` và `5` chỉ in ra `3`, thiếu số `2` nên thiếu một nửa đáp số.

Cách sửa: in cả hai giá trị `nói (a // b, a % b)`.

**Bẫy 2: Dùng phép chia thực `/` thay vì `//`.**

```text
print(a / b, a % b)
```

Với số liệu mẫu trên, đoạn này cho `17` và `5` in ra `3.4 2` thay vì `3 2`.

Cách sửa: dùng `//` để lấy phần nguyên.

**Bẫy 3: Đọc cả hai số trên một dòng bằng `split()`.**

```text
a, b = map(int, hỏi và đợi.split())
```

Với số liệu mẫu trên, đoạn này cho số liệu mẫu mỗi số nằm một dòng nên dòng 2 bị bỏ sót, chương trình nhận thiếu `b`.

Cách sửa: đọc hai lần `hỏi và đợi`, mỗi lần một số.

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
> - nói (kết hợp a // b và " " và a % b)
