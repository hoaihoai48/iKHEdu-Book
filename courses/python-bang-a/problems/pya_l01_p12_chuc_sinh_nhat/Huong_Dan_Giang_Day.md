# Hướng Dẫn Giảng Dạy: Lời chúc sinh nhật cá nhân hóa
Chuyên đề: **Tính Toán Cơ Bản & Nền Tảng Python**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là điền tên và tuổi vào khung thiệp mẫu: `Chuc mung sinh nhat <Ten>, ban tron <Tuoi> tuoi!`. Với mẫu thì tên là `Nam` và tuổi là `10`.
- Quy trình gồm ba bước với hai biến `ten` và `tuoi` trong lời giải: đọc chuỗi `"Nam"` vào `ten` bằng `input()` (giữ nguyên chữ, không đổi sang số), đọc `10` vào `tuoi` bằng `int(input())`, rồi dùng chuỗi `f"..."` để ghép cả hai vào đúng vị trí trong câu chúc.
- Xử lý biên: ràng buộc cho tuổi từ 1 tới 100. Thầy cô cho các con thử tuổi biên `1` cho ra `... ban tron 1 tuoi!` và tuổi biên `100` cho ra `... ban tron 100 tuoi!`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: Nam và 10)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `ten = input()` với dòng 1 gõ `Nam` | `ten = "Nam"` | (chưa in gì) |
| 2 | `tuoi = int(input())` với dòng 2 gõ `10` | `tuoi = 10` | (chưa in gì) |
| 3 | `print(f"Chuc mung sinh nhat {ten}, ban tron {tuoi} tuoi!")` | `ten = "Nam"`, `tuoi = 10` | `Chuc mung sinh nhat Nam, ban tron 10 tuoi!` |
| 4 | Kết thúc chương trình | — | Kết quả cuối cùng đúng như dòng trên. |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: đổi tuổi sang số sai cách, viết `tuoi = input()` không có `int()` thì khi ghép vẫn hiện đúng `10`, nhưng nếu sau này tính toán sẽ bị nối chữ. Cách sửa: viết `tuoi = int(input())`.
- Bẫy 2: quên dấu phẩy hoặc dấu chấm than trong mẫu, ví dụ in `Chuc mung sinh nhat Nam ban tron 10 tuoi` thì thiếu dấu `,` sau tên và thiếu `!` cuối câu nên bị tính là kết quả sai. Cách sửa: sao chép đúng mẫu `..., ban tron ... tuoi!`.
- Bẫy 3: dùng dấu cộng để ghép mà quên đổi số thành chữ, ví dụ `"... tron " + tuoi + " tuoi!"` thì chương trình báo lỗi vì không cộng chữ với số được. Cách sửa: dùng chuỗi `f"..."` như trong lời giải.

---

## 4. Lời giải tham khảo
```python
ten = input()
tuoi = int(input())
print(f"Chuc mung sinh nhat {ten}, ban tron {tuoi} tuoi!")
```
