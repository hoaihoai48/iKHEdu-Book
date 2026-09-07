# Hướng Dẫn Giảng Dạy: Bốn mùa trong năm
Chuyên đề: **Lựa Chọn Nhiều Hướng (if - elif - else)**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là tra tháng `t` vào bốn nhóm: `1, 2, 3` là `XUAN`; `4, 5, 6` là `HA`; `7, 8, 9` là `THU`; `10, 11, 12` là `DONG`.
- Cách làm của lời giải mẫu: đọc `t`, kiểm tra `if t in [1, 2, 3]` rồi tới các `elif` theo nhóm. Với mẫu `t = 4`: nhóm xuân sai, nhóm `4, 5, 6` đúng nên in `HA`.
- Xử lý biên: ràng buộc `-100 <= M <= 100`. Thầy cô lưu ý lời giải mẫu không có nhánh cho tháng ngoài `1..12`, nên với `M = 0` hay `M = 13` chương trình không in gì; khi dạy cần đối chiếu với chương trình kiểm tra của lớp mình.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)
Sample 1 với input mẫu: `4`.
| Bước | Việc làm | Giá trị của `t` | In ra |
|---|---|---|---|
| 1 | Đọc input | `t = 4` | — |
| 2 | Kiểm tra `4` trong `[1, 2, 3]`? Sai | xuống nhánh `elif` | — |
| 3 | Kiểm tra `4` trong `[4, 5, 6]`? Đúng | rẽ nhánh hai | — |
| 4 | In kết quả | — | `HA` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — viết điều kiện dài dòng sai: bạn nhỏ viết `if t == 4 or 5 or 6`. Với `t = 1` cụm này vẫn đúng nên in `HA`, sai. Cách sửa: dùng `t in [4, 5, 6]` như lời giải mẫu.
- Bẫy 2 — xếp tháng `6` vào mùa thu: bạn nhỏ viết nhóm thu là `[6, 7, 8]`. Với `t = 6` sẽ in `THU` thay vì `HA`. Cách sửa: giữ đúng bốn nhóm của lời giải mẫu.
- Bẫy 3 — in `HE` thay vì `HA`: đề kể mùa Hạ (Hè) nên có bạn in `HE`. Với mẫu `4`, chương trình kiểm tra chờ `HA` nên sẽ báo kết quả sai. Cách sửa: in đúng `HA`.

---

## 4. Lời giải tham khảo
```python
t = int(input().strip())
if t in [1, 2, 3]:
    print("XUAN")
elif t in [4, 5, 6]:
    print("HA")
elif t in [7, 8, 9]:
    print("THU")
elif t in [10, 11, 12]:
    print("DONG")
```
