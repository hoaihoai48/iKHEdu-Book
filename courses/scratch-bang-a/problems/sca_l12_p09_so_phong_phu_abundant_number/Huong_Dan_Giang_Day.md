# Hướng Dẫn Giảng Dạy: Số phong phú (abundant number)
Chuyên đề: **Lập Trình Thuật Toán & Khối Lệnh Scratch 3.0**

---

## 1. Ý tưởng & Phân tích thuật toán
- Bản chất của bài này: số phong phú là số mà tổng các ước nhỏ hơn nó lớn hơn chính nó; xét từng `num` từ `1` tới `20`.
- `num = 12`: ước nhỏ hơn là `1, 2, 3, 4, 6`, tổng `16 > 12` nên ghi `12`.
- `num = 18`: ước nhỏ hơn là `1, 2, 3, 6, 9`, tổng `21 > 18` nên ghi `18`.
- `num = 20`: ước nhỏ hơn là `1, 2, 4, 5, 10`, tổng `22 > 20` nên ghi `20`; các số còn lại không thỏa mãn.
- Danh sách cuối là `["12", "18", "20"]`, in ra `12 18 20`.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 20)
| `num` | Các ước nhỏ hơn | Tổng | So với `num` | Ghi? |
| --- | --- | --- | --- | --- |
| 12 | `1, 2, 3, 4, 6` | 16 | `16 > 12` | ghi |
| 18 | `1, 2, 3, 6, 9` | 21 | `21 > 18` | ghi |
| 20 | `1, 2, 4, 5, 10` | 22 | `22 > 20` | ghi |
| các số khác tới 20 | — | `<= num` | không lớn hơn | không ghi |

Kết quả in ra: `12 18 20`, khớp với kết quả mẫu.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- Bẫy 1: dùng điều kiện `tong == num` (số hoàn hảo) thay vì `tong > num`. Với mẫu `20` không số nào thỏa mãn nên chẳng in gì. Sửa lại: `if tong > num` như bài giải.
- Bẫy 2: cộng cả chính `num` vào tổng. Khi đó mọi số đều có tổng lớn hơn chính nó và in ra cả dãy `1..20`. Sửa lại: chỉ cộng khi `i < num` và `j < num` như bài giải.
- Bẫy 3: so sánh `tong >= num`. Với mẫu `20` thì trùng cờ vẫn ra `12 18 20`, nhưng với đoạn chứa số hoàn hảo như `6` sẽ ghi thừa số `6`. Sửa lại: điều kiện đúng là `tong > num`.

---

## 4. Lời giải tham khảo & Kịch bản Khối lệnh Scratch 3.0

### 4.1. Khối lệnh đồ họa trực quan (Visual Scratch Blocks)

![Khối lệnh Scratch 3.0 giải mẫu](solution_blocks_vi.png)

> 💡 **Kịch bản thực hiện từng bước:**
> - khi bấm vào cờ xanh
> - hỏi [Nhập n:] và đợi
> - đặt [n] thành (câu trả lời)
> - nói (" ".join(ket_qua)
