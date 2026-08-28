# TÀI LIỆU GỐC — CHƯƠNG 1: SẮP XẾP

## Vai trò tài liệu

Tài liệu này là bản thảo hoàn chỉnh dùng để biên soạn Chương 1 — Sắp xếp. Nội dung được cấu trúc theo đúng progression nhận thức sư phạm: **Hiểu bản chất cơ học $\to$ Làm chủ công cụ thực chiến $\to$ Nhận diện ứng dụng $\to$ Tổng kết & Luyện tập phân tầng**.

---

## Chương 1 — Sắp xếp (Sorting)

### Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Hiểu sắp xếp là bước tiền xử lý tạo trật tự dữ liệu, làm chủ thuật toán Selection Sort và hàm `std::sort`, viết được hàm so sánh tùy biến và ứng dụng giải quyết các bài toán gom nhóm, khoảng cách |
| Kiến thức cần có | Cú pháp C++ cơ bản (`int`, `vector<int>`, vòng lặp `for`, câu lệnh `if`, hoán vị `swap`) |
| Phạm vi | Bản chất sắp xếp, Selection Sort $\mathcal{O}(N^2)$, `std::sort` $\mathcal{O}(N \log N)$, Comparator `bool cmp()`, bài toán gom nhóm và cặp kề nhau |
| Cấu trúc chương | 3 Bài học lý thuyết & thực hành + 1 Bài tổng kết & luyện tập phân tầng |

### Learning outcomes

Sau chương này, em có thể:
1. Giải thích vì sao trật tự dữ liệu giúp các bước tìm kiếm, đếm và gom nhóm trở nên đơn giản hơn.
2. Mô phỏng bằng tay và cài đặt được thuật toán Selection Sort $\mathcal{O}(N^2)$ với thao tác `swap`.
3. Sử dụng thành thạo hàm `sort()` của thư viện C++ để sắp xếp tăng dần, giảm dần trong thời gian $\mathcal{O}(N \log N)$.
4. Tự viết hàm so sánh tùy biến (Custom Comparator) theo các quy tắc đặc thù (chẵn/lẻ, trị tuyệt đối).
5. Nhận diện và áp dụng trật tự sắp xếp để đếm số giá trị phân biệt và tìm cặp phần tử gần nhau nhất.
6. Hoàn thành bộ bài tập phân tầng từ củng cố cú pháp đến vận dụng thi đấu.

---

### Bài 1.1 — Bản chất của Sắp xếp & Thuật toán Selection Sort

#### 1. Mục tiêu bài

Sau Bài 1.1, em hiểu rõ tại sao cần sắp xếp, mô phỏng được quá trình chọn phần tử nhỏ nhất bằng tay và tự tay viết được thuật toán Selection Sort $\mathcal{O}(N^2)$.

#### 2. Khởi động: Vì sao cần sắp xếp?

Cho dãy số nguyên chưa có thứ tự:

```text
8  3  6  1  5
```

- Nếu muốn tìm số lớn nhất, em chỉ cần duyệt một lượt từ trái sang phải và giữ lại số lớn nhất đã gặp.
- Nhưng nếu cần **tìm khoảng cách nhỏ nhất giữa hai số bất kỳ**, hoặc **đếm xem có bao nhiêu số khác nhau**, việc dữ liệu nằm lộn xộn sẽ khiến em phải so sánh từng cặp một ($\mathcal{O}(N^2)$).
- Nếu dãy số đã được xếp tăng dần:

```text
1  3  5  6  8
```

Mọi thứ trở nên cực kỳ rõ ràng: hai số gần nhau nhất chắc chắn phải đứng cạnh nhau, các số giống nhau sẽ tự động nằm liền kề nhau!

> **Sắp xếp không tạo ra dữ liệu mới. Sắp xếp là bước tạo trật tự để các bước xử lý tiếp theo trở nên dễ dàng và nhanh chóng hơn.**

#### 3. Ý tưởng thuật toán Selection Sort (Sắp xếp chọn)

