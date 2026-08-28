# TÀI LIỆU GỐC — CHƯƠNG 4: ĐẾM PHÂN PHỐI

## Vai trò tài liệu

Tài liệu này là bản gốc nội dung dùng để biên soạn Chương 4 — Đếm phân phối. Nội dung được viết và review tại đây trước khi tổng hợp sang bản thảo sách. Chương này giới thiệu kỹ thuật chuyển đổi tư duy quan trọng: **thay vì so sánh vét cạn từng cặp phần tử ($\mathcal{O}(N^2)$), ta sử dụng mảng tần suất trực tiếp để giải quyết bài toán chỉ với một lần duyệt $\mathcal{O}(N)$**.

## Đối tượng và phạm vi

Tài liệu dành cho học sinh đã biết mảng 1 chiều (`vector<int>`), chỉ số mảng, vòng lặp và xâu ký tự. Phạm vi bao gồm kỹ thuật ánh xạ giá trị thành chỉ số, mảng đếm tần suất số nguyên và chữ cái, kỹ thuật đếm cặp $\mathcal{O}(N)$ và nguyên lý Dirichlet trực quan.

## Nguyên tắc biên soạn

Mỗi bài học tuân thủ chuỗi sư phạm: mục tiêu, khởi động trực quan, ý tưởng, mô phỏng tay từng bước, pseudocode, code C++ ngắn gọn, theo dõi biến khi debug, tự kiểm tra, luyện tập ngắn và tóm tắt.

---

## Chương 4 — Đếm phân phối

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững kỹ thuật dùng giá trị làm chỉ số mảng để thống kê, đếm cặp và phân tích dữ liệu trong $\mathcal{O}(N)$ |
| Kiến thức cần có | Mảng 1 chiều (`vector<int>`), chỉ số mảng, vòng lặp, chuỗi ký tự (`string`), kiểu `long long` |
| Phạm vi | Mảng tần suất trực tiếp, tìm Mode/Min-Max tần suất, mảng chữ cái 26 ký tự, kỹ thuật đếm cặp trong $\mathcal{O}(N)$ và nguyên lý Dirichlet |
| Số bài | 5 bài học lý thuyết & thực hành + 1 bài tổng kết và bài tập phân tầng |

### Learning outcomes

Sau chương này, em có thể:
1. Xây dựng và cập nhật bảng đếm tần suất các giá trị trong thời gian $\mathcal{O}(N)$ bằng kỹ thuật chuyển giá trị thành chỉ số mảng.
2. Tìm phần tử xuất hiện nhiều nhất, ít nhất hoặc kiểm tra phần tử đa số tuyệt đối trong một dãy số.
3. Ánh xạ các ký tự chữ cái thường `'a'..'z'` thành chỉ số `0..25` để kiểm tra chuỗi Anagram trong thời gian tuyến tính.
4. Đếm số lượng cặp phần tử thỏa mãn điều kiện bằng nhau hoặc có tổng bằng $S$ trong $\mathcal{O}(N)$ mà không dùng hai vòng lặp lồng nhau.
5. Vận dụng nguyên lý Dirichlet để tìm kiếm đoạn con liên tiếp có tổng chia hết cho $N$.
6. Tránh bẫy tràn số khi đếm số lượng cặp phần tử vượt ngưỡng 32-bit ($2 \times 10^9$).

### Câu hỏi trung tâm của chương

> **Làm thế nào để đếm tần suất, tìm phần tử xuất hiện nhiều nhất và đếm hàng tỷ cặp phần tử chỉ qua MỘT lần duyệt mảng duy nhất mà không bị quá thời gian?**

---

### Bài 4.1 — Mảng tần suất trực tiếp: biến giá trị thành chỉ số

#### Mục tiêu bài

Sau Bài 4.1, em hiểu bản chất của mảng tần suất, biết cách dùng chính giá trị của phần tử làm chỉ số mảng để đếm số lần xuất hiện của các phần tử trong $\mathcal{O}(N)$.

#### Khởi động

