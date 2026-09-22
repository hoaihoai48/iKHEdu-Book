# Bài 16: DUYỆT CHUỖI, BIẾN ĐỔI KÝ TỰ VÀ TÁCH TỪ

## 1. Kỹ thuật xử lý chuỗi và biến đổi văn bản

Trong bài 15, chúng ta đã nắm vững các khối lệnh cơ bản và kỹ thuật trích xuất chuỗi con. Trong bài học này, chúng ta sẽ bước vào những kỹ thuật xử lý văn bản đỉnh cao thường xuyên xuất hiện trong các đề thi lập trình:

- **Duyệt qua từng ký tự của chuỗi:** Đếm tần số xuất hiện của một chữ cái, đếm số lượng chữ số, nguyên âm, phụ âm.

- **Biến đổi chuỗi (String Transformation):** Thay thế một ký tự này bằng ký tự khác, loại bỏ ký tự rác, chuẩn hóa khoảng trắng.

- **Tách từ (Split Words):** Phân rã một câu văn hoàn chỉnh thành từng từ độc lập nạp vào Danh sách (List).

---

## 2. Kỹ thuật duyệt chuỗi và đếm ký tự

Để kiểm tra xem một chữ cái (ví dụ chữ `'a'`) xuất hiện bao nhiêu lần trong câu văn $S$:

1. Khởi tạo biến đếm: `đặt [dem v] thành (0)`.

2. Khởi tạo chỉ số: `đặt [i v] thành (1)`.

3. Lặp đúng `(độ dài của (S))` lần:

   - Nếu ký tự thứ $i$ đúng là chữ `'a'` (`< (ký tự (i) của (S)) = [a] >`): Tăng `dem` lên 1.
   - Luôn tăng `i` lên 1 để kiểm tra ký tự tiếp theo.

4. Sau vòng lặp, `dem` chứa số lần xuất hiện của chữ `'a'`.

---

## 3. Thuật toán tách từ (Split) nạp vào danh sách

Trong Scratch, không có sẵn một khối đơn lẻ để tách từ tự động. Đây là bài toán kiểm tra năng lực tư duy thuật toán tuyệt vời của học sinh.

### 3.1. Bản chất tư duy của thuật toán tách từ:

- Một câu văn gồm các từ được ngăn cách nhau bởi **dấu cách (khoảng trắng `[ ]`)**.

- Ta dùng một chiếc hộp tạm thời mang tên **`tu_tam`** (chuỗi ký tự rỗng ban đầu).

- Duyệt qua từng ký tự từ đầu đến cuối câu:

  - Nếu ký tự đang xét **không phải là dấu cách**: Ta ghép ký tự đó vào đuôi của `tu_tam` (`kết hợp (tu_tam) (ký tự hiện tại)`).
  - Nếu gặp **dấu cách**: Điều đó báo hiệu một từ vừa hoàn thành! Nếu `tu_tam` không rỗng, ta lập tức **đưa `tu_tam` vào Danh sách từ**, sau đó **làm rỗng `tu_tam`** để sẵn sàng đón nhận từ tiếp theo!

- **Bước chốt hạ quan trọng:** Sau khi duyệt hết câu, từ cuối cùng thường không có dấu cách phía sau để kích hoạt, do đó ta phải kiểm tra và đưa `tu_tam` cuối cùng vào danh sách!

![Thuật toán tách từ nạp vào danh sách](assets/rendered_blocks/l16_split_words_vi.png)

---

## 4. Bảng mô phỏng tách câu `"DI HOC"` vào danh sách (Dry run)

Câu ban đầu: $S = \text{"DI HOC"}$. Độ dài $= 6$. Ký tự tại các vị trí:

- Vị trí 1: `'D'`

- Vị trí 2: `'I'`

- Vị trí 3: `' '` *(dấu cách)*

- Vị trí 4: `'H'`

- Vị trí 5: `'O'`

- Vị trí 6: `'C'`

| Vòng lặp | Chỉ số `i` | Ký tự `S[i]` | Có phải dấu cách không? | Biến `tu_tam` sau bước | Danh sách `[Danh sách Từ]` |
|:---:|:---:|:---:|:---:|:---:|:---:|
| *Bắt đầu* | — | — | — | `""` | `[]` *(Rỗng)* |
| **1** | $i = 1$ | `'D'` | Không | `"D"` | `[]` |
| **2** | $i = 2$ | `'I'` | Không | `"DI"` | `[]` |
| **3** | $i = 3$ | `' '` | **CÓ** (Gặp dấu cách!) | `""` *(Làm rỗng)* | `["DI"]` *(Đã nạp từ thứ nhất)* |
| **4** | $i = 4$ | `'H'` | Không | `"H"` | `["DI"]` |
| **5** | $i = 5$ | `'O'` | Không | `"HO"` | `["DI"]` |
| **6** | $i = 6$ | `'C'` | Không | `"HOC"` | `["DI"]` |
| **Sau lặp** | — | — | *Xử lý từ cuối:* `tu_tam = "HOC"` | `""` | `["DI", "HOC"]` *(Hoàn thành!)* |

$\implies$ Kết quả: `[Danh sách Từ]` có đúng 2 phần tử là `"DI"` và `"HOC"`.

---

## 5. Các bẫy lỗi thường gặp (Bug Traps)

> **Bẫy 1: Bỏ quên từ cuối cùng của câu văn (The Last Word Bug)**
> - *Hiện tượng:* Người dùng nhập câu văn bình thường mà không gõ phím cách ở cuối câu (ví dụ: `"EM YEU SCRATCH"`).
> - *Hậu quả:* Vòng lặp duyệt hết ký tự cuối cùng `'H'`, nhưng vì không gặp dấu cách nên kịch bản không thêm vào danh sách. Khi kết thúc chương trình, từ `"SCRATCH"` vẫn nằm kẹt trong biến `tu_tam`!
> - *Khắc phục:* Luôn luôn bổ sung khối kiểm tra ngay sau vòng lặp:
>   `nếu < (độ dài của (tu_tam)) > (0) > thì thêm (tu_tam) vào [Danh sách Từ v]`.

