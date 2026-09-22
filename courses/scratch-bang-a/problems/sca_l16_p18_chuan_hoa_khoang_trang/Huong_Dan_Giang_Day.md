# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: dọn thiệp của bạn Na sao cho đầu cuối sạch cách thừa, giữa các từ đúng một dấu cách.
- Quy trình:
  - Đọc câu vào biến `s`. Với số liệu mẫu, `s = "  Python rat la tuyet "` (dư cách đầu cuối và giữa `rat` với `la` có 2 cách).
  - Gọi `s.split()` được `['Python', 'rat', 'la', 'tuyet']`, mọi cách thừa tự mất.
  - Nối lại bằng `" ".join(...)` được `Python rat la tuyet` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Python rat la tuyet (thừa cách hai đầu))
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "  Python rat la tuyet "` | cách thừa nhiều chỗ |
| 2 | `s.split()` | `['Python', 'rat', 'la', 'tuyet']` | sạch cách thừa |
| 3 | `" ".join(...)` rồi in | màn hình hiện `Python rat la tuyet` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ gọt hai đầu bằng `strip()`. Đoạn sai:
```text
s = câu trả lời
nói (s.strip())

```
Với mẫu trên giữa `rat` và `la` vẫn còn 2 dấu cách, đáp án đúng là `Python rat la tuyet` đều một cách. Cách sửa: dùng `" ".join(s.split())`.
- Bẫy 2: nối không có dấu cách `"".join(s.split())`. Đoạn sai:
```text
s = câu trả lời
nói ("".join(s.split()))

```
Với mẫu trên in ra `Pythonratlatuyet` dính liền, đáp án đúng là `Python rat la tuyet`. Cách sửa: nối bằng `" ".join(...)`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - nói (giá trị)
