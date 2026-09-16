# Hướng Dẫn Giảng Dạy: Tách mảng chẵn và mảng lẻ
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là chia dãy thành hai hàng: hàng số chẵn và hàng số lẻ, mỗi hàng giữ nguyên thứ tự ban đầu.
- Với số mẫu `N = 6`, dãy `1 4 7 8 2 9`: hàng chẵn gồm `4 8 2`, hàng lẻ gồm `1 7 9`.
- Quy trình trong lời giải với các biến `n`, `a`, `chan`, `le`, `x`:
  - Đọc `n = 6`, dãy `a = [1, 4, 7, 8, 2, 9]`.
  - Lọc `x % 2 == 0` được `chan = [4, 8, 2]`; lọc `x % 2 != 0` được `le = [1, 7, 9]`.
  - In hàng chẵn trước, hàng lẻ sau.
- Giá trị biên cụ thể: dãy toàn số chẵn thì hàng lẻ rỗng và vẫn in một dòng trống; dãy toàn số lẻ thì ngược lại.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 6 / 1 4 7 8 2 9)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 6` |
| 2 | Đọc dãy `a` | `a = [1, 4, 7, 8, 2, 9]` |
| 3 | Lọc chẵn | `chan = [4, 8, 2]` |
| 4 | Lọc lẻ | `le = [1, 7, 9]` |
| 5 | In dòng 1 | màn hình hiện `4 8 2` |
| 6 | In dòng 2 | màn hình hiện `1 7 9` |

Kết quả cuối cùng khớp với đáp án mẫu: `4 8 2` rồi `1 7 9`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — in hàng lẻ trước hàng chẵn:
```text
n = int(câu trả lời.strip())
a = list(map(int, câu trả lời.split()))
chan = [x for x in a if x % 2 == 0]
le = [x for x in a if x % 2 != 0]
print(*le)
print(*chan)
```
Với mẫu trên in ra `1 7 9` rồi `4 8 2`, ngược thứ tự đáp án mẫu. Cách sửa: in `chan` trước rồi mới in `le`.
- Bẫy 2 — sắp xếp lại làm mất thứ tự ban đầu:
```text
n = int(câu trả lời.strip())
a = list(map(int, câu trả lời.split()))
chan = sorted([x for x in a if x % 2 == 0])
le = sorted([x for x in a if x % 2 != 0])
print(*chan)
print(*le)
```
Với mẫu trên in ra `2 4 8` thay vì `4 8 2` sai. Cách sửa: lọc trực tiếp, không gọi `sorted`.
- Bẫy 3 — in cả hai hàng trên một dòng:
```text
n = int(câu trả lời.strip())
a = list(map(int, câu trả lời.split()))
chan = [x for x in a if x % 2 == 0]
le = [x for x in a if x % 2 != 0]
print(*chan, *le)
```
Với mẫu trên in ra `4 8 2 1 7 9` trên một dòng, không khớp đáp án mẫu hai dòng. Cách sửa: in hai khối lệnh `nói` riêng.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - xóa tất cả của [danh_sach]
> - đặt [i] thành (1)
> - lặp lại (n) lần:
> -   hỏi [Nhập phần tử:] và đợi
> -   thêm (câu trả lời) vào [danh_sach]
> -   thay đổi [i] một lượng (1)
> - nói (phần tử thứ 1 của [danh_sach])
