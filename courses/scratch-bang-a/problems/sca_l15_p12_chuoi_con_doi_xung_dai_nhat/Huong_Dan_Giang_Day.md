# Hướng Dẫn Giảng Dạy

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất: chuỗi con là một đoạn ký tự đứng liền nhau; cần tìm đoạn đọc xuôi ngược giống nhau mà dài nhất trong vòng hạt của bạn Mít.
- Quy trình với biến thật trong lời giải (`s`, `n`, `dai_nhat`, `i`, `j`, `doan`):
  - Đọc `s = "ABCBADE"`, `n = 7`, khởi động `dai_nhat = 1` (một chữ cái đơn luôn đối xứng).
  - Cho `i` chạy từ 0 đến 6, `j` chạy từ `i + 1` đến 7, cắt `doan = s[i:j]` rồi kiểm tra `doan == doan[::-1]`.
  - Với mẫu, đoạn `s[0:5]` là `ABCBA` đọc ngược vẫn là `ABCBA` nên `dai_nhat` thành 5. Không còn đoạn nào dài hơn nên in 5.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: ABCBADE)
| Bước | Lệnh chạy | Giá trị trong máy | Ghi chú |
|---|---|---|---|
| 1 | `s = câu trả lời` | `s = "ABCBADE"`, `n = 7` | vòng hạt 7 chữ |
| 2 | `dai_nhat = 1` | `1` | mỗi chữ đơn đều đối xứng |
| 3 | `i = 0, j = 5` | `doan = "ABCBA"` | đoạn từ 0 đến 4 |
| 4 | `doan == doan[::-1]` | `"ABCBA" == "ABCBA"` đúng | cập nhật `dai_nhat = 5` |
| 5 | các cặp còn lại | không vượt qua 5 | ví dụ `s[1:4] = "BCB"` dài 3 |
| 6 | `nói (dai_nhat)` | màn hình hiện `5` | khớp Output mẫu |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: so với cả chuỗi gốc `if doan == s[::-1]`. Đoạn sai:
```text
s = câu trả lời
n = len(s)
dai_nhat = 1
for i in range(n):
    for j in range(i + 1, n + 1):
        doan = s[i:j]
        if doan == s[::-1]:
            if len(doan) > dai_nhat:
                dai_nhat = len(doan)
nói (dai_nhat)

```
Với mẫu `ABCBADE`, `s[::-1]` là `EDABCBA` nên hầu như không đoạn nào khớp, in ra `1`, đáp án đúng là `5`. Cách sửa: so với chính nó đảo lại `doan == doan[::-1]`.
- Bẫy 2: cắt đoạn sai `doan = s[i:j + 1]` vượt biên. Đoạn sai khiến đoạn dài nhất có thể bị tính lệch và vòng lặp dễ lẫn, ví dụ với mẫu vẫn có nguy cơ cho số khác 5 tùy cách viết. Cách sửa: giữ đúng `doan = s[i:j]` với `j` chạy tới `n`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập s:] và đợi
> - đặt [s] thành (câu trả lời)
> - đặt [n] thành (độ dài của s)
> - đặt [dai_nhat] thành (1)
> - đặt [i] thành (0)
> - lặp lại (n) lần:
> -   đặt [j] thành (i + 1)
> -   lặp lại (n + 1 - i + 1) lần:
> -     đặt [doan] thành (giá trị)
> -     nếu <doan = giá trị> thì:
> -       nếu <độ dài của doan > dai_nhat> thì:
> -         đặt [dai_nhat] thành (độ dài của doan)
> -     thay đổi [j] một lượng 1
> -   thay đổi [i] một lượng 1
> - nói (dai_nhat)
