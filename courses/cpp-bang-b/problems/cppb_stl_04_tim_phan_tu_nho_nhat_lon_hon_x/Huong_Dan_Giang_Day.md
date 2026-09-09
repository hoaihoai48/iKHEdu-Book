# Hướng Dẫn Giảng Dạy: Tìm Phần Tử Nhỏ Nhất Lớn Hơn Hoặc Bằng X

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên và $Q$ truy vấn, mỗi truy vấn gồm một số nguyên $X$. Hãy lập trình tìm phần tử nhỏ nhất trong mảng lớn hơn hoặc bằng $X$. Nếu không có phần tử nào thỏa mãn, in ra `-1`.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
* `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
* `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
* `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `5 3 10 20 30 40 50 25 50 60` $\implies$ Đầu ra kỳ vọng: `30 50 -1`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 3 10 20 30 40 50 25 50 60` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng $[1, 4, 6, 8, 10]$ và các truy vấn $X$: - Truy vấn $X = 5$: Phần tử nhỏ nhất trong mảng $\ge 5$ là 6. - Truy vấn $X = 11$: Khô... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `30 50 -1` |

*Giải thích chi tiết:* Với mảng $[1, 4, 6, 8, 10]$ và các truy vấn $X$:

- Truy vấn $X = 5$: Phần tử nhỏ nhất trong mảng $\ge 5$ là 6.
- Truy vấn $X = 11$: Không có phần tử nào trong mảng $\ge 11$, in ra -1.

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

int main() {
ios::sync_with_stdio(false);
cin.tie(nullptr);

int n, q;
if (!(cin >> n >> q)) return 0;
if (n <= 0) return 0;

set<long long> st;
for (int i = 0; i < n; ++i) {
long long x;
cin >> x;
st.insert(x);
}

while (q--) {
long long x;
cin >> x;
auto it = st.lower_bound(x);
if (it == st.end()) {
cout << -1 << "\n";
} else {
cout << *it << "\n";
}
}
return 0;
}
```
