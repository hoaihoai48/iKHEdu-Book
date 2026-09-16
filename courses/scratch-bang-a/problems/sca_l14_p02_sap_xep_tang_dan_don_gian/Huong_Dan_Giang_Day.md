# Hướng Dẫn Giảng Dạy: Sắp xếp tăng dần đơn giản
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là xếp các số từ bé đến lớn.
- Với số mẫu `N = 5`, dãy `9 2 7 1 5`: xếp lại thành `1 2 5 7 9`.
- Quy trình trong lời giải với các biến `n`, `a`:
  - Đọc `n = 5`, dãy `a = [9, 2, 7, 1, 5]`.
  - Gọi `a.sort()` được `[1, 2, 5, 7, 9]` rồi in ra.
- Giá trị biên cụ thể: `N = 1` thì in nguyên số đó; dãy đã tăng sẵn thì kết quả giống hệt đầu vào.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 / 9 2 7 1 5)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n` | `n = 5` |
| 2 | Đọc dãy `a` | `a = [9, 2, 7, 1, 5]` |
| 3 | Gọi `a.sort()` | `a = [1, 2, 5, 7, 9]` |
| 4 | In kết quả | màn hình hiện `1 2 5 7 9` |

Kết quả cuối cùng khớp với đáp án mẫu: `1 2 5 7 9`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — quên xếp mà in nguyên dãy nhập:
```text
n = int(câu trả lời.strip())
a = list(map(int, câu trả lời.split()))
print(*a)
```
Với mẫu trên in ra `9 2 7 1 5` sai. Cách sửa: gọi `a.sort()` trước khi in.
- Bẫy 2 — xếp giảm dần:
```text
n = int(câu trả lời.strip())
a = list(map(int, câu trả lời.split()))
a.sort(reverse=True)
print(*a)
```
Với mẫu trên in ra `9 7 5 2 1` sai. Cách sửa: xếp tăng dần mặc định bằng `a.sort()`.
- Bẫy 3 — gán kết quả của `sort`:
```text
n = int(câu trả lời.strip())
a = list(map(int, câu trả lời.split()))
a = a.sort()
print(*a)
```
`a.sort()` xếp ngay trên danh sách và trả về rỗng nên `a` thành rỗng, in ra dòng trống thay vì `1 2 5 7 9`. Cách sửa: gọi `a.sort()` riêng một dòng rồi in `*a`.

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