Ý tưởng cốt lõi của Selection Sort gói gọn trong một câu:
> **Ở mỗi vị trí $i$ từ đầu đến cuối mảng, tìm phần tử nhỏ nhất trong phần chưa sắp xếp rồi đổi chỗ (`swap`) nó về vị trí $i$.**

##### Mô phỏng từng bước cho dãy `8 3 6 1 5` ($N = 5$):

| Lượt $i$ | Vị trí đang xét | Phần chưa sắp xếp | Phần tử nhỏ nhất tìm được | Thao tác đổi chỗ | Dãy số sau lượt đó |
|:---:|:---:|:---:|:---:|:---:|---|
| **Lượt 1** | $i = 0$ | `[8, 3, 6, 1, 5]` | Số `1` tại vị trí 3 | `swap(a[0], a[3])` | `[1, 3, 6, 8, 5]` *(Số 1 đã đúng vị trí)* |
| **Lượt 2** | $i = 1$ | `[3, 6, 8, 5]` | Số `3` tại vị trí 1 | `swap(a[1], a[1])` | `[1, 3, 6, 8, 5]` *(Số 3 đã đúng vị trí)* |
| **Lượt 3** | $i = 2$ | `[6, 8, 5]` | Số `5` tại vị trí 4 | `swap(a[2], a[4])` | `[1, 3, 5, 8, 6]` *(Số 5 đã đúng vị trí)* |
| **Lượt 4** | $i = 3$ | `[8, 6]` | Số `6` tại vị trí 4 | `swap(a[3], a[4])` | `[1, 3, 5, 6, 8]` *(Toàn bộ dãy đã tăng dần)* |

