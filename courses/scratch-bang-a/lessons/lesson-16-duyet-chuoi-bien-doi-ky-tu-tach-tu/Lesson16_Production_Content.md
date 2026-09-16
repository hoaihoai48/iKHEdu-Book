# BÀI 16: DUYỆT CHUỖI, BIẾN ĐỔI KÝ TỰ VÀ TÁCH TỪ

**Khóa học:** Scratch — Tư duy Khối lệnh, Đồ họa & Thuật toán Thi đấu (Bảng A)  
**Mã bài học:** `SCA-L16` | **Chương 6:** Xử Lý Chuỗi Ký Tự  
**Thời lượng khuyến nghị:** 2 – 3 buổi học (90 phút/buổi)  
**Ánh xạ chuẩn:** Tương đương Bài 14, 15 của Python Bảng A (`courses/python-bang-a/problems/pya_l14_*`, `pya_l15_*`)  

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)

Sau khi hoàn thành bài học này, học sinh sẽ đạt được các chuẩn năng lực:
- **`LO-01` (Duyệt tuần tự từng ký tự trong chuỗi):** Dùng vòng lặp với biến đếm $i$ chạy từ $1$ đến `độ dài của (chuỗi)` để xét từng ký tự `ký tự (i) của (chuỗi)`.
- **`LO-02` (Đếm tần số xuất hiện của một ký tự):** Đếm xem ký tự $C$ (ví dụ chữ `'a'`) xuất hiện bao nhiêu lần trong câu văn.
- **`LO-03` (Kỹ thuật Thay thế & Lọc ký tự):** Xây dựng chuỗi kết quả mới: duyệt từng ký tự của chuỗi gốc, nếu là ký tự cần đổi thì ghép ký tự mới, ngược lại ghép ký tự cũ.
- **`LO-04` (Kỹ thuật Tách từ theo dấu cách - Split thủ công):** Vì Scratch không có hàm `.split()` như Python, học sinh tự lập trình thuật toán:
  - Tích lũy các ký tự vào biến `tu_hien_tai`.
  - Khi gặp ký tự dấu cách `' '` $\implies$ Lưu `tu_hien_tai` vào danh sách các từ rồi xóa rỗng để đón từ tiếp theo.
- **`LO-05` (Bài toán kinh điển):** Đếm số từ trong câu, nén chuỗi ký tự (RLE), mã hóa mật thư dịch chuyển Caesar, đảo ngược thứ tự các từ.

---

## 2. Thuật Toán Đếm Ký Tự Trong Chuỗi

Đếm số lần chữ cái `'a'` xuất hiện trong chuỗi $S$:

```text
đặt [dem v] thành (0)
đặt [i v] thành (1)
lặp lại (độ dài của (S)) lần
    nếu < (ký tự (i) của (S)) = [a] > thì
        thay đổi [dem v] một lượng (1)
    thay đổi [i v] một lượng (1)
nói (dem)
```

---

## 3. Thuật Toán Tách Từ (Split) Nạp Vào Danh Sách

Bài toán: Cho chuỗi $S = \text{"HOC LAP TRINH"}$. Tách từng từ và thêm vào `[Danh sách Từ]`:

```text
xóa tất cả của [Danh sách Từ v]
đặt [tu_tam v] thành []
đặt [i v] thành (1)

lặp lại (độ dài của (S)) lần
    nếu < (ký tự (i) của (S)) = [ ] > thì
        nếu < (độ dài của (tu_tam)) > (0) > thì
            thêm (tu_tam) vào [Danh sách Từ v]
            đặt [tu_tam v] thành []
    nếu không thì
        đặt [tu_tam v] thành (kết hợp (tu_tam) (ký tự (i) của (S)))
    thay đổi [i v] một lượng (1)

// Đừng quên từ cuối cùng sau khi hết chuỗi!
nếu < (độ dài của (tu_tam)) > (0) > thì
    thêm (tu_tam) vào [Danh sách Từ v]
```

---

## 4. Tử Huyệt & Các Bẫy Lỗi Thường Gặp (Bug Traps)

