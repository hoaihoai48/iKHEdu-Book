# Hướng Dẫn Giảng Dạy: So Sánh Đệ Quy Tuyến Tính & Chia Đôi Khi Tìm Min/Max
Chuyên đề: **Bài 10: Thuật toán đệ quy & cây gọi hàm**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng số nguyên A gồm N phần tử. Hãy cài đặt hàm đệ quy chia đôi để tìm giá trị nhỏ nhất (min) và lớn nhất (max) trong mảng.

- **Phương pháp tiếp cận — Thuật toán đệ quy & Cây gọi hàm:**
  - Xác định trường hợp cơ sở (Base Case) để chặn đệ quy vô hạn.
  - Thiết lập công thức truy hồi và theo dõi luồng thực thi trên cây gọi hàm.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 3 1 9 4 2)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 3 1 9 4 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Giá trị nhỏ nhất trong mảng là 1, giá trị lớn nhất là 9. Kết quả in ra: 1 9.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 9` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Giá trị nhỏ nhất trong mảng là 1, giá trị lớn nhất là 9. Kết quả in ra: 1 9.

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

long long getMinRec(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    return min(getMinRec(a, l, mid), getMinRec(a, mid + 1, r));
}

long long getMaxRec(const vector<long long> &a, int l, int r) {
    if (l == r) return a[l];
    int mid = l + (r - l) / 2;
    return max(getMaxRec(a, l, mid), getMaxRec(a, mid + 1, r));
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    cout << getMinRec(a, 0, n - 1) << " " << getMaxRec(a, 0, n - 1) << "\n";
    return 0;
}
```
