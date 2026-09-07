# Hướng Dẫn Giảng Dạy: Thuật Toán Sắp Xếp Trộn (Merge Sort)
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho mảng N số nguyên. Hãy tự cài đặt hoàn chỉnh thuật toán Merge Sort chia để trị để sắp xếp mảng theo thứ tự tăng dần.

- **Phương pháp tiếp cận — Chia để trị (Divide and Conquer):**
  - Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
  - Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 5 4 2 1 5 3)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `5 4 2 1 5 3` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Mảng sau khi sắp xếp tăng dần bằng Merge Sort là: 1 2 3 4 5.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1 2 3 4 5` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Mảng sau khi sắp xếp tăng dần bằng Merge Sort là: 1 2 3 4 5.

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

void merge(vector<long long> &a, vector<long long> &temp, int l, int mid, int r) {
    int i = l, j = mid + 1, k = l;
    while (i <= mid && j <= r) {
        if (a[i] <= a[j]) temp[k++] = a[i++];
        else temp[k++] = a[j++];
    }
    while (i <= mid) temp[k++] = a[i++];
    while (j <= r) temp[k++] = a[j++];
    for (int idx = l; idx <= r; ++idx) a[idx] = temp[idx];
}

void mergeSort(vector<long long> &a, vector<long long> &temp, int l, int r) {
    if (l >= r) return;
    int mid = l + (r - l) / 2;
    mergeSort(a, temp, l, mid);
    mergeSort(a, temp, mid + 1, r);
    merge(a, temp, l, mid, r);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<long long> a(n), temp(n);
    for (int i = 0; i < n; ++i) cin >> a[i];
    mergeSort(a, temp, 0, n - 1);
    for (int i = 0; i < n; ++i) cout << a[i] << (i + 1 == n ? "" : " ");
    cout << "\n";
    return 0;
}
```
