# Hướng Dẫn Giảng Dạy: Hàng Đợi Ưu Tiên K Phần Tử Lớn Nhất

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách gồm $N$ số nguyên và số nguyên dương $K$. Hãy lập trình tìm và in ra $K$ phần tử lớn nhất trong dãy theo thứ tự giảm dần.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
* `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
* `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
* `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `6 3 10 50 30 20 60 40` $\implies$ Đầu ra kỳ vọng: `60 50 40`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `6 3 10 50 30 20 60 40` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng gồm 6 phần tử $[3, 2, 1, 5, 6, 4]$ và cần lấy $K = 2$ phần tử lớn nhất: Hai phần tử lớn nhất trong dãy là 6 và 5. In ra theo t... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `60 50 40` |

*Giải thích chi tiết:* Với mảng gồm 6 phần tử $[3, 2, 1, 5, 6, 4]$ và cần lấy $K = 2$ phần tử lớn nhất:
Hai phần tử lớn nhất trong dãy là 6 và 5. In ra theo thứ tự giảm dần: 6 5.

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

int n, k;
if (!(cin >> n >> k)) return 0;
if (n <= 0 || k <= 0 || k > n) return 0;

priority_queue<long long, vector<long long>, greater<long long>> min_heap;

for (int i = 0; i < n; ++i) {
long long x;
cin >> x;
min_heap.push(x);
if ((int)min_heap.size() > k) {
min_heap.pop();
}
}

vector<long long> result;
while (!min_heap.empty()) {
result.push_back(min_heap.top());
min_heap.pop();
}
sort(result.rbegin(), result.rend());

for (int i = 0; i < k; ++i) {
cout << result[i] << (i + 1 == k "" : " ");
}
cout << "\n";
return 0;
}
```
