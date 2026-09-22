# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: với `n = 12`, vừa kiểm tra `(12 mod i) == 0` vừa kiểm tra `(i mod 2) == 0`, cả hai điều kiện đúng mới đếm.
- Biến `dem` bắt đầu bằng `0`, mỗi ước chẵn làm `dem = dem + 1`.
- Các ước của `12` là `1, 2, 3, 4, 6, 12`, trong đó số chẵn là `2, 4, 6, 12` nên kết quả là `4`.
- Thầy cô cho các em gạch chân các ước chẵn của `12` trước khi nhìn vào điều kiện kép trong chương trình.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 12)
| `i` | `(12 mod i) == 0` | `(i mod 2) == 0` | `dem` sau bước |
| --- | --- | --- | --- |
| 1 | đúng | sai | 0 |
| 2 | đúng | đúng | 1 |
| 3 | đúng | sai | 1 |
| 4 | đúng | đúng | 2 |
| 5 | sai | — | 2 |
| 6 | đúng | đúng | 3 |
| 7–11 | sai | — | 3 |
| 12 | đúng | đúng | 4 |

Kết quả in ra: `4`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: chỉ kiểm tra ước mà quên kiểm tra chẵn:
```text
if (n mod i) == 0:
    dem = dem + 1

```
với mẫu `12` sẽ đếm cả `1, 3` và in ra `6`, là kết quả sai. Sửa lại: `if (n mod i) == 0 and (i mod 2) == 0`.
- Bẫy 2: kiểm tra `(n mod 2) == 0` thay vì `(i mod 2) == 0`. Với mẫu `12` thì `12` là số chẵn nên đếm cả 6 ước và in `6`. Sửa lại: kiểm tra từng `i`, tức `(i mod 2) == 0`.
- Bẫy 3: dùng `or` thay vì `and`. Với mẫu `12` các số `1, 3, 5, 7, 8, 9, 10, 11` bị đếm thêm nên ra `11`. Sửa lại: phải đồng thời hai điều kiện nên dùng `and`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [dem] thành (0)
> - đặt [i] thành (1)
> - lặp lại (n) lần:
> -   nếu <điều kiện> thì:
> -     đặt [dem] thành (dem + 1)
> -   thay đổi [i] một lượng 1
> - nói (dem)
