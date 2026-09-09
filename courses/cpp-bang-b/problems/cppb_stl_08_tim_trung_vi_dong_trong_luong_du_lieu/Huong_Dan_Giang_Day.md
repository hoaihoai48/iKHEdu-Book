# Hướng Dẫn Giảng Dạy: Tìm Trung Vị Động Trong Luồng Dữ Liệu

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho một luồng dữ liệu gồm $N$ số nguyên đến lần lượt từng số một. Với mỗi số được thêm vào, hãy in ra giá trị trung vị của toàn bộ dãy số đã nhận được từ đầu đến thời điểm đó (lấy phần nguyên dưới nếu số lượng phần tử chẵn).

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
* `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
* `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
* `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫuMẫu thử (Sample 1): Đầu vào: `4 5 15 1 3` $\implies$ Đầu ra kỳ vọng: `5 5 5 3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 5 15 1 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với luồng dữ liệu đến lần lượt: 5, 15, 1, 3: - Nhận 5: dãy [5] $\to$ trung vị là 5. - Nhận 15: dãy [5, 15] $\to$ trung vị là 5 (hoặc tr... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `5 5 5 3` |

*Giải thích chi tiết:* Với luồng dữ liệu đến lần lượt: 5, 15, 1, 3:

- Nhận 5: dãy [5] $\to$ trung vị là 5.
- Nhận 15: dãy [5, 15] $\to$ trung vị là 5 (hoặc trung bình lấy nguyên).
- Nhận 1: dãy [1, 5, 15] $\to$ trung vị là 5.
- Nhận 3: dãy [1, 3, 5, 15] $\to$ trung vị là 3 (hoặc phần nguyên).
Kết quả in ra dãy trung vị động tương ứng.

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

int n;
if (!(cin >> n)) return 0;
if (n <= 0) return 0;

priority_queue<long long> left_max;
priority_queue<long long, vector<long long>, greater<long long>> right_min;

for (int i = 0; i < n; ++i) {
long long x;
cin >> x;

if (left_max.empty() || x <= left_max.top()) {
left_max.push(x);
} else {
right_min.push(x);
}

if (left_max.size() > right_min.size() + 1) {
right_min.push(left_max.top());
left_max.pop();
} else if (right_min.size() > left_max.size()) {
left_max.push(right_min.top());
right_min.pop();
}

cout << left_max.top() << (i + 1 == n "" : " ");
}
cout << "\n";
return 0;
}
```
