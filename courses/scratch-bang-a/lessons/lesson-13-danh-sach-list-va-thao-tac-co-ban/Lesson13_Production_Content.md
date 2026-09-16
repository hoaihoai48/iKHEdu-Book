# Bài 13: DANH SÁCH (LIST) VÀ CÁC THAO TÁC CƠ BẢN

## 1. Các Khối Lệnh Danh Sách Trong Scratch 3.0

Trong nhóm **Các biến số (Variables)**, khi bấm tạo **Danh sách (List)** màu cam đậm:

![Minh họa khối lệnh danh sách Scratch Tiếng Việt](../../assets/rendered_blocks/l13_list_operations_vi.png)

| Khối lệnh Scratch | Tương đương Python | Chức năng |
|---|---|---|
| `thêm (X) vào [ds v]` | `ds.append(X)` | Chèn giá trị $X$ vào cuối danh sách |
| `xóa (1) của [ds v]` | `del ds[0]` | Xóa phần tử ở vị trí chỉ định |
| `xóa tất cả của [ds v]` | `ds.clear()` | Xóa sạch toàn bộ danh sách |
| `phần tử (i) của [ds v]` | `ds[i - 1]` | Đọc giá trị tại vị trí thứ $i$ (tính từ 1) |
| `kích thước của [ds v]` | `len(ds)` | Đếm số lượng phần tử hiện có |
| `[ds v] chứa (X) ?` | `X in ds` | Kiểm tra xem giá trị $X$ có trong danh sách không |

---

## 2. Khung Mẫu Nhập & Duyệt Danh Sách Chuẩn

### Bước 1: Nhập $N$ số vào danh sách
```text
xóa tất cả của [Dãy số v]
hỏi [Nhap so phan tu N:] và đợi
đặt [N v] thành (câu trả lời)

lặp lại (N) lần
    hỏi [Nhap so tiep theo:] và đợi
    thêm (câu trả lời) vào [Dãy số v]
```

### Bước 2: Duyệt danh sách để tính tổng
```text
đặt [tong v] thành (0)
đặt [i v] thành (1)
lặp lại (kích thước của [Dãy số v]) lần
    thay đổi [tong v] một lượng (phần tử (i) của [Dãy số v])
    thay đổi [i v] một lượng (1)
nói (tong)
```

---

## 3. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Quên khối `xóa tất cả của danh sách` khi bấm cờ xanh**
> - *Hiện tượng:* Không xóa danh sách cũ khi bắt đầu chạy lại chương trình.
> - *Hậu quả:* Các phần tử của lần chạy trước vẫn còn nguyên, danh sách ngày càng dài ra và kết quả bị sai be bét!
> - *Khắc phục:* Luôn đặt `xóa tất cả của [danh_sách]` ngay dưới cờ xanh.

> **Bẫy 2: Lỗi chỉ số 0 (Zero Index Trap)**
> - *Hiện tượng:* Quen tay viết `phần tử (0) của [danh_sách]`.
> - *Hậu quả:* Trong Scratch không có phần tử số 0! Khối này sẽ trả về giá trị rỗng hoặc số 0.
> - *Khắc phục:* Nhớ rằng phần tử đầu tiên trong Scratch luôn là **số 1**.

---

## 4. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Phần tử đầu tiên trong danh sách Scratch có chỉ số là:**
   - A. 0
   - B. 1 *(Đáp án đúng: 1-based index)*
   - C. -1
   - D. Tùy chọn

2. **Khối nào dùng để thêm một giá trị vào cuối danh sách?**
   - A. `thêm () vào [danh_sách]` *(Đáp án đúng)*
   - B. `đặt [danh_sách] thành ()`
   - C. `chèn () vào [danh_sách]`
   - D. `thay đổi [danh_sách] một lượng ()`

3. **Để biết danh sách đang có bao nhiêu phần tử, ta dùng khối:**
   - A. `kích thước của [danh_sách]` *(Đáp án đúng)*
   - B. `độ dài của ()`
   - C. `số lượng của ()`
   - D. `phần tử cuối của ()`

4. **Nếu danh sách có 5 phần tử, phần tử cuối cùng nằm ở vị trí số mấy?**
   - A. 4
   - B. 5 *(Đáp án đúng)*
   - C. 6
   - D. 0

5. **Lệnh nào xóa sạch mọi dữ liệu trong danh sách?**
   - A. `xóa tất cả của [danh_sách]` *(Đáp án đúng)*
   - B. `xóa (1) của [danh_sách]`
   - C. `ẩn danh sách`
   - D. `đặt [danh_sách] thành 0`

6. **Biểu thức lấy phần tử cuối cùng của danh sách bất kỳ là:**
   - A. `phần tử (kích thước của [danh_sách]) của [danh_sách]` *(Đáp án đúng)*
   - B. `phần tử (-1) của [danh_sách]`
   - C. `phần tử (0) của [danh_sách]`
   - D. `phần tử cuối cùng`

7. **Vòng lặp duyệt qua toàn bộ danh sách cần lặp lại bao nhiêu lần?**
   - A. `kích thước của [danh_sách]` lần *(Đáp án đúng)*
   - B. 10 lần
   - C. 100 lần
   - D. Vô hạn lần

8. **Khối lục giác `[danh_sách] chứa (X) ?` trả về giá trị gì?**
   - A. Đúng (True) nếu X có trong danh sách, ngược lại Sai (False) *(Đáp án đúng)*
   - B. Số vị trí của X
   - C. Số lần xuất hiện của X
   - D. Giá trị X

9. **Nếu lấy `phần tử (10) của [danh_sách]` khi danh sách chỉ có 3 phần tử, kết quả là:**
   - A. Chuỗi rỗng (không có gì) *(Đáp án đúng)*
   - B. Báo lỗi dừng chương trình
   - C. Số 0
   - D. Tự động thêm phần tử

10. **Lý do bắt buộc phải `xóa tất cả của danh sách` khi bắt đầu là:**
    - A. Để dọn sạch dữ liệu của lần chạy trước đó *(Đáp án đúng)*
    - B. Để giải phóng bộ nhớ máy tính
    - C. Bắt buộc của Scratch
    - D. Để nhân vật không bị lag
