# Hướng Dẫn Giảng Dạy: Hệ Thống Xếp Hạng Thi Đấu Dynamic

Chuyên đề: **Cấu Trúc Dữ Liệu STL Nâng Cao (Set, Map, Priority Queue)**

---

## 1. Ý tưởng & Phân tích thuật toán

- **Bản chất bài toán:** Cho danh sách $Q$ thao tác của hệ thống. Bạn hãy lập trình mô phỏng lại hệ thống và in ra kết quả cho mỗi thao tác tra cứu điểm.

- **Phương pháp tiếp cận & Chiến lược tối ưu:**
- **Lựa chọn cấu trúc dữ liệu tối ưu:**
  * `set` / `multiset`: Quản lý tập hợp tự động sắp xếp theo cây đỏ đen, hỗ trợ chèn, xoá, tìm kiếm trong $\mathcal{O}(\log N)$.
  * `map`: Ánh xạ khoá - giá trị với các truy vấn đếm tần suất, nén toạ độ trong $\mathcal{O}(\log N)$.
  * `priority_queue`: Hàng đợi ưu tiên (Binary Heap) cho phép lấy phần tử cực đại/cực tiểu trong $\mathcal{O}(1)$ và cập nhật trong $\mathcal{O}(\log N)$.
- **Kỹ thuật nén toạ độ:** Sao chép mảng, sắp xếp tăng dần, loại bỏ phần tử trùng bằng `unique()` và tìm thứ hạng nén qua `lower_bound()` trong $\mathcal{O}(N \log N)$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table)
Mẫu thử (Sample 1): Đầu vào: `4 1 Alice 100 1 Bob 150 2 Alice 1 Alice 60` $\implies$ Đầu ra kỳ vọng: `100`.

| Bước | Thao tác thực hiện | Dữ liệu biến đổi & Trạng thái | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Khởi tạo & Đọc dữ liệu | Nạp Input: `4 1 Alice 100 1 Bob 150 2 Alice 1 Alice 60` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Chạy thuật toán từng bước | Phân tích mẫu: Diễn biến 4 thao tác của hệ thống thi đấu: 1. Thao tác 1 (`1 Alice 100`): Alice được cộng 100 điểm. Điểm hiện tại của Alice là 100. 2. ... | Cập nhật các biến / mảng trạng thái |
| 3 | Xuất kết quả chuẩn | Đối chiếu trạng thái cuối cùng | Output chuẩn: `100` |

*Giải thích chi tiết:* Diễn biến 4 thao tác của hệ thống thi đấu:

1. Thao tác 1 (`1 Alice 100`): Alice được cộng 100 điểm. Điểm hiện tại của Alice là 100.
2. Thao tác 2 (`1 Bob 150`): Bob được cộng 150 điểm. Điểm hiện tại của Bob là 150.
3. Thao tác 3 (`2 Alice`): Truy vấn điểm của Alice. Hệ thống in ra điểm hiện tại là 100.
4. Thao tác 4 (`1 Alice 60`): Alice được cộng thêm 60 điểm nữa. Điểm tích lũy mới của Alice trở thành $100 + 60 = 160$.

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

    map<string, long long> scores;
    multiset<long long> all_scores;

    while (q--) {
        int type;
        cin >> type;
        if (type == 1) { // Cộng điểm cho thí sinh
            string name;
            long long delta;
            cin >> name >> delta;

            if (scores.count(name)) {
                auto it = all_scores.find(scores[name]);
                if (it != all_scores.end()) all_scores.erase(it);
            }

            scores[name] += delta;
            all_scores.insert(scores[name]);
        } else { // Truy vấn điểm của thí sinh
            string name;
            cin >> name;
            cout << (scores.count(name) ? scores[name] : 0) << "\n";
        }
    }
    return 0;
}
```
