# Hướng Dẫn Giảng Dạy: Tìm Kiếm Trên Mảng Sắp Xếp Bị Xoay Vòng (Rotated Array)
Chuyên đề: **Bài 05: Thuật toán tìm kiếm nhị phân**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên phân biệt bị xoay vòng tại một trục không xác định. Có Q truy vấn tìm vị trí xuất hiện (0-indexed) của số nguyên X. Nếu không tìm thấy, in ra -1.

- **Phương pháp tiếp cận — Tìm kiếm nhị phân (Binary Search):**
  - Nhận diện tính đơn điệu của hàm mục tiêu hoặc không gian tìm kiếm.
  - Thu hẹp không gian nghiệm $[L, R]$ qua điểm giữa $mid = L + (R - L) / 2$. Độ phức tạp thời gian đạt $\mathcal{O}(\log N)$ hoặc $\mathcal{O}(N \log(\text{range}))$.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 7 3 4 5 6 7 0 1 2 0 3 5)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `7 3 4 5 6 7 0 1 2 0 3 5` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng bị xoay vòng [4, 5, 6, 7, 0, 1, 2]: - Số 0 ở vị trí chỉ số 4. - Số 3 không tồn tại -> -1. - Số 5 ở vị trí chỉ số 1.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `4 -1 1` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng bị xoay vòng [4, 5, 6, 7, 0, 1, 2]:
- Số 0 ở vị trí chỉ số 4.
- Số 3 không tồn tại -> -1.
- Số 5 ở vị trí chỉ số 1.

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

int search_rotated(const vector<long long>& a, long long target) {
    int low = 0, high = (int)a.size() - 1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (a[mid] == target) return mid + 1; // 1-based

        if (a[low] <= a[mid]) {
            // Nửa trái được sắp xếp
            if (a[low] <= target && target < a[mid]) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        } else {
            // Nửa phải được sắp xếp
            if (a[mid] < target && target <= a[high]) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }
    }
    return -1;
}

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
        cout << search_rotated(a, x) << "\n";
    }

    return 0;
}
```