> **Bẫy 2: Lỗi nhiều dấu cách liên tiếp nhau (Double Spaces Trap)**
> - *Hiện tượng:* Giữa hai từ người dùng bấm 2 hoặc 3 dấu cách liên tiếp (ví dụ `"HOC   TIN"`).
> - *Hậu quả:* Nếu không kiểm tra `< (độ dài của (tu_tam)) > 0 >`, các từ rỗng (khoảng trắng rác) sẽ bị nạp liên tục vào danh sách!
> - *Khắc phục:* Chỉ thêm vào danh sách khi biến `tu_tam` thực sự có chứa chữ cái (`độ dài > 0`).

> **Bẫy 3: Phân biệt chữ hoa và chữ thường trong Scratch**
> - *Hiện tượng:* Trong Scratch, khối so sánh `< [A] = [a] >` mặc định coi là **BẰNG NHAU** (Scratch không phân biệt hoa - thường trong phép so sánh bằng).
> - *Hậu quả:* Nếu đề bài yêu cầu đếm riêng chữ cái viết hoa và chữ cái viết thường, phép so sánh bằng thông thường sẽ đếm gộp cả hai.
> - *Khắc phục sư phạm:* Khi cần phân biệt tuyệt đối hoa - thường, giáo viên hướng dẫn học sinh kỹ thuật so khớp qua trang phục nhân vật (Costume Name) hoặc bảng mã quy ước.

---

## 6. Bộ câu hỏi trắc nghiệm củng cố (Concept Quizzes)

1. **Vòng lặp duyệt qua toàn bộ một chuỗi ký tự $S$ cần chạy đúng bao nhiêu lần?**
   - A. `(độ dài của (S)) - 1` lần
   - B. `độ dài của (S)` lần *(Đáp án đúng: duyệt từ ký tự 1 đến hết)*
   - C. `(độ dài của (S)) + 1` lần
   - D. 10 lần

2. **Dấu hiệu cơ bản nhất để nhận biết sự kết thúc của một từ trong câu văn thông thường là:**
   - A. Dấu chấm phẩy
   - B. Dấu cách (khoảng trắng) *(Đáp án đúng)*
   - C. Chữ cái 'Z'
   - D. Chữ số 0

3. **Trong thuật toán tách từ, biến `tu_tam` có vai trò gì?**
   - A. Đếm số lượng từ trong câu
   - B. Tích lũy ghép các chữ cái của một từ đang đọc dở *(Đáp án đúng)*
   - C. Lưu độ dài của câu văn
   - D. Xóa dấu cách thừa

4. **Khi gặp một dấu cách, sau khi đã đưa `tu_tam` vào danh sách, ta bắt buộc phải:**
   - A. Tăng `tu_tam` lên 1
   - B. Làm rỗng biến `tu_tam` để chuẩn bị đón từ mới *(Đáp án đúng)*
   - C. Dừng vòng lặp ngay lập tức
   - D. Đặt `tu_tam` thành dấu cách

5. **Vì sao phải có khối lệnh kiểm tra và thêm `tu_tam` vào danh sách ở ngay sau vòng lặp duyệt chuỗi?**
   - A. Để câu văn dài hơn
   - B. Để tránh bỏ sót từ cuối cùng của câu khi không có dấu cách ở đuôi *(Đáp án đúng)*
   - C. Để đảo ngược câu văn
   - D. Để xóa danh sách

6. **Trong Scratch, biểu thức điều kiện `< [M] = [m] >` sẽ trả về giá trị:**
   - A. SAI
   - B. ĐÚNG *(Đáp án đúng: Scratch mặc định không phân biệt hoa thường khi so sánh chuỗi)*
   - C. Báo lỗi cú pháp
   - D. Không xác định

7. **Giả sử $S = \text{"A B C"}$. Sau khi chạy qua thuật toán tách từ chuẩn, danh sách sẽ có bao nhiêu phần tử?**
   - A. 1
   - B. 2
   - C. 3 *(Đáp án đúng: `"A"`, `"B"`, `"C"`)*
   - D. 5

8. **Để đếm xem câu văn có bao nhiêu dấu cách, ta làm thế nào?**
   - A. Cho biến đếm tăng 1 mỗi khi gặp `< (ký tự (i) của (S)) = [ ] >` *(Đáp án đúng)*
   - B. Lấy `độ dài của (S)` chia đôi
   - C. Dùng khối `kích thước của danh sách`
   - D. Không thể đếm được trong Scratch

9. **Nếu giữa hai từ có 3 dấu cách liên tiếp, điều kiện nào giúp ta không thêm các từ rỗng vào danh sách?**
   - A. `< (i) > (1) >`
   - B. `< (độ dài của (tu_tam)) > (0) >` *(Đáp án đúng: chỉ thêm khi từ tạm có ký tự)*
   - C. `< (tu_tam) = [ ] >`
   - D. `< (độ dài của (S)) > (0) >`

10. **Kỹ thuật ghép từng ký tự vào biến kết quả `chuoi_moi` bằng lệnh `đặt [chuoi_moi] thành (kết hợp (chuoi_moi) (ký tự))` được gọi là:**
    - A. Tích lũy chuỗi (String Accumulation) *(Đáp án đúng)*
    - B. Xóa chuỗi
    - C. Cắt lát chuỗi
    - D. Sắp xếp chuỗi