#### 4. Cài đặt C++

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    // Thuat toan Selection Sort O(N^2)
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        swap(a[i], a[min_idx]);
    }

    // In ket qua
    for (int i = 0; i < n; i++) {
        if (i > 0) cout << ' ';
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

#### 5. Bảng theo dõi biến khi Debug

| Biến | Ý nghĩa | Lưu ý quan trọng |
|---|---|---|
| `i` | Vị trí đang cần đặt phần tử đúng | Vòng lặp ngoài chỉ cần chạy đến `n - 2` vì khi $n-1$ phần tử đầu đã đúng, phần tử cuối cùng tự động đúng. |
| `j` | Vị trí đang duyệt tìm phần tử nhỏ nhất | Luôn bắt đầu từ `i + 1` đến `n - 1`. Điều kiện dừng là `j < n`, không viết `j <= n`. |
| `min_idx` | Chỉ số của phần tử nhỏ nhất tìm được | Khởi tạo bằng `i` trước khi chạy vòng lặp `j`. |

#### 6. Quiz Trắc nghiệm nhanh

**Câu 1:** Thao tác sắp xếp một mảng số nguyên làm thay đổi điều gì?  
- A. Làm thay đổi giá trị của các phần tử trong mảng.  
- B. Làm thay đổi số lượng phần tử trong mảng.  
- C. Làm thay đổi vị trí (thứ tự) của các phần tử trong mảng.  
- D. Tự động xóa bỏ các phần tử có giá trị trùng nhau.  
👉 **Đáp án:** **C**. Sắp xếp chỉ hoán đổi vị trí của các phần tử để tạo trật tự, bảo toàn 100% giá trị và số lượng ban đầu.

**Câu 2:** Với dãy $N$ phần tử, thuật toán Selection Sort thực hiện bao nhiêu lượt duyệt ở vòng lặp ngoài?  
- A. Đúng $N$ lượt.  
- B. $N - 1$ lượt.  
- C. $N / 2$ lượt.  
- D. $N^2$ lượt.  
👉 **Đáp án:** **B**. Khi $N - 1$ phần tử đã được đưa về đúng vị trí ở bên trái, phần tử cuối cùng chắc chắn là phần tử lớn nhất và đã tự nằm đúng chỗ.

**Câu 3:** Cho dãy số `5 2 4 1`. Sau lượt đầu tiên ($i = 0$) của Selection Sort, trạng thái dãy số là gì?  
- A. `2 5 4 1`  
- B. `1 2 4 5`  
- C. `1 5 4 2`  
- D. `1 2 5 4`  
👉 **Đáp án:** **C**. Phần tử nhỏ nhất là `1` tại chỉ số 3, đổi chỗ với phần tử đầu tiên `5` $\implies$ dãy thành `1 5 4 2`.

#### 7. Bài tập thực hành nộp code tại chỗ

##### Bài thực hành 1.1A — Kiểm tra dãy đã tăng dần chưa
- **Mục tiêu:** Rèn luyện kỹ năng duyệt mảng kiểm tra điều kiện thứ tự kề nhau.
- **Đề bài:** Cho mảng gồm $N$ số nguyên $A_1, A_2, \dots, A_N$. Kiểm tra xem mảng đã được sắp xếp theo thứ tự không giảm ($A_i \le A_{i+1}$ với mọi $1 \le i < N$) hay chưa.
- **Input:** 
  - Dòng 1 ghi số nguyên dương $N$ ($1 \le N \le 10^5$).
  - Dòng 2 ghi $N$ số nguyên $A_i$ ($|A_i| \le 10^9$).
- **Output:** In `YES` nếu dãy đã tăng dần, ngược lại in `NO`.
- **Sample:**
  ```text
  Input:
  4
  1 3 5 8
  Output:
  YES
  ```

##### Bài thực hành 1.1B — Cài đặt Selection Sort
- **Mục tiêu:** Cài đặt chính xác thuật toán Selection Sort để hiểu bản chất đổi chỗ.
- **Đề bài:** Cho mảng $N$ số nguyên ($1 \le N \le 1000$). Hãy sắp xếp mảng theo thứ tự tăng dần bằng thuật toán Selection Sort và in ra kết quả.
- **Sample:**
  ```text
  Input:
  5
  8 3 6 1 5
  Output:
  1 3 5 6 8
  ```

#### 8. Tóm tắt bài

- Sắp xếp là bước tiền xử lý giúp tạo trật tự cho dữ liệu.
- Selection Sort lặp lại việc chọn phần tử nhỏ nhất và đưa về vị trí hiện tại bằng `swap`.
- Độ phức tạp thời gian của Selection Sort là $\mathcal{O}(N^2)$, phù hợp khi $N \le 1000$.

---

### Bài 1.2 — Sắp xếp tối ưu với `std::sort` & Hàm so sánh (Comparator)

#### 1. Mục tiêu bài

Sau Bài 1.2, em biết cách sử dụng hàm `std::sort()` có sẵn trong thư viện C++ để sắp xếp cực nhanh với $\mathcal{O}(N \log N)$, biết cách đảo ngược thứ tự và tự viết hàm so sánh (Comparator) theo luật riêng.

#### 2. Hàm `std::sort()` trong C++

Trong thi đấu lập trình, khi $N = 10^5$, thuật toán $\mathcal{O}(N^2)$ mất $10^{10}$ phép tính (chạy mất $\approx 10$ giây $\implies$ quá thời gian TLE).  
C++ cung cấp sẵn hàm `std::sort()` trong thư viện `<algorithm>` (đã có sẵn trong `#include <bits/stdc++.h>`).

- **Cú pháp sắp xếp tăng dần:**
  ```cpp
  sort(a.begin(), a.end());
  ```
- **Cú pháp sắp xếp giảm dần:**
  ```cpp
  sort(a.begin(), a.end(), greater<int>());
  ```
- **Độ phức tạp:** $\mathcal{O}(N \log N)$. Với $N = 10^5$, số phép tính chỉ khoảng $1.7 \times 10^6$ thao tác, chạy trong chưa tới **0.02 giây**!

#### 3. Tùy biến thứ tự với Hàm so sánh (Custom Comparator)

Khi đề bài yêu cầu thứ tự đặc thù (ví dụ: số chẵn đứng trước số lẻ, sắp xếp theo giá trị tuyệt đối...), ta tự định nghĩa một hàm so sánh:

```cpp
bool cmp(int u, int v) {
    // Tra ve true neu muon 'u' dung truoc 'v' trong day ket qua
    // Tra ve false neu nguoc lai
}
```

##### Ví dụ 1: Sắp xếp theo giá trị tuyệt đối tăng dần
Nếu hai số có trị tuyệt đối bằng nhau thì số nhỏ hơn đứng trước:

```cpp
bool cmpAbs(int u, int v) {
    if (abs(u) != abs(v)) {
        return abs(u) < abs(v); // Tri tuyet doi nho hon dung truoc
    }
    return u < v; // Neu tri tuyet doi bang nhau, so nho hon dung truoc
}
```

##### Ví dụ 2: Số chẵn đứng trước, số lẻ đứng sau
Trong cùng nhóm chẵn hoặc nhóm lẻ, số nào nhỏ hơn đứng trước:

```cpp
bool cmpEvenOdd(int u, int v) {
    if (u % 2 != v % 2) {
        return (u % 2 == 0); // So chan (u % 2 == 0) dung truoc so le
    }
    return u < v; // Cung tinh chan le: xep tang dan
}
```

> **Nguyên tắc sống còn (Strict Weak Ordering):** Trong hàm `cmp`, chỉ dùng toán tử `<` hoặc `>`, **tuyệt đối KHÔNG dùng `<=` hoặc `>=`**. Nếu hai phần tử bằng nhau (`u == v`), hàm `cmp` **bắt buộc phải trả về `false`** để tránh lỗi bộ nhớ (Runtime Error).

#### 4. Cài đặt C++ mẫu

```cpp
#include <bits/stdc++.h>
using namespace std;

// Sap xep: Chan dung truoc tang dan, Le dung sau giam dan
bool customCmp(int u, int v) {
    bool u_even = (abs(u) % 2 == 0);
    bool v_even = (abs(v) % 2 == 0);

    if (u_even != v_even) {
        return u_even; // Chan dung truoc Le
    }
    if (u_even) {
        return u < v;  // Ca hai deu chan: tang dan
    }
    return u > v;      // Ca hai deu le: giam dan
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end(), customCmp);

    for (int i = 0; i < n; i++) {
        if (i > 0) cout << ' ';
        cout << a[i];
    }
    cout << '\n';

    return 0;
}
```

#### 5. Quiz Trắc nghiệm nhanh

**Câu 1:** Độ phức tạp thời gian của hàm `std::sort()` trong C++ trên mảng $N$ phần tử là bao nhiêu?  
- A. $\mathcal{O}(N)$  
- B. $\mathcal{O}(N \log N)$  
- C. $\mathcal{O}(N^2)$  
- D. $\mathcal{O}(\log N)$  
👉 **Đáp án:** **B**. `std::sort` sử dụng thuật toán lai IntroSort kết hợp QuickSort, HeapSort và InsertionSort, đảm bảo $\mathcal{O}(N \log N)$ trong mọi trường hợp.

**Câu 2:** Khi viết hàm so sánh `bool cmp(int a, int b)`, nếu $a$ và $b$ bằng nhau ($a == b$), hàm phải trả về kết quả gì?  
- A. Luôn trả về `true`.  
- B. Luôn trả về `false`.  
- C. Trả về `1`.  
- D. Tùy ý trả về `true` hay `false`.  
👉 **Đáp án:** **B**. C++ yêu cầu tính chất Strict Weak Ordering, khi $a == b$ thì $a$ không thể đứng trước $b$ và ngược lại, bắt buộc trả về `false`.

**Câu 3:** Lệnh nào sau đây sắp xếp `vector<int> a` theo thứ tự giảm dần?  
- A. `sort(a.begin(), a.end());`  
- B. `sort(a.rbegin(), a.rend());`  
- C. `sort(a.begin(), a.end(), greater<int>());`  
- D. Cả B và C đều đúng.  
👉 **Đáp án:** **D**. Cả hai cách dùng `rbegin()/rend()` hoặc `greater<int>()` đều cho kết quả sắp xếp giảm dần chính xác.

#### 6. Bài tập thực hành nộp code tại chỗ

##### Bài thực hành 1.2A — Sắp xếp theo trị tuyệt đối
- **Đề bài:** Cho mảng $N$ số nguyên ($N \le 10^5, |A_i| \le 10^9$). Hãy sắp xếp mảng theo giá trị tuyệt đối tăng dần. Nếu hai số có cùng trị tuyệt đối, số âm đứng trước số dương.
- **Sample:**
  ```text
  Input:
  5
  -3 2 -1 3 1
  Output:
  -1 1 2 -3 3
  ```

##### Bài thực hành 1.2B — Số lớn nhất ghép từ hai số
- **Đề bài:** Cho hai số nguyên dương $A$ và $B$. Ghép $A$ và $B$ lại theo thứ tự nào để tạo thành số lớn hơn ($AB$ hay $BA$)?
- **Gợi ý:** Dùng so sánh xâu `to_string(a) + to_string(b) > to_string(b) + to_string(a)`.

#### 7. Tóm tắt bài

- Dùng `sort(a.begin(), a.end())` để đạt tốc độ tối đa $\mathcal{O}(N \log N)$.
- Dùng `greater<int>()` để sắp xếp giảm dần.
- Tự viết hàm `bool cmp()` khi cần quy tắc sắp xếp tùy biến, luôn tuân thủ nguyên tắc trả về `false` khi hai phần tử bằng nhau.

---

### Bài 1.3 — Các dạng bài toán ứng dụng Trật tự sắp xếp

#### 1. Mục tiêu bài

Sau Bài 1.3, em biết cách biến đổi bài toán thực tế bằng bước tiền xử lý sắp xếp, nhận diện được 2 dạng bài toán kinh điển: gom nhóm phần tử trùng lặp và tìm cặp kề nhau tối ưu.

#### 2. Dạng 1: Gom nhóm & Đếm số giá trị phân biệt

##### Bài toán
Cho dãy $N$ số nguyên ($N \le 10^5$). Đếm xem trong dãy có bao nhiêu số **khác nhau** (phân biệt)?

##### Nhận xét trực quan
- Nếu dãy chưa sắp xếp `[3, 1, 3, 2, 1]`, các số giống nhau nằm rải rác.
- Sau khi sắp xếp: `[1, 1, 2, 3, 3]`.
- **Tính chất vàng:** Các phần tử giống nhau sẽ tự động dồn lại thành từng khối đứng cạnh nhau!
- **Thuật toán:** Phần tử đầu tiên luôn là 1 giá trị mới. Từ phần tử thứ 2 trở đi, nếu $A[i] \ne A[i-1]$ thì ta vừa gặp thêm một giá trị phân biệt mới!

```cpp
sort(a.begin(), a.end());
int distinct_count = 1;
for (int i = 1; i < n; i++) {
    if (a[i] != a[i - 1]) {
        distinct_count++;
    }
}
```

#### 3. Dạng 2: Tìm khoảng cách nhỏ nhất giữa hai phần tử bất kỳ

##### Bài toán
Cho dãy $N$ số nguyên ($N \le 10^5$). Tìm độ chênh lệch nhỏ nhất $|A[i] - A[j]|$ giữa hai phần tử bất kỳ ($i \ne j$).

##### Nhận xét trực quan
- So sánh mọi cặp mất $\mathcal{O}(N^2)$ $\implies$ Quá thời gian.
- **Định lý khoảng cách:** Sau khi sắp xếp tăng dần $A_1 \le A_2 \le \dots \le A_N$, hai số có khoảng cách nhỏ nhất **bắt buộc phải là hai số đứng liền kề nhau** ($A_i$ và $A_{i+1}$).
- **Thuật toán:** Chỉ cần sắp xếp trong $\mathcal{O}(N \log N)$, sau đó duyệt 1 vòng lặp từ $0$ đến $N-2$ để tìm $\min(A_{i+1} - A_i)$ trong $\mathcal{O}(N)$!

```cpp
sort(a.begin(), a.end());
int min_diff = a[1] - a[0];
for (int i = 1; i < n - 1; i++) {
    min_diff = min(min_diff, a[i + 1] - a[i]);
}
```

#### 4. Cài đặt C++ mẫu (Tìm cặp số gần nhau nhất)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n) || n < 2) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    sort(a.begin(), a.end());

    int min_diff = a[1] - a[0];
    for (int i = 1; i < n - 1; i++) {
        min_diff = min(min_diff, a[i + 1] - a[i]);
    }

    cout << min_diff << '\n';

    return 0;
}
```

#### 5. Quiz Trắc nghiệm nhanh

**Câu 1:** Sau khi sắp xếp một mảng số nguyên tăng dần, các phần tử có giá trị bằng nhau sẽ nằm ở đâu?  
- A. Nằm ở đầu mảng.  
- B. Nằm ở cuối mảng.  
- C. Nằm liền kề nhau liên tục thành một đoạn.  
- D. Nằm rải rác ngẫu nhiên.  
👉 **Đáp án:** **C**. Sắp xếp đưa các giá trị bằng nhau về đứng cạnh nhau.

**Câu 2:** Để tìm độ chênh lệch nhỏ nhất giữa hai phần tử bất kỳ trong mảng đã sắp xếp tăng dần, ta cần kiểm tra những cặp phần tử nào?  
- A. Tất cả các cặp $(i, j)$ với $i < j$.  
- B. Chỉ cần kiểm tra các cặp phần tử đứng liền kề nhau $(A_i, A_{i+1})$.  
- C. Phần tử đầu tiên và phần tử cuối cùng.  
- D. Phần tử nhỏ nhất và phần tử lớn nhất.  
👉 **Đáp án:** **B**. Khoảng cách giữa hai số bất kỳ luôn lớn hơn hoặc bằng khoảng cách giữa hai số đứng liền kề ở giữa chúng.

#### 6. Bài tập thực hành nộp code tại chỗ

##### Bài thực hành 1.3A — Đếm số giá trị phân biệt
- **Đề bài:** Cho mảng $N$ số nguyên ($N \le 10^5, |A_i| \le 10^9$). Đếm số lượng giá trị khác nhau trong mảng.
- **Sample:**
  ```text
  Input:
  6
  3 1 4 1 5 9
  Output:
  5
  ```

##### Bài thực hành 1.3B — Tìm phần tử nhỏ thứ K
- **Đề bài:** Cho mảng $N$ số nguyên ($N \le 10^5$). In ra giá trị của phần tử nhỏ thứ $K$ sau khi sắp xếp tăng dần (chỉ số tính từ 1).
- **Sample:**
  ```text
  Input:
  5 3
  7 10 4 3 20
  Output:
  7
  ```

#### 7. Tóm tắt bài

- Sắp xếp biến bài toán so sánh mọi cặp ($\mathcal{O}(N^2)$) thành bài toán chỉ cần duyệt các cặp kề nhau ($\mathcal{O}(N)$).
- Ứng dụng tiêu biểu: Đếm số giá trị phân biệt, tìm khoảng cách nhỏ nhất, tìm phần tử thứ $K$.

---

### Bài 1.4 — Tổng kết chương & Bộ đề luyện tập phân tầng

#### 1. Bảng tóm tắt kiến thức cốt lõi

| Khái niệm | Ý nghĩa | Độ phức tạp | Cú pháp C++ |
|---|---|:---:|---|
| **Selection Sort** | Tìm phần tử nhỏ nhất và swap về vị trí đúng | $\mathcal{O}(N^2)$ | 2 vòng for lồng nhau + `swap(a[i], a[min_idx])` |
| **`std::sort`** | Hàm sắp xếp tối ưu của C++ | $\mathcal{O}(N \log N)$ | `sort(a.begin(), a.end())` |
| **Sắp xếp giảm dần** | Sắp xếp từ lớn đến bé | $\mathcal{O}(N \log N)$ | `sort(a.begin(), a.end(), greater<int>())` |
| **Custom Comparator** | Tùy biến quy tắc so sánh | $\mathcal{O}(N \log N)$ | `sort(a.begin(), a.end(), cmp)` |
| **Gom nhóm** | Gom các số bằng nhau lại cạnh nhau | $\mathcal{O}(N \log N)$ | `sort` rồi kiểm tra `a[i] != a[i-1]` |
| **Khoảng cách nhỏ nhất** | Tìm hiệu nhỏ nhất giữa 2 phần tử | $\mathcal{O}(N \log N)$ | `sort` rồi lấy $\min(a[i+1] - a[i])$ |

#### 2. Những bẫy lỗi thường gặp

| Lỗi thường gặp | Hậu quả | Cách phòng tránh |
|---|---|---|
| Dùng toán tử `<=` hoặc `>=` trong hàm `cmp` | Gây lỗi tràn bộ nhớ (Runtime Error) do vi phạm Strict Weak Ordering | Chỉ dùng `<` hoặc `>`, khi $a == b$ luôn trả về `false` |
| Quên dùng `#include <bits/stdc++.h>` | Báo lỗi hàm `sort()` chưa được khai báo | Luôn có `#include <bits/stdc++.h>` ở đầu chương trình |
| Truy cập ngoài mảng khi duyệt cặp kề nhau | Báo lỗi Out of Bound (`a[i+1]` khi $i = n-1$) | Vòng lặp duyệt cặp kề nhau chỉ chạy đến `i < n - 1` |

