# Hệ thống bài tập thực hành — bài 14: Duyệt chuỗi và biến đổi ký tự

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L14-P01` | In từng chữ cái xuống dòng | `Cơ bản` | Độ dài chuỗi $\le 100$ | Vòng lặp duyệt cơ bản `for ch in s` |
| 02 | `PYA-L14-P02` | Chuyển toàn bộ thành chữ hoa | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Sử dụng phương thức `s.upper()` |
| 03 | `PYA-L14-P03` | Đếm ký tự 'A' (cả hoa lẫn thường) | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Đếm với `ch.upper() == 'A'` |
| 04 | `PYA-L14-P04` | Đếm chữ cái in hoa & in thường | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Sử dụng `ch.isupper()` và `ch.islower()` |
| 05 | `PYA-L14-P05` | Tách riêng chữ số ra khỏi văn bản | `Cơ bản` | Độ dài chuỗi $\le 1000$ | Lọc các ký tự thỏa mãn `ch.isdigit()` |
| 06 | `PYA-L14-P06` | Tính tổng các chữ số trong chuỗi | `Luyện tập` | Độ dài chuỗi $\le 10^5$ | Chuyển `int(ch)` và cộng dồn |
| 07 | `PYA-L14-P07` | Đổi chữ hoa thành thường & ngược lại | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Đảo ngược trạng thái chữ (swap case) |
| 08 | `PYA-L14-P08` | Thay thế ký tự bí mật | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Sử dụng phương thức `s.replace()` |
| 09 | `PYA-L14-P09` | Xóa bỏ toàn bộ dấu cách | `Luyện tập` | Độ dài chuỗi $\le 10^5$ | Lọc bỏ `ch == " "` |
| 10 | `PYA-L14-P10` | Đếm số lượng nguyên âm | `Luyện tập` | Độ dài chuỗi $\le 1000$ | Đếm các chữ cái thuộc tập `u, e, o, a, i` |
| 11 | `PYA-L14-P11` | Nén chuỗi ký tự (run-length encoding) | `Vận dụng` | Độ dài chuỗi $\le 1000$ | Đếm số ký tự liên tiếp giống nhau `AAABBC \to A3B2C1` |
| 12 | `PYA-L14-P12` | Trích xuất số lớn nhất trong văn bản | `Thử thách` | Độ dài chuỗi $\le 1000$ | Gom các cụm chữ số liên tiếp thành số nguyên |

---

### Bài 1 (Cơ bản): In từng chữ cái xuống dòng (`PYA-L14-P01`)

* **Yêu cầu:** Nhập vào một từ $S$. Hãy in ra từng chữ cái của từ đó, mỗi chữ cái nằm trên một dòng riêng biệt.
* **Input:** Một chuỗi ký tự $S$ ($1 \le |S| \le 100$).
* **Output:** Mỗi ký tự trên một dòng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `CAT` | `C`<br>`A`<br>`T` |

---

### Bài 2 (Cơ bản): Chuyển toàn bộ thành chữ hoa (`PYA-L14-P02`)

* **Yêu cầu:** Nhập một dòng văn bản $S$. Hãy chuyển tất cả các chữ cái trong $S$ thành chữ in hoa và in ra màn hình.
* **Input:** Một dòng văn bản $S$.
* **Output:** Chuỗi sau khi đã in hoa toàn bộ.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `ikhedu vietnam` | `IKHEDU VIETNAM` |

---

### Bài 3 (Cơ bản): Đếm ký tự 'A' (cả hoa lẫn thường) (`PYA-L14-P03`)

* **Yêu cầu:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu chữ cái `'A'` hoặc `'a'` xuất hiện trong chuỗi $S$.
* **Input:** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng chữ cái 'A' hoặc 'a'.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `An va Ba hoc bai` | `4` | Gồm chữ 'A' (1 lần) và 'a' (3 lần trong 'va', 'Ba', 'bai'). |

---

### Bài 4 (Cơ bản): Đếm chữ cái in hoa & in thường (`PYA-L14-P04`)

* **Yêu cầu:** Cho một chuỗi $S$. Hãy đếm xem có bao nhiêu chữ cái in hoa và bao nhiêu chữ cái in thường trong chuỗi đó.
* **Input:** Chuỗi ký tự $S$.
* **Output:** Hai số nguyên cách nhau một khoảng trắng: số lượng chữ in hoa trước, số lượng chữ in thường sau.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Lap Trinh Python` | `3 11` | Chữ in hoa: 'L', 'T', 'P' (3 chữ). |

---

### Bài 5 (Cơ bản): Tách riêng chữ số ra khỏi văn bản (`PYA-L14-P05`)

