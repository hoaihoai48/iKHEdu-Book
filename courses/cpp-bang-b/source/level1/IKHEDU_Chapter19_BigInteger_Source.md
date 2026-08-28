# TÀI LIỆU GỐC — CHƯƠNG 19: XỬ LÝ SỐ NGUYÊN LỚN (BIG INTEGER)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật biểu diễn và thực hiện 4 phép tính số học (+, -, *, /) trên các số nguyên lớn hàng nghìn chữ số vượt qua giới hạn của kiểu dữ liệu 64-bit `long long` trong C++; biểu diễn số lớn bằng xâu ký tự (`string`) hoặc mảng chữ số (`vector<int>`) |
| Kiến thức cần có | Xâu ký tự (`string`), mảng, vòng lặp, toán tử chia và chia dư |
| Phạm vi | Biểu diễn số lớn bằng `string`, Phép so sánh 2 số lớn, Phép cộng số lớn, Phép trừ số lớn (có nhớ), Phép nhân số lớn với số nhỏ/số lớn, Phép chia số lớn cho số nhỏ và phép Modulo số lớn |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Đọc và biểu diễn số nguyên lớn hàng nghìn chữ số bằng `string` hoặc `vector<int>` đảo ngược — `LO-01`.
2. Cài đặt hàm so sánh 2 số nguyên lớn dựa trên độ dài và thứ tự từ điển — `LO-02`.
3. Cài đặt chính xác phép Cộng và phép Trừ số lớn (kèm kỹ thuật xử lý biến nhớ `carry`) — `LO-03`.
4. Cài đặt phép Nhân số lớn với số lớn và phép Chia/Modulo số lớn cho số nguyên thường trong $\mathcal{O}(N)$ — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để máy tính thực hiện các phép cộng, nhân trên những con số có hàng nghìn chữ số vượt xa giới hạn $10^{18}$ của kiểu `long long`?**

---

### Bài 19.1 — Biểu diễn số lớn và Phép so sánh

#### 1. Khái niệm & Biểu diễn mảng đảo ngược
- Số $A = 12345$ được lưu dưới dạng xâu `string a = "12345"`. Để thuận tiện cho việc cộng/trừ từ hàng đơn vị sang hàng chục, ta duyệt từ cuối về đầu hoặc đảo ngược xâu: `a[0] = 5, a[1] = 4, a[2] = 3, a[3] = 2, a[4] = 1`.
- **So sánh 2 số lớn:**
  - Nếu độ dài khác nhau: Số nào có độ dài lớn hơn thì số đó lớn hơn.
  - Nếu độ dài bằng nhau: So sánh theo thứ tự từ điển từ trái sang phải.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 19.1: Xếp Hạng Giá Trị Gói Thầu Quốc Tế**  
