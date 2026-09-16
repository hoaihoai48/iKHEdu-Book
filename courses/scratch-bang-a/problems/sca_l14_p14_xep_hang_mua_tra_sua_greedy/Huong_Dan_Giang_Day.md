# Hướng Dẫn Giảng Dạy: Xếp hàng mua trà sữa (Greedy)
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán

- Bản chất của bài này là cho bạn pha nhanh lên mua trước thì cả hàng chờ ít nhất, vì mỗi phút pha xong sớm giúp mọi bạn đứng sau bớt chờ.
- Với số mẫu `N = 3`, các thời gian `3 1 2`: xếp lại thành `1 2 3`. Bạn thứ nhất chờ `1` phút, bạn thứ hai chờ `1 + 2 = 3` phút, bạn thứ ba chờ `1 + 2 + 3 = 6` phút; tổng thời gian chờ là `1 + 3 + 6 = 10`.
- Quy trình trong lời giải với các biến `n`, `cac_so`, `tong`, `da_cho`, `t`:
  - Đọc `n = 3`, gom `cac_so = [3, 1, 2]` rồi xếp thành `[1, 2, 3]`, đặt `tong = 0`, `da_cho = 0`.
  - Xét `t = 1`: `da_cho = 1`, `tong = 1`. Xét `t = 2`: `da_cho = 3`, `tong = 4`. Xét `t = 3`: `da_cho = 6`, `tong = 10`.
  - In `10`.
- Giá trị biên cụ thể: `N = 1` thì tổng chờ bằng đúng thời gian của bạn duy nhất đó; `T` tới `1000` và `N` tới `10^5` nên tổng vừa trong số nguyên thường.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 / 3 1 2)

| Bước | Thao tác | Giá trị |
|------|----------|---------|
| 1 | Đọc `n`, gom `cac_so` | `n = 3`, `cac_so = [3, 1, 2]` |
| 2 | Xếp `sorted` | `cac_so = [1, 2, 3]`, `tong = 0`, `da_cho = 0` |
| 3 | Xét `t = 1` | `da_cho = 1`, `tong = 1` |
| 4 | Xét `t = 2` | `da_cho = 3`, `tong = 4` |
| 5 | Xét `t = 3` | `da_cho = 6`, `tong = 10` |
| 6 | In kết quả | màn hình hiện `10` |

Kết quả cuối cùng khớp với đáp án mẫu: `10`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp

- Bẫy 1 — giữ nguyên thứ tự nhập mà không xếp:
```text
n = int(câu trả lời.split()[0])
cac_so = []
while len(cac_so) < n:
    try:
        cac_so.extend(map(int, câu trả lời.split()))
    except EOFError:
        break
tong = 0
da_cho = 0
for t in cac_so:
    da_cho = da_cho + t
    tong = tong + da_cho
print(tong)
```
Với mẫu `3 1 2`, thời gian chờ từng bạn thành `3`, `4`, `6`, tổng `13` lớn hơn đáp án tối ưu `10`. Cách sửa: xếp `cac_so = sorted(cac_so)` trước vòng lặp.
- Bẫy 2 — cộng tổng thời gian pha thay vì tổng thời gian chờ:
```text
n = int(câu trả lời.split()[0])
cac_so = []
while len(cac_so) < n:
    try:
        cac_so.extend(map(int, câu trả lời.split()))
    except EOFError:
        break
cac_so = sorted(cac_so)
print(sum(cac_so))
```
Với mẫu trên in ra `1 + 2 + 3 = 6` sai. Cách sửa: cộng dồn `da_cho` của từng bạn vào `tong`.
- Bẫy 3 — xếp ngược bạn pha lâu lên trước:
```text
n = int(câu trả lời.split()[0])
cac_so = []
while len(cac_so) < n:
    try:
        cac_so.extend(map(int, câu trả lời.split()))
    except EOFError:
        break
cac_so = sorted(cac_so, reverse=True)
tong = 0
da_cho = 0
for t in cac_so:
    da_cho = da_cho + t
    tong = tong + da_cho
print(tong)
```
Với mẫu trên, thứ tự `3 2 1` cho thời gian chờ `3`, `5`, `6`, tổng `14` sai. Cách sửa: xếp tăng dần để bạn nhanh lên trước.

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
