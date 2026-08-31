# Chuyên đề 16: Cấu trúc dữ liệu STL: Set, map & heap

## 1. Bản chất các cấu trúc dữ liệu nâng cao trong thư viện chuẩn STL

Trong lập trình thi đấu hiện đại, việc tự cài đặt lại cây nhị phân cân bằng hay bảng băm từ đầu cho mọi bài toán là không khả thi. C++ Standard Template Library (STL) cung cấp các cấu trúc dữ liệu tối ưu hóa cực mạnh:
* **`std::set` / `std::map`:** Cây đỏ-đen (Red-Black Tree) tự cân bằng, luôn duy trì các phần tử theo thứ tự tăng dần. Các thao tác tìm kiếm, chèn, xóa đều có độ phức tạp đảm bảo $\mathcal{O}(\log N)$.
* **`std::unordered_map` / `std::unordered_set`:** Bảng băm trực tiếp (Hash Table), đạt thời gian trung bình $\mathcal{O}(1)$ cho các truy vấn.
* **`std::priority_queue`:** Cấu trúc Heap nhị phân hoàn chỉnh, cho phép truy xuất phần tử lớn nhất (hoặc nhỏ nhất) trong $\mathcal{O}(1)$ và thêm/bớt trong $\mathcal{O}(\log N)$.

![So sánh Set Map vs Unordered Map](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-16-cau-truc-du-lieu-stl-set-map/assets/stl_set_map_rb_tree_vi.svg)

## 2. Kỹ thuật nén tọa độ (Coordinate Compression)

### 2.1. Bản chất bài toán & khi nào cần nén tọa độ?
* **Vấn đề:** Các giá trị trong mảng $A$ có thể rất lớn ($A[i] \le 10^9$ hoặc $10^{18}$), ta không thể dùng giá trị này làm chỉ số mảng đếm tần suất hoặc dựng cây Segment Tree / Fenwick Tree. Tuy nhiên, số lượng phần tử $N$ lại rất nhỏ ($N \le 10^5$).
* **Nguyên lý Nén Tọa Độ:** Ánh xạ tập giá trị rời rạc ban đầu về tập số nguyên liên tiếp $\{0, 1, 2, \dots, K-1\}$ ($K \le N$) sao cho **giữ nguyên thứ tự tương quan lớn bé** giữa các phần tử:
$$A[i] < A[j] \iff \text{rank}(A[i]) < \text{rank}(A[j])$$

![Mô hình Nén Tọa Độ](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-16-cau-truc-du-lieu-stl-set-map/assets/coordinate_compression_model_vi.svg)

### 2.2. Quy trình 4 bước chuẩn mực trong C++
1. **Sao chép mảng:** `vector<long long> vals = a;`

2. **Sắp xếp tăng dần:** `sort(vals.begin(), vals.end());`
3. **Lọc bỏ trùng lặp:** `vals.erase(unique(vals.begin(), vals.end()), vals.end());`
4. **Ánh xạ bằng Tìm kiếm nhị phân:**
   ```cpp
   int compressed_val = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
   ```

## 3. Hàng đợi ưu tiên (Priority Queue / heap)

![Hàng đợi ưu tiên Max-Heap vs Min-Heap](/Users/vu/Developer/ikhEdu_lessons/courses/cpp-bang-b/lessons/lesson-16-cau-truc-du-lieu-stl-set-map/assets/priority_queue_heap_vi.svg)

* **Max-Heap (Mặc định):** `priority_queue<long long> max_pq;` $\implies$ `top()` trả về giá trị lớn nhất.

* **Min-Heap (Đảo thứ tự):** `priority_queue<long long, vector<long long>, greater<long long>> min_pq;` $\implies$ `top()` trả về giá trị nhỏ nhất.

* **Ứng dụng kinh điển:** Tìm $K$ phần tử lớn nhất/nhỏ nhất trong luồng dữ liệu online, thuật toán Dijkstra, thuật toán Prim, duy trì Trung vị động (Median) bằng 2 Heap.

## 4. Các bẫy lỗi lập trình kinh điển (bug traps)

