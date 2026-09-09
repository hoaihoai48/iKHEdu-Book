# Hướng Dẫn Giảng Dạy: Cặp Điểm Gần Nhất (Closest Pair Of Points)

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho tọa độ của $N$ điểm trên mặt phẳng. Hãy lập trình tìm bình phương khoảng cách Euclid nhỏ nhất giữa hai điểm bất kỳ.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
* `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
* `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
* `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `4 0 0 1 2 3 1 4 0` $\implies$ Đầu ra kỳ vọng: `5`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 0 0 1 2 3 1 4 0` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 4 điểm tọa độ: $(0, 0), (1, 1), (2, 2), (2, 0)$: Khoảng cách giữa điểm $(1, 1)$ và $(2, 2)$ có bình phương là $(2-1)^2 + (2-1)^2 = ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `5` |

*Giải thích chi tiết:* Với 4 điểm tọa độ: $(0, 0), (1, 1), (2, 2), (2, 0)$:
Khoảng cách giữa điểm $(1, 1)$ và $(2, 2)$ có bình phương là $(2-1)^2 + (2-1)^2 = 1 + 1 = 2$.
Khoảng cách giữa điểm $(1, 1)$ và $(2, 0)$ có bình phương là $(2-1)^2 + (0-1)^2 = 1 + 1 = 2$.
Bình phương khoảng cách nhỏ nhất giữa hai điểm bất kỳ là 2.

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

struct Point {
long long x, y;
};

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n;
if (!(cin >> n)) return 0;
if (n <= 1) { cout << 0 << "\n"; return 0; }

vector<Point> pts(n);
for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;

sort(pts.begin(), pts.end(), [](const Point& a, const Point& b) {
if (a.x != b.x) return a.x < b.x;
return a.y < b.y;
});

long long min_dist_sq = LLONG_MAX;
set<pair<long long, long long>> active_set; // Lưu (y, x)

int left = 0;
for (int i = 0; i < n; ++i) {
long long d = ceil(sqrt(min_dist_sq));
while (left < i && pts[i].x - pts[left].x >= d) {
active_set.erase({pts[left].y, pts[left].x});
left++;
}

auto it_low = active_set.lower_bound({pts[i].y - d, LLONG_MIN});
auto it_high = active_set.upper_bound({pts[i].y + d, LLONG_MAX});

for (auto it = it_low; it != it_high; ++it) {
long long dy = pts[i].y - it->first;
long long dx = pts[i].x - it->second;
min_dist_sq = min(min_dist_sq, dx * dx + dy * dy);
}

active_set.insert({pts[i].y, pts[i].x});
}

cout << min_dist_sq << "\n";
return 0;
}
```
