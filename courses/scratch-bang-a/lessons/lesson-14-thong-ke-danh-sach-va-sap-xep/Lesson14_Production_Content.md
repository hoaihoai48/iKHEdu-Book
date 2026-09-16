# Bài 14: THỐNG KÊ DANH SÁCH VÀ THUẬT TOÁN SẮP XẾP

## 1. Thuật Toán Tìm Giá Trị Lớn Nhất (Max) Trong Danh Sách

```text
đặt [max v] thành (phần tử (1) của [Dãy số v])
đặt [vi_tri_max v] thành (1)

đặt [i v] thành (2)
lặp lại (((kích thước của [Dãy số v]) - (1))) lần
    nếu < (phần tử (i) của [Dãy số v]) > (max) > thì
        đặt [max v] thành (phần tử (i) của [Dãy số v])
        đặt [vi_tri_max v] thành (i)
    thay đổi [i v] một lượng (1)

nói (kết hợp [Gia tri lon nhat la: ] (max))
```

---

## 2. Thuật Toán Sắp Xếp Nổi Bọt (Bubble Sort) Trong Scratch

Để sắp xếp danh sách gồm $N$ số tăng dần:
- Dùng 2 vòng lặp lồng nhau.
- So sánh `phần tử (j)` và `phần tử (j + 1)`. Nếu phần tử trước lớn hơn phần tử sau, ta hoán đổi chúng bằng biến trung gian `tam`:

```text
đặt [tam v] thành (phần tử (j) của [Dãy số v])
thay thế phần tử (j) của [Dãy số v] bằng (phần tử ((j) + (1)) của [Dãy số v])
thay thế phần tử ((j) + (1)) của [Dãy số v] bằng (tam)
```

---

## 3. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Khởi tạo biến `max` bằng số 0**
> - *Hiện tượng:* Đặt `max = 0` khi bắt đầu tìm số lớn nhất.
> - *Hậu quả:* Nếu tất cả các số trong danh sách đều là số âm (ví dụ $-5, -12, -3$), chương trình sẽ kết luận số lớn nhất là $0$ (trong khi số 0 hoàn toàn không có trong danh sách!).
> - *Khắc phục:* Luôn gán `max = phần tử (1) của [danh_sách]`.

> **Bẫy 2: Hoán đổi trực tiếp không dùng biến trung gian `tam`**
> - *Hiện tượng:* Gán phần tử sau đè lên phần tử trước ngay lập tức.
> - *Hậu quả:* Giá trị của phần tử trước bị mất vĩnh viễn!
> - *Khắc phục:* Bắt buộc dùng 3 bước với biến `tam`.

---

## 4. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Giá trị khởi tạo an toàn nhất cho biến `max` khi tìm số lớn nhất trong danh sách là:**
   - A. Phần tử thứ nhất của danh sách *(Đáp án đúng)*
   - B. Số 0
   - C. Số 999999
   - D. Số âm vô cùng

2. **Muốn tính trung bình cộng của danh sách, ta lấy tổng các phần tử chia cho:**
   - A. `kích thước của [danh_sách]` *(Đáp án đúng)*
   - B. 2
   - C. 10
   - D. Phần tử đầu tiên

3. **Thuật toán sắp xếp nổi bọt hoạt động bằng cách:**
   - A. So sánh các cặp phần tử liền kề và đổi chỗ nếu sai thứ tự *(Đáp án đúng)*
   - B. Xóa hết các số nhỏ
   - C. Chỉ chọn số lớn nhất
   - D. Đảo ngược danh sách

4. **Để hoán đổi 2 phần tử trong danh sách, ta cần sử dụng thêm:**
   - A. Một biến trung gian `tam` *(Đáp án đúng)*
   - B. Một danh sách mới
   - C. Một nhân vật mới
   - D. Khối phát tin

5. **Nếu danh sách có 5 phần tử, sau vòng lặp ngoài đầu tiên của Bubble Sort, phần tử nào chắc chắn về đúng vị trí?**
   - A. Phần tử lớn nhất về cuối cùng *(Đáp án đúng)*
   - B. Phần tử nhỏ nhất về đầu
   - C. Tất cả các phần tử
   - D. Chưa phần tử nào

6. **Tìm kiếm tuyến tính (Linear Search) có độ phức tạp thời gian là:**
   - A. $\mathcal{O}(N)$ *(Đáp án đúng: duyệt qua từng phần tử)*
   - B. $\mathcal{O}(1)$
   - C. $\mathcal{O}(N^2)$
   - D. $\mathcal{O}(\log N)$

7. **Khối lệnh dùng để sửa giá trị một phần tử tại vị trí $k$ trong Scratch là:**
   - A. `thay thế phần tử (k) của [danh_sách] bằng ()` *(Đáp án đúng)*
   - B. `đặt [danh_sách] thành ()`
   - C. `thêm () vào [danh_sách]`
   - D. `chèn () vào [danh_sách]`

8. **Khi tìm giá trị nhỏ nhất (Min), điều kiện cập nhật là:**
   - A. `< (phần tử (i)) < (min) >` *(Đáp án đúng)*
   - B. `< (phần tử (i)) > (min) >`
   - C. `< phần tử (i) = 0 >`
   - D. `< min = 0 >`

9. **Danh sách ban đầu: `[4, 2, 5]`. Sau khi sắp xếp tăng dần, danh sách trở thành:**
   - A. `[2, 4, 5]` *(Đáp án đúng)*
   - B. `[5, 4, 2]`
   - C. `[2, 5, 4]`
   - D. `[4, 5, 2]`

10. **Nếu danh sách không chứa phần tử cần tìm, thuật toán tìm kiếm nên thông báo:**
    - A. Không tìm thấy (ví dụ in ra `-1` hoặc `KHONG CO`) *(Đáp án đúng)*
    - B. Báo lỗi
    - C. Dừng toàn bộ Scratch
    - D. In số 0
