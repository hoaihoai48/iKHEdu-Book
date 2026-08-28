# TÀI LIỆU GỐC — CHƯƠNG 3: SỐ HỌC CƠ BẢN (NUMBER THEORY)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững các khái niệm ước, bội, ước chung lớn nhất (GCD), bội chung nhỏ nhất (LCM), số nguyên tố và phân tích thừa số nguyên tố; áp dụng giải các bài toán tối ưu và kiểm tra tính chất số trong tin học |
| Kiến thức cần có | Vòng lặp `for`/`while`, câu lệnh điều kiện `if-else`, toán tử chia dư `%`, hàm (`function`), kiểu dữ liệu `long long` |
| Phạm vi | Ước và bội, thuật toán Euclid tìm GCD, tính LCM an toàn (chống tràn số), kiểm tra số nguyên tố tối ưu $\mathcal{O}(\sqrt{N})$, phân tích thừa số nguyên tố, sàng số nguyên tố cơ bản |
| Số bài | 5 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Tìm tập các ước và đếm số ước của một số nguyên dương trong thời gian tối ưu $\mathcal{O}(\sqrt{N})$ — `LO-01`.
2. Trình bày và cài đặt thuật toán Euclid tìm ước chung lớn nhất (GCD) của hai hoặc nhiều số — `LO-02`.
3. Tính bội chung nhỏ nhất (LCM) một cách an toàn bằng quy tắc "chia trước khi nhân" chống tràn số — `LO-03`.
4. Kiểm tra một số nguyên có phải số nguyên tố trong $\mathcal{O}(\sqrt{N})$ — `LO-04`.
5. Thực hiện phân tích một số nguyên dương thành tích các thừa số nguyên tố — `LO-05`.
6. Nhận biết và xử lý chính xác các trường hợp biên: $N = 0, 1$, số âm, số nguyên lớn vượt kiểu `int` — `LO-06`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để kiểm tra và phân tích tính chất chia hết của một số nguyên lớn mà không cần duyệt qua từng số từ $1$ đến $N$?**

---

### Bài 3.1 — Ước, bội và cách tìm ước tối ưu $\mathcal{O}(\sqrt{N})$

#### 1. Khái niệm & Ý tưởng tối ưu $\mathcal{O}(\sqrt{N})$
- Số nguyên dương $d$ được gọi là **ước** của số nguyên dương $N$ nếu phép chia $N$ cho $d$ không có dư ($N \% d == 0$). Khi đó, $N$ được gọi là **bội** của $d$.
- **Cách làm ngây thơ ($\mathcal{O}(N)$):** Duyệt biến $i$ từ $1$ đến $N$. Nếu $N \% i == 0$ thì $i$ là ước. Cách này sẽ bị quá thời gian (Time Limit Exceeded) khi $N = 10^9$ ($10^9$ phép tính mất $\approx 10$ giây).
- **Quy luật đối xứng cặp ước:** Nếu $d$ là một ước của $N$ thì thương số $N / d$ cũng chắc chắn là một ước của $N$.
  - Ví dụ với $N = 36$: Các cặp ước là $(1, 36), (2, 18), (3, 12), (4, 9), (6, 6)$.
  - Nhận xét: Trong mỗi cặp ước $(d, N/d)$, ước nhỏ hơn $d$ luôn thỏa mãn $d \le \sqrt{N}$.
  - **Thuật toán tối ưu:** Chỉ cần duyệt $d$ từ $1$ đến $\lfloor\sqrt{N}\rfloor$ (tức là $d \times d \le N$). Với mỗi ước $d$, ta thu được đồng thời cả 2 ước là $d$ và $N/d$ (nếu $d \ne N/d$). Độ phức tạp giảm xuống $\mathcal{O}(\sqrt{N})$, khi $N = 10^9$ chỉ cần tối đa $\approx 31.622$ phép tính (chưa tới $0.001$ giây).

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 3.1: Phân Chia Kiện Hàng Logistics Cảng Hải Phòng**  
> **Bối cảnh:** Tại Trung tâm Logistics Cảng Hải Phòng, một lô hàng gồm $N$ container hàng hóa tiêu chuẩn cần được chia đều vào các kho bãi lưu trữ tạm thời sao cho mỗi kho chứa đúng cùng một số lượng container nguyên vẹn.  
> **Nhiệm vụ:** Là chuyên viên điều phối kho bãi, em cần xác định tổng số phương án chia kho hợp lệ (tương ứng số lượng ước số của $N$) và liệt kê kích thước của tất cả các kho có thể thiết lập theo thứ tự tăng dần.  
> 
> **Input:**  
> - Một dòng duy nhất chứa số nguyên dương $N$ ($1 \le N \le 10^{12}$).  
> 
> **Output:**  
> - Dòng 1: Ghi số lượng phương án chia kho hợp lệ.  
> - Dòng 2: Ghi danh sách kích thước các kho theo thứ tự tăng dần, cách nhau bởi một khoảng trắng.  
> 
> **Sample:**  
> - **Input:** `36`  
> - **Output:**  
>   `9`  
>   `1 2 3 4 6 9 12 18 36`  
> - **Giải thích:** Có 9 phương án chia 36 container: chia thành 1 kho 36 cont, 2 kho 18 cont, ..., hoặc 36 kho 1 cont.

