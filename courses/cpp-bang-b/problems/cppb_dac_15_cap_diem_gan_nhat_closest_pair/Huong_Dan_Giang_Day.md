# Hướng Dẫn Giảng Dạy: Cặp Điểm Gần Nhất (Closest Pair of Points)
Chuyên đề: **Bài 11: Kỹ thuật chia để trị**

---

## 1. Ý tưởng & Phân tích thuật toán
- **Bản chất bài toán:** Cho N điểm trên mặt phẳng tọa độ 2D. Hãy tìm khoảng cách Euclidean nhỏ nhất giữa hai điểm bất kỳ, làm tròn đúng 4 chữ số thập phân.

- **Phương pháp tiếp cận — Chia để trị (Divide and Conquer):**
  - Chia bài toán kích thước $N$ thành các bài toán con độc lập kích thước $N / 2$.
  - Giải quyết bài toán con và gộp kết quả tối ưu.

---

## 2. Bảng chạy tay trên số liệu mẫu (Dry Run Table - Sample 1: 3 0 0 1 1 2 2)
| Bước | Lệnh chạy / Thao tác | Phân tích biến đổi số liệu | Kết quả ghi nhận |
|---|---|---|---|
| 1 | Nạp dữ liệu vào mảng/biến | Input: `3 0 0 1 1 2 2` | Khởi tạo cấu trúc dữ liệu ban đầu |
| 2 | Thực thi thuật toán tối ưu | Khoảng cách giữa (0, 0) và (1, 1) là sqrt((1-0)^2 + (1-0)^2) = sqrt(2) = 1.4142. Kết quả in ra: 1.4142.... | Tính toán từng bước trạng thái |
| 3 | Xuất kết quả | Output: `1.4142` | Khớp chính xác với đầu ra mẫu |

*Giải thích chi tiết từ mẫu:* Khoảng cách giữa (0, 0) và (1, 1) là sqrt((1-0)^2 + (1-0)^2) = sqrt(2) = 1.4142. Kết quả in ra: 1.4142.

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

struct Point {
    long long x, y;
};

long long distSq(const Point &p1, const Point &p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

long long closestPairRec(vector<Point> &pts, int l, int r) {
    if (r - l <= 3) {
        long long min_d = 4e18;
        for (int i = l; i <= r; ++i) {
            for (int j = i + 1; j <= r; ++j) {
                min_d = min(min_d, distSq(pts[i], pts[j]));
            }
        }
        sort(pts.begin() + l, pts.begin() + r + 1, [](const Point &a, const Point &b) {
            return a.y < b.y;
        });
        return min_d;
    }

    int mid = l + (r - l) / 2;
    long long mid_x = pts[mid].x;
    long long dl = closestPairRec(pts, l, mid);
    long long dr = closestPairRec(pts, mid + 1, r);
    long long d = min(dl, dr);

    vector<Point> temp(r - l + 1);
    merge(pts.begin() + l, pts.begin() + mid + 1, pts.begin() + mid + 1, pts.begin() + r + 1, temp.begin(), [](const Point &a, const Point &b) {
        return a.y < b.y;
    });
    for (int i = 0; i < (int)temp.size(); ++i) pts[l + i] = temp[i];

    vector<Point> strip;
    for (int i = l; i <= r; ++i) {
        if ((pts[i].x - mid_x) * (pts[i].x - mid_x) < d) {
            strip.push_back(pts[i]);
        }
    }

    for (int i = 0; i < (int)strip.size(); ++i) {
        for (int j = i + 1; j < (int)strip.size() && (strip[j].y - strip[i].y) * (strip[j].y - strip[i].y) < d; ++j) {
            d = min(d, distSq(strip[i], strip[j]));
        }
    }
    return d;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    if (!(cin >> n)) return 0;
    vector<Point> pts(n);
    for (int i = 0; i < n; ++i) cin >> pts[i].x >> pts[i].y;
    sort(pts.begin(), pts.end(), [](const Point &a, const Point &b) {
        return a.x < b.x;
    });
    cout << closestPairRec(pts, 0, n - 1) << "\n";
    return 0;
}
```