> **Bẫy 1: Bỏ quên từ cuối cùng của câu**
> - *Hiện tượng:* Người dùng không gõ dấu cách ở cuối câu văn.
> - *Hậu quả:* Vòng lặp kết thúc mà từ cuối cùng vẫn nằm kẹt trong biến `tu_tam`, không được thêm vào danh sách!
> - *Khắc phục:* Luôn thêm đoạn kiểm tra `nếu độ dài của tu_tam > 0 thì thêm vào danh sách` ở ngay sau vòng lặp.

> **Bẫy 2: Phân biệt chữ hoa và chữ thường trong so sánh chuỗi**
> - *Lưu ý đặc biệt trong Scratch:* Khối so sánh bằng `< [A] = [a] >` trong Scratch mặc định **KHÔNG phân biệt hoa thường** (đều coi là bằng nhau).
> - Để xử lý thi đấu phân biệt hoa thường, học sinh được giáo viên hướng dẫn bảng mã ký tự hoặc kiểm tra qua trang phục nhân vật.

---

## 5. Bộ Câu Hỏi Trắc Nghiệm Củng Cố (Concept Quizzes)

1. **Vòng lặp duyệt qua toàn bộ chuỗi ký tự chạy bao nhiêu lần?**
   - A. `độ dài của (chuỗi)` lần *(Đáp án đúng)*
   - B. 10 lần
   - C. 100 lần
   - D. 1 lần

2. **Khi duyệt chuỗi bằng biến đếm $i$, ký tự hiện tại đang xét được lấy bằng:**
   - A. `ký tự (i) của (chuỗi)` *(Đáp án đúng)*
   - B. `phần tử (i) của (chuỗi)`
   - C. `độ dài của (i)`
   - D. `i`

3. **Thuật toán tách từ nhận diện ranh giới giữa các từ nhờ vào:**
   - A. Ký tự dấu cách `' '` *(Đáp án đúng)*
   - B. Chữ số 0
   - C. Dấu chấm phẩy
   - D. Dấu gạch chéo

4. **Tại sao cần khối thêm `tu_tam` sau khi kết thúc vòng lặp tách từ?**
   - A. Để nạp nốt từ cuối cùng của câu (khi cuối câu không có dấu cách) *(Đáp án đúng)*
   - B. Để dọn sạch bộ nhớ
   - C. Bắt buộc của Scratch
   - D. Để in ra màn hình

5. **Chuỗi `"AAABBC"` sau khi nén độ dài RLE sẽ trở thành:**
   - A. `"3A2B1C"` *(Đáp án đúng)*
   - B. `"ABC"`
   - C. `"6"`
   - D. `"AAABB"`

6. **Số lượng từ trong câu `"Chuc mung nam moi"` là:**
   - A. 4 từ *(Đáp án đúng)*
   - B. 3 từ
   - C. 16 từ
   - D. 5 từ

7. **Trong Scratch, khối `< [Cat] = [cat] >` trả về giá trị gì?**
   - A. Đúng (True) *(Scratch không phân biệt hoa thường trong khối so sánh)* *(Đáp án đúng)*
   - B. Sai (False)
   - C. Lỗi
   - D. Không xác định

8. **Để xóa một ký tự khỏi chuỗi, thuật toán sẽ:**
   - A. Bỏ qua ký tự đó, không ghép nó vào chuỗi kết quả mới *(Đáp án đúng)*
   - B. Dùng khối xóa ký tự
   - C. Nhấn phím Backspace
   - D. Thay bằng dấu cách

9. **Mã hóa Caesar dịch chuyển ký tự sang phải $K$ vị trí là kỹ thuật dùng trong:**
   - A. Mật mã học cổ điển *(Đáp án đúng)*
   - B. Nén ảnh
   - C. Tính toán hình học
   - D. Vẽ tranh bằng bút vẽ

10. **Biến tích lũy từ `tu_tam` sau khi đã đưa vào danh sách cần phải:**
    - A. Đặt lại thành chuỗi rỗng `[]` *(Đáp án đúng)*
    - B. Giữ nguyên
    - C. Đặt thành số 0
    - D. Đặt thành dấu cách