Khi kiểm phiếu bầu cử lớp trưởng cho 3 ứng viên mang số báo danh 1, 2, 3:
- Thay vì mỗi lần đọc một phiếu lại phải lật lại toàn bộ danh sách phiếu trước đó để đếm, thư ký vẽ 3 ô số 1, 2, 3 lên bảng.
- Mỗi khi đọc một phiếu ghi số nào, thư ký chỉ cần gạch thêm một vạch vào đúng ô số đó.
- Sau khi đọc xong $N$ phiếu, số vạch trong từng ô chính là số phiếu của từng ứng viên!
- Chiếc bảng chia ô đó trong lập trình chính là **Mảng tần suất (Frequency Array)**.

#### Ý tưởng mảng tần suất

- **Cách làm ngây thơ ($\mathcal{O}(N^2)$):** Với mỗi phần tử $A[i]$, duyệt lại toàn bộ mảng từ đầu đến cuối để đếm. Với $N = 10^5$, hai vòng lặp lồng nhau mất $10^{10}$ phép tính $\implies$ Quá thời gian (TLE).
- **Mảng tần suất ($\mathcal{O}(N)$):**
  1. Khởi tạo một mảng đếm `cnt` kích thước đủ lớn, ban đầu tất cả bằng `0`.
  2. Khi đọc phần tử giá trị `x`, ta tăng biến đếm tại chỉ số `x` lên 1:
     $$\text{cnt}[x] = \text{cnt}[x] + 1 \quad (\text{hoặc } \text{cnt}[x]\text{++})$$
  3. Sau khi đọc xong, `cnt[v]` lưu trữ chính xác số lần xuất hiện của giá trị `v`.

#### Mô phỏng ghi nhận tần suất cho dãy $A = [3, 1, 3, 2, 1, 3]$

| Bước | Đọc giá trị $x$ | Thao tác | Trạng thái mảng `cnt` (`cnt[0..3]`) |
|:---:|:---:|:---:|:---:|
| Khởi tạo | - | `cnt = {0, 0, 0, 0}` | `[0: 0, 1: 0, 2: 0, 3: 0]` |
| 1 | $3$ | `cnt[3]++` | `[0: 0, 1: 0, 2: 0, 3: 1]` |
| 2 | $1$ | `cnt[1]++` | `[0: 0, 1: 1, 2: 0, 3: 1]` |
| 3 | $3$ | `cnt[3]++` | `[0: 0, 1: 1, 2: 0, 3: 2]` |
| 4 | $2$ | `cnt[2]++` | `[0: 0, 1: 1, 2: 1, 3: 2]` |
| 5 | $1$ | `cnt[1]++` | `[0: 0, 1: 2, 2: 1, 3: 2]` |
| 6 | $3$ | `cnt[3]++` | `[0: 0, 1: 2, 2: 1, 3: 3]` |

👉 **Kết quả:** Số 1 xuất hiện 2 lần, số 2 xuất hiện 1 lần, số 3 xuất hiện 3 lần.

#### Pseudocode

