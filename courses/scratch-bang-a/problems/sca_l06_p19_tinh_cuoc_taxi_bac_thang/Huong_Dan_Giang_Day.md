# Hướng Dẫn Giảng Dạy: Tính cước taxi bậc thang
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này là giá ba bậc theo km `n`: `1` km đầu giá `10` nghìn, từ km thứ `2` tới km thứ `10` mỗi km `8` nghìn, từ km thứ `11` trở đi mỗi km `6` nghìn.
- Cách làm của lời giải mẫu: đọc `n`; nếu `n <= 1` in `10`, nếu `n <= 10` in `10 + (n - 1) * 8`, còn lại in `10 + 9 * 8 + (n - 10) * 6`. Với mẫu `n = 1`: `1 <= 1` đúng nên in `10`.
- Xử lý biên: ràng buộc `1 <= N <= 100`. Thầy cô cho thử `n = 5` (`10 + 4 * 8 = 42`) và `n = 12` (`10 + 72 + 12 = 94`).

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 1)
Sample 1 với input mẫu: `1`.
| Bước | Việc làm | Giá trị của `n` | In ra |
|---|---|---|---|
| 1 | Đọc input | `n = 1` | — |
| 2 | Kiểm tra `1 <= 1`? Đúng | rẽ nhánh một | — |
| 3 | In `10` | — | `10` |

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1 — nhân cả quãng đường một giá: bạn nhỏ viết `nói (n * 8)`. Với mẫu `n = 1` sẽ in `8` thay vì `10`. Cách sửa: giữ giá mở cửa `10` cho km đầu như lời giải mẫu.
- Bẫy 2 — quên trừ phần đã tính: bạn nhỏ viết `10 + n * 8` cho nhánh giữa. Với `n = 5` sẽ in `50` thay vì `42`. Cách sửa: chỉ nhân `(n - 1) * 8`.
- Bẫy 3 — đảo thứ tự nhánh: bạn nhỏ viết `if n <= 10` trước `if n <= 1`. Với `n = 1` sẽ rơi ngay nhánh `10 + 0 * 8 = 10`, trùng cờ vẫn đúng, nhưng với cách viết `if n > 10` trước mà quên `elif` thì dễ in hai lần. Cách sửa: giữ đúng thứ tự `n <= 1`, `n <= 10`, còn lại như lời giải mẫu.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - nếu <n <= 1> thì:
> -   nói [YES]
> - nếu không thì:
> -   nói [NO]
