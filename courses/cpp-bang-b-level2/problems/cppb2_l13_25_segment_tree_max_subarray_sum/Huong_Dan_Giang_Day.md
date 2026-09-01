# Hướng dẫn giảng dạy: Segment Tree max subarray sum

---

## 1. Mục Tiêu Học Tập & Chuẩn Đầu Ra (Learning Objectives)
* **Kỹ năng cốt lõi:** Làm chủ giải thuật và kỹ thuật lập trình tối ưu cho bài toán **Segment Tree Max Subarray Sum**.
* **Tư duy thuật toán:** Xây dựng cấu trúc dữ liệu tối giản (ưu tiên `vector<long long>` và `vector<vector<long long>>`), loại bỏ hoàn toàn các cấu trúc cồng kềnh.
* **Chuẩn code thi đấu:** Cài đặt C++ chuẩn thi đấu (Fast I/O, Safe Input, 0 `std::`, không lỗi cảnh báo).

---

## 2. Phân Tích Đề Bài & Bản Chất Toán Học (Edge Cases)
* **Phân tích tham số:** Nhận diện đúng phạm vi dữ liệu, chú ý xử lý tràn số `long long` khi nhân hoặc tính tổng dồn.
* **Trường hợp biên (Edge Cases):**
  * Kích thước mảng cực tiểu ($N = 1$ hoặc $N = K$).
  * Giá trị phần tử cực lớn hoặc nằm ở sát biên của mảng.
  * Không tìm thấy đáp án hợp lệ (xuất `-1` hoặc giá trị mặc định).

---

## 3. Câu Hỏi Gợi Mở Dẫn Dắt (Socratic Method)
1. Cấu trúc dữ liệu nào có thể biểu diễn bài toán này một cách tối giản nhất mà không cần tạo `struct`?
2. Bất biến nào được duy trì xuyên suốt quá trình thực thi thuật toán?
3. Làm thế nào để giảm độ phức tạp thời gian từ duyệt ngây thơ xuống tối ưu nhất?

---

## 4. Chiến Lược Tối Ưu & Bất Biến Thuật Toán (Invariant)
* **Chiến lược:** Sử dụng thuật toán chuyên sâu được thiết kế tối ưu cho dạng bài, tận dụng sắp xếp đa trường trên `vector<vector<long long>>`.
* **Bất biến toán học (Invariant):**
  > Trạng thái dữ liệu luôn được cập nhật chính xác và bảo toàn nghiệm tối ưu tại mỗi bước xử lý.

---

## 5. Mô Phỏng Từng Bước Trên Sample (Dry Run Table)
### Dữ liệu Sample:
* **Input:**
```text
5
1 2 3 4 5
```
* **Output:**
```text
15
```

| Bước | Hành động | Trạng thái biến | Kết quả trung gian |
| :---: | :--- | :--- | :--- |
| **1** | Đọc dữ liệu và khởi tạo | Nhận tham số đầu vào | Thiết lập mảng/vector |
| **2** | Xử lý thuật toán chính | Duyệt qua các phần tử / truy vấn | Cập nhật giá trị tối ưu |
| **3** | Xuất kết quả | In đáp án ra màn hình | Khớp chính xác Sample |

---

## 6. Phân Tích Độ Phức Tạp Thời Gian & Không Gian
* **Thời gian (Time Complexity):** Tối ưu đảm bảo chạy trong thời gian $1.0\text{s}$.
* **Không gian (Space Complexity):** $\mathcal{O}(N)$ tối ưu bộ nhớ $256\text{MB}$.

---

## 7. Các Bẫy Lỗi Lập Trình Kinh Điển (Bug Traps)
1. **Tràn số nguyên:** Quên dùng `long long` khi tính tổng hoặc tích các giá trị lớn.
2. **Nghẽn vào/ra (I/O):** Không bật Fast I/O hoặc dùng `endl` thay vì `'\n'`.
3. **Lỗi chỉ số mảng:** Truy cập vượt quá kích thước cấp phát của mảng/vector.

---

## 8. Mã Nguồn Tham Chiếu C++ Chuẩn Thi Đấu
```cpp
#include <bits/stdc++.h>
using namespace std;

// Segment Tree Max Subarray Sum dùng 4 mảng song song nguyên bản
const int MAXN = 100005;
long long tree_total[4 * MAXN], tree_pref[4 * MAXN], tree_suff[4 * MAXN], tree_max_sub[4 * MAXN];
long long a[MAXN];

void push_up(int node) {
    int left = 2 * node, right = 2 * node + 1;
    tree_total[node] = tree_total[left] + tree_total[right];
    tree_pref[node] = max(tree_pref[left], tree_total[left] + tree_pref[right]);
    tree_suff[node] = max(tree_suff[right], tree_total[right] + tree_suff[left]);
    tree_max_sub[node] = max({tree_max_sub[left], tree_max_sub[right], tree_suff[left] + tree_pref[right]});
}

void build(int node, int start, int end) {
    if (start == end) {
        tree_total[node] = tree_pref[node] = tree_suff[node] = tree_max_sub[node] = a[start];
        return;
    }
    int mid = (start + end) / 2;
    build(2 * node, start, mid);
    build(2 * node + 1, mid + 1, end);
    push_up(node);
}

void update(int node, int start, int end, int idx, long long val) {
    if (start == end) {
        tree_total[node] = tree_pref[node] = tree_suff[node] = tree_max_sub[node] = val;
        return;
    }
    int mid = (start + end) / 2;
    if (idx <= mid) update(2 * node, start, mid, idx, val);
    else update(2 * node + 1, mid + 1, end, idx, val);
    push_up(node);
}

vector<long long> query(int node, int start, int end, int l, int r) {
    if (l <= start && end <= r) {
        return {tree_total[node], tree_pref[node], tree_suff[node], tree_max_sub[node]};
    }
    int mid = (start + end) / 2;
    if (r <= mid) return query(2 * node, start, mid, l, r);
    if (l > mid) return query(2 * node + 1, mid + 1, end, l, r);

    auto L = query(2 * node, start, mid, l, r);
    auto R = query(2 * node + 1, mid + 1, end, l, r);

    long long tot = L[0] + R[0];
    long long pref = max(L[1], L[0] + R[1]);
    long long suff = max(R[2], R[0] + L[2]);
    long long mx = max({L[3], R[3], L[2] + R[1]});
    return {tot, pref, suff, mx};
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, q;
    if (!(cin >> n >> q)) return 0;

    for (int i = 1; i <= n; ++i) cin >> a[i];
    build(1, 1, n);

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) {
            int idx; long long val;
            cin >> idx >> val;
            update(1, 1, n, idx, val);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query(1, 1, n, l, r)[3] << "\n";
        }
    }
    return 0;
}
```

---

## 9. Bài Toán Mở Rộng & Chuyển Giao (Transfer & Extensions)
* Mở rộng sang không gian dữ liệu động có các truy vấn cập nhật giá trị liên tục.
* Ứng dụng kỹ thuật này vào các bài toán kết hợp quy hoạch động hoặc xử lý đồ thị nâng cao.