```text
cnt = mảng kích thước MAX_VAL + 1, khởi tạo bằng 0
for x trong dãy A:
    cnt[x] = cnt[x] + 1

distinctCount = 0
for v từ 0 đến MAX_VAL:
    nếu cnt[v] > 0:
        distinctCount tăng 1

in distinctCount
for v từ 0 đến MAX_VAL:
    nếu cnt[v] > 0:
        in v và cnt[v]
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    int distinctCount = 0;
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > 0) {
            distinctCount++;
        }
    }

    cout << distinctCount << '\n';
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > 0) {
            cout << v << " xuat hien " << cnt[v] << " lan\n";
        }
    }

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Chi tiết | Lưu ý |
|---|---|
| Kích thước mảng | Luôn khai báo `MAX_VAL + 1` để truy cập được chỉ số `MAX_VAL`. |
| Giá trị $A_i$ âm | Nếu có số âm, cần tịnh tiến chỉ số: `cnt[x + OFFSET]++`. |

#### Tự kiểm tra

1. Mảng tần suất trực tiếp áp dụng tốt nhất khi giá trị các phần tử nằm trong khoảng nào?
2. Vì sao mảng tần suất giúp giảm độ phức tạp từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$?

#### Luyện tập ngắn

- **LT 4.1A:** Nhập dãy $N$ số nguyên ($N \le 10^5, 0 \le A_i \le 10^5$). In ra các giá trị chỉ xuất hiện đúng 1 lần theo thứ tự tăng dần.
- **LT 4.1B:** Cho dãy $N$ số nguyên trong đoạn $[-1000, 1000]$. Dùng mảng tần suất tịnh tiến để đếm số lần xuất hiện của từng số.

#### Tóm tắt bài

Mảng tần suất biến **giá trị thành chỉ số** giúp tra cứu và cập nhật số lần xuất hiện trong $\mathcal{O}(1)$.

---

### Bài 4.2 — Thống kê tần suất: Tìm Mode, Min-Max và Phần tử đa số

#### Mục tiêu bài

Sau Bài 4.2, em biết cách tìm phần tử xuất hiện nhiều nhất (Mode) và xác định phần tử đa số tuyệt đối (xuất hiện $> N/2$ lần) bằng một lần duyệt mảng tần suất.

#### Khởi động

Trong cuộc bỏ phiếu bầu lớp trưởng với $N = 7$ phiếu, ứng viên chỉ trúng cử nếu nhận được quá bán (nhiều hơn $7/2 = 3.5 \implies$ ít nhất 4 phiếu). Giá trị xuất hiện $> N/2$ lần này được gọi là **Phần tử đa số (Majority Element)**.

#### Ý tưởng thống kê

1. **Tìm phần tử xuất hiện nhiều nhất (Mode):**  
   Duyệt `v` từ `0` đến `MAX_VAL`. Duy trì biến `maxFreq` và `bestVal`. Nếu `cnt[v] > maxFreq`, cập nhật `maxFreq = cnt[v]` và `bestVal = v`.
2. **Tìm phần tử đa số tuyệt đối:**  
   Kiểm tra xem có giá trị `v` nào thỏa mãn `cnt[v] > n / 2` không. Trong mảng $N$ phần tử, **tối đa chỉ có thể có duy nhất một phần tử đa số tuyệt đối**.

#### Mô phỏng tìm phần tử đa số cho $A = [3, 3, 4, 2, 3, 3, 5]$ ($N = 7$, ngưỡng $> 3$)

| Giá trị $v$ | Tần suất `cnt[v]` | Điều kiện `cnt[v] > 3` | Kết luận |
|:---:|:---:|:---:|---|
| 2 | 1 | Sai | Không phải đa số |
| 3 | 4 | Đúng ($4 > 3$) | **Là phần tử đa số tuyệt đối!** |
| 4 | 1 | Sai | Không phải đa số |
| 5 | 1 | Sai | Không phải đa số |

#### Pseudocode

```text
majority = -1
for v từ 0 đến MAX_VAL:
    nếu cnt[v] > n / 2:
        majority = v
        dừng vòng lặp
in majority
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x]++;
    }

    int majority = -1;
    for (int v = 0; v <= MAX_VAL; v++) {
        if (cnt[v] > n / 2) {
            majority = v;
            break;
        }
    }

    cout << majority << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Tình huống | Kiểm tra |
|---|---|
| Không có ai đa số | Biến `majority` giữ nguyên giá trị `-1`. |
| Nhiều số cùng tần suất lớn nhất | Dùng `cnt[v] > maxFreq` khi duyệt từ nhỏ đến lớn sẽ tự động giữ lại giá trị nhỏ nhất. |

#### Tự kiểm tra

1. Một mảng có độ dài $N = 10$ có thể có 2 phần tử cùng xuất hiện 6 lần không? Vì sao?
2. Vì sao phần tử đa số tuyệt đối nếu tồn tại thì luôn là duy nhất?

#### Luyện tập ngắn

- **LT 4.2A:** Tìm giá trị xuất hiện nhiều lần nhất trong mảng $N$ số. Nếu có nhiều giá trị, in giá trị nhỏ nhất.
- **LT 4.2B:** Tìm giá trị xuất hiện ít nhất một lần nhưng có số lần xuất hiện nhỏ nhất trong mảng.

#### Tóm tắt bài

Duyệt mảng tần suất $\mathcal{O}(\text{MAX\_VAL})$ cho phép dễ dàng tìm Mode và xác định phần tử đa số tuyệt đối trong chớp mắt.

---

### Bài 4.3 — Mảng tần suất trên bảng chữ cái và Kiểm tra chuỗi Anagram

#### Mục tiêu bài

Sau Bài 4.3, em biết cách ánh xạ các chữ cái `'a'..'z'` thành chỉ số `0..25` để đếm tần suất ký tự và kiểm tra hai chuỗi Anagram trong thời gian $\mathcal{O}(N)$.

#### Khởi động

