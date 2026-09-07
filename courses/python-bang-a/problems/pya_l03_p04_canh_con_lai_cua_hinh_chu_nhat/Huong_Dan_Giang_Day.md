# Hướng Dẫn Giảng Dạy: Cạnh còn lại của hình chữ nhật
Chuyên đề: **Toán Học & Hình Học Đời Thường**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất hình chữ nhật: nửa chu vi bằng `P // 2`, cạnh còn lại bằng nửa chu vi trừ cạnh đã biết `a`.
- Quy trình trong lời giải: đọc `p` ở dòng 1 và `a` ở dòng 2, rồi in `p // 2 - a`; với mẫu `P = 30` và `a = 5` thì nửa chu vi `30 // 2 = 15` và cạnh còn lại `15 - 5 = 10`.
- Xử lý biên: đề cho `P` là số chẵn và `a` nhỏ hơn `P // 2` nên kết quả luôn là số tự nhiên dương.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 30\n5)
Với số mẫu dòng 1 là `30` và dòng 2 là `5`, chương trình phải in ra `10`.

| Bước | Hành động | Giá trị biến | Kết quả |
|---|---|---|---|
| 1 | Đọc `p = int(input())` | `p = 30` | chu vi 30 |
| 2 | Đọc `a = int(input())` | `a = 5` | cạnh biết 5 |
| 3 | Tính `p // 2` | `30 // 2 = 15` | nửa chu vi 15 |
| 4 | Tính `15 - 5` | `10` | khớp kết quả mẫu `10` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — đọc hai số một dòng: viết `p, a = map(int, input().split())` thì với mẫu mỗi số một dòng sẽ bị lỗi thiếu số; cách sửa là đọc hai lần `input()` riêng.
- Bẫy 2 — quên chia đôi chu vi: viết `print(p - a)` thì với mẫu ra `25` thay vì `10`; cách sửa là `p // 2 - a`.
- Bẫy 3 — dùng chia thực: viết `print(p / 2 - a)` thì với mẫu in ra `10.0` thay vì `10`; cách sửa là dùng chia nguyên `//`.

---

## 4. Lời giải tham khảo
```python
p = int(input())
a = int(input())
print(p // 2 - a)
```
