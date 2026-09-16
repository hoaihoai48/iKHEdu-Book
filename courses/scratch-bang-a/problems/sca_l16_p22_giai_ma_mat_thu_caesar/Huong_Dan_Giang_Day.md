# Hướng Dẫn Giảng Dạy: Giải mã mật thư Caesar
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: ngược với mã hóa, kéo mỗi chữ cái lùi lại `K` nấc để tìm thư gốc, hết `A` thì vòng lại `Z`.
- Quy trình với biến thật (`s`, `k`, `res`, `ch`):
  - Đọc bản mật mã `s = "DEFABC"`, `k = 3`.
  - Với từng `ch`, tính `chr((ord(ch) - ord('A') - k) % 26 + ord('A'))`: `D` về `A`, `E` về `B`, `F` về `C`, `A` về `X`, `B` về `Y`, `C` về `Z`.
  - Nối lại được `ABCXYZ` rồi in ra.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: DEFABC và 3)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s`, `k` | `s = "DEFABC"`, `k = 3` | bản mật mã và bước nhảy |
| 2 | `D, E, F` trừ 3 | `A, B, C` | lùi thẳng |
| 3 | `A, B, C` trừ 3 | `X, Y, Z` | vòng lại cuối bảng |
| 4 | `nói ("".join(res))` | màn hình hiện `ABCXYZ` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng công thức mã hóa (cộng `k`) thay vì giải mã. Đoạn sai:
```text
s = câu trả lời.strip()
k = int(câu trả lời.strip())
res = []
for ch in s:
    if 'A' <= ch <= 'Z':
        res.append(chr((ord(ch) - ord('A') + k) % 26 + ord('A')))
    else:
        res.append(ch)
print("".join(res))
```
Với mẫu `DEFABC` và `3` in ra `GHIDEF` (mã hóa hai lần), đáp án đúng là `ABCXYZ`. Cách sửa: trừ `k` như lời giải.
- Bẫy 2: trừ trực tiếp `chr(ord(ch) - k)` nên `A, B, C` văng khỏi bảng chữ. Đoạn sai khiến ba chữ cuối thành ký tự lạ thay vì `XYZ`. Cách sửa: vòng lại bằng `% 26` như lời giải.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập k:] và đợi
> - đặt [k] thành (câu trả lời)
> - đặt [xau] thành (câu trả lời)
> - đặt [do_dai] thành (độ dài của xau)
> - đặt [i] thành (1)
> - lặp lại (do_dai) lần:
> -   nói (ký tự thứ i của xau) trong (1) giây
> -   thay đổi [i] một lượng (1)