* **Bối cảnh:** Trong một văn bản mật mã có các chữ số bị giấu lẫn vào giữa các chữ cái.
* **Yêu cầu:** Cho chuỗi $S$. Hãy nhặt ra toàn bộ các ký tự là chữ số ('0' - '9') và ghép chúng lại theo thứ tự ban đầu để in ra màn hình. Nếu không có chữ số nào, in ra `KHONG CO`.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Chuỗi các chữ số ghép lại, hoặc `KHONG CO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Toi sinh nam 2014 vao thang 08` | `201408` |

---

### Bài 6 (Luyện tập): Tính tổng các chữ số trong chuỗi (`PYA-L14-P06`)

* **Yêu cầu:** Cho một chuỗi văn bản $S$. Hãy tính tổng giá trị của tất cả các chữ số xuất hiện trong chuỗi đó.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 10^5$).
* **Output:** Một số nguyên duy nhất là tổng các chữ số.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `A1B2C3D4` | `10` | $1 + 2 + 3 + 4 = 10$. |

---

### Bài 7 (Luyện tập): Đổi chữ hoa thành thường & ngược lại (`PYA-L14-P07`)

* **Yêu cầu:** Cho chuỗi ký tự $S$. Hãy biến đổi chuỗi bằng quy tắc: chữ hoa đổi thành chữ thường, chữ thường đổi thành chữ hoa, các ký tự khác (số, dấu câu, khoảng trắng) giữ nguyên.
* **Input:** Một chuỗi văn bản $S$.
* **Output:** Chuỗi sau khi biến đổi.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Hello World 123` | `hELLO wORLD 123` |
* **Gợi ý:** Có thể dùng `s.swapcase()` hoặc duyệt từng ký tự.

---

### Bài 8 (Luyện tập): Thay thế ký tự bí mật (`PYA-L14-P08`)

* **Yêu cầu:** Nhập một chuỗi $S$. Hãy thay thế tất cả các ký tự khoảng trắng `" "` trong $S$ bằng dấu gạch dưới `"_"` và in ra kết quả.
* **Input:** Một chuỗi $S$.
* **Output:** Chuỗi sau khi thay thế.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `hoc lap trinh de vui` | `hoc_lap_trinh_de_vui` |
* **Gợi ý:** Dùng `s.replace(" ", "_")`.

---

### Bài 9 (Luyện tập): Xóa bỏ toàn bộ dấu cách (`PYA-L14-P09`)

* **Yêu cầu:** Cho một dòng văn bản $S$. Hãy xóa bỏ tất cả các ký tự khoảng trắng trong chuỗi để thu được một chuỗi viết liền hoàn toàn.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 10^5$).
* **Output:** Chuỗi viết liền không còn khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Tin Hoc Tre Bang A` | `TinHocTreBangA` |

---

### Bài 10 (Luyện tập): Đếm số lượng nguyên âm (`PYA-L14-P10`)

* **Bối cảnh:** Trong tiếng Anh, 5 chữ cái: `A, E, I, O, U` (cả hoa lẫn thường) được gọi là nguyên âm (vowels).
* **Yêu cầu:** Cho một chuỗi ký tự $S$. Hãy đếm xem có bao nhiêu ký tự nguyên âm trong chuỗi $S$.
* **Input:** Chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng nguyên âm.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `EDUCATION` | `5` | Các nguyên âm: E, U, A, I, O (có 5 nguyên âm). |

---

### Bài 11 (Vận dụng): Nén chuỗi ký tự (run-length encoding) (`PYA-L14-P11`)
*(Đề thi Tin học trẻ Bảng A)*

* **Bối cảnh:** Thuật toán nén chuỗi đơn giản thay thế một dãy các ký tự giống nhau liên tiếp bằng ký tự đó kèm theo số lần lặp lại.
  Ví dụ: `AAABBC` nén thành `A3B2C1`.
* **Yêu cầu:** Cho một chuỗi $S$ chỉ gồm các chữ cái in hoa. Hãy in ra dạng nén của chuỗi $S$.
* **Input:** Một chuỗi $S$ ($1 \le |S| \le 1000$).
* **Output:** Chuỗi sau khi nén.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `AAABBCCCC` | `A3B2C4` |

---

### Bài 12 (Thử thách): Trích xuất số lớn nhất trong văn bản (`PYA-L14-P12`)
*(Đề thi Tin học trẻ cấp Tỉnh/Thành phố Bảng A)*

* **Bối cảnh:** Trong một bài báo cáo có các con số nằm rải rác giữa các câu chữ. Một con số có thể có nhiều chữ số liên tiếp nhau.
* **Yêu cầu:** Cho chuỗi văn bản $S$. Hãy tìm và in ra giá trị của **con số nguyên lớn nhất** xuất hiện trong chuỗi đó. Dữ liệu đảm bảo có ít nhất 1 chữ số.
* **Input:** Một chuỗi văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số nguyên lớn nhất tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Lop 5A co 38 hoc sinh va 105 quyen sach` | `105` | Các con số xuất hiện là: 5, 38, 105. Số lớn nhất là 105. |
