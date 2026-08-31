# CHUYÊN ĐỀ 11: KỸ THUẬT CHIA ĐỂ TRỊ (DIVIDE AND CONQUER)

---

## 1. Cầu Nối Tư Duy: Recurrence $\to$ Recursion Tree $\to$ Complexity

Ở Chuyên đề 10, chúng ta đã làm chủ kỹ thuật Đệ quy: giải bài toán quy mô $N$ bằng cách thu nhỏ dần bài toán. Từ cấu trúc code đệ quy, ta có thể thiết lập **Hệ thức truy hồi (Recurrence)** và phân tích qua **Cây đệ quy (Recursion Tree)** để tìm ra độ phức tạp chính xác:

$$\text{Code Đệ Quy} \longrightarrow \text{Hệ Thức Truy Hồi (Recurrence)} \longrightarrow \text{Cây Đệ Quy (Recursion Tree)} \longrightarrow \text{Độ Phức Tạp (Complexity)}$$

* **Đệ quy tuyến tính (Chuyên đề 10):**
  $$T(N) = T(N-1) + \mathcal{O}(1) \implies \text{Cây 1 nhánh thẳng, độ sâu } N \implies \Theta(N)$$
* **Đệ quy phân nhánh chia đôi (Chuyên đề 11):**
  $$T(N) = 2T\left(\frac{N}{2}\right) + \mathcal{O}(N) \implies \text{Cây nhị phân đầy đủ, chiều cao } \log_2 N \implies \Theta(N \log N)$$
* **Đệ quy phân nhánh giảm 1 (Chuyên đề 10):**
  $$T(N) = 2T(N-1) + \mathcal{O}(1) \implies \text{Cây nhị phân bùng nổ, } 2^N \text{ lá} \implies \Theta(2^N)$$

> **Quy luật cốt lõi:** "Đệ quy" chỉ là cơ chế cài đặt; cấu trúc cây lời gọi và khối lượng công việc ở mỗi tầng mới là yếu tố quyết định độ phức tạp.

---

## 2. Phân Biệt Cốt Lõi: Đệ Quy (Recursion) $\ne$ Chia Để Trị (Divide & Conquer)

Học sinh rất dễ nhầm lẫn giữa hai khái niệm này:

| Khái Niệm | Bản Chất | Ví Dụ Điển Hình |
|---|---|---|
| **Đệ Quy (Recursion)** | **Cơ chế thực thi:** Kỹ thuật lập trình trong đó một hàm tự gọi lại chính nó thông qua Call Stack. | Tính $N!$, Fibonacci, Duyệt mảng tuần tự. |
| **Chia Để Trị (D&C)** | **Chiến lược thiết kế thuật toán:** Phân rã bài toán thành các bài toán con cùng bản chất nhưng nhỏ hơn, giải từng phần và gộp lại. | Merge Sort, Inversion Count, Closest Pair. |

* Tính $N! = N \times (N-1)!$ là **Đệ quy** nhưng **không phải D&C** (vì chỉ thu nhỏ 1 phần tử mà không có bước chia và gộp cấu trúc).
* Merge Sort là **D&C hoàn chỉnh** sử dụng cơ chế Đệ quy để điều khiển.

---

## 3. Bản Chất Vấn Đề & Hai Kiểu Phân Rã: Divide vs Partition

**Divide & Conquer** là chiến lược phân rã một bài toán thành các bài toán con có cùng bản chất nhưng kích thước nhỏ hơn, giải các bài toán con, rồi kết hợp kết quả lại để thu được lời giải cho bài toán ban đầu.

### Phân Biệt Hai Kiểu Phân Rã Dữ Liệu:
1. **Divide (Phân chia theo vị trí chỉ số):**
   * Chia cố định theo chỉ số mảng (thường là tại trung điểm `mid = l + (r - l) / 2`).
   * *Ví dụ:* Merge Sort chia `[1 2 3 4 5 6 7 8]` thành `[1 2 3 4]` và `[5 6 7 8]`.