> **Bối cảnh:** $N$ hồ sơ dự thầu có giá trị là các số nguyên dương cực lớn (lên tới $1000$ chữ số).  
> **Nhiệm vụ:** Tìm giá trị gói thầu lớn nhất trong danh sách.  
> **Input:** `3` \ `99999999999999999999` \ `100000000000000000000` \ `50000000000000000000` $\implies$ **Output:** `100000000000000000000`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isGreater(const string &a, const string &b) {
    if (a.size() != b.size()) return a.size() > b.size();
    return a > b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    string maxVal = "";
    for (int i = 0; i < n; i++) {
        string s;
        cin >> s;
        if (maxVal == "" || isGreater(s, maxVal)) {
            maxVal = s;
        }
    }

    cout << maxVal << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 19.1

##### Bài 19.1.1 — Sắp Xếp Danh Sách Số Nguyên Lớn Tăng Dần
- **Bối cảnh:** Sắp xếp $N$ số nguyên lớn (mỗi số có tới 500 chữ số) theo thứ tự tăng dần.
- **Input:** `3` \ `100` \ `20` \ `5` $\implies$ **Output:** `5 20 100`

##### Bài 19.1.2 — Tìm Số Lớn Nhất Trong N Số Nguyên Lớn
- **Bối cảnh:** In ra số nguyên lớn nhất trong $N$ số có độ dài $10^4$ chữ số.
- **Input:** `2` \ `999` \ `1000` $\implies$ **Output:** `1000`

---

### Bài 19.2 — Phép cộng và Phép trừ số lớn

#### 1. Khái niệm & Kỹ thuật biến nhớ `carry`
- Cộng từng hàng chữ số từ phải sang trái, giữ lại `carry = sum / 10`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 19.2: Tổng Doanh Số Chuỗi Bán Lẻ Toàn Cầu**  
> **Bối cảnh:** Tính tổng giá trị của hai số nguyên dương lớn $A$ và $B$ có tới $10^5$ chữ số: $A + B$.  
> **Input:** `99999999999999999999 1` $\implies$ **Output:** `100000000000000000000`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string addBigInt(string a, string b) {
    string res = "";
    int i = (int)a.size() - 1, j = (int)b.size() - 1;
    int carry = 0;

    while (i >= 0 || j >= 0 || carry) {
        int sum = carry;
        if (i >= 0) sum += (a[i--] - '0');
        if (j >= 0) sum += (b[j--] - '0');
        res.push_back((sum % 10) + '0');
        carry = sum / 10;
    }

    reverse(res.begin(), res.end());
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << addBigInt(a, b) << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 19.2

##### Bài 19.2.1 — Hiệu Hai Số Nguyên Lớn (A - B Với A >= B)
- **Bối cảnh:** Cho hai số lớn $A$ và $B$ ($A \ge B$). Tính và in ra kết quả $A - B$.
- **Input:** `1000 1` $\implies$ **Output:** `999`

##### Bài 19.2.2 — Tổng Ba Số Nguyên Lớn
- **Bối cảnh:** Tính $A + B + C$ với $|A|, |B|, |C| \le 10^4$ chữ số.
- **Input:** `999 1 1` $\implies$ **Output:** `1001`

---

### Bài 19.3 — Phép nhân số lớn

#### 1. Khái niệm & Thuật toán
- Nhân số lớn với số nhỏ $\mathcal{O}(N)$.
- Nhân số lớn với số lớn $\mathcal{O}(N \times M)$ bằng mảng tích lũy.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 19.3: Nhân Số Lớn Với Số Lớn**  
> **Bối cảnh:** Tính tích của 2 số nguyên dương $A$ và $B$ có tới $1000$ chữ số.  
> **Input:** `123 45` $\implies$ **Output:** `5535`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

string multiplyBigInt(string a, string b) {
    if (a == "0" || b == "0") return "0";
    int n = a.size(), m = b.size();
    vector<int> res(n + m, 0);

    for (int i = n - 1; i >= 0; i--) {
        for (int j = m - 1; j >= 0; j--) {
            int mul = (a[i] - '0') * (b[j] - '0');
            int sum = mul + res[i + j + 1];
            res[i + j + 1] = sum % 10;
            res[i + j] += sum / 10;
        }
    }

    string ans = "";
    int i = 0;
    while (i < (int)res.size() && res[i] == 0) i++;
    while (i < (int)res.size()) ans.push_back(res[i++] + '0');

    return ans.empty() ? "0" : ans;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string a, b;
    if (!(cin >> a >> b)) return 0;

    cout << multiplyBigInt(a, b) << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 19.3

##### Bài 19.3.1 — Tính Lũy Thừa $2^N$ Chính Xác Không Lấy Dư
- **Bối cảnh:** Tính và in ra toàn bộ các chữ số của $2^N$ với $N \le 1000$.
- **Input:** `10` $\implies$ **Output:** `1024`

##### Bài 19.3.2 — Tính Giai Thừa N! Chính Xác
- **Bối cảnh:** Tính $N!$ với $N \le 100$ in ra toàn bộ các chữ số.
- **Input:** `5` $\implies$ **Output:** `120`

---

### Bài 19.4 — Phép chia số lớn cho số nhỏ và Modulo

#### 1. Khái niệm & Sơ đồ Horner
- Chia số lớn $S$ cho số nhỏ $M$: Duyệt từ trái sang phải, `rem = (rem * 10 + (c - '0')) % M`.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 19.4: Kiểm Tra Tính Chia Hết Của Khóa Mã Hóa 10.000 Chữ Số**  
> **Bối cảnh:** Cho số nguyên lớn $S$ có tới $10^4$ chữ số và một số nguyên $M \le 10^9$. Hãy tính phần dư $S \pmod M$.  
> **Input:** `123456789101112131415 13` $\implies$ **Output:** `4`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    long long m;
    if (!(cin >> s >> m)) return 0;

    long long rem = 0;
    for (char c : s) {
        rem = (rem * 10 + (c - '0')) % m;
    }

    cout << rem << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 19.4

##### Bài 19.4.1 — Phép Chia Nguyên Cho Số Nhỏ
- **Bối cảnh:** Cho số lớn $A$ và số nhỏ $B \le 10^9$. In ra thương nguyên $\lfloor A / B \rfloor$.
- **Input:** `100 4` $\implies$ **Output:** `25`

##### Bài 19.4.2 — Kiểm Tra Số Lớn Chia Hết Cho 11
- **Bối cảnh:** Kiểm tra số lớn $S$ có chia hết cho 11 không bằng hiệu tổng các chữ số ở vị trí lẻ và chẵn.
- **Input:** `121` $\implies$ **Output:** `YES`

---

### Bài 19.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 19.5.1 — So Sánh Hai Số Nguyên Lớn
- **Bối cảnh:** In `<, =, >` khi so sánh hai số nguyên $A$ và $B$ có tới $10^5$ chữ số.

##### Bài 19.5.2 — Tổng Hai Số Cực Đại
- **Bối cảnh:** Tính $A + B$ với $|A|, |B| \le 10^5$ chữ số.

##### Bài 19.5.3 — Hiệu Hai Số Nguyên Dương Lớn
- **Bối cảnh:** Tính $A - B$ (đảm bảo $A \ge B$) với độ dài $10^5$ chữ số.

##### Bài 19.5.4 — Nhân Số Lớn Với Số Nguyên Nhỏ
- **Bối cảnh:** Tính $A \times K$ với $|A| \le 10^5$ chữ số và $K \le 10^9$.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 19.5.5 — Nhân Hai Số Nguyên Lớn $\mathcal{O}(N \times M)$
- **Bối cảnh:** Tính $A \times B$ với $|A|, |B| \le 2000$ chữ số.

##### Bài 19.5.6 — Tính Giai Thừa Của Số Lớn $N!$
- **Bối cảnh:** Tính chính xác giá trị $N!$ (không lấy modulo) với $N \le 500$ (in toàn bộ các chữ số).

##### Bài 19.5.7 — Số Fibonacci Thứ 1000 Chính Xác
- **Bối cảnh:** Tính số Fibonacci $F_{1000}$ bằng mảng cộng số lớn.

##### Bài 19.5.8 — Phép Chia Số Lớn Cho Số Nguyên Nhỏ
- **Bối cảnh:** Cho số lớn $A$ và số nhỏ $B \le 10^9$. In thương số nguyên $\lfloor A / B \rfloor$ và phần dư $A \% B$.

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 19.5.9 — Phép Chia Số Lớn Cho Số Lớn (BigInt Division)
- **Bối cảnh:** Tính $\lfloor A / B \rfloor$ khi cả $A$ và $B$ đều là số lớn bằng Tìm kiếm nhị phân kết hợp nhân số lớn.

##### Bài 19.5.10 — Căn Bậc Hai Của Số Nguyên Lớn 1000 Chữ Số
- **Bối cảnh:** Tìm $\lfloor\sqrt{A}\rfloor$ với $A$ có $1000$ chữ số bằng Binary Search + BigInt.

##### Bài 19.5.11 — Nhân Số Lớn Siêu Tốc Bằng Biến Đổi Fourier Nhanh (FFT)
- **Bối cảnh:** Nhân hai số lớn $10^5$ chữ số trong $\mathcal{O}(N \log N)$ bằng thuật toán FFT.

##### Bài 19.5.12 — Chuyển Đổi Số Lớn Giữa Các Hệ Cơ Số
- **Bối cảnh:** Chuyển đổi số lớn từ hệ thập phân sang hệ nhị phân hoặc hệ thập lục phân.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Bỏ sót số 0 vô nghĩa ở đầu (ví dụ in `0015` thay vì `15` sau phép trừ) | Dùng vòng lặp `while (res.size() > 1 && res.back() == '0') res.pop_back();` |
| Quên đảo ngược xâu kết quả sau khi `push_back` | Luôn gọi `reverse(res.begin(), res.end())` ở cuối hàm |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt chính xác phép Cộng, Trừ và Nhân số lớn với số nhỏ. |
| **Vận dụng (Tầng B)** | Tính chính xác $N!$ và Nhân 2 số lớn $\mathcal{O}(NM)$ không lỗi số 0 đầu. |
| **Thành thạo (Tầng C)** | Cài đặt chia số lớn cho số lớn và tính căn bậc hai số lớn. |
