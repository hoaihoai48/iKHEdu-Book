# Bài 14: THỐNG KÊ DANH SÁCH VÀ THUẬT TOÁN SẮP XẾP

## 1. Sức Mạnh Của Thống Kê Dữ Liệu Trong Lập Trình

Sau khi đã lưu trữ được hàng loạt con số vào danh sách, nhiệm vụ quan trọng tiếp theo của người lập trình là **trích xuất thông tin có giá trị** từ mớ dữ liệu thô đó:

- Tìm giá trị lớn nhất (**Max**) hoặc nhỏ nhất (**Min**) trong các bài toán đo lường, chấm thi.
- Tính giá trị **Trung bình cộng** của dãy số.
- Đếm số lượng phần tử thỏa mãn tính chất đặc thù (bao nhiêu số nguyên tố, bao nhiêu bạn đạt điểm 10).
- **Sắp xếp thứ tự (Sorting):** Một trong những thuật toán kinh điển và quan trọng nhất của khoa học máy tính.

---

## 2. Thuật Toán Tìm Giá Trị Lớn Nhất (Max) & Nhỏ Nhất (Min)

Trong Scratch, không có sẵn khối tìm Max tự động cho cả danh sách tự động. Do đó, học sinh bắt buộc phải tự cài đặt thuật toán tìm kiếm tuần tự.

![Thuật toán tìm Max trong danh sách](assets/rendered_blocks/l14_find_max_list_vi.png)

### 2.1. Bản chất tư duy của thuật toán tìm Max:

1. **Giả định ban đầu:** Coi phần tử đầu tiên là số lớn nhất tạm thời: `đặt [max v] thành (phần tử (1) của [Dãy số v])`, đồng thời ghi nhận `đặt [vi_tri_max v] thành (1)`.

2. **Duyệt qua các phần tử còn lại:** Cho biến `i` chạy từ vị trí `2` đến hết danh sách (`kích thước - 1` lần).

3. **So sánh & cập nhật:** Nếu gặp bất kỳ phần tử nào lớn hơn `max` hiện tại (`< (phần tử (i) của [Dãy số]) > (max) >`):

   - Cập nhật kỷ lục mới: `đặt [max v] thành (phần tử (i) của [Dãy số v])`.
   - Cập nhật vị trí mới: `đặt [vi_tri_max v] thành (i)`.

4. Sau khi duyệt hết danh sách, biến `max` chắc chắn giữ giá trị lớn nhất toàn bộ dãy.

> 💡 **Mẹo đối xứng:** Để tìm giá trị nhỏ nhất (**Min**), ta làm y hệt, chỉ cần đổi dấu so sánh thành `< (phần tử (i) của [Dãy số]) < (min) >`.

---

## 3. Thuật Toán Sắp Xếp Nổi Bọt (Bubble Sort)

**Sắp xếp nổi bọt (Bubble Sort)** là thuật toán sắp xếp trực quan và dễ hiểu nhất cho học sinh Tiểu học.

### 3.1. Ý tưởng thuật toán:
Giống như các bọt khí nhẹ hơn sẽ nổi dần lên mặt nước:

- Ta duyệt qua danh sách, so sánh từng cặp hai phần tử đứng liền kề nhau: `phần tử (j)` và `phần tử (j + 1)`.
- Nếu phần tử đứng trước lại lớn hơn phần tử đứng sau (sai trật tự tăng dần), ta lập tức **hoán đổi vị trí** của chúng!
- Lặp lại quá trình so sánh cặp này nhiều vòng, cho đến khi toàn bộ các số lớn đều dạt dần về cuối danh sách.

![Thuật toán sắp xếp nổi bọt Bubble Sort](assets/rendered_blocks/l14_bubble_sort_vi.png)

### 3.2. Kỹ thuật hoán đổi 2 phần tử bằng biến trung gian `tam`:
Để đổi chỗ giá trị ở vị trí `j` và `j + 1` mà không làm mất dữ liệu:

1. `đặt [tam v] thành (phần tử (j) của [Dãy số v])` *(Cất giá trị ô thứ j vào biến tam)*