Hai từ tiếng Anh **"listen"** và **"silent"** tuy viết khác nhau nhưng gồm đúng cùng một bộ chữ cái: 1 chữ 'e', 1 chữ 'i', 1 chữ 'l', 1 chữ 'n', 1 chữ 's', 1 chữ 't'. Hai từ như vậy gọi là **Anagram** (từ đảo mã).

#### Ánh xạ chữ cái thành chỉ số mảng

- Bảng chữ cái tiếng Anh in thường có 26 ký tự từ `'a'` đến `'z'`.
- Công thức ánh xạ: Trừ đi ký tự gốc `'a'`:
  $$\text{Index} = c - \text{'a'}$$
  - `'a' - 'a' = 0`
  - `'b' - 'a' = 1`
  - `'z' - 'a' = 25`
- Chỉ cần mảng `vector<int> cnt(26, 0)` để đếm tần suất mọi ký tự.

> **Hai chuỗi $S$ và $T$ là Anagram của nhau khi và chỉ khi chúng có cùng độ dài và mảng tần suất 26 chữ cái của chúng hoàn toàn giống nhau.**

#### Pseudocode

```text
nếu độ dài S != độ dài T: trả về false
cntS = mảng 26 số 0
cntT = mảng 26 số 0

for c trong S: cntS[c - 'a']++
for c trong T: cntT[c - 'a']++

for i từ 0 đến 25:
    nếu cntS[i] != cntT[i]: trả về false
trả về true
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s, t;
    if (!(cin >> s >> t)) return 0;

    if (s.length() != t.length()) {
        cout << "NO\n";
        return 0;
    }

    vector<int> cntS(26, 0);
    vector<int> cntT(26, 0);

    for (char c : s) cntS[c - 'a']++;
    for (char c : t) cntT[c - 'a']++;

    bool isAnagram = true;
    for (int i = 0; i < 26; i++) {
        if (cntS[i] != cntT[i]) {
            isAnagram = false;
            break;
        }
    }

    if (isAnagram) cout << "YES\n";
    else cout << "NO\n";

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Chi tiết | Kiểm tra |
|---|---|
| `c - 'a'` | Đảm bảo ký tự `c` là chữ cái in thường (`'a' <= c <= 'z'`). |
| So sánh độ dài | Luôn kiểm tra `s.length() != t.length()` đầu tiên để thoát sớm. |

#### Tự kiểm tra

1. Phép trừ `c - 'a'` cho kết quả là kiểu dữ liệu gì?
2. Làm thế nào để kiểm tra một xâu có thể sắp xếp lại thành xâu đối xứng (Palindrome) không? (Gợi ý: Có tối đa 1 ký tự có số lần xuất hiện lẻ).

#### Luyện tập ngắn

- **LT 4.3A:** Tìm chữ cái xuất hiện nhiều lần nhất trong xâu $S$ ($|S| \le 10^5$).
- **LT 4.3B:** Kiểm tra xâu $S$ có thể đổi chỗ các ký tự để tạo thành xâu đối xứng không.

#### Tóm tắt bài

Ánh xạ `c - 'a'` biến bảng chữ cái thành mảng 26 phần tử, là công cụ tối ưu $\mathcal{O}(N)$ cho các bài toán xử lý xâu ký tự.

---

### Bài 4.4 — Kỹ thuật đếm cặp $\mathcal{O}(N)$ bằng Bảng tần suất

#### Mục tiêu bài

Sau Bài 4.4, em làm chủ kỹ thuật đếm số lượng cặp $(i, j)$ ($i < j$) có tổng bằng $S$ hoặc bằng nhau trong $\mathcal{O}(N)$ và biết cách phòng tránh bẫy tràn số.

#### Khởi động

Một bãi xe cần ghép từng cặp 2 xe sao cho tổng trọng tải đúng bằng $S = 6$ tấn.
- Thay vì với mỗi xe lại đi tìm trong toàn bộ bãi ($\mathcal{O}(N^2)$), bác tài xế vừa kéo xe tải trọng $x$ vào, vừa nhìn sổ xem trước đó đã có bao nhiêu xe tải trọng bù $6 - x$.
- Có bao nhiêu xe bù có sẵn $\implies$ tạo được bấy nhiêu cặp mới ngay lập tức!

#### Kỹ thuật "Vừa duyệt vừa đếm"

- Khi xét phần tử đứng sau tại vị trí $j$ có giá trị $x = A[j]$, phần tử đứng trước $A[i]$ ($i < j$) muốn ghép đôi để có tổng bằng $S$ phải có giá trị:
  $$\text{comp} = S - x$$
- Số phần tử đứng trước thỏa mãn chính là số lần `comp` đã xuất hiện trong mảng `cnt` tính đến trước bước $j$.
- **Thứ tự thực hiện:**
  1. `totalPairs += cnt[comp]` (cộng số cặp tạo được với các phần tử đứng trước).
  2. `cnt[x]++` (ghi nhận phần tử hiện tại vào mảng đếm).

> **Bẫy tràn số:** Với $N = 10^5$, số lượng cặp có thể đạt tới $\frac{N(N-1)}{2} \approx 5 \times 10^9 > 2 \times 10^9 \implies$ Bắt buộc dùng kiểu `long long` cho biến đếm kết quả.

#### Mô phỏng đếm cặp tổng $S = 6$ cho $A = [1, 5, 3, 3, 5]$

| Bước $j$ | Giá trị $x = A[j]$ | Giá trị bù $\text{comp} = 6 - x$ | `cnt[comp]` hiện có | Cộng dồn `totalPairs` | Cập nhật `cnt` |
|:---:|:---:|:---:|:---:|:---:|---|
| 0 | $1$ | $5$ | $0$ | $0$ | `cnt[1] = 1` |
| 1 | $5$ | $1$ | $1$ | $0 + 1 = 1$ | `cnt[5] = 1` |
| 2 | $3$ | $3$ | $0$ | $1$ | `cnt[3] = 1` |
| 3 | $3$ | $3$ | $1$ | $1 + 1 = 2$ | `cnt[3] = 2` |
| 4 | $5$ | $1$ | $1$ | $2 + 1 = 3$ | `cnt[5] = 2` |

👉 **Tổng số cặp: 3 cặp** (chính xác 100%).

#### Pseudocode

```text
totalPairs = 0 (kiểu long long)
cnt = mảng MAX_VAL + 1 số 0

