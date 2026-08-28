# TÀI LIỆU GỐC — CHƯƠNG 3: SỐ HỌC

## Vai trò tài liệu

Tài liệu này là bản gốc nội dung dùng để biên soạn Chương 3 — Số học. Nội dung được viết và review tại đây trước khi tổng hợp sang bản thảo sách. Chương này trang bị các công cụ số học nền tảng: **ước, bội, ước chung lớn nhất (GCD), bội chung nhỏ nhất (LCM), số nguyên tố, phân tích thừa số và Sàng Eratosthenes**.

## Đối tượng và phạm vi

Tài liệu dành cho học sinh đã biết vòng lặp, câu lệnh điều kiện, mảng/vector và kiểu dữ liệu `long long`. Luồng bài học dẫn dắt trực quan từ việc tìm ước bằng tay, thuật toán Euclid, quy tắc chia trước khi nhân, tối ưu bước nhảy kiểm tra nguyên tố cho đến sàng lọc hàng loạt. Các lý thuyết nâng cao như hàm số học và định lý Legendre được trình bày như bài toán mở rộng có hướng dẫn, không nhồi nhét công thức nặng nề.

## Nguyên tắc biên soạn

Mỗi bài học tuân thủ chuỗi sư phạm: mục tiêu, khởi động trực quan, ý tưởng, mô phỏng tay từng bước, pseudocode, code C++ ngắn gọn, theo dõi biến khi debug, tự kiểm tra, luyện tập ngắn và tóm tắt.

---

## Chương 3 — Số học

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu bản chất các quy luật số học để giảm số phép tính từ hàng tỷ bước xuống vài chục thao tác |
| Kiến thức cần có | Vòng lặp `for`/`while`, câu lệnh `if-else`, toán tử chia dư `%`, mảng/vector, kiểu dữ liệu `long long` |
| Phạm vi | Ước và bội, thuật toán Euclid tìm GCD, tính LCM an toàn, kiểm tra số nguyên tố $\mathcal{O}(\sqrt{N})$, phân tích thừa số và Sàng Eratosthenes |
| Số bài | 6 bài học lý thuyết & thực hành + 1 bài tổng kết và bài tập phân tầng |

### Learning outcomes

Sau chương này, em có thể:
1. Giải thích quy luật đối xứng của các cặp ước và tìm toàn bộ ước trong $\mathcal{O}(\sqrt{N})$.
2. Mô phỏng và cài đặt thuật toán Euclid tìm ước chung lớn nhất (GCD) trong $\mathcal{O}(\log(\min(A, B)))$.
3. Tính bội chung nhỏ nhất (LCM) an toàn bằng quy tắc "chia trước khi nhân" chống tràn số nguyên 64-bit.
4. Kiểm tra một số nguyên có phải số nguyên tố trong $\mathcal{O}(\sqrt{N})$ với bước nhảy $6k \pm 1$.
5. Phân tích một số nguyên dương thành tích các thừa số nguyên tố bằng thuật toán chia dần.
6. Cài đặt và sử dụng Sàng Eratosthenes $\mathcal{O}(N \log \log N)$ để trả lời nhanh các truy vấn số nguyên tố.
7. Xử lý chính xác các trường hợp biên: $N = 0, 1$, số âm và số lớn vượt kiểu `int` ($10^9 \to 10^{18}$).

### Câu hỏi trung tâm của chương

> **Làm thế nào để kiểm tra, đếm và phân tích tính chất chia hết của một số nguyên lớn mà không làm chương trình bị quá thời gian hay tràn bộ nhớ?**

---

### Bài 3.1 — Ước, bội và quy luật đối xứng cặp ước

#### Mục tiêu bài

Sau Bài 3.1, em có thể giải thích định nghĩa ước - bội, nhận biết quy luật đối xứng qua $\sqrt{N}$ và viết được chương trình tìm toàn bộ ước của số nguyên $N \le 10^{12}$ trong thời gian dưới $0.01$ giây.

#### Khởi động

Giả sử em có $N = 36$ chiếc kẹo và muốn chia đều vào các túi, mỗi túi có đúng $d$ chiếc.
- Nếu mỗi túi có $d = 2$ chiếc $\implies$ cần $36 / 2 = 18$ túi. Cặp số $(2, 18)$ cùng xuất hiện từ một phép chia hết!
- Liệu em có cần thử duyệt từ $1$ đến tận $36$ để tìm tất cả các cách chia không?

#### Ước, bội và quy luật đối xứng

- Số nguyên dương $d$ là **ước** của $N$ nếu phép chia $N$ cho $d$ có phần dư bằng $0$ (`N % d == 0`). Khi đó $N$ là **bội** của $d$.
- Nếu $d$ là một ước của $N$ thì thương số $N / d$ cũng chắc chắn là một ước của $N$:
  $$d \times \frac{N}{d} = N$$
