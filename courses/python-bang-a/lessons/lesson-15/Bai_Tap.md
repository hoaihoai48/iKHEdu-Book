# Hệ thống bài tập thực hành — bài 15: Tách từ và mã hóa thay thế

---

## Bảng ma trận bài tập (12 bài tập phân tầng cơ bản → thử thách)

| STT | Mã bài | Tên bài toán | Cấp độ | Ràng buộc dữ liệu | Mục tiêu rèn luyện |
|:---:|:---:|---|:---:|---|---|
| 01 | `PYA-L15-P01` | Đếm số từ trong câu | `Cơ bản` | Dòng văn bản $\le 1000$ ký tự | Sử dụng `len(s.split())` |
| 02 | `PYA-L15-P02` | Từ đầu tiên & từ cuối cùng | `Cơ bản` | Câu có ít nhất 1 từ | Truy xuất `ds[0]` và `ds[-1]` |
| 03 | `PYA-L15-P03` | Mã ASCII của ký tự | `Cơ bản` | 1 ký tự duy nhất | Hàm `ord(ch)` |
| 04 | `PYA-L15-P04` | Ký tự kế tiếp trong bảng chữ cái | `Cơ bản` | Ký tự từ 'A' đến 'y' | `chr(ord(ch) + 1)` |
| 05 | `PYA-L15-P05` | Tìm từ dài nhất trong câu | `Cơ bản` | Dòng văn bản $\le 1000$ ký tự | So sánh độ dài các từ sau `split()` |
| 06 | `PYA-L15-P06` | Chuẩn hóa khoảng trắng | `Luyện tập` | Dòng văn bản có nhiều dấu cách | `" ".join(s.split())` |
| 07 | `PYA-L15-P07` | Viết hoa chữ cái đầu mỗi từ (title case) | `Luyện tập` | Dòng văn bản $\le 1000$ ký tự | Chuẩn hóa họ và tên người |
| 08 | `PYA-L15-P08` | Đảo ngược từng từ trong câu | `Luyện tập` | Dòng văn bản $\le 1000$ ký tự | Đảo ngược từng từ giữ nguyên thứ tự từ |
| 09 | `PYA-L15-P09` | Mật mã Caesar dịch chuyển K | `Luyện tập` | Chuỗi in hoa, $1 \le K \le 25$ | Thuật toán mã hóa Caesar cổ điển |
| 10 | `PYA-L15-P10` | Giải mã mật thư Caesar | `Luyện tập` | Chuỗi in hoa, $1 \le K \le 25$ | Dịch ngược $K$ vị trí để tìm thông điệp gốc |
| 11 | `PYA-L15-P11` | Từ xuất hiện nhiều nhất trong đoạn | `Vận dụng` | Văn bản $\le 10^4$ ký tự | Đếm tần suất xuất hiện của từng từ |
| 12 | `PYA-L15-P12` | Mật mã thay thế hoán vị (anagram) | `Thử thách` | Hai chuỗi $\le 10^5$ ký tự | Kiểm tra 2 từ cấu tạo từ cùng tập ký tự |

---

### Bài 1 (Cơ bản): Đếm số từ trong câu (`PYA-L15-P01`)

* **Yêu cầu:** Nhập một dòng văn bản $S$ có thể chứa nhiều khoảng trắng thừa ở đầu, cuối hoặc giữa các từ. Hãy đếm xem câu văn đó có bao nhiêu từ.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Số lượng từ trong câu.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `  Chuc   mung nam   moi   ` | `4` | Có 4 từ: 'Chuc', 'mung', 'nam', 'moi'. |

---

### Bài 2 (Cơ bản): Từ đầu tiên & từ cuối cùng (`PYA-L15-P02`)

* **Yêu cầu:** Cho một câu văn $S$. Hãy in ra từ đầu tiên và từ cuối cùng của câu văn đó trên 2 dòng riêng biệt.
* **Input:** Một dòng văn bản có ít nhất 1 từ.
* **Output:** Dòng 1 in từ đầu tiên, dòng 2 in từ cuối cùng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `Hoc lap trinh Python cuc vui` | `Hoc`<br>`vui` |

---

### Bài 3 (Cơ bản): Mã ASCII của ký tự (`PYA-L15-P03`)

* **Yêu cầu:** Nhập một ký tự bất kỳ từ bàn phím. Hãy in ra mã số ASCII của ký tự đó.
* **Input:** Một ký tự duy nhất $C$.
* **Output:** Một số nguyên là mã ASCII.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `A` | `65` |
  | `a` | `97` |

---

### Bài 4 (Cơ bản): Ký tự kế tiếp trong bảng chữ cái (`PYA-L15-P04`)

* **Yêu cầu:** Nhập vào một chữ cái in hoa từ `'A'` đến `'Y'`. Hãy in ra chữ cái đứng ngay liền sau nó trong bảng chữ cái tiếng Anh.
* **Input:** Một ký tự in hoa $C \in ['A' \dots 'Y']$.
* **Output:** Chữ cái liền sau.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `C` | `D` |
* **Gợi ý:** `chr(ord(c) + 1)`.

---

### Bài 5 (Cơ bản): Tìm từ dài nhất trong câu (`PYA-L15-P05`)

