# Hướng Dẫn Giảng Dạy: Đếm Số Phần Tử Phân Biệt Trong Cửa Sổ K

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho mảng $A$ gồm $N$ số nguyên và kích thước cửa sổ $K$. Hãy lập trình in ra số lượng phần tử phân biệt trong mỗi cửa sổ kích thước $K$ khi trượt từ trái sang phải.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `7 4 1 2 1 3 4 2 3` $\implies$ Đầu ra kỳ vọng: `3 4 4 3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `7 4 1 2 1 3 4 2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với mảng gồm 7 phần tử $[1, 2, 1, 3, 4, 2, 3]$ và kích thước cửa sổ $K = 4$: - Cửa sổ 1 [1, 2, 1, 3]: gồm các giá trị phân biệt {1, 2, ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `3 4 4 3` |

*Giải thích chi tiết:* Với mảng gồm 7 phần tử $[1, 2, 1, 3, 4, 2, 3]$ và kích thước cửa sổ $K = 4$:
- Cửa sổ 1 [1, 2, 1, 3]: gồm các giá trị phân biệt {1, 2, 3} $\to$ 3 phần tử.
- Cửa sổ 2 [2, 1, 3, 4]: gồm {1, 2, 3, 4} $\to$ 4 phần tử.
- Cửa sổ 3 [1, 3, 4, 2]: gồm {1, 2, 3, 4} $\to$ 4 phần tử.
- Cửa sổ 4 [3, 4, 2, 3]: gồm {2, 3, 4} $\to$ 3 phần tử.
Kết quả in ra: 3 4 4 3.

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

    vector<int> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];

    map<int, int> freq;
    for (int i = 0; i < k; ++i) freq[a[i]]++;

    cout << freq.size();

    for (int i = k; i < n; ++i) {
        // Xóa phần tử cũ
        freq[a[i - k]]--;
        if (freq[a[i - k]] == 0) freq.erase(a[i - k]);

        // Thêm phần tử mới
        freq[a[i]]++;

        cout << " " << freq.size();
    }
    cout << "\n";
    return 0;
}
```
