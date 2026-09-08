# Hướng Dẫn Giảng Dạy: Hợp Nhất Các Đoạn Số (Merge Intervals)

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách $N$ khoảng thời gian $[L_i, R_i]$. Hãy lập trình hợp nhất các khoảng giao nhau và in ra danh sách các khoảng thời gian sau khi đã hợp nhất theo thứ tự thời điểm bắt đầu tăng dần.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4 1 3 2 6 8 10 15 18` $\implies$ Đầu ra kỳ vọng: `3 1 6 8 10 15 18`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 1 3 2 6 8 10 15 18` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với các khoảng thời gian $[1, 3], [2, 6], [8, 10], [15, 18]$: - Khoảng $[1, 3]$ và $[2, 6]$ giao nhau vì $2 \le 3$, hợp nhất thành khoả... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3 1 6 8 10 15 18` |

*Giải thích chi tiết:* Với các khoảng thời gian $[1, 3], [2, 6], [8, 10], [15, 18]$:

- Khoảng $[1, 3]$ và $[2, 6]$ giao nhau vì $2 \le 3$, hợp nhất thành khoảng $[1, 6]$.
- Các khoảng $[8, 10]$ và $[15, 18]$ độc lập không giao nhau.
Kết quả thu được 3 khoảng: $[1, 6], [8, 10], [15, 18]$.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
* Sử dụng toán tử `st.erase(val)` trên `multiset` sẽ xoá TẤT CẢ các phần tử có giá trị bằng `val`. Để chỉ xoá đúng một phần tử, bắt buộc dùng con trỏ `st.erase(st.find(val))`.
* Truy cập vào khoá chưa tồn tại trong `map` qua cú pháp `mp[key]` sẽ tự động chèn một cặp mới với giá trị mặc định là 0, làm tăng kích thước bộ nhớ ngoài ý muốn. Khi kiểm tra tồn tại, nên dùng `mp.count(key)` hoặc `mp.find(key) != mp.end()`.
* Hàng đợi ưu tiên `priority_queue` mặc định là Max-Heap. Muốn biến thành Min-Heap cần khai báo đầy đủ: `priority_queue<long long, vector<long long>, greater<long long>> pq;`.

---

## 4. Lời giải tham khảo
```cpp
#include <bits/stdc++.h>
using namespace std;

struct Interval {
    long long l, r;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Interval> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].l >> a[i].r;

    sort(a.begin(), a.end(), [](const Interval& x, const Interval& y) {
        if (x.l != y.l) return x.l < y.l;
        return x.r < y.r;
    });

    vector<Interval> merged;
    merged.push_back(a[0]);

    for (int i = 1; i < n; ++i) {
        if (a[i].l <= merged.back().r) {
            merged.back().r = max(merged.back().r, a[i].r);
        } else {
            merged.push_back(a[i]);
        }
    }

    cout << merged.size() << "\n";
    for (const auto& iv : merged) {
        cout << iv.l << " " << iv.r << "\n";
    }
    return 0;
}
```
