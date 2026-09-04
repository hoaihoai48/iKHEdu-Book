# Bài 13: Chỉ số và cắt lát chuỗi

## 1. Tóm tắt kiến thức trọng tâm
- Chuỗi ký tự (String) đánh chỉ số bắt đầu từ **0**.
  - Ký tự đầu tiên: `s[0]`.
  - Ký tự cuối cùng: `s[-1]`.
  - Độ dài chuỗi: `len(s)`.
- **Cắt lát chuỗi (Slicing) `s[start:stop]`:** Lấy từ `start` đến `stop - 1`.
  - Lấy $K$ ký tự đầu: `s[:K]`.
  - Lấy từ vị trí $K$ đến hết: `s[K:]`.
  - **Đảo ngược chuỗi tức thì:** `s[::-1]`.
- Chuỗi trong Python là **bất biến (Immutable)**: Không thể gán sửa trực tiếp `s[0] = 'X'`.

## 2. Concept quiz: 14 câu trắc nghiệm bắt bẫy củng cố khái niệm

#### Câu 1: Ký tự đầu tiên của chuỗi `s = "VIETNAM"` có chỉ số index là bao nhiêu?
- **A.** 1
- **B.** **[Đáp án đúng]** 0
- **C.** -1
- **D.** Không có chỉ số
- > *Giải thích:* Trong Python và khoa học máy tính, chỉ số chuỗi luôn bắt đầu từ 0.

#### Câu 2: Biểu thức `s[-1]` dùng để làm gì?
- **A.** Lấy ký tự đầu tiên
- **B.** Xóa một ký tự
- **C.** **[Đáp án đúng]** Lấy ký tự cuối cùng của chuỗi
- **D.** Đếm số ký tự
- > *Giải thích:* Chỉ số âm đếm ngược từ phải sang trái, `-1` là phần tử cuối cùng.

#### Câu 3: Cho chuỗi `s = "TIN HOC"`. Hàm `len(s)` trả về kết quả là:
- **A.** 6
- **B.** **[Đáp án đúng]** 7
- **C.** 8
- **D.** 5
- > *Giải thích:* Dấu cách (khoảng trắng) cũng được tính là một ký tự: 'T','I','N',' ','H','O','C' = 7.

#### Câu 4: Cho `s = "PYTHON"`. Lệnh `print(s[6])` sẽ dẫn đến điều gì?
- **A.** In ra chữ cái cuối cùng
- **B.** In ra khoảng trắng
- **C.** **[Đáp án đúng]** Báo lỗi `IndexError: string index out of range`
- **D.** In ra số 6
- > *Giải thích:* Độ dài chuỗi là 6 thì chỉ số lớn nhất chỉ là 5. Gọi `s[6]` là vượt quá giới hạn.

#### Câu 5: Cho chuỗi `s = "HELLO"`. Kết quả của `s[1:4]` là gì?
- **A.** `"HEL"`
- **B.** `"HELL"`
- **C.** **[Đáp án đúng]** `"ELL"`
- **D.** `"ELLO"`
- > *Giải thích:* Lấy từ index 1 (`'E'`), 2 (`'L'`), 3 (`'L'`). Không lấy index 4.

#### Câu 6: Cú pháp nào sau đây giúp đảo ngược toàn bộ chuỗi `s` trong Python?
- **A.** `s.reverse()`
- **B.** `s[0:-1]`
- **C.** **[Đáp án đúng]** `s[::-1]`
- **D.** `s[1:len(s)]`
- > *Giải thích:* `s[::-1]` là cú pháp slicing với bước nhảy `-1` lùi từ cuối về đầu.

#### Câu 7: Chuỗi trong Python có cho phép gán đè ký tự trực tiếp như `s[0] = 'A'` không?
- **A.** Có, thay đổi bình thường
- **B.** **[Đáp án đúng]** Không, chuỗi trong Python là kiểu bất biến (Immutable), lệnh này báo lỗi `TypeError`
- **C.** Chỉ đổi được nếu chuỗi viết hoa
- **D.** Tự động thêm vào cuối
- > *Giải thích:* Chuỗi là đối tượng bất biến (Immutable) trong Python, không thể gán lại từng ký tự qua index.

#### Câu 8: Cho `s = "ABCDEF"`. Lệnh `s[::2]` sẽ in ra:
- **A.** `"ABC"`
- **B.** `"DEF"`
- **C.** **[Đáp án đúng]** `"ACE"`
- **D.** `"BDF"`
- > *Giải thích:* Bước nhảy `step = 2`: lấy vị trí 0 (`'A'`), vị trí 2 (`'C'`), vị trí 4 (`'E'`).

#### Câu 9: Cho `s = "KHOAHOC"`. Biểu thức `s[:4]` tương đương với:
- **A.** `s[0:4]`
- **B.** **[Đáp án đúng]** Lấy 4 ký tự đầu tiên (`"KHOA"`)
- **C.** Cả A và B đều đúng
- **D.** `s[1:4]`
- > *Giải thích:* Khuyết `start` mặc định là từ đầu (index 0).

#### Câu 10: Cho `s = "LAPTRINH"`. Biểu thức `s[3:]` cho kết quả:
- **A.** `"LAP"`
- **B.** **[Đáp án đúng]** `"TRINH"`
- **C.** `"PTRINH"`
- **D.** `"TRIN"`
- > *Giải thích:* Bắt đầu từ index 3 (chữ `'T'`) và lấy đến hết chuỗi.

#### Câu 11: Cho đoạn code sau:
```python
s = "12345"
print(s[1] + s[2])
```
Kết quả in ra là gì?
- **A.** 5
- **B.** **[Đáp án đúng]** `"23"`
- **C.** 23 (số nguyên)
- **D.** Báo lỗi
- > *Giải thích:* `s` là chuỗi nên `s[1]` là `'2'` và `s[2]` là `'3'`. Phép cộng chuỗi nối thành `"23"`.

#### Câu 12: Biểu thức kiểm tra một từ `w` có phải là từ đối xứng (palindrome) hay không là:
- **A.** `w == w`
- **B.** `len(w) % 2 == 0`
- **C.** **[Đáp án đúng]** `w == w[::-1]`
- **D.** `w[0] == w[-1]`
- > *Giải thích:* Từ đối xứng khi đọc ngược lại giống hệt từ ban đầu.

#### Câu 13: Cho `s = "iKHEDU"`. Lệnh `s[-3:]` trả về:
- **A.** `"iKH"`
- **B.** **[Đáp án đúng]** `"EDU"`
- **C.** `"ED"`
- **D.** `"DU"`
- > *Giải thích:* Index -3 là chữ `'E'`, lấy đến hết chuỗi là `"EDU"`.

#### Câu 14: Biểu thức `s[:-1]` có tác dụng gì?
- **A.** Lấy ký tự cuối cùng
- **B.** **[Đáp án đúng]** Cắt bỏ đi ký tự cuối cùng của chuỗi (lấy từ đầu đến sát cuối)
- **C.** Đảo ngược chuỗi
- **D.** Báo lỗi cú pháp
- > *Giải thích:* Cắt từ đầu đến trước vị trí `-1`, tức là bỏ đi ký tự cuối cùng.
