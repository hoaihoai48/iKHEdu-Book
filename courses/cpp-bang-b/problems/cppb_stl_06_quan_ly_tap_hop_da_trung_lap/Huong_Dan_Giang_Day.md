# Hướng Dẫn Giảng Dạy: Quản Lý Tập Hợp Đa Trùng Lặp (Multiset)

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho $Q$ thao tác thuộc một trong 3 loại: `1 x` (thêm $x$), `2 x` (xóa một phần tử $x$), `3` (in ra giá trị nhỏ nhất hiện tại). Hãy lập trình mô phỏng lại hệ thống và in ra kết quả cho các thao tác loại 3.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `5 1 5 1 5 3 5 2 5 3 5` $\implies$ Đầu ra kỳ vọng: `2 1`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `5 1 5 1 5 3 5 2 5 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Với chuỗi thao tác: thêm 5, thêm 2, thêm 5, truy vấn min -> in ra 2; xóa 2, truy vấn min -> in ra 5. | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `2 1` |

*Giải thích chi tiết:* Với chuỗi thao tác: thêm 5, thêm 2, thêm 5, truy vấn min -> in ra 2; xóa 2, truy vấn min -> in ra 5.

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

    int q;
    if (!(cin >> q)) return 0;

    multiset<long long> ms;

    while (q--) {
        int type;
        long long x;
        cin >> type >> x;

        if (type == 1) { // Thêm x
            ms.insert(x);
        } else if (type == 2) { // Xóa đúng 1 bản sao của x nếu có
            auto it = ms.find(x);
            if (it != ms.end()) ms.erase(it);
        } else { // Đếm số lượng x
            cout << ms.count(x) << "\n";
        }
    }
    return 0;
}
```