2. **Partition (Phân hoạch theo quan hệ với Pivot):**
   * Chia động dựa trên việc so sánh các phần tử với một giá trị chốt (`pivot`), kích thước 2 nửa có thể không đều nhau.
   * *Ví dụ:* QuickSelect phân hoạch `[7 2 9 1 5 3 8]` với `pivot = 5` thành `[2 1 3]` (nhỏ hơn 5), `[5]`, và `[7 9 8]` (lớn hơn 5).

![Mô hình Thuật toán Chia để trị (Divide & Conquer)](file:///Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-11-chia-de-tri/assets/dnc_model_vi.svg)

---

## 4. Khung Tư Duy D&C (The D&C Mental Model)

Trước bất kỳ bài toán nào nghi ngờ sử dụng Chia Để Trị, hãy luôn trả lời **4 câu hỏi định hướng**:

1. **Tôi chia bài toán ở đâu?** (Tại điểm giữa `mid`, theo trục tọa độ $x$, hay qua `pivot`?)
2. **Bài toán con có kích thước bao nhiêu?** ($N/2, N_1, N_2$?)
3. **Tôi cần giải bao nhiêu bài toán con?** (Chỉ 1 nhánh như Binary Search/QuickSelect hay cả 2 nhánh như Merge Sort?)
4. **Tôi combine kết quả của các bài toán con như thế nào?** (Đây là bước quyết định độ phức tạp!)

![Cây quyết định lựa chọn thuật toán Chia để trị](file:///Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-11-chia-de-tri/assets/dnc_decision_tree_vi.svg)

---

## 5. Mô Phỏng Từng Bước Thuật Toán Sắp Xếp Trộn (Merge Sort Simulation)

Xét mảng ban đầu: `A = [38, 27, 43, 3, 9, 82, 10]`.

### Sơ Đồ Cây Phân Rã & Gộp Mảng (Divide & Merge Tree):

![Mô phỏng Cây phân rã và gộp Merge Sort](file:///Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-11-chia-de-tri/assets/mergesort_tree_vi.svg)

---

## 6. Combine Step & Loop Invariant — Trái Tim Của Divide & Conquer

> **Chân lý sư phạm:** Sức mạnh và sự tinh tế của Chia Để Trị không nằm ở việc "bẻ nhỏ bài toán", mà nằm ở **cách ta xử lý và kết hợp (Combine) các kết quả ở pha Unwinding**.

### Bất Biến Vòng Lặp (Loop Invariant) Trong Hàm `merge()`:
Khi gộp 2 mảng con đã sắp xếp `a[l..mid]` và `a[mid+1..r]` vào `temp`:
* **Bất biến:** Tại mỗi bước lặp, mảng đệm `temp[l..k-1]` luôn chứa chính xác $(k - l)$ phần tử nhỏ nhất đã được chọn từ hai nửa `a[l..mid]` và `a[mid+1..r]` theo thứ tự không giảm.
* **Quy tắc chọn:**
  * Nếu $a[i] \le a[j]$: Chọn $a[i]$ đưa vào `temp[k]`, tăng `i` và `k` (điều kiện $\le$ bảo toàn tính **Stable Sort**).
  * Nếu $a[i] > a[j]$: Chọn $a[j]$ đưa vào `temp[k]`, tăng `j` và `k`.

---

## 7. Bảng Trực Giác Recurrence & Định Lý Thợ (Master Theorem)

Trước khi dùng công thức tổng quát, hãy nắm vững **4 hệ thức truy hồi kinh điển**:

| Hệ Thức Truy Hồi | Cấu Trúc Nhánh | Chi Phí Từng Tầng | Độ Phức Tạp | Thuật Toán Tiêu Biểu |
|---|---|---|:---:|---|
| $T(N) = T(N/2) + \mathcal{O}(1)$ | 1 nhánh, giảm nửa | $\mathcal{O}(1)$ mỗi tầng | $\Theta(\log N)$ | Binary Search |
| $T(N) = T(N/2) + \mathcal{O}(N)$ | 1 nhánh, quét $N$ | $N + N/2 + N/4 + \dots$ | $\Theta(N)$ (Expected) | QuickSelect |
| $T(N) = 2T(N/2) + \mathcal{O}(1)$| 2 nhánh, gộp $\mathcal{O}(1)$ | Số lá $N$ thống trị | $\Theta(N)$ | Tìm Min/Max chia đôi |
| $T(N) = 2T(N/2) + \mathcal{O}(N)$| 2 nhánh, gộp $\mathcal{O}(N)$ | Mỗi tầng đều tốn $\mathcal{O}(N)$ | $\Theta(N \log N)$ | Merge Sort, Inversion |

### Công Thức Tổng Quát (Master Theorem):
Với $T(N) = a \cdot T(N/b) + \Theta(N^d)$ ($a \ge 1, b > 1$):
1. **$a < b^d$ ($\log_b a < d$):** Chi phí ngoài đệ quy thống trị $\implies T(N) = \Theta(N^d)$.
2. **$a = b^d$ ($\log_b a = d$):** Chi phí phân bố đều trên $\log_b N$ tầng $\implies T(N) = \Theta(N^d \log N)$.
3. **$a > b^d$ ($\log_b a > d$):** Số nút lá bùng nổ thống trị $\implies T(N) = \Theta(N^{\log_b a})$ *(ví dụ Karatsuba $a=3, b=2, d=1 \implies \Theta(N^{\log_2 3}) \approx \Theta(N^{1.585})$)*.

---

## 8. Bảng Nhận Diện Dấu Hiệu Thuật Toán (D&C Pattern Recognition)

| Dấu Hiệu Đặc Trưng | Mô Hình Thuật Toán D&C Phù Hợp |
|---|---|
| Mảng đã sắp xếp + cần tìm kiếm một giá trị | **Binary Search đệ quy** (D&C đơn nhánh) |
| Chia đôi mảng + cần sắp xếp cả 2 nửa | **Merge Sort** (D&C đa nhánh + Combine 2 con trỏ) |
| Cần đếm số cặp phần tử có quan hệ giữa 2 nửa | **Inversion Counting** (Đếm khi Merge) |
| Cần tìm phần tử nhỏ thứ $K$ trên mảng chưa sắp xếp | **QuickSelect** (Partition chọn 1 nhánh) |
| Tìm max / min trong mô hình cây thi đấu đấu loại | **Tournament Tree** (Lưu lịch sử đối đầu) |
| Tìm đoạn con liên tiếp có tính chất tối ưu | **Maximum Subarray D&C** (Xét đoạn vắt qua `mid`) |
| Tập điểm trong không gian 2D cần tìm khoảng cách min | **Closest Pair of Points** (Chia hoành độ + Quét Strip) |
| Tìm trung vị của 2 dãy đã sắp xếp | **Binary Partition D&C** ($\mathcal{O}(\log(\min)))$ |

---

## 9. Chuỗi Chuyển Giao Tri Thức: Merge $\to$ Merge Sort $\to$ Inversion Counting

Điểm đặc sắc nhất của chuyên đề là **chuỗi kế thừa thuật toán**:

$$\text{Merge Step (2 con trỏ)} \longrightarrow \text{Merge Sort } \Theta(N \log N) \longrightarrow \text{Đếm Nghịch Thế (Inversion Count)}$$

### Ứng Dụng Đỉnh Cao: Đếm Cặp Nghịch Thế (Inversion Counting) $\mathcal{O}(N \log N)$
* **Khái niệm:** Cặp nghịch thế là cặp chỉ số $(i, j)$ sao cho $i < j$ nhưng $A_i > A_j$.
* **Bất biến gộp kỳ diệu:** Khi chia mảng thành `Left[l..mid]` và `Right[mid+1..r]` đã sắp xếp:
  * Khi duyệt con trỏ `i` trên `Left` và `j` trên `Right`, nếu $L[i] > R[j]$, thì do $L$ đã sắp xếp tăng dần, **toàn bộ các phần tử từ $L[i]$ đến $L[mid]$ đều lớn hơn $R[j]$**!
  * Ta cộng ngay một lượng bằng $(mid - i + 1)$ vào biến đếm nghịch thế trong **$\mathcal{O}(1)$ thao tác cộng dồn**.
  * Bước `merge` vẫn tốn $\mathcal{O}(N)$ thời gian, giúp tổng thời gian đếm toàn bộ mảng đạt $\Theta(N \log N)$ chuẩn thi đấu thay vì $\mathcal{O}(N^2)$ vét cạn.

---

## 10. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)

1. **Bẫy cấp phát bộ nhớ đệm trong Merge Sort:**
   * Việc tạo các `vector` mới bên trong mỗi lần gọi `mergeSort()` gây thêm nhiều lần cấp phát/giải phóng động và sao chép dữ liệu, làm tăng constant factor.
   * **Cách phòng chống:** Khai báo một mảng đệm toàn cục duy nhất `vector<long long> temp(N);` và truyền tham chiếu vào hàm đệ quy để tái sử dụng cho mọi bước gộp, giữ Auxiliary Memory ở mức $\Theta(N)$.
2. **Tràn số nguyên 32-bit khi đếm số cặp nghịch thế:**
   * Số lượng cặp nghịch thế tối đa của mảng $N = 10^5$ là $N(N-1)/2 \approx 5 \times 10^9$ (vượt giới hạn của `int` $2 \times 10^9$).
   * **Cách phòng chống:** Biến đếm nghịch thế bắt buộc dùng kiểu `long long`.
3. **Bẫy tràn số khi tính Midpoint:**
   * Viết `mid = (l + r) / 2;` có thể tràn `int` khi $l + r > 2 \cdot 10^9$. Luôn viết: `mid = l + (r - l) / 2;`.
4. **Bẫy bỏ sót đoạn crossing trong Maximum Subarray:**
   * Đoạn con lớn nhất có thể nằm trọn bên trái, trọn bên phải, hoặc vắt ngang qua tâm `mid`. Bắt buộc phải tính `maxCrossingSum` từ `mid` lan sang 2 phía.

---

## 11. Mẫu Cài Đặt Chuẩn Thi Đấu (Competitive Templates)

```cpp
# include <bits/stdc++.h>
using namespace std;

using ll = long long;

// 1. Thuật toán Merge Sort chuẩn O(N log N) dùng buffer tái sử dụng
void merge(vector<ll> &a, vector<ll> &temp, int l, int mid, int r) {
    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        // <= giữ tính stable: phần tử bên trái thắng khi bằng nhau
        if (a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
}

void mergeSort(vector<ll> &a, vector<ll> &temp, int l, int r) {
    if (l >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(a, temp, l, mid);
    mergeSort(a, temp, mid + 1, r);
    merge(a, temp, l, mid, r);
}

// 2. Thuật toán Đếm Số Cặp Nghịch Thế O(N log N)
ll countInversions(vector<ll> &a, vector<ll> &temp, int l, int r) {
    if (l >= r) return 0;
    int mid = l + (r - l) / 2;
    ll inv = 0;
    inv += countInversions(a, temp, l, mid);
    inv += countInversions(a, temp, mid + 1, r);

    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) {
            temp[k++] = a[i++];
        } else {
            temp[k++] = a[j++];
            inv += (mid - i + 1); // Đếm O(1) nhờ cấu trúc đã sắp xếp
        }
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
    return inv;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<ll> a = {38, 27, 43, 3, 9, 82, 10};
    int n = a.size();
    vector<ll> temp(n);

    cout << "So cap nghich the: " << countInversions(a, temp, 0, n - 1) << "\n";
    return 0;
}
```

---

## 12. Hệ Thống Câu Hỏi Kiểm Tra Khái Niệm (Concept Quiz)

#### Câu 1 (Bản chất 3 giai đoạn Chia để trị):
Ba bước cơ bản trong một giải thuật Chia để trị (Divide and Conquer) diễn ra theo thứ tự nào sau đây?
* A. `Solve` $\to$ `Divide` $\to$ `Combine`.
* B. **(Đáp án đúng)** `Divide` (Chia bài toán) $\to$ `Solve` (Trị / Giải đệ quy các bài toán con) $\to$ `Combine` (Gộp kết quả).
* C. `Combine` $\to$ `Divide` $\to$ `Solve`.
* D. `Divide` $\to$ `Combine` $\to$ `Solve`.
> *Giải thích:* Giải thuật D&C trước hết chia bài toán lớn thành các phần độc lập, giải đệ quy từng phần, sau đó gộp kết quả lại ở pha Unwinding.

---

#### Câu 2 (Suy luận hệ thức truy hồi từ cấu trúc code):
Quan sát đoạn mã đệ quy sau:
```cpp
void process(int n) {
    if (n <= 1) return;
    process(n / 2);
    process(n / 2);
    for (int i = 0; i < n; i++) {
        // Thao tác xử lý tốn O(1)
    }
}
```
Hệ thức truy hồi (Recurrence) mô tả chính xác thời gian thực thi `T(n)` của hàm trên là:
* A. `T(n) = T(n / 2) + O(n)`
* B. **(Đáp án đúng)** `T(n) = 2 * T(n / 2) + O(n)`
* C. `T(n) = T(n - 1) + O(n)`
* D. `T(n) = 2 * T(n - 1) + O(1)`
> *Giải thích:* Hàm tạo ra 2 lời gọi đệ quy kích thước `n / 2` và một vòng lặp `for` chạy `n` lần tốn chi phí ngoài đệ quy `f(n) = O(n)`. Theo Master Theorem, `T(n) = Theta(n log n)`.

---

#### Câu 3 (So sánh bản chất: Cùng chia đôi nhưng khác biệt độ phức tạp):
Hai thuật toán A (`T(N) = T(N/2) + O(1)`) và B (`T(N) = 2T(N/2) + O(N)`) đều chia đôi mảng ở mỗi bước. Lý do cốt lõi khiến thuật toán A đạt `O(log N)` trong khi B tốn `O(N log N)` là gì?
* A. Thuật toán A không dùng ngôn ngữ C++.
* B. **(Đáp án đúng)** Thuật toán A chỉ đi vào 1 nhánh duy nhất với chi phí mỗi tầng `O(1)`, trong khi thuật toán B bắt buộc phải giải cả 2 nhánh và tốn chi phí gộp `O(N)` trên mỗi tầng trong tổng số `log2 N` tầng.
* C. Thuật toán B tiêu tốn nhiều bộ nhớ RAM hơn.
* D. Thuật toán A chỉ chạy trên số nguyên dương.
> *Giải thích:* Số lượng nhánh đệ quy được khám phá và chi phí gộp ngoài đệ quy quyết định toàn bộ sự khác biệt giữa $\mathcal{O}(\log N)$ và $\mathcal{O}(N \log N)$.

---

#### Câu 4 (Kiểu dữ liệu cho đếm cặp nghịch thế):
Với mảng có `N = 10^5` phần tử, biến lưu trữ tổng số cặp nghịch thế bắt buộc phải có kiểu dữ liệu nào để chống tràn số?
* A. `int`
* B. `float`
* C. **(Đáp án đúng)** `long long` (vì số cặp nghịch thế tối đa lên tới `N*(N-1)/2 approx 5*10^9`, vượt quá giới hạn 32-bit).
* D. `bool`
> *Giải thích:* Mảng giảm dần hoàn toàn có số cặp nghịch thế bằng `N*(N-1)/2`, vượt ngưỡng $2 \times 10^9$ của `int` 32-bit.

---

#### Câu 5 (Cơ chế đếm cặp nghịch thế khi Merge):
Trong thuật toán đếm số cặp nghịch thế bằng Merge Sort, khi con trỏ `i` trỏ vào nửa trái `Left[l..mid]` và con trỏ `j` trỏ vào nửa phải `Right[mid+1..r]`, nếu `Left[i] > Right[j]`, số lượng cặp nghịch thế được cộng thêm vào kết quả trong $\mathcal{O}(1)$ là bao nhiêu?
* A. Đúng `1` cặp.
* B. **(Đáp án đúng)** `mid - i + 1` cặp.
* C. `j - mid` cặp.
* D. `r - l + 1` cặp.
> *Giải thích:* Vì mảng con `Left` đã được sắp xếp tăng dần, nên nếu `Left[i] > Right[j]` thì tất cả các phần tử từ chỉ số `i` đến `mid` trong mảng `Left` đều lớn hơn `Right[j]`.

---

#### Câu 6 (Bẫy Maximum Subarray D&C):
Khi tìm đoạn con có tổng lớn nhất bằng Chia để trị trên đoạn `[l, r]`, ngoài đoạn con lớn nhất nằm trọn ở nửa trái và trọn ở nửa phải, ta bắt buộc phải xem xét thêm trường hợp nào?
* A. Đoạn con rỗng.
* B. **(Đáp án đúng)** Đoạn con lớn nhất bắt đầu từ nửa trái kéo dài qua tâm `mid` sang nửa phải (Crossing Subarray).
* C. Toàn bộ mảng ban đầu.
* D. Phần tử nhỏ nhất trong mảng.
> *Giải thích:* Đoạn con tối ưu có thể vắt ngang qua ranh giới phân chia giữa hai nửa mảng.

---

#### Câu 7 (Tối ưu bộ nhớ trong Merge Sort):
Để tối ưu thời gian thực thi và tránh overhead cấp phát bộ nhớ động trong hàm `mergeSort()`, kỹ thuật cài đặt chuẩn thi đấu là gì?
* A. Khai báo `vector<long long>` mới trong mỗi lần gọi hàm `merge()`.
* B. **(Đáp án đúng)** Khai báo một mảng đệm tạm duy nhất `vector<long long> temp(N)` và truyền tham chiếu vào hàm đệ quy để tái sử dụng cho mọi bước gộp.
* C. Dùng vòng lặp `while(true)`.
* D. Ép kiểu toàn bộ mảng sang chuỗi ký tự.
> *Giải thích:* Tái sử dụng một vùng nhớ đệm duy nhất giúp tránh việc cấp phát/giải phóng nhiều buffer trong quá trình đệ quy, giảm overhead và giữ auxiliary memory ở mức $\Theta(N)$.

---

#### Câu 8 (Tournament Tree tìm phần tử lớn thứ hai với $N = 2^k$):
Trên mảng có kích thước $N = 2^k$ ($N$ là lũy thừa của $2$), bằng kỹ thuật Tournament Tree (cây thi đấu), số phép so sánh tối thiểu để tìm ra phần tử lớn thứ hai là:
* A. `2 * N`
* B. **(Đáp án đúng)** `N + log2(N) - 2` phép so sánh.
* C. `N^2`
* D. `N log N`
> *Giải thích:* Tìm nhà vô địch tốn $N - 1$ phép so sánh. Phần tử lớn thứ hai bắt buộc phải là một trong những phần tử từng thua trực tiếp nhà vô địch trong cây thi đấu (đúng $\log_2 N$ phần tử). Tìm max trong nhóm này tốn thêm $\log_2 N - 1$ phép $\implies$ Tổng cộng đúng $(N - 1) + (\log_2 N - 1) = N + \log_2 N - 2$ phép.

---

#### Câu 9 (Đặc tính Stable Sort của Merge Sort):
Merge Sort được gọi là thuật toán sắp xếp ổn định (Stable Sort) vì lý do nào sau đây?
* A. Thuật toán chạy không bao giờ bị lỗi bộ nhớ.
* B. **(Đáp án đúng)** Trong bước gộp `merge()`, khi hai phần tử có giá trị bằng nhau (`a[i] == a[j]`), thuật toán luôn ưu tiên chọn phần tử ở nửa trái (`i`) trước nhờ điều kiện `a[i] <= a[j]`, giữ nguyên thứ tự xuất hiện ban đầu.
* C. Thuật toán có độ phức tạp như nhau trong mọi trường hợp.
* D. Thuật toán không sử dụng phép nhân.
> *Giải thích:* Bất biến chọn phần tử bên trái khi bằng nhau bảo toàn tính thứ tự tương đối của các phần tử có khóa bằng nhau.

---

#### Câu 10 (Lũy thừa ma trận chia để trị):
Tính lũy thừa ma trận vuông $A^N$ cấp $2 \times 2$ modulo $M$ bằng Chia để trị có độ phức tạp thời gian tiệm cận là:
* A. `Theta(N)`
* B. `Theta(N^2)`
* C. **(Đáp án đúng)** `Theta(log N)` (mỗi phép nhân ma trận $2 \times 2$ tốn $\mathcal{O}(1)$ với 8 phép nhân số học).
* D. `Theta(1)`
> *Giải thích:* Thuật toán chia đôi số mũ $N \to N/2$ sau mỗi bước tương tự như lũy thừa nhị phân số học, độ sâu đệ quy là $\log_2 N$.

---

## 13. Ma Trận 16 Bài Tập Thực Hành Đa Chiều (Time / Call Stack / Auxiliary Memory / Max Depth)

### Phân Tầng Lộ Trình Học Tập Lesson 11:
* **Nhóm Cốt Lõi (Core Foundations - `CPPB-DAC-01` $\to$ `12`):** Binary Search D&C, RMQ D&C, Tournament Tree, Cài đặt Merge Step, Merge Sort trọn vẹn, Đếm số cặp nghịch thế, Maximum Subarray D&C, Majority Element Voting, Lũy thừa ma trận $2 \times 2$, Đỉnh mảng Unimodal, Tổng cấp số nhân D&C, Đếm cặp $A_i > 2A_j$.
* **Nhóm Nâng Cao & Thử Thách (Advanced & Challenge `CPPB-DAC-13` $\to$ `16`):** QuickSelect D&C ($\mathcal{O}(N)$ expected), Đếm đoạn con tổng nằm trong $[L, R]$, Cặp điểm gần nhất trong mặt phẳng (Closest Pair $\mathcal{O}(N \log N)$), Median của 2 mảng đã sắp xếp ($\mathcal{O}(\log(\min(N, M)))$).

| STT | Mã Bài | Tên Bài Toán | Cấp Độ | Phân Loại | Time Complexity | Call Stack | Aux Memory | Max Depth |
|:---:|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 01 | `CPPB-DAC-01` | **Tìm Kiếm Nhị Phân Bằng Đệ Quy (Cầu Nối D&C)** | `P0` | **Core** | $\Theta(\log N)$ | $\Theta(\log N)$ | $\mathcal{O}(1)$ | $\log_2 N$ |
| 02 | `CPPB-DAC-02` | **Tìm Min Trên Đoạn Bằng Chia Để Trị (RMQ D&C)**| `P0` | **Core** | $\Theta(N)$ | $\Theta(\log N)$ | $\mathcal{O}(1)$ | $\log_2 N$ |
| 03 | `CPPB-DAC-03` | **Tìm Phần Tử Lớn Thứ Hai (Tournament Tree)**| `P1` | **Core** | $\Theta(N)$ | $\Theta(\log N)$ | $\Theta(\log N)$ | $\log_2 N$ |
| 04 | `CPPB-DAC-04` | **Gộp Hai Mảng Đã Sắp Xếp (Merge Step)** | `P1` | **Core** | $\Theta(N + M)$ | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $1$ |
| 05 | `CPPB-DAC-05` | **Thuật Toán Sắp Xếp Trộn (Merge Sort)** | `P2` | **Core** | $\Theta(N \log N)$ | $\Theta(\log N)$ | $\Theta(N)$ | $\log_2 N$ |
| 06 | `CPPB-DAC-06` | **Đếm Số Cặp Nghịch Thế (Inversion Count)** | `P2` | **Core** | $\Theta(N \log N)$ | $\Theta(\log N)$ | $\Theta(N)$ | $\log_2 N$ |
| 07 | `CPPB-DAC-07` | **Đoạn Con Tổng Lớn Nhất (Maximum Subarray)** | `P2` | **Core** | $\Theta(N \log N)$ | $\Theta(\log N)$ | $\mathcal{O}(1)$ | $\log_2 N$ |
| 08 | `CPPB-DAC-08` | **Tìm Phần Tử Đa Số (Majority Element) D&C** | `P2` | **Core** | $\Theta(N \log N)$ | $\Theta(\log N)$ | $\mathcal{O}(1)$ | $\log_2 N$ |
| 09 | `CPPB-DAC-09` | **Lũy Thừa Ma Trận Chia Để Trị $2 \times 2$** | `P3` | **Core** | $\Theta(\log N)$ | $\Theta(\log N)$ | $\mathcal{O}(1)$ | $\log_2 N$ |
| 10 | `CPPB-DAC-10` | **Tìm Điểm Cực Đại Mảng Unimodal (Peak Index)**| `P3` | **Core** | $\Theta(\log N)$ | $\Theta(\log N)$ | $\mathcal{O}(1)$ | $\log_2 N$ |
| 11 | `CPPB-DAC-11` | **Tính Tổng Cấp Số Nhân D&C** | `P3` | **Core** | $\Theta(\log N)$ | $\Theta(\log N)$ | $\mathcal{O}(1)$ | $\log_2 N$ |
| 12 | `CPPB-DAC-12` | **Đếm Số Cặp $A_i > 2A_j$ (Significant Inversions)**| `P3` | **Core** | $\Theta(N \log N)$ | $\Theta(\log N)$ | $\Theta(N)$ | $\log_2 N$ |
| 13 | `CPPB-DAC-13` | **Thuật Toán QuickSelect Tìm K-th Element** | `P4` | *Advanced* | $\Theta(N) \text{ exp} / \Theta(N^2) \text{ worst}$ | $\Theta(\log N) \text{ exp} / \Theta(N) \text{ worst}$ | $\mathcal{O}(1)$ | $\log_2 N \text{ exp} / N \text{ worst}$ |
| 14 | `CPPB-DAC-14` | **Đếm Số Đoạn Con Tổng Trong Đoạn $[L, R]$**| `P4` | *Advanced* | $\Theta(N \log N)$ | $\Theta(\log N)$ | $\Theta(N)$ | $\log_2 N$ |
| 15 | `CPPB-DAC-15` | **Cặp Điểm Gần Nhất (Closest Pair of Points)**| `P4` | *Challenge* | $\Theta(N \log N)$ | $\Theta(\log N)$ | $\Theta(N)$ | $\log_2 N$ |
| 16 | `CPPB-DAC-16` | **Median Của Hai Mảng Đã Sắp Xếp** | `P5` | *Challenge* | $\Theta(\log(\min))$ | $\Theta(\log(\min))$ | $\mathcal{O}(1)$ | $\log_2(\min)$ |
