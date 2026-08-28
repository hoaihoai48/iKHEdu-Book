# TÀI LIỆU GỐC — CHƯƠNG 8: XỬ LÝ XÂU KÝ TỰ CƠ BẢN (BASIC STRINGS)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật xử lý xâu ký tự trong C++ (`std::string`); làm chủ bảng mã ASCII, xâu đối xứng (Palindrome), đếm tần suất ký tự và tách từ |
| Kiến thức cần có | Biến, kiểu dữ liệu `char`, mảng một chiều, vòng lặp `for` |
| Phạm vi | Thao tác trên `string`, Bảng mã ASCII, Xâu Palindrome $\mathcal{O}(N)$, Đếm tần suất 26 chữ cái, Tách từ `stringstream` |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Sử dụng thành thạo các phương thức cơ bản của `std::string` (`size()`, `push_back()`, `substr()`, `find()`) — `LO-01`.
2. Chuyển đổi linh hoạt giữa ký tự và mã ASCII (`c - 'a'`, `c - '0'`, `toupper()`, `tolower()`) — `LO-02`.
3. Cài đặt thuật toán kiểm tra xâu đối xứng (Palindrome) trong $\mathcal{O}(N)$ — `LO-03`.
4. Ứng dụng mảng đếm tần suất 26 ký tự để kiểm tra xâu đảo chữ (Anagram) và chuẩn hóa văn bản — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để xử lý, đối soát và trích xuất thông tin từ các chuỗi văn bản một cách chính xác và hiệu quả trong C++?**

---

### Bài 8.1 — Bản chất của kiểu `string` và Bảng mã ASCII

#### 1. Khái niệm & Bảng mã ASCII
- Mỗi ký tự `char` thực chất là một số nguyên 8-bit ($0..255$).
- `'a'` đến `'z'` có mã $97..122$. Để chuyển sang chỉ số $0..25: 	ext{index} = c - 	ext{'a'}$.
- `'0'` đến `'9'` có mã $48..57$. Để lấy giá trị số: $	ext{val} = c - 	ext{'0'}$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 8.1: Thống Kê Loại Ký Tự Trong Mật Khẩu Hệ Thống**  
> **Bối cảnh:** Hệ thống xác thực mật khẩu ngân hàng cần thống kê số lượng chữ in hoa, chữ in thường, và chữ số trong một chuỗi mật khẩu $S$.  
> **Input:** `iKHEDU C++ 2026!`  
> **Output:** `6 6 4` (6 chữ hoa: K, H, E, D, U, C; 6 chữ thường: i; 4 chữ số: 2, 0, 2, 6).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!getline(cin, s)) return 0;

    int upperCount = 0, lowerCount = 0, digitCount = 0;
    for (char c : s) {
        if (isupper(c)) upperCount++;
        else if (islower(c)) lowerCount++;
        else if (isdigit(c)) digitCount++;
    }

    cout << upperCount << " " << lowerCount << " " << digitCount << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 8.1

##### Bài 8.1.1 — Đếm Số Ký Tự Nguyên Âm Trong Tên Riêng
- **Bối cảnh:** Đếm số lượng nguyên âm (a, e, i, o, u không phân biệt hoa thường) trong xâu $S$.
- **Input:** `Nguyen Van An` $\implies$ **Output:** `4`

##### Bài 8.1.2 — Chuyển Đổi Chữ Hoa Thành Chữ Thường
- **Bối cảnh:** Đổi toàn bộ các ký tự in hoa trong xâu thành in thường.
- **Input:** `HELLO World` $\implies$ **Output:** `hello world`

---

### Bài 8.2 — Xâu đối xứng (Palindrome)

