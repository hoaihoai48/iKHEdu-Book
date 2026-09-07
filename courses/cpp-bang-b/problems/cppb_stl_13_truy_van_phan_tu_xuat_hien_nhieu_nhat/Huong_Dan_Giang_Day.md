# Hướng Dẫn Giảng Dạy: Phần Tử Xuất Hiện Nhiều Nhất (Mode)

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách $N$ lá phiếu nguyên. Hãy lập trình tìm mã số xuất hiện nhiều lần nhất. Nếu có nhiều mã số cùng xuất hiện nhiều nhất, in ra mã số có giá trị nhỏ nhất trong số đó.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `6 1 3 2 1 4 1` $\implies$ Đầu ra kỳ vọng: `1 3`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `6 1 3 2 1 4 1` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với dãy số $[1, 2, 2, 3, 1]$: Cả hai số 1 và 2 đều xuất hiện đúng 2 lần (nhiều nhất). Theo quy định ưu tiên giá trị số học nhỏ hơn, ta ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `1 3` |

*Giải thích chi tiết:* Với dãy số $[1, 2, 2, 3, 1]$:
Cả hai số 1 và 2 đều xuất hiện đúng 2 lần (nhiều nhất). Theo quy định ưu tiên giá trị số học nhỏ hơn, ta chọn số 1. Kết quả in ra là 1.

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

    map<long long, int> freq;
    long long best_val = -1;
    int max_freq = 0;

    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        freq[x]++;
        if (freq[x] > max_freq || (freq[x] == max_freq && x < best_val)) {
            max_freq = freq[x];
            best_val = x;
        }
    }

    cout << best_val << " " << max_freq << "\n";
    return 0;
}
```
