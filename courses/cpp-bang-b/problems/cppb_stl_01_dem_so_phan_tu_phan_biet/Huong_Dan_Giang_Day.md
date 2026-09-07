# Hướng Dẫn Giảng Dạy: Đếm Số Phần Tử Phân Biệt

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách gồm $N$ số nguyên đại diện cho mã định danh. Hãy lập trình đếm và in ra số lượng giá trị phân biệt xuất hiện trong dãy số.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 2 3 2 2 3` $\implies$ Đầu ra kỳ vọng: `2`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 2 3 2 2 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với dãy gồm 5 số nguyên $[2, 3, 2, 1, 3]$: Các giá trị phân biệt xuất hiện trong dãy là $\{1, 2, 3\}$. Có tất cả 3 giá trị phân biệt, k... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2` |

*Giải thích chi tiết:* Với dãy gồm 5 số nguyên $[2, 3, 2, 1, 3]$:
Các giá trị phân biệt xuất hiện trong dãy là $\{1, 2, 3\}$. Có tất cả 3 giá trị phân biệt, kết quả in ra là 3.

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

    set<long long> st;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        st.insert(x);
    }

    cout << st.size() << "\n";
    return 0;
}
```