#### Phân tích I-P-O:
- **Input:** $N \le 10^{12}$ (bắt buộc dùng kiểu `long long`).
- **Process:** Duyệt $d$ từ $1$ đến $\sqrt{N}$ ($d \times d \le N$). Lưu $d$ và $N/d$ vào `vector<long long> divisors`, sắp xếp tăng dần.
- **Output:** In `divisors.size()` và toàn bộ mảng ước.

#### Cài đặt C++
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

    cout << divisors.size() << "\n";
    for (int i = 0; i < (int)divisors.size(); i++) {
        cout << divisors[i] << (i + 1 == (int)divisors.size() ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

---

#### 3. Bẫy lỗi thường gặp
| Lỗi | Hậu quả | Cách tự kiểm tra |
|---|---|---|
| Dùng `d <= sqrt(n)` trong vòng lặp | Gọi hàm `sqrt()` nhiều lần làm chậm chương trình và có thể sai số thực | Thay bằng `d * d <= n` |
| Quên kiểm tra $d \ne N/d$ với số chính phương | Ước $\sqrt{N}$ bị thêm 2 lần vào danh sách (ví dụ số 36 bị thêm hai số 6) | Luôn có điều kiện `if (d * d != n)` trước khi thêm `n / d` |
| Tràn số ở điều kiện `d * d <= n` khi dùng `int` | Với $N = 10^{12}$, `d` chạy tới $10^6$, `d * d` vẫn vừa `long long` nhưng nếu khai báo `int d` thì `d * d` sẽ bị tràn | Khai báo `long long d` cho vòng lặp |

---

#### 4. Bài tập thực hành Bài 3.1

##### Bài 3.1.1 — Kiểm Định Viên Kim Cương Hoàn Hảo
- **Bối cảnh:** Trong ngành chế tác đá quý, một khối kim cương nhân tạo có mã định danh nguyên dương $N$ được chứng nhận đạt chuẩn "Cấu trúc hoàn hảo" nếu tổng tất cả các trọng số thành phần (là các ước nguyên dương thực sự nhỏ hơn $N$) bằng chính giá trị $N$.
- **Nhiệm vụ:** Cho mã số $N$, hãy in `YES` nếu khối kim cương đạt chuẩn hoàn hảo, ngược lại in `NO`.
- **Input:** Một số nguyên $N$ ($1 \le N \le 10^9$).
- **Output:** In `YES` hoặc `NO`.
- **Sample:** `6` $\implies$ **Output:** `YES` (ước nhỏ hơn 6 là 1, 2, 3 có tổng $1 + 2 + 3 = 6$).

##### Bài 3.1.2 — Tra Cứu Mã Vận Đơn Viettel Post
- **Bối cảnh:** Trung tâm khai thác bưu chính Viettel Post tiếp nhận $Q$ bưu kiện. Mỗi bưu kiện có mã kiểm tra $N$. Hệ thống cần biết số lượng ước của $N$ để phân làn xử lý tự động.
- **Input:** Dòng 1 ghi số truy vấn $Q$ ($1 \le Q \le 1000$). $Q$ dòng tiếp theo, mỗi dòng chứa một mã số $N$ ($1 \le N \le 10^9$).
- **Output:** Với mỗi truy vấn, in ra số lượng ước nguyên dương của $N$ trên một dòng.
- **Sample:**  
  `2`  
  `12`  
  `7`  
  $\implies$ **Output:**  
  `6`  
  `2`

---

### Bài 3.2 — Ước chung lớn nhất (GCD) và Thuật toán Euclid

#### 1. Khái niệm & Thuật toán Euclid
- **Ước chung lớn nhất (GCD - Greatest Common Divisor):** $\gcd(a, b)$ là số nguyên dương lớn nhất vừa là ước của $a$, vừa là ước của $b$.
- **Định lý Euclid:** $\gcd(a, b) = \gcd(b, a \% b)$ với điều kiện dừng $\gcd(a, 0) = a$.
- **Độ phức tạp:** Mỗi bước chia lấy dư, số dư giảm đi ít nhất một nửa $\implies \mathcal{O}(\log(\min(a, b)))$. Với hai số $10^{18}$, thuật toán Euclid chỉ mất chưa tới $60$ phép chia dư!

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 3.2: Tối Giản Tỷ Lệ Pha Chế Dược Phẩm Long Châu**  
> **Bối cảnh:** Chuỗi nhà thuốc FPT Long Châu nghiên cứu công thức dung dịch kháng khuẩn mới. Tỷ lệ thể tích giữa hai dung môi $A$ và $B$ hiện đang là $\frac{A}{B}$.  
> **Nhiệm vụ:** Để đưa vào dây chuyền đóng chai tự động, em cần rút gọn tỷ lệ $\frac{A}{B}$ về dạng phân số tối giản $\frac{P}{Q}$ ($P, Q$ nguyên dương, $\gcd(P, Q) = 1$).  
> 
> **Input:**  
> - Một dòng chứa hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^{18}$).  
> 
> **Output:**  
> - Ghi hai số nguyên $P$ và $Q$ cách nhau bởi một khoảng trắng.  
> 
> **Sample:** `12 18` $\implies$ **Output:** `2 3`.  
> **Giải thích:** $\gcd(12, 18) = 6 \implies P = 12 / 6 = 2, Q = 18 / 6 = 3$.

#### Cài đặt C++
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
    cout << a / g << " " << b / g << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 3.2

##### Bài 3.2.1 — Đồng Bộ Nhịp Đèn Cảnh Báo Sân Bay
- **Bối cảnh:** Tại Cảng hàng không Quốc tế Long Thành, hệ thống an toàn đường băng có $N$ cột đèn tín hiệu chớp tắt theo chu kỳ độc lập. Cột đèn thứ $i$ phát tín hiệu chớp sáng sau mỗi $A_i$ mili-giây ($1 \le i \le N$).
- **Nhiệm vụ:** Tìm khoảng thời gian lớn nhất $G$ (mili-giây) sao cho mọi chu kỳ đèn $A_i$ đều là bội số nguyên lần của $G$, nhằm thiết lập xung nhịp đồng hồ chủ (Master Clock) cho toàn bộ hệ thống.
- **Input:** Dòng 1 ghi $N$ ($1 \le N \le 10^5$). Dòng 2 ghi $N$ số nguyên $A_1, A_2, \dots, A_N$ ($1 \le A_i \le 10^9$).
- **Output:** Ghi một số nguyên duy nhất là $\gcd(A_1, A_2, \dots, A_N)$.
- **Sample:** `4` \ `24 36 60 48` $\implies$ **Output:** `12`

##### Bài 3.2.2 — Cặp Tần Số Không Giao Thoa VinaPhone
- **Bối cảnh:** Nhà mạng VinaPhone phân bổ $N$ kênh tần số viễn thông $A_1, A_2, \dots, A_N$. Hai kênh tần số $A_i$ và $A_j$ ($i < j$) được xem là "hoàn toàn không gây nhiễu chéo" nếu chúng nguyên tố cùng nhau ($\gcd(A_i, A_j) = 1$).
- **Nhiệm vụ:** Đếm tổng số cặp kênh tần số $(i, j)$ không gây nhiễu chéo.
- **Input:** Dòng 1 ghi $N$ ($1 \le N \le 2000$). Dòng 2 ghi $N$ số nguyên $A_i$ ($1 \le A_i \le 10^9$).
- **Output:** Ghi số lượng cặp thỏa mãn.
- **Sample:** `3` \ `2 3 4` $\implies$ **Output:** `2` (các cặp (2, 3) và (3, 4)).

---

### Bài 3.3 — Bội chung nhỏ nhất (LCM) và Kỹ thuật chống tràn số

#### 1. Khái niệm & Quy tắc an toàn (Safe LCM)
- **Bội chung nhỏ nhất (LCM - Least Common Multiple):** $\text{lcm}(a, b)$ là số nguyên dương nhỏ nhất chia hết cho cả $a$ và $b$.
- **Mối liên hệ giữa GCD và LCM:**  
  $$a \times b = \gcd(a, b) \times \text{lcm}(a, b) \implies \text{lcm}(a, b) = \frac{a \times b}{\gcd(a, b)}$$
- **Bẫy tràn số cực kỳ nguy hiểm:**  
  Nếu ta tính `(a * b) / gcd(a, b)`, tích `a * b` có thể lên tới $10^9 \times 10^9 = 10^{18}$ (hoặc vượt $10^{18}$ nếu $a, b > 10^9$) gây tràn số nguyên!
- **Quy tắc vàng: Chia trước khi Nhân:**  
  ```cpp
  long long lcm(long long a, long long b) {
      return (a / gcd(a, b)) * b;
  }
  ```

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 3.3: Lịch Trình Giao Nhau Của Tuyến Bus Điện VinBus**  
> **Bối cảnh:** Hệ thống xe bus điện thông minh VinBus có 2 tuyến xe cùng xuất phát từ Trạm trung chuyển Grand Park lúc 06:00 sáng. Tuyến 1 hoàn thành 1 vòng lộ trình trong $A$ phút, Tuyến 2 hoàn thành 1 vòng trong $B$ phút.  
> **Nhiệm vụ:** Tìm khoảng thời gian ngắn nhất sau bao nhiêu phút thì cả hai xe bus lại cùng lúc quay trở về trạm xuất phát lần đầu tiên.  
> **Input:** Hai số nguyên dương $A$ và $B$ ($1 \le A, B \le 10^9$).  
> **Output:** Ghi một số nguyên duy nhất là thời gian gặp nhau $\text{lcm}(A, B)$.  
> **Sample:** `12 18` $\implies$ **Output:** `36`.

#### Cài đặt C++
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
    return (a / gcd(a, b)) * b; // Chia trước khi nhân
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b;
    if (!(cin >> a >> b)) return 0;

    cout << lcm(a, b) << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 3.3

##### Bài 3.3.1 — Chu Kỳ Vận Hành Dây Chuyền VinFast
- **Bối cảnh:** Dây chuyền dập khung xe tự động của nhà máy ô tô VinFast gồm 3 cánh tay robot $R_1, R_2, R_3$ có chu kỳ bảo trì định kỳ lần lượt là $A, B, C$ giờ.
- **Nhiệm vụ:** Tìm thời điểm sớm nhất (tính theo giờ) sau khi vận hành mà cả 3 robot đều cùng lúc bước vào kỳ bảo trì.
- **Input:** Ba số nguyên dương $A, B, C$ ($1 \le A, B, C \le 10^6$).
- **Output:** In $\text{lcm}(A, B, C)$.
- **Sample:** `4 6 8` $\implies$ **Output:** `24`

##### Bài 3.3.2 — Đóng Thùng Nông Sản Xuất Khẩu
- **Bối cảnh:** Công ty xuất khẩu trái cây đóng sầu riêng vào các thùng tiêu chuẩn. Biết rằng số lượng quả sầu riêng $N$ khi đóng vào các loại thùng chứa 6 quả, 8 quả hay 10 quả đều vừa vặn không thừa quả nào.
- **Nhiệm vụ:** Tìm số lượng quả sầu riêng $N$ nhỏ nhất ($N > 0$).
- **Output:** Ghi một số nguyên duy nhất.
- **Sample Output:** `120`

---

### Bài 3.4 — Số nguyên tố và Kỹ thuật kiểm tra tối ưu $\mathcal{O}(\sqrt{N})$

#### 1. Định nghĩa & Thuật toán kiểm tra
- **Số nguyên tố:** Là số nguyên $> 1$ chỉ có đúng $2$ ước nguyên dương là $1$ và chính nó ($2, 3, 5, 7, 11, 13, 17, 19, \dots$).
- **Tối ưu $\mathcal{O}(\sqrt{N})$:** Nếu $N$ là hợp số thì $N$ phải có ít nhất một ước $d$ thỏa mãn $2 \le d \le \sqrt{N}$. Do đó, chỉ cần kiểm tra xem $N$ có chia hết cho số nào từ $2$ đến $\sqrt{N}$ không.

---

#### 2. Hàm kiểm tra số nguyên tố chuẩn mẫu

```cpp
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
```

---

#### 3. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 3.4: Mã Hóa Khóa Bảo Mật Giao Dịch VietinBank**  
> **Bối cảnh:** Hệ thống thanh toán trực tuyến Ngân hàng TMCP Công Thương Việt Nam (VietinBank) sử dụng các số nguyên tố trong dải $[L, R]$ để sinh khóa phiên bảo mật SSL/TLS.  
> **Nhiệm vụ:** Hãy đếm xem có bao nhiêu khóa nguyên tố hợp lệ nằm trong dải số $[L, R]$.  
> **Input:** Hai số nguyên $L$ và $R$ ($1 \le L \le R \le 10^{12}, R - L \le 10^5$).  
> **Output:** Ghi số lượng số nguyên tố trong đoạn $[L, R]$.  
> **Sample:** `10 20` $\implies$ **Output:** `4` (gồm 11, 13, 17, 19).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

bool isPrime(long long n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == 0) return false;
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long l, r;
    if (!(cin >> l >> r)) return 0;

    int countPrime = 0;
    for (long long x = l; x <= r; x++) {
        if (isPrime(x)) {
            countPrime++;
        }
    }

    cout << countPrime << "\n";

    return 0;
}
```

---

#### 4. Bài tập thực hành Bài 3.4

##### Bài 3.4.1 — Tìm Cổng Kết Nối Khả Dụng Tiếp Theo
- **Bối cảnh:** Máy chủ trung tâm cần mở cổng dịch vụ bảo mật có số hiệu là số nguyên tố nhỏ nhất lớn hơn hoặc bằng cổng $N$ được yêu cầu.
- **Input:** Số nguyên $N$ ($2 \le N \le 10^9$).
- **Output:** Ghi số nguyên tố tìm được.
- **Sample:** `14` $\implies$ **Output:** `17`

##### Bài 3.4.2 — Mã Pin Thẻ ATM Thuần Nguyên Tố
- **Bối cảnh:** Ngân hàng phát hành mã PIN đặc biệt gồm các số "Thuần nguyên tố": bản thân số đó là số nguyên tố và mọi chữ số cấu thành của nó cũng đều là số nguyên tố (thuộc tập $\{2, 3, 5, 7\}$).
- **Input:** Số nguyên $N$ ($1 \le N \le 10^9$).
- **Output:** In `YES` nếu $N$ là số thuần nguyên tố, ngược lại in `NO`.
- **Sample:** `23` $\implies$ **Output:** `YES`

---

### Bài 3.5 — Phân tích thừa số nguyên tố

#### 1. Khái niệm & Thuật toán
- **Định lý cơ bản của số học:** Mọi số nguyên $N > 1$ đều có thể biểu diễn duy nhất dưới dạng tích các lũy thừa của thừa số nguyên tố:
  $$N = p_1^{e_1} \times p_2^{e_2} \times \dots \times p_k^{e_k}$$
  (Ví dụ: $60 = 2^2 \times 3^1 \times 5^1$).
- **Thuật toán chia dần $\mathcal{O}(\sqrt{N})$:**
  1. Duyệt $p$ từ $2$ đến $\sqrt{N}$.
  2. Nếu $N \% p == 0$, ta đếm số mũ $e$ bằng cách chia liên tục $N$ cho $p$ trong khi $N \% p == 0$.
  3. Sau khi duyệt hết đến $\sqrt{N}$, nếu phần dư của $N$ vẫn còn $> 1$ thì giá trị $N$ còn lại chính là một thừa số nguyên tố cuối cùng với số mũ $1$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 3.5: Phân Rã Khóa Mã Hóa RSA Thành Thừa Số**  
> **Bối cảnh:** Trong giải mã hệ mật mã bất đối xứng RSA, một modulo mã hóa $N$ được tạo thành từ tích các số nguyên tố.  
> **Nhiệm vụ:** Em hãy viết chương trình phân tích số nguyên $N$ ra tích các thừa số nguyên tố theo chuẩn $p_1\text{\textasciicircum}e_1 * p_2\text{\textasciicircum}e_2 \dots$  
> **Input:** Số nguyên dương $N$ ($2 \le N \le 10^{12}$).  
> **Output:** Chuỗi phân tích thừa số nguyên tố.  
> **Sample:** `60` $\implies$ **Output:** `2^2 * 3^1 * 5^1`.

#### Cài đặt C++
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
    cout << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 3.5

##### Bài 3.5.1 — Ước Nguyên Tố Mạnh Nhất
- **Bối cảnh:** Trong mật mã học, độ an toàn của khóa phụ thuộc vào ước nguyên tố lớn nhất của nó. Hãy tìm ước nguyên tố lớn nhất của số $N \le 10^{12}$.
- **Input:** `100` $\implies$ **Output:** `5`

##### Bài 3.5.2 — Đếm Số Ước Bằng Phân Tích Thừa Số
- **Bối cảnh:** Dựa vào công thức: nếu $N = p_1^{e_1} \dots p_k^{e_k}$ thì tổng số ước của $N$ là $(e_1 + 1)\dots(e_k + 1)$. Tính số lượng ước của số cực lớn $N \le 10^{14}$.
- **Input:** `60` $\implies$ **Output:** `12`

---

### Bài 3.6 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)

##### Bài 3.6.1 — Thống Kê Điểm Thưởng Nền Tảng Học Tập iKHEDU
- **Bối cảnh:** Hệ thống học tập trực tuyến iKHEDU trao điểm thưởng $N$ cho học viên xuất sắc. Học viên được nhận thêm số quà bằng tổng tất cả các ước nguyên dương của $N$.
- **Nhiệm vụ:** Tính tổng tất cả các ước nguyên dương của $N$ ($1 \le N \le 10^9$).
- **Sample:** `12` $\implies$ **Output:** `28` ($1+2+3+4+6+12 = 28$).
- 💡 **Góc kiến thức:** Hàm tổng các ước $\sigma(N)$ là một trong những hàm nhân tính quan trọng nhất của lý thuyết số.

##### Bài 3.6.2 — Đồng Bộ Nhịp Băng Chuyền Cảng Cát Lái
- **Bối cảnh:** Hai hệ thống băng chuyền bốc dỡ hàng tại Cảng Cát Lái có chu kỳ vận hành $A$ và $B$ pico-giây ($A, B \le 10^{18}$).
- **Nhiệm vụ:** Tìm chu kỳ xung nhịp chung lớn nhất $\gcd(A, B)$.
- **Sample:** `1000000000000 250000000000` $\implies$ **Output:** `250000000000`.

##### Bài 3.6.3 — Kiểm Tra Tường Lửa Đám Mây Viettel Cloud
- **Bối cảnh:** Tường lửa Viettel Cloud quét $T$ gói tin đến. Gói tin có mã định danh $N$ được cho phép vượt qua nếu $N$ là một số nguyên tố.
- **Input:** Dòng 1 ghi $T$ ($1 \le T \le 100$). $T$ dòng sau, mỗi dòng chứa $N$ ($1 \le N \le 10^{12}$).
- **Output:** In `YES` nếu là số nguyên tố, ngược lại in `NO`.

##### Bài 3.6.4 — Mã Định Danh Căn Cước Công Dân May Mắn
- **Bối cảnh:** Một số CCCD được xem là mang lại may mắn nếu tổng các chữ số của nó là một số nguyên tố.
- **Input:** Số nguyên $N$ ($1 \le N \le 10^{18}$).
- **Output:** In `YES` nếu tổng chữ số là số nguyên tố, ngược lại in `NO`.

---

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)

##### Bài 3.6.5 — Xác Thực Khóa Bán Nguyên Tố (Semi-Prime Security)
- **Bối cảnh:** Một khóa bảo mật được gọi là "Bán nguyên tố" nếu nó được tạo thành từ tích của đúng hai số nguyên tố (có thể trùng nhau, ví dụ $4 = 2 \times 2, 6 = 2 \times 3, 9 = 3 \times 3$).
- **Nhiệm vụ:** Kiểm tra số $N$ ($1 \le N \le 10^9$) có phải là số bán nguyên tố không.
- **Sample:** `6` $\implies$ `YES`, `8` $\implies$ `NO` (vì $8 = 2^3$, có 3 thừa số).

##### Bài 3.6.6 — Tối Giản Dãy Tỷ Lệ Giao Dịch Chứng Khoán
- **Bối cảnh:** Sàn giao dịch chứng khoán HOSE ghi nhận $N$ tỷ lệ giá trị cổ phiếu dạng $\frac{A_i}{B_i}$.
- **Nhiệm vụ:** Rút gọn toàn bộ $N$ phân số về dạng tối giản trong thời gian tối ưu.
- **Giới hạn:** $N \le 10^5, A_i, B_i \le 10^9$.

##### Bài 3.6.7 — Mạng Lưới Cảm Biến Không Nhiễu Sóng
- **Bối cảnh:** Một mạng lưới gồm $N$ cảm biến IoT có tần số $A_1, A_2, \dots, A_N$.
- **Nhiệm vụ:** Đếm số cặp cảm biến $(i, j)$ với $i < j$ hoạt động không gây nhiễu ($\gcd(A_i, A_j) = 1$).
- **Giới hạn:** $N \le 2000, A_i \le 10^9$.

##### Bài 3.6.8 — Thiết Kế Hộp Quà Có Đúng K Cách Chia
- **Bối cảnh:** Cửa hàng lưu niệm muốn đóng một gói quà gồm $N$ món đồ sao cho số lượng cách chia đều gói quà vào các hộp nhỏ đúng bằng $K$ cách (tức là $N$ có đúng $K$ ước số).
- **Nhiệm vụ:** Tìm số nguyên dương $N$ nhỏ nhất có đúng $K$ ước số ($1 \le K \le 30$).
- **Sample:** `3` $\implies$ **Output:** `4` (vì 4 có đúng 3 ước là 1, 2, 4).

---

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)

##### Bài 3.6.9 — Bội Chung Nhỏ Nhất Của Dãy Số Modulo $10^9+7$
- **Bối cảnh:** Tính chu kỳ đồng bộ tổng thể của $N$ máy chủ vệ tinh $\text{lcm}(A_1, A_2, \dots, A_N) \pmod{10^9+7}$.
- **Phương pháp:** Phân tích từng $A_i$ ra thừa số nguyên tố, lấy số mũ cực đại của mỗi thừa số nguyên tố trên toàn dãy và tính tích theo Modulo.
- **Giới hạn:** $N \le 100, A_i \le 1000$.

##### Bài 3.6.10 — Định Lý Legendre Đếm Số Chữ Số 0 Tận Cùng Của Giai Thừa
- **Bối cảnh:** Tính số lượng chữ số $0$ liên tiếp ở tận cùng của $N!$ trong hệ thập phân.
- **Nhiệm vụ:** Áp dụng công thức Legendre tính số mũ của thừa số 5 trong $N!$: $E_5(N!) = \lfloor N/5 \rfloor + \lfloor N/25 \rfloor + \lfloor N/125 \rfloor + \dots$
- **Giới hạn:** $1 \le N \le 10^{18}$.

##### Bài 3.6.11 — Khôi Phục Kích Thước Bản Thiết Kế Từ GCD và LCM
- **Bối cảnh:** Cho biết $G = \gcd(A, B)$ và $L = \text{lcm}(A, B)$ của hai chiều dài bản thiết kế vi mạch.
- **Nhiệm vụ:** Tìm hai số nguyên dương $A$ và $B$ sao cho tổng $A + B$ đạt giá trị nhỏ nhất có thể. Nếu không tồn tại, in `-1`.
- **Giới hạn:** $1 \le G, L \le 10^{12}$.

##### Bài 3.6.12 — Sàng Nguyên Tố Eratosthenes Siêu Tốc Cho 10 Triệu Số
- **Bối cảnh:** Xây dựng mảng đánh dấu số nguyên tố từ $1$ đến $N = 10^7$ trong thời gian dưới $0.15$ giây để phục vụ truy vấn thời gian thực cho hệ thống AI.
- **Yêu cầu:** Cài đặt Sàng Eratosthenes $\mathcal{O}(N \log \log N)$ tối ưu bộ nhớ `vector<bool>` hoặc `bitset`.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Bỏ sót ước cuối cùng khi $N > 1$ sau vòng lặp thừa số | Luôn thêm `if (n > 1)` ở cuối hàm phân tích |
| Tràn số khi nhân trong LCM | Luôn chia trước khi nhân: `(a / gcd(a, b)) * b` |
| Quên xử lý $N = 0, 1$ trong hàm nguyên tố | Đặt điều kiện chặn `if (n < 2) return false;` ở dòng đầu tiên |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Cài đặt chính xác hàm tìm ước $\mathcal{O}(\sqrt{N})$, hàm `gcd` Euclid và hàm `isPrime` không lỗi tràn số. |
| **Vận dụng (Tầng B)** | Vận dụng mượt mà phân tích thừa số nguyên tố và `lcm` an toàn vào bài toán thực tế. |
| **Thành thạo (Tầng C)** | Áp dụng được công thức Legendre và tư duy phân tích thừa số nguyên tố cho số lớn. |
