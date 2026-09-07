# Hướng Dẫn Giảng Dạy: Lập Lịch Công Việc Số Máy Chủ Ít Nhất

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách thời gian bắt đầu và kết thúc của $N$ tác vụ. Hãy lập trình xác định số lượng máy chủ vật lý tối thiểu cần chuẩn bị để phục vụ toàn bộ các tác vụ.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `3 0 30 5 10 15 20` $\implies$ Đầu ra kỳ vọng: `2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `3 0 30 5 10 15 20` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 3 tác vụ: [0, 30], [5, 10], [15, 20]: Tại thời điểm $t = 5$, tác vụ 1 [0, 30] đang chạy trên máy 1, nên tác vụ 2 [5, 10] bắt buộc p... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2` |

*Giải thích chi tiết:* Với 3 tác vụ: [0, 30], [5, 10], [15, 20]:
Tại thời điểm $t = 5$, tác vụ 1 [0, 30] đang chạy trên máy 1, nên tác vụ 2 [5, 10] bắt buộc phải mở thêm máy 2.
Tại thời điểm $t = 15$, tác vụ 2 đã xong nhưng tác vụ 1 vẫn đang chạy, nên tác vụ 3 có thể tái sử dụng máy 2.
Số máy chủ tối thiểu cần dùng là 2.

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

struct Job {
    long long s, e;
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;
    if (n <= 0) return 0;

    vector<Job> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i].s >> a[i].e;

    sort(a.begin(), a.end(), [](const Job& x, const Job& y) {
        if (x.s != y.s) return x.s < y.s;
        return x.e < y.e;
    });

    priority_queue<long long, vector<long long>, greater<long long>> servers;

    for (int i = 0; i < n; ++i) {
        if (!servers.empty() && servers.top() <= a[i].s) {
            servers.pop();
        }
        servers.push(a[i].e);
    }

    cout << servers.size() << "\n";
    return 0;
}
```