1. **Bẫy Worst-case $\mathcal{O}(N)$ của `unordered_map` do Anti-Hash Test:**
* Trong các kỳ thi competitive, hàm băm mặc định `std::hash` của `unordered_map` rất dễ bị các test đối kháng (Anti-hash tests) làm tràn bucket $\implies$ Độ phức tạp tụt xuống $\mathcal{O}(N^2)$ và bị TLE.
* **Quy tắc an toàn:** Dùng `std::map` khi $N \le 2 \cdot 10^5$ (đảm bảo $\mathcal{O}(N \log N)$), hoặc dùng Custom Hash an toàn với hằng số thời gian ngẫu nhiên `chrono`.
2. **Bẫy xóa phần tử trong `std::multiset`:**
* Lệnh `ms.erase(x)` sẽ **xóa TOÀN BỘ** các phần tử có giá trị bằng $x$ trong multiset!
* **Cú pháp chuẩn khi chỉ muốn xóa 1 bản sao:** `ms.erase(ms.find(x));`.
3. **Bẫy truy cập `map[key]` tự động chèn phần tử mới:**
* Khi gọi `if (mp[x] > 0)`, nếu $x$ chưa tồn tại trong map, C++ sẽ tự động chèn cặp `(x, 0)` vào map làm tăng kích thước bộ nhớ.

* **Cú pháp an toàn:** Dùng `if (mp.count(x))` hoặc `if (mp.find(x) != mp.end())`.

## 5. Mẫu cài đặt chuẩn thi đấu (competitive templates)