- Trong mỗi cặp ước $(d, N/d)$, số nhỏ hơn không bao giờ vượt quá $\sqrt{N}$. Vì nếu cả hai số đều lớn hơn $\sqrt{N}$ thì tích của chúng sẽ lớn hơn $\sqrt{N} \times \sqrt{N} = N$ (vô lý).

> **Chỉ cần duyệt $d$ từ $1$ đến $\lfloor\sqrt{N}\rfloor$ ($d \times d \le N$). Với mỗi ước $d$ tìm thấy, ta lấy thêm ước đối xứng $N/d$.**

#### Mô phỏng từng lượt tìm ước của $N = 36$ ($\sqrt{36} = 6$)

| Lượt duyệt $d$ | $36 \% d == 0$? | Cặp ước thu được $(d, 36/d)$ | Ghi chú |
|:---:|:---:|:---:|---|
| $1$ | Có | $(1, 36)$ | Lấy cả 1 và 36 |
| $2$ | Có | $(2, 18)$ | Lấy cả 2 và 18 |
| $3$ | Có | $(3, 12)$ | Lấy cả 3 và 12 |
| $4$ | Có | $(4, 9)$ | Lấy cả 4 và 9 |
| $5$ | Không | Bỏ qua | 36 không chia hết cho 5 |
| $6$ | Có | $(6, 6)$ | $d = N/d \implies$ chỉ lấy một số 6 |

#### Pseudocode

```text
divisors = danh sách rỗng
for d từ 1 đến khi d * d > n:
    nếu n % d == 0:
        thêm d vào divisors
        nếu d != n / d:
            thêm (n / d) vào divisors
sắp xếp divisors tăng dần
in số lượng và danh sách ước
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    vector<long long> divisors;
    for (long long d = 1; d * d <= n; d++) {
        if (n % d == 0) {
            divisors.push_back(d);
            if (d * d != n) {
                divisors.push_back(n / d);
            }
        }
    }

    sort(divisors.begin(), divisors.end());

    cout << divisors.size() << '\n';
    for (int i = 0; i < (int)divisors.size(); i++) {
        if (i > 0) cout << ' ';
        cout << divisors[i];
    }
    cout << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Biến | Câu hỏi kiểm tra |
|---|---|
| `d` | Đã khai báo kiểu `long long` chưa? (Nếu khai báo `int d`, khi $N = 10^{12}$ thì `d * d` sẽ tràn số gây lặp vô hạn). |
| `d * d != n` | Có bị trùng ước khi $N$ là số chính phương ($36 = 6 \times 6$) không? |
| `d * d <= n` | Đã dùng phép nhân nguyên thay vì gọi hàm `sqrt(n)` chưa? |

#### Tự kiểm tra

1. Vì sao trong mỗi cặp ước $(d, N/d)$ luôn có ít nhất một số $\le \sqrt{N}$?
2. Số nguyên dương $N$ có số lượng ước là số lẻ khi và chỉ khi $N$ là số gì?
3. Với $N = 10^{12}$, vòng lặp `for` chạy tối đa bao nhiêu lần?

#### Luyện tập ngắn

- **LT 3.1A:** Viết chương trình tính tổng tất cả các ước của $N$ ($N \le 10^9$) trong $\mathcal{O}(\sqrt{N})$.
- **LT 3.1B:** Kiểm tra xem số $N$ có phải là số hoàn hảo không (số hoàn hảo bằng tổng các ước thực sự nhỏ hơn nó, ví dụ $6 = 1 + 2 + 3$).

#### Tóm tắt bài

Ước số luôn đi theo từng cặp $(d, N/d)$. Duyệt $d$ từ $1$ đến $\sqrt{N}$ giúp giảm độ phức tạp từ $\mathcal{O}(N)$ xuống $\mathcal{O}(\sqrt{N})$, giải quyết nhẹ nhàng bài toán $N \le 10^{12}$.

---

### Bài 3.2 — Ước chung lớn nhất (GCD) và Thuật toán Euclid

#### Mục tiêu bài

Sau Bài 3.2, em hiểu bản chất của ước chung lớn nhất, nắm vững thuật toán Euclid $\mathcal{O}(\log(\min(A, B)))$ và tự tin cài đặt hàm `gcd` để rút gọn phân số hoặc tìm chu kỳ chung.

#### Khởi động

Em có một mảnh sân hình chữ nhật dài $105\text{ cm}$, rộng $45\text{ cm}$. Em muốn lát kín sân bằng các viên gạch vuông có kích thước lớn nhất mà không phải cắt gọt viên nào.
- Cạnh viên gạch phải là ước chung của cả $105$ và $45$.
- Viên gạch lớn nhất có cạnh bằng **Ước chung lớn nhất** $\gcd(105, 45)$.

#### Thuật toán Euclid

- **Ước chung lớn nhất ($\gcd(a, b)$):** Là số nguyên dương lớn nhất chia hết cả $a$ và $b$. Nếu $\gcd(a, b) = 1$, ta gọi $a$ và $b$ là hai số **nguyên tố cùng nhau**.
- **Định lý Euclid:** Ước chung lớn nhất của hai số không thay đổi khi thay số lớn bằng số dư của phép chia số lớn cho số nhỏ:
  $$\gcd(a, b) = \gcd(b, a \% b)$$
  Quá trình dừng lại khi số dư bằng $0$, khi đó số còn lại chính là $\gcd$.

#### Mô phỏng từng bước cho cặp $(a = 105, b = 45)$

| Bước | $a$ | $b$ | Phép chia dư $a \% b$ | Cập nhật tiếp theo |
|:---:|:---:|:---:|:---:|---|
| 1 | $105$ | $45$ | $105 \% 45 = 15$ | $a = 45, b = 15$ |
| 2 | $45$ | $15$ | $45 \% 15 = 0$ | $a = 15, b = 0$ |
| 3 | $15$ | $0$ | Dừng vì $b = 0$ | **Kết quả: $\gcd = 15$** |

Sau mỗi bước, số dư giảm đi ít nhất một nửa. Thuật toán chạy với độ phức tạp $\mathcal{O}(\log(\min(A, B)))$, với hai số $10^{18}$ chỉ mất chưa tới 60 phép chia dư!

#### Pseudocode

```text
hàm gcd(a, b):
    trong khi b != 0:
        r = a % b
        a = b
        b = r
    trả về a
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    long long g = gcd(a, b);
    cout << a / g << " " << b / g << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Biến | Câu hỏi kiểm tra |