2. `thay thế phần tử (j) của [Dãy số v] bằng (phần tử ((j) + (1)) của [Dãy số v])` *(Ghi đè ô j+1 vào ô j)*

3. `thay thế phần tử ((j) + (1)) của [Dãy số v] bằng (tam)` *(Lấy giá trị từ biến tam ghi vào ô j+1)*

---

## 4. Bảng Mô Phỏng Sắp Xếp Dãy Số `[9, 4, 2]` Bằng Bubble Sort (Dry Run Table)

Giả sử danh sách gồm 3 phần tử ban đầu: `[9, 4, 2]`. $N = 3$.

| Lần lặp ngoài `i` | Lần lặp trong `j` | Cặp so sánh `(j, j+1)` | So sánh `< ds[j] > ds[j+1] >` | Hành động | Trạng thái danh sách sau bước |
|:---:|:---:|:---:|:---:|---|:---:|
| — | — | — | — | Trạng thái bắt đầu | `[9, 4, 2]` |
| **Vòng 1** | $j = 1$ | `(9, 4)` | $9 > 4$ $\to$ **ĐÚNG** | Hoán đổi $9$ và $4$ bằng biến `tam` | `[4, 9, 2]` |
| | $j = 2$ | `(9, 2)` | $9 > 2$ $\to$ **ĐÚNG** | Hoán đổi $9$ và $2$ bằng biến `tam` | `[4, 2, 9]` |
| | *(Hết vòng 1: Số 9 lớn nhất đã nổi bọt về đúng vị trí cuối cùng!)* | | | | |
| **Vòng 2** | $j = 1$ | `(4, 2)` | $4 > 2$ $\to$ **ĐÚNG** | Hoán đổi $4$ và $2$ bằng biến `tam` | `[2, 4, 9]` |
| | $j = 2$ | `(4, 9)` | $4 > 9$ $\to$ SAI | Không đổi chỗ | `[2, 4, 9]` |

$\implies$ Sau 2 vòng lặp lớn, danh sách đã được sắp xếp tăng dần hoàn hảo: `[2, 4, 9]`.

---

## 5. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Khởi tạo biến `max` bằng số 0**
> - *Hiện tượng:* Đặt `max = 0` khi chuẩn bị tìm giá trị lớn nhất trong danh sách.
> - *Hậu quả khủng khiếp:* Nếu tất cả các số trong danh sách đều là số âm (ví dụ: `[-15, -7, -32, -4]`), máy tính sẽ so sánh và kết luận số lớn nhất là **0**! (Trong khi số 0 hoàn toàn không hề có trong danh sách!).
> - *Khắc phục:* Luôn luôn khởi tạo `max = phần tử (1) của danh sách`.

> **Bẫy 2: Hoán đổi trực tiếp không dùng biến trung gian `tam`**
> - *Hiện tượng:* Học sinh thay thế ngay: `thay thế phần tử (j) bằng phần tử (j + 1)` rồi lại `thay thế phần tử (j + 1) bằng phần tử (j)`.
> - *Hậu quả:* Ngay tại bước 1, giá trị ban đầu của phần tử `j` đã bị ghi đè và mất sạch vĩnh viễn! Hai ngăn tủ lúc này đều chứa cùng một giá trị giống hệt nhau!
> - *Khắc phục:* Bắt buộc phải dùng chiếc cốc phụ (biến `tam`) để hứng dữ liệu tạm thời.

> **Bẫy 3: Duyệt chỉ số `j` vượt quá biên danh sách**
> - *Hiện tượng:* Trong vòng lặp trong, cho $j$ chạy đến tận $N$ (`kích thước của danh sách`).
> - *Hậu quả:* Lúc này khối `phần tử (j + 1)` sẽ truy cập vào vị trí $N + 1$ (vị trí không tồn tại, giá trị rỗng). Phép so sánh sẽ bị sai lệch hoàn toàn.
> - *Khắc phục:* Vòng lặp trong chỉ cho $j$ chạy tối đa đến `kích thước - 1`.