### Mẫu 1: Kỹ thuật nén tọa độ chuẩn mực

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n <= 0) return 0;

    vector<long long> a(n);

    for (int i = 0; i < n; ++i) {
        cin >> a[i];

    }

    // 1. Tạo mảng nén
    vector<long long> vals = a;

    sort(vals.begin(), vals.end());
    vals.erase(unique(vals.begin(), vals.end()), vals.end());

    // 2. Ánh xạ từng phần tử
    vector<int> compressed(n);

    for (int i = 0; i < n; ++i) {
        compressed[i] = lower_bound(vals.begin(), vals.end(), a[i]) - vals.begin();
    }

    for (int i = 0; i < n; ++i) {
        cout << compressed[i] << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

### Mẫu 2: Duy trì trung vị động bằng 2 heap (median of stream)

```cpp
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    if (n <= 0) return 0;

    priority_queue<long long> left_max; // Nửa nhỏ hơn (Max-Heap)

    priority_queue<long long, vector<long long>, greater<long long>> right_min; // Nửa lớn hơn (Min-Heap)

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;

        if (left_max.empty() || x <= left_max.top()) {
            left_max.push(x);
        } else {
            right_min.push(x);
        }

        // Tự cân bằng kích thước: left_max luôn có size == right_min hoặc size == right_min + 1
        if (left_max.size() > right_min.size() + 1) {

            right_min.push(left_max.top());
            left_max.pop();
        } else if (right_min.size() > left_max.size()) {

            left_max.push(right_min.top());
            right_min.pop();
        }

        // In trung vị hiện tại
        cout << left_max.top() << (i + 1 == n ? "" : " ");
    }
    cout << "\n";

    return 0;
}
```

## Câu hỏi trắc nghiệm củng cố khái niệm

#### Câu 1 (Bản chất std::set):

Cấu trúc dữ liệu `std::set` trong C++ được cài đặt dựa trên cấu trúc cây nào?

- **A.** Cây nhị phân tìm kiếm thông thường (BST).

- **B.** **[Đáp án đúng]** Cây Đỏ-Đen (Red-Black Tree) tự cân bằng.

- **C.** Cây phân đoạn (Segment Tree).

- **D.** Bảng băm (Hash Table).

> *Giải thích:* Red-Black Tree đảm bảo độ cao của cây luôn là $\mathcal{O}(\log N)$, giữ cho mọi thao tác tìm kiếm, chèn, xóa đạt $\mathcal{O}(\log N)$ trong mọi trường hợp.

#### Câu 2 (Xóa 1 phần tử trong std::multiset):

Để xóa đúng một phần tử có giá trị $x$ trong `std::multiset<int> ms`, cú pháp nào sau đây là chính xác?

- **A.** `ms.erase(x);`

- **B.** **[Đáp án đúng]** `auto it = ms.find(x); if (it != ms.end()) ms.erase(it);`

- **C.** `ms.pop(x);`

- **D.** `ms.remove(x);`

> *Giải thích:* `ms.erase(x)` sẽ xóa sạch toàn bộ các phần tử có giá trị $x$. Để xóa 1 phần tử, phải truyền iterator thông qua `ms.find(x)`.

#### Câu 3 (Độ phức tạp nén tọa độ):

Cho mảng $N$ phần tử. Quy trình nén tọa độ gồm sao chép, sắp xếp `sort`, lọc $unique$ và ánh xạ `lower_bound` có tổng độ phức tạp thời gian là bao nhiêu?

- **A.** $\mathcal{O}(N^2)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(N \log N)$

- **C.** $\mathcal{O}(N)$

- **D.** $\mathcal{O}(\log N)$

> *Giải thích:* Bước `sort` tốn $\mathcal{O}(N \log N)$, bước $unique$ tốn $\mathcal{O}(N)$, $N$ lần gọi `lower_bound` tốn $N \log N \implies$ Tổng thời gian $\mathcal{O}(N \log N)$.

#### Câu 4 (Mục đích cốt lõi của nén tọa độ):

Tại sao ta cần nén tọa độ khi giá trị các phần tử lên tới $10^9$?

- **A.** Để mảng có thứ tự tăng dần.

- **B.** **[Đáp án đúng]** Để chuyển miền giá trị cực lớn về đoạn $[0, K-1]$ ($K \le N$) giúp sử dụng được mảng đếm tần suất hoặc cây Fenwick/Segment Tree.

- **C.** Để xóa các phần tử âm.

- **D.** Để giảm thời gian đọc dữ liệu.

> *Giải thích:* Thu nhỏ miền giá trị mà không làm thay đổi thứ tự quan hệ lớn bé giữa các phần tử.

#### Câu 5 (Cấu trúc Min-Heap trong C++):

Khai báo nào sau đây tạo ra một Hàng đợi ưu tiên Min-Heap trong C++?

- **A.** `priority_queue<int> pq;`

- **B.** **[Đáp án đúng]** `priority_queue<int, vector<int>, greater<int>> pq;`

- **C.** `priority_queue<int, less<int>> pq;`

- **D.** `min_heap<int> pq;`

> *Giải thích:* Mặc định `priority_queue` dùng functor `less<T>` tạo Max-Heap. Dùng `greater<T>` để đảo chiều so sánh thành Min-Heap.

#### Câu 6 (Độ phức tạp các thao tác priority_queue):

Trong `std::priority_queue`, độ phức tạp thời gian của các hàm `top()`, `push()`, `pop()` lần lượt là:

- **A.** $\mathcal{O}(1), \mathcal{O}(1), \mathcal{O}(1)$

- **B.** **[Đáp án đúng]** $\mathcal{O}(1), \mathcal{O}(\log N), \mathcal{O}(\log N)$

- **C.** $\mathcal{O}(\log N), \mathcal{O}(\log N), \mathcal{O}(\log N)$

- **D.** $\mathcal{O}(N), \mathcal{O}(\log N), \mathcal{O}(1)$

> *Giải thích:* `top()` chỉ đọc đỉnh heap trong $\mathcal{O}(1)$. `push()` và `pop()` thực hiện vun đống (heapify up/down) theo chiều cao cây $\mathcal{O}(\log N)$.

#### Câu 7 (Bẫy truy cập std::map):

Khi thực hiện kiểm tra $if (mp[key] = 5)$ mà $key$ chưa từng xuất hiện trong $map$, điều gì sẽ xảy ra?

- **A.** Chương trình báo lỗi biên dịch.

- **B.** **[Đáp án đúng]** C++ tự động chèn $key$ vào $map$ với giá trị mặc định là 0, làm tăng kích thước của map.

- **C.** Hàm trả về `false` và map không thay đổi.

- **D.** Chương trình bị Runtime Error.

> *Giải thích:* Toán tử `[]` của `std::map` có side-effect tự động khởi tạo phần tử mới nếu chưa tồn tại. Cần dùng `mp.find(key)` để kiểm tra an toàn.

#### Câu 8 (Khác biệt giữa set và unordered_set):

Ưu điểm lớn nhất của `std::set` so với `std::unordered_set` là gì?

- **A.** Chạy nhanh hơn trong mọi trường hợp.

- **B.** **[Đáp án đúng]** Luôn duy trì thứ tự tăng dần và hỗ trợ các hàm tìm kiếm cận `lower_bound`, `upper_bound` trong $\mathcal{O}(\log N)$.

- **C.** Chiếm ít bộ nhớ hơn.

- **D.** Cho phép chứa các phần tử trùng lặp.

> *Giải thích:* `std::unordered_set` không có thứ tự và không hỗ trợ tìm kiếm cận trên/dưới.

#### Câu 9 (Tìm kiếm lower_bound trên std::set):

Để tìm phần tử nhỏ nhất $\ge x$ trong `std::set<int> st`, cú pháp nào có hiệu năng tối ưu $\mathcal{O}(\log N)$?

- **A.** `lower_bound(st.begin(), st.end(), x);`

- **B.** **[Đáp án đúng]** `st.lower_bound(x);`

- **C.** `find(st.begin(), st.end(), x);`

- **D.** `binary_search(st.begin(), st.end(), x);`

> *Giải thích:* Phải dùng hàm thành viên `st.lower_bound(x)` chạy trên cây trong $\mathcal{O}(\log N)$. Hàm toàn cục `std::lower_bound` duyệt trên iterator của set sẽ mất $\mathcal{O}(N)$.

#### Câu 10 (Duy trì Trung vị động):

Trong bài toán tìm trung vị động của luồng dữ liệu, ta sử dụng cặp cấu trúc dữ liệu nào tối ưu nhất?

- **A.** Hai mảng `vector`.

- **B.** **[Đáp án đúng]** Một Max-Heap chứa nửa phần tử nhỏ và một Min-Heap chứa nửa phần tử lớn.

- **C.** Một `std::queue` và một `std::stack`.

- **D.** Hai cây phân đoạn.

> *Giải thích:* Hai Heap giữ cân bằng kích thước cho phép truy xuất phần tử trung vị ở đỉnh heap trong $\mathcal{O}(1)$ và thêm phần tử mới trong $\mathcal{O}(\log N)$.

#### Câu 11 (Cấu trúc std::map lồng nhau):

Muốn lưu tần suất xuất hiện của các cặp tọa độ $(x, y)$, kiểu dữ liệu nào sau đây là chuẩn mực?

- **A.** `vector<int> mp;`

- **B.** **[Đáp án đúng]** `map<vector<long long>, int> mp;` hoặc `map<pair<long long, long long>, int> mp;`

- **C.** `set<int> mp;`

- **D.** `unordered_map<pair<int, int>, int> mp;` (không có custom hash).

> *Giải thích:* `std::pair` hoặc `vector` có sẵn toán tử so sánh `<` nên dùng trực tiếp làm key trong `std::map` cực kỳ an toàn.

#### Câu 12 (Đếm số phần tử phân biệt trong cửa sổ):

Để đếm số phần tử phân biệt trong cửa sổ trượt độ dài $K$ một cách hiệu quả, cấu trúc nào sau đây là tối ưu nhất?

- **A.** Mỗi bước tạo một $set$ mới $\mathcal{O}(K \log K)$.

- **B.** **[Đáp án đúng]** Duy trì một mảng đếm tần suất hoặc $map$ kết hợp biến đếm `distinct_count` cập nhật trong $\mathcal{O}(1)$.

- **C.** Dùng `stack`.

- **D.** Sắp xếp lại cửa sổ mỗi bước.

> *Giải thích:* Khi cửa sổ trượt, chỉ có 1 phần tử thêm vào và 1 phần tử bị loại ra, cập nhật biến đếm trong $\mathcal{O}(1)$.

#### Câu 13 (Hàm std::unique trong C++):

Hàm `std::unique(v.begin(), v.end())` chỉ hoạt động chính xác khi nào?

- **A.** Khi vector có kích thước chẵn.

- **B.** **[Đáp án đúng]** Khi vector đã được sắp xếp trước đó.

- **C.** Khi vector chỉ chứa số dương.

- **D.** Luôn hoạt động chính xác với mọi mảng chưa sắp xếp.

> *Giải thích:* `std::unique` chỉ loại bỏ các phần tử trùng lặp đứng LIỀN KỀ nhau. Do đó mảng bắt buộc phải được `sort` trước.

#### Câu 14 (Hàng đợi ưu tiên lưu Struct / Comparator):

Muốn `priority_queue` ưu tiên phần tử có giá trị nhỏ nhất, nếu dùng Struct thì toán tử `operator<` phải định nghĩa như thế nào?

- **A.** `bool operator<(const Node& other) const { return val < other.val; }`

- **B.** **[Đáp án đúng]** `bool operator<(const Node& other) const { return val > other.val; }` (Đảo dấu so sánh).

- **C.** `bool operator<(const Node& other) const { return val == other.val; }`

- **D.** Không thể dùng struct trong priority_queue.

> *Giải thích:* `priority_queue` mặc định đưa phần tử lớn nhất theo quan hệ `<` lên đỉnh. Để phần tử nhỏ nhất lên đỉnh, ta đảo ngược định nghĩa thành `val > other.val`.

#### Câu 15 (Duyệt toàn bộ phần tử trong std::map):

Cách duyệt in toàn bộ các cặp `(key, value)` trong `std::map<string, int> mp` theo thứ tự từ điển chuẩn C++11 là:

- **A.** `for (int i = 0; i < mp.size(); ++i) cout << mp[i];`

- **B.** **[Đáp án đúng]** `for (const auto& p : mp) cout << p.first << " " << p.second << "\n";`

- **C.** `for (auto it = mp.end(); it != mp.begin(); ++it)`

- **D.** Dùng vòng lặp `while`.

> *Giải thích:* Dùng range-based for loop duyệt tuần tự các pair `(first, second)` theo đúng thứ tự sắp xếp của cây đỏ đen.

## Ma trận bài tập thực hành (P0 → P5)

| Mã Bài Tập | Tên Bài Toán | Mức Độ | Trọng Tâm Kiến Thức & Kỹ Năng STL |
|---|---|:---:|---|
| `CPPB-STL-01` | Đếm Số Phần Tử Phân Biệt | **P0** | Dùng `std::set` hoặc sort + unique cơ bản $\mathcal{O}(N \log N)$. |
| `CPPB-STL-02` | Bảng Tra Cứu Tần Suất Từ Khóa | **P1** | Sử dụng `std::map<string, int>` đếm số lần xuất hiện. |
| `CPPB-STL-03` | Nén Tọa Độ Mảng Số Lớn | **P1** | Áp dụng quy trình 4 bước nén giá trị về $[0, K-1]$. |
| `CPPB-STL-04` | Tìm Phần Tử Nhỏ Nhất Lớn Hơn X | **P2** | Sử dụng `st.lower_bound(x)` trên `std::set`. |
| `CPPB-STL-05` | Hàng đợi ưu tiên K Phần Tử Lớn Nhất | **P2** | Dùng Min-Heap kích thước $K$ duy trì top $K$ phần tử. |
| `CPPB-STL-06` | Quản Lý Tập Hợp Đa Trùng Lặp (Multiset) | **P2** | Thao tác chèn, tìm kiếm và xóa đúng 1 bản sao với `ms.find()`. |
| `CPPB-STL-07` | Hợp Nhất Các Đoạn Số (Merge Intervals) | **P2** | Sắp xếp các đoạn theo đầu mút kết hợp cấu trúc dữ liệu. |
| `CPPB-STL-08` | Tìm Trung Vị Động Trong Luồng Dữ Liệu | **P3** | Cặp Max-Heap / Min-Heap tự cân bằng $\mathcal{O}(\log N)$ mỗi truy vấn. |
| `CPPB-STL-09` | Đếm Số Phần Tử Phân Biệt Trong Cửa Sổ K | **P3** | Cửa sổ trượt kết hợp `map` tần suất duy trì `distinct_count`. |
| `CPPB-STL-10` | Nối Dây Chi Phí Nhỏ Nhất (Huffman Greedy) | **P3** | Min-Heap liên tục lấy 2 phần tử nhỏ nhất và đẩy tổng vào lại. |
| `CPPB-STL-11` | Lập Lịch Công Việc Tối Ưu Máy Chủ | **P3** | `priority_queue` quản lý thời điểm máy chủ rảnh rỗi. |
| `CPPB-STL-12` | Đếm Cặp Số Có Hiệu Bằng K Số Lớn | **P4** | Nén tọa độ kết hợp mảng đếm tần suất hoặc tìm kiếm nhị phân. |
| `CPPB-STL-13` | Truy Vấn Phần Tử Xuất Hiện Nhiều Nhất | **P4** | Cấu trúc dữ liệu kết hợp duy trì tần suất cực đại online. |
| `CPPB-STL-14` | Tìm Cặp Điểm Gần Nhất (Closest Pair) | **P4** | Đường quét (Sweep-line) kết hợp `std::set` $\mathcal{O}(N \log N)$. |
| `CPPB-STL-15` | Hệ Thống Xếp Hạng Thi Đấu Dynamic (Mastery) | **P5** | Cấu trúc dữ liệu STL đa tiêu chí hỗ trợ cập nhật điểm và xếp hạng. |