#### 3. Phiếu tự đánh giá năng lực

| Năng lực mục tiêu | Chưa chắc chắn | Làm được khi có gợi ý | Tự làm thành thạo |
|---|:---:|:---:|:---:|
| Mô phỏng và cài đặt Selection Sort bằng tay |  |  |  |
| Sử dụng thành thạo `std::sort` tăng/giảm |  |  |  |
| Tự viết hàm so sánh `bool cmp()` không bị lỗi |  |  |  |
| Đếm số giá trị phân biệt bằng `sort` trong $\mathcal{O}(N \log N)$ |  |  |  |
| Tìm cặp phần tử kề nhau tối ưu |  |  |  |

---

### Bộ đề luyện tập phân tầng (Problem Set)

#### TẦNG A — CỦNG CỐ CÚ PHÁP & NỀN TẢNG

##### Bài 1.4.1 — Dãy số tăng dần
- **Đề bài:** Đọc vào $N$ số nguyên và in các số theo thứ tự tăng dần.
- **Input:** Dòng 1 ghi số nguyên dương $N$ ($1 \le N \le 10^5$). Dòng 2 ghi $N$ số nguyên $A_i$ ($|A_i| \le 10^9$).
- **Output:** Dãy số sau khi sắp xếp tăng dần, cách nhau bởi dấu cách.
- **Sample:**
  ```text
  Input:
  5
  8 3 6 1 5
  Output:
  1 3 5 6 8
  ```

