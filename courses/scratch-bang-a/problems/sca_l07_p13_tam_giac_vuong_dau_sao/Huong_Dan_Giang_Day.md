# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: dòng thứ `i` có đúng `i` dấu sao. Nhân chuỗi `'*' * i` được một hàng có độ dài tăng dần từ 1 tới N.
- Quy trình trong lời giải: đọc `n`, vòng lặp cho `i` chạy từ 1 tới `n`, mỗi lượt `nói ('*' * i)` in một hàng.
- Xử lý biên: với N nhỏ nhất là 1 thì chỉ in một dòng `*`; với N lớn nhất là 50 thì hàng cuối có đúng 50 dấu sao.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 4)
| Lượt lặp | Giá trị của `i` | `'*' * i` | Dòng in ra |
|---|---|---|---|
| 1 | 1 | `*` | * |
| 2 | 2 | `**` | ** |
| 3 | 3 | `***` | *** |
| 4 | 4 | `****` | **** |

Bốn dòng ghép lại thành tam giác mẫu, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — dùng `range(n)`:
```text
n = câu trả lời
for i in range(n):
    nói ('*' * i)

```
Với mẫu `4` dòng đầu là chuỗi rỗng và chỉ in tới 3 sao, cho kết quả sai. Cách sửa: dùng `range(1, n + 1)`.
- Bẫy 2 — in sao cách nhau dấu cách:
```text
n = câu trả lời
for i in range(1, n + 1):
    nói ('* ' * i)

```
Với mẫu `4` dòng đầu thành `* ` có dấu cách thừa, chương trình kiểm tra báo kết quả sai. Cách sửa: nhân đúng `'*' * i` không thêm dấu cách.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - đặt [i] thành (1)
> - lặp lại (n) lần:
> -   nói (* * i)
> -   thay đổi [i] một lượng 1