|---|---|
| `b != 0` | Vòng lặp dừng khi $b = 0$, kết quả trả về là $a$. |
| $a < b$ | Nếu truyền vào $a = 45, b = 105$, bước đầu tiên $45 \% 105 = 45 \implies$ thuật toán tự động đảo lại thành $a = 105, b = 45$. |

#### Tự kiểm tra

1. Điều kiện dừng của thuật toán Euclid là gì?
2. Hai số nguyên dương được gọi là nguyên tố cùng nhau khi $\gcd(a, b)$ bằng bao nhiêu?
3. Muốn tìm $\gcd$ của 3 số $a, b, c$, ta làm thế nào?

#### Luyện tập ngắn

- **LT 3.2A:** Nhập vào dãy $N$ số nguyên ($N \le 10^5, A_i \le 10^9$). Tìm ước chung lớn nhất của cả dãy.
- **LT 3.2B:** Rút gọn phân số $\frac{A}{B}$ về dạng tối giản $\frac{P}{Q}$.

#### Tóm tắt bài

Thuật toán Euclid $\gcd(a, b) = \gcd(b, a \% b)$ chạy với tốc độ logarithmic $\mathcal{O}(\log(\min(A, B)))$, là công cụ nhanh nhất để tìm ước chung và rút gọn phân số.

---

### Bài 3.3 — Bội chung nhỏ nhất (LCM) và Kỹ thuật chống tràn số

#### Mục tiêu bài

Sau Bài 3.3, em hiểu mối liên hệ giữa GCD và LCM, nắm vững quy tắc **"Chia trước khi Nhân"** để tính LCM của các số lớn mà không bao giờ bị tràn số.

#### Khởi động

Hai chiếc xe cùng xuất phát từ bến lúc 6h sáng. Xe A cứ $12$ phút quay lại bến một lần, xe B cứ $18$ phút quay lại bến một lần. Sau bao lâu hai xe lại cùng lúc về bến?
- Khoảng thời gian đó chính là **Bội chung nhỏ nhất** $\text{lcm}(12, 18) = 36$ phút.

#### Mối liên hệ và Bẫy tràn số

- **Bội chung nhỏ nhất ($\text{lcm}(a, b)$):** Số nguyên dương nhỏ nhất chia hết cho cả $a$ và $b$.
- **Công thức liên hệ:**
  $$a \times b = \gcd(a, b) \times \text{lcm}(a, b) \implies \text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}$$
- **Bẫy tràn số:** Nếu tính `(a * b) / gcd(a, b)` khi $a, b = 10^9$, tích $a \times b = 10^{18}$ sẽ tràn số `int` ngay lập tức.
- **Quy tắc an toàn:** Vì $a$ luôn chia hết cho $\gcd(a, b)$, ta chia trước rồi mới nhân:
  $$\text{lcm}(a, b) = \left( \frac{a}{\gcd(a, b)} \right) \times b$$

#### Pseudocode