for x trong dãy A:
    comp = S - x
    nếu comp nằm trong khoảng [0, MAX_VAL]:
        totalPairs = totalPairs + cnt[comp]
    cnt[x] = cnt[x] + 1

in totalPairs
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 200000;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, s;
    if (!(cin >> n >> s)) return 0;

    vector<int> cnt(MAX_VAL + 1, 0);
    long long totalPairs = 0;

    for (int j = 0; j < n; j++) {
        int x;
        cin >> x;

        int comp = s - x;
        if (comp >= 0 && comp <= MAX_VAL) {
            totalPairs += cnt[comp];
        }

        if (x >= 0 && x <= MAX_VAL) {
            cnt[x]++;
        }
    }

    cout << totalPairs << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Thao tác | Đánh giá |
|---|---|
| Cộng `cnt[comp]` trước rồi mới `cnt[x]++` |  Đúng, tự động bảo đảm chỉ ghép với phần tử đứng trước ($i < j$). |
| Khai báo `long long totalPairs` |  Đúng, chống tràn số khi số cặp vượt $2 \times 10^9$. |

#### Tự kiểm tra

1. Nếu đổi thứ tự thực hiện `cnt[x]++` trước rồi mới cộng `totalPairs += cnt[comp]`, điều gì sẽ xảy ra khi $x + x = S$?
2. Muốn đếm số cặp bằng nhau ($A_i = A_j$), giá trị `comp` bằng bao nhiêu?

#### Luyện tập ngắn

- **LT 4.4A:** Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $A_i = A_j$ trong mảng $N$ phần tử ($N \le 10^5$).
- **LT 4.4B:** Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $A_i - A_j = D$ ($D \ge 0$).

#### Tóm tắt bài

Kỹ thuật "vừa duyệt vừa đếm" kết hợp mảng tần suất giúp đếm cặp trong $\mathcal{O}(N)$. Luôn dùng `long long` cho biến đếm kết quả.

---

### Bài 4.5 — Nguyên lý Dirichlet trong Tin học

#### Mục tiêu bài

Sau Bài 4.5, em hiểu nguyên lý Dirichlet (nguyên lý chuồng bồ câu) và biết cách áp dụng mảng số dư tiền tố để tìm đoạn con liên tiếp có tổng chia hết cho $N$.

