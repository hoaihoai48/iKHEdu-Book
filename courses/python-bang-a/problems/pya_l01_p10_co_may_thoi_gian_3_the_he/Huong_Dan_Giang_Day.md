# Hướng Dẫn Giảng Dạy: Cỗ máy thời gian 3 thế hệ
Chuyên đề: **Chào Python & Chiếc Hộp Biến Số**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tính tuổi ba thế hệ dây chuyền: con `a = 10`, bố hơn con `b = 30` nên bố `10 + 30 = 40`, ông hơn bố `c = 25` nên ông `40 + 25 = 65`, tổng cả ba là `10 + 40 + 65 = 115`. Thầy cô vẽ cây gia đình ba tầng để các con dễ thấy.
- Quy trình gồm bốn bước với các biến `a`, `b`, `c`, `tuoi_bo`, `tuoi_ong` trong lời giải: đọc `10` vào `a`, `30` vào `b`, `25` vào `c`, tính `tuoi_bo = a + b = 40`, tính `tuoi_ong = tuoi_bo + c = 65`, rồi in ba dòng `40`, `65`, `115`.
- Xử lý biên: ràng buộc cho `a` từ 1 tới 20, `b` và `c` từ 20 tới 40. Thầy cô cho các con thử biên nhỏ `1, 20, 20` cho ra `21`, `41`, `63`, và biên lớn `20, 40, 40` cho ra `60`, `100`, `180`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 10, 30 và 25)
| Bước | Lệnh chạy | Giá trị biến | Màn hình hiện ra |
|------|-----------|--------------|------------------|
| 1 | `a = int(input())` với dòng 1 gõ `10` | `a = 10` | (chưa in gì) |
| 2 | `b = int(input())` với dòng 2 gõ `30` | `b = 30` | (chưa in gì) |
| 3 | `c = int(input())` với dòng 3 gõ `25` | `c = 25` | (chưa in gì) |
| 4 | `tuoi_bo = a + b` tức `10 + 30` | `tuoi_bo = 40` | (chưa in gì) |
| 5 | `tuoi_ong = tuoi_bo + c` tức `40 + 25` | `tuoi_ong = 65` | (chưa in gì) |
| 6 | `print(tuoi_bo)` | — | `40` |
| 7 | `print(tuoi_ong)` | — | `65` |
| 8 | `print(a + tuoi_bo + tuoi_ong)` tức `10 + 40 + 65` | — | `115` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: tính tuổi ông từ tuổi con, viết `tuoi_ong = a + c` thì với mẫu `10, 30, 25` tuổi ông ra `35` thay vì `65`. Cách sửa: ông hơn bố nên viết `tuoi_ong = tuoi_bo + c`.
- Bẫy 2: tính tổng sai, viết `print(a + b + c)` thì với mẫu màn hình hiện `65` thay vì `115` vì đó chỉ là tổng các khoảng chênh. Cách sửa: tổng ba người là `a + tuoi_bo + tuoi_ong`.
- Bẫy 3: in cả ba tuổi trên một dòng như `print(tuoi_bo, tuoi_ong, ...)` thì màn hình hiện `40 65 115` chung một dòng thay vì ba dòng riêng. Cách sửa: viết ba lệnh `print` riêng.

---

## 4. Lời giải tham khảo
```python
a = int(input())
b = int(input())
c = int(input())
tuoi_bo = a + b
tuoi_ong = tuoi_bo + c
print(tuoi_bo)
print(tuoi_ong)
print(a + tuoi_bo + tuoi_ong)
```
