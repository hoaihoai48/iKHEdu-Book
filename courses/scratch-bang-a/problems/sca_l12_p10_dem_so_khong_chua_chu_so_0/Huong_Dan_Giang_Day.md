# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: xét từng `i` từ `1` tới `15`, số nào có ít nhất một chữ số `0` thì bỏ, còn lại thì `dem = dem + 1`.
- Mỗi số được soi từng chữ số bằng `(temp mod 10)`: gặp dư `0` là gắn cờ `co_so_0 = True` và dừng soi số đó.
- Từ `1` tới `15` chỉ có đúng số `10` chứa chữ số `0` (vì `(10 mod 10) == 0`), còn lại `14` số đều sạch.
- Đáp án là `15 - 1 = 14`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 15)
| `i` | Soi chữ số | Có số 0? | `dem` |
| --- | --- | --- | --- |
| 1–9 | một chữ số khác 0 | không | 1–9 |
| 10 | `(10 mod 10) == 0` | có, bỏ qua | 9 |
| 11 | `1`, `1` | không | 10 |
| 12 | `2`, `1` | không | 11 |
| 13 | `3`, `1` | không | 12 |
| 14 | `4`, `1` | không | 13 |
| 15 | `5`, `1` | không | 14 |

Kết quả in ra: `14`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: kiểm tra `(i mod 10) == 0` thay vì soi mọi chữ số. Với mẫu `15` thì trùng cờ vẫn ra `14`, nhưng với `N = 101` sẽ bỏ sót số `101` (số `0` nằm ở giữa). Sửa lại: soi từng chữ số bằng vòng lặp `while temp > 0` như bài giải.
- Bẫy 2: quên `break` sau khi phát hiện chữ số `0`. Với mẫu `15` vẫn đúng, nhưng với số nhiều chữ số `0` chương trình soi thừa không cần thiết. Sửa lại: `break` ngay khi gặp dư `0`.
- Bẫy 3: đếm ngược (đếm số chứa số `0`). Với mẫu `15` sẽ in `1` thay vì `14`. Sửa lại: chỉ cộng khi `not co_so_0`.

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
> -   đặt [temp] thành (i)
> -   đặt [co_so_0] thành (False)
> -   lặp lại cho đến khi <temp = 0>:
> -     nếu <temp mod 10 = 0> thì:
> -       đặt [co_so_0] thành (True)
> -       dừng kịch bản này
> -     đặt [temp] thành (temp chia nguyên 10)
> -   nếu <điều kiện> thì:
> -     đặt [dem] thành (dem + 1)
> -   thay đổi [i] một lượng 1
> - nói (dem)