#### Khởi động

Nếu có **4 chiếc áo** và chỉ có **3 chiếc móc treo**, khi treo hết 4 chiếc áo chắc chắn sẽ có **ít nhất một chiếc móc treo từ 2 chiếc áo trở lên**.

#### Nguyên lý Dirichlet và Đoạn con chia hết

- **Nguyên lý cơ bản:** Nhốt $N + 1$ đồ vật vào $N$ chiếc hộp $\implies$ tồn tại ít nhất một hộp chứa từ 2 đồ vật trở lên.
- **Ứng dụng tìm đoạn con chia hết cho $N$:**  
  Xét $N$ tổng tiền tố $S_1, S_2, \dots, S_N$. Lấy số dư khi chia cho $N$: $R_i = S_i \pmod N$.
  - Nếu có $S_k \pmod N == 0 \implies$ đoạn $[1, k]$ chia hết cho $N$.
  - Nếu không, $N$ số dư chỉ nhận $N - 1$ giá trị từ $1$ đến $N - 1$. Theo Dirichlet, chắc chắn có hai vị trí $u < v$ sao cho $S_u \equiv S_v \pmod N \implies$ tổng đoạn từ $u + 1$ đến $v$ là $S_v - S_u$ chia hết cho $N$!

#### Mô phỏng cho dãy $N = 5$: $A = [2, 3, 7, 1, 4]$

| $i$ | $A_i$ | Tổng tiền tố $S_i$ | Số dư $R_i = S_i \pmod 5$ | Ghi nhận vị trí đầu tiên của số dư |
|:---:|:---:|:---:|:---:|---|
| $0$ | - | $S_0 = 0$ | $0$ | `firstPos[0] = 0` |
| $1$ | $2$ | $S_1 = 2$ | $2$ | `firstPos[2] = 1` |
| $2$ | $3$ | $S_2 = 5$ | $0$ | Trùng số dư 0 $\implies$ **Đoạn $[1, 2]$ tổng bằng 5 chia hết cho 5!** |

#### Pseudocode

```text
firstPos = mảng kích thước n, gán toàn bộ bằng -1
firstPos[0] = 0
prefix = 0

for i từ 1 đến n:
    prefix = prefix + a[i]
    rem = (prefix % n + n) % n
    nếu firstPos[rem] != -1:
        in (firstPos[rem] + 1) và i
        dừng
    firstPos[rem] = i
```

