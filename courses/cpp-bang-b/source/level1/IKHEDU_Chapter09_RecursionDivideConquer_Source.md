# TÀI LIỆU GỐC — CHƯƠNG 9: ĐỆ QUY VÀ CHIA ĐỂ TRỊ (RECURSION & DIVIDE AND CONQUER)

## Bản đồ chương

| Trường | Nội dung |
|---|---|
| Mục tiêu | Nắm vững tư duy giải bài toán bằng cách gọi lại chính nó với quy mô nhỏ hơn (Đệ quy); làm chủ chiến lược Chia để trị (Divide and Conquer), thuật toán sắp xếp trộn Merge Sort và Lũy thừa nhị phân |
| Kiến thức cần có | Hàm, ngăn xếp lời gọi (Call Stack), điều kiện dừng (Base Case), độ phức tạp |
| Phạm vi | Cấu trúc hàm đệ quy, Lũy thừa nhị phân $\mathcal{O}(\log B)$, Thuật toán Merge Sort $\mathcal{O}(N \log N)$, Đếm số cặp nghịch thế |
| Số bài | 4 bài học lý thuyết & ví dụ mẫu + 1 bài luyện tập phân tầng |
| Tổng bài tập | 12 bài tập tự chứa (Tầng A: 4 bài, Tầng B: 4 bài, Tầng C: 4 bài) |

### Learning outcomes

Sau chương này, em có thể:
1. Viết đúng hàm đệ quy có điều kiện dừng (Base Case) rõ ràng và bước đệ quy tiến về điểm dừng — `LO-01`.
2. Cài đặt thuật toán Lũy thừa nhị phân tính $A^B$ trong thời gian $\mathcal{O}(\log B)$ — `LO-02`.
3. Trình bày và cài đặt hoàn chỉnh thuật toán sắp xếp Merge Sort $\mathcal{O}(N \log N)$ — `LO-03`.
4. Ứng dụng kỹ thuật trộn của Merge Sort để đếm số cặp nghịch thế trong $\mathcal{O}(N \log N)$ — `LO-04`.

### Câu hỏi trung tâm của chương

> **Làm thế nào để giải quyết một bài toán phức tạp bằng cách chia nó thành các bài toán con giống hệt nhưng có kích thước nhỏ hơn?**

---

### Bài 9.1 — Bản chất của Hàm đệ quy và Điều kiện dừng

#### 1. Khái niệm & Cấu trúc bắt buộc của Đệ quy
- **2 thành phần bắt buộc:**
  1. **Điều kiện dừng (Base Case):** Trường hợp đơn giản nhất trả về kết quả ngay lập tức để tránh tràn ngăn xếp `Stack Overflow`.
  2. **Bước đệ quy (Recursive Step):** Gọi lại hàm với tham số giảm dần về phía Base Case.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 9.1: Sinh Trưởng Của Quần Thể Sinh Vật Fibonacci**  
> **Bối cảnh:** Nhà sinh vật học theo dõi chu kỳ sinh sản của một loài sinh vật đặc hữu. Số cá thể trưởng thành tại thế hệ thứ $N$ tuân theo dãy Fibonacci: $F_0 = 0, F_1 = 1, F_N = F_{N-1} + F_{N-2}$. Đồng thời, số tổ hợp ghép cặp gen tại thế hệ $N$ tương ứng với giá trị giai thừa $N!$.  
> **Nhiệm vụ:** Em hãy viết hàm đệ quy tính giá trị $N!$ và số Fibonacci thứ $N$.  
> **Input:** `5` $\implies$ **Output:** `120 5`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

long long factorial(int n) {
    if (n <= 1) return 1;
    return 1LL * n * factorial(n - 1);
}