* **Yêu cầu:** Cho một câu văn $S$. Hãy tìm và in ra từ có độ dài dài nhất trong câu. Nếu có nhiều từ cùng độ dài dài nhất, in ra từ đầu tiên xuất hiện.
* **Input:** Một dòng văn bản $S$.
* **Output:** Từ dài nhất tìm được.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Hoc lap trinh rat thu vi` | `trinh` | Từ 'trinh' có 5 chữ cái (dài nhất). |

---

### Bài 6 (Luyện tập): Chuẩn hóa khoảng trắng (`PYA-L15-P06`)

* **Bối cảnh:** Khi đánh máy, một bạn học sinh lỡ tay bấm rất nhiều dấu cách thừa giữa các từ và ở hai đầu câu văn.
* **Yêu cầu:** Cho chuỗi văn bản $S$. Hãy chuẩn hóa câu văn sao cho: không còn khoảng trắng ở đầu và cuối câu, giữa mỗi từ chỉ có duy nhất **một dấu cách**.
* **Input:** Một dòng văn bản $S$ ($1 \le |S| \le 1000$).
* **Output:** Câu văn chuẩn hóa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `   Python     rat   la     tuyet      ` | `Python rat la tuyet` |
* **Gợi ý:** Dùng `" ".join(s.split())`.

---

### Bài 7 (Luyện tập): Viết hoa chữ cái đầu mỗi từ (title case) (`PYA-L15-P07`)

* **Yêu cầu:** Nhập họ và tên của một bạn học sinh viết chưa đúng quy tắc (ví dụ: `nguyen van an`). Hãy chuẩn hóa họ tên bằng cách viết hoa chữ cái đầu tiên của mỗi từ và viết thường các chữ cái còn lại.
* **Input:** Một chuỗi họ tên.
* **Output:** Họ tên sau khi chuẩn hóa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `nguyen van an` | `Nguyen Van An` |

---

### Bài 8 (Luyện tập): Đảo ngược từng từ trong câu (`PYA-L15-P08`)

* **Yêu cầu:** Cho một câu văn. Hãy đảo ngược thứ tự các chữ cái trong từng từ một, nhưng giữ nguyên vị trí của các từ trong câu.
* **Input:** Một dòng văn bản.
* **Output:** Câu văn mới với từng từ bị đảo ngược.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `Toi yeu Viet Nam` | `ioT uey teiV maN` | 'Toi' -> 'ioT', 'yeu' -> 'uey'... |

---

### Bài 9 (Luyện tập): Mật mã Caesar dịch chuyển K (`PYA-L15-P09`)
*(Bài toán kinh điển Tin học trẻ Bảng A)*

* **Bối cảnh:** Hoàng đế Caesar mã hóa bức thư gồm các chữ cái in hoa (`'A'` đến `'Z'`) bằng cách dịch chuyển mỗi chữ cái sang phải $K$ bước theo vòng tròn 26 chữ cái ($A \to B \dots Z \to A$).
* **Yêu cầu:** Cho chuỗi $S$ chỉ gồm các chữ cái in hoa và số nguyên $K$ ($1 \le K \le 25$). Hãy in ra bản mật mã sau khi mã hóa.
* **Input:** Dòng 1 chứa chuỗi $S$. Dòng 2 chứa số $K$.
* **Output:** Chuỗi sau khi mã hóa.
* **Ví dụ mẫu:**
  | Input | Output | Giải thích |
  |---|---|---|
  | `ABCXYZ`<br>`3` | `DEFABC` | 'A'->'D', 'B'->'E', 'X'->'A', 'Y'->'B', 'Z'->'C'. |
* **Công thức toán học:** `chr((ord(ch) - ord('A') + k) % 26 + ord('A'))`.

---

### Bài 10 (Luyện tập): Giải mã mật thư Caesar (`PYA-L15-P10`)

* **Yêu cầu:** Cho một bản mật mã $S$ (chỉ gồm các chữ cái in hoa) đã bị mã hóa Caesar với bước nhảy $K$. Hãy giải mã để tìm lại thông điệp ban đầu.
* **Input:** Dòng 1 chứa bản mật mã $S$. Dòng 2 chứa số nguyên $K$ ($1 \le K \le 25$).
* **Output:** Thông điệp ban đầu trước khi mã hóa.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `DEFABC`<br>`3` | `ABCXYZ` |

---

### Bài 11 (Vận dụng): Từ xuất hiện nhiều nhất trong đoạn (`PYA-L15-P11`)

* **Yêu cầu:** Cho một đoạn văn bản chỉ gồm các từ cách nhau bởi khoảng trắng. Hãy tìm xem từ nào xuất hiện nhiều lần nhất trong đoạn văn đó và xuất hiện bao nhiêu lần. Dữ liệu đảm bảo chỉ có 1 từ xuất hiện nhiều nhất.
* **Input:** Một đoạn văn bản $S$ gồm các chữ cái viết thường.
* **Output:** Từ xuất hiện nhiều nhất và số lần xuất hiện, cách nhau một khoảng trắng.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `cam quyt mit dua cam xoai cam dua` | `cam 3` |

---

### Bài 12 (Thử thách): Mật mã thay thế hoán vị (anagram) (`PYA-L15-P12`)
*(Đề thi Tin học trẻ Bảng A)*

* **Bối cảnh:** Hai từ được gọi là "Anagram" (hoán vị ký tự của nhau) nếu chúng có thể tạo thành từ nhau bằng cách xáo trộn lại thứ tự các chữ cái (ví dụ: `silent` và `listen`, `heart` và `earth`).
* **Yêu cầu:** Cho 2 từ $S_1$ và $S_2$. Kiểm tra xem chúng có phải là Anagram của nhau không. In `YES` nếu đúng, ngược lại in `NO`.
* **Input:** Hai dòng, mỗi dòng chứa một từ viết thường ($1 \le |S_1|, |S_2| \le 10^5$).
* **Output:** `YES` hoặc `NO`.
* **Ví dụ mẫu:**
  | Input | Output |
  |---|---|
  | `listen`<br>`silent` | `YES` |
  | `hello`<br>`world` | `NO` |
* **Gợi ý:** Kiểm tra nếu `sorted(s1) == sorted(s2)`.
