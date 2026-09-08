# Hướng Dẫn Giảng Dạy: Nối Dây Chi Phí Nhỏ Nhất (Huffman Greedy)

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách chiều dài $N$ đoạn cáp. Hãy lập trình tìm thứ tự nối cáp sao cho tổng chi phí hàn nối là nhỏ nhất có thể.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4 4 3 2 6` $\implies$ Đầu ra kỳ vọng: `29`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 4 3 2 6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với 4 đoạn dây có độ dài $[4, 3, 2, 6]$: 1. Nối hai dây ngắn nhất 2 và 3 thành dây độ dài 5, chi phí tốn $2 + 3 = 5$. Danh sách dây còn... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `29` |

*Giải thích chi tiết:* Với 4 đoạn dây có độ dài $[4, 3, 2, 6]$:

1. Nối hai dây ngắn nhất 2 và 3 thành dây độ dài 5, chi phí tốn $2 + 3 = 5$. Danh sách dây còn: [4, 5, 6].
2. Nối tiếp hai dây ngắn nhất 4 và 5 thành dây độ dài 9, chi phí tốn $4 + 5 = 9$. Danh sách dây còn: [6, 9].
3. Nối hai dây cuối 6 và 9 thành dây độ dài 15, chi phí tốn $6 + 9 = 15$.
Tổng chi phí nhỏ nhất là $5 + 9 + 15 = 29$.

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
    if (n <= 1) { cout << 0 << "\n"; return 0; }

    priority_queue<long long, vector<long long>, greater<long long>> min_heap;
    for (int i = 0; i < n; ++i) {
        long long x;
        cin >> x;
        min_heap.push(x);
    }

    long long total_cost = 0;
    while (min_heap.size() > 1) {
        long long a = min_heap.top(); min_heap.pop();
        long long b = min_heap.top(); min_heap.pop();
        long long sum = a + b;
        total_cost += sum;
        min_heap.push(sum);
    }

    cout << total_cost << "\n";
    return 0;
}
```