```text
hàm lcm(a, b):
    nếu a == 0 hoặc b == 0: trả về 0
    trả về (a / gcd(a, b)) * b
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << lcm(a, b) << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Thao tác | Đánh giá |
|---|---|
| `(a * b) / gcd(a, b)` | ❌ Nguy hiểm, dễ tràn số trung gian. |
| `(a / gcd(a, b)) * b` |  An toàn, luôn là phép chia hết. |

#### Tự kiểm tra

1. Tại sao phép chia `a / gcd(a, b)` không bao giờ có dư?
2. Nếu $a$ và $b$ nguyên tố cùng nhau thì $\text{lcm}(a, b)$ bằng bao nhiêu?

#### Luyện tập ngắn

- **LT 3.3A:** Nhập vào 3 số $A, B, C \le 10^6$. Tính $\text{lcm}(A, B, C)$.
- **LT 3.3B:** Tìm số nguyên dương nhỏ nhất chia cho cả 4, 5, 6 đều dư 1.

#### Tóm tắt bài

$\text{lcm}(a, b) = (a / \gcd(a, b)) \times b$. Luôn **chia trước khi nhân** để bảo vệ chương trình khỏi bẫy tràn số 64-bit.

---

### Bài 3.4 — Số nguyên tố và Kỹ thuật kiểm tra tối ưu $\mathcal{O}(\sqrt{N})$

#### Mục tiêu bài

Sau Bài 3.4, em hiểu định nghĩa số nguyên tố, cài đặt được hàm kiểm tra nguyên tố $\mathcal{O}(\sqrt{N})$ và nắm được kỹ thuật tăng tốc bước nhảy $6k \pm 1$.

#### Khởi động

Số nguyên tố giống như các "viên gạch nguyên tử" của thế giới số tự nhiên — chúng không thể phân tách thành tích của các số nhỏ hơn. Mọi thuật toán mã hóa ngân hàng và bảo mật ngày nay đều dựa trên tính chất này.

#### Khái niệm & Thuật toán kiểm tra

- **Số nguyên tố:** Là số nguyên $> 1$ chỉ có đúng 2 ước nguyên dương phân biệt là $1$ và chính nó ($2, 3, 5, 7, 11, 13, \dots$).
- Số $0$ và $1$ **không phải** là số nguyên tố.
- **Quy tắc $\mathcal{O}(\sqrt{N})$:** Nếu $N > 1$ là hợp số, nó luôn có ít nhất một ước nguyên tố $d \le \sqrt{N}$. Do đó, chỉ cần kiểm tra xem $N$ có chia hết cho số nào từ $2$ đến $\sqrt{N}$ không.
- **Tối ưu bước nhảy $6k \pm 1$:** Mọi số nguyên tố $> 3$ đều có dạng $6k - 1$ hoặc $6k + 1$. Sau khi kiểm tra chia hết cho 2 và 3, ta chỉ cần thử các số $i$ và $i + 2$ với bước nhảy $i += 6$, giúp giảm bớt $2/3$ số phép chia.

#### Mô phỏng kiểm tra $N = 29$ ($\sqrt{29} \approx 5.38$)

| Bước | Số thử chia | $29 \% i == 0$? | Kết luận |
|:---:|:---:|:---:|---|
| 1 | $2$ | Không | 29 là số lẻ |
| 2 | $3$ | Không | 29 không chia hết cho 3 |
| 3 | $5$ ($i = 5$) | Không | $5 \times 5 = 25 \le 29$, không chia hết |
| 4 | $7$ ($i + 2 = 7$) | Bỏ qua | $7 \times 7 = 49 > 29$, dừng vòng lặp |

👉 **Kết luận:** 29 là số nguyên tố.

#### Pseudocode

```text
hàm isPrime(n):
    nếu n < 2: trả về false
    nếu n == 2 hoặc n == 3: trả về true
    nếu n % 2 == 0 hoặc n % 3 == 0: trả về false
    i = 5
    trong khi i * i <= n:
        nếu n % i == 0 hoặc n % (i + 2) == 0:
            trả về false
        i = i + 6
    trả về true
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    if (isPrime(n)) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Giá trị biên | Kết quả đúng | Lỗi thường gặp |
|---|---|---|
| $N = 0, 1$ | `false` | Quên chặn điều kiện $N < 2$. |
| $N = 2, 3$ | `true` | Bị loại nhầm bởi các điều kiện chia hết. |
| $N = 10^{12}$ | Chạy dưới $0.001$s | Dùng `int i` gây tràn số ở `i * i`. |

#### Tự kiểm tra

1. Số nguyên tố chẵn duy nhất là số nào?
2. Vì sao một hợp số $N$ luôn có ước nguyên tố $\le \sqrt{N}$?

#### Luyện tập ngắn

- **LT 3.4A:** Tìm số nguyên tố nhỏ nhất lớn hơn số nguyên dương $N$ ($N \le 10^9$).
- **LT 3.4B:** Đếm số lượng số nguyên tố trong đoạn $[L, R]$ với $R - L \le 10^5, R \le 10^{12}$.

#### Tóm tắt bài

Kiểm tra số nguyên tố chỉ cần duyệt đến $\sqrt{N}$. Kết hợp bước nhảy $6k \pm 1$ giúp hàm `isPrime()` đạt tốc độ tối đa cho mọi $N \le 10^{12}$.

