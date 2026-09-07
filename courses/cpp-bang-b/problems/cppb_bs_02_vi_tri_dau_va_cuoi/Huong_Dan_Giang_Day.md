# Hướng Dẫn Giảng Dạy: Tìm Vị Trí Xuất Hiện Đầu Tiên & Cuối Cùng
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N phần tử đã sắp xếp tăng dần. Với mỗi giá trị X trong Q truy vấn, hãy tìm vị trí xuất hiện đầu tiên và cuối cùng của X. Nếu X không có trong mảng, in ra `-1 -1`.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 3 1 2 2 2 3 4 5 2 3 6)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `7 3 1 2 2 2 3 4 5 2 3 6` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | - Số 2 xuất hiện từ vị trí 2 đến vị trí 4 -> in `2 4`. - Số 3 chỉ xuất hiện tại vị trí 5 -> in `5 5`. - Số 6 không có tr... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `2 4 5 5 -1 -1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* - Số 2 xuất hiện từ vị trí 2 đến vị trí 4 -> in `2 4`.
- Số 3 chỉ xuất hiện tại vị trí 5 -> in `5 5`.
- Số 6 không có trong mảng -> in `-1 -1`.

---

## 3. Lưu ý & Bẫy lỗi thường gặp
- **Bẫy 1 — Tràn số nguyên:** Khi tính toán tổng, tích hoặc lũy thừa lớn hơn $2 \cdot 10^9$, bắt buộc phải sử dụng kiểu dữ liệu `long long` (64-bit) để tránh tràn số âm.
- **Bẫy 2 — Chỉ số mảng & Giới hạn biên:** Chú ý giữa đánh chỉ số 0-based (`0 .. N-1`) và 1-based (`1 .. N`). Kiểm tra kỹ trường hợp $N = 1$ hoặc giá trị biên tối đa của đề bài.
- **Bẫy 3 — Tối ưu thời gian I/O:** Luôn sử dụng `ios::sync_with_stdio(false); cin.tie(nullptr);` ở đầu hàm `main()` để đọc ghi nhanh, tránh bị TLE khi số lượng testcase lớn.

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

    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        cin >> a[i];
    }

    while (q--) {
        long long x;
        cin >> x;
        auto it1 = lower_bound(a.begin(), a.end(), x);
        if (it1 == a.end() || *it1 != x) {
            cout << "-1 -1\n";
        } else {
            auto it2 = upper_bound(a.begin(), a.end(), x);
            int first_idx = it1 - a.begin() + 1;
            int last_idx = it2 - a.begin();
            cout << first_idx << " " << last_idx << "\n";
        }
    }

    return 0;
}
```