#### 1. Khái niệm & Thuật toán kiểm tra $\mathcal{O}(N)$
- Xâu đọc xuôi hay đọc ngược đều giống nhau. Kiểm tra bằng 2 con trỏ từ 2 đầu `l = 0, r = s.size() - 1`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 8.2: Kiểm Tra Biển Số Xe Đối Xứng Phong Thủy**  
> **Bối cảnh:** Khách hàng muốn kiểm tra biển số xe có phải là chuỗi đối xứng may mắn (Palindrome) hay không.  
> **Input:** `racecar` $\implies$ **Output:** `YES`.  
> **Input:** `ikhedu` $\implies$ **Output:** `NO`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPalindrome(const string &s) {
    int l = 0, r = (int)s.size() - 1;
    while (l < r) {
        if (s[l++] != s[r--]) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    cout << (isPalindrome(s) ? "YES\n" : "NO\n");
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 8.2

##### Bài 8.2.1 — Đoạn Mã Đối Xứng Dài Nhất Trong Bản Tin
- **Bối cảnh:** Tìm độ dài xâu con đối xứng liên tiếp dài nhất trong bản tin $S$ ($|S| \le 1000$).
- **Input:** `babad` $\implies$ **Output:** `3`

##### Bài 8.2.2 — Đếm Số Xâu Đối Xứng Độ Dài 3
- **Bối cảnh:** Đếm số lượng xâu con độ dài 3 là Palindrome trong xâu $S$.
- **Input:** `ababa` $\implies$ **Output:** `3` ("aba", "bab", "aba")

---

### Bài 8.3 — Bảng đếm tần suất 26 chữ cái và Xâu đảo chữ (Anagram)

#### 1. Khái niệm & Thuật toán
- Hai xâu là Anagram nếu có cùng bảng đếm tần suất 26 chữ cái.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 8.3: Đối Soát Khóa Mã Hóa Đảo Vị Trí**  
> **Bối cảnh:** Hai xâu $S$ và $T$ được kiểm tra xem có phải là phiên bản hoán vị các ký tự của nhau hay không.  
> **Input:** `listen silent` $\implies$ **Output:** `YES`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isAnagram(const string &s, const string &t) {
    if (s.size() != t.size()) return false;
    vector<int> cnt(26, 0);
    for (char c : s) cnt[c - 'a']++;
    for (char c : t) cnt[c - 'a']--;
    for (int i = 0; i < 26; i++) {
        if (cnt[i] != 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    cout << (isAnagram(s, t) ? "YES\n" : "NO\n");
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 8.3

##### Bài 8.3.1 — Ký Tự Xác Thực Duy Nhất Trong Tin Nhắn
- **Bối cảnh:** Tìm ký tự đầu tiên trong xâu chỉ xuất hiện đúng 1 lần.
- **Input:** `swiss` $\implies$ **Output:** `w`

##### Bài 8.3.2 — Kiểm Tra Xâu Đảo Chữ Anagram Cơ Bản
- **Bối cảnh:** Kiểm tra xem xâu $S$ và $T$ có phải là Anagram của nhau không.
- **Input:** `anagram nagaram` $\implies$ **Output:** `YES`

---

### Bài 8.4 — Xử lý xâu con, Tách từ và Chuẩn hóa văn bản

#### 1. Khái niệm & Kỹ thuật dùng `stringstream`
- `stringstream ss(s)`: Tách các từ cách nhau bởi khoảng trắng.
- `s.substr(pos, len)`: Cắt xâu con từ vị trí `pos` độ dài `len`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 8.4: Chuẩn Hóa Danh Sách Họ Tên Thí Sinh**  
> **Bối cảnh:** Chuẩn hóa họ tên học sinh nhập từ bàn phím có nhiều khoảng trắng thừa và viết hoa lộn xộn.  
> **Input:** `  nGuYEn   vAn   aN  ` $\implies$ **Output:** `Nguyen Van An`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string formatWord(string w) {
    if (w.empty()) return "";
    w[0] = toupper(w[0]);
    for (size_t i = 1; i < w.size(); i++) {
        w[i] = tolower(w[i]);
    }
    return w;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!getline(cin, s)) return 0;

    stringstream ss(s);
    string word, result = "";

    while (ss >> word) {
        if (!result.empty()) result += " ";
        result += formatWord(word);
    }

    cout << result << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 8.4

##### Bài 8.4.1 — Đếm Số Từ Trong Câu Văn
- **Bối cảnh:** Đếm số lượng từ trong một câu văn có nhiều khoảng trắng thừa bằng `stringstream`.
- **Input:** `  Lap   trinh   C++   ` $\implies$ **Output:** `3`

##### Bài 8.4.2 — Tìm Từ Dài Nhất Trong Văn Bản
- **Bối cảnh:** Tìm từ có độ dài lớn nhất trong chuỗi văn bản.
- **Input:** `Hoc lap trinh cung iKHEDU` $\implies$ **Output:** `iKHEDU`

---

### Bài 8.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)
##### Bài 8.5.1 — Đảo Ngược Chuỗi Dữ Liệu
- **Bối cảnh:** In xâu đảo ngược từ cuối về đầu.
##### Bài 8.5.2 — Thống Kê Nguyên Âm Tiếng Anh
- **Bối cảnh:** Đếm số nguyên âm trong xâu.
##### Bài 8.5.3 — Kiểm Tra Xâu Đối Xứng Cơ Bản
- **Bối cảnh:** Kiểm tra Palindrome.
##### Bài 8.5.4 — Chuyển Đổi Chữ Hoa Đồng Bộ
- **Bối cảnh:** Đổi toàn bộ xâu thành in hoa.

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)
##### Bài 8.5.5 — Tạo Mã Đối Xứng Ngắn Nhất
- **Bối cảnh:** Thêm ít nhất bao nhiêu ký tự vào cuối để xâu thành Palindrome.
##### Bài 8.5.6 — Nén Dữ Liệu Run-Length Encoding
- **Bối cảnh:** Nén xâu `aaabbc` thành `a3b2c1`.
##### Bài 8.5.7 — Đoạn Mã Đối Xứng Dài Nhất $\mathcal{O}(N^2)$
- **Bối cảnh:** Tìm độ dài Palindrome con dài nhất.
##### Bài 8.5.8 — Giải Mã Chuỗi Nén Dữ Liệu
- **Bối cảnh:** Giải mã `a3b2c1` thành `aaabbc`.

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)
##### Bài 8.5.9 — Khôi Phục Chuỗi Nhị Phân Đối Xứng Từ Dấu ?
- **Bối cảnh:** Điền '0'/'1' tạo Palindrome từ điển nhỏ nhất.
##### Bài 8.5.10 — Tìm Chu Kỳ Xung Nhịp Nhỏ Nhất Của Tín Hiệu
- **Bối cảnh:** Tìm chu kỳ nhỏ nhất của xâu $S$.
##### Bài 8.5.11 — Xâu Con Chung Dài Nhất Hai Đoạn Mã
- **Bối cảnh:** LCS 2 xâu $|S|, |T| \le 1000$.
##### Bài 8.5.12 — Ghép Số Lớn Nhất Từ Danh Sách Xâu
- **Bối cảnh:** Sắp xếp ghép xâu bằng comparator $A + B > B + A$.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Dùng `cin >> s` khi đọc chuỗi có dấu cách (bị mất phần sau khoảng trắng) | Luôn dùng `getline(cin, s)` kèm `cin.ignore()` nếu trước đó có lệnh đọc số |
| Trừ chỉ số âm khi ký tự không phải chữ thường `c - 'a'` | Kiểm tra `islower(c)` trước khi tính chỉ số |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Xử lý thành thạo ASCII và kiểm tra Palindrome cơ bản. |
| **Vận dụng (Tầng B)** | Chuẩn hóa văn bản và giải bài toán nén/giải mã xâu RLE. |
| **Thành thạo (Tầng C)** | Áp dụng Quy hoạch động tìm LCS và giải bài toán ghép xâu lớn nhất. |