---

### Bài 3.5 — Phân tích thừa số nguyên tố

#### Mục tiêu bài

Sau Bài 3.5, em biết cách phân rã một số nguyên dương thành tích các thừa số nguyên tố bằng thuật toán chia dần $\mathcal{O}(\sqrt{N})$ và ứng dụng để đếm số lượng ước.

#### Khởi động

Số $60$ có thể viết thành $2 \times 2 \times 3 \times 5 = 2^2 \times 3^1 \times 5^1$. Mọi số nguyên $> 1$ đều có duy nhất một cách phân tích như vậy.

#### Thuật toán chia dần

1. Cho $p$ chạy từ $2$ đến khi $p \times p > N$.
2. Nếu $N \% p == 0$, ta đếm số mũ của $p$ bằng cách chia $N$ liên tục cho $p$ trong khi $N \% p == 0$.
3. Sau vòng lặp, nếu giá trị $N$ còn lại $> 1$ thì giá trị đó chính là thừa số nguyên tố cuối cùng (với số mũ 1).

#### Mô phỏng từng bước phân tích $N = 60$

| Bước | $N$ hiện tại | $p$ đang xét | Thao tác chia rút gọn | Thừa số thu được | $N$ sau khi chia |
|:---:|:---:|:---:|---|:---:|:---:|
| 1 | $60$ | $p = 2$ | $60 \% 2 == 0 \implies 60 / 2 = 30 \implies 30 / 2 = 15$ | $2^2$ | $15$ |
| 2 | $15$ | $p = 3$ | $15 \% 3 == 0 \implies 15 / 3 = 5$ | $3^1$ | $5$ |
| 3 | $5$ | $p = 4$ | $4 \times 4 = 16 > 5 \implies$ dừng vòng lặp | - | $5$ |
| 4 | $5 > 1$ | - | Thừa số nguyên tố cuối cùng là $5^1$ | $5^1$ | $1$ |

👉 **Kết quả:** $60 = 2^2 \times 3^1 \times 5^1$.

#### Pseudocode

```text
for p từ 2 đến khi p * p > n:
    nếu n % p == 0:
        exp = 0
        trong khi n % p == 0:
            exp tăng 1
            n = n / p
        in p và exp
nếu n > 1:
    in n và exp = 1
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long n;
    if (!(cin >> n)) return 0;

    bool first = true;
    for (long long p = 2; p * p <= n; p++) {
        if (n % p == 0) {
            int exp = 0;
            while (n % p == 0) {
                exp++;
                n /= p;
            }
            if (!first) cout << " * ";
            cout << p << "^" << exp;
            first = false;
        }
    }

    if (n > 1) {
        if (!first) cout << " * ";
        cout << n << "^1";
    }
    cout << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Tình huống | Hiện tượng | Cách xử lý đúng |
|---|---|---|
| Số nguyên tố $N = 13$ | Vòng lặp dừng ngay ở $p = 2$ | Khối lệnh `if (n > 1)` sẽ in ra $13^1$. |
| Hợp số $p = 4, 6$ | Có bị in nhầm làm thừa số không? | Không, vì các thừa số nguyên tố nhỏ hơn ($2, 3$) đã chia rút gọn hết $N$ từ trước. |

#### Tự kiểm tra

1. Vì sao không cần kiểm tra $p$ có phải số nguyên tố trước khi chia?
2. Nếu $N = 2^3 \times 3^2 \times 5^1$, số lượng ước của $N$ tính bằng công thức nào? (Đáp án: $(3+1)(2+1)(1+1) = 24$ ước).

#### Luyện tập ngắn

- **LT 3.5A:** Nhập vào số nguyên dương $N \le 10^{12}$. Tìm ước nguyên tố lớn nhất của $N$.
- **LT 3.5B:** Đếm số lượng ước nguyên dương của $N$ ($N \le 10^{12}$) dựa vào phân tích thừa số nguyên tố.

#### Tóm tắt bài

Thuật toán chia dần $\mathcal{O}(\sqrt{N})$ tự động lọc ra các thừa số nguyên tố. Đây là chìa khóa tính nhanh số lượng ước và tổng ước của số cực lớn.

---

### Bài 3.6 — Sàng số nguyên tố Eratosthenes

#### Mục tiêu bài

Sau Bài 3.6, em hiểu nguyên lý sàng lọc bội số, cài đặt thành thạo Sàng Eratosthenes $\mathcal{O}(N \log \log N)$ và biết cách trả lời tức thì $\mathcal{O}(1)$ các truy vấn kiểm tra nguyên tố cho hàng triệu số.

#### Khởi động

Nếu cần kiểm tra số nguyên tố cho $Q = 10^6$ truy vấn, mỗi truy vấn $x \le 10^7$:
- Dùng `isPrime(x)` tốn $10^6 \times \sqrt{10^7} \approx 3 \times 10^9$ phép tính $\implies$ Mất 30 giây (TLE).
- **Giải pháp:** Tiền xử lý một lần duy nhất bằng **Sàng Eratosthenes** trong $0.1$ giây, sau đó mỗi truy vấn chỉ mất $\mathcal{O}(1)$ để tra cứu!

#### Cơ chế Sàng lọc

1. Ban đầu giả sử tất cả các số từ $2$ đến $N$ đều là số nguyên tố (`is_prime[i] = true`).
2. Xét từ số nguyên tố đầu tiên $p = 2$: Giữ lại số 2, gạch bỏ các bội số của 2 ($4, 6, 8, \dots$).
3. Tìm số tiếp theo chưa bị gạch là $p = 3$: Giữ lại số 3, gạch bỏ các bội của 3 ($9, 12, 15, \dots$, bắt đầu từ $p \times p = 9$).
4. Tiếp tục đến $p \le \sqrt{N}$. Tất cả các số chưa bị gạch còn lại chính là **toàn bộ số nguyên tố trong đoạn $[2, N]$**.

#### Mô phỏng sàng từ 2 đến 20

```text
Ban đầu:     2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
Gạch bội 2:  2  3  .  5  .  7  .  9  . 11  . 13  . 15  . 17  . 19  .
Gạch bội 3:  2  3  .  5  .  7  .  .  . 11  . 13  .  .  . 17  . 19  .
Còn lại:     2, 3, 5, 7, 11, 13, 17, 19
```

#### Pseudocode

```text
is_prime[0] = is_prime[1] = false
mọi vị trí từ 2 đến N gán bằng true

