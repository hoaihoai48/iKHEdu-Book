# Hướng Dẫn Giảng Dạy: Tìm tất cả số hoàn hảo nhỏ hơn N
Chuyên đề: **Đếm Số Theo Quy Luật & Các Con Số Đặc Biệt**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: xét từng `num` từ `2` tới `30`, tính tổng các ước nhỏ hơn `num`, tổng bằng `num` thì ghi vào danh sách `ket_qua`.
- Với `num = 6`: các ước nhỏ hơn là `1, 2, 3`, tổng `6` nên ghi `6`.
- Với `num = 28`: các ước nhỏ hơn là `1, 2, 4, 7, 14`, tổng `1 + 2 + 4 + 7 + 14 = 28` nên ghi `28`.
- Các `num` còn lại tới `30` không thỏa mãn, danh sách cuối là `["6", "28"]`, in ra `6 28`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 30)
| `num` | Các ước nhỏ hơn `num` | Tổng | Ghi? |
| --- | --- | --- | --- |
| 6 | `1, 2, 3` | `6` | ghi `6` |
| 7–27 (trừ 28) | — | khác chính nó | không ghi |
| 28 | `1, 2, 4, 7, 14` | `28` | ghi `28` |
| 29, 30 | — | khác chính nó | không ghi |

Kết quả in ra: `6 28`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: cộng cả chính `num` vào tổng. Với mẫu `30`, `num = 6` cho tổng `12` nên bị loại, danh sách rỗng và không in gì. Sửa lại: chỉ cộng khi `i < num` và `j < num` như bài giải.
- Bẫy 2: quên kiểm tra `j != i`. Với `num = 36` (chính phương) ước `6` bị cộng hai lần, tổng sai. Sửa lại: giữ điều kiện `j != i` như bài giải.
- Bẫy 3: in danh sách trực tiếp `print(ket_qua)`. Với mẫu `30` sẽ in `['6', '28']` kèm ngoặc và dấu phẩy, là kết quả sai. Sửa lại: `print(" ".join(ket_qua))`.

---

## 4. Lời giải tham khảo
```python
n = int(input())
ket_qua = []
for num in range(2, n + 1):
    tong = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            j = num // i
            if i < num:
                tong = tong + i
            if j != i and j < num:
                tong = tong + j
    if tong == num:
        ket_qua.append(str(num))
if ket_qua:
    print(" ".join(ket_qua))
```