##### Bài 1.4.2 — Dãy số giảm dần
- **Đề bài:** Đọc vào $N$ số nguyên và in các số theo thứ tự giảm dần.
- **Input:** $N$ và dãy $N$ số nguyên ($N \le 10^5$).
- **Output:** Dãy số sau khi sắp xếp giảm dần.
- **Sample:**
  ```text
  Input:
  6
  4 9 1 9 3 2
  Output:
  9 9 4 3 2 1
  ```

##### Bài 1.4.3 — Tìm phần tử lớn thứ K
- **Đề bài:** Cho mảng $N$ số nguyên ($1 \le K \le N \le 10^5$). Tìm phần tử lớn thứ $K$ trong mảng.
- **Sample:**
  ```text
  Input:
  5 2
  10 30 20 50 40
  Output:
  40
  ```

---

#### TẦNG B — VẬN DỤNG MẪU & KỸ THUẬT

##### Bài 1.4.4 — Sắp xếp chẵn trước lẻ sau
- **Đề bài:** Cho dãy $N$ số nguyên. Hãy sắp xếp sao cho các số chẵn đứng trước (tăng dần), các số lẻ đứng sau (tăng dần).
- **Sample:**
  ```text
  Input:
  6
  5 2 8 7 1 4
  Output:
  2 4 8 1 5 7
  ```