for p từ 2 đến khi p * p > N:
    nếu is_prime[p] == true:
        for i từ p * p đến N, mỗi bước tăng p:
            is_prime[i] = false
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_N = 10000000;
vector<bool> is_prime(MAX_N + 1, true);

void sieve() {
    is_prime[0] = is_prime[1] = false;
    for (int p = 2; p * p <= MAX_N; p++) {
        if (is_prime[p]) {
            for (int i = p * p; i <= MAX_N; i += p) {
                is_prime[i] = false;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve();

    int q;
    if (!(cin >> q)) return 0;

    while (q--) {
        int x;
        cin >> x;
        if (is_prime[x]) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Chi tiết | Lý do |
|---|---|
| `i = p * p` | Các bội nhỏ hơn ($2p, 3p$) đã bị các số $2, 3$ gạch từ trước, bắt đầu từ $p \times p$ giúp tiết kiệm thời gian. |
| `vector<bool>` | Mỗi phần tử chỉ tốn 1 bit, $10^7$ phần tử chỉ tốn $\approx 1.2\text{ MB}$ RAM. |

#### Tự kiểm tra

1. Vì sao vòng lặp ngoài chỉ cần chạy đến $p \times p \le N$?
2. Sàng Eratosthenes cho $N = 10^7$ mất bao lâu để hoàn thành? (Đáp án: $\approx 0.08$ giây).

#### Luyện tập ngắn

- **LT 3.6A:** In ra toàn bộ số nguyên tố trong đoạn $[1, N]$ với $N \le 10^6$.
- **LT 3.6B:** Đếm số lượng số nguyên tố trong đoạn $[L, R]$ với $1 \le L \le R \le 10^6$.

#### Tóm tắt bài

Sàng Eratosthenes là thuật toán tiền xử lý số nguyên tố kinh điển $\mathcal{O}(N \log \log N)$. Sau khi sàng, việc kiểm tra nguyên tố chỉ tốn $\mathcal{O}(1)$.

---

### Bài 3.7 — Ôn tập, kiểm tra và bài chuyển giao

#### Mục tiêu bài

Bài này giúp em củng cố toàn bộ kỹ năng số học từ cơ bản đến nâng cao. Mỗi bài tập tập trung vào việc áp dụng đúng công thức và xử lý số lớn an toàn.

#### Tầng A — Củng cố nền tảng

##### Bài 3.7.1 — Tính tổng các ước
Đọc số nguyên dương $N$ ($1 \le N \le 10^9$). Tính tổng tất cả các ước nguyên dương của $N$.
- **Input:** Một số nguyên $N$.
- **Output:** Tổng các ước nguyên dương của $N$.
- **Ví dụ:** `12` $\implies$ Output: `28` (vì $1 + 2 + 3 + 4 + 6 + 12 = 28$).

##### Bài 3.7.2 — Ước chung lớn nhất của hai số lớn
Cho hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^{18}$). Tìm $\gcd(A, B)$.
- **Input:** Hai số nguyên $A$ và $B$.
- **Output:** Giá trị $\gcd(A, B)$.
- **Ví dụ:** `1000000000000 250000000000` $\implies$ Output: `250000000000`.

##### Bài 3.7.3 — Kiểm tra nhiều số nguyên tố
Cho $T$ số nguyên dương $N$ ($T \le 100, N \le 10^{12}$). Với mỗi số, kiểm tra xem có phải số nguyên tố không.
- **Input:** Dòng đầu ghi $T$. $T$ dòng sau, mỗi dòng ghi một số $N$.
- **Output:** In `YES` nếu là số nguyên tố, ngược lại in `NO`.
- **Ví dụ:** `17` cho `YES`; `1` cho `NO`.

##### Bài 3.7.4 — Tổng chữ số nguyên tố
Cho số nguyên dương $N$ ($1 \le N \le 10^{18}$). Kiểm tra xem tổng các chữ số của $N$ có phải là số nguyên tố hay không.
- **Input:** Số nguyên $N$.
- **Output:** In `YES` hoặc `NO`.
- **Ví dụ:** `124` $\implies$ Output: `YES` (vì $1 + 2 + 4 = 7$).

---

#### Tầng B — Vận dụng mẫu

##### Bài 3.7.5 — Số bán nguyên tố (Semi-Prime)
Số bán nguyên tố là số bằng tích của đúng hai số nguyên tố (ví dụ $4 = 2 \times 2, 6 = 2 \times 3$). Kiểm tra xem $N$ ($1 \le N \le 10^9$) có phải là số bán nguyên tố không.
- **Input:** Số nguyên $N$.
- **Output:** In `YES` hoặc `NO`.
- **Ví dụ:** `6` cho `YES`; `8` cho `NO` (vì $8 = 2^3$, có 3 thừa số).

##### Bài 3.7.6 — Rút gọn dãy phân số
Cho $N$ cặp số nguyên dương $A_i, B_i$ ($N \le 10^5, A_i, B_i \le 10^9$). Rút gọn từng phân số $\frac{A_i}{B_i}$ về dạng tối giản $\frac{P_i}{Q_i}$.
- **Input:** Dòng đầu ghi $N$. $N$ dòng sau, mỗi dòng ghi $A_i, B_i$.
- **Output:** Ghi $N$ dòng, mỗi dòng chứa hai số $P_i, Q_i$.

##### Bài 3.7.7 — Đếm cặp nguyên tố cùng nhau
Cho dãy $N$ số nguyên ($N \le 2000, A_i \le 10^9$). Đếm số cặp $(i, j)$ với $1 \le i < j \le N$ thỏa mãn $\gcd(A_i, A_j) = 1$.
- **Input:** Dòng 1 ghi $N$. Dòng 2 ghi $N$ số $A_i$.
- **Output:** Số lượng cặp nguyên tố cùng nhau.

##### Bài 3.7.8 — Tìm số nhỏ nhất có đúng K ước
Cho số nguyên $K$ ($1 \le K \le 30$). Tìm số nguyên dương $N$ nhỏ nhất có đúng $K$ ước số nguyên dương.
- **Input:** Số nguyên $K$.
- **Output:** Số $N$ nhỏ nhất tìm được.
- **Ví dụ:** `3` $\implies$ Output: `4` (ước là 1, 2, 4).

---

#### Tầng C — Chuyển giao

##### Bài 3.7.9 — Bội chung nhỏ nhất của dãy số
Cho $N$ số nguyên $A_1, A_2, \dots, A_N$ ($N \le 100, A_i \le 1000$). Tính $\text{lcm}(A_1, \dots, A_N) \pmod{10^9+7}$.
- **Gợi ý:** Phân tích từng số ra thừa số nguyên tố, lấy số mũ lớn nhất của mỗi thừa số trên toàn dãy.

##### Bài 3.7.10 — Đếm số chữ số 0 tận cùng của N!
Cho số nguyên dương $N$ ($1 \le N \le 10^{18}$). Đếm số chữ số 0 liên tiếp ở tận cùng của $N!$.
- **Gợi ý:** Áp dụng định lý Legendre tính số mũ của thừa số 5 trong $N!$: $\lfloor N/5 \rfloor + \lfloor N/25 \rfloor + \dots$
- **Ví dụ:** `10` $\implies$ Output: `2`.

##### Bài 3.7.11 — Khôi phục hai số từ GCD và LCM
Cho $G = \gcd(A, B)$ và $L = \text{lcm}(A, B)$ ($G, L \le 10^{12}$). Tìm hai số nguyên dương $A \le B$ sao cho $A + B$ nhỏ nhất. Nếu không tồn tại, in `-1`.
- **Ví dụ:** `2 60` $\implies$ Output: `10 12`.

##### Bài 3.7.12 — Sàng nguyên tố hàng loạt
Cài đặt Sàng Eratosthenes cho $10^7$ số và trả lời $Q$ truy vấn kiểm tra số nguyên tố ($Q \le 10^6$).
- **Input:** Dòng đầu ghi $Q$. $Q$ dòng sau, mỗi dòng ghi một số $x \le 10^7$.
- **Output:** Với mỗi truy vấn, in `1` nếu là số nguyên tố, ngược lại in `0`.

---

#### Phiếu tự đánh giá

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Tìm ước trong $\mathcal{O}(\sqrt{N})$ |  |  |  |
| Cài đặt thuật toán Euclid tìm GCD |  |  |  |
| Tính LCM an toàn (chia trước nhân) |  |  |  |
| Kiểm tra số nguyên tố tối ưu $6k \pm 1$ |  |  |  |
| Phân tích thừa số nguyên tố bằng chia dần |  |  |  |
| Cài đặt Sàng Eratosthenes $\mathcal{O}(N \log \log N)$ |  |  |  |
| Xử lý số lớn $10^{18}$ với `long long` |  |  |  |

#### Tiêu chí hoàn thành chương

Em có thể xem mình đã nắm chắc chương khi:
1. Giải thích được vì sao chỉ cần duyệt đến $\sqrt{N}$ để tìm ước và kiểm tra nguyên tố.
2. Viết được hàm `gcd` và `lcm` an toàn không quá 5 dòng code.
3. Cài đặt được Sàng Eratosthenes từ trí nhớ trong 2 phút.
4. Không mắc bẫy tràn số khi làm việc với số nguyên $10^9 \to 10^{18}$.

---

### Tổng kết chương

> **Số học là nền tảng của các thuật toán tối ưu. Nắm vững tính chất đối xứng $\sqrt{N}$, thuật toán Euclid và Sàng Eratosthenes giúp em biến những bài toán duyệt hàng triệu số phức tạp thành những câu lệnh chớp nhoáng.**

| Cần nhớ | Nội dung |
|---|---|
| Tập ước số | Duyệt $d \times d \le N$, mỗi lần lấy cặp $(d, N/d)$ với $\mathcal{O}(\sqrt{N})$ |
| Thuật toán Euclid | $\gcd(a, b) = \gcd(b, a \% b)$ với $\mathcal{O}(\log(\min(A, B)))$ |
| Quy tắc an toàn LCM | $\text{lcm}(a, b) = (a / \gcd(a, b)) \times b$ (chia trước khi nhân) |
| Số nguyên tố | Số $> 1$ chỉ có 2 ước; kiểm tra chia hết từ $2$ đến $\sqrt{N}$ bước nhảy $6k \pm 1$ |
| Thừa số nguyên tố | Chia dần cho $p$ từ $2$ đến $\sqrt{N}$; nếu sau cùng $N > 1$ thì $N$ là thừa số cuối |
| Sàng Eratosthenes | Gạch bội số bắt đầu từ $p \times p$ với $\mathcal{O}(N \log \log N)$ |

#### Những lỗi thường gặp

| Lỗi | Cách tự kiểm tra |
|---|---|
| Tràn số khi tính tích trong LCM | Luôn lấy `(a / gcd(a, b)) * b` |
| Quên trường hợp $N = 0, 1$ khi kiểm tra nguyên tố | Luôn chặn `if (n < 2) return false;` đầu tiên |
| Bỏ sót ước nguyên tố cuối cùng sau vòng lặp $\sqrt{N}$ | Luôn kiểm tra `if (n > 1)` sau vòng lặp |
| Dùng `int` cho biến lặp `d * d <= n` | Khi $N = 10^{12}$, biến lặp $d$ phải là `long long` |
| Tràn mảng trong Sàng Eratosthenes | Khai báo kích thước mảng là `MAX_N + 1` |

---

### Code tham chiếu

```cpp
#include <bits/stdc++.h>
using namespace std;

// 1. Uoc chung lon nhat (Euclid)
long long gcd(long long a, long long b) {
    while (b != 0) {
        long long r = a % b;
        a = b;
        b = r;
    }
    return a;
}

// 2. Boi chung nho nhat an toan (Chia truoc khi nhan)
long long lcm(long long a, long long b) {
    if (a == 0 || b == 0) return 0;
    return (a / gcd(a, b)) * b;
}

// 3. Kiem tra so nguyen to toi uu O(sqrt(N)) buoc nhay 6k +- 1
bool isPrime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) {
            return false;
        }
    }
    return true;
}

// 4. Sang so nguyen to Eratosthenes O(N log log N)
const int MAX_VAL = 1000000;
vector<bool> is_prime_sieve(MAX_VAL + 1, true);

void sieve() {
    is_prime_sieve[0] = is_prime_sieve[1] = false;
    for (int p = 2; p * p <= MAX_VAL; p++) {
        if (is_prime_sieve[p]) {
            for (int i = p * p; i <= MAX_VAL; i += p) {
                is_prime_sieve[i] = false;
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    sieve();

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << "GCD: " << gcd(a, b) << "\n";
    cout << "LCM: " << lcm(a, b) << "\n";
    cout << "a is Prime: " << (isPrime(a) ? "YES" : "NO") << "\n";
    cout << "b is Prime: " << (isPrime(b) ? "YES" : "NO") << "\n";

    return 0;
}
```