long long fibo(int n) {
    if (n == 0) return 0;
    if (n == 1) return 1;
    return fibo(n - 1) + fibo(n - 2);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    cout << factorial(n) << " " << fibo(n) << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 9.1

##### Bài 9.1.1 — Tổng Trọng Lượng Chữ Số Trong Mã Đơn Hàng
- **Bối cảnh:** Tính tổng các chữ số của mã số nguyên dương $N$ bằng đệ quy.
- **Input:** `1234` $\implies$ **Output:** `10`

##### Bài 9.1.2 — Trò Chơi Tháp Hà Nội Truyền Thống
- **Bối cảnh:** Chuyển $N$ đĩa từ cọc $A$ sang cọc $C$ qua cọc trung gian $B$. In các bước chuyển.
- **Input:** `2` $\implies$ **Output:** `A -> B`, `A -> C`, `B -> C`.

---

### Bài 9.2 — Lũy thừa nhị phân (Binary Exponentiation)

#### 1. Khái niệm & Thuật toán $\mathcal{O}(\log B)$
- Công thức chia đôi: $A^B = (A^{B/2})^2$ (nếu $B$ chẵn), $A^B = A \times (A^{B/2})^2$ (nếu $B$ lẻ).

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 9.2: Xác Thực Chữ Ký Số Hệ Thống Bảo Hiểm Xã Hội (BHXH)**  
> **Bối cảnh:** Hệ thống cổng dịch vụ công BHXH Việt Nam tính toán khóa chứng thực $A^B \pmod M$ với $B \le 10^{18}$.  
> **Input:** `2 10 1000000007` $\implies$ **Output:** `1024`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

long long powerMod(long long a, long long b, long long m) {
    if (b == 0) return 1 % m;
    long long half = powerMod(a, b / 2, m);
    long long res = (half * half) % m;
    if (b % 2 == 1) {
        res = (res * (a % m)) % m;
    }
    return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    long long a, b, m;
    if (!(cin >> a >> b >> m)) return 0;

    cout << powerMod(a, b, m) << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 9.2

##### Bài 9.2.1 — Lũy Thừa Nhanh Bằng Vòng Lặp Bit
- **Bối cảnh:** Cài đặt hàm tính $A^B \pmod M$ bằng vòng lặp `while (b > 0)`.
- **Input:** `3 5 1000` $\implies$ **Output:** `243`

##### Bài 9.2.2 — Đếm Số Dãy Nhị Phân Độ Dài N
- **Bối cảnh:** Tính $2^N \pmod{10^9+7}$ với $N \le 10^{18}$ bằng đệ quy lũy thừa nhị phân.
- **Input:** `10` $\implies$ **Output:** `1024`

---

### Bài 9.3 — Chiến lược Chia để trị và Thuật toán Merge Sort

#### 1. Khái niệm & 3 bước Chia để trị
1. **Divide:** Chia mảng thành 2 nửa tại $mid$.
2. **Conquer:** Sắp xếp đệ quy từng nửa.
3. **Combine:** Trộn (Merge) 2 nửa trong $\mathcal{O}(N)$. Tổng thời gian: $\mathcal{O}(N \log N)$.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 9.3: Sắp Xếp Danh Sách Điểm Thi Bằng Merge Sort**  
> **Bối cảnh:** Sắp xếp $N$ điểm số theo thứ tự tăng dần bằng thuật toán Merge Sort.  
> **Input:** `5` \ `5 2 4 1 3` $\implies$ **Output:** `1 2 3 4 5`.

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

void merge(vector<int> &a, int l, int mid, int r) {
    vector<int> leftArr(a.begin() + l, a.begin() + mid + 1);
    vector<int> rightArr(a.begin() + mid + 1, a.begin() + r + 1);

    int i = 0, j = 0, k = l;
    while (i < (int)leftArr.size() && j < (int)rightArr.size()) {
        if (leftArr[i] <= rightArr[j]) a[k++] = leftArr[i++];
        else a[k++] = rightArr[j++];
    }
    while (i < (int)leftArr.size()) a[k++] = leftArr[i++];
    while (j < (int)rightArr.size()) a[k++] = rightArr[j++];
}

void mergeSort(vector<int> &a, int l, int r) {
    if (l >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(a, l, mid);
    mergeSort(a, mid + 1, r);
    merge(a, l, mid, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    mergeSort(a, 0, n - 1);
    for (int i = 0; i < n; i++) cout << a[i] << (i + 1 == n ? "" : " ");
    cout << "\n";

    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 9.3

##### Bài 9.3.1 — Sắp Xếp Giảm Dần Bằng Merge Sort
- **Bối cảnh:** Sửa đổi bước trộn để sắp xếp mảng $N$ phần tử theo thứ tự giảm dần.
- **Input:** `4` \ `1 4 2 8` $\implies$ **Output:** `8 4 2 1`

##### Bài 9.3.2 — Trộn Hai Dãy Đã Sắp Xếp Không Dùng Mảng Phụ
- **Bối cảnh:** Trộn hai dãy đã sắp xếp $A$ và $B$ in ra màn hình trong $\mathcal{O}(N + M)$.
- **Input:** `2 2` \ `1 5` \ `2 4` $\implies$ **Output:** `1 2 4 5`

---

### Bài 9.4 — Ứng dụng: Đếm số cặp nghịch thế (Inversions Counting)

#### 1. Khái niệm & Thuật toán $\mathcal{O}(N \log N)$
- Đếm số cặp $(i, j)$ có $i < j$ nhưng $A[i] > A[j]$ thông qua bước trộn Merge Sort.

---

#### 2. Bài toán mẫu có hướng dẫn

> **Bài toán mẫu 9.4: Đánh Giá Mức Độ Xáo Trộn Bảng Xếp Hạng V-League**  
> **Bối cảnh:** Ban tổ chức giải bóng đá V-League cần đo lường mức độ xáo trộn thứ hạng của các câu lạc bộ so với mùa giải trước thông qua số cặp nghịch thế trong bảng điểm $A_1, A_2, \dots, A_N$.  
> **Input:** `5` \ `2 4 1 3 5` $\implies$ **Output:** `3` (các cặp: (2, 1), (4, 1), (4, 3)).

#### Cài đặt C++
```cpp
#include <bits/stdc++.h>
using namespace std;

long long mergeAndCount(vector<int> &a, int l, int mid, int r) {
    vector<int> leftArr(a.begin() + l, a.begin() + mid + 1);
    vector<int> rightArr(a.begin() + mid + 1, a.begin() + r + 1);

    int i = 0, j = 0, k = l;
    long long invCount = 0;

    while (i < (int)leftArr.size() && j < (int)rightArr.size()) {
        if (leftArr[i] <= rightArr[j]) {
            a[k++] = leftArr[i++];
        } else {
            a[k++] = rightArr[j++];
            invCount += (leftArr.size() - i);
        }
    }
    while (i < (int)leftArr.size()) a[k++] = leftArr[i++];
    while (j < (int)rightArr.size()) a[k++] = rightArr[j++];

    return invCount;
}

long long mergeSortAndCount(vector<int> &a, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    long long count = 0;
    count += mergeSortAndCount(a, l, mid);
    count += mergeSortAndCount(a, mid + 1, r);
    count += mergeAndCount(a, l, mid, r);
    return count;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<int> a(n);
    for (int i = 0; i < n; i++) cin >> a[i];

    cout << mergeSortAndCount(a, 0, n - 1) << "\n";
    return 0;
}
```

---

#### 3. Bài tập thực hành Bài 9.4

##### Bài 9.4.1 — Đếm Số Cặp Nghịch Thế Cho Dãy Đảo Ngược
- **Bối cảnh:** Cho dãy giảm dần $N, N-1, \dots, 1$. Tính số cặp nghịch thế: $\frac{N(N-1)}{2}$.
- **Input:** `4` \ `4 3 2 1` $\implies$ **Output:** `6`

##### Bài 9.4.2 — Kiểm Tra Dãy Đã Sắp Xếp Bằng Số Nghịch Thế
- **Bối cảnh:** Dãy có 0 cặp nghịch thế khi và chỉ khi nó đã được sắp xếp tăng dần. In `YES` nếu invCount = 0, ngược lại in `NO`.
- **Input:** `3` \ `1 2 3` $\implies$ **Output:** `YES`

---

### Bài 9.5 — Luyện tập tổng hợp và đánh giá chương

### Đề bài 12 bài tập phân tầng tự chứa (iKHEDU Standard)

#### Tầng A — Củng cố nền tảng (Rating 1000 - 1200)
##### Bài 9.5.1 — Tổng Trọng Lượng Kiện Hàng Đệ Quy
- **Bối cảnh:** Tính tổng mảng bằng đệ quy.
##### Bài 9.5.2 — Tháp Truyền Tín Hiệu Hà Nội
- **Bối cảnh:** In các bước di chuyển tháp Hà Nội.
##### Bài 9.5.3 — Lũy Thừa Nhanh Khóa Bảo Mật
- **Bối cảnh:** Tính $A^B \pmod{10^9+7}$.
##### Bài 9.5.4 — Đảo Ngược Số Báo Danh
- **Bối cảnh:** In ngược chữ số bằng đệ quy.

#### Tầng B — Vận dụng thi đấu (Rating 1200 - 1500)
##### Bài 9.5.5 — Đếm Cặp Nghịch Thế Bảng Điểm Thí Sinh
- **Bối cảnh:** Đếm số nghịch thế $N \le 10^5$.
##### Bài 9.5.6 — Số Fibonacci Thế Hệ Thứ $10^{18}$
- **Bối cảnh:** Lũy thừa ma trận nhị phân.
##### Bài 9.5.7 — Khoảng Cách Hai Trạm Cảm Biến 1D Gần Nhất
- **Bối cảnh:** Chia để trị $\mathcal{O}(N \log N)$.
##### Bài 9.5.8 — Sinh Toàn Bộ Chuỗi Ngoặc Hợp Lệ
- **Bối cảnh:** Quay lui sinh dãy ngoặc đúng độ dài $2N$.

#### Tầng C — Chuyển giao & Nâng cao (Rating 1500 - 1800)
##### Bài 9.5.9 — Cặp Điểm Gần Nhất Trên Bản Đồ 2D - Closest Pair of Points
- **Bối cảnh:** Chia để trị $\mathcal{O}(N \log N)$.
##### Bài 9.5.10 — Nhân Đa Thức Siêu Tốc Karatsuba
- **Bối cảnh:** Nhân 2 số lớn trong $\mathcal{O}(N^{1.585})$.
##### Bài 9.5.11 — Đoạn Tăng Trưởng Doanh Thu Lớn Nhất Bằng Chia Để Trị
- **Bối cảnh:** Maximum Subarray $\mathcal{O}(N \log N)$.
##### Bài 9.5.12 — Vẽ Bản Đồ Fractal Hoa Tuyết Koch
- **Bối cảnh:** Đệ quy vẽ Fractal $3^N \times 3^N$.

---

### Bẫy lỗi thường gặp & Rubric đánh giá
| Lỗi thường gặp | Cách kiểm soát |
|---|---|
| Thiếu Base Case gây lỗi tràn bộ nhớ Call Stack (`Stack Overflow`) | Luôn viết Base Case đầu tiên trong hàm |
| Quên dùng `long long` cho biến đếm nghịch thế khi $N = 2 \times 10^5$ (số nghịch thế tối đa $\approx 2 \times 10^{10}$) | Biến đếm nghịch thế bắt buộc là kiểu `long long` |

### Rubric hoàn thành chương
| Mức độ | Tiêu chí đánh giá |
|---|---|
| **Cơ bản (Tầng A)** | Viết được hàm đệ quy dừng đúng và cài đặt lũy thừa nhị phân $\mathcal{O}(\log B)$. |
| **Vận dụng (Tầng B)** | Cài đặt chính xác Merge Sort và đếm số cặp nghịch thế trong $\mathcal{O}(N \log N)$. |
| **Thành thạo (Tầng C)** | Áp dụng tư duy Chia để trị cho bài toán hình học 2D và nhân số lớn Karatsuba. |