##### Bài 1.4.5 — Cặp đôi hoàn hảo
- **Đề bài:** Cho dãy $N$ số nguyên ($N \le 10^5$). Tìm hai phần tử có độ chênh lệch $|A_i - A_j|$ nhỏ nhất ($i \ne j$). In ra độ chênh lệch nhỏ nhất đó.
- **Sample:**
  ```text
  Input:
  4
  1 9 5 3
  Output:
  2
  ```
  *(Giải thích: Cặp $(1, 3)$ và $(3, 5)$ đều có hiệu là 2).*

##### Bài 1.4.6 — Đếm phần tử duy nhất
- **Đề bài:** Cho mảng $N$ số nguyên. Đếm xem có bao nhiêu phần tử chỉ xuất hiện **đúng 1 lần** trong mảng.
- **Sample:**
  ```text
  Input:
  6
  2 3 2 5 3 7
  Output:
  2
  ```
  *(Giải thích: Có 2 số chỉ xuất hiện 1 lần là số 5 và số 7).*

---

#### TẦNG C — NÂNG CAO & VẬN DỤNG THỰC TẾ

##### Bài 1.4.7 — Ghép số lớn nhất
- **Đề bài:** Cho $N$ số nguyên không âm ($N \le 10^5, A_i \le 10^9$). Hãy sắp xếp và ghép tất cả các số lại với nhau để tạo thành số có giá trị lớn nhất.
- **Gợi ý:** Dùng comparator xâu `bool cmp(string a, string b) { return a + b > b + a; }`.
- **Sample:**
  ```text
  Input:
  4
  3 30 34 5 9
  Output:
  9534330
  ```