---

## 6. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Giá trị khởi tạo an toàn nhất cho biến `max` khi tìm số lớn nhất trong danh sách là:**
   - A. Phần tử thứ nhất của danh sách *(Đáp án đúng: `phần tử (1)`)*
   - B. Số 0
   - C. Số 999999
   - D. Số âm vô cùng

2. **Muốn tính trung bình cộng của toàn bộ danh sách, ta lấy tổng các phần tử chia cho:**
   - A. `kích thước của [Dãy số v]` *(Đáp án đúng: số lượng phần tử)*
   - B. 2
   - C. 10
   - D. Phần tử cuối cùng của danh sách

3. **Thuật toán sắp xếp nổi bọt (Bubble Sort) hoạt động dựa trên nguyên lý nào?**
   - A. Chia đôi danh sách thành hai nửa
   - B. Liên tục so sánh và hoán đổi các cặp phần tử đứng liền kề nếu chúng sai thứ tự *(Đáp án đúng)*
   - C. Tìm phần tử nhỏ nhất rồi ném ra danh sách mới
   - D. Chọn ngẫu nhiên hai phần tử để đổi chỗ

4. **Để hoán đổi giá trị giữa hai ô nhớ mà không bị mất dữ liệu, ta cần tối thiểu:**
   - A. 1 bước duy nhất
   - B. 2 bước
   - C. 3 bước kết hợp 1 biến trung gian *(Đáp án đúng)*
   - D. Không thể làm được trong Scratch

5. **Nếu danh sách đang có 4 phần tử, sau vòng duyệt thứ nhất của Bubble Sort (vòng lặp $j$), phần tử nào chắc chắn đã về đúng vị trí cuối cùng?**
   - A. Phần tử nhỏ nhất
   - B. Phần tử lớn nhất toàn danh sách *(Đáp án đúng: số lớn nhất đã nổi về cuối)*
   - C. Phần tử đứng đầu
   - D. Phần tử ở vị trí thứ hai

6. **Khi tìm giá trị nhỏ nhất (Min), ta cần khởi tạo biến `min` bằng:**
   - A. Phần tử thứ nhất của danh sách *(Đáp án đúng: `phần tử (1)`)*
   - B. Số 0
   - C. Số lớn nhất có thể
   - D. Số âm vô cùng

7. **Điều kiện nào trong Bubble Sort chứng tỏ cặp số liền kề đang bị sai thứ tự (cần sắp xếp tăng dần)?**
   - A. `< (phần tử (j)) < (phần tử ((j) + (1))) >`
   - B. `< (phần tử (j)) > (phần tử ((j) + (1))) >` *(Đáp án đúng: số trước lớn hơn số sau)*
   - C. `< (phần tử (j)) = (phần tử ((j) + (1))) >`
   - D. `< (j) > ((j) + (1)) >`

8. **Trong vòng lặp trong của Bubble Sort, biến chỉ số `j` chỉ được chạy đến:**
   - A. `kích thước của danh sách`
   - B. `(kích thước của danh sách) - 1` *(Đáp án đúng: để `j + 1` không bị vượt biên)*
   - C. `(kích thước của danh sách) + 1`
   - D. 1

9. **Nếu một danh sách có 5 phần tử đã được sắp xếp tăng dần, ta muốn sắp xếp giảm dần thì chỉ cần:**
   - A. Đổi dấu so sánh từ `>` thành `<` trong điều kiện hoán đổi *(Đáp án đúng)*
   - B. Xóa danh sách và nhập lại
   - C. Nhân tất cả các số với -1
   - D. Bỏ biến trung gian `tam`

10. **Giả sử danh sách đang là `[8, 2, 5]`. Sau 1 lần hoán đổi đầu tiên giữa $j=1$ và $j=2$, danh sách trở thành:**
    - A. `[2, 8, 5]` *(Đáp án đúng: số 8 và số 2 đổi chỗ cho nhau)*
    - B. `[8, 5, 2]`
    - C. `[2, 5, 8]`
    - D. `[5, 2, 8]`