#### Code C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> firstPos(n, -1);
    firstPos[0] = 0;

    long long currentPrefix = 0;
    int ansL = -1, ansR = -1;

    for (int i = 1; i <= n; i++) {
        long long x;
        cin >> x;
        currentPrefix += x;
        int rem = (currentPrefix % n + n) % n;

        if (firstPos[rem] != -1) {
            ansL = firstPos[rem] + 1;
            ansR = i;
            break;
        } else {
            firstPos[rem] = i;
        }
    }

    cout << ansL << " " << ansR << '\n';

    return 0;
}
```

#### Điều cần theo dõi khi debug

| Biến | Lưu ý |
|---|---|
| `firstPos[0] = 0` | Mốc số dư 0 ở trước mảng (tổng rỗng). |
| `(prefix % n + n) % n` | Công thức an toàn đảm bảo số dư không âm. |

#### Tự kiểm tra

1. Vì sao mảng $N$ phần tử luôn tìm được ít nhất một đoạn con có tổng chia hết cho $N$?
2. Công thức `ansL = firstPos[rem] + 1` vì sao phải cộng thêm 1?

#### Luyện tập ngắn

- **LT 4.5A:** Đếm tổng số đoạn con liên tiếp có tổng chia hết cho $K$ ($K \le 10^5$) bằng mảng tần suất số dư tiền tố.
- **LT 4.5B:** Cho $N + 1$ số nguyên thuộc $[1, 2N]$. Chứng minh luôn có 2 số mà số này là bội của số kia.

#### Tóm tắt bài

Nguyên lý Dirichlet kết hợp mảng lưu vị trí số dư tiền tố giải quyết bài toán tìm đoạn con chia hết trong $\mathcal{O}(N)$.

---

### Bài 4.6 — Ôn tập, kiểm tra và bài chuyển giao

#### Mục tiêu bài

Bài này giúp em củng cố các kỹ thuật thống kê tần suất, đếm cặp và đoạn con chia hết.

#### Tầng A — Củng cố nền tảng

##### Bài 4.6.1 — Phổ điểm kỳ thi
Cho điểm thi của $N$ thí sinh từ $0$ đến $10$ ($N \le 10^5, 0 \le A_i \le 10$). In số thí sinh đạt từng mức điểm từ 0 đến 10.
- **Input:** $N$ và dãy $N$ điểm số.
- **Output:** 11 số nguyên tương ứng số lượng thí sinh đạt điểm $0..10$.
- **Ví dụ:** `5` và `8 9 8 10 8` $\implies$ Output: `0 0 0 0 0 0 0 0 3 1 1`.

##### Bài 4.6.2 — Phần tử độc nhất
Cho dãy $N$ số nguyên ($N \le 10^5, 1 \le A_i \le 10^5$). Tìm giá trị nhỏ nhất chỉ xuất hiện đúng 1 lần. Nếu không có, in `-1`.
- **Ví dụ:** `6` và `4 2 7 2 4 9` $\implies$ Output: `7`.

##### Bài 4.6.3 — Ký tự hiếm nhất
Cho xâu $S$ gồm các chữ cái in thường ($|S| \le 10^5$). Tìm chữ cái xuất hiện ít nhất một lần nhưng có số lần xuất hiện nhỏ nhất.
- **Ví dụ:** `banana` $\implies$ Output: `b`.

##### Bài 4.6.4 — Thống kê độ tuổi
Cho độ tuổi của $N$ người và $Q$ truy vấn $[L, R]$. Đếm số người có độ tuổi trong đoạn $[L, R]$ ($N, Q \le 10^5, 18 \le L \le R \le 60$).

---

#### Tầng B — Vận dụng mẫu

##### Bài 4.6.5 — Đếm cặp có tổng bằng K
Cho dãy $N$ số nguyên ($N \le 10^5, 0 \le A_i \le 10^5$). Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $A_i + A_j = K$.
- **Ví dụ:** `4 10` và `3 7 5 7` $\implies$ Output: `2`.

##### Bài 4.6.6 — Đếm cặp có hiệu bằng D
Cho dãy $N$ số nguyên ($N \le 10^5, 0 \le A_i \le 10^5$). Đếm số cặp $(i, j)$ với $i < j$ thỏa mãn $|A_i - A_j| = D$.

##### Bài 4.6.7 — Phần tử xuất hiện nhiều hơn N/3 lần
Cho dãy $N$ số nguyên. Tìm tất cả các giá trị xuất hiện nhiều hơn $\lfloor N / 3 \rfloor$ lần theo thứ tự tăng dần. Nếu không có, in `-1`.

##### Bài 4.6.8 — Ghép đôi hoàn hảo
Cho $2N$ số nguyên. Kiểm tra xem có thể ghép $2N$ số thành $N$ cặp số bằng nhau hay không. In `YES` hoặc `NO`.
- **Ví dụ:** `4` số `41 42 41 42` $\implies$ Output: `YES`.

---

#### Tầng C — Chuyển giao

##### Bài 4.6.9 — Đếm bộ ba có tổng bằng S
Cho dãy $N$ số nguyên ($N \le 2000, 0 \le A_i \le 10^5$). Đếm số bộ ba $(i, j, k)$ với $i < j < k$ thỏa mãn $A_i + A_j + A_k = S$.
- **Gợi ý:** Cố định phần tử ở giữa $j$, dùng mảng tần suất đếm các phần tử $i < j$.

##### Bài 4.6.10 — Đếm đoạn con có tổng chia hết cho K
Cho dãy $N$ số nguyên ($N \le 10^5, A_i \le 10^9$). Đếm số đoạn con liên tiếp có tổng chia hết cho $K$ ($K \le 10^5$).
- **Ví dụ:** `4 3` và `1 2 3 3` $\implies$ Output: `4`.

##### Bài 4.6.11 — Ghép đôi cùng điểm số
Cho dãy $A$ gồm $N$ số và dãy $B$ gồm $M$ số ($N, M \le 10^5, 0 \le A_i, B_j \le 10^5$). Đếm số cách chọn một số từ $A$ và một số từ $B$ bằng nhau.
- **Công thức:** $\sum \text{cntA}[v] \times \text{cntB}[v]$.

##### Bài 4.6.12 — Đếm cặp chuỗi Anagram
Cho $N$ chuỗi ký tự ngắn ($N \le 10^5, |S_i| \le 10$). Đếm số cặp chuỗi $(i, j)$ với $i < j$ là Anagram của nhau.

---

#### Phiếu tự đánh giá

| Năng lực | Chưa chắc | Làm khi có gợi ý | Tự làm được |
|---|:---:|:---:|:---:|
| Xây dựng mảng tần suất $\mathcal{O}(N)$ |  |  |  |
| Tìm Mode và Phần tử đa số tuyệt đối |  |  |  |
| Ánh xạ chữ cái `'a'..'z'` kiểm tra Anagram |  |  |  |
| Đếm cặp có tổng bằng $S$ trong $\mathcal{O}(N)$ |  |  |  |
| Khai báo `long long` chống tràn số khi đếm cặp |  |  |  |
| Tìm đoạn con chia hết cho $N$ bằng Dirichlet |  |  |  |

#### Tiêu chí hoàn thành chương

Em có thể xem mình đã nắm chắc chương khi:
1. Giải thích được tại sao mảng tần suất giúp giảm độ phức tạp từ $\mathcal{O}(N^2)$ xuống $\mathcal{O}(N)$.
2. Viết được hàm đếm cặp tổng bằng $S$ không dùng 2 vòng lặp lồng nhau.
3. Biết cách ánh xạ chữ cái bằng phép trừ `c - 'a'`.
4. Không mắc bẫy tràn số khi đếm số lượng cặp.

---

### Tổng kết chương

> **Mảng tần suất là bước đột phá từ tư duy so sánh tuần tự sang tư duy định vị trực tiếp. Bằng cách biến giá trị thành chỉ số, ta giải quyết bài toán thống kê và đếm cặp trong thời gian tuyến tính $\mathcal{O}(N)$.**

| Cần nhớ | Nội dung |
|---|---|
| Mảng tần suất | `cnt[x]++` với $0 \le x \le \text{MAX\_VAL}$, thời gian $\mathcal{O}(N)$, bộ nhớ $\mathcal{O}(\text{MAX\_VAL})$ |
| Bảng chữ cái | Mảng kích thước 26 phần tử với chỉ số `c - 'a'` |
| Đếm cặp tổng $S$ | Cộng `cnt[S - x]` trước rồi mới `cnt[x]++` |
| Đếm cặp bằng nhau | Cộng dồn `cnt[x]` khi duyệt hoặc tính $\sum \frac{C(C-1)}{2}$ |
| Chống tràn số | Biến đếm cặp bắt buộc dùng kiểu `long long` |
| Dirichlet | $N$ tổng tiền tố chia cho $N$ luôn có 2 tổng cùng số dư $\implies$ đoạn con chia hết |

#### Những lỗi thường gặp

| Lỗi | Cách tự kiểm tra |
|---|---|
| Kích thước mảng `cnt` nhỏ hơn $\max(A_i)$ | Luôn khai báo `MAX_VAL >= max(A_i)` |
| Tràn số khi đếm số lượng cặp | Biến đếm số cặp phải là `long long` |
| Quên trường hợp $A_i$ âm | Tịnh tiến chỉ số `cnt[x + OFFSET]` |
| Số dư bị âm khi tính `prefix % N` | Dùng công thức an toàn `(prefix % N + N) % N` |

---

### Code tham chiếu

```cpp
#include <bits/stdc++.h>
using namespace std;

const int MAX_VAL = 100000;

// 1. Dem so cap co tong bang S trong O(N)
long long countPairsWithSum(const vector<int> &a, int s) {
    vector<int> cnt(MAX_VAL + 1, 0);
    long long totalPairs = 0;

    for (int x : a) {
        int comp = s - x;
        if (comp >= 0 && comp <= MAX_VAL) {
            totalPairs += cnt[comp];
        }
        if (x >= 0 && x <= MAX_VAL) {
            cnt[x]++;
        }
    }
    return totalPairs;
}

// 2. Kiem tra hai chuoi Anagram O(N)
bool isAnagram(const string &s, const string &t) {
    if (s.length() != t.length()) return false;
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

    int n, s;
    if (!(cin >> n >> s)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "Pairs with sum " << s << ": " << countPairsWithSum(a, s) << "\n";

    return 0;
}
```