##### Bài 1.4.8 — Thu gom rác tối ưu
- **Đề bài:** Trên một trục đường thẳng có $N$ thùng rác tại các tọa độ $X_1, X_2, \dots, X_N$. Một xe chở rác có thể chở tối đa 2 thùng mỗi chuyến. Tìm số chuyến xe ít nhất để thu gom hết các thùng rác nếu mỗi chuyến tổng khoảng cách từ gốc không vượt quá $D$.
- **Gợi ý:** Sắp xếp tọa độ tăng dần và dùng kỹ thuật tham lam kết hợp hai đầu mút.

---

### Code tham chiếu tổng hợp toàn chương

```cpp
#include <bits/stdc++.h>
using namespace std;

// 1. Thuat toan Selection Sort O(N^2)
void selectionSort(vector<int> &a) {
    int n = a.size();
    for (int i = 0; i < n - 1; i++) {
        int min_idx = i;
        for (int j = i + 1; j < n; j++) {
            if (a[j] < a[min_idx]) {
                min_idx = j;
            }
        }
        swap(a[i], a[min_idx]);
    }
}

// 2. Custom Comparator: Chan truoc (tang dan), Le sau (tang dan)
bool customComparator(int u, int v) {
    bool u_even = (abs(u) % 2 == 0);
    bool v_even = (abs(v) % 2 == 0);
    if (u_even != v_even) {
        return u_even;
    }
    return u < v;
}

// 3. Dem so gia tri phan biet O(N log N)
int countDistinct(vector<int> a) {
    if (a.empty()) return 0;
    sort(a.begin(), a.end());
    int cnt = 1;
    for (size_t i = 1; i < a.size(); i++) {
        if (a[i] != a[i - 1]) cnt++;
    }
    return cnt;
}

// 4. Tim khoang cach nho nhat O(N log N)
int minDifference(vector<int> a) {
    if (a.size() < 2) return 0;
    sort(a.begin(), a.end());
    int min_diff = a[1] - a[0];
    for (size_t i = 1; i < a.size() - 1; i++) {
        min_diff = min(min_diff, a[i + 1] - a[i]);
    }
    return min_diff;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << "Distinct elements: " << countDistinct(a) << "\n";
    cout << "Min difference: " << minDifference(a) << "\n";

    return 0;
}
```
